import unittest
from selenium import webdriver
import settings

class Login(unittest.TestCase):

    @classmethod
    def setUpClass(inst):
        # create a new Firefox session
        inst.driver = webdriver.Firefox()
        inst.driver.implicitly_wait(30)
        inst.driver.maximize_window()
 
    def test_login(self):
        # navigate to the application home page
        self.driver.get("https://courses.ultimateqa.com/users/sign_in")

        # my_username = "jrantala+temp@gmail.com"
        # my_password = "foofoofoo"
        my_username = settings.UltimateQA['username']
        my_password = settings.UltimateQA['password']

        username = self.driver.find_element_by_id("user_email")
        password = self.driver.find_element_by_id("user_password")
        
        username.send_keys(my_username)
        password.send_keys(my_password)
        
        submit = self.driver.find_element_by_id("btn-signin")
        
        submit.click()
        # verify that we've gotten through login and landed on the next page
        self.assertEqual("Ultimate QA", self.driver.title)

    @classmethod
    def tearDownClass(inst):
        # close the browser window
        inst.driver.quit()

if __name__ == '__main__':
    unittest.main()
