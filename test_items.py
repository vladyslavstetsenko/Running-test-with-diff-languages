import time

from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_find_the_button(browser):
    # Check if "add to basket" button exist
    browser.get(link)
    time.sleep(30)
    btn = browser.find_element(By.XPATH, "//form[@id='add_to_basket_form']/button[@type='submit']")

    assert btn, "Button does not found"


