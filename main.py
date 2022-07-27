import tkinter as tk
from invests.compound_interest import CompoundInterest
from pages.calc_ci_page import CalcCIPage



def main():
    window = tk.Tk()

    calc_ci_page = CalcCIPage(window, 400, 700) 

    window.mainloop()

    



if __name__ == "__main__":
    main()