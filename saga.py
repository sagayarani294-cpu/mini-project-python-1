id = input("Enter employee ID:")
name = input("Enter name:")
salary = float (input("Enter basic salary:"))


allowance = salary * 0.15
deduction = salary * 0.05
net_salary =salary +allowance - deduction


print("\nEmployee details")
print("ID:",id)
print("Name:" ,name)
print("Basic salary:",salary)
print("allowance:", allowance)
print("deduction:" ,deduction)
print("Net salary:" ,net_salary)
