from time import sleep

from selenium.common import NoSuchElementException, StaleElementReferenceException, InvalidArgumentException
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from settings import driver, url, file
from work_json import write_active_json, read_json


def get_page_now(web_driver):
    selector = '#coinlist_paginate > ul > li.paginate_button.page-item.active'
    while True:
        if search_element(web_driver, selector):
            result = web_driver.find_element(By.CSS_SELECTOR, selector).text
            break
        else:
            pass
    return int(result)


def search_element(web_driver, selector):
    try:
        web_driver.find_element(By.CSS_SELECTOR, selector)
        return True
    except (NoSuchElementException, StaleElementReferenceException, InvalidArgumentException):
        return False


def get_active_name(page=0, page_now=1, data=None):
    driver.get(url)
    if data is None:
        data = {}
    while True:
        if page > page_now:
            break
        actives_odd = driver.find_elements(By.CLASS_NAME, 'odd')
        actives_even = driver.find_elements(By.CLASS_NAME, 'even')
        actives = actives_odd + actives_even
        driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.END)
        for active in actives:
            text = active.text
            if text:
                art_active = ''.join(active.text.split('\n')[0]).split()[-1]
                name_active = ' '.join(''.join(active.text.split('\n')[0]).split()[:-1])
                data[art_active] = {name_active: None}
        write_active_json(file, data)
        data = {}
        page_now = get_page_now(driver)
        driver.find_element(By.CLASS_NAME, 'next').click()
        sleep(2)
        page += 1
    return True


def get_link_active():
    i = 0
    data = read_json(file)
    for key, value in data.items():
        for active_name in value:
            driver.get(url)
            search = driver.find_element(By.CLASS_NAME, 'search_0')
            sleep(1)
            search.send_keys(active_name)
            sleep(1)
            active = driver.find_elements(By.CLASS_NAME, 'odd')[0]
            while True:
                active_text = ' '.join(''.join(active.text.split('\n')[0]).split()[:-1])
                if active_text != active_name:
                    sleep(.2)
                    continue
                active.click()
                break
            link_active = driver.current_url
            result = {active_name: link_active}
            data[key] = result
        if i % 10 == 0:
            write_active_json(file, data)
            data = {}
        i += 1


if __name__ == '__main__':
    get_active_name()
    get_link_active()
