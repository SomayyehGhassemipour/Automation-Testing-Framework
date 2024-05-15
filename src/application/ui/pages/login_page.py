from selenium.webdriver.support.ui import WebDriverWait
class LoginPage:
  
  # Placeholder constants
  URL = None
  USERNAME_FLD = None
  PASSWORD_FLD = None
  LOGIN_BTN = None

  # login methods
  def __init__(self, driver, url: str, login_fld: str, password_fld: str, login_btn: str):
    self.driver = driver

    # Initialize the constants
    URL = url
    USERNAME_FLD = login_fld
    PASSWORD_FLD = password_fld
    LOGIN_BTN = login_btn

  def navigate_to(self):
    self.driver.get(self.URL)
  
  def try_login(self, username: str, password: str):
    pass

  def check_wrong_creds_message(self):
    # Find error
    # Check the message with specific text "...."
    return False
  
  def check_documentation_link(self):
    pass
    

  

