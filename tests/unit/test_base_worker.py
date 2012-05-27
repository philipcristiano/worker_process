from mock import patch, MagicMock

from workerprocess.worker import BaseWorker
import workerprocess.worker as mod


@patch('workerprocess.worker.WorkerRunner')
def test_starting_worker(mock_worker_runner):
    BaseWorker.main()

    mock_worker_runner.assert_called_with(BaseWorker)
    mock_worker_runner().run.assert_called_with()
