import csv
from time import sleep

from selenium.webdriver import Firefox
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = Firefox()
driver.get('https://www.google.com/')
sleep(1)
driver.find_element("xpath", '/html/body/div[2]/div[2]/div[3]/span/div/div/div/div[3]/div[1]/button[1]').click()


def recherche(driver_in_fonction):
    search = "cybersecurity"

    search_input = driver_in_fonction.find_element("xpath", '//input[@aria-label="Rech."]')
    search_input.send_keys(search)

    search_input.send_keys(Keys.RETURN)

# /html/body/div[7]/div/div[11]/div[1]/div[1]/div[2]/div/div[1]/div/div/div/div[1]/a/div[2]/span[2] # c'est le link
# /html/body/div[7]/div/div[11]/div[1]/div[1]/div[2]/div/div[1]/div/div/div/div[1]/a/div[1]/span #le titre du site
# /html/body/div[2]/div[2]/div[3]/span/div/div/div/div[3]/div[1]/button[1]/div

def data(post_in_fonction):
    titre = post_in_fonction.find_element("xpath", ".//h3").text    #probleme ca trouve pas les titres   #div/div/div[1]/div/a/h3
    #link = post_in_fonction.find_element(By.TAG_NAME, "cite").text    #div/div/div[1]/div/a/div/cite
    link = post_in_fonction.find_element("xpath", ".//a").get_attribute('href')

    article = (titre, link)
    return article

#/html/body/div[7]/div/div[11]/div[1]/div[2]/div[2]/div/div/div[4]/div/div/div[1]/div/a/h3 # sur la page 1
#/html/body/div[7]/div/div[11]/div/div[2]/div[2]/div/div/div[1]/div/div/div[1]/div/a/h3 # sur les autres pages

#/html/body/div[7]/div/div[11]/div[1]/div[2]/div[2]/div/div/div[4]/div/div/div[1]/div/a/div/cite
#/html/body/div[7]/div/div[11]/div/div[2]/div[2]/div/div/div[1]/div/div/div[1]/div/a/div/cite

#/html/body/div[7]/div/div[11]/div/div[5]

#/html/body/div[7]/div/div[11]/div/div[2]/div[2]/div/div/div[1]
#/html/body/div[7]/div/div[11]/div/div[2]/div[2]/div/div




recherche(driver)

site_data = []
site_ids = set()
action = True
max_site = 200
nb_of_site = 50
while nb_of_site > max_site:  # pas plus de 200 sites
    nb_of_site = max_site

#/html/body/div[7]/div/div[11]/div/div[2]/div[2]/div/div/div[2]/div/div/div[1]/div/a/div/cite

while action:
    sleep(1)
    driver.find_element("xpath", '/html/body/div[7]/div/div[11]/div[1]/div[4]/div/div[2]/table/tbody/tr/td[12]/a/span[1]').click()  # /html/body/div[7]/div/div[11]/div[1]/div[4]/div/div[2]/table/tbody/tr/td[12]/a/span[1]

    tags = driver.find_elements("xpath", '/html/body/div[7]/div/div[11]/div/div[2]/div[2]/div/div/div')
    sleep(1)
    for site in tags:

        datas = data(site)
        if datas:
            site_id = ''.join(datas)
            if site_id not in site_ids:
                site_ids.add(site_id)
                site_data.append(datas)
                if len(site_data) > nb_of_site:
                    action = False
                    break
    while action:
        driver.find_element("xpath", '/html/body/div[7]/div/div[11]/div[1]/div[4]/div/div[2]/table/tbody/tr/td[12]/a/span[1]').click()  #/html/body/div[7]/div/div[11]/div[1]/div[4]/div/div[2]/table/tbody/tr/td[12]/a/span[1]
        #/html/body/div[7]/div/div[11]/div/div[4]/div/div[2]/table/tbody/tr/td[12]/a/span[2]
        sleep(1)
        break

with open("cybersecurity2.csv", "w", newline='', encoding='utf-8') as f:
    entete = ["titre", "url"]
    writer = csv.writer(f)
    writer.writerow(entete)
    writer.writerows(site_data)
