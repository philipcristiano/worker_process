from dingus import Dingus, DingusTestCase

from worker_process.worker import BaseWorker
import worker_process.worker as mod

class WhenStartingBaseWorker(DingusTestCase(BaseWorker)):

    def setup(self):
        super(WhenStartingBaseWorker, self).setup()

        BaseWorker.main()

    def should_create_event_worker_runner(self):
        assert mod.WorkerRunner.calls('()', mod.BaseWorker)

    def should_start_running(self):
        assert mod.WorkerRunner().calls('run')
