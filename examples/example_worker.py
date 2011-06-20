import time

from workerprocess import BaseWorker


class ExampleWorker(BaseWorker):

    def tick(self):
        print 'Tick!'
        time.sleep(1)


if __name__ == '__main__':
    ExampleWorker.main()
