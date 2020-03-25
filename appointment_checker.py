import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.action_chains import ActionChains
# select date range
# go to website
# click on book now
# select service
# check for "free" day
# select next arrow if none
# go until hit last date in range

def search_for_appointment(date_range_start, date_range_end, months):

    driver.get("http://miaminbeauty.com/#book-online")

    element = driver.find_element_by_name("service")
    element.click()

    all_options = element.find_elements_by_tag_name("option")
    for option in all_options:
        if option.get_attribute("value") == "1":
            option.click()

    for x in range(date_range_start, date_range_end+1):
        calendar = driver.find_element_by_class_name("ui-datepicker-calendar")
        days = calendar.find_elements_by_tag_name("td")
        for day in days:
            if "free" in day.get_attribute("class"):
                return(day.get_attribute("class"))

        next_month = driver.find_element_by_class_name("ui-datepicker-next")
        driver.get("http://miaminbeauty.com/#book-online")
        time.sleep(2)
        next_month.click()
    
    return None

if __name__ == "__main__":
    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July',
          'August', 'September', 'October', 'November', 'December']

    date_range_start = 5
    date_range_end = 9

    driver = webdriver.Chrome('/Users/ashleytaylor/Downloads/chromedriver')
    #driver = webdriver.Remote(
    #   command_executor='http://127.0.0.1:4444/wd/hub',
    #   desired_capabilities=DesiredCapabilities.CHROME)

    availability = search_for_appointment(date_range_start, date_range_end, months)
    if availability:
        print(availability)