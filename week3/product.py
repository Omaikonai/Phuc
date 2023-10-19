# Create a class Product with attributes id, name, price, quantity.
# All attributes are private, provide getters for all attributes.
# Provide setters for name, price, quantity.
class Product:
    """
    A class representing a product.

    Attributes:
    -----------
    id : int
        The ID of the product.
    name : str
        The name of the product.
    price : float
        The price of the product.
    quantity : int
        The quantity of the product.

    Methods:
    --------
    get_id() -> int
        Returns the ID of the product.
    get_name() -> str
        Returns the name of the product.
    set_name(name: str)
        Sets the name of the product.
    get_price() -> float
        Returns the price of the product.
    set_price(price: float)
        Sets the price of the product.
    get_quantity() -> int
        Returns the quantity of the product.
    set_quantity(quantity: int)
        Sets the quantity of the product.
    """
    def __init__(self, id: int, name: str, price: float, quantity: int):
        self.__id = id
        self.__name = name
        self.__price = price
        self.__quantity = quantity

    def get_id(self) -> int:
        return self.__id

    def get_name(self) -> str:
        return self.__name

    def set_name(self, name: str):
        self.__name = name

    def get_price(self) -> float:
        return self.__price

    def set_price(self, price: float):
        self.__price = price

    def get_quantity(self) -> int:
        return self.__quantity

    def set_quantity(self, quantity: int):
        self.__quantity = quantity
    
    def show_info(self):
        print(f"ID: {self.__id}\nName: {self.__name}\nPrice: {self.__price}\nQuantity: {self.__quantity}")
    
    def payment(self, tax):
        return self.__price * self.__quantity * (1 + tax)