import os
import sys
sys.path.append(os.path.split(os.path.abspath(os.path.dirname(__file__)))[0])
# from nautcore.telemetry.logging.logger import Logger
from common.parameters_config import ParametersConfig


class LogLevel:
    INFO = "info"
    ERROR = "error"
    DEBUG = "debug"


class LogUtils:
    def print(self, log_level, msg, e=None):
        if ParametersConfig.is_local == True:
            print(msg)
        else:
            workflow_id = os.environ.get('WORKFLOW_ID')
            # nautlogger = Logger(workflow_id=workflow_id)
            # if log_level == LogLevel.INFO:
            #     nautlogger.log_info(msg)
            # elif log_level == LogLevel.ERROR:
            #     nautlogger.log_error(msg, e)
            # elif log_level == LogLevel.DEBUG:
            #     nautlogger.log_debug(msg)
            # else:
            #     nautlogger.log_info(msg)


if __name__ == "__main__":
    logUtils = LogUtils()
    logUtils.print(LogLevel.INFO, 'Hello')
