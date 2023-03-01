
from typing import List, Union
from common.playwright_helper import PlayWrightHelper
from common.selenium_helper import SeleniumHelper
from playwright.sync_api import BrowserContext, Locator, Page
from selenium.webdriver.chrome.webdriver import WebDriver as ChromeDriver
from selenium.webdriver.edge.webdriver import WebDriver as EdgeDriver
from selenium.webdriver.firefox.webdriver import WebDriver as FirefoxDriver
from selenium.webdriver.remote.webelement import WebElement


class HelperHandle:
    #清空
    helper: Union[PlayWrightHelper, SeleniumHelper] = None
    module_type = None

    def set_helper(self, module_type) -> Union[SeleniumHelper, PlayWrightHelper]:
        HelperHandle.module_type = module_type
        if module_type == 'selenium':
            HelperHandle.helper: SeleniumHelper = SeleniumHelper()
        elif module_type == 'playwright':
            HelperHandle.helper: PlayWrightHelper = PlayWrightHelper()
        else:
            raise Exception('Unsupported module type:' + module_type)

    def get_browser(self,) -> Union[BrowserContext, EdgeDriver, ChromeDriver, FirefoxDriver]:
        return HelperHandle.helper.get_browser()

    def open_page(self,browser: Union[BrowserContext, EdgeDriver, ChromeDriver, FirefoxDriver],url,):
        return HelperHandle.helper.open_page(browser, url)

    def click(self, page: Union[Page, EdgeDriver, ChromeDriver, FirefoxDriver], config):
        HelperHandle.helper.click(page, config)

    def input_text(self, page: Union[Page, EdgeDriver, ChromeDriver, FirefoxDriver], config, text):
        HelperHandle.helper.input_text(page, config, text)

    def find_element(self, page: Union[Page, EdgeDriver, ChromeDriver, FirefoxDriver], config) -> Union[Locator, WebElement]:
        return HelperHandle.helper.find_element(page, config)

    def find_elements(self, page: Union[Page, EdgeDriver, ChromeDriver, FirefoxDriver], config) -> Union[List[Locator], List[WebElement]]:
        return HelperHandle.helper.find_elements(page, config)

    def get_element_text(self, page: Union[Page, EdgeDriver, ChromeDriver, FirefoxDriver], config):
        return HelperHandle.helper.get_element_text(page, config)

    def wait_element_visible(self,page: Union[Page, EdgeDriver, ChromeDriver, FirefoxDriver],config,timeout_second=None,):
        HelperHandle.helper.wait_element_visible(page, config, timeout_second)

    def wait_element_text_to_be_present(self,page: Union[Page, EdgeDriver, ChromeDriver, FirefoxDriver],config,text,timeout_second=None,):
        HelperHandle.helper.wait_element_text_to_be_present(
            page, config, text, timeout_second
        )

    def wait_element_text_not_to_be_present(self,page: Union[Page, EdgeDriver, ChromeDriver, FirefoxDriver],config,text,timeout_second=None,):
        HelperHandle.helper.wait_element_text_not_to_be_present(
            page, config, text, timeout_second
        )

    def wait_element_attribute_text_is(self,page: Union[Page, EdgeDriver, ChromeDriver, FirefoxDriver],config,attribute,text,timeout_second=None,):
        HelperHandle.helper.wait_element_attribute_text_is(
            page, config, attribute, text, timeout_second
        )

    def element_is_visible(self, page: Union[Page, EdgeDriver, ChromeDriver, FirefoxDriver], config) -> bool:
        return HelperHandle.helper.element_is_visible(page, config)

    def element_is_enable(self, page: Union[Page, EdgeDriver, ChromeDriver, FirefoxDriver], config) -> bool:
        return HelperHandle.helper.element_is_enable(page, config)

    def check_element_text_is(self,page: Union[Page, EdgeDriver, ChromeDriver, FirefoxDriver],config,excepted_text,):
        HelperHandle.helper.check_element_text_is(page, config, excepted_text)

    def check_page_title_is(self, page: Union[Page, EdgeDriver, ChromeDriver, FirefoxDriver], target_title):
        HelperHandle.helper.check_page_title_is(page, target_title)

    def check_page_url_is(self, page: Union[Page, EdgeDriver, ChromeDriver, FirefoxDriver], excepted_url):
        HelperHandle.helper.check_page_url_is(page, excepted_url)
        
    def click_open_new_page(self,config,browser: BrowserContext = None,page: Page = None,driver: Union[ChromeDriver, EdgeDriver, FirefoxDriver] = None,):
        if HelperHandle.module_type == 'selenium':
            HelperHandle.helper.click_open_new_page(driver, config)
        if HelperHandle.module_type == 'playwright':
            HelperHandle.helper.click_open_new_page(browser, page, config)

    def switch_to_page(self,browser: BrowserContext = None,page_driver: Union[Page, ChromeDriver, EdgeDriver, FirefoxDriver] = None,index=None,):
        if HelperHandle.module_type == 'selenium':
            HelperHandle.helper.switch_to_page(page_driver, index)
        if HelperHandle.module_type == 'playwright':
            return HelperHandle.helper.switch_to_page(browser, page_driver, index)

    def close_page(self, page: Union[Page, ChromeDriver, EdgeDriver, FirefoxDriver]):
        HelperHandle.helper.close_page(page)

    def quit_browser(self, browser: Union[BrowserContext, ChromeDriver, EdgeDriver, FirefoxDriver]):
        HelperHandle.helper.quit_browser(browser)

    def upload(self, page: Union[Page, EdgeDriver, ChromeDriver, FirefoxDriver], config, typ):
        HelperHandle.helper.upload(page, config, typ)