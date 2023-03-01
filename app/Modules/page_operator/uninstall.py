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
from page_config.uninstall import (
    Uninstall,
)


helperHandle = HelperHandle()
logger = LogUtils()
module_type = ParametersConfig().module_type


class Uninstall_all():
    def __init__(self, browser):
        self.browser = browser
        self.conf_365= deepcopy(Create_365)
        self.conf_same = deepcopy(Same)
        self.conf_uninstall= deepcopy(Uninstall)


    def uninstall(self):
        page_driver = (
            self.browser.pages[0] if module_type == 'playwright' else self.browser
        )
        helperHandle.wait_element_visible(page_driver,self.conf_same['click context menu'])
        count=helperHandle.find_elements(page_driver,self.conf_same['Delete'])
            
        for i in range(len(count)):
            a="(//div[contains(text(),'2023')])"+"["+f"{i+1}"+"]"
            print(a)
            self.conf_same['Delete']['value']=a
            print(self.conf_same['Delete']['value'])
            helperHandle.find_element(page_driver,self.conf_same['Delete']).click()
            helperHandle.click(page_driver,self.conf_uninstall['click Properties'])
            helperHandle.click(page_driver,self.conf_uninstall['click Edit'])
            if helperHandle.wait_element_visible(page_driver,self.conf_uninstall['required included1']) == None:
                helperHandle.click(page_driver,self.conf_uninstall['required included1'])
                helperHandle.click(page_driver,self.conf_uninstall['Excluded'])
                helperHandle.click(page_driver,self.conf_uninstall['Click ok'])
                helperHandle.click(page_driver,self.conf_uninstall['required included2'])
                helperHandle.click(page_driver,self.conf_uninstall['Excluded'])
                helperHandle.click(page_driver,self.conf_uninstall['Click ok'])
            else:
                helperHandle.click(page_driver,self.conf_uninstall['available included1'])
                helperHandle.click(page_driver,self.conf_uninstall['Excluded'])
                helperHandle.click(page_driver,self.conf_uninstall['Click ok'])
                helperHandle.click(page_driver,self.conf_uninstall['available included2'])
                helperHandle.click(page_driver,self.conf_uninstall['Excluded'])
                helperHandle.click(page_driver,self.conf_uninstall['Click ok'])

            if helperHandle.element_is_visible(page_driver,self.conf_uninstall['Uninstall'])==False:
                pass
            else:
                helperHandle.click(page_driver,self.conf_uninstall['Uninstall'])
                helperHandle.input_text(page_driver,self.conf_365['Click Search'],'win1')
                helperHandle.click(page_driver,self.conf_365['Click win10app'])
                helperHandle.click(page_driver,self.conf_365['Click win11app'])
                helperHandle.click(page_driver,self.conf_365['Click Select'])
            helperHandle.click(page_driver,self.conf_uninstall['Review save and Save'])
            helperHandle.click(page_driver,self.conf_uninstall['Review save and Save'])
            self.go_to_windows()
            helperHandle.wait_element_visible(page_driver,self.conf_same['click context menu'])
            count=helperHandle.find_elements(page_driver,self.conf_same['Delete'])


    def go_to_windows(self):
        page_driver = (
            self.browser.pages[0] if module_type == 'playwright' else self.browser
        )
        helperHandle.click(page_driver,self.conf_365['Click go to windows'])


