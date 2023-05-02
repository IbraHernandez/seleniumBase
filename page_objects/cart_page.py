from seleniumbase import BaseCase


class CartPage(BaseCase):
    def open_page(self):
        self.open("https://practice.automationbro.com/cart")

    converse_add_to_cart_btn = "a[aria-label='Add “Converse” to your cart']"
    cart_count_text = "ul[class='header-action-list'] span[class='count']"
    subtotal_text = ".cart-subtotal > td:nth-child(2) > span:nth-child(1) > bdi:nth-child(1)"
    product_quantity_input = "input[title='Qty']"
    update_cart_btn = "button[name='update_cart']"
    loading_overlay = "div[class='blockUI blockOverlay']"
