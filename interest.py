# Calculate interest over time

from prettytable import PrettyTable
t = PrettyTable()
t.field_names = ["Year", "Sum", "Yearly increase", "Monthly increase"]
diff = int(0)

# Take input parameters and call on next function
def takeInput():
    sum = float(input("Starting sum : "))
    interest = float(input("Yearly interest/roi : "))
    years = int(input("Years to run : "))
    manualDeposit = int(input("Deposited manually each year (Can be 0) : "))
    calculateRes(sum, years, interest, manualDeposit)

# Clear table, iterate all the years and add to table, then print
def calculateRes(sum, years, interest, manualDeposit):
    startsum = sum
    startyears = years
    t.clear_rows()
    year = 1
    while years is not 0:
        diff = (sum * (1 + interest/100) - sum)
        sum = (sum * (1 + interest/100))
        sum = sum + manualDeposit
        t.add_row([year, format(sum, '.2f'), format(diff, '.2f'), format((diff / 12), '.2f')])
        years = years - 1
        year = year + 1
    print(t)
    menuScr(startsum, startyears, interest, manualDeposit)

# Once first run is complete, get menu for changing variables.
def menuScr(sum, years, interest, manualDeposit):
    while True:
        print("Starting sum:%s, Interest:%s, Years:%s, Deposits:%s" % (sum, interest, years, manualDeposit))
        print("Change (s)tarting sum, (i)nterest, (y)ears, (d)eposits, (r)un again or (e)xit\n:", end = '')
        userChoice = input()
        if userChoice.lower() == "s":
            sum = float(input("New starting sum : "))
        elif userChoice.lower() == "i":
            interest = float(input("New interest/roi : "))
        elif userChoice.lower() == "y":
            years = int(input("Years to run : "))
        elif userChoice.lower() == "d":
            manualDeposit = int(input("Deposits every year : "))
        elif userChoice.lower() == "r":
            calculateRes(sum, years, interest, manualDeposit)
        elif userChoice.lower() == "e":
            exit()





# Run first input, run calculation, print, go to menu
takeInput()
