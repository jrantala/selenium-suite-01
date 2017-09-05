import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Ajax(unittest.TestCase):

    @classmethod
    def setUpClass(inst):
        # create a new Firefox session
        inst.driver = webdriver.Firefox()
        inst.driver.maximize_window()
 
    def test_ajax(self):
        # navigate to the application home page
        self.driver.get("https://www.w3schools.com/js/js_ajax_intro.asp")

        # find the button associated with the ajax call
        buttons = self.driver.find_elements_by_tag_name("button")
        button = None
        for b in buttons:
            if b.text == 'Change Content':
                button = b

        # ajax call
        button.click()

        # wait until <div id="demo"> (which contains the text
        # modified by the ajax call) to appear
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "demo"))
        )

        # modified text to look for
        ptexts = ['AJAX is not a programming language.',
                  'AJAX is a technique for accessing web servers from a web page.',
                  'AJAX stands for Asynchronous JavaScript And XML.']

        div_demo = self.driver.find_element_by_id("demo")
        paragraphs = div_demo.find_elements_by_tag_name("p")
        for p in paragraphs:
            self.assertIn(p.text, ptexts)


    @classmethod
    def tearDownClass(inst):
        # close the browser window
        inst.driver.quit()

if __name__ == '__main__':
    unittest.main()
