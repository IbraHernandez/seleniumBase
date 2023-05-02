from page_objects.home_page import HomePage


class HomeTest(HomePage):
    def setUp(self):
        super().setUp()
        print('Running before each test')
        # open home page
        self.open("https://practice.automationbro.com/my-account")
        # login
        self.login()
        self.open_page()

    def tearDown(self):
        HomePage.logOut(self)

        super().tearDown()

    def test_home_page(self):
        # assert title
        self.assert_title("Practice E-Commerce Site – Automation Bro")
        # assert logo
        self.click("#menu-item-489 > a:nth-child(1)")
        self.assert_element(HomePage.logo_icon)
        # click on the get started button and asser the url
        self.click(HomePage.get_started)
        get_started_url = self.get_current_url()
        self.assert_equal(get_started_url, "https://practice.automationbro.com/#get-started")
        self.assert_true("get-started" in get_started_url)

        # get the text of the header and assert the value
        self.assert_text("Think different. Make different.", HomePage.heading_text)

        # excercise: scroll down and assert the copyrigth page
        self.scroll_to_bottom()
        self.assert_text("Copyright © 2020 Automation Bro", HomePage.copyright_text)
        print(self.get_text(HomePage.copyright_text))

    def test_menu_links(self):
        expected_links = ['Home', 'About', 'Shop', 'Blog', 'Contact', 'My account']

        # find menu links elements
        menu_links_el = self.find_elements(HomePage.menu_links)

        # loop through our menu links
        for idx, link_el in enumerate(menu_links_el):
            print(idx, link_el.text)
            self.assert_equal(expected_links[idx], link_el.text)
