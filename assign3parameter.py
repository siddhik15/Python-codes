#Function with parameter
def Addition(no,no2):
    ans= no + no2
    return ans
print(Addition(5,6))
#Function without parameter
def Addition():
    x=int(input("Enter the no:"))
    y=int(input("Enter the no"))
    return x+y

result=Addition()
print(result)