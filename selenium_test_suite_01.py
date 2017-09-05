
import unittest
import HTMLTestRunner
import os

from selenium_test_login_ultimateqa import Login
from selenium_test_search import SearchText
from selenium_test_ajax import Ajax

login_tests = unittest.TestLoader().loadTestsFromTestCase(Login)
search_tests = unittest.TestLoader().loadTestsFromTestCase(SearchText)
ajax_tests = unittest.TestLoader().loadTestsFromTestCase(Ajax)

test_suite = unittest.TestSuite([login_tests, search_tests, ajax_tests])

dir = os.getcwd()
outfile = open(dir + "/selenium_test_suite_01.html", "w")
 
runner = HTMLTestRunner.HTMLTestRunner(stream=outfile,title='Test Report', description='Acceptance Tests')
 
runner.run(test_suite)
