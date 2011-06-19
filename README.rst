Worker Process
==============

This package provides a wrapper to create standalone worker processes.

Example Worker
======================

Workers are created by extending the BaseWorker class and implementing a tick
method to execute then calling .main() on the class. This will start an
infite loop calling that function.

The worker can be stopped gracefully by sending a SIGTERM to the process.

>>> import time
...
... from worker_process import BaseWorker
...
...
... class ExampleWorker(BaseWorker):
...
...     def tick(self):
...         print 'Tick!'
...         time.sleep(1)
...
...
... if __name__ == '__main__':
...     ExampleWorker.main()
