# ## A customer gets a free delivery if their order is Rs. 2,000 or more or they have a premium membership.

# #### The customer’s order is Rs. 1,500 and they have a premium membership.

#     Create variables for the order amount and membership status, then check whether the customer gets free delivery.
    
#     Print the result.



order_amount = 1500
premium_member = True

free_delivery = order_amount >= 2000 or premium_member

print(free_delivery)