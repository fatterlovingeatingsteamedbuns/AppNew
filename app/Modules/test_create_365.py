import json
import allure
from common.base import get_test_result_metric
from page_operator.common_page_operator import CommonPageOperator
from common.log_utils import LogLevel, LogUtils
from common.helper_handle import HelperHandle
from common.parameters_config import ParametersConfig
from page_operator.create_365_app import (
    Create365
)
logger = LogUtils()
helperHandle = HelperHandle()
# data = json.loads(data)
# env = data['env']
# test_result_metrics = get_test_result_metric(env)
# helperHandle.set_helper(ParametersConfig().module_type)
# browser = helperHandle.get_browser()
# commonPageOperator = CommonPageOperator(browser, env)
# create_365 = (
#             Create365(browser)
#         )


@allure.epic('App Regssion')
@allure.feature('365')          
class TestCreate365:
    def init_page_opr(self, env):
        helperHandle.set_helper(ParametersConfig().module_type)
        self.browser = helperHandle.get_browser()
        self.commonPageOperator = CommonPageOperator(self.browser, env)
        self.create_365 = (
            Create365(self.browser)
        )
        
    
    @allure.step(
        'step_01:Login MEM portal with admin account.'
     )
    def step_01(self,username, password):
        logger.print(
            LogLevel.INFO,
            'Step_01:Login MEM portal with admin account.',
        )
        self.commonPageOperator.login_MEM_portal(username, password)
        
    @allure.step(
        'step_02:Go to Apps -> Windows page.'
     )
    def step_02(self):
        logger.print(
            LogLevel.INFO,
            'Step_02:Go to Apps -> Windows page.',
        )
        self.commonPageOperator.goto_blade('Apps','Windows')


    @allure.step(
        'step_03:Choose 365 app type.'
     )
    def step_03(self):
        logger.print(
            LogLevel.INFO,
            'Step_03:Choose 365 app type.',
        )
        self.create_365.before_choose_app_type()
    

    @allure.step(
        'step_04:Modify app suite information----Suite Name.'
     )
    def step_04(self,typ):
        logger.print(
            LogLevel.INFO,
            'Step_04:Modify app suite information----Suite Name.',
        )
        self.create_365.first_page_365(typ)


    @allure.step(
        'step_05:Modify Config app suite----Default file format and Update channel.'
     )
    def step_05(self):
        logger.print(
            LogLevel.INFO,
            'Step_05:Modify Config app suite----Default file format and Update channel.',
        )
        self.create_365.second_page_365()


    @allure.step(
        'step_06:Modify scopre tags----Do nothing.'
     )
    def step_06(self):
        logger.print(
            LogLevel.INFO,
            'Step_06:step_01:Modify scopre tags----Do nothing.',
        )
        self.create_365.third_page_365()


    @allure.step(
        'step_07:Add the group that you want install.'
     )
    def step_07(self,typ):
        logger.print(
            LogLevel.INFO,
            'Step_07:Add the group that you want install.',
        )
        self.create_365.forth_page_365(typ)


    @allure.step(
        'step_08:Click create.'
     )
    def step_08(self):
        logger.print(
            LogLevel.INFO,
            'Step_08:Click create.',
        )
        self.create_365.fifth_page_365()


    @allure.step(
        'step_09:Verify create 365 app successfully or not.'
     )
    def step_09(self):
        logger.print(
            LogLevel.INFO,
            'Step_09:Verify create 365 app successfully or not.',
        )
        self.commonPageOperator.check_successfully()


        


    @allure.description('create 365 app')
    def test_case01(self,data):
        logger.print(LogLevel.INFO, "Start【CPC Monitor filter works well】test")
        data = json.loads(data)
        env = data['env']
        test_result_metrics = get_test_result_metric(env)
        try:
            self.init_page_opr(env)
            self.step_01(data['username'], data['password'])
            self.step_02()
            self.step_03()
            self.step_04('365')
            self.step_05()
            self.step_06()
            self.step_07('365')
            self.step_08()
            self.step_09()
            assert True
        except Exception as err:
            logger.print(LogLevel.ERROR, 'Exception:{}'.format(err), err)
            assert False
        finally:
             helperHandle.quit_browser(self.browser)


    @allure.description('create list 365 app')
    def test_case10(self,data):
        logger.print(LogLevel.INFO, "Start【CPC Monitor filter works well】test")
        data = json.loads(data)
        env = data['env']
        test_result_metrics = get_test_result_metric(env)
        try:
            self.init_page_opr(env)
            self.step_01(data['username'], data['password'])
            self.step_02()
            self.step_03()
            self.step_04('list 365')
            self.step_05()
            self.step_06()
            self.step_07('list 365')
            self.step_08()
            self.step_09()
            assert True
        except Exception as err:
            logger.print(LogLevel.ERROR, 'Exception:{}'.format(err), err)
            assert False
        finally:
             helperHandle.quit_browser(self.browser)


if __name__ == '__main__':
    
    a=TestCreate365()
    a.test_case01()
    a.test_case10()

