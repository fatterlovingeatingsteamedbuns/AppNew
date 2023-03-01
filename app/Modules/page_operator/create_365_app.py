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
from page_config.uninstall import (
    Uninstall,
)
helperHandle = HelperHandle()
logger = LogUtils()
module_type = ParametersConfig().module_type


class Create365:

    def __init__(self, browser):
        self.browser = browser
        self.conf_365= deepcopy(Create_365)
        self.conf_same = deepcopy(Same)
        self.conf_uninstall = deepcopy(Uninstall)

    def before_choose_app_type(self):
        page_driver = (
            self.browser.pages[0] if module_type == 'playwright' else self.browser
        )
        helperHandle.click(page_driver,self.conf_same['Click Add'])
        helperHandle.click(page_driver,self.conf_same['Click Down'])
        helperHandle.click(page_driver,self.conf_365['Click 365 type'])
        helperHandle.click(page_driver,self.conf_same['Click Select'])

    def first_page_365(self,typ):
        page_driver = (
            self.browser.pages[0] if module_type == 'playwright' else self.browser
        )
        helperHandle.wait_element_visible(page_driver,self.conf_365['Change Name'])
        helperHandle.input_text(page_driver,self.conf_365['Change Name'],dt_strftime()+f"       {typ}")
        helperHandle.click(page_driver,self.conf_365['Click Next'])

    def second_page_365(self):
        page_driver = (
            self.browser.pages[0] if module_type == 'playwright' else self.browser
        )
        print(self.conf_365['Click Default file format'])
        helperHandle.click(page_driver,self.conf_365['Click Default file format'])
        time.sleep(1)
        num=helperHandle.find_elements(page_driver,self.conf_365['Down'])
        print(num)
        a=len(num)
        # print(a)
        rint = random.randint(0,a-1)
        # rint=str(rint)
        # locator= self.conf_365['Down']['value'] +'['+ rint +']'
        locator=num[rint]
        locator.click()
        #helperHandle.click(page_driver,locator)
        # locator.click()
        helperHandle.wait_element_visible(page_driver,self.conf_365['Click DUpdate channel'])
        helperHandle.click(page_driver,self.conf_365['Click DUpdate channel'])
        time.sleep(1)
        num1=helperHandle.find_elements(page_driver,self.conf_365['Down2'])
        a1=len(num1)
        rint1 = random.randint(1,a1-1)
        locator1=num1[rint1]
        locator1.click()
        # helperHandle.click(page_driver,locator1)
        helperHandle.click(page_driver,self.conf_365['Click Next'])



    def third_page_365(self):
        page_driver = (
            self.browser.pages[0] if module_type == 'playwright' else self.browser
        )
        helperHandle.wait_element_visible(page_driver,self.conf_365['Click Next'])
        helperHandle.click(page_driver,self.conf_365['Click Next'])
    
    def forth_page_365(self,typ):
        page_driver = (
            self.browser.pages[0] if module_type == 'playwright' else self.browser
        )
        if typ=='365':
            helperHandle.click(page_driver,self.conf_365['Click Add group'])
        elif typ=='list 365':
            helperHandle.click(page_driver,self.conf_365['Add group'])
        helperHandle.wait_element_visible(page_driver,self.conf_365['Click Search'])
        helperHandle.input_text(page_driver,self.conf_365['Click Search'],'win1')
        time.sleep(2)
        helperHandle.click(page_driver,self.conf_365['Click win10app'])
        helperHandle.click(page_driver,self.conf_365['Click win11app'])
        helperHandle.click(page_driver,self.conf_365['Click Select'])
        helperHandle.click(page_driver,self.conf_365['Click Next'])

    def fifth_page_365(self):
        page_driver = (
            self.browser.pages[0] if module_type == 'playwright' else self.browser
        )
        helperHandle.click(page_driver,self.conf_365['Click Next'])


    def delete(self):
        page_driver = (
            self.browser.pages[0] if module_type == 'playwright' else self.browser
        )
        helperHandle.wait_element_visible(page_driver,self.conf_same['click context menu'])

        
        while True:
            count_list=helperHandle.find_elements(page_driver,self.conf_same['Delete'])
            for i in range(len(count_list)):
                helperHandle.click(page_driver,self.conf_same['click context menu'])
                helperHandle.click(page_driver,self.conf_same['click delete button'])
                helperHandle.click(page_driver,self.conf_same['click yes'])
                helperHandle.wait_element_visible(page_driver,self.conf_same['click context menu'])
                
            
                    

    
    

if __name__ == '__main__':
    
    helperHandle.set_helper(ParametersConfig().module_type)
    browser = helperHandle.get_browser()
    data=open(f'C:\\Users\\v-jaspershi\\Downloads\\CMD-Test-Shared\\CMD-Test-Shared\\workspace\\win365\\AppRegressionNew\\app\\data.json')
    data = json.load(data)
    env = data[0]['env']
    #test_result_metrics = get_test_result_metric(env)
    c = Create365(browser)
    common = CommonPageOperator(browser,env)
    common.login_MEM_portal(data[0]['username'], data[0]['password'])
    common.goto_blade(tab='Apps',blade='Windows')
    #c.delete()
    # c.before_choose_app_type()
    # c.first_page_365()
    # c.second_page_365()
    # c.third_page_365()
    # c.forth_page_365()
    # c.fifth_page_365()
    c.uninstall()