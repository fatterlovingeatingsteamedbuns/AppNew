import os
import json
import pytest
from common.log_utils import LogUtils, LogLevel
from common.parameters_config import ParametersConfig
from common.base import retrive_data


if __name__ == "__main__":
    ###
    logUtils = LogUtils()
    logUtils.print(
        LogLevel.INFO, 'Use module type:{}'.format(ParametersConfig().module_type)
    )
    Modules_DIR = os.path.dirname(os.path.abspath(__file__))
    logUtils.print(LogLevel.INFO, 'Modules_DIR=' + Modules_DIR)

    allure_report_json = os.path.join(ParametersConfig.allure_report_dir, 'json')
    allure_report_html = os.path.join(ParametersConfig.allure_report_dir, 'html')
    if not os.path.exists(allure_report_json):
        os.makedirs(allure_report_json)
    if not os.path.exists(allure_report_html):
        os.makedirs(allure_report_html)

    dataset = retrive_data()
    logUtils.print(LogLevel.INFO, dataset)
    for data in dataset:
        pytest.main(
            [
                '-sv',
                # os.path.join(Modules_DIR, 'test_create_365.py'),
                # os.path.join(Modules_DIR, 'test_create_edge.py'),
                # os.path.join(Modules_DIR, 'test_create_notepad.py'),
                # os.path.join(Modules_DIR, 'test_create_orca.py'),
                # os.path.join(Modules_DIR, 'test_create_web_link.py'),
                # os.path.join(Modules_DIR, 'test_list_store.py'),
                os.path.join(Modules_DIR, 'test_uninstall_all.py'),
                '--data=' + json.dumps(data),
                '--reruns',
                '3',
                '--reruns-delay',
                '5',
                '--alluredir=' + allure_report_json,
            ]
        )
    os.system(
        'allure generate '
        + allure_report_json
        + ' -o '
        + allure_report_html
        + ' --clean'
    )
    os.system('allure open ' + allure_report_html)
