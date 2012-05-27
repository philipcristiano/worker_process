from mock import call, patch, MagicMock
from nose.tools import eq_

from workerprocess.worker import BaseWorker, WorkerRunner
import workerprocess.worker as mod


@patch('signal.signal')
def test_worker_runner_init(mock_signal):
    worker = MagicMock(BaseWorker)
    worker_runner = WorkerRunner(worker)

    mock_signal.assert_any_calls(mock_signal.SIGTERM, worker_runner._handle_sigterm)
    mock_signal.assert_any_calls(mock_signal.SIGHUP, worker_runner._handle_sighup)
    assert worker_runner._should_continue_running


@patch('signal.signal')
def test_worker_runner_run(mock_signal):
    worker = MagicMock(BaseWorker)
    worker_runner = WorkerRunner(worker)
    with patch.object(worker_runner, 'should_continue_running', side_effect=[True, False]) as scr:
        worker_runner.run()

    calls = [call(), call().startup(), call().tick(), call().shutdown()]
    worker.mock_calls
    eq_(worker.mock_calls, calls)
