from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from decimal import Decimal



class CraigslistScraper(object):

    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=r"./chromedriver")

    #
    # Victoria
    #

    def scrape(self):
        self.driver.get('https://victoria.craigslist.ca/')

        cash = 0
        count = 0 
        options = self.driver.find_element_by_id('hhh0')
        # hack to get all the <li> elements
        options = options.find_elements_by_css_selector('*')
        target = options[0]
        target.click()

        dropdown = self.driver.find_element_by_name("min_bedrooms")
        for option in dropdown.find_elements_by_tag_name('option'):
            if option.text == '1':
                option.click() 
                break

        dropdown = self.driver.find_element_by_name("max_bedrooms")
        for option in dropdown.find_elements_by_tag_name('option'):
            if option.text == '1':
                option.click() 
                break

        titles = self.driver.find_elements_by_class_name('result-title')
        prices = self.driver.find_elements_by_class_name('result-price')
        

        for title, price in zip(titles, prices):
            results = (title.text, price.text) 
            dollars_dec = int(price.text[1:])
            cash = cash + dollars_dec
            if(dollars_dec != 0):
                count = count + 1


        #
        # 2 bedroom
        #
        self.driver.get('https://victoria.craigslist.ca/')

        options2 = self.driver.find_element_by_id('hhh0')
        # hack to get all the <li> elements
        options2 = options2.find_elements_by_css_selector('*')
        target2 = options2[0]
        target2.click()

        cash2 = 0
        count2 = 0 
        dropdown2 = self.driver.find_element_by_name("min_bedrooms")
        for option in dropdown2.find_elements_by_tag_name('option'):
            if option.text == '2':
                option.click() 
                break

        dropdown2 = self.driver.find_element_by_name("max_bedrooms")
        for option in dropdown2.find_elements_by_tag_name('option'):
            if option.text == '2':
                option.click() 
                break

        titles2 = self.driver.find_elements_by_class_name('result-title')
        prices2 = self.driver.find_elements_by_class_name('result-price')
        

        for title, price in zip(titles2, prices2):
            results2 = (title.text, price.text) 
            dollars_dec2 = int(price.text[1:])
            cash2 = cash2 + dollars_dec2
            if(dollars_dec2 != 0):
                count2 = count2 + 1

        

        #
        # 3 bedroom
        #
        self.driver.get('https://victoria.craigslist.ca/')

        options3 = self.driver.find_element_by_id('hhh0')
        # hack to get all the <li> elements
        options3 = options3.find_elements_by_css_selector('*')
        target3 = options3[0]
        target3.click()

        cash3 = 0
        count3 = 0 

        dropdown3 = self.driver.find_element_by_name("min_bedrooms")
        for option in dropdown3.find_elements_by_tag_name('option'):
            if option.text == '3':
                option.click() 
                break

        dropdown3 = self.driver.find_element_by_name("max_bedrooms")
        for option in dropdown3.find_elements_by_tag_name('option'):
            if option.text == '3':
                option.click() 
                break

        titles3 = self.driver.find_elements_by_class_name('result-title')
        prices3 = self.driver.find_elements_by_class_name('result-price')
        

        for title, price in zip(titles3, prices3):
            results3 = (title.text, price.text) 
            dollars_dec3 = int(price.text[1:])
            cash3 = cash3 + dollars_dec3
            if(dollars_dec3 != 0):
                count3 = count3 + 1


        #
        # 4 bedroom
        #
        self.driver.get('https://victoria.craigslist.ca/')

        options4 = self.driver.find_element_by_id('hhh0')
        # hack to get all the <li> elements
        options4 = options4.find_elements_by_css_selector('*')
        target4 = options4[0]
        target4.click()

        cash4 = 0
        count4 = 0 

        dropdown4 = self.driver.find_element_by_name("min_bedrooms")
        for option in dropdown4.find_elements_by_tag_name('option'):
            if option.text == '4':
                option.click() 
                break

        dropdown4 = self.driver.find_element_by_name("max_bedrooms")
        for option in dropdown4.find_elements_by_tag_name('option'):
            if option.text == '4':
                option.click() 
                break

        titles4 = self.driver.find_elements_by_class_name('result-title')
        prices4 = self.driver.find_elements_by_class_name('result-price')
        

        for title, price in zip(titles4, prices4):
            results4 = (title.text, price.text) 
            dollars_dec4 = int(price.text[1:])
            cash4 = cash4 + dollars_dec4
            if(dollars_dec4 != 0):
                count4 = count4 + 1


                #
        # 5bedroom
        #
        self.driver.get('https://victoria.craigslist.ca/')

        options5 = self.driver.find_element_by_id('hhh0')
        # hack to get all the <li> elements
        options5 = options5.find_elements_by_css_selector('*')
        target5 = options5[0]
        target5.click()

        cash5 = 0
        count5 = 0 

        dropdown5 = self.driver.find_element_by_name("min_bedrooms")
        for option in dropdown5.find_elements_by_tag_name('option'):
            if option.text == '5':
                option.click() 
                break

        dropdown5 = self.driver.find_element_by_name("max_bedrooms")
        for option in dropdown5.find_elements_by_tag_name('option'):
            if option.text == '5':
                option.click() 
                break

        titles5 = self.driver.find_elements_by_class_name('result-title')
        prices5 = self.driver.find_elements_by_class_name('result-price')
        

        for title, price in zip(titles5, prices5):
            results5 = (title.text, price.text) 
            dollars_dec5 = int(price.text[1:])
            cash5 = cash5 + dollars_dec5
            if(dollars_dec5 != 0):
                count5 = count5 + 1


        with open('craigslist-page1-housing-stats.txt', 'w') as f:
           #f.write(str(results))
            f.write("average 1 bedroom price in Victoria: " + str(cash/count) + "\n")
            f.write("average 2 bedroom price in Victoria: " + str(cash2/count2) + "\n")
            f.write("average 3 bedroom price in Victoria: " + str(cash3/count3)+ "\n")
            f.write("average 4 bedroom price in Victoria: " + str(cash4/count4)+ "\n")
            f.write("average 5 bedroom price in Victoria: " + str(cash5/count5)+ "\n")
            #f.write("average three bedroom price in Vancouver: " + str(cash1/count1))

        with open('vic_housing_data.csv', 'w') as f:
           #f.write(str(results))
            f.write("Bedroom," + "Price" + "\n")
            f.write("1," + str(cash/count) + "\n")
            f.write("2," + str(cash2/count2) + "\n")
            f.write("3," + str(cash3/count3)+ "\n")
            f.write("4," + str(cash4/count4)+ "\n")
            f.write("5," + str(cash5/count5)+ "\n")

    #
    # Vancouver
    #
    '''def scrapeVan(self):

        self.driver.get('https://vancouver.craigslist.ca/')

        cash1 = 0
        count1 = 0 
        options1 = self.driver.find_element_by_id('hhh0')
        # hack to get all the <li> elements
        options1 = options1.find_elements_by_css_selector('*')
        target1 = options1[0]
        target1.click()

        dropdown1 = self.driver.find_element_by_name("min_bedrooms")
        for option in dropdown1.find_elements_by_tag_name('option'):
            if option.text == '3':
                option.click() 
                break

        dropdown1 = self.driver.find_element_by_name("max_bedrooms")
        for option in dropdown1.find_elements_by_tag_name('option'):
            if option.text == '3':
                option.click() 
                break

        titles1 = self.driver.find_elements_by_class_name('result-title')
        prices1 = self.driver.find_elements_by_class_name('result-price')
        

        for title, price in zip(titles1, prices1):
            results1 = (title.text, price.text) 
            dollars_dec1 = int(price.text[1:])
            cash1 = cash1 + dollars_dec1
            if(dollars_dec1 != 0):
                count1 = count1 + 1


   def main():
'''


def main():
    scraper = CraigslistScraper()
    print('Scraping site Victoria Housing...')
    scraper.scrape()
   # print('Scraping site Vancouver Housing...')
   # scraper.scrapeVan()


if __name__ == '__main__':
    main()
