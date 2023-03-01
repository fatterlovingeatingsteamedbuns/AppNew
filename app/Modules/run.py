import os, json
from common.base import retrive_data
from common.log_utils import LogUtils, LogLevel
from common.parameters_config import ParametersConfig
import pytest


if __name__ == "__main__":
    logUtils = LogUtils()
    logUtils.print(LogLevel.INFO, 'Use module type:' + ParametersConfig().module_type)
    Modules_DIR = os.path.dirname(os.path.abspath(__file__))
    logUtils.print(LogLevel.INFO, 'Modules_DIR=' + Modules_DIR)

    dataset = retrive_data()
    logUtils.print(LogLevel.INFO, dataset)
    for data in dataset:
        _data = {
            'username': data['username'],
            'password': data['password'],
            'env': data['env'],
        }
        pytest.main(
            [
                '-sv',
                os.path.join(Modules_DIR, ''),
                '--data=' + json.dumps(_data),
                '--reruns',
                '3',
                '--reruns-delay',
                '5',
            ]
        )
