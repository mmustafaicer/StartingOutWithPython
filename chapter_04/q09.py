# ocean levels
# set an accumulator
yearly_increase=0

start_year=2019
end_year=2044

# print headings
print("Years\t\tOcean Rise in mm")
print("--------------------------------")

for y in range (start_year, end_year+1, 1):
    yearly_increase+=1.6
    print(y, "\t\t", format(yearly_increase, ".1f"))