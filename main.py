from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from datetime import datetime
import time


options = Options()
options.add_argument("--headless")

def app_test():
    url = 'https://www.kodhit.com/vote/2022'

    driver = webdriver.Firefox(options=options)
    driver.get(url)
    print(driver.title)
    time.sleep(5)

    elements = driver.find_elements(By.CSS_SELECTOR, ".hvr-reveal")
    for element in elements:
        print(element.text)
        if element.text == "Extraordinary Attorney Woo":
            driver.execute_script("arguments[0].click();", element)
            break
    time.sleep(2)

    button_element = driver.find_element(By.CSS_SELECTOR, ".v-btn--large")
    # button_element.click()
    driver.execute_script("arguments[0].click();", button_element)
    time.sleep(2)

    buttons = driver.find_elements(By.CSS_SELECTOR, ".v-btn__content")
    for button in buttons:
        print(button.text)
        if button.text == "ยืนยัน":
            driver.execute_script("arguments[0].click();", button)
            break
    time.sleep(10)
    driver.quit()

if __name__ == '__main__':
    start_time = datetime.now()
    print('Time start:', str(start_time))
    app_test()
    end_time = datetime.now()
    print('Time end:', str(end_time))
    print('Time difference:', str(end_time - start_time))
