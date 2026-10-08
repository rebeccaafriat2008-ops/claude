#==================Midterm Exam==================

# #=>Question 1: Average Speed of a Trip
# def average_speed(distance1,time1,distance2,time2):
#     total_distance=distance1+distance2
#     total_time=time1+time2
#     average=total_distance/total_time
#     return average
#
# distance1=float(input("Enter first distance (km): "))
# time1=float(input("Enter first travel time (hours): "))
# distance2=float(input("Enter second distance (km): "))
# time2=float(input("Enter second travel time (hours): "))
# print()
# print("Average speed:",round(average_speed(distance1,time1,distance2,time2),2),"km/h")

# #=>Question 2: Student Result
# def student_result(midterm,final_exam):
#     final_grade=midterm*0.40+final_exam*0.60
#     if final_grade>=80:
#         return "Excellent"
#     elif final_grade>=60:
#         return "Pass"
#     else:
#         return "Fail"
#
# midterm=float(input("Enter midterm grade: "))
# final_exam=float(input("Enter final exam grade: "))
# print()
# print("Result:",student_result(midterm,final_exam))

# #=>Question 3: Number Processing
# total=0
# divisible_by_three=0
# for count in range(1,7):
#     number=int(input("Enter number "+str(count)+": "))
#     if number%2==0: #if number is even
#         total+=number/2 #total=total+number/2
#     else: #if number is odd
#         total+=number*2 #total=total+number*2
#     if number%3==0:
#         divisible_by_three+=1
#
# print()
# print("Calculated total:",total)
# print("Numbers divisible by 3:",divisible_by_three)

#=>Question 4: Middle Cross Pattern
n=int(input("Enter a positive odd integer: "))
middle=n//2 #the index of the middle row and middle column
for row in range(n): #outer loop for changing the row
    for column in range(n): #inner loop for printing the symbol at each column
        if row==middle or column==middle:
            print("+",end=" ")
        else:
            print("-",end=" ")
    print() #changing the row
