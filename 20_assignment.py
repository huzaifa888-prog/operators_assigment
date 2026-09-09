### You are creating a student result calculator.

# A student has:

#     Mathematics: 85
#     English: 72
#     Python: 90
#     Total possible marks per subject: 100
#     Student name: "Ahmed"
#     Required passing marks per subject: 50

# ### Create variables and:

#     Calculate the student's total marks 
#     Calculate the average marks.
#     Calculate the percentage.
#     Check whether the student passed Mathematics.
#     Check whether the student passed all three subjects.
#     Check whether the name contains the letter "A".
#     Check whether the average marks are greater than or equal to 80.
#     Store the final percentage and check whether it is truthy.

# Print all results.

name = "Ahmed"

math = 85
english = 72
python = 90

total_possible = 300
passing_marks = 50

# Total marks
total_marks = math + english + python

# Average
average = total_marks / 3

# Percentage
percentage = (total_marks / total_possible) * 100

# Mathematics pass?
math_passed = math >= passing_marks

# All subjects passed?
all_passed = math >= passing_marks and english >= passing_marks and python >= passing_marks

# Name contains "A"?
contains_A = "A" in name

# Average >= 80?
average_check = average >= 80

# Percentage truthy?
percentage_truthy = bool(percentage)

# Print results
print("Student Name:", name)
print("Total Marks:", total_marks)
print("Average Marks:", average)
print("Percentage:", percentage)
print("Passed Mathematics:", math_passed)
print("Passed All Subjects:", all_passed)
print("Name Contains A:", contains_A)
print("Average >= 80:", average_check)
print("Percentage is Truthy:", percentage_truthy)
