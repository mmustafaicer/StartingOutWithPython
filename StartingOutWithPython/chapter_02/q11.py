# Male and Female Percentages

# Ask user for male and female numbers

male=int(input("Please enter the number of males in the class: "))
female=int(input("Please enter the number of females in the class: "))
total=male+female

# Calculate the percentages.
p_male=(male/total)*100
p_female=(female/total)*100

# Display the data.
print()
print("Male is %", p_male, sep='')
print("Female is %", p_female, sep='')
