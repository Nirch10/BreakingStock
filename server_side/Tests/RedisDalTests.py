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

    def test_update_availability(self):
        all = self.dal.get_stocks()
        self.dal.update_stock_availability(next(iter(all)), False)
        all = self.dal.get_stocks()
        print("dom")

    def test_update_current_price(self):
        all = self.dal.get_stocks()
        self.dal.update_current_price(next(iter(all)), 1.7)
        all = self.dal.get_stocks()
        print("dom")

    def test_get_current_profit(self):
        all = self.dal.get_stocks()
        for v in all:
            profit = self.dal.get_stock_profit_money(v)
            print(profit)

    def test_get_current_profit_percentage(self):
        all = self.dal.get_stocks()
        for v in all:
            profit = self.dal.get_stock_profit_percentage(v)
            print(str(profit - 100.0) + '%')
        print()




