import time

from workerprocess import BaseWorker


class ExampleWorker(BaseWorker):

    def startup(self):
        print 'Starting...'

    def tick(self):
        print 'Tick!'
        time.sleep(1)

    def shutdown(self):
        print 'Shutting down.'

    def sighup(self):
        print 'Hanging up.'


if __name__ == '__main__':
    ExampleWorker.main()
