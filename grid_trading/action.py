import configparser
import os

from grid_trading.grid import BasicGrid


class Action(object):
    grid = None

    def __init__(self, wb_sheet):
        self.wb_sheet = wb_sheet
        self.config = configparser.RawConfigParser()

    def _load_config(self, filepath):
        if filepath:
            config_path = filepath
        else:
            root_dir = os.path.dirname(os.path.abspath('.'))
            config_path = os.path.join(root_dir, "grid_trading.ini")
        self.config.read(config_path, encoding="utf-8-sig")

    def log(self, msg):
        self.wb_sheet.range("A1").value = msg

    def calculate(self):
        # load config
        self._load_config(None)

        # load grid model
        section = self.config.get('DEFAULT', 'section')
        if not self.config.has_section(section):
            self.log('没有找到配置文件section项: [{}]'.format(section))
            return
        grid_model = self.config.get(section, 'grid_model')
        if grid_model == BasicGrid.grid_model:
            self.grid = BasicGrid()

        if not self.grid:
            self.log('没有找到网格模型: {}'.format(grid_model))
            return

        # calculate
        self.grid.load_config(self.config[section])
        self.grid.calculate(self.wb_sheet)
