from copy import deepcopy
from time import sleep
import os
import sys
sys.path.append(os.path.split(os.path.abspath(os.path.dirname(__file__)))[0])
from common.helper_handle import HelperHandle
from common.log_utils import LogLevel, LogUtils
from common.parameters_config import ParametersConfig
from page_operator.common_page_operator import CommonPageOperator
# from common_page_operator import CommonPageOperator
from common.times import dt_strftime
import time
import json
import random
from page_config.create_365 import (
    Create_365,
)
from page_config.same import (
    Same,
)
from page_config.create_edge import (
    Create_edge,
)
helperHandle = HelperHandle()
logger = LogUtils()
module_type = ParametersConfig().module_type

class CreateEdge:

    def __init__(self, browser):
        self.browser = browser
        self.conf_365= deepcopy(Create_365)
        self.conf_edge= deepcopy(Create_edge)
        self.conf_same = deepcopy(Same)

    def before_choose_app_type(self):
        page_driver = (
            self.browser.pages[0] if module_type == 'playwright' else self.browser
        )
        helperHandle.click(page_driver,self.conf_same['Click Add'])
        helperHandle.click(page_driver,self.conf_same['Click Down'])
        helperHandle.click(page_driver,self.conf_edge['Click edge type'])
        helperHandle.click(page_driver,self.conf_edge['Click Select'])

    def first_page_edge(self,version):
        page_driver = (
            self.browser.pages[0] if module_type == 'playwright' else self.browser
        )
        helperHandle.wait_element_visible(page_driver,self.conf_edge['Change Name'])
        if version=='Stable' or version=='list Stable':
            helperHandle.input_text(page_driver,self.conf_edge['Change Name'],dt_strftime()+f"   {version}  Edge")
        elif version=='Beta':
            helperHandle.input_text(page_driver,self.conf_edge['Change Name'],dt_strftime()+f"   {version}  Edge")
        elif version=='Dev':
            helperHandle.input_text(page_driver,self.conf_edge['Change Name'],dt_strftime()+f"   {version}  Edge")
        helperHandle.click(page_driver,self.conf_365['Click Next'])


    def second_page_edge(self,version):
        page_driver = (
            self.browser.pages[0] if module_type == 'playwright' else self.browser
        )
        if version=='Stable' or version=='list Stable':
            pass
        elif version=='Beta':
            helperHandle.click(page_driver,self.conf_edge['Click Channel'])
            helperHandle.click(page_driver,self.conf_edge['Click Beta'])
        elif version=='Dev':
            helperHandle.click(page_driver,self.conf_edge['Click Channel'])
            helperHandle.click(page_driver,self.conf_edge['Click Dev'])

        if version=='Stable' or version=='list Stable':
            helperHandle.click(page_driver,self.conf_edge['Click Language'])
        elif version=='Beta' or version=='Dev':
            helperHandle.click(page_driver,self.conf_edge['Click Language Beta and Dev'])

        time.sleep(1)
        num=helperHandle.find_elements(page_driver,self.conf_edge['Select Language'])
        a=len(num)
        rint = random.randint(1,a-1)
        locator=num[rint]
        locator.click()
        helperHandle.click(page_driver,self.conf_365['Click Next'])


    def third_page_edge(self):
        page_driver = (
            self.browser.pages[0] if module_type == 'playwright' else self.browser
        )
        helperHandle.click(page_driver,self.conf_365['Click Next'])


    def forth_page_edge(self,version):
        page_driver = (
            self.browser.pages[0] if module_type == 'playwright' else self.browser
        )
        if version=='not list':
            helperHandle.click(page_driver,self.conf_edge['Click Add group'])
        elif version=='list':
            helperHandle.click(page_driver,self.conf_edge['Add group'])
        helperHandle.wait_element_visible(page_driver,self.conf_365['Click Search'])
        helperHandle.input_text(page_driver,self.conf_365['Click Search'],'win1')
        helperHandle.click(page_driver,self.conf_365['Click win10app'])
        helperHandle.click(page_driver,self.conf_365['Click win11app'])
        helperHandle.click(page_driver,self.conf_365['Click Select'])
        helperHandle.click(page_driver,self.conf_365['Click Next'])


    def fifth_page_edge(self):
        page_driver = (
            self.browser.pages[0] if module_type == 'playwright' else self.browser
        )
        helperHandle.click(page_driver,self.conf_365['Click Next'])
        


if __name__ == '__main__':
    
    helperHandle.set_helper(ParametersConfig().module_type)
    browser = helperHandle.get_browser()
    data=open(f'C:\\Users\\v-jaspershi\\Downloads\\CMD-Test-Shared\\CMD-Test-Shared\\workspace\\win365\\AppRegressionNew\\app\\data.json')
    data = json.load(data)
    env = data[0]['env']
    #test_result_metrics = get_test_result_metric(env)
    c = CreateEdge(browser)
    common = CommonPageOperator(browser,env)
    common.login_MEM_portal(data[0]['username'], data[0]['password'])
    common.goto_blade(tab='Apps',blade='Windows')
    c.before_choose_app_type()
    c.first_page_edge('Dev')
    c.second_page_edge('Dev')
    c.third_page_edge()
    c.forth_page_edge()
    c.fifth_page_edge()