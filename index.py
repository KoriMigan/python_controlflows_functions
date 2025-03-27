# function to calculate the final price after applying a discount

def calculate_discount(price, discount_percent):
       if discount_percent >= 20:
           return price - (price * discount_percent/100)
       else:
           return price

# creating variables for user's values
original_price= float(input("Enter the original price of the item: "))
discount_percentage= float(input("Enter the discount percentage the item: "))


# use of the above created function to calculate the final price 
final_price= calculate_discount(original_price, discount_percentage)
print(f"The final price of the item is:", final_price)




    