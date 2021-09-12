# Currency Converter Program

# list of currencies that are available for conversion
currency_list = ["USD", "EUR", "JPY", "GBP", "AUD", "CAD", "CHF", "CNY", "SEK", "NZD", "MXN", "SGD", "HKD", "NOK", "KRW", "TRY", "INR", "RUB", "BRL", "ZAR"]
# list of exchange rates: 1NZD to list of currencies that are available for conversion
exchange_rate_list = [0.7, 0.6, 76.95, 0.5, 0.95, 0.88, 0.64, 4.52, 6.07, 1, 14, 0.95, 5.42, 6.25, 801.03, 6.04, 51.91, 51.37, 3.65, 10.3]
last_updated = "11/08/2021 14:10"
still_converting = True


def calculate_converted_value(currency_from, currency_to, value):       # calculates the exchange rate and multiplies it with the amount to get an answer
    currency_from_position = currency_list.index(currency_from)         # finds the position value of the currency chosen by the user (from)
    currency_to_position = currency_list.index(currency_to)             # finds the position value of the currency chosen by the user (to)
    rate = exchange_rate_list[currency_to_position] / exchange_rate_list[currency_from_position]                # finds the exchange rate from to   $1 from = ~ to
    reversed_rate = exchange_rate_list[currency_from_position] / exchange_rate_list[currency_to_position]       # finds the reversed exchange rate to from   $1 to = ~ from
    answer = float("{:.2f}".format(rate * value))       # finds the answer by multiplying it
    return rate, reversed_rate, answer


def calculate_reversed_converted_value(currency_from, currency_to, value):      # calculates the exchange rate and multiplies it with the amount to get an answer
    currency_from_position = currency_list.index(currency_from)                 # finds the position value of the currency chosen by the user (from)
    currency_to_position = currency_list.index(currency_to)                     # finds the position value of the currency chosen by the user (to)
    reversed_rate = exchange_rate_list[currency_from_position] / exchange_rate_list[currency_to_position]       # finds the reversed exchange rate to from   $1 to = ~ from
    rate = exchange_rate_list[currency_to_position] / exchange_rate_list[currency_from_position]                # finds the exchange rate from to   $1 from = ~ to
    reversed_answer = float("{:.2f}".format(reversed_rate * value))     # finds the answer by multiplying it
    return reversed_rate, rate, reversed_answer


while still_converting:     # while user wants to keep converting, run the loop
    print("These are the currencies available for converting: \n"
          "US Dollar (USD) \n"
          "Euro (EUR) \n"
          "Yen (JPY) \n"
          "Pound Sterling (GBP) \n"
          "Australian Dollar (AUD) \n"
          "Canadian (CAD) \n"
          "Swiss Franc (CHF) \n"
          "Chinese Renminbi (CNY) \n"
          "Swedish Krona (SEK) \n"
          "New Zealand Dollar (NZD) \n"
          "Mexican Peso (MXN) \n"
          "Singapore Dollar (SGD) \n"
          "Hong Kong Dollar (HKD) \n"
          "Norwegian Krone (NOK) \n"
          "South Korea Won (KRW) \n"
          "Turkish Lira (TRY) \n"
          "Indian Rupee (INR) \n"
          "Russian Ruble (RUB) \n"
          "Brazilian Real (BRL) \n"
          "South African Rand (ZAR)")

    while True:     # this loop forces the user to enter a valid input
        selected_currency_from = input("Please enter a currency code (e.g. US = USD) that you would like to convert from: ").strip().upper()
        if selected_currency_from in currency_list:     # checks if the selected currency is available for conversion
            break
        else:       # if not, ask the user to enter a currency code that is available for conversion
            print("Please enter a currency code that is available for conversion.")

    while True:      # this loop forces the user to enter a valid input
        selected_currency_to = input("Please enter a currency code (e.g. US = USD) that you would like to convert to: ").strip().upper()
        if selected_currency_to in currency_list:       # checks if the selected currency is available for conversion
            break
        else:       # if not, ask the user to enter a currency code that is available for conversion
            print("Please enter a currency code that is available for conversion.")

    while True:     # this loop forces the user to enter a valid input
        try:        # when user enters a number, it will try to convert it using float
            converting_value = float(input("Please enter an amount that you would like to convert: "))
            if converting_value < 0:        # checks if the amount is in the right range
                print("Please enter a value larger than 0.")     # if not, ask the user to enter an amount in the right range
            else:
                break
        except ValueError:      # when the input is not a number, it prints out an error message and rerun the loop
            print("Please enter a valid input.")

    exchange_rate, reversed_exchange_rate, converted_value = calculate_converted_value(selected_currency_from, selected_currency_to, converting_value)
    print("---------------------------------------------------------\n"     # print out the answer and the exchange rates
          "As of {4} the outcome of your conversion is: \n"
          "{2} {0} = {3} {1} \n"
          "1 {0} = {5} {1} \n"
          "1 {1} = {6} {0} ".format(selected_currency_from, selected_currency_to, converting_value, converted_value, last_updated, exchange_rate, reversed_exchange_rate))

    while True:     # this loop forces the user to enter a valid input
        choice_reverse = input("Do you want to convert from {} to {} ? Type Y for yes and N for no.".format(selected_currency_to, selected_currency_from)).strip().upper()
        if choice_reverse == "Y":       # if user wants to know the reverse value, run calculation
            reversed_exchange_rate, exchange_rate, reversed_converted_value = calculate_reversed_converted_value(selected_currency_from, selected_currency_to, converting_value)
            print("---------------------------------------------------------\n"     # print out the answer and the exchange rates
                  "As of {4} the outcome of your conversion is: \n"
                  "{2} {1} = {3} {0} \n"
                  "1 {1} = {6} {0} \n"
                  "1 {0} = {5} {1} ".format(selected_currency_from, selected_currency_to, converting_value, reversed_converted_value, last_updated, exchange_rate, reversed_exchange_rate))
            break       # prevents infinite loop
        elif choice_reverse == "N":
            break       # because user doesn't want it, exit the loop
        else:           # asks for a valid input
            print("Please enter either Y or N.")

    while True:     # this loop forces the user to enter a valid input
        confirm = input("Would you like to keep converting? Type Y for yes and N for no.").strip().upper()
        if confirm == "Y":      # if user wants to continue converting, return to the beginning
            break               # prevents infinite loop
        elif confirm == "N":    # if user wants to stop, exit program
            still_converting = False
            break
        else:       # asks for a valid input
            print("Please enter either Y or N.")
