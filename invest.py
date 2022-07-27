class Invest:
    def __init__(self, starting_amount, yearly_return):
        """
        set invest starting amount and yearly return 
        """
        self._starting_amount = starting_amount
        self._yearly_return = yearly_return
        self._current_amount = starting_amount
    
    @property
    def starting_amount(self):
        return self._starting_amount
    
    @starting_amount.setter
    def starting_amount(self, starting_amount):
        self._starting_amount = starting_amount

    @property
    def yearly_return(self):
        return self._yearly_return

    @yearly_return.setter
    def yearly_return(self, yearly_return):
        self.yearly_return = yearly_return

    @property
    def current_amount(self):
        return self._current_amount

    @current_amount.setter
    def current_amount(self, current_amount):
        self._current_amount = current_amount
    
    def get_money_by_years(self, years):
        return self._starting_amount + self._starting_amount * ((years * self._yearly_return)/100) 

    def get_money_by_monthes(self, monthes):
        return self._starting_amount + self._starting_amount * ((monthes * self._yearly_return/12)/100)


if __name__ == "__main__":
    invest = Invest(1000, 10)
    print(invest.get_money_by_years(2))
    print(invest.get_money_by_monthes(2))
