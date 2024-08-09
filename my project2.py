from matplotlib import pyplot as plt
import pandas as pd
import yfinance as yf
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
# # # We drop out Adj Close column because it is as eqaule as Close column.
df["Month"] = df["Date"].apply(lambda d: d.month)
# # # We add a new column to our df which name is Month and it shows us number of month in each year.
df["Benefit"] = df["Close"] - df["Open"]
# # # We add another new column to our df which name is Benefit with it's own formula -> (price of close - price of open)
df.drop(columns=["Date"], inplace=True)
# # # We drop out Date column because the type of that is datetime64 and it can't calculate in Sum function.

benefit = df[df["Benefit"] > 0]
loss = df[df["Benefit"] < 0]
# print(type(benefit))
# print(type(loss))
# # # We devide Benefit column in to 2 new dataframes. positive(benefit) and negetive(loss).
benefit_sum = benefit.groupby("Month").sum()
loss_sum = loss.groupby("Month").sum()
# # # We group these 2 dataframes in depend on Month and then calculate Sum of them and assign them into benefit_sum (type == df) ->
# and loss_sum (type == df).

# # # In this program we just consider benefit, not a loss. That's a reason why we devided our df in to 2 group ->
# (benefit_sum and loss_sum)
benefit_sum["Month"] = benefit_sum.index
# # # We make Month column with our indexes.

benefit_sum.index = ["January", "February", "March", "April", "May",
                     "June", "July", "August", "September", "October", "November", "December"]
# # # We assign names of months to our indexes.

print(benefit_sum)
print("-"*120)
print(benefit_sum["Benefit"].idxmax(),
      "is a month which has the most benefit, so", benefit_sum["Benefit"].idxmax(), "is the Best month to have an investment")
print(benefit_sum["Benefit"].idxmin(),
      "is a month which has the least benefit, so", benefit_sum["Benefit"].idxmin(), "is the Worst month to have an investment")
# # # we print benefit_sum df and a Month which has the most and the least benefit (we don't consider loss!!!).

print("-"*120)
anwser = input(
    "Do you want to display a Scatter of Benefit's amount in each Month of Year ??? type (yes) to show -> ")
# # # Here we have a question
if anwser == "yes":
    plt.figure(figsize=(9, 7))
    plt.scatter(benefit_sum.index, benefit_sum["Benefit"], s=100)
    plt.xticks(rotation=25, size=10)
    plt.xlabel("Months", color="purple", size=12)
    plt.ylabel("Benefit", color="red")
    plt.title("Amount of Benefit in each Month of Year")
    plt.show()
# # # If your anwser was (yes), program would show you a Scatter of Benefit's amount.
else:
    pass
# # # If you typed sth except (yes), program wouldn't do anything.
