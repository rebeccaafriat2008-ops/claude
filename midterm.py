#=>Question 1: Mixing a Solution
#Part 1 - define the function
def final_concentration(volume,concentration,water):
    pure_substance=volume*concentration/100
    total_volume=volume+water
    final=(pure_substance/total_volume)*100
    return final

#Part 2 - test the function
volume=float(input("Enter the volume of concentrated liquid (mL): "))
concentration=float(input("Enter its concentration (%): "))
water=float(input("Enter the amount of water added (mL): "))
print()
print("Final concentration:",round(final_concentration(volume,concentration,water),2),"%") #test the function with passing real values


#=>Question 2: Movie Ticket Price
#Part 1 - define the function
def calculate_ticket(age,weekend):
    if age<5:            #children under 5 are always free
        return 0
    elif age<=17:        #5-17
        price=8
    elif age<=64:        #18-64
        price=15
    else:                #65 or older
        price=10

    if weekend=="yes":   #on weekends $3 is added
        price+=3         #price=price+3
    return price

#Part 2 - test the function
age=int(input("Enter your age: "))
weekend=input("Is it the weekend? ")
print()
print("Ticket price: $"+str(calculate_ticket(age,weekend))) #test the function with passing real values


#=>Question 3: Electricity Consumption
total_consumption=0  #for the total electricity consumption
total_cost=0         #for the total electricity cost
days_above_20=0      #for how many days had consumption greater than 20 kWh

for day in range(1,8):
    consumption=float(input("Enter consumption for day "+str(day)+": "))
    if consumption<=20:
        daily_cost=consumption*0.10
    else:
        daily_cost=consumption*0.15
        days_above_20+=1          #days_above_20=days_above_20+1
    total_consumption+=consumption  #total_consumption=total_consumption+consumption
    total_cost+=daily_cost          #total_cost=total_cost+daily_cost

print()
print("Total consumption:",total_consumption,"kWh")
print("Days above 20 kWh:",days_above_20)
print("Total cost: $"+str(round(total_cost,2)))


#=>Question 4: Zero One Pattern
n=int(input("Enter a positive integer: "))
print()
for row in range(1,n+1): #outer loop for changing the row
    for column in range(1,n+1): #inner loop for printing a number at each column
        if row%2==1:     #odd rows print 0
            print("0",end=" ")
        else:            #even rows print 1
            print("1",end=" ")
    print() #changing the row (part of the outer loop)
