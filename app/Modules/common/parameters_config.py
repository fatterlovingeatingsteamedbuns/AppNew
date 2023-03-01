import sys


class ParametersConfig:
    # Current support chrome only
    driver_type = 'chrome'

    default_timeout_second = 90
    click_safe_wait_second = 1

    default_module = 'playwright'

    show_browser_window = True

    is_local = True

    allure_report_dir = 'D:\\allure-report'

    #本地跑的时候依然是playright
    @property
    def module_type(self) -> str:
        type = ParametersConfig.default_module
        py_args = sys.argv
        if py_args is not None and len(py_args) > 1:
            type = py_args[1]

        return type


if __name__ == "__main__":
    para = ParametersConfig()
    para.module_type