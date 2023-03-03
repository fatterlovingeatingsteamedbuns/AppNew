import json
import allure
from common.base import get_test_result_metric
from page_operator.common_page_operator import CommonPageOperator
from common.log_utils import LogLevel, LogUtils
from common.helper_handle import HelperHandle
from common.parameters_config import ParametersConfig
from page_operator.list_store import (
    ListStore
)
logger = LogUtils()
helperHandle = HelperHandle()
@allure.epic('App Regssion')
@allure.feature('list store')
class TestCreateStore():

    def init_page_opr(self, env):
        helperHandle.set_helper(ParametersConfig().module_type)
        self.browser = helperHandle.get_browser()
        self.commonPageOperator = CommonPageOperator(self.browser, env)
        self.liststore = (
            ListStore(self.browser)
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
        'step_02:Choose 365 app type.'
     )
    def step_02(self):
        logger.print(
            LogLevel.INFO,'step_02:Choose 365 app type.')
        self.liststore.before_choose_app_type()
        
    
    @allure.step(
        'step_03:Modify Name.'
     )
    def step_03(self):
        logger.print(
            LogLevel.INFO,'step_03:Modify Name.')
        self.liststore.first_page_list_store()
    

    @allure.step(
        'step_04:Modify Scopes tags----Do nothing.'
     )
    def step_04(self):
        logger.print(
            LogLevel.INFO,'step_04:Modify Scopes tags----Do nothing.')
        self.liststore.second_page_list_store()


    @allure.step(
        'step_05:Add the group that you want install.'
     )
    def step_05(self):
        logger.print(
            LogLevel.INFO,'step_05:Add the group that you want install.')
        self.liststore.third_page_list_store()


    @allure.step(
        'step_06:Click create.'
     )
    def step_06(self):
        logger.print(
            LogLevel.INFO,'step_06:Click create.')
        self.liststore.forth_page_list_store()


    @allure.step(
        'step_06:Click create.'
     )
    def step_06(self):
        logger.print(
            LogLevel.INFO,'step_06:Click create.')
        self.liststore.forth_page_list_store()
        self.commonPageOperator.check_successfully()


    @allure.description('create list store app')
    def test_case09(self,data):
        logger.print(LogLevel.INFO, "Start【CPC Monitor filter works well】test")
        data = json.loads(data)
        env = data['env']
        test_result_metrics = get_test_result_metric(env)
        try:
            self.init_page_opr(env)
            self.step_01(data['username'], data['password'])
            self.step_02()
            self.step_03()
            #self.step_04()
            self.step_05()
            self.step_06()
            assert True
        except Exception as err:
            logger.print(LogLevel.ERROR, 'Exception:{}'.format(err), err)
            assert False
        finally:
             helperHandle.quit_browser(self.browser)



if __name__ == '__main__':
    testcreatenotepad=TestCreateStore()
    testcreatenotepad.test_case09()