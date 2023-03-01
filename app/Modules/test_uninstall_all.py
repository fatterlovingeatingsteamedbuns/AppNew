import json
import allure
from common.base import get_test_result_metric
from page_operator.common_page_operator import CommonPageOperator
from common.log_utils import LogLevel, LogUtils
from common.helper_handle import HelperHandle
from common.parameters_config import ParametersConfig
from page_operator.uninstall import (
    Uninstall_all
)
logger = LogUtils()
helperHandle = HelperHandle()
@allure.epic('App Regssion')
@allure.feature('Uninstall')
class TestUninstall():

    def init_page_opr(self, env):
        helperHandle.set_helper(ParametersConfig().module_type)
        self.browser = helperHandle.get_browser()
        self.commonPageOperator = CommonPageOperator(self.browser, env)
        self.uninstallall = (
            Uninstall_all(self.browser)
        )


    @allure.step(
        'step_01:Login MEM portal with admin account,go to Apps -> Windows page.'
     )
    def step_01(self,username, password):
        logger.print(
            LogLevel.INFO,
            'Step_01:Login MEM portal with admin account,go to Apps -> Windows page.',
        )
        self.commonPageOperator.login_MEM_portal(username, password)
        self.commonPageOperator.goto_blade('Apps','Windows')


    @allure.step(
        'step_02:Uninstall.'
     )
    def step_02(self):
        logger.print(
            LogLevel.INFO,'step_02:Uninstall.')
        self.uninstallall.uninstall()




    @allure.description('Uninstall all')
    def test_case14(self,data):
        logger.print(LogLevel.INFO, "Start【CPC Monitor filter works well】test")
        data = json.loads(data)
        env = data['env']
        test_result_metrics = get_test_result_metric(env)
        try:
            self.init_page_opr(env)
            self.step_01(data['username'], data['password'])
            self.step_02()
            assert True
        except Exception as err:
            logger.print(LogLevel.ERROR, 'Exception:{}'.format(err), err)
            assert False
        finally:
             helperHandle.quit_browser(self.browser)