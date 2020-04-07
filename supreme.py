from selenium import webdriver
from selenium.webdriver.support.ui import Select
from time import sleep

class supremeBot:
    def __init__(self, size, quantity, name, email, number, address, zip, state, country, credit, month, year, cvv):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.supremenewyork.com/shop/all")
        # sleep(1)

        #Select Product you want
        #Sleep required here
        self.driver.find_element_by_xpath('/html/body/div[2]/ul/li[187]/div/a').click()
        sleep(1)

        #Select size of product
        sizeDropDown = self.driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/form/fieldset[1]/select')
        sizeOptions = Select(sizeDropDown)
        sizeOptions.select_by_visible_text(size)
        # sleep(1)

        #Select quantity of product(if there is an option)
        quantityDropDown = self.driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/form/fieldset[2]/select')
        quantityOptions = Select(quantityDropDown)
        quantityOptions.select_by_value(quantity)
        # sleep(1)

        #Click add to cart and checkout
        #Sleep required here
        self.driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/form/fieldset[3]/input').click()
        sleep(1)
        self.driver.find_element_by_xpath('/html/body/div[2]/div/div[1]/div/a[2]').click()
        sleep(1)

        #Input billing and credit card info
        self.driver.find_element_by_xpath("/html/body/div[2]/div[1]/form/div[2]/div[1]/fieldset/div[1]/input")\
            .send_keys(name)
        # sleep(1)

        self.driver.find_element_by_xpath("/html/body/div[2]/div[1]/form/div[2]/div[1]/fieldset/div[2]/input")\
            .send_keys(email)
        # sleep(1)

        self.driver.find_element_by_xpath("/html/body/div[2]/div[1]/form/div[2]/div[1]/fieldset/div[3]/input")\
            .send_keys(number)
        # sleep(1)

        self.driver.find_element_by_xpath("/html/body/div[2]/div[1]/form/div[2]/div[1]/fieldset/div[4]/div[1]/input")\
            .send_keys(address)
        # sleep(1)

        self.driver.find_element_by_xpath("/html/body/div[2]/div[1]/form/div[2]/div[1]/fieldset/div[5]/div[1]/input")\
            .send_keys(zip)
        # sleep(1)

        # self.driver.find_element_by_xpath("/html/body/div[2]/div[1]/form/div[2]/div[1]/fieldset/div[5]/div[2]/input")\
        #     .send_keys(city)
        # sleep(1)

        stateDropDown = self.driver.find_element_by_xpath("/html/body/div[2]/div[1]/form/div[2]/div[1]/fieldset/div[5]/div[3]/select")
        stateOptions = Select(stateDropDown)
        stateOptions.select_by_visible_text(state)

        # sleep(1)

        countryDropdown = self.driver.find_element_by_xpath("/html/body/div[2]/div[1]/form/div[2]/div[1]/fieldset/div[6]/select")
        countryOptions = Select(countryDropdown)
        countryOptions.select_by_visible_text(country)
        sleep(5)

        self.driver.find_element_by_xpath("/html/body/div[2]/div[1]/form/div[2]/div[2]/fieldset/div[1]/div[2]/input")\
            .send_keys(credit)
        # sleep(1)

        monthDropDown = self.driver.find_element_by_xpath("/html/body/div[2]/div[1]/form/div[2]/div[2]/fieldset/div[1]/div[3]/div[1]/select[1]")
        monthOptions = Select(monthDropDown)
        monthOptions.select_by_visible_text(month)
        # sleep(1)

        yearDropDown = self.driver.find_element_by_xpath("/html/body/div[2]/div[1]/form/div[2]/div[2]/fieldset/div[1]/div[3]/div[1]/select[2]")
        yearOptions = Select(yearDropDown)
        yearOptions.select_by_visible_text(year)
        # sleep(1)

        self.driver.find_element_by_xpath("/html/body/div[2]/div[1]/form/div[2]/div[2]/fieldset/div[1]/div[3]/div[2]/input")\
            .send_keys(cvv)
        # sleep(1)

        #Check Terms and Agreement and Process Payment
        self.driver.find_element_by_xpath("/html/body/div[2]/div[1]/form/div[2]/div[2]/fieldset/p[2]/label/div/ins").click()
        # sleep(1)

        self.driver.find_element_by_xpath("/html/body/div[2]/div[1]/form/div[3]/div[2]/input").click()
        # sleep(1)


supremeBot("Medium", "2",
    "test", "test@gmail.com", "7181234567", "test street", "90210", "CA", "USA",
    "1234123412341234", "05", "2025", "123")
