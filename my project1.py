import pandas as pd
import yfinance as yf
from matplotlib import pyplot as plt
# # # We must import libraries which are needed.

df = yf.download("BTC-USD", start="2015-01-01", end="2024-01-01")
# # # At first we download dataframe of Bitcoin's information during 9 years with yfinance library
# print(df)
# print(type(df))
# # # We can print our df and df's type to see them.

df["Date"] = df.index
# # # We assign df's indexes to Date column.
# df.info()
# # # We can also see information of our df.

df.drop(columns=["Adj Close"], inplace=True)
# # # We drop out Adj Close column because it is as same as Close column.
df["Weekday"] = df["Date"].apply(lambda d: d.isoweekday())
# # # We add a new column to our df which name is Weekday and it shows us number of day in each week.
df["Benefit"] = df["Close"] - df["Open"]
# # # We add another new column to our df which name is Benefit with it's own formula -> (price of close - price of open)
df.drop(columns=["Date"], inplace=True)
# # # We drop out Date columns because the type of that is datetime and it can't calculate in Sum function.

benefit = df[df["Benefit"] > 0]
loss = df[df["Benefit"] < 0]
# print(type(benefit))
# print(type(loss))

# # # We devide Benefit column in to 2 new dataframes. positive(benefit) and negetive(loss).
benefit_sum = benefit.groupby("Weekday").sum()
loss_sum = loss.groupby("Weekday").sum()
# # # We group these 2 dataframes in depends on weekday and then calculate Sum of them and assign them into benefit_sum (type == df)
# and loss_sum (type == df).

# # # In this program we just consider benefit, not a loss. That's a reason why we devided our df in to 2 group ->
# (benefit_sum and loss_sum)

benefit_sum["Weekday"] = benefit_sum.index
# # # We make Weekday column with our indexes.

benefit_sum.index = ["Saturday", "Sunday", "Monday",
                     "Tuesday", "Wednesday", "Thursday", "Friday"]
# # # We assign names of weekday to our indexes.

print(benefit_sum)
print("-"*120)
print(benefit_sum["Benefit"].idxmax(), "is a day which has the most benefit, so",
      benefit_sum["Benefit"].idxmax(), "is the Best day of week to have an investment")
print(benefit_sum["Benefit"].idxmin(), "is a day which has the least benefit, so",
      benefit_sum["Benefit"].idxmin(), "is the Worst day of week to have an investment")
# # # We print benefit_sum df and a day which has the most and the least benefit (we don't consider loss!!!).

print("-"*120)
anwser = input("Do you want to display a Scatter of Benefit's amount in each Day of Week ??? type (yes) to show  -> ")
# # # Here we have a question
if anwser == "yes":
    plt.scatter(benefit_sum.index, benefit_sum["Benefit"], s=100)
    plt.xlabel("Days", color="blue")
    plt.ylabel("Benefit", color="red")
    plt.title("Amount of Benefit in each Day of Week")
    plt.show()
# # # If your anwser was (yes), program would show you a Scatter of Benefit's amount.
else:
    pass
# # # If you typed sth except (yes), program wouldn't do anything.
