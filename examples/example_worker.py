import time

from worker_process import BaseWorker


class ExampleWorker(BaseWorker):

    def run_once(self):
        print 'Tick!'
        time.sleep(1)


if __name__ == '__main__':

    ExampleWorker.main()
