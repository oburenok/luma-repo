import abc


class ABCPage(abc.ABC):
    """
    This is abstract class for all pages
    """
    @abc.abstractmethod
    def logout(self):
        pass

    @abc.abstractmethod
    def create_account(self):
        pass

    @abc.abstractmethod
    def search_products(self):
        pass

    @abc.abstractmethod
    def enter_text_in_search_field(self, text):
        pass

    @abc.abstractmethod
    def click_search(self):
        pass

    @abc.abstractmethod
    def open_cart(self):
        pass

    @abc.abstractmethod
    def verify_cart_subtotal(self):
        pass

    @abc.abstractmethod
    def click_proceed_to_checkout(self):
        pass

    @abc.abstractmethod
    def load(self):
        pass


class ABCLoginPage(abc.ABC):
    """
    This is abstract class for login page
    """
    @abc.abstractmethod
    def login(self):
        pass

    @abc.abstractmethod
    def restore_password(self):
        pass
