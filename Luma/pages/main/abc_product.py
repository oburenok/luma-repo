import abc


class ABCProduct(abc.ABC):
    """
    This is interface to interact with product and cart, according to Composite Pattern
    """

    @abc.abstractmethod
    def get_price(self):
        pass

    @abc.abstractmethod
    def verify_price(self):
        pass

    @abc.abstractmethod
    def verify_quantity(self):
        pass

    @abc.abstractmethod
    def verify_name(self):
        pass

    @abc.abstractmethod
    def add_to_cart(self):
        pass

    @abc.abstractmethod
    def remove_from_cart(self):
        pass

    @abc.abstractmethod
    def update_product(self):
        pass

    @abc.abstractmethod
    def is_composite(self):
        pass


