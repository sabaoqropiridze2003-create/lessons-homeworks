
class ForceUnderscoreMeta(type):
    def __new__(cls, name, bases, dct):
        for attr_name, attr_value in dct.items():
            if attr_name.startswith("__") and attr_name.endswith("__"):
                continue

            if callable(attr_value):
                if not attr_name.startswith("_"):
                    raise ValueError(
                        f"In class '{name}', the method name '{attr_name}' is invalid! "
                        f"All methods must start with an underscore '_' symbol."
                    )

        return super().__new__(cls, name, bases, dct)


class CorrectClass(metaclass=ForceUnderscoreMeta):
    class_variable = "I am a string attribute, not a method."

    def __init__(self):
        pass

    def _valid_method(self):
        return "This method is valid because it starts with an underscore!"


obj = CorrectClass()
print(obj.class_variable)
print(obj._valid_method())
print("Test 1 passed successfully!\n")


print("-" * 50)

try:
    class IncorrectClass(metaclass=ForceUnderscoreMeta):
        def _test_one(self):
            return "This method is correct."

        def bad_method(self):
            return "This will trigger the ValueError."

except ValueError as error:
    print("The metaclass successfully caught the violation!")
    print(f"Error message: {error}")
