import pytest
import os
from appium import webdriver

@pytest.fixture(scope="function")
def driver():
  driver = webdriver.Remote(
    command_executor='http://0.0.0.0:4723/wd/hub',
    desired_capabilities={
      'app': os.path.expanduser(
        './android/app/build/outputs/apk/app-debug.apk'),
        'platformName': 'Android',
        'deviceName': 'Android Emulator'
      }
    )

  yield driver # test code runs after this line

  ## teardown
  driver.quit()
