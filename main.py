import random
MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_count = {
#This dictionary consists of symbols in the slot machine and how many of them are in each column, their value decreases from A to D.
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}

symbol_value = {
#This dictionary consists of values assigned to symbols.
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}


def check_winnings(columns, lines, bet, values):
#This function checks if the player won on any line by checking if all three columns in one row have the same symbol.

    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol]*bet
            winning_lines.append(line + 1)

    return winnings, winning_lines
            



def deposit():
#This function firstly checks if the user has entered a digit, then checks if that digit is greater than zero.
#If all checks are true, the function returns the entered value.
#While loop runs until the user has entered a valid amount.

    while True:
        amount = input("How much money would you like to deposit? $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than zero.")
        else:
            print("Please enter a number.")

    return amount

def get_number_of_lines():
#This function is similar to deposit() but it's using a global constant MAX_LINESt to keep the program dynamic.

    while True:
        lines = input("Enter the number of lines to bet on: [1 - " + str(MAX_LINES) + "]? ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Please enter a valid amount of lines you want to bet on. [1 - " + str(MAX_LINES) + "]")
        else:
            print("Please enter a number.")

    return lines

def get_bet():
#More global constants are used in this function.

    while True:
        bet = input("Enter the amount you want to bet on each line: [$" + str(MIN_BET) + " - $" + str(MAX_BET) + "]? ")
        if bet.isdigit():
            bet = int(bet)
            if MIN_BET <= bet <= MAX_BET:
                break
            else:
                print(f"Please enter a valid amount of money you want to bet. [${MIN_BET} - ${MAX_BET}]")
        else:
            print("Please enter a number.")

    return bet

def get_slot_machine_spin(rows, cols, symbols):
    #This fills up all_symbols with elements using frequencies of appearing listed in the dictionary above.
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)
    
    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:] #This copies the value of all_symbols to current_symbols (without [:] current_symbols would just store the same object as all_symbols).
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)

        columns.append(column)
    
    return columns

def print_slot_machine(columns):
#This function loops through every row and then loops through every column, where it prints the element of the column which corresponds with its row.
#Enumerate function is used for the program to know when it reached the last element of a row so it doesn't print a separator |.

    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end = " | ")
            else:
                print(column[row], end = "")
        print("")

def game(balance):
#This function runs one instance of the game and returns the new balance.

    lines = get_number_of_lines()

    while True:
    #This while loop is here to check if the player has enough money to place a bet.
    #Loop runs until the player places a valid bet.
 
        bet = get_bet()
        total_bet = bet*lines
        if total_bet <= balance:
            break
        else:
            print(f"You do not have enough money on your account. Your current balance is ${balance}.")

    print(balance, lines)
    print(f"You are betting ${bet} on {lines} lines. Your total bet is: ${bet*lines}.")

    slot = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slot)
    winnings, winning_lines = check_winnings(slot, lines, bet, symbol_value)
    print(f"You won ${winnings}")
    print(f"You won on lines: ", *winning_lines)

    return winnings - total_bet

def main():
    balance = deposit()
    while True:
        print(f"Current balance is: ${balance}")
        if balance == 0:
            break
        spin = input("Press enter to play. Press Q to quit.")
        if spin.lower == "q":
            break
        balance += game(balance)
    
    print(f"You left with ${balance}.")


main()