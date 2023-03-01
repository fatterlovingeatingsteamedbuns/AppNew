import json
import allure
from common.base import get_test_result_metric
from page_operator.common_page_operator import CommonPageOperator
from common.log_utils import LogLevel, LogUtils
from common.helper_handle import HelperHandle
from common.parameters_config import ParametersConfig
from page_operator.create_web_link_app import (
    CreateWebLink
)
logger = LogUtils()
helperHandle = HelperHandle()

@allure.epic('App Regssion')
@allure.feature('Web link')
class TestCreateWebLink:
    def init_page_opr(self, env):
        helperHandle.set_helper(ParametersConfig().module_type)
        self.browser = helperHandle.get_browser()
        self.commonPageOperator = CommonPageOperator(self.browser, env)
        self.create_web_link = (
            CreateWebLink(self.browser)
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
        'step_02:Choose web link  app type.'
     )
    def step_02(self):
        logger.print(
            LogLevel.INFO,
            'Step_02:Choose web link app type.',
        )
        self.create_web_link.before_choose_app_type()
    

    @allure.step(
        'step_03:Modify Name,Description and App url.'
     )
    def step_03(self):
        logger.print(
            LogLevel.INFO,
            'Step_03:Modify Name,Description and App url.',
        )
        self.create_web_link.first_page_web_link()




    @allure.step(
        'step_04:Modify scopre tags----Do nothing.'
     )
    def step_04(self):
        logger.print(
            LogLevel.INFO,
            'Step_04:step_01:Modify scopre tags----Do nothing.',
        )
        self.create_web_link.second_page_web_link()


    @allure.step(
        'step_05:Add the group that you want install.'
     )
    def step_05(self):
        logger.print(
            LogLevel.INFO,
            'Step_05:Add the group that you want install.',
        )
        self.create_web_link.third_page_web_link()


    @allure.step(
        'step_06:Click create.'
     )
    def step_06(self):
        logger.print(
            LogLevel.INFO,
            'Step_06:Click create.',
        )
        self.create_web_link.forth_page_web_link()


    @allure.step(
        'step_07:Verify create web link  app successfully or not.'
     )
    def step_07(self):
        logger.print(
            LogLevel.INFO,
            'Step_07:Verify create web link app successfully or not.',
        )
        self.commonPageOperator.check_successfully()


        


    @allure.description('create web link app')
    def test_case05(self,data):
        logger.print(LogLevel.INFO, "Start【CPC Monitor filter works well】test")
        data = json.loads(data)
        env = data['env']
        test_result_metrics = get_test_result_metric(env)
        try:
            self.init_page_opr(env)
            self.step_01(data['username'], data['password'])
            self.step_02()
            self.step_03()
            self.step_04()
            self.step_05()
            self.step_06()
            self.step_07()
            assert True
        except Exception as err:
            logger.print(LogLevel.ERROR, 'Exception:{}'.format(err), err)
            assert False
        finally:
             helperHandle.quit_browser(self.browser)


if __name__ == '__main__':
    
    a=TestCreateWebLink()
    a.test_case05()
