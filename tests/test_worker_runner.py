from dingus import Dingus, DingusTestCase

from worker_process.worker import WorkerRunner
import worker_process.worker as mod


class BaseWorkerRunner(DingusTestCase(WorkerRunner)):

    def setup(self):
        super(BaseWorkerRunner, self).setup()
        self.worker_class = Dingus('worker')
        self.worker = self.worker_class()

        self.runner = WorkerRunner(self.worker_class)

class WhenCreatingWorkerRunner(BaseWorkerRunner):

    def setup(self):
        BaseWorkerRunner.setup(self)

    def should_default_to_continue_running(self):
        assert self.runner._should_continue_running == True

    def should_register_sigterm_handler(self):
        assert mod.signal.calls('signal', mod.signal.SIGTERM, self.runner._handle_sigterm)


class WhenReceivingSigTerm(BaseWorkerRunner):

    def setup(self):
        BaseWorkerRunner.setup(self)
        self.signum = Dingus('signum')
        self.frame = Dingus('frame')

        self.runner._handle_sigterm(self.signum, self.frame)

    def should_no_longer_continue_running(self):
        assert self.runner._should_continue_running == False


class WhenRunning(BaseWorkerRunner):

    def setup(self):
        BaseWorkerRunner.setup(self)
        self.runner.tick = Dingus('tick')
        self.runner._should_continue_running = False

        self.runner.run()

    def should_startup_worker(self):
        assert self.worker.calls('startup')

    def should_shutdown_worker(self):
        assert self.worker.calls('shutdown')
