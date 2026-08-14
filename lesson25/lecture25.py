# singlton

# ჩვეულებრივი მაგალითი

# class AppConfig:
#     def __init__(self):
#         self.debug = False
#         self.database_url = "localhost:5432"
#         self.app_name = "MyApp"
#         print(f"AppConfig has been created: {id(self)}")


# config1 = AppConfig()
# config2 = AppConfig()
# config3 = AppConfig()

# print(config1 is config2)

# სინგლრონის მაგალ;ითი


class AppConfig:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls.debug = False
            cls.database_url = "localhost:5432"
            cls.app_name = "MyApp"
            print("AppConfig has been created for the first time")
        return cls._instance


config1 = AppConfig()
config2 = AppConfig()
config3 = AppConfig()

print(config1 is config2)
