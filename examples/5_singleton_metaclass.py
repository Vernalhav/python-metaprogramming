class Singleton(type):
    instances = {}
    
    def __call__(cls, *args, **kwargs):
        if cls not in Singleton.instances:
            Singleton.instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)

        return Singleton.instances[cls]


class DatabaseConfig(metaclass=Singleton):
    pass

class Logger(metaclass=Singleton):
    pass


dbConfig1 = DatabaseConfig()
dbConfig2 = DatabaseConfig()

logger1 = Logger()
logger2 = Logger()

print(f'{dbConfig1 is dbConfig2}')
print(f'{logger1 is logger2}')