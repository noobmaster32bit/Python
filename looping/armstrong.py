num=input("Enter a number : ") #153
length=len(num)
num=int(num)
real=num # this real variable is used to check for armstrong number becos the value of num after exiting the while loop is 0 so num cannot be compared with sum so another variable is used to store the initial vale of num and is compared with the num to check for armstrong number.
sum=0

while (num!=0):
    digit=num%10
    exp=digit**length
    sum=sum+exp
    num=num//10

print(f"{real} is armstrong number" if sum==real else " not armstrong")
