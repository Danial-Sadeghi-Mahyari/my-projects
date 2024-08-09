import pandas as pd
import yfinance as yf
from matplotlib import pyplot as plt
# # # We must import libraries which are needed.

df = yf.download("BTC-USD", start="2015-01-01", end="2024-01-01")
# # # At first we download dataframe of Bitcoin's information during 9 years with yfinance library (from first of 2015 to end of 2023)
# print(df)
# print(type(df))
# # # We can print our df and df's type to see them.

df["Date"] = df.index
# # # We assign df's indexes to Date column, it means we create a new column that name is Date.
# df.info()
# # # We can also see information of our df.

df.drop(columns=["Adj Close"], inplace=True)
# # # We drop out Adj Close column because it is as same as Close column.
df["Month"] = df["Date"].apply(lambda d: d.month)
# # # We add a new column to our df which name is Month and it shows us number of month in each year.
df["Tolerance"] = df["High"] - df["Low"]
# # # We add another new column to our df that name is Tolerance with it's own formula -> (The highest price - The Lowest price)
df.drop(columns=["Date"], inplace=True)
# # # We drop out Date columns because the type of that is datetime and it can't calculate in Sum function.
df = df.groupby("Month").sum()
# # # We group our df in depends on Month and then calculate Sum of that.


df.index = ["January", "February", "March", "April", "May",
            "June", "July", "August", "September", "October", "November", "December"]
# # # We assign names of months to our indexes.

print(df)
print("-"*120)
print(df["Tolerance"].idxmax(),
      "is a month of year which has the most Tolerance, so", df["Tolerance"].idxmin(), "is the Worst month to have an investment")
print(df["Tolerance"].idxmin(),
      "is a month of year which has the least Tolerance, so", df["Tolerance"].idxmin(), "is the Best month to have an investment")
# # # We print df and a day of week which has the most and the least Tolerance.

print("-"*120)
anwser = input(
    "Do you want to display a Scatter of Tolerance's amount in each Month of year ??? type (yes) to show  -> ")
# # # Here we have a question
if anwser == "yes":
    plt.figure(figsize=(9, 7))
    plt.scatter(df.index, df["Tolerance"], s=100)
    plt.xticks(rotation=25, size=10)
    plt.xlabel("Months", color="purple", size=12)
    plt.ylabel("Tolerance", color="red")
    plt.title("Amount of Tolerance in each Month of Year")
    plt.show()
# # # If your anwser was (yes), program would show you a Scatter of Tolerance's amount.
else:
    pass
# # # If you typed sth except (yes), program wouldn't do anything.
