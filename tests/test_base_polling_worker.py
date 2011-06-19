from dingus import Dingus, DingusTestCase

from worker_process.worker import BasePollingWorker
import worker_process.worker as mod


class WhenStartingBasePollingWorker(DingusTestCase(BasePollingWorker)):

    def setup(self):
        super(WhenStartingBasePollingWorker, self).setup()

        BasePollingWorker.main()

    def should_create_polling_worker_runner(self):
        assert mod.PollingWorkerRunner.calls('()', mod.BasePollingWorker)

    def should_start_running(self):
        assert mod.PollingWorkerRunner().calls('run')

