laptop_price = 85000
student_has = 100000
discount = 5000
laptop_bag_cost = 2500
promotion_code = "SAVE10"

laptop_after_discount = laptop_price - discount
final_bill = laptop_bag_cost + laptop_after_discount
remaining_money = student_has - final_bill
enough_money = student_has >= final_bill
promotion_check = "SAVE10" in promotion_code
bill_check = final_bill > 80000
enough_money_truthy = bool(enough_money)

print("LAptop Price After Discount:", laptop_after_discount)
print("Final bill:", final_bill)
print("Remaining money:", remaining_money)
print("Student has enough money:", enough_money)
print("SAVE10 present:", promotion_check)
print("Final Bill Greater Than 80000:", bill_check)
print("Enough Money is Truthy:", enough_money_truthy)
