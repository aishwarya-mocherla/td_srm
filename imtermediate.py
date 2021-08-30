#RANDOM PASSWORD (the square of sum of both digits of your date wrapped in first two and last two letters of your name wrapped in between first digit and last digit of your birth date and the whole thing reversed)
# name: junaid dob:25 ;;;; pw= 5diuj2
name = input("enter name (firstname): ")
dob = input("enter date of birth (DD): ")
one = dob[0]
two = name[0:2]
three = name[-2:]
four = dob[-1]
five = (int(one) + int(four))**2
five = str(five)
ans1 = one + two + five +three + four 
print(ans1[ : :-1])