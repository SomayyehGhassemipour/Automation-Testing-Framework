from application.ui.pages.login_page import LoginPage
from selenium import webdriver

class GithubUI:

  def __init__(self) -> None:
    self.driver = webdriver.Chrome()
    self.login_page = LoginPage(self.driver, "https://github.com/login", '//*[@id="login_field"]', '//*[@id="password"]', '//*[@id="login"]/div[4]/form/div/input[13]' )

  def try_login(self, username: str, password: str):
    return self.login_page.try_login(username, password)

  def close(self):
    self.driver.close()




