Worker Process
==============

This package provides a wrapper to create standalone worker processes.

Example Worker
======================

Workers are created by extending the BaseWorker class and implementing a tick
method to execute then calling .main() on the class. This will start an
infinite loop calling that function.

The worker can be rate limited with `max_ticks_per_second`.

The worker can be stopped gracefully by sending a SIGTERM to the process.

    >>> import time
    ...
    ... from workerprocess import BaseWorker
    ...
    ...
    ... class ExampleWorker(BaseWorker):
    ...
    ...     max_ticks_per_second = 10
    ...
    ...     def tick(self):
    ...         print 'Tick!'
    ...         time.sleep(1)
    ...
    ... ExampleWorker.main()
