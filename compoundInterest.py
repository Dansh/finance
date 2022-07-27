from invest import Invest

class CompoundInterest(Invest):
    def __init__(self, starting_amount, yearly_return, monthly_invest):
        super().__init__(starting_amount, yearly_return)
        self._monthly_invest = monthly_invest
    
    def get_money_by_years(self, year):
        self.current_amount += self._current_amount * (self._yearly_return/12/ 100)  # For the first month when only starting amount counts               
        for _ in range(int(year*12-1)):
            self._current_amount += self._monthly_invest
            self.current_amount += self._current_amount * (self._yearly_return/12/ 100)               
        return self._current_amount
    

if __name__ == "__main__":
    ci = CompoundInterest(150, 10, 150)
    print(ci.get_money_by_year(30))
