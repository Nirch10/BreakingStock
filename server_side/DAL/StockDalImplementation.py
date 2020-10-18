import uuid
import json
import redis as redis

from DAL.IStockDal import IStockDal
from Models.Stock import Stock


class RedisStockDal(IStockDal):
    def __init__(self, redis_host: str, redis_port: int, password: str = '', redis_db: int = 0):
        self.redis = redis.Redis(host=redis_host, port=redis_port, db=redis_db, password=password)

    def get_stock(self, stock_id: str) -> Stock:
        stock = self.redis.get(str.encode(stock_id))
        stock = self.__parse_json_stock(json.loads(stock))
        return stock

    def get_stocks(self) -> dict:
        keys = self.redis.keys('*')
        results = {}
        try:
            for key in keys:
                json_stock = json.loads(self.redis.get(key))
                stock = self.__parse_json_stock(json_stock)
                results[key.decode()] = stock
        except Exception:
            return {}
        return results

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
        self.redis.set(str(uuid.uuid4()), json.dumps(stock.__dict__))

    def __get_current_price_and_init_cost(self, stock: Stock) -> tuple:
        current_sum, cost_sum = 0
        for key in self.redis.scan_iter(stock):
            self.redis.set(key, stock)
        return tuple(current_sum, cost_sum)

    def __parse_json_stock(self, json_stock: str) -> Stock:
        try:
            stock = Stock(stock_name=json_stock['name'], stock_cost=json_stock['cost'], stock_curr_price=json_stock['curr_price'], available=json_stock['available'])
            return stock
        except Exception:
            return None

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
