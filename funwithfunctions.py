#Create a function called odd_even that counts from 1 to 2000. As your loop executes have your program print the number of that iteration and specify whether it's an odd or even number.
def odd_even():
for i in range(0, 2000):
    if i%2 == 0:
      print i, "This is an even number."
    else:
      print i, "This is an odd number."


#Create a function called 'multiply' that iterates through each value in a list (e.g. a = [2, 4, 10, 16]) and returns a list where each value has been multiplied by 5.

def multiply(arr,num):
    for x in range(len(arr)):
        arr[x] *= num
    return arr
a = [2,4,10,16]
b = multiply(a,5)
print b

#Hacher Challenge

def layered_multiples(multiplied_list):
    new_list = []
    for num in multiplied_list:
        new_list.append([1] * num)
    return new_list

print layered_multiples(multiply([2,4,5], 2 ))
