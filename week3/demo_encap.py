
class Animal:
    """
    A class representing an animal with a name and age.

    Attributes:
    __name (str): The name of the animal (private attribute).
    __age (int): The age of the animal (private attribute).
    """

    def __init__(self, name, age):
        """
        Initializes a new instance of the Animal class.

        Args:
        name (str): The name of the animal.
        age (int): The age of the animal.
        """
        self.__name = name # name is private attribte
        self.__age = age # age is private attribute
    
    def show(self):
        """
        Prints the name and age of the animal.
        """
        print(f'Name: {self.__name}, Age: {self.__age}')

    def get_age(self):
        """
        Returns the age of the animal.

        Returns:
        int: The age of the animal.
        """
        return self.__age

    def set_age(self, age):
        """
        Sets the age of the animal.

        Args:
        age (int): The new age of the animal.
        """
        if age < 0:
            print('Age must be greater than 0.')
            return
        self.__age = age

    def get_name(self):
        """
        Returns the name of the animal.

        Returns:
        str: The name of the animal.
        """
        return self.__name

    def set_name(self, name):
        """
        Sets the name of the animal.

        Args:
        name (str): The new name of the animal.
        """
        if name == '':
            print('Name must not be empty.')
            return
        self.__name = name