from DAL.IStockDal import IStockDal
from Models.Stock import Stock


class RedisStockDal(IStockDal):
    def get_stock(self, stock_id: int) -> Stock:
        pass

    def get_stocks(self) -> list:
        pass

    def delete_stock(self, stock: Stock) -> None:
        pass

    def get_stock_profit_money(self, stock: Stock) -> float:
        pass

    def get_stock_profit_percentage(self, stock: Stock) -> float:
        pass

    def add_stock(self, stock: Stock) -> None:
        pass


class CsvStockDal(IStockDal):
    def add_stock(self, stock: Stock) -> None:
        pass

    def get_stock(self, stock_id: int) -> Stock:
        pass

    def get_stocks(self) -> list:
        pass

    def delete_stock(self, stock: Stock) -> None:
        pass

    def get_stock_profit_money(self, stock: Stock) -> float:
        pass

    def get_stock_profit_percentage(self, stock: Stock) -> float:
        pass
