import csv
import json
import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

states_list = []
with open("states.json", "r") as file:
    states_list = json.load(file)
    states_list.sort(reverse=True)

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--no-sandbox")
service = ChromeService(executable_path="./chromedriver.exe")

driver = webdriver.Chrome(service=service, options=chrome_options)
wait = WebDriverWait(driver, 10)

try:
    for state in states_list:
        print(f"Running for {state} state")
        start_url = f"https://www.greatschools.org/{state}/schools/?gradeLevels%5B%5D=h&page="

        school_links = set()
        page_num = 1
        while True:
            url = start_url + str(page_num)
            try:
                driver.get(url)
                wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "a.name")))
                soup = BeautifulSoup(driver.page_source, "html.parser")

                for a in soup.body.select("a.name[href]"):
                    school_links.add("https://www.greatschools.org" + a["href"])

                pagination_container = soup.find("div", class_="pagination-container")
                if pagination_container:
                    chevron_right_spans = pagination_container.find_all("span", class_="icon-chevron-right")
                    
                    if len(chevron_right_spans) >= 2:
                        next_button_span = chevron_right_spans[1]
                        next_button = next_button_span.find_parent("a", class_="anchor-button")
                        if next_button:
                            if "disabled" in next_button.get("class", []) and not next_button.get("href"):
                                break
                            else:
                                page_num += 1
                else:
                    print("Couldn't find the pagination container.")
                    break

            except Exception as e:
                print(f"Error encountered for {url}. Error: {e}")
                page_num += 1
                continue

        for link in school_links:
            print(f"Running for {link} school")
            try:
                driver.get(link)
                wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "a[href*='mailto:']")))
                soup = BeautifulSoup(driver.page_source, "html.parser")

                mailto_links = soup.select("a[href*='mailto:']")
                school_leader_name = (soup.select_one("span.school-leader").get_text(strip=True) if soup.select_one("span.school-leader") else "N/A")
                school_name = (soup.select_one("title").get_text(strip=True) if soup.select_one("title") else "N/A")

                with open("us_school_emails.csv", "a", newline="", encoding="utf-8") as file:
                    writer = csv.writer(file)
                    for mailto_link in mailto_links:
                        email_address = mailto_link.get("href").replace("mailto:", "")
                        writer.writerow([state, link, school_name, school_leader_name, email_address])
            except Exception as e:
                print(f"Failed to connect to {link}. Error: {e}")
                time.sleep(2)

finally:
    driver.quit()
