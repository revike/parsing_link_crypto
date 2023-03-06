from time import sleep

from selenium.common import ElementClickInterceptedException, NoSuchElementException
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from settings import driver, url, time_sleep, file
from work_json import write_active_json


def get_page_now(web_driver):
    result = web_driver.find_element(
        By.CSS_SELECTOR, '#coinlist_paginate > ul > li.paginate_button.page-item.active').text
    return int(result)


driver.get(url)
sleep(time_sleep)

data = {}

i = 1
page = 1
page_now = 1
next_page = True

while True:
    try:
        if f'{page}' != f'{page_now}':
            driver.find_element(By.CLASS_NAME, 'next').click()
            sleep(time_sleep)
            page_now += 1
            continue
        driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.HOME)
        sleep(time_sleep)
        driver.find_element(By.XPATH, f'//*[@id="coinlist"]/tbody/tr[{i}]/td[1]').click()
        url_active = driver.current_url
        name_active = driver.find_element(By.TAG_NAME, 'h6').find_element(By.TAG_NAME, 'span').text
        data[name_active[1:-1]] = url_active
        driver.back()
        sleep(time_sleep)
        driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.END)
        sleep(time_sleep)
        page_now = get_page_now(driver)
        sleep(time_sleep)
        driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.HOME)
        sleep(time_sleep)
        i += 1
    except ElementClickInterceptedException:
        driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.END)
        sleep(time_sleep)
    except NoSuchElementException:
        write_active_json(file, data)
        driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.END)
        sleep(time_sleep)
        data = {}
        driver.find_element(By.CLASS_NAME, 'next').click()
        sleep(time_sleep)
        page_now = get_page_now(driver)
        page += 1
        sleep(time_sleep)
        driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.HOME)
        i = 1
        sleep(time_sleep)
