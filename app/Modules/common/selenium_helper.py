from enum import Enum
from time import sleep
from typing import Union, List


from common.log_utils import LogLevel, LogUtils
from common.parameters_config import ParametersConfig
from selenium import webdriver
#浏览器配置
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.firefox.options import Options as FireFoxOptions
#每个获取出来的元素的所属类
from selenium.webdriver.remote.webelement import WebElement
#判断页面元素的方法
from selenium.webdriver.support import expected_conditions as EC
#等待
from selenium.webdriver.support.ui import WebDriverWait
#驱动
from selenium.webdriver.chrome.webdriver import WebDriver as ChromeDriver
from selenium.webdriver.edge.webdriver import WebDriver as EdgeDriver
from selenium.webdriver.firefox.webdriver import WebDriver as FirefoxDriver
#模拟鼠标操作的常用方法
from selenium.webdriver import ActionChains


class DriverType(Enum):
    Remote = "remote"
    Firefox = "firefox"
    Chrome = "chrome"
    Edge = "edge"


logUtils = LogUtils()


class SeleniumHelper:
    def __init__(self):
        self.driver_type = ParametersConfig.driver_type
        self.show_browser_window = ParametersConfig.show_browser_window
        self.default_timeout_second = ParametersConfig.default_timeout_second
        helperHandle.click_safe_wait_second = ParametersConfig.click_safe_wait_second

    def get_browser(self):
        if self.driver_type == DriverType.Firefox.value:
            options = FireFoxOptions()
            if not self.show_browser_window:
                options.add_argument("--headless")
            firefoxDriver = webdriver.Firefox(options=options)
            firefoxDriver.implicitly_wait(self.default_timeout_second)
            return firefoxDriver
        elif self.driver_type == DriverType.Chrome.value:
            options = ChromeOptions()
            options.add_argument('--no-sandbox')
            options.add_argument('--disable-gpu')
            options.add_argument('--disable-dev-shm-usage')
            options.add_argument("--incognito")
            if not self.show_browser_window:
                options.add_argument("--headless")
            chrome_driver = webdriver.Chrome(options=options)
            chrome_driver.set_window_size(1800, 1000)
            chrome_driver.implicitly_wait(self.default_timeout_second)
            return chrome_driver
        elif self.driver_type == DriverType.Edge.value:
            options = EdgeOptions()
            options.add_argument('--start-maximized')
            options.add_argument("--inprivate")
            if not self.show_browser_window:
                options.add_argument("--headless")
            driver = webdriver.Edge(options=options)
            driver.implicitly_wait(self.default_timeout_second)
            return driver

    def open_page(self, driver: Union[ChromeDriver, EdgeDriver, FirefoxDriver], url):
        """Open url and validate"""
        try:
            driver.get(url)
            logUtils.print(LogLevel.INFO, "Open page：{}".format(url))
        except Exception as error:
            driver.quit()
            raise Exception('Open url:{} error: {}'.format(url, error))

    def click(self, driver: Union[ChromeDriver, EdgeDriver, FirefoxDriver], config):
        sleep(helperHandle.click_safe_wait_second)
        self.wait_element_clickable(driver, config)
        ele: WebElement = self.find_element(driver, config)
        ActionChains(driver).move_to_element(ele).click().perform()
        msg = "Click element:({},{},{})".format(
            config['name'], config['locator_type'], config['value']
        )
        logUtils.print(LogLevel.INFO, msg)

    def input_text(
        self,
        driver: Union[ChromeDriver, EdgeDriver, FirefoxDriver],
        config,
        input_keys: str,
    ):
        sleep(helperHandle.click_safe_wait_second)
        self.wait_element_visible(driver, config)
        ele = self.find_element(driver, config)
        ele.send_keys(input_keys)
        logUtils.print(LogLevel.INFO, config['name'] + ' input text:' + input_keys)

    def find_element(
        self, driver: Union[ChromeDriver, EdgeDriver, FirefoxDriver], config
    ):
        logUtils.print(LogLevel.INFO, 'Find element:({})'.format(config))
        ele_list = driver.find_elements(config['locator_type'], config['value'])
        if len(ele_list) == 0:
            raise Exception('No such element:({})'.format(config))
        else:
            return ele_list[0]

    def find_elements(
        self, driver: Union[ChromeDriver, EdgeDriver, FirefoxDriver], config
    ):
        logUtils.print(LogLevel.INFO, 'Find element:({})'.format(config))
        ele_list = driver.find_elements(config['locator_type'], config['value'])
        return ele_list

    def get_element_text(
        self, driver: Union[ChromeDriver, EdgeDriver, FirefoxDriver], config
    ):
        self.wait_element_visible(driver, config)
        ele: WebElement = self.find_element(driver, config)
        text = ele.text
        logUtils.print(LogLevel.INFO, 'Get {} text:{}'.format(config['name'], text))
        return text

    def wait_element_visible(
        self,
        driver: Union[ChromeDriver, EdgeDriver, FirefoxDriver],
        config,
        timeout_second=None,
    ):
        logUtils.print(
            LogLevel.INFO,
            'Wait element:({},{}) visible'.format(config['name'], config['value']),
        )
        if timeout_second is None:
            timeout_second = self.default_timeout_second
        element: WebElement = WebDriverWait(driver, timeout_second).until(
            EC.visibility_of_element_located((config['locator_type'], config['value']))
        )
        while EC.visibility_of(element) == False or element.is_enabled() == False:
            sleep(1)
            element = self.find_element(driver, config)

    def wait_element_text_to_be_present(
        self,
        driver: Union[ChromeDriver, EdgeDriver, FirefoxDriver],
        config,
        text,
        timeout_second=None,
    ):
        logUtils.print(
            LogLevel.INFO,
            'Wait element:({},{}) text is "{}"'.format(
                config['name'], config['value'], text
            ),
        )
        if timeout_second is None:
            timeout_second = self.default_timeout_second
        ele = EC.text_to_be_present_in_element(
            (config['locator_type'], config['value']), text
        )
        WebDriverWait(driver, timeout_second).until(ele)

    def wait_element_text_not_to_be_present(
        self,
        driver: Union[ChromeDriver, EdgeDriver, FirefoxDriver],
        config,
        text,
        timeout_second=None,
    ):
        logUtils.print(
            LogLevel.INFO,
            'Wait element:({},{}) text is not "{}"'.format(
                config['name'], config['value'], text
            ),
        )
        if timeout_second is None:
            timeout_second = self.default_timeout_second
        ele = EC.text_to_be_present_in_element(
            (config['locator_type'], config['value']), text
        )
        WebDriverWait(driver, timeout_second).until_not(ele)

    def wait_element_attribute_text_is(
        self,
        driver: Union[ChromeDriver, EdgeDriver, FirefoxDriver],
        config,
        attribute,
        text,
        timeout_second=None,
    ):
        logUtils.print(
            LogLevel.INFO,
            'Wait element:({},{}) attribute have "{}={}"'.format(
                config['name'], config['value'], attribute, text
            ),
        )
        if timeout_second is None:
            timeout_second = self.default_timeout_second
        self.wait_element_visible(driver, config)
        item = WebDriverWait(driver, timeout_second).until(
            EC.text_to_be_present_in_element_attribute(
                (config['locator_type'], config['value']),
                attribute,
                text,
            )
        )
        return item

    def element_is_visible(
        self, driver: Union[ChromeDriver, EdgeDriver, FirefoxDriver], config
    ):
        result = self.find_element(driver, config)
        if isinstance(result, WebElement):
            return EC.visibility_of(result)
        elif isinstance(result, List) and len(result) > 0:
            return True
        else:
            return False

    def element_is_enable(
        self, driver: Union[ChromeDriver, EdgeDriver, FirefoxDriver], config
    ):
        ele = self.find_element(driver, config)
        result = ele.get_attribute('aria-disabled')
        logUtils.print(
            LogLevel.INFO,
            'Element:({},{}) aria-disabled={}'.format(
                config['name'], config['value'], result
            ),
        )
        if result == 'true':
            return False
        else:
            return True

    def check_element_text_is(
        self,
        driver: Union[ChromeDriver, EdgeDriver, FirefoxDriver],
        config,
        excepted_text,
    ):
        ele_text = self.get_element_text(driver, config)
        if ele_text != excepted_text:
            raise Exception(
                'Element text:"" is not as excepted:""'.format(ele_text, excepted_text)
            )

    def check_page_title_is(
        self, driver: Union[ChromeDriver, EdgeDriver, FirefoxDriver], target_title
    ):
        current_title = driver.title.strip()
        logUtils.print(
            LogLevel.INFO, 'Current page title is "{}"'.format(current_title)
        )
        logUtils.print(
            LogLevel.INFO, 'Expected page title is "{}"'.format(target_title)
        )
        if current_title not in target_title:
            raise Exception(
                'Page title is not as excepted.Excepted:{}, Actual:{}'.format(
                    target_title, current_title
                )
            )

    def check_page_url_is(
        self, driver: Union[ChromeDriver, EdgeDriver, FirefoxDriver], excepted_url
    ):
        current_url = driver.current_url
        logUtils.print(LogLevel.INFO, 'Current page url is "{}"'.format(current_url))
        logUtils.print(LogLevel.INFO, 'Expected page url is "{}"'.format(excepted_url))
        if current_url not in excepted_url:
            raise Exception(
                'Page url is not as excepted.Excepted:{}, Actual:{}'.format(
                    excepted_url, current_url
                )
            )

    def click_open_new_page(
        self, driver: Union[ChromeDriver, EdgeDriver, FirefoxDriver], config
    ):
        helperHandle.click(driver, config)
        handles = driver.window_handles
        driver.switch_to.window(handles[1])
        logUtils.print(LogLevel.INFO, 'Open new page {}'.format(driver.current_url))

    def switch_to_page(
        self, driver: Union[ChromeDriver, EdgeDriver, FirefoxDriver], page_index
    ):
        handles = driver.window_handles
        driver.switch_to.window(handles[page_index])

    def close_page(self, driver: Union[ChromeDriver, EdgeDriver, FirefoxDriver]):
        driver.close()

    def quit_browser(self, driver: Union[ChromeDriver, EdgeDriver, FirefoxDriver]):
        driver.quit()

    def wait_element_clickable(self,driver: Union[ChromeDriver, EdgeDriver, FirefoxDriver],config,timeout_second=None,):
        self.wait_element_visible(driver, config)
        ele = EC.element_to_be_clickable((config['locator_type'], config['value']))
        if timeout_second is None:
            timeout_second = self.default_timeout_second
        WebDriverWait(driver, timeout_second).until(ele)
