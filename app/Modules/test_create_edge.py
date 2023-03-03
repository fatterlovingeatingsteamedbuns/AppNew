import json
import allure
from common.base import get_test_result_metric
from page_operator.common_page_operator import CommonPageOperator
from common.log_utils import LogLevel, LogUtils
from common.helper_handle import HelperHandle
from common.parameters_config import ParametersConfig
# from page_operator.create_365_app import (
#     Create365
# )
from page_operator.create_edge_app import (
    CreateEdge
)
logger = LogUtils()
helperHandle = HelperHandle()

@allure.epic('App Regssion')
@allure.feature('Edge')
class TestCreateEdge:
    def init_page_opr(self, env):
        helperHandle.set_helper(ParametersConfig().module_type)
        self.browser = helperHandle.get_browser()
        self.commonPageOperator = CommonPageOperator(self.browser, env)
        self.create_edge = (
            CreateEdge(self.browser)
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
        'step_02:Choose edge app type.'
     )
    def step_02(self):
        logger.print(
            LogLevel.INFO,
            'Step_02:Choose edge app type.',
        )
        self.create_edge.before_choose_app_type()
    

    @allure.step(
        'step_03:Modify Name.'
     )
    def step_03(self,version):
        logger.print(
            LogLevel.INFO,
            'Step_03:Modify Name.',
        )
        self.create_edge.first_page_edge(version)


    @allure.step(
        'step_04:Select the appropriate channel.'
     )
    def step_04(self,version):
        logger.print(
            LogLevel.INFO,
            'Step_04:Select the appropriate channel.',
        )
        self.create_edge.second_page_edge(version)


    @allure.step(
        'step_05:Modify scopre tags----Do nothing.'
     )
    def step_05(self):
        logger.print(
            LogLevel.INFO,
            'Step_05:Modify scopre tags----Do nothing.',
        )
        self.create_edge.third_page_edge()

    @allure.step(
        'step_06:Add the group that you want install.'
     )
    def step_06(self,version):
        logger.print(
            LogLevel.INFO,
            'Step_06:Add the group that you want install.',
        )
        self.create_edge.forth_page_edge(version)


    @allure.step(
        'step_07:Click create.'
     )
    def step_07(self):
        logger.print(
            LogLevel.INFO,
            'Step_07:Click create.',
        )
        self.create_edge.fifth_page_edge()


    @allure.step(
        'step_08:Verify create edge app successfully or not.'
     )
    def step_08(self):
        logger.print(
            LogLevel.INFO,
            'Step_08:Verify create edge app successfully or not.',
        )
        self.commonPageOperator.check_successfully()



    @allure.description('create stable edge app')
    def test_case02(self,data):
        logger.print(LogLevel.INFO, "Start【CPC Monitor filter works well】test")
        data = json.loads(data)
        env = data['env']
        test_result_metrics = get_test_result_metric(env)
        try:
            self.init_page_opr(env)
            self.step_01(data['username'], data['password'])
            self.step_02()
            self.step_03('Stable')
            self.step_04('Stable')
            #self.step_05()
            self.step_06('not list')
            self.step_07()
            self.step_08()
            assert True
        except Exception as err:
            logger.print(LogLevel.ERROR, 'Exception:{}'.format(err), err)
            assert False
        finally:
             helperHandle.quit_browser(self.browser)

    @allure.description('create beta edge app')
    def test_case03(self,data):
        logger.print(LogLevel.INFO, "Start【CPC Monitor filter works well】test")
        data = json.loads(data)
        env = data['env']
        test_result_metrics = get_test_result_metric(env)
        try:
            self.init_page_opr(env)
            self.step_01(data['username'], data['password'])
            self.step_02()
            self.step_03('Beta')
            self.step_04('Beta')
            #self.step_05()
            self.step_06('not list')
            self.step_07()
            self.step_08()
            assert True
        except Exception as err:
            logger.print(LogLevel.ERROR, 'Exception:{}'.format(err), err)
            assert False
        finally:
             helperHandle.quit_browser(self.browser)

    @allure.description('create dev edge app')
    def test_case04(self,data):
        logger.print(LogLevel.INFO, "Start【CPC Monitor filter works well】test")
        data = json.loads(data)
        env = data['env']
        test_result_metrics = get_test_result_metric(env)
        try:
            self.init_page_opr(env)
            self.step_01(data['username'], data['password'])
            self.step_02()
            self.step_03('Dev')
            self.step_04('Dev')
            #self.step_05()
            self.step_06('not list')
            self.step_07()
            self.step_08()
            assert True
        except Exception as err:
            logger.print(LogLevel.ERROR, 'Exception:{}'.format(err), err)
            assert False
        finally:
             helperHandle.quit_browser(self.browser)

    @allure.description('create list edge app')
    def test_case11(self,data):
        logger.print(LogLevel.INFO, "Start【CPC Monitor filter works well】test")
        data = json.loads(data)
        env = data['env']
        test_result_metrics = get_test_result_metric(env)
        try:
            self.init_page_opr(env)
            self.step_01(data['username'], data['password'])
            self.step_02()
            self.step_03('list Stable')
            self.step_04('list Stable')
            #self.step_05()
            self.step_06('list')
            self.step_07()
            self.step_08()
            assert True
        except Exception as err:
            logger.print(LogLevel.ERROR, 'Exception:{}'.format(err), err)
            assert False
        finally:
             helperHandle.quit_browser(self.browser)





if __name__ == '__main__':
    
    a=TestCreateEdge()
    a.test_case02()
    a.test_case03()
    a.test_case04()