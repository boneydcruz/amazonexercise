from Pages.testcase import LoginPage
from Base.base import Base
import pytest


@pytest.mark.usefixtures('set_up')
class TestLogin(Base):

 def test_login_success(self):
        driver = self.driver
        driver = LoginPage(driver)
