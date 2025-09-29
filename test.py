print("hello world")
# this is the first pull
x = 10
print(x==10)
print(x==11)
print(x>12)
print("\n lets make it more fun")
Name= "tamin"
age= 33
if Name=="tamin" and age==33:
    
    print()
    age = 32
    print ("your name is", Name, " and you are ",age ,"years old")

new_variable =102
new_variable_second =101
first_array = [1,2]
second_array = []

if new_variable > 101:
    print("1")

if first_array:
    print("2")

if len(first_array)==2:
    print("3")

if len(first_array) + len(second_array)==2:
    print("4")
elif second_array is first_array:
    print("mattch found")
else:
    print("match not found")