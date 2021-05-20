# test_for_Firefox_and_Chrome

use selenium and pytest

Проба пера для тестирования задач на браузерах Firefox и Chrome


pytest -s -v --browser_name=chrome test_parser.py

pytest -s -v --browser_name=firefox test_parser.py


For test_rerun.py:

pytest -v --tb=line --reruns 1 --browser_name=chrome test_rerun.py
