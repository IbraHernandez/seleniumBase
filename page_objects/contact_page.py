from seleniumbase import BaseCase


class ContactPage(BaseCase):
    contact_name = ".contact-name input"
    contact_email = ".contact-email input"
    contact_phone = ".contact-phone input"
    message = ".contact-message textarea"

