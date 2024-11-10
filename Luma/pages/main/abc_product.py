import abc


class ABCProduct(abc.ABC):
    """
    This is interface to interact with product and cart, according to Composite Pattern
    """

    @abc.abstractmethod
    def get_price(self):
        pass

    @abc.abstractmethod
    def verify_price(self, price):
        pass

    @abc.abstractmethod
    def get_qty(self):
        pass

    @abc.abstractmethod
    def verify_qty(self, quantity):
        pass

    @abc.abstractmethod
    def get_name(self):
        pass

    @abc.abstractmethod
    def verify_name(self, name):
        pass

    @abc.abstractmethod
    def add_to_cart(self):
        pass

