import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import pytest

import conftest


def get_num(x):
    return int(''.join(el for el in x if el.isdigit()))


@pytest.fixture
def browser():
    print("\nstart browser for test..")
    #browser = webdriver.Chrome()
    browser = webdriver.Chrome(r'C:\\chromedriver\chromedriver.exe')
    yield browser
    print("\nquit browser..")
    time.sleep(2)
    browser.quit()


link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'


class TestBookPage():

    def test_exists_button_for_add_book_to_basket(self, browser, language):
        browser.get(link)
        language_selector = Select(
            browser.find_element_by_css_selector('select.form-control'))
        language_selector.select_by_value(language)

        button_change_language = \
            browser.find_element_by_css_selector('form#language_selector.'
                                                 'navbar-left.navbar-form '
                                                 'button.btn.btn-default')
        button_change_language.click()

        button_add_to_basket = \
            browser.find_element_by_css_selector('.btn-add-to-basket')
        button_add_to_basket.click()

        browser.implicitly_wait(2)

        basket_data = browser.find_element_by_css_selector('.basket-mini')
        basket_summ = int(get_num(basket_data.text))
        assert basket_summ > 0


if __name__ == '__main__':
    pytest.main()

