def test_basic(driver):
  WAIT_SEC = 10
  driver.implicitly_wait(WAIT_SEC)

  elem = driver.find_element_by_accessibility_id('testview')

  assert elem is not None

def test_button(driver):
  WAIT_SEC = 10
  driver.implicitly_wait(WAIT_SEC)

  btn = driver.find_element_by_accessibility_id('button')
  btn.click()
  btn.click()

  counter = driver.find_element_by_accessibility_id('counter')
  assert counter.text == '2'