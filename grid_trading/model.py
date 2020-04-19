class BasicGridModel(object):
    def __init__(self):
        self.base_price = 0
        self.volume_per_trading = 100
        self.increase_rate = 0.01
        self.decrease_rate = 0.01
        self.min_volume = 0
        self.max_volume = 0
        self.price_ceiling = 0
        self.price_floor = 0

    def load_config(self):
        mode = 'basic_grid'
        self.base_price = self.config.get(mode, 'base_price')
        self.volume_per_trading = self.config.get(mode, 'volume_per_trading')
        self.increase_rate = self.config.get(mode, 'increase_rate')
        self.decrease_rate = self.config.get(mode, 'decrease_rate')
        self.min_volume = self.config.get(mode, 'min_volume')
        self.max_volume = self.config.get(mode, 'max_volume')
        self.price_ceiling = self.config.get(mode, 'price_ceiling')
        self.price_floor = self.config.get(mode, 'price_floor')


class GridCellModel(object):
    def __init__(self):
        self.price = 1.00
        self.volume = 100
        self.total_volume = 0
        self.remark = ''
