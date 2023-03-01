import json
import allure
from common.base import get_test_result_metric
from page_operator.common_page_operator import CommonPageOperator
from common.log_utils import LogLevel, LogUtils
from common.helper_handle import HelperHandle
from common.parameters_config import ParametersConfig
from page_operator.create_notepad import (
    CreateNotepad
)
logger = LogUtils()
helperHandle = HelperHandle()

@allure.epic('App Regssion')
@allure.feature('Notepad')
class TestCreatenotepad:
    def init_page_opr(self, env):
        helperHandle.set_helper(ParametersConfig().module_type)
        self.browser = helperHandle.get_browser()
        self.commonPageOperator = CommonPageOperator(self.browser, env)
        self.createnotepad = (
            CreateNotepad(self.browser)
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
        'step_02:Choose notepad or spartan app type.'
     )
    def step_02(self):
        logger.print(
            LogLevel.INFO,('step_02:Choose notepad or spartan app type.'))
        #self.basePage.init_driver()
        self.createnotepad.before_choose_app_type()
        
   
    @allure.step(
        'step_03:Modify Name Description.'
        )
    def step_03(self,typ):
        logger.print(
            LogLevel.INFO,('step_03:Modify Name Description.'))
        self.createnotepad.first_page_notepad(typ)
        

    @allure.step(
        'step_04:Modify scopre tags----Do nothing.'
     )
    def step_04(self):
        logger.print(
            LogLevel.INFO,('step_04:Modify scopre tags----Do nothing.'))
        self.createnotepad.second_page_notepad()


    @allure.step(
        'step_05:Add the group that you want install.'
     )
    def step_05(self,typ):
        logger.print(
            LogLevel.INFO,('step_05:Add the group that you want install.'))
        self.createnotepad.third_page_notepad(typ)


    @allure.step(
        'step_06:Click create.'
     )
    def step_06(self):
        logger.print(
            LogLevel.INFO,('step_06:Click create.'))
        self.createnotepad.forth_page_notepad()

    @allure.step(
            'step_07:Verify create notepad/spartan app successfully or not.'
        )
    def step_07(self):
        logger.print(
            LogLevel.INFO,
            'Step_07:Verify create notepad/spartan app successfully or not.',
        )
        self.commonPageOperator.check_successfully()



    @allure.description('create notepad app')
    def test_case06(self,data):
        logger.print(LogLevel.INFO, "Start【CPC Monitor filter works well】test")
        data = json.loads(data)
        env = data['env']
        test_result_metrics = get_test_result_metric(env)
        try:
            self.init_page_opr(env)
            self.step_01(data['username'], data['password'])
            self.step_02()
            self.step_03('notepad')
            self.step_04()
            self.step_05('notepad')
            self.step_06()
            self.step_07()
            assert True
        except Exception as err:
            logger.print(LogLevel.ERROR, 'Exception:{}'.format(err), err)
            assert False
        finally:
            helperHandle.quit_browser(self.browser)

    @allure.description('create spartan app')
    def test_case07(self,data):
        logger.print(LogLevel.INFO, "Start【CPC Monitor filter works well】test")
        data = json.loads(data)
        env = data['env']
        test_result_metrics = get_test_result_metric(env)
        try:
            self.init_page_opr(env)
            self.step_01(data['username'], data['password'])
            self.step_02()
            self.step_03('spartan')
            self.step_04()
            self.step_05('spartan')
            self.step_06()
            self.step_07()
            assert True
        except Exception as err:
            logger.print(LogLevel.ERROR, 'Exception:{}'.format(err), err)
            assert False
        finally:
            helperHandle.quit_browser(self.browser)

    @allure.description('create list notepad app')
    def test_case12(self,data):
        logger.print(LogLevel.INFO, "Start【CPC Monitor filter works well】test")
        data = json.loads(data)
        env = data['env']
        test_result_metrics = get_test_result_metric(env)
        try:
            self.init_page_opr(env)
            self.step_01(data['username'], data['password'])
            self.step_02()
            self.step_03('list notepad')
            self.step_04()
            self.step_05('list notepad')
            self.step_06()
            self.step_07()
            assert True
        except Exception as err:
            logger.print(LogLevel.ERROR, 'Exception:{}'.format(err), err)
            assert False
        finally:
            helperHandle.quit_browser(self.browser)









if __name__ == '__main__':
    testcreatenotepad=TestCreatenotepad()
    testcreatenotepad.test_case06()
    testcreatenotepad.test_case07()
    

