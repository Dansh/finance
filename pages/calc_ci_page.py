from pages.page import Page
import tkinter as tk
from invests.compound_interest import CompoundInterest

class CalcCIPage(Page):
    def __init__(self, window, width, height):
        super().__init__(window, width, height)
        self.draw_widgets()

    def draw_widgets(self):
        self.title = tk.Label(text="מחשבון ריבית דריבית")
        self.title.place(relx=0.5, rely=0.1, anchor="center")

        self.starting_amount_label = tk.Label(text="Starting Amount - ")
        self.starting_amount_label.place(relx = 0.25, rely=0.25, anchor="center")

        self.starting_amount_input = tk.Entry()
        self.starting_amount_input.place(relx = 0.65, rely= 0.25, anchor="center")

        self.yearly_return_label = tk.Label(text="Yearly Return - ")
        self.yearly_return_label.place(relx = 0.25, rely=0.32, anchor="center")

        self.yearly_return_input = tk.Entry()
        self.yearly_return_input.place(relx = 0.65, rely= 0.32, anchor="center")

        self.monthly_invest_label = tk.Label(text="Monthly Invest - ")
        self.monthly_invest_label.place(relx = 0.25, rely=0.39, anchor="center")

        self.monthly_invest_input = tk.Entry()
        self.monthly_invest_input.place(relx = 0.65, rely= 0.39, anchor="center")

        self.years_label = tk.Label(text="Years: ")
        self.years_label.place(relx = 0.2, rely= 0.50, anchor="center")

        self.years_input = tk.Entry(width="2")
        self.years_input.place(relx = 0.3, rely=0.50, anchor="center")

        self.submit_button = tk.Button(text="חשב", width="10", height="2", command=lambda : self.submit_ci(self.starting_amount_input.get(), self.yearly_return_input.get(), self.monthly_invest_input.get(), self.years_input.get()))
        self.submit_button.place(relx = 0.65, rely=0.50, anchor="center")
    
    def submit_ci(self, starting_amount, yearly_return, monthly_invest, years):
        self.ci = CompoundInterest(float(starting_amount), float(yearly_return), float(monthly_invest))
        self.money_after_years = self.ci.get_money_by_years(float(years))
        self.money_after_years_label = tk.Label(text="Money After {} Years - {:.2f}".format(years, self.money_after_years))
        self.money_after_years_label.place(relx = 0.25, rely=0.7)