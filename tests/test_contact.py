from seleniumbase import BaseCase
from page_objects.contact_page import ContactPage
from page_objects.home_page import HomePage


class ContactTest(HomePage):
    def setUp(self):
        super().setUp()
        print('Running before each test')
        # open home page
        self.open("https://practice.automationbro.com/my-account")
        # login
        self.login()
        self.open_page()

    def tearDown(self):
        print('Running after each test')
        self.logOut()

    def test_contact_page(self):
        # open the page
        self.open("https://practice.automationbro.com/contact")

        # scroll to the form
        self.scroll_to("#evf-form-277")
        self.save_screenshot("empty_contact_from", "custom_screenshots")
        # fill in all the fields
        self.send_keys(ContactPage.contact_name, "Test Name")
        self.send_keys(ContactPage.contact_email, "Test@mail.com")
        self.send_keys(ContactPage.contact_phone, "123456789")
        self.send_keys(ContactPage.message, "This is a test message")

        # take screenshot when form is filled
        self.scroll_to("#evf-form-277")
        self.save_screenshot("filled_contact_from", "custom_screenshots")
        # click submit button
        self.click("#evf-submit-277")
        # verify submit message
        self.assert_text("Thanks for contacting us! We will be in touch with you shortly", "div[role=alert]")
