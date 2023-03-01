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
from page_config.create_edge import (
    Create_edge,
)
from page_config.list_store import (
    List_store
)

helperHandle = HelperHandle()
logger = LogUtils()
module_type = ParametersConfig().module_type


class ListStore():
    def __init__(self, browser):
        self.browser = browser
        self.conf_365= deepcopy(Create_365)
        self.conf_edge= deepcopy(Create_edge)
        self.conf_same = deepcopy(Same)
        self.conf_list_store= deepcopy(List_store)
        


    def before_choose_app_type(self):
        page_driver = (
            self.browser.pages[0] if module_type == 'playwright' else self.browser
        )
        helperHandle.click(page_driver,self.conf_same['Click Add'])
        helperHandle.click(page_driver,self.conf_same['Click Down'])
        helperHandle.click(page_driver,self.conf_list_store['Select store'])
        helperHandle.click(page_driver,self.conf_same['Click Select'])


    def first_page_list_store(self):
        page_driver = (
            self.browser.pages[0] if module_type == 'playwright' else self.browser
        )
        helperHandle.wait_element_visible(page_driver,self.conf_list_store['Name'])
        
        helperHandle.input_text(page_driver,self.conf_list_store['Name'],dt_strftime()+"       list store")
        helperHandle.wait_element_visible(page_driver,self.conf_list_store['Edit Description'])
        
        helperHandle.click(page_driver,self.conf_list_store['Edit Description'])
        helperHandle.input_text(page_driver,self.conf_list_store['Description'],unicode(100))
        helperHandle.click(page_driver,self.conf_list_store['OK'])
        helperHandle.input_text(page_driver,self.conf_list_store['Publisher'],gen_random_string())
        helperHandle.input_text(page_driver,self.conf_list_store['Appstore URL'],"https://www.microsoft.com/store/p/lync/9wzdncrfhvhm")
        helperHandle.click(page_driver,self.conf_list_store['Next'])

    def second_page_list_store(self):
        page_driver = (
            self.browser.pages[0] if module_type == 'playwright' else self.browser
        )
        helperHandle.click(page_driver,self.conf_list_store['Next'])

    def third_page_list_store(self):
        page_driver = (
            self.browser.pages[0] if module_type == 'playwright' else self.browser
        )
        helperHandle.click(page_driver,self.conf_list_store['Add group'])
        helperHandle.wait_element_visible(page_driver,self.conf_365['Click Search'])
        
        helperHandle.input_text(page_driver,self.conf_365['Click Search'],'win1')
        time.sleep(2)
        helperHandle.click(page_driver,self.conf_365['Click win10app'])
        helperHandle.click(page_driver,self.conf_365['Click win11app'])
        helperHandle.click(page_driver,self.conf_365['Click Select'])
        helperHandle.click(page_driver,self.conf_list_store['Next'])

    def forth_page_list_store(self):
        page_driver = (
            self.browser.pages[0] if module_type == 'playwright' else self.browser
        )
        helperHandle.click(page_driver,self.conf_list_store['Click Create'])




if __name__ == '__main__':
    helperHandle.set_helper(ParametersConfig().module_type)
    browser = helperHandle.get_browser()
    data=open(f'C:\\Users\\v-jaspershi\\Downloads\\CMD-Test-Shared\\CMD-Test-Shared\\workspace\\win365\\AppRegressionNew\\app\\data.json')
    data = json.load(data)
    env = data[0]['env']
    #test_result_metrics = get_test_result_metric(env)
    c = ListStore(browser)
    common = CommonPageOperator(browser,env)
    common.login_MEM_portal(data[0]['username'], data[0]['password'])
    common.goto_blade(tab='Apps',blade='Windows')
    c.before_choose_app_type()
    c.first_page_list_store()
    c.second_page_list_store()
    c.third_page_list_store()
    c.forth_page_list_store()
    c.forth_page_list_store()