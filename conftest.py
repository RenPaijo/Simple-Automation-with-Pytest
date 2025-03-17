import os
from datetime import datetime
import time
from selenium import webdriver
import pytest

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    now = datetime.now()
    pytest_html = item.config.pluginmanager.getplugin("html")
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, "extra", [])

    if report.when == "call" or report.when == "setup":
        xfail = hasattr(report, "wasxfail")
        if (report.skipped and xfail) or (report.failed and not xfail):
            test_name = item.nodeid.replace("::", "_").replace("/", "_")
            file_name = f"screenshot-{test_name}-{now.strftime('%Y-%m-%d_%H-%M-%S')}.png"
            _capture_screenshot(file_name)
            if file_name:
                html = (
                    f'<div><img src="{os.path.join("screenshots", file_name)}" alt="screenshot" style="width:304px;height:228px;" '
                    'onclick="window.open(this.src)" align="right"/></div>'
                )
                extra.append(pytest_html.extras.html(html))
        report.extra = extra


def _capture_screenshot(name):
    screenshot_dir = "screenshots"
    if not os.path.exists(screenshot_dir):
        os.makedirs(screenshot_dir)
    screenshot_path = os.path.join(screenshot_dir, name)
    global driver
    time.sleep(0.5)
    try:
        driver.get_screenshot_as_file(screenshot_path)
    except Exception as e:
        print(f"Failed to capture screenshot: {e}")


def pytest_html_report_title(report):
    report.title = "Automation Report Aldan Maulana Fajri"


@pytest.fixture(scope="function", autouse=True)
def setup(request):
    global driver
    options = webdriver.ChromeOptions()
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    options.add_argument("--headless=new")
    options.add_argument("--window-size=1920,1080")
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(5)
    driver.get("https://demoqa.com/login")
    driver.maximize_window()

    test_name = request.node.nodeid.replace("::", "_").replace("/", "_")
    screenshot_dir = "screenshots"
    for filename in os.listdir(screenshot_dir):
        if filename.startswith(f"screenshot-{test_name}-") and filename.endswith(".png"):
            os.remove(os.path.join(screenshot_dir, filename))

    request.cls.driver = driver
    yield driver
    driver.quit()