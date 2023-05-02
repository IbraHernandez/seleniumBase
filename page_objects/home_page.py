from seleniumbase import BaseCase

class HomePage(BaseCase):
    logo_icon = ".custom-logo-link"
    get_started = "#get-started"
    heading_text = "h1"
    copyright_text = ".tg-site-footer-section-1"
    menu_links = "#primary-menu li[id*=menu-item-]"
    username = "#username"
    password = "#password"
    login_button = "button[name=login]"
    accountURL = "https://practice.automationbro.com/my-account"
    logout_button = ".woocommerce-MyAccount-content > p:nth-child(2) > a:nth-child(3)"

    def open_page(self):
        self.open_url("https://practice.automationbro.com")

    def login(self):
        self.send_keys(self.username, "ibrahdzmes@gmail.com")
        self.send_keys(self.password, "testuser9071")
        self.click(self.login_button)

    def logOut(self):
        print('Running after each test')
        self.open(self.accountURL)
        self.click(self.logout_button)