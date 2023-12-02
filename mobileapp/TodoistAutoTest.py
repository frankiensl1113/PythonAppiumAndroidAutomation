import time
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.touch_action import TouchAction
from selenium.common import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from TodoistAction import TodoistAction

todoist_action = TodoistAction()

task_name = "New Task"
project_name = "ProjectAlpha"
desired_id = None

capabilities = dict(
    platformName='Android',
    deviceName='emulator-5554',
    appPackage='com.todoist',
    appActivity='com.todoist.activity.HomeActivity',
    noReset=False
)

capabilities_noreset = dict(
    platformName='Android',
    deviceName='emulator-5554',
    appPackage='com.todoist',
    appActivity='com.todoist.activity.HomeActivity',
    noReset=True
)
# Create
projectresponse = todoist_action.add_project(project_name)

appium_server_url = 'http://localhost:4723'

capabilities_options = UiAutomator2Options().load_capabilities(capabilities)

driver = webdriver.Remote(command_executor=appium_server_url, options=capabilities_options)

wait = WebDriverWait(driver, 10)

signin_options = driver.find_element(by=AppiumBy.XPATH,
                                     value='//android.widget.TextView[@resource-id="com.todoist:id/more_signin_options"]')
signin_options.click()

email_login = wait.until(EC.visibility_of_element_located(
    (By.XPATH, '//android.widget.TextView[@resource-id="com.todoist:id/email_login"]')))
email_login.click()

email_address = wait.until(
    EC.visibility_of_element_located((By.XPATH, '//android.widget.EditText[@resource-id="email"]')))
email_address.clear()
email_address.send_keys('apple_001831.3fbdadf57cb4450b9e08bc947dc32fee.0933@users.todoist.com')

password = driver.find_element(by=AppiumBy.XPATH, value='//android.widget.EditText[@resource-id="password"]')
password.clear()
password.send_keys('Ab@12345678')

login_btn = wait.until(
    EC.visibility_of_element_located((By.XPATH, '//android.view.View[@resource-id="auth_button_tag"]')))
login_btn.click()

time.sleep(5)

# Bottom Left menu button
menu_btn = wait.until(
    EC.visibility_of_element_located((By.XPATH, '//android.widget.ImageButton[@content-desc="Menu"]')))
menu_btn.click()

# Get screen size
screen_size = driver.get_window_size()
screen_width = screen_size['width']
screen_height = screen_size['height']

# Define start and end coordinates for the swipe gesture
start_x = screen_width // 2
start_y = screen_height - 100
end_x = screen_width // 2
end_y = screen_height // 2

# Perform the swipe gesture to bring up the dynamic relative layout and the list.
driver.swipe(start_x, start_y, end_x, end_y, duration=800)

# Check whether the ProjectAlpha exist by checking the Project button
try:
    project_btn = wait.until(
        EC.visibility_of_element_located((By.XPATH, '//android.widget.TextView[@text="ProjectAlpha"]')))
    assert project_btn is not None
    print("ProjectAlpha Button Created in the android app: PASS")
except TimeoutException:
    print("ProjectAlpha Button Not exist: FAIL")

# Click the Project
btn_project = wait.until(
    EC.visibility_of_element_located((By.XPATH, '//android.widget.TextView[@text="ProjectAlpha"]')))
btn_project.click()

# Click the + button
btn_add = wait.until(
    EC.visibility_of_element_located((By.XPATH, '//android.widget.ImageButton[@content-desc="Quick add"]')))
btn_add.click()

# Click the edittext space and fill in the task name
edittext_message = wait.until(
    EC.visibility_of_element_located((By.XPATH, '//android.widget.EditText[@resource-id="android:id/message"]')))
edittext_message.clear()
edittext_message.send_keys(task_name)

# Click the send button
btn_send = wait.until(EC.visibility_of_element_located((By.XPATH, '//android.widget.ImageView[@content-desc="Add"]')))
btn_send.click()

driver.hide_keyboard()

screen_size = driver.get_window_size()

# Calculate the center coordinates
center_x = screen_size['width'] / 2
center_y = screen_size['height'] / 2

# Perform a tap action at the center of the screen
action = TouchAction(driver)
action.tap(x=center_x, y=center_y).perform()

# Obtain list of active tasks
response = todoist_action.get_active_task()

desired_content = task_name

for task in response:
    if task.content == desired_content:
        desired_id = task.id
        break

if desired_id is not None:
    print(f"Verified the created task with content '{desired_content}': {desired_id} in the API response: PASS")
else:
    print(f"No task found with content '{desired_content}'")

driver.quit()

capabilities_options = UiAutomator2Options().load_capabilities(capabilities_noreset)

print("Restart Todoist App")
driver = webdriver.Remote(command_executor=appium_server_url, options=capabilities_options)

wait = WebDriverWait(driver, 10)


btn_browse = wait.until(EC.visibility_of_element_located((By.XPATH, '//android.widget.TextView[@text="Browse"]')))
btn_browse.click()

print("Open test project ProjectAlpha")
btn_projectalpha = wait.until(
    EC.visibility_of_element_located((By.XPATH, '//android.widget.TextView[@text="ProjectAlpha"]')))
btn_projectalpha.click()

print("Complete test task New Task")
btn_projectalpha_complete = wait.until(
    EC.visibility_of_element_located((By.XPATH, '//android.widget.CheckBox[@content-desc="Complete"]')))
btn_projectalpha_complete.click()

print("Reopen test task via API.")
# print(desired_id)
response = todoist_action.reopen_task(desired_id)

time.sleep(10)

btn_browse = wait.until(EC.visibility_of_element_located((By.XPATH, '//android.widget.TextView[@text="Browse"]')))
btn_browse.click()

btn_projectalpha = wait.until(
    EC.visibility_of_element_located((By.XPATH, '//android.widget.TextView[@text="ProjectAlpha"]')))
btn_projectalpha.click()

try:
    textview_new_task = wait.until(
        EC.visibility_of_element_located((By.XPATH, '//android.widget.TextView[@resource-id="com.todoist:id/text"]')))
    textview_content = textview_new_task.text

    if textview_content == task_name:
        print(f"Verified Reopen Task: Success ")
    else:
        print(f"Reopen Task: FAIL ")

    print("Complete the task to keep record clean for next run.")
    # Complete the task to keep record clean for next run.
    btn_projectalpha_complete = wait.until(
        EC.visibility_of_element_located((By.XPATH, '//android.widget.CheckBox[@content-desc="Complete"]')))
    btn_projectalpha_complete.click()

except TimeoutException:
    print("Reopen task API is called")
    print("Task is not created in the android device due to todoist side issue: FAIL")

driver.quit()
