# Define a main() function that calls the other functions in order:
from actions import CustomActions
from constants.constants_names import URLNYTIMES
from exceptions import CustomException
from constants import constants_names
import configparser
import os
import logging

# Creating folder for logs ig does not exists
if not os.path.exists("output/logs"):
    os.makedirs("output/logs")
logging.basicConfig(filename='output/logs/trace-robot.log', level=logging.ERROR)
# Taking initial configuration from config file
config = configparser.ConfigParser()
config.read('src/config.ini')
# Reading parameters from the file
search_phrase = config.get('search', 'SEARCH_PHRASE')
news_categories = config.get('search', 'CATEGORY').split(',')
news_categories = [category.upper() for category in news_categories]

# checking search phrase is not empty
if not search_phrase:
    search_phrase = " "
# Getting number of months to filter by data
num_months = config.get('search', 'NUMBER_OF_MONTHS')

#Intiliazing the robot
def main():
    # Create an instance of my custom actions class
    custom_actions = CustomActions(URLNYTIMES)
    try:
    # Execute the function to open the web site
        if custom_actions.open_website(constants_names.URLNYTIMES):
            if custom_actions.maximaze_nav():
                # Accept the cookies
                if custom_actions.accept_cookies():
                    # Click on search bar
                    if custom_actions.click_search_bar():
                        # Enter the search phrase imported from config file
                        if custom_actions.write_search_term(search_phrase):
                            # Apply the date filters also imported from config file
                            if custom_actions.apply_datetime(num_months):
                            # Apply the filter categories from the list in config file
                            # (categories MUST BE separated by coma
                            # example Books,Business,Movies,New York,Opinion )
                                if custom_actions.apply_categories(news_categories):
                            # Call to the function where we extract the info
                            #of the articles
                                    articles = custom_actions.extract_articles(search_phrase)
                            #Save the excel file with the info of the web site
                                    if custom_actions.write_to_excel(articles):
                                        print("Excel file exported")
    except Exception as e:
        logging.error(f"An exception occurred: {e}")
 
# Call the main() function, checking that we are running as a stand-alone script:
if __name__ == "__main__":
    main()
