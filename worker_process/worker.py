"""
Worker
======
Classes that a worker process should use.
"""

import signal
import socket
import time


class BaseWorker(object):

    def startup(self):
        pass

    def shutdown(self):
        pass


class BaseEventWorker(BaseWorker):
    """Base class for all workers to extend.
    """

    @classmethod
    def main(cls):
        """Entry point to use for a worker. This in general should not be
        overridden.
        """
        runner = EventWorkerRunner(cls)
        runner.run()


class BasePollingWorker(BaseWorker):
    """Base class for polling-based workers to inherit from."""

    @classmethod
    def main(cls):
        """Entry point to use for a worker. This in general should not be
        overridden.

        """
        runner = PollingWorkerRunner(cls)
        runner.run()


class WorkerRunner(object):

    def __init__(self, cls):
        self.instance = cls()
        self._should_continue_running = True
        signal.signal(signal.SIGTERM, self._handle_sigterm)

    def run(self):  # pragma: no cover
        """Start the worker"""
        #log.info('Starting worker loop...')

        self.instance.startup()
        while self._should_continue_running:
            self.tick()
        self.instance.shutdown()

        #log.info('Stopping worker loop.')

        #self._connection.close()

    def _stop(self):
        """Trigger the event loop to stop"""
        #log.info('Stopping worker loop...')
        self._should_continue_running = False

    def _handle_sigterm(self, signum, frame):
        """Stops the worker when terminated"""
        #log.info('Received SIGTERM')
        self._stop()

    def tick(self):
        """Run for one unit of work.
        """
        raise NotImplementedError('Subclasses must define tick.')


class EventWorkerRunner(WorkerRunner):
    """Async worker class that registers callbacks and drains events."""

    def __init__(self, klass):
        WorkerRunner.__init__(self, klass)
        self.queue_name = klass.__module__
        self._subscribe(klass)

        msg = 'event: {0} queue_name: {1} callback: {2}'.\
              format(klass.event_type, klass.__module__,
                     self.instance.process_event)
        #log.info('Setting up AMQP connection: {0}'.format(msg))

    def _subscribe(self, klass):
        """Subscribes to the event queue"""
        if not isinstance(klass.event_type, list):
            klass.event_type = [klass.event_type]

        for event_type in klass.event_type:
            self._connection.events.subscribe(
                event_type,
                klass.__module__,
                self.instance.process_event
            )

    def tick(self):
        """Run for one unit of work

        Block waiting for a single event with a timeout of one second.
        """
        try:
            self._connection.events.drain_events(timeout=1)
        except socket.timeout:
            return False
        return True


class PollingWorkerRunner(WorkerRunner):
    """A runner for running a job periodically.
    """

    def tick(self):
        """Run for one unit of work

        This runs the worker for one cycle.  Then the runner sleeps
        for 5 seconds.  If the worker returns `True` or someone has
        called `stop` on this runner it will return immediately
        without sleeping.
        """
        dont_wait = self.instance.run_once()
        if self._should_continue_running and not dont_wait:
            time.sleep(5)
