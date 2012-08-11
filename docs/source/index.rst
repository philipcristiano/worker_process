.. workerprocess documentation master file, created by
   sphinx-quickstart on Sat Aug 11 13:03:07 2012.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to workerprocess's documentation!
=========================================

WorkerProcess is a library that makes your day simpler by providing an easy base class for background workers.

.. literalinclude:: ../../examples/example_worker.py

The `tick` method will be called in an infinite loop. WorkerProcess will handle
`SIGTERM` and `SIGHUP`. You can override the default `SIGHUP` behavior (of
nothing) by adding the method `sighup`. `startup` and `shutdown` methods are
available as well that will run before and after the loop.

WorkerProcess can also limit the number of loops per second with the
`max_ticks_per_second` variable. This supports floating point numbers as well
so `.1` will run once every 10 seconds. This is mainly used for keeping the
worker from going into a busy loop.

A full example:

.. literalinclude:: ../../examples/full_worker.py


.. toctree::
   :maxdepth: 2



Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

