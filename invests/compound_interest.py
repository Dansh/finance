from invests.invest import Invest

class CompoundInterest(Invest):
    def __init__(self, starting_amount, yearly_return, monthly_invest):
        """
        Create a compound interest instance
        @param - starting_amount (float) starting amount of money to invest 
        @param - yearly_return (float) return for every year in percents
        @param - monthly_invest (float) amount of money being invested every month
        """
        super().__init__(starting_amount, yearly_return) # calls the Invest init method which sets also current_amount=starting_amount
        self._monthly_invest = monthly_invest
    
    def get_money_by_years(self, year):
        """
        @desc - doing the math behind the compound interest invest, For Example: 
                starting amount = 100, yearly_return = 10(%), monthly_invest = 150
                takes 10/12(%) of 100 and adds to 100 = 100.83 - after first month
                adds 150 = 250.83, takes 10/12(%) of 250.83 and adds = 252.92 and so on...
        @param - year (float) the number of years to calc (can also be 1/12 year (represents 1 month))
        @returns - (float) amount of money you'll have after @param:year passes
        """
        self.current_amount += self._current_amount * (self._yearly_return/12/ 100)  # For the first month when only starting amount counts               
        for _ in range(int(year*12-1)): # run for every month
            self._current_amount += self._monthly_invest # adds monthly invest
            self.current_amount += self._current_amount * (self._yearly_return/12/ 100)       
        return self._current_amount 
    


