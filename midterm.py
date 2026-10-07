#=>Question 1: Mixing a Solution
def final_concentration(volume,concentration,water):
    pure_substance=volume*concentration/100
    total_volume=volume+water
    final=(pure_substance/total_volume)*100
    return final

volume=float(input("Enter the volume of concentrated liquid (mL): "))
concentration=float(input("Enter its concentration (%): "))
water=float(input("Enter the amount of water added (mL): "))
print()
print("Final concentration:",round(final_concentration(volume,concentration,water),2),"%")


#=>Question 2: Movie Ticket Price
def calculate_ticket(age,weekend):
    if age<5:
        return 0
    elif age<=17:
        price=8
    elif age<=64:
        price=15
    else:
        price=10

    if weekend=="yes":
        price+=3
    return price

age=int(input("Enter your age: "))
weekend=input("Is it the weekend? ")
print()
print("Ticket price: $"+str(calculate_ticket(age,weekend)))


#=>Question 3: Electricity Consumption
total_consumption=0
total_cost=0
days_above_20=0

for day in range(1,8):
    consumption=float(input("Enter consumption for day "+str(day)+": "))
    if consumption<=20:
        daily_cost=consumption*0.10
    else:
        daily_cost=consumption*0.15
        days_above_20+=1
    total_consumption+=consumption
    total_cost+=daily_cost

print()
print("Total consumption:",total_consumption,"kWh")
print("Days above 20 kWh:",days_above_20)
print("Total cost: $"+str(round(total_cost,2)))


#=>Question 4: Zero One Pattern
n=int(input("Enter a positive integer: "))
print()
for row in range(1,n+1):
    for column in range(1,n+1):
        if row%2==1:
            print("0",end=" ")
        else:
            print("1",end=" ")
    print()
