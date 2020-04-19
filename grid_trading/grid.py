class BasicGrid(object):
    grid_model = 'basic_grid'
    cells = []

    def __init__(self):
        self.base_price = None
        self.base_volume = None
        self.volume_per_trading = None
        self.increase_rate = None
        self.decrease_rate = None
        self.min_volume = None
        self.max_volume = None
        self.price_ceiling = None
        self.price_floor = None

    def load_config(self, config):
        self.base_price = config.getfloat('base_price')
        self.base_volume = config.getfloat('base_volume')
        self.volume_per_trading = config.getint('volume_per_trading')
        self.increase_rate = config.getfloat('increase_rate')
        self.decrease_rate = config.getfloat('decrease_rate')
        self.min_volume = config.getint('min_volume')
        self.max_volume = config.getint('max_volume')
        self.price_ceiling = config.getfloat('price_ceiling')
        self.price_floor = config.getfloat('price_floor')

    def _log(self, wb_sheet, msg):
        wb_sheet.range("A1").value = msg

    def _validate(self, wb_sheet):
        if not self.base_price or self.base_price < 0:
            self._log(wb_sheet, '缺少base_price参数')
            return False
        if not self.base_volume or self.base_volume < 0:
            self._log(wb_sheet, '缺少base_volume参数')
            return False
        if not self.volume_per_trading or self.volume_per_trading < 0:
            self._log(wb_sheet, '缺少volume_per_trading参数')
            return False
        if not self.increase_rate:
            self._log(wb_sheet, '缺少increase_rate参数')
            return False
        if not self.decrease_rate:
            self._log(wb_sheet, '缺少decrease_rate参数')
            return False
        if not self.min_volume and not self.price_ceiling:
            self._log(wb_sheet, '缺少min_volume or price_ceiling参数')
            return False
        if not self.max_volume and not self.price_floor:
            self._log(wb_sheet, '缺少max_volume or price_floor参数')
            return False

        return True

    def calculate(self, wb_sheet):
        if not self._validate(wb_sheet):
            return

        # 向上
        last_price = self.base_price
        total_volume = self.base_volume
        while True:
            cell = {
            'price' : last_price,
            cell.volume = self.volume_per_trading,
            cell.total_volume = total_volume,
            }
            self.cells.append(cell)

            last_price += last_price * self.increase_rate
            total_volume -= self.volume_per_trading
            if self.price_ceiling and last_price > self.price_ceiling:
                break
            if self.min_volume and total_volume < self.min_volume:
                break

        # 向下
        last_price = self.base_price
        total_volume = self.base_volume
        while True:
            last_price -= last_price * self.decrease_rate
            total_volume += self.volume_per_trading
            if self.price_floor and last_price < self.price_floor:
                break
            if self.max_volume and total_volume < self.max_volume:
                break

            cell = BasicCell()
            cell.price = last_price
            cell.volume = self.volume_per_trading
            cell.total_volume = total_volume
            self.cells.append(cell)

    def _output_excel(self, wb_sheet):

        for cell in self.cells:
            wb_sheet.range("A1").value = msg
