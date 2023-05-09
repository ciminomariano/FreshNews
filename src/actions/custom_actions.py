import datetime
import time
import xlsxwriter
import re
import os
import requests
from RPA.Browser.Selenium import Selenium

from exceptions.custom_exceptions import CustomException, log_section_not_found, log_element_not_found
from exceptions.selenium_exceptions import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from datetime import datetime, timedelta


class CustomActions:
    def __init__(self, url):
        self.browser = Selenium()
        self.url = url

    def open_website(self, url):
        try:
            self.browser.open_available_browser(url)
            time.sleep(5)
            return True
        except NoSuchElementException:
            raise CustomException("We could not find any element at the page")
        except WebDriverException:
            raise CustomException("The page could not be loaded")

    def maximaze_nav(self):
        try:
            self.browser.maximize_browser_window()
            time.sleep(5)
            return True
        except Exception:
            raise CustomException("The Browser could not be Maximized")

    def accept_cookies(self):
        try:            
            time.sleep(5)

            boton_accept = self.browser.find_element('xpath://button[@data-testid="GDPR-accept"]')
            
            if boton_accept:
                boton_accept.click()
                print("Accept button Found, clicking on it")
                time.sleep(1)
                return True
        except Exception as e:
            raise CustomException("The element boton_aceppt from cookies"
                                  "was not found")

    def click_search_bar(self):
        try:
            
            search_button = self.browser.find_element('css:button[data-test-id="search-button"]')                                
            search_button.click()
            time.sleep(5)
            print("Search button found :), clicking on it")
            return True
        except TimeoutException as e:
            print("Search button not found")

    def write_search_term(self, term):
        try:
            search_input = self.browser.find_element('css:input[data-testid="search-input"]')
            time.sleep(3)
            search_input.send_keys(term)
            time.sleep(1)
            search_input.send_keys(Keys.ENTER)
            time.sleep(5)
            return True
        except TimeoutException:
            print("Time expired to find search input bar")

    def apply_categories(self, news_categories):
        try:
            
            section_button = self.browser.find_element('xpath://button[@data-testid="search-multiselect-button"]')                        
            section_button.click()
            time.sleep(5)
            print("Section button clicked")

            categories_xpath = {
                "arts": '//input[@type="checkbox" and @data-testid="DropdownLabelCheckbox" and @value="Arts|nyt://section/6e6ee292-b4bd-5006-a619-9ceab03524f2"]',                
                "books": '//input[@type="checkbox" and @data-testid="DropdownLabelCheckbox" and @value="Books|nyt://section/550f75e2-fc37-5d5c-9dd1-c665ac221b49"]',
                "business": '//input[@type="checkbox" and @value="Business|nyt://section/0415b2b0-513a-5e78-80da-21ab770cb753"]',
                "movies": '//input[@type="checkbox" and @data-testid="DropdownLabelCheckbox" and @value="Movies|nyt://section/62b3d471-4ae5-5ac2-836f-cb7ad531c4cb"]',
                "new york": '//input[@value="New York|nyt://section/39480374-66d3-5603-9ce1-58cfa12988e2"]',
                "opinion": '//input[@type="checkbox" and @data-testid="DropdownLabelCheckbox" and @value="Opinion|nyt://section/d7a71185-aa60-5635-bce0-5fab76c7c297"]',
                "sports": '//input[@value="Sports|nyt://section/4381411b-670f-5459-8277-b181485a19ec"]',
                "style": '//input[@data-testid="DropdownLabelCheckbox" and @value="Style|nyt://section/146e2c45-6586-59ef-bc23-90e88fe2cf0a"]',
                "magazine": '//input[@type="checkbox" and @data-testid="DropdownLabelCheckbox" and @value="Magazine|nyt://section/a913d1fb-3cdf-556b-9a81-f0b996a1a202"]',
                "u.s": '//input[@type="checkbox" and @data-testid="DropdownLabelCheckbox" and @value="U.S.|nyt://section/a34d3d6c-c77f-5931-b951-241b4e28681c"]',
                "technology": '//input[@value="Technology|nyt://section/4224240f-b1ab-50bd-881f-782d6a3bc527"]',
                "world": "//input[@data-testid='DropdownLabelCheckbox' and @value='World|nyt://section/70e865b6-cc70-5181-84c9-8368b3a5c34b']",
            }


            for category in news_categories:

                x_path = categories_xpath.get(category.lower())
                                

                if category == "ARTS":
                    try:                                                                                                
                        business_category = self.browser.find_element('xpath:' + x_path) 
                        business_category.click()
                        time.sleep(2)
                    except Exception as e:
                        log_section_not_found(category, e)

                elif category == "BOOKS":
                    try:
                        any_checkbox = self.browser.find_element('xpath:' + x_path) 
                        any_checkbox.click()
                        time.sleep(2)
                    except Exception as e:
                        log_section_not_found(category, e)

                elif category == "BUSINESS":
                    try:
                        business_category = self.browser.find_element('xpath:' + x_path) 
                        business_category.click()
                        time.sleep(2)
                    except Exception as e:
                        log_section_not_found(category, e)

                elif category == "MOVIES":
                    try:
                        business_category = self.browser.find_element('xpath:' + x_path) 
                        business_category.click()
                        time.sleep(2)
                    except Exception as e:
                        log_section_not_found(category, e)

                elif category == "NEW YORK":
                    try:
                        new_york_category = self.browser.find_element('xpath:' + x_path) 
                        new_york_category.click()
                        time.sleep(2)
                    except Exception as e:
                        log_section_not_found(category, e)

                elif category == "OPINION":
                    try:
                        new_york_category = self.browser.find_element('xpath:' + x_path) 
                        new_york_category.click()
                        time.sleep(2)
                    except Exception as e:
                        log_section_not_found(category, e)

                elif category == "SPORTS":
                    try:
                        sports_category = self.browser.find_element('xpath:' + x_path) 
                        sports_category.click()
                        time.sleep(2)
                    except Exception as e:
                        log_section_not_found(category, e)

                elif category == "STYLE":
                    try:
                        style_category = self.browser.find_element('xpath:' + x_path) 
                        style_category.click()
                        time.sleep(2)
                    except Exception as e:
                        log_section_not_found(category, e)

                elif category == "MAGAZINE":
                    try:
                        magazine_category = self.browser.find_element('xpath:' + x_path) 
                        magazine_category.click()
                        time.sleep(2)
                    except Exception as e:
                        log_section_not_found(category, e)

                elif category == "U.S":
                    try:
                        opinion_category = self.browser.find_element('xpath:' + x_path) 
                        opinion_category.click()
                        time.sleep(2)
                    except Exception as e:
                        log_section_not_found(category, e)

                elif category == "TECHNOLOGY":
                    try:
                        technology_category = self.browser.find_element('xpath:' + x_path) 
                        technology_category.click()
                        time.sleep(2)
                    except Exception as e:
                        log_section_not_found(category, e)

                elif category == "WORLD":
                    try:
                        technology_category = self.browser.find_element('xpath:' + x_path) 
                        technology_category.click()
                        time.sleep(2)
                    except Exception as e:
                        log_section_not_found(category, e)

        except TimeoutException:
            print("Time expired to find the button ")
        
        return True
            
    def apply_datetime(self, num_months):
        now = datetime.now()
        num_months = int(num_months)
        if num_months == 0:
            num_months = 1
        start_date = now - timedelta(days=30 * num_months - 1)
        start_date_str = start_date.strftime("%m/%d/%Y")
        end_date_str = now.strftime("%m/%d/%Y")

        # Clicking on the Filter Data Button
        try:                                    
            date_range_button = self.browser.find_element('css:button[data-testid="search-date-dropdown-a"]')
            date_range_button.click()   
            time.sleep(5)            
            print("range button found")
        except:
            print("Failed to click on date range button")

        # Clicking on the specific dates button
        try:
            specific_dates_button = self.browser.find_element("css:button[value='Specific Dates']")
            specific_dates_button.click()
            time.sleep(4)
            print("specific dates button found")
        except Exception as e:
            print("Failed to click on specific dates button")

        # Adding start date
        try:
            start_date_input = self.browser.find_element('id:startDate')
            start_date_input.clear()
            start_date_input.send_keys(start_date_str)
            time.sleep(10)
            print("Added start date")
        except:
            print("Failed to add start date")

        # Adding end date
        try:
            end_date_input = WebDriverWait(self.browser.driver, 10).until(EC.element_to_be_clickable((By.ID, "endDate")))
            end_date_input.clear()
            end_date_input.send_keys(end_date_str)
            end_date_input.send_keys(Keys.ENTER)
            time.sleep(5)
            print("Added end date")
        except Exception as e:
            print("Failed to add end date")

        return True
   
   
    def extract_articles(self, search_phrases):
        # Open the URL in a new browser window
        #url = self.browser.current_url
        #self.browser.open_available_browser(url)
        # Wait for the page to load        

        # Get all the articles on the page
        data = []
        for article in self.browser.find_elements('xpath:' +'//li[@data-testid="search-bodega-result"]'):
            try:
                # Get the article's title, date, description and image url
                #title = self.browser.find_element(By.XPATH, '//h4[@class="css-2fgx4k"]')
                #title = article.find_element('xpath:' + './/h4[@class="css-2fgx4k"]')
                title = article.find_element(by='xpath', value='.//h4[@class="css-2fgx4k"]')


                date = article.find_element(by='xpath', value='.//span[@data-testid="todays-date"]')
                description = article.find_element(by='xpath', value= './/p[@class="css-16nhkrn"]')
                image_url = article.find_element(by='xpath', value='.//img').get_attribute('src')
                image_name = image_url.split('/')[-1].split('?')[0]

                # Count search phrases in title
                title_count = 0
                if isinstance(search_phrases, str):
                    if search_phrases.lower() in title.text.lower():
                        title_count += 1
                else:
                    for phrase in search_phrases:
                        if phrase.lower() in title.text.lower():
                            title_count += 1

                # Count search phrases in description
                description_count = 0
                if isinstance(search_phrases, str):
                    if search_phrases.lower() in description.text.lower():
                        description_count += 1
                else:
                    for phrase in search_phrases:
                        if phrase.lower() in description.text.lower():
                            description_count += 1

                # Check if title or description contains any amount of money
                money_regex = r"\$?\d+(,\d{3})*(\.\d+)?( USD| dollars?)?"
                has_money = bool(re.search(money_regex, title.text + description.text))

                # Download the image and save it to the output directory
                output_dir = 'output/images'
                if not os.path.exists(output_dir):
                    os.makedirs(output_dir)
                image_path = os.path.join(output_dir, image_name)
                response = requests.get(image_url)
                with open(image_path, 'wb') as f:
                    f.write(response.content)


                article_data = {
                    'title': title.text,
                    'date': date.get_attribute('aria-label'),
                    'description': description.text,
                    'image_name': image_name,
                    'image_path': image_path,
                    'title_count': title_count,
                    'description_count': description_count,
                    'has_money': has_money
                }
                data.append(article_data)

            except Exception as e:
                # If any of the required elements are missing, skip the article
                continue

        # Close the browser window

        return data

    def write_to_excel(self,data):
        # Create a new workbook and add a worksheet
        os.makedirs('output/excel/', exist_ok=True)
        workbook = xlsxwriter.Workbook('output/excel/articles.xlsx')
        worksheet = workbook.add_worksheet()

        # Write the header row
        header = ['title', 'date', 'description', 'image_name','image_path','title_count','description_count','has_money']
        for col, heading in enumerate(header):
            worksheet.write(0, col, heading)

        # Write the data rows
        for row, article in enumerate(data):
            worksheet.write(row + 1, 0, article['title'])
            worksheet.write(row + 1, 1, article['date'])
            worksheet.write(row + 1, 2, article['description'])
            worksheet.write(row + 1, 3, article['image_name'])
            worksheet.write(row + 1, 4, article['image_path'].replace("\\", "/"))  # replace the path separator with a slash
            worksheet.write(row + 1, 5, article['title_count'])
            worksheet.write(row + 1, 6, article['description_count'])
            worksheet.write(row + 1, 7, article['has_money'])

        # Close the workbook
        workbook.close()
