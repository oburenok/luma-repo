"""
Singleton Design Pattern
"""


class SingletonMeta(type):
    """
    The Singleton class
    """

    _instances = {}

    def __call__(cls, *args, **kwargs):
        """
        Returns instance of the class if it is already existing, otherwise create the one
        """
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]
