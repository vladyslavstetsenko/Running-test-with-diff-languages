import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def chrome_options(user_language):
    # Options for Chrome browser
    options = Options()
    options.add_argument("--start-maximized")
    options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
    return options


def firefox_options(user_language):
    # Options for Firefox browser
    fp = webdriver.FirefoxProfile()
    fp.set_preference("intl.accept_languages", user_language)
    return fp


def pytest_addoption(parser):
    # Add "language" command line option
    # Add "browser_name" command line option
    parser.addoption(
        "--language", action="store", default=None, help="Choose your preference language. Example: --language=es"
    )
    parser.addoption(
        "--browser_name", action="store", default='chrome', help="Choose the browser: firefox or chrome"
    )


@pytest.fixture(scope="function")
def browser(request):
    # Pass "browser_name, language" values from command line to a test function
    browser_name = request.config.getoption("browser_name")
    user_language = request.config.getoption("language")

    # Initialization of chosen browser with a custom language
    if browser_name == 'chrome':
        print("\n start chrome browser to test..")
        browser = webdriver.Chrome(options=chrome_options(user_language))
    elif browser_name == 'firefox':
        print("\nstart firefox browser to test..")
        browser = webdriver.Firefox(firefox_profile=firefox_options(user_language))
    else:
        raise pytest.UsageError("undefined browser name")

    yield browser
    print("\nquit browser..")
    browser.quit()
