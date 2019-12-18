# Calculate interest over time

from prettytable import PrettyTable
t = PrettyTable()
t.field_names = ["Year", "Sum", "Increase"]
diff = int(0)

# Take input parameters and call on next function
def takeInput():
    sum = float(input("Starting sum : "))
    interest = float(input("Yearly interest/roi : "))
    years = int(input("Years to run : "))
    calculateRes(sum, years, interest)

# Clear table, iterate all the years and add to table, then print
def calculateRes(sum, years, interest):
    startsum = sum
    startyears = years
    t.clear_rows()
    year = 1
    while years is not 0:
        diff = (sum * (1 + interest/100) - sum)
        sum = (sum * (1 + interest/100))
        t.add_row([year, format(sum, '.2f'), format(diff, '.2f')])
        years = years - 1
        year = year + 1
    print(t)
    menuScr(startsum, startyears, interest)

# Once first run is complete, get menu for changing variables.
def menuScr(sum, years, interest):
    while True:
        print("Starting sum:%s, Interest:%s, Years:%s" % (sum, interest, years))
        print("Change (s)tarting sum, (i)nterest, (y)ears, (r)un again or (e)xit\n:", end = '')
        userChoice = input()
        if userChoice.lower() == "s":
            sum = float(input("New starting sum : "))
        elif userChoice.lower() == "i":
            interest = float(input("New interest/roi : "))
        elif userChoice.lower() == "y":
            years = int(input("Years to run : "))
        elif userChoice.lower() == "r":
            calculateRes(sum, years, interest)
        elif userChoice.lower() == "e":
            exit()

# Run first input, run calculation, print, go to menu
takeInput()
