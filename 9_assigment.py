## A restaurant has 53 customers. Each table can seat 6 customers.

### Task:
    # Create variables for:

    #     total_customers = 6
    #     customers_per_table = 53
    #     filled_tables = customers_per_table % total_customer
    #     print("The maximum number of completely filled tables is", filled_tables)


### Then calculate and print the maximum number of completely filled tables.

total_customers = 6
customers_per_table = 53
filled_tables = customers_per_table // total_customers
print("The maximum number of completely filled tables is", filled_tables)