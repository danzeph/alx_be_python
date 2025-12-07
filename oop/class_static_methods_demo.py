class Calculator:
    """
    A class demonstrating the use of static and class methods.
    """
    # Class Attribute referenced by the class method
    calculation_type = "Arithmetic Operations"

    @staticmethod
    def add(a, b):
        """
        Static Method: Takes two arguments and returns their sum.
        It does not access class or instance data.
        """
        return a + b

    @classmethod
    def multiply(cls, a, b):
        """
        Class Method: Takes the class itself (cls) as the first argument.
        It accesses the class attribute calculation_type.
        """
        # Accessing the class attribute via the 'cls' parameter
        print(f"Calculation type: {cls.calculation_type}")
        return a * b

# Note: The demonstration is provided in main.py, as per the task.
