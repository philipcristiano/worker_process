Worker Process
==============

This package provides a wrapper to create standalone worker processes.

Types of Workers
================

To create a worker you inherit from a BaseWorker class and implement a single
function to complete the work and optionally startup and shutdown functions.

Example Polling Worker
======================

Polling workers will execute the work function between 5 second waits. If the
function returns True it will execute again immediately.

    from worker_process import BasePollWorker

    class ExampleWorker(BasePollWorker):

        def run_once(self):
            print 'Tick!'

            return False

