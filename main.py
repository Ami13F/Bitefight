import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from AttachType import AttachType
from Authentication import login_player


def have_energy(text: str):
    return int(text.split(" ")[0]) >= 4


def attack(attach_type: AttachType):
    time.sleep(1)
    if attach_type == AttachType.METROPOLIS:
        driver.find_element(By.XPATH,
                            '//*[@id="humanHuntResult"]/div[5]/div[2]/table/tbody/tr/td[2]/div/div/button').click()
    elif attach_type == AttachType.FARM:
        driver.find_element(By.XPATH,
                            '//*[@id="humanHuntResult"]/div[1]/div[2]/table/tbody/tr/td[2]/div/div/button').click()

    back = driver.find_element(By.CLASS_NAME, 'btn-right')
    back.click()


with webdriver.Opera() as driver:
    wait = WebDriverWait(driver, 10)
    driver.get("https://s102-ro.bitefight.gameforge.com/user/login")
    driver.maximize_window()
    login_player(driver)

    el = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Raid")))
    el.click()
    el = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Vânătoare de oameni")))
    el.click()
    energy = driver.find_element(By.XPATH, '//*[@id="infobar_energy"]/div[3]')

    while have_energy(energy.text):
        attack(AttachType.METROPOLIS)
        energy = driver.find_element(By.XPATH, '//*[@id="infobar_energy"]/div[3]')

    print("War complete! Good job")
