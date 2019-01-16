base_hours=40       # according to question this is benchmark. After that it is overtime.
ot_multiplier=1.5   # over time multiplier

# get the hours worked and the hourly pay rate.
hours=float(input("Enter the number of hours worked: "))
pay_rate=float(input("Enter the hourly pay rate: "))

print()
if hours>base_hours:
    # Calculate the gross pay
    overtime_hours=hours-base_hours # overtimed hours
    overtime_pay=overtime_hours*pay_rate*ot_multiplier
    gross_pay=(base_hours*pay_rate)+overtime_pay
    
else:
    # Calculate the gross pay without overtime
    gross_pay=hours*pay_rate
    
# Display the gross pay
print("The gross pay is $", format(gross_pay, ",.2f"), sep='')