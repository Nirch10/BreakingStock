class Stock:
    def __init__(self, stock_name: str, stock_curr_price: float = 0.0, stock_cost: float = 0.0,
                 available: bool = True) -> None:
        self.name = stock_name
        self.curr_price = stock_curr_price
        self.cost = stock_cost
        self.available = available

    def set_curr_price(self, new_price: float) -> None:
        self.curr_price = new_price

    def set_stock_name(self, new_name: str) -> None:
        self.name = new_name

    def set_cost(self, new_cost: float) -> None:
        self.cost = new_cost

    def set_availability(self, new_availability: bool):
        self.available = new_availability

    def get_name(self) -> str:
        return self.name

    def get_curr_price(self) -> float:
        return self.curr_price

    def get_cost(self) -> float:
        return self.cost
