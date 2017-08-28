import unittest
from selenium import webdriver
 
class SearchText(unittest.TestCase):

    @classmethod
    def setUpClass(inst):
        # create a new Firefox session
        inst.driver = webdriver.Firefox()
        inst.driver.implicitly_wait(30)
        inst.driver.maximize_window()
 
    def test_search_by_text(self):
        # navigate to the application home page
        self.driver.get("http://www.google.com/")

        # get the search textbox
        search_field = self.driver.find_element_by_name("q")
 
        # enter search keyword and submit
        search_field.send_keys("Selenium")
        search_field.submit()
 
        # get the list of elements which are displayed after the search
 
        element_list = self.driver.find_elements_by_class_name("r")
        no=len(element_list)
        self.assertEqual(11, len(element_list))
 

    def test_search_by_text_joerantala(self):
        # navigate to the application home page
        self.driver.get("http://www.google.com/")

        # get the search textbox
        search_field = self.driver.find_element_by_name("q")
 
        # enter search keyword and submit
        search_field.send_keys("joerantala")
        search_field.submit()
 
        # verify that there are at least 2 hits
        element_list = self.driver.find_elements_by_class_name("r")
        no=len(element_list)
        self.assertGreater(len(element_list),2)

 
    @classmethod
    def tearDownClass(inst):
        # close the browser window
        inst.driver.quit()

if __name__ == '__main__':
    unittest.main()
