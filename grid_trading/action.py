import configparser
import os

from grid_trading.grid import BasicGrid


class Action(object):
    grid = None

    def __init__(self):
        self.config = configparser.RawConfigParser()

    def load_config(self, filepath):
        if filepath:
            config_path = filepath
        else:
            root_dir = os.path.dirname(os.path.abspath('.'))
            config_path = os.path.join(root_dir, "grid_trading.ini")
        self.config.read(config_path)

        if self.grid:
            self.grid.load_config(self.config)

    def set_grid_model(self):
        self.grid = BasicGrid()
        self.grid.load_config(self.config)

    def calculate(self, grid_model=None):
        if grid_model:
            self.grid = BasicGrid()
        self.load_config(None)
