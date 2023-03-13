
from data import load_config
from configparser import ConfigParser

config = ConfigParser()
config.read('config.ini')
a = 'node1'
mas = ['ip', 'password']
print(config.get(a, vars = mas))
    