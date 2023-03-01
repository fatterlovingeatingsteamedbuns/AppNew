from copy import deepcopy
from time import sleep
import os
import sys
sys.path.append(os.path.split(os.path.abspath(os.path.dirname(__file__)))[0])
from common.helper_handle import HelperHandle
from common.log_utils import LogLevel, LogUtils
from common.common_utils import unicode,gen_random_string
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
from page_config.create_orca import (
    Create_orca,
)
from page_config.create_notepad import (
    Create_notepad,
)
helperHandle = HelperHandle()
logger = LogUtils()
module_type = ParametersConfig().module_type
common = CommonPageOperator
class CreateOrca:

    def __init__(self, browser):
        self.browser = browser
        self.conf_365= deepcopy(Create_365)
        self.conf_orca= deepcopy(Create_orca)
        self.conf_notepad= deepcopy(Create_notepad)
        self.conf_same = deepcopy(Same)

    def before_choose_app_type(self):
        page_driver = (
            self.browser.pages[0] if module_type == 'playwright' else self.browser
        )
        helperHandle.click(page_driver,self.conf_same['Click Add'])
        helperHandle.click(page_driver,self.conf_same['Click Down'])
        helperHandle.click(page_driver,self.conf_orca['Select Orca'])
        helperHandle.click(page_driver,self.conf_same['Click Select'])


    def first_page_orca(self,typ):
        page_driver = (
            self.browser.pages[0] if module_type == 'playwright' else self.browser
        )
        helperHandle.click(page_driver,self.conf_notepad['Click Select app package file'])
        helperHandle.upload(page_driver,self.conf_notepad['Click Select a file'],typ)
        helperHandle.click(page_driver,self.conf_notepad['Click Ok'])
        helperHandle.wait_element_visible(page_driver,self.conf_notepad['Name'])
        helperHandle.input_text(page_driver,self.conf_notepad['Name'],dt_strftime()+f"     {typ}")
        helperHandle.wait_element_visible(page_driver,self.conf_notepad['Edit Description'])
        helperHandle.click(page_driver,self.conf_notepad['Edit Description'])
        helperHandle.click(page_driver,self.conf_notepad['Preview'])
        helperHandle.input_text(page_driver,self.conf_orca['Description'],unicode(100))
        helperHandle.click(page_driver,self.conf_notepad['Description OK'])
        helperHandle.input_text(page_driver,self.conf_notepad['Publisher'],gen_random_string())
        helperHandle.click(page_driver,self.conf_365['Click Next'])


    def second_page_orca(self):
        page_driver = (
            self.browser.pages[0] if module_type == 'playwright' else self.browser
        )
        helperHandle.click(page_driver,self.conf_365['Click Next'])




    def third_page_orca(self):
        page_driver = (
            self.browser.pages[0] if module_type == 'playwright' else self.browser
        )
        helperHandle.click(page_driver,self.conf_orca['Click Operating system architecture'])
        helperHandle.click(page_driver,self.conf_orca['Click 32'])
        helperHandle.click(page_driver,self.conf_orca['Click 64'])
        helperHandle.click(page_driver,self.conf_orca['Second Click Operating system architecture'])
        helperHandle.click(page_driver,self.conf_orca['Click Minimum operating system'])
        num=helperHandle.find_elements(page_driver,self.conf_365['Down2'])
        a=len(num)
        rint = random.randint(0,a-1)
        locator=num[rint]
        locator.click()
        helperHandle.click(page_driver,self.conf_365['Click Next'])


    def forth_page_orca(self):
        page_driver = (
            self.browser.pages[0] if module_type == 'playwright' else self.browser
        )
        helperHandle.click(page_driver,self.conf_orca['Click Rules format'])
        helperHandle.click(page_driver,self.conf_orca['Click Manually'])
        helperHandle.click(page_driver,self.conf_orca['Click Add'])
        helperHandle.click(page_driver,self.conf_orca['Click Rule type'])
        helperHandle.click(page_driver,self.conf_orca['Click MSI'])
        helperHandle.click(page_driver,self.conf_orca['Click OK'])
        helperHandle.click(page_driver,self.conf_365['Click Next'])


        
    def fifth_page_orca(self):
        page_driver = (
            self.browser.pages[0] if module_type == 'playwright' else self.browser
        )
        helperHandle.click(page_driver,self.conf_365['Click Next'])

    def sixth_page_orca(self):
        page_driver = (
            self.browser.pages[0] if module_type == 'playwright' else self.browser
        )
        helperHandle.click(page_driver,self.conf_365['Click Next'])

    def seventh_page_orca(self):
        page_driver = (
            self.browser.pages[0] if module_type == 'playwright' else self.browser
        )
        helperHandle.click(page_driver,self.conf_365['Click Next'])

    
    def eighth_page_orca(self,typ):
        page_driver = (
            self.browser.pages[0] if module_type == 'playwright' else self.browser
        )
        if typ=='orca':
            helperHandle.click(page_driver,self.conf_orca['Click Add group'])
        elif typ=='list orca':
            helperHandle.click(page_driver,self.conf_orca['Click list group'])
        helperHandle.wait_element_visible(page_driver,self.conf_365['Click Search'])
        helperHandle.input_text(page_driver,self.conf_365['Click Search'],'win1')
        helperHandle.click(page_driver,self.conf_365['Click win10app'])
        helperHandle.click(page_driver,self.conf_365['Click win11app'])
        helperHandle.click(page_driver,self.conf_365['Click Select'])
        helperHandle.click(page_driver,self.conf_365['Click Next'])




    def ninth_page_orca(self):
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
    c = CreateOrca(browser)
    common = CommonPageOperator(browser,env)
    common.login_MEM_portal(data[0]['username'], data[0]['password'])
    common.goto_blade(tab='Apps',blade='Windows')
    c.before_choose_app_type()
    c.first_page_orca('orca')
    c.second_page_orca()
    c.third_page_orca()
    c.forth_page_orca()
    c.fifth_page_orca()
    c.sixth_page_orca()
    c.seventh_page_orca()
    c.eighth_page_orca()
    c.ninth_page_orca()

