import uuid

import redis as redis

from DAL.IStockDal import IStockDal
from Models.Stock import Stock


class RedisStockDal(IStockDal):
    def __init__(self, redis_host: str, redis_port: int, password: str, redis_db: int):
        self.redis = redis.Redis(host=redis_host, port=redis_port, db=redis_db, password=password)

    def get_stock(self, stock_id: str) -> Stock:
        stock = self.redis.get(stock_id)
        return stock

    def get_stocks(self) -> list:
        _, keys = self.redis.scan("*")
        return self.redis.mget(keys)

    def delete_stock(self, stock: Stock) -> None:
        for key in self.redis.scan_iter(stock):
            self.redis.delete(key)

    def update_stock_availability(self, stock: Stock, availability: bool) -> None:
        stock.set_availability(availability)
        for key in self.redis.scan_iter(stock):
            self.redis.set(key, stock)

    def get_stock_profit_money(self, stock: Stock) -> float:
        curr_price, cost = self.__get_current_price_and_init_cost(stock)
        return curr_price - cost

    def get_stock_profit_percentage(self, stock: Stock) -> float:
        curr_price, cost = self.__get_current_price_and_init_cost(stock)
        return (curr_price * 100) / cost

    def add_stock(self, stock: Stock) -> None:
        self.redis.set(str(uuid.uuid4()), stock)

    def __get_current_price_and_init_cost(self, stock: Stock) -> tuple:
        current_sum, cost_sum = 0
        for key in self.redis.scan_iter(stock):
            self.redis.set(key, stock)
        return tuple(current_sum, cost_sum)

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
