"""
Worker
======
Classes that a worker process should use.
"""
import signal

__all__ = ['BaseWorker']

class BaseWorker(object):
    """Base class for all workers to extend.
    """

    @classmethod
    def main(cls):
        """Entry point to use for a worker. This in general should not be
        overridden.
        """
        runner = WorkerRunner(cls)
        runner.run()

    def tick(self):
        """Run for one unit of work."""
        raise NotImplementedError('Subclasses must define tick.')

    def startup(self):
        pass

    def shutdown(self):
        pass


class WorkerRunner(object):

    def __init__(self, cls):
        self.instance = cls()
        self._should_continue_running = True
        signal.signal(signal.SIGTERM, self._handle_sigterm)

    def run(self):
        """Start the worker"""
        self.instance.startup()
        while self._should_continue_running:
            self.instance.tick()
        self.instance.shutdown()

    def _stop(self):
        """Trigger the event loop to stop"""
        self._should_continue_running = False

    def _handle_sigterm(self, signum, frame):
        """Stops the worker when terminated"""
        self._stop()
