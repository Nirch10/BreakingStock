import abc

from Models.Stock import Stock


class IStockDal(abc.ABC):
    @abc.abstractmethod
    def add_stock(self, stock: Stock) -> None:
        pass

    @abc.abstractmethod
    def get_stock(self, stock_id: int) -> Stock:
        pass

    @abc.abstractmethod
    def get_stocks(self) -> list:
        pass

    @abc.abstractmethod
    def delete_stock(self, stock_id: str) -> None:
        pass

    @abc.abstractmethod
    def update_stock_availability(self, stock: Stock, availability: bool) -> None:
        pass

    @abc.abstractmethod
    def get_stock_profit_money(self, stock: Stock) -> float:
        pass

    @abc.abstractmethod
    def get_stock_profit_percentage(self, stock: Stock) -> float:
        pass
