import pytest
from selenium import webdriver
from Pages.testcase import LoginPage


@pytest.fixture()
def test_setup():
    global driver
    driver = webdriver.Firefox()
    driver.maximize_window()
    yield
    driver.close()


def test_amazonexercise(test_setup):
    """""   driver.get("https://www.amazon.com.mx/")
       driver.find_element_by_id('twotabsearchtextbox').send_keys('iphone')
       driver.find_element_by_id('nav-search-submit-button').click()
       driver.execute_script("window.scrollTo(0, 6900)")
       driver.implicitly_wait(10)
       driver.find_element_by_css_selector("li.a-normal:nth-child(3) > a:nth-child(1)").click()
       driver.find_element_by_css_selector("div[data-index='1']").click()
       driver.implicitly_wait(10)"""""
    loginpage = LoginPage(driver)
    loginpage.search()
#   x = driver.title
#   assert x == "amazon"

#   element = driver.find_element_by_xpath('//*[@id="breadcrumb-back-link"]').text
#   assert element == 'Volver a resultados'

