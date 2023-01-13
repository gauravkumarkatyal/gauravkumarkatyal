from selenium import webdriver
import os
import pandas
import requests
from selenium.webdriver.common.by import By

driver=webdriver.Chrome(executable_path='./chromedriver_win32/chromedriver.exe')

def get_diseases():
    driver.get('https://dermnetnz.org/image-library')
    diseases = driver.find_elements(By.XPATH, '//a[@class="imageList__group__item"]')
    records=[]
    for disease in diseases:
        raw={
            'link':disease.get_attribute('href'),
            'name':disease.find_element(By.XPATH, './/div[@class="imageList__group__item__copy"]//h6').text,
            'imageUrl': disease.find_element(By.XPATH, './/div[@class="imageList__group__item__image"]//img').get_attribute('src'),

        }
        
        records.append(raw)
    return records

def create_folder(folder_name):
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

def download_images(folder_name, records):
    create_folder(folder_name)
    for record in records:
        icon_name = record["imageUrl"].split("/")[-1]
        with open(f"{folder_name}/{icon_name}", "wb") as icon_file:
            icon_file.write(requests.get(record["imageUrl"]).content)
        print(record["imageUrl"])
        record["icon_path"] = f"{folder_name}/{icon_name}"


def save_into_csv(records):
    output = pandas.DataFrame(records)
    output.to_csv('dermnetnz.csv', index=False)

def main():
    folder_name = "icons"
    records = get_diseases()
    download_images(folder_name, records)
    save_into_csv(records)
    driver.quit()

main()