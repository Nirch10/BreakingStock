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

    def delete_stock(self, stock_id: str) -> None:
        self.redis.delete(str.encode(stock_id))

    def update_stock_availability(self, stock_id: str, availability: bool) -> None:
        stock = self.get_stock(stock_id)
        stock.set_availability(availability)
        self.redis.set(str.encode(stock_id), json.dumps(stock.__dict__))

    def update_current_price(self, stock_id: str, current_price: float) -> None:
        stock = self.get_stock(stock_id)
        stock.set_curr_price(current_price)
        self.redis.set(str.encode(stock_id), json.dumps(stock.__dict__))

    def get_stock_profit_money(self, stock_id: str) -> float:
        curr_price, cost = self.__get_current_price_and_init_cost(stock_id)
        return curr_price - cost

    def get_stock_profit_percentage(self, stock_id: Stock) -> float:
        curr_price, cost = self.__get_current_price_and_init_cost(stock_id)
        return (curr_price * 100) / cost

    def add_stock(self, stock: Stock) -> None:
        self.redis.set(str(uuid.uuid4()), json.dumps(stock.__dict__))

    def __get_current_price_and_init_cost(self, stock_id: str) -> tuple:
        stock = self.get_stock(stock_id)
        current_sum = stock.get_curr_price()
        cost_sum = stock.get_cost()
        return current_sum, cost_sum

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
