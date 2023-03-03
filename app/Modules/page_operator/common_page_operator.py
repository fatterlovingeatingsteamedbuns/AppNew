from copy import deepcopy
from time import sleep

import json
from common.base import get_test_result_metric


from common.env_config import (
    EnvList,
    GCB_EnvConf,
    GCP_EnvConf,
    GHB_EnvConf,
    GHP_EnvConf,
    INT_EnvConf,
    PE_EnvConf,
    PPE_EnvConf,
    SH_EnvConf,
)
from common.helper_handle import HelperHandle
from common.log_utils import LogLevel, LogUtils
from common.parameters_config import ParametersConfig
from page_config.common_page_config import CommonPageConf
from selenium.webdriver.remote.webelement import WebElement
from page_config.same import Same
logUtils = LogUtils()
helperHandle = HelperHandle()
module_type = ParametersConfig().module_type


class CommonPageOperator:
    def __init__(self, browser, env):
        self.browser = browser
        self.conf = deepcopy(CommonPageConf)
        self.conf_same=deepcopy(Same)
        if env == EnvList.SH:
            self.env_conf = deepcopy(SH_EnvConf)
        elif env == EnvList.PPE:
            self.env_conf = deepcopy(PPE_EnvConf)
        elif env == EnvList.PE:
            self.env_conf = deepcopy(PE_EnvConf)
        elif env == EnvList.GCB:
            self.env_conf = deepcopy(GCB_EnvConf)
        elif env == EnvList.GCP:
            self.env_conf = deepcopy(GCP_EnvConf)
        elif env == EnvList.GHB:
            self.env_conf = deepcopy(GHB_EnvConf)
        elif env == EnvList.GHP:
            self.env_conf = deepcopy(GHP_EnvConf)
        elif env == EnvList.INT:
            self.env_conf = deepcopy(INT_EnvConf)
        else:
            raise Exception("Unsupported environment:" + env)

    def login_MEM_portal(self, username, password):
        start_url = self.env_conf['mem_portal_url']
        helperHandle.open_page(self.browser, start_url)
        page_driver = (
            self.browser.pages[0] if module_type == 'playwright' else self.browser
        )
        helperHandle.input_text(page_driver, self.conf['User name'], username)
        helperHandle.click(page_driver, self.conf['Next'])
        # sleep(2)
        # helperHandle.input_text(page_driver, self.conf['Password'], password)
        # helperHandle.click(page_driver, self.conf['Login'])
        # helperHandle.click(page_driver, self.conf['Remain login state'])
        logUtils.print(
            LogLevel.INFO, "User：%s login：%s success" % (username, start_url)
        )
        helperHandle.wait_element_visible(page_driver, self.conf['Blade title'])

    def goto_blade(self, tab='Devices', blade='Overview'):
        """
        tab = Home, Dashboard, All devices, Apps, Users, Groups ...
        """
        page_driver = (
            self.browser.pages[0] if module_type == 'playwright' else self.browser
        )
        if tab == 'Devices' and blade == 'Overview':
            return
        conf = self.conf
        if helperHandle.element_is_visible(page_driver, self.conf['main page']):
            pass
        else:
            helperHandle.click(page_driver, conf['row'])
        helperHandle.click(page_driver, conf[tab])
        helperHandle.click(page_driver, conf[blade])
        logUtils.print(LogLevel.INFO, 'Go to [{} -> {}] blade'.format(tab, blade))

    def check_successfully(self):
        page_driver = (
            self.browser.pages[0] if module_type == 'playwright' else self.browser
        )
        text=helperHandle.get_element_text(page_driver, self.conf_same['Click Overview'])
        if text=='Overview':
            logUtils.print(LogLevel.INFO, 'successfully')
        else:
            logUtils.print(LogLevel.INFO, 'fail')

    # def upload(self,locator,typ):
    #     page_driver = (
    #         self.browser.pages[0] if module_type == 'playwright' else self.browser
    #     )
    #     if isinstance(locator,WebElement):
    #         ele=locator
    #     else:
    #         ele=helperHandle.find_element(page_driver,locator)
    #     if typ=='notepad':
    #         ele.set_input_files('C:/Users/v-jaspershi/Desktop/App/App/SampleApps/VersionOne/npp.installer.msi')
    #     elif typ=='spartan':
    #         ele.set_input_files('C:/Users/v-jaspershi/Desktop/App/App/SampleApps/VersionOne/Spartan.appxbundle')
    #     elif typ=='orca':
    #         ele.set_input_files('C:/Users/v-jaspershi/Desktop/App/App/SampleApps/VersionOne/orca.intunewin')


    

if __name__ == "__main__":
    helperHandle.set_helper(ParametersConfig().module_type)
    browser = helperHandle.get_browser()
    data=open(f'C:\\Users\\v-jaspershi\\Downloads\\CMD-Test-Shared\\CMD-Test-Shared\\workspace\\win365\\app\\data.json')
    data = json.load(data)
    env = data[0]['env']
    #test_result_metrics = get_test_result_metric(env)
    c = CommonPageOperator(browser,env)
    c.login_MEM_portal(data[0]['username'], data[0]['password'])
    c.goto_blade(tab='Apps',blade='Windoes')