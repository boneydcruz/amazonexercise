import pytest
from selenium import webdriver


class Base:

    @pytest.fixture(autouse=True)
    def set_up(self):
        print("Initiating Firefox driver")
        self.driver = webdriver.Firefox()
        print("-----------------------------------------")
        print("Test is started")
        self.driver.implicitly_wait(10)
        self.driver.get("https://www.amazon.com.mx/")
        self.driver.maximize_window()

        yield self.driver
        if self.driver is not None:
            print("-----------------------------------------")
            print("Tests is finished")
            self.driver.close()
            self.driver.quit()
