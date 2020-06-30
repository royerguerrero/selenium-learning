import unittest
from selenium import webdriver

class RegisterNewUser(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r'C:/chromedriver.exe')
        driver = self.driver
        driver.implicitly_wait(30)
        driver.maximize_window()
        driver.get('http://demo-store.seleniumacademy.com/')

    def test_new_user(self):
        driver = self.driver
        driver.find_element_by_xpath('//*[@id="header"]/div/div[2]/div/a').click()
        driver.find_element_by_link_text('Register').click()
        
        self.assertEqual('Create New Customer Account', driver.title)

        first_name = driver.find_element_by_id('firstname')
        middle_name = driver.find_element_by_id('middlename')
        last_name = driver.find_element_by_id('lastname')
        email = driver.find_element_by_id('email_address')
        password = driver.find_element_by_id('password')
        confirm_password = driver.find_element_by_id('confirmation')
        newsletter = driver.find_element_by_id('is_subscribed')
        submit_button = driver.find_element_by_xpath('//*[@id="form-validate"]/div[2]/button')

        self.assertTrue(
            first_name.is_enabled()
            and last_name.is_enabled()
            and email.is_enabled()
            and password.is_enabled()
            and confirm_password.is_enabled()
            and submit_button.is_enabled()
        )

        first_name.send_keys('Test')
        middle_name.send_keys('Test')
        last_name.send_keys('Test')
        email.send_keys('test@test.com')
        password.send_keys('Test')
        confirm_password.send_keys('Test')
        submit_button.click()

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main(verbosity=2)