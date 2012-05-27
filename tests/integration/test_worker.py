import signal

#from nose.tools import eq_

from workerprocess.worker import BaseWorker, WorkerRunner


def create_callable_to_stop_worker_runner(worker_runner):
    "Creates a callable that will stop the worker_runner"

    def handler(signum, frame):
        "Handler to stop the worker"
        assert frame
        worker_runner._stop()

    return handler


class Worker(BaseWorker):
    "Test worker"

    def __init__(self):
        self.counter = 0

    def tick(self):
        self.counter += 1


def test_worker():
    worker_runner = WorkerRunner(Worker)
    handler = create_callable_to_stop_worker_runner(worker_runner)
    signal.signal(signal.SIGALRM, handler)
    signal.alarm(1)
    worker_runner.run()

    print worker_runner.instance.counter

