import unittest

from DAL.StockDalImplementation import RedisStockDal
from Models.Stock import Stock


class RedisDalTests(unittest.TestCase):
    def setUp(self):
        self.dal = RedisStockDal(redis_host="127.0.0.1", redis_port=6379)

    def test_add_user(self):
        user = Stock(stock_name="test", stock_cost=1.5, stock_curr_price=5.2)
        self.dal.add_stock(user)

    def test_get_stocks(self):
        res = self.dal.get_stocks()
        for r in res:
            print(r)

    def test_get_stock(self):
        all = self.dal.get_stocks()
        first = self.dal.get_stock(next(iter(all)))
        print(first)

    def test_delete_stock(self):
        all = self.dal.get_stocks()
        self.dal.delete_stock(next(iter(all)))
        all = self.dal.get_stocks()
        print("dom")


