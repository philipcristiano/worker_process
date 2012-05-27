"""
Worker
======
Classes that a worker process should use.
"""
import signal
import time

__all__ = ['BaseWorker']

class BaseWorker(object):
    """Base class for all workers to extend.
    """

    max_ticks_per_second = 0
    """If greater than zero this worker will run at most this mane ticks"""

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
        """Called before the loop starts."""
        pass

    def shutdown(self):
        """Called after the loop stops."""
        pass

    def sighup(self):
        """Called when a SIGHUP is sent to the worker process."""
        pass


class WorkerRunner(object):
    """Run an instance of BaseWorker"""

    def __init__(self, cls):
        self.instance = cls()
        self._should_continue_running = True
        self._last_run_time = time.time()
        signal.signal(signal.SIGTERM, self._handle_sigterm)
        signal.signal(signal.SIGHUP, self._handle_sighup)

    def run(self):
        """Start the worker"""
        self.instance.startup()
        while self.should_continue_running():
            self._wait_for_next_time_to_run()
            self.instance.tick()
        self.instance.shutdown()

    def should_continue_running(self):
        "Predicate to check if this worker_runner should continue running"
        return self._should_continue_running

    def _wait_for_next_time_to_run(self):
        "Waits the amount of time required for the next tick"
        if not self._rate_limiting_enabled():
            return
        now = time.time()
        time_between_ticks = 1.0 / self.instance.max_ticks_per_second
        next_run_time = self._last_run_time + time_between_ticks
        if now < next_run_time:
            time_to_sleep = next_run_time - now
            time.sleep(time_to_sleep)

        self._last_run_time = next_run_time

    def _rate_limiting_enabled(self):
        "Should this instance try to rate limit?"
        return self.instance.max_ticks_per_second > 0

    def _stop(self):
        """Trigger the event loop to stop"""
        self._should_continue_running = False

    def _handle_sigterm(self, signum, frame):
        """Stops the worker when terminated"""
        self._stop()

    def _handle_sighup(self, signum, frame):
        """Calls the worker sighup"""
        self.instance.sighup()

