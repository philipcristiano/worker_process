from dingus import Dingus, DingusTestCase

from worker_process.worker import BaseEventWorker
import worker_process.worker as mod

class WhenStartingBaseEventWorker(DingusTestCase(BaseEventWorker)):

    def setup(self):
        super(WhenStartingBaseEventWorker, self).setup()

        BaseEventWorker.main()

    def should_create_event_worker_runner(self):
        assert mod.EventWorkerRunner.calls('()', mod.BaseEventWorker)

    def should_start_running(self):
        assert mod.EventWorkerRunner().calls('run')
