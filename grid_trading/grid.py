import configparser

from grid_trading.model import BasicGridModel


class Grid(object):
    def __init__(self):
        self.config = configparser.RawConfigParser()
        self.grid_model = BasicGridModel()

    def load_config(self):
        self.config.read('main.ini')

        mode = 'basic_grid'
        self.grid_model.base_price = self.config.get(mode, 'base_price')
        self.grid_model.volume_per_trading = self.config.get(mode, 'volume_per_trading')
        self.grid_model.increase_rate = self.config.get(mode, 'increase_rate')
        self.grid_model.decrease_rate = self.config.get(mode, 'decrease_rate')
        self.grid_model.min_volume = self.config.get(mode, 'min_volume')
        self.grid_model.max_volume = self.config.get(mode, 'max_volume')
        self.grid_model.price_ceiling = self.config.get(mode, 'price_ceiling')
        self.grid_model.price_floor = self.config.get(mode, 'price_floor')

    def calculate(self):
        self.load_config()
