from enum import Enum
from time import sleep

from common.log_utils import LogLevel, LogUtils
from common.parameters_config import ParametersConfig
from playwright.sync_api import (
    Browser,
    BrowserContext,
    Locator,
    Page,
    expect,
    sync_playwright,
)

logUtils = LogUtils()


class DriverType(Enum):
    Remote = "remote"
    Firefox = "firefox"
    Chrome = "chrome"
    Edge = "edge"


class LocatorType:
    XPATH = 'xpath'


playwright = sync_playwright().start()


class PlayWrightHelper:
    def __init__(self):
        self.driver_type = ParametersConfig.driver_type
        self.headless = not ParametersConfig.show_browser_window
        self.default_timeout_second = ParametersConfig.default_timeout_second
        self.click_safe_wait_second = ParametersConfig.click_safe_wait_second

    def get_browser(self):
        browser: Browser = None
        if self.driver_type == DriverType.Chrome.value:
            browser = playwright.chromium.launch(
                channel="chrome", headless=self.headless
            )

        elif self.driver_type == DriverType.Edge.value:
            browser = playwright.firefox.launch(
                channel="msedge", headless=self.headless
            )
        elif self.driver_type == DriverType.Firefox:
            browser = playwright.firefox.launch(
                channel="firefox", headless=self.headless
            )
        else:
            raise Exception('Unsupported browser:' + self.driver_type)
        browser_context = browser.new_context(viewport={'width': 1800, 'height': 1000})
        browser_context.set_default_timeout(1000 * self.default_timeout_second)
        return browser_context

    def open_page(self, browser: BrowserContext, url):
        """Open url and validate"""
        try:
            page = browser.new_page()
            page.goto(url)
            page.wait_for_load_state('domcontentloaded')
            page.set_default_timeout(1000 * self.default_timeout_second)
            logUtils.print(LogLevel.INFO, "Open page：{}".format(url))
        except Exception as error:
            raise Exception('Open page:{} failed: {}'.format(url, error))

    def click(self, page: Page, config):
        sleep(self.click_safe_wait_second)
        self.find_element(page, config).click()
        msg = "Click element:({},{},{})".format(
            config['name'], config['locator_type'], config['value']
        )
        logUtils.print(LogLevel.INFO, msg)

    def input_text(self, page: Page, config, input_keys: str):
        sleep(self.click_safe_wait_second)
        self.find_element(page, config).fill(input_keys)
        logUtils.print(LogLevel.INFO, config['name'] + ' input text:' + input_keys)

    def find_element(self, page: Page, config):
        logUtils.print(LogLevel.INFO, 'Find element:({})'.format(config))
        type, value = config['locator_type'], config['value']
        if type == LocatorType.XPATH:
            locator = page.locator('xpath=' + value)
        else:
            raise Exception('Unsupported locator type:' + type)
        return locator

    def find_elements(self, page: Page, config):
        logUtils.print(LogLevel.INFO, 'Find elements:({})'.format(config))
        type, value = config['locator_type'], config['value']
        if type == LocatorType.XPATH:
            locator = page.locator('xpath=' + value)
        else:
            raise Exception('Unsupported locator type:' + type)
        return locator.all()

    def get_element_text(self, page: Page, config):
        self.wait_element_visible(page, config)
        ele: Locator = self.find_element(page, config)
        text = ele.text_content()
        logUtils.print(LogLevel.INFO, 'Get {} text:{}'.format(config['name'], text))
        return text

    def wait_element_visible(self, page: Page, config, timeout_second=None):
        logUtils.print(
            LogLevel.INFO,
            'Wait element:({},{}) visible'.format(config['name'], config['value']),
        )
        if timeout_second is None:
            timeout_second = self.default_timeout_second
        locator = self.find_element(page, config)
        expect(locator).to_be_visible(timeout=1000 * timeout_second)

    def wait_element_text_to_be_present(
        self, page: Page, config, text, timeout_second=None
    ):
        logUtils.print(
            LogLevel.INFO,
            'Wait element:({},{}) text is "{}"'.format(
                config['name'], config['value'], text
            ),
        )
        if timeout_second is None:
            timeout_second = self.default_timeout_second
        locator = self.find_element(page, config)
        expect(locator).to_have_text(text, timeout=1000 * timeout_second)

    def wait_element_text_not_to_be_present(
        self, page: Page, config, text, timeout_second=None
    ):
        logUtils.print(
            LogLevel.INFO,
            'Wait element:({},{}) text is not "{}"'.format(
                config['name'], config['value'], text
            ),
        )
        if timeout_second is None:
            timeout_second = self.default_timeout_second
        locator = self.find_element(page, config)
        expect(locator).not_to_have_text(text, timeout=1000 * timeout_second)

    def wait_element_attribute_text_is(
        self, page: Page, config, attribute, value, timeout_second=None
    ):
        logUtils.print(
            LogLevel.INFO,
            'Wait element:({},{}) attribute have "{}={}"'.format(
                config['name'], config['value'], attribute, value
            ),
        )
        if timeout_second is None:
            timeout_second = self.default_timeout_second
        locator = self.find_element(page, config)
        expect(locator).to_have_attribute(
            attribute, value, timeout=1000 * timeout_second
        )

    def element_is_visible(self, page: Page, config):
        locator = self.find_element(page, config)
        result = locator.is_visible()
        logUtils.print(
            LogLevel.INFO,
            'Element:({},{}) is visible:{}'.format(
                config['name'], config['value'], result
            ),
        )
        return result

    def element_is_enable(self, page: Page, config):
        locator = self.find_element(page, config)
        result = locator.get_attribute('aria-disabled')
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

    def check_element_text_is(self, page: Page, config, excepted_text):
        ele_text = self.get_element_text(page, config)
        if ele_text != excepted_text:
            raise Exception(
                'Element text:"" is not as excepted:""'.format(ele_text, excepted_text)
            )

    def check_page_title_is(self, page: Page, target_title):
        current_title = page.title()
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

    def check_page_url_is(self, page: Page, excepted_url):
        current_url = page.url
        logUtils.print(LogLevel.INFO, 'Current page url is "{}"'.format(current_url))
        logUtils.print(LogLevel.INFO, 'Expected page url is "{}"'.format(excepted_url))
        if current_url not in excepted_url:
            raise Exception(
                'Page url is not as excepted.Excepted:{}, Actual:{}'.format(
                    excepted_url, current_url
                )
            )

    def click_open_new_page(self, browser: BrowserContext, page: Page, config):
        with browser.expect_page() as new_page_info:
            self.click(page, config)
            new_page = new_page_info.value
        new_page.wait_for_load_state('domcontentloaded')
        logUtils.print(LogLevel.INFO, 'Open new page {}'.format(new_page.url))

    def switch_to_page(self, browser: BrowserContext, page_index):
        return browser.pages[page_index]

    def close_page(self, page: Page):
        page.close()

    def quit_browser(self, browser: BrowserContext):
        browser.close()

    def upload(self, page: Page, config,typ):
        # if isinstance(locator,WebElement):
        #     ele=locator
        # else:
        locator = self.find_element(page, config)
        if typ=='notepad' or typ=='list notepad':
            locator.set_input_files('C:/Users/v-jaspershi/Desktop/App/App/SampleApps/VersionOne/npp.installer.msi')
        elif typ=='spartan':
            locator.set_input_files('C:/Users/v-jaspershi/Desktop/App/App/SampleApps/VersionOne/Spartan.appxbundle')
        elif typ=='orca' or typ=='list orca':
            locator.set_input_files('C:/Users/v-jaspershi/Desktop/App/App/SampleApps/VersionOne/orca.intunewin')

