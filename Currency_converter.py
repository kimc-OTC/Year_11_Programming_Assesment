# Currency Converter Program

# list of currencies that are available for conversion
currency_list = ["USD", "EUR", "JPY", "GBP", "AUD", "CAD", "CHF", "CNY", "SEK", "NZD", "MEX", "SGD", "HKD", "NOK", "KRW", "TRY", "INR", "RUB", "BRL", "ZAR"]
# list of exchange rates: 1NZD to list of currencies that are available for conversion
exchange_rate_list = [0.7, 0.6, 76.95, 0.5, 0.95, 0.88, 0.64, 4.52, 6.07, 1, 14, 0.95, 5.42, 6.25, 801.03, 6.04, 51.91, 51.37, 3.65, 10.3]
last_updated = "11/08/2021 14:10"
still_converting = True


def calculate_converted_value(currency_from, currency_to, value):
    currency_from_position = currency_list.index(currency_from)
    currency_to_position = currency_list.index(currency_to)
    rate = exchange_rate_list[currency_to_position] / exchange_rate_list[currency_from_position]  # $1 to = from
    reversed_rate = exchange_rate_list[currency_from_position] / exchange_rate_list[currency_to_position]
    answer = float("{:.2f}".format(rate * value))
    return rate, reversed_rate, answer


def calculate_reversed_converted_value(currency_from, currency_to, value):
    currency_from_position = currency_list.index(currency_from)
    currency_to_position = currency_list.index(currency_to)
    reversed_rate = exchange_rate_list[currency_from_position] / exchange_rate_list[currency_to_position]
    rate = exchange_rate_list[currency_to_position] / exchange_rate_list[currency_from_position]  # $1 to = from
    reversed_answer = float("{:.2f}".format(reversed_rate * value))
    return reversed_rate, rate, reversed_answer


while still_converting:     # while user wants to keep converting, run the loop
    print("These are the currencies available for converting: \n"
          "US Dollar (USD), Euro (EUR), Yen (JPY), Pound Sterling (GBP), Australian Dollar (AUD), Canadian (CAD), Swiss Franc (CHF), Chinese Renminbi (CNY), Swedish Krona (SEK), New Zealand Dollar (NZD), Mexican Peso (MEX), Singapore Dollar (SGD), Hong Kong Dollar (HKD), Norwegian Krone (NOK), South Korea Won (KRW), Turkish Lira (TRY), Indian Rupee (INR), Russian Ruble (RUB), Brazilian Real (BRL), South African Rand (ZAR)")

    while True:     # this loop forces the user to enter a valid input
        selected_currency_from = input("Please enter a currency code (e.g. US = USD) that you would like to convert from:").strip().upper()
        if selected_currency_from in currency_list:     # checks if the selected currency is available for conversion
            break
        else:       # if not, ask the user to enter a currency code that is available for conversion
            print("Please enter a currency code that is available for conversion.")

    while True:      # this loop forces the user to enter a valid input
        selected_currency_to = input("Please enter a currency code (e.g. US = USD) that you would like to convert to:").strip().upper()
        if selected_currency_to in currency_list:       # checks if the selected currency is available for conversion
            break
        else:       # if not, ask the user to enter a currency code that is available for conversion
            print("Please enter a currency code that is available for conversion.")

    while True:     # this loop forces the user to enter a valid input
        try:        # when user enters a number, it will try to convert it using float
            converting_value = float(input("Please enter an amount that you would like to convert:"))
            if converting_value < 0:        # checks if the amount is in the right range
                print("Please enter a value larger than 0")     # if not, ask the user tp enter an amount in the right range
            else:
                break
        except ValueError:      # when the input is not a string, it prints out an error message and rerun the loop
            print("Please enter a valid input")

    exchange_rate, reversed_exchange_rate, converted_value = calculate_converted_value(selected_currency_from, selected_currency_to, converting_value)
    print("The outcome of your conversion from {0} to {1} of {2} is {3} at {4}. \n"
          "The exchange rate from {0} to {1} is {5}. \n"
          "The exchange rate from {1} to {0} is {6}.".format(selected_currency_from, selected_currency_to, converting_value, converted_value, last_updated, exchange_rate, reversed_exchange_rate))

    reversed_exchange_rate, exchange_rate, reversed_converted_value = calculate_reversed_converted_value(selected_currency_from, selected_currency_to, converting_value)
    print("The outcome of your conversion from {1} to {0} of {2} is {3} at {4}. \n"
          "The exchange rate from {0} to {1} is {5}. \n"
          "The exchange rate from {1} to {0} is {6}.".format(selected_currency_from, selected_currency_to, converting_value, reversed_converted_value, last_updated, exchange_rate, reversed_exchange_rate))
