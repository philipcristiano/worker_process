from workerprocess import BaseWorker


class ExampleWorker(BaseWorker):

    max_ticks_per_second = 1

    def startup(self):
        print 'Starting...'

    def tick(self):
        print 'Tick!'

    def shutdown(self):
        print 'Shutting down.'

    def sighup(self):
        print 'Hanging up.'


if __name__ == '__main__':
    ExampleWorker.main()
