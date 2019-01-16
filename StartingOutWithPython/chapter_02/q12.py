# Stock Transaction Program

# These are the given variables in the question.
num_share=2000          # Number of shares
per_share_before=40     # Value of each share when he purchased
com_rate=0.03           # Commission rate for stockbroker
per_share_after=42.75   # Value of each share when sells
commission1=per_share_before*num_share*com_rate # Commission when he buys
commission2=per_share_after*num_share*com_rate  # Commission when he sells

print("The amount of money Joe paid for the stock is $", num_share*per_share_before, sep='' )
print("The amount of commission Joe paid his broker when he bought the stock is $", \
      num_share*per_share_before*com_rate, sep='')
print("The amount that Joe sold the stock for is $", num_share*per_share_after, sep='')
print("The amount of commission Joe paid his broker when he sold the stock is $", \
      num_share*per_share_after*com_rate, sep='')
print("Joe made a profit amount of $", \
      ((per_share_after-per_share_before)*2000)-(commission1+commission2))