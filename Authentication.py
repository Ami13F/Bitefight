from selenium.webdriver.common.by import By

import config


def login_player(driver):
    driver.find_element(By.XPATH, '/html/body/div[8]/div/div/span[2]/button[2]').click()
    username = driver.find_element(By.XPATH, '//*[@id="loginForm"]/table/tbody/tr[1]/td[2]/input')
    username.send_keys(config.username)
    password = driver.find_element(By.XPATH, '//*[@id="loginForm"]/table/tbody/tr[2]/td[2]/input')
    password.send_keys(config.password)
    login = driver.find_element(By.XPATH, '//*[@id="loginForm"]/table/tbody/tr[4]/td[2]/input')
    login.click()
