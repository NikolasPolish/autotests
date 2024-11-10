# from playwright.sync_api import sync_playwright

# playwright = sync_playwright().start()

# browser = playwright.chromium.launch(headless=False, slow_mo=700)
# page = browser.new_page()
# page.goto('https://www.saucedemo.com/')
# page.wait_for_load_state('load')

# page.fill(selector='#user-name', value='standard_user')
# page.fill(selector='#password', value='secret_sauce')
# page.click(selector='.submit-button')


# #прогрузка страницы
# page.wait_for_url(url='https://www.saucedemo.com/inventory.html', timeout=10000)
# #прогрузка определенного селектора
# page.wait_for_selector('#inventory_container')
# batton_add_card = '[data-test="add-to-cart-sauce-labs-backpack"]'
# card_button = '.inventory_item_description:has-text("Sauce Labs Backpack") button:has-text("Add to cart")'

# page.is_visible(selector=batton_add_card)
# page.is_enabled(selector=batton_add_card)
# page.click(card_button)

# page.is_visible(".shopping_cart_link")
# page.click(".shopping_cart_link")
# page.wait_for_url(url='https://www.saucedemo.com/cart.html', timeout=10000)

# button_checkout = '#checkout'
# page.wait_for_selector(button_checkout)
# page.is_visible(button_checkout)
# page.is_enabled(button_checkout)
# page.click(button_checkout)
# page.wait_for_url(url='https://www.saucedemo.com/checkout-step-one.html', timeout=10000)


# page.fill(selector='#first-name', value='play')
# page.fill(selector='#last-name', value='wright')
# page.fill(selector='#postal-code', value='secret_sauce')
# page.click(selector='#continue')
# page.click(selector='#finish')
# page.click(selector='#react-burger-menu-btn')
# page.click(selector='#logout_sidebar_link')

# browser.close()
# playwright.stop()
