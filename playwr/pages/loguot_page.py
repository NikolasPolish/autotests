from pages.base_page import BasePage

class LogOut(BasePage):
    BURGER_MENU = '#react-burger-menu-btn'
    BURGER_LOGOUT_MENU = '#logout_sidebar_link'

    def __init__(self, page):
        super().__init__(page)
        self._endpoint = ''

    def open_menu(self):
        self.wait_for_selector_and_click(self.BURGER_MENU)
    
    def burger_logout(self):
        self.wait_for_selector_and_click(self.BURGER_LOGOUT_MENU)