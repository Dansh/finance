import tkinter as tk
from compoundInterest import CompoundInterest

def submit_ci(starting_amount, yearly_return, monthly_invest, years):
    ci = CompoundInterest(float(starting_amount), float(yearly_return), float(monthly_invest))
    money_after_years = ci.get_money_by_years(float(years))
    money_after_years_label = tk.Label(text="Money After {} Years - {:.2f}".format(years, money_after_years))
    money_after_years_label.place(relx = 0.25, rely=0.7)

def main():
    window = tk.Tk()

    window.geometry("400x700") # set window size (widthxheight)
    window.resizable(0,0)

    title = tk.Label(text="מחשבון ריבית דריבית")
    title.place(relx=0.5, rely=0.1, anchor="center")

    starting_amount_label = tk.Label(text="Starting Amount - ")
    starting_amount_label.place(relx = 0.25, rely=0.25, anchor="center")

    starting_amount_input = tk.Entry()
    starting_amount_input.place(relx = 0.65, rely= 0.25, anchor="center")

    yearly_return_label = tk.Label(text="Yearly Return - ")
    yearly_return_label.place(relx = 0.25, rely=0.32, anchor="center")

    yearly_return_input = tk.Entry()
    yearly_return_input.place(relx = 0.65, rely= 0.32, anchor="center")

    monthly_invest_label = tk.Label(text="Monthly Invest - ")
    monthly_invest_label.place(relx = 0.25, rely=0.39, anchor="center")

    monthly_invest_input = tk.Entry()
    monthly_invest_input.place(relx = 0.65, rely= 0.39, anchor="center")

    years_label = tk.Label(text="Years: ")
    years_label.place(relx = 0.2, rely= 0.50, anchor="center")

    years_input = tk.Entry(width="2")
    years_input.place(relx = 0.3, rely=0.50, anchor="center")

    submit_button = tk.Button(text="חשב", width="10", height="2", command=lambda : submit_ci(starting_amount_input.get(), yearly_return_input.get(), monthly_invest_input.get(), years_input.get()))
    submit_button.place(relx = 0.65, rely=0.50, anchor="center")


    window.mainloop()

    




if __name__ == "__main__":
    main()