import json
import allure
from common.base import get_test_result_metric
from page_operator.common_page_operator import CommonPageOperator
from common.log_utils import LogLevel, LogUtils
from common.helper_handle import HelperHandle
from common.parameters_config import ParametersConfig
from page_operator.create_orca import (
    CreateOrca
)
logger = LogUtils()
helperHandle = HelperHandle()

@allure.epic('App Regssion')
@allure.feature('orca')
class TestCreateOrca:
    def init_page_opr(self, env):
        helperHandle.set_helper(ParametersConfig().module_type)
        self.browser = helperHandle.get_browser()
        self.commonPageOperator = CommonPageOperator(self.browser, env)
        self.create_orca = (
            CreateOrca(self.browser)
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
        'step_02:Choose orca app type.'
     )
    def step_02(self):
        logger.print(
            LogLevel.INFO,
            'step_02:Choose orca app type.',
        )
        #self.basePage.init_driver()
        self.create_orca.before_choose_app_type()
        
    
    @allure.step(
        'step_03:Modify Name Description Publisher.'
     )
    def step_03(self,typ):
        logger.print(
            LogLevel.INFO,
            'step_03:Modify Name Description Publisher.',
        )
        self.create_orca.first_page_orca(typ)
    

    @allure.step(
        'step_04:Modify Program----Do nothing.'
     )
    def step_04(self):
        logger.print(
            LogLevel.INFO,
            'step_04:Modify Program----Do nothing.',
        )
        self.create_orca.second_page_orca()


    @allure.step(
        'step_05:Modify system orchitecture and operating system.'
     )
    def step_05(self):
        logger.print(
            LogLevel.INFO,
            'step_05:Modify system orchitecture and operating system.',
        )
        self.create_orca.third_page_orca()


    @allure.step(
        'step_06:Modify Detection rules.'
     )
    def step_06(self):
        logger.print(
            LogLevel.INFO,
            'step_06:Modify Detection rules.',
        )
        self.create_orca.forth_page_orca()


    @allure.step(
        'step_07:Modify Dependencies----Do nothing.'
     )
    def step_07(self):
        logger.print(
            LogLevel.INFO,
            'step_07:Modify Dependencies----Do nothing.',
        )
        self.create_orca.fifth_page_orca()
    

    @allure.step(
        'step_08:Modify Superdence----Do nothing.'
     )
    def step_08(self):
        logger.print(
            LogLevel.INFO,
            'step_08:Modify Superdence----Do nothing.',
        )
        self.create_orca.sixth_page_orca()


    @allure.step(
        'step_09:Modify Scopes tags----Do nothing.'
     )
    def step_09(self):
        logger.print(
            LogLevel.INFO,
            'step_09:Modify Scopes tags----Do nothing.',
        )
        self.create_orca.seventh_page_orca()


    @allure.step(
        'step_10:Add the group that you want install.'
     )
    def step_10(self,typ):
        logger.print(
            LogLevel.INFO,
            'step_10:Add the group that you want install.',
        )
        self.create_orca.eighth_page_orca(typ)


    @allure.step(
        'step_11:Click create.'
     )
    def step_11(self):
        logger.print(
            LogLevel.INFO,
            'step_11:Click create.',
        )
        self.create_orca.ninth_page_orca()
        self.commonPageOperator.check_successfully()

    @allure.description('create orca app')
    def test_case08(self,data):
        logger.print(LogLevel.INFO, "Start【CPC Monitor filter works well】test")
        data = json.loads(data)
        env = data['env']
        test_result_metrics = get_test_result_metric(env)
        try:
            self.init_page_opr(env)
            self.step_01(data['username'], data['password'])
            self.step_02()
            self.step_03('orca')
            self.step_04()
            self.step_05()
            self.step_06()
            self.step_07()
            self.step_08()
            #self.step_09()
            self.step_10('orca')
            self.step_11()
            assert True
        except Exception as err:
            logger.print(LogLevel.ERROR, 'Exception:{}'.format(err), err)
            assert False
        finally:
            helperHandle.quit_browser(self.browser) 

    @allure.description('create list orca app')
    def test_case13(self,data):
        logger.print(LogLevel.INFO, "Start【CPC Monitor filter works well】test")
        data = json.loads(data)
        env = data['env']
        test_result_metrics = get_test_result_metric(env)
        try:
            self.init_page_opr(env)
            self.step_01(data['username'], data['password'])
            self.step_02()
            self.step_03('list orca')
            self.step_04()
            self.step_05()
            self.step_06()
            self.step_07()
            self.step_08()
            #self.step_09()
            self.step_10('list orca')
            self.step_11()
            assert True
        except Exception as err:
            logger.print(LogLevel.ERROR, 'Exception:{}'.format(err), err)
            assert False
        finally:
            helperHandle.quit_browser(self.browser) 






if __name__ == '__main__':
    testcreatenotepad=TestCreateOrca()
    testcreatenotepad.test_case08()
    testcreatenotepad.test_case13()