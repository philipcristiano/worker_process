from worker_process import BasePollWorker


class ExampleWorker(BasePollWorker):

    def run_once(self):
        print 'Tick!'

        return False


if __name__ == '__main__':

    ExampleWorker.main()
