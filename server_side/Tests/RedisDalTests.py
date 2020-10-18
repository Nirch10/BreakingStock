import unittest

from DAL.StockDalImplementation import RedisStockDal
from Models.Stock import Stock


class RedisDalTests(unittest.TestCase):
    def setUp(self):
        self.dal = RedisStockDal(redis_host="127.0.0.1", redis_port=6379)

    def test_add_user(self):
        self.setUp()
        user = Stock(stock_name="test", stock_cost=1.5, stock_curr_price=5.2)
        self.dal.add_stock(user)

    def get_stocks(self):
        self.setUp()
        res = self.dal.get_stocks()
        for r in res:
            print(r)


