# dashboard_generator.py

import os
import csv
import pandas

#Receive input for the Year
#Receive input for the Month
#concatenate the Year and month onto the file name below


csv_file_path = os.path.join(os.path.dirname(__file__), "..", "data", "monthly-sales", "sales-201710.csv")

df = pandas.read_csv(csv_file_path)
pandas.options.display.float_format = '${:,.2f}'.format

def to_usd(my_price):
    """
    Converts a numeric value to usd-formatted string, for printing and display purposes.

    Param: my_price (int or float) like 4000.444444

    Example: to_usd(4000.444444)

    Returns: $4,000.44
    """
    return f"${my_price:,.2f}" #> $12,000.71

#total_sales = 0
#with open(csv_file_path, "r") as csv_file: # "r" means "open the file for reading"
#    reader = csv.DictReader(csv_file) # assuming your CSV has headers
#    # reader = csv.reader(csv_file) # if your CSV doesn't have headers
#    for row in reader:
#        total_sales = total_sales + float(row["sales price"])


print("-----------------------")
print("MONTH: March 2018")

print("-----------------------")
print("CRUNCHING THE DATA...")

print("-----------------------")
print("TOTAL MONTHLY SALES:", to_usd(df["sales price"].sum()))

print("-----------------------")
print("TOP SELLING PRODUCTS:")
top_sellers = df.groupby(["product"]).sum()
top_sellers = top_sellers.sort_values('sales price', ascending=False)
top_sellers = top_sellers.reset_index()
top_sellers.index = top_sellers.index + 1
print(top_sellers[["product" , "sales price"]].to_string(header=False))

print("-----------------------")
print("VISUALIZING THE DATA...")