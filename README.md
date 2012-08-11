Worker Process
==============

This package provides a wrapper to create standalone worker processes.

[![Build Status](https://secure.travis-ci.org/philipcristiano/worker_process.png?branch=master)](http://travis-ci.org/philipcristiano/worker_process)

There is more [documentation](http://workerprocess.readthedocs.org/en/latest/) at ReadTheDocs.

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

A `sighup` method on the function will be called if the process receives a
SIGHUP

Running the Worker
==================
The easiest way to be able to run the worker is by adding a console\_script
entry point in your setup.py:

    entry_points="""
    [console_scripts]
    example_worker_process = yourpackage.yourmodule:ExampleWorker.main
    """,

After installing your package you will be able to run the command
`example_worker_process` from the command line.
