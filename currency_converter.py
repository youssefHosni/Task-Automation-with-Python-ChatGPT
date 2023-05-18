import argparse
from forex_python.converter import CurrencyRates, CurrencyCodes

# Initialize the currency rates and codes objects
c = CurrencyRates()
codes = CurrencyCodes()

# Set up the argument parser
parser = argparse.ArgumentParser(description="Convert currencies using forex-python")
parser.add_argument("amount", type=float, help="The amount to convert")
parser.add_argument("from_currency", type=str, help="The currency you're converting from (e.g. USD)", metavar="from")
parser.add_argument("to_currency", type=str, help="The currency you're converting to (e.g. EUR)", metavar="to")

# Parse the arguments
args = parser.parse_args()

# Get the amount and currencies from the arguments
amount = args.amount
from_currency = args.from_currency.upper()
to_currency = args.to_currency.upper()

# Get the currency symbols for display purposes
from_symbol = codes.get_symbol(from_currency)
to_symbol = codes.get_symbol(to_currency)

# Convert the currencies
result = c.convert(from_currency, to_currency, amount)

# Print the result
print(f"{from_symbol}{amount:.2f} {from_currency} is equal to {to_symbol}{result:.2f} {to_currency}")
