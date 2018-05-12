import pytest
import os
from appium import webdriver

AWS = 'aws'
LOCAL = 'local'
ANDROID = 'android'
IOS = 'ios'

def get_desired_capabilities(location=AWS, type=ANDROID):
  if location == LOCAL:
    if type == ANDROID:
      return {
        'app': os.path.expanduser(
          './android/app/build/outputs/apk/app-debug.apk'
        ),
        'platformName': 'Android',
        'deviceName': 'Android Emulator'
      }
    else:
      return {
        'app': os.path.expanduser(
          './ios/build/Build/Products/Release-iphonesimulator/rnappium.app'
        ),
        'platformName': 'ios',
        'deviceName': 'iPhone 8',
        'automationName': 'XCUITest'
      }
  else:
    return {}

@pytest.fixture(scope="function")
def driver():
  driver = webdriver.Remote(
    command_executor='http://0.0.0.0:4723/wd/hub',
    desired_capabilities=get_desired_capabilities(
      location=os.environ.get('LOCATION'),
      type=os.environ.get('TYPE')
    )
  )

  yield driver # test code runs after this line

  ## teardown
  driver.quit()
