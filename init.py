from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import unittest
import time
import os
import pytest
import inspect


# @pytest.fixture(scope="function")
# def browser():
#     print("\nstart browser for test..")
#     browser = webdriver.Chrome(r'C:\\chromedriver\chromedriver.exe')
#     browser.minimize_window()
#     yield browser
#     # этот код выполнится после завершения теста
#     print("\nquit browser..")
#     time.sleep(2)
#     browser.quit()


class TestBookPage():
    # номер 5
    @pytest.mark.smoke
    def test_guest_can_add_book_to_basket5(self, browser):
        assert True

    # номер 6
    @pytest.mark.regression
    def test_guest_can_see_book_price6(self, browser):
        assert True





if __name__ == '__main__':
#Preference -> Tools -> Python integrated Tools - Choose py.test as Default test runner.
    filename = inspect.getframeinfo(inspect.currentframe()).filename
    path = os.path.dirname(os.path.abspath(filename))
    pytest.main(['-v', os.path.join(path, filename)])

