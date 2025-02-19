# write a program to print numbers from  -1 to -10

for i in range(-1,-11,-1):
    print(i)

# sum of digits in a number  - and add when it is even 

number=int(input("Enter a number to check: "))
check_number=number
sum=0
while check_number>0:
    res=check_number%10
    check_number=check_number//10
    if res%2==0:
        sum+=res
print(sum)

# using functions

def even_sum_number(number):
    check_number=number
    sum=0
    while check_number>0:
        res=check_number%10
        check_number=check_number//10
        if res%2==0:
            sum+=res
    return "SUM: ",sum
number=int(input("Enter a number to check: "))  
print(even_sum_number(number))    

# prime number or not prime

def prime_check(num_input):
    if num_input <= 1:
        return False  # 0 and 1 are not prime numbers
    
    for i in range(2, int(num_input ** 0.5) + 1): 
        if num_input % i == 0:
            return False  
    
    return True  

num_input = int(input("Enter a number: "))
res = prime_check(num_input)
print(f"{num_input} is {'a prime number' if res else 'not a prime number'}")

number=56565
temp=number
sum=0
while temp>0:
    res=temp%10
    temp=temp//10
    for i in range(2,res+1):
        if res%i==0:
            sum+=res
        else:
            pass    
print(sum)


# checking amstrong number
number=int(input("Enter: "))
sum=0
temp=number
while temp>0:
    rem=temp%10
    print(rem)
    sum+=rem**3
    temp=temp//10

print(("amstrong")if sum==number else print("Not amstrong"))    


# in the range

lower_var=100
highere_var=999
for i in range(lower_var,highere_var+1):
    len_num=len(str(i))
    temp=i
    sum=0
    while temp>0:
      res=temp%10
      sum+=res**len_num
      temp=temp//10
    if i==sum:
       print(i)

# febanacci series
input_num=int(input('Enter your number: '))
n1=0
n2=1
print(n1)
print(n2)
for i in range(0,input_num+1):
    temp=n1+n2
    n1=n2
    n2=temp
    print(n2)

    # # 1. Create a function that takes two numbers as arguments and returns their sum.

def sum_two_Arguments():
    x=int(input("Enter X value: "))
    y=int(input("Enter y value: "))
    return x+y
print("1) FIRST QUESTION")    
result=sum_two_Arguments()
print("sum of two arguments is :",result)

# ======================================================================
#  2. Write a function that takes an integer minutes and converts it to seconds.

def min_sec_conversion():
    x1=int(input("Enter minutes: "))
    return x1*60
print("2) MINUTES TO SECONDS CONVERSION")
result1=min_sec_conversion()
print("seconds is:",result1)
# ============================================================================
#  3. Create a function that takes two arguments. Both arguments are integers, a and b. Return true if one of them is 10 or if their sum is 10.

print("3) CHECKING EITHER VALUE IS TRUE OR FALSE")
def check_number():
    x2=int(input("Enter a x2 value:"))
    x3=int(input("Enter a x3 value:"))
    if x2==10 or x3==10 or (x2+x3)==10:
        return True
    else:
        return False
result3=check_number()

print("Conditions are met: ",result3)

# ===========================================================================================

#  4. Create a function that takes two strings as arguments and returns either true or false
#  depending on whether the total number of characters in the first string is equal to the total
#  number of characters in the second string.

print("4) STRINGS LENGTH EQUAL ARE NOT")
def strings_equal():
    x4=str(input("Enter first string: "))
    x5=str(input("Enter second string: "))
    if len(x4)==len(x5):
        return True
    else:
        return False
res=strings_equal()

print("result=",res)

# ================================================================================================

#  5. Create a function that takes an array of numbers and returns the largest number.

def Largest_Number(arr):
    if not arr:
        return None
    Largest=arr[0]
    for number in arr:
        if number>Largest:
            Largest=number
    return Largest
arr=[5,7,9,1,2]    
res1=Largest_Number(arr)
print("5) LARGEST IN ARRAY")
print("given array:",arr, "Largest is:",res1)
# =====================================================================================================


#  6. Create a function that takes two strings as arguments and returns the number of times the first
#  character (the single character) is found in the second string.

def length_character_in_string(alphabet,text):
    count=text.count(alphabet)
    return count
alphabet=str(input("Enter Alphabet: "))
text=str(input("Enter Character: "))
res2=length_character_in_string(alphabet,text)
print("6) CHARACTER COUNT IN TEXT: ",res2)

# ======================================================================


#  7. Create a function that takes a string and returns the number (count) of vowels contained within it

def vowel_check(str1):
    vowels="aeiouAEIOU"
    count=0
    for i in vowels:
        if i in str1:
            count+=1
    return count
str1="WelCOmE to PytHOn"
res5=vowel_check(str1)  
print("7) CHECKS VOWEL IN TEXT")
print("given string is: ",str1 ,"count is:",res5)


# =================================================================================

#  8. Given a string, create a function to reverse the string.


def reverse_str(text2):
    return text2[::-1]
text2="WELCOME TO PYTHON"
res6=reverse_str(text2)
print("8) STRING REVERSE")
print("given text is: ",text2 ,"output is:",res6 )

# =========================================================================================

#  9. Write a program that defines a function to multiply an integer by 2. Then, loop from 0 to a given
#  integer n, passing each value to the function and printing the result

def multiply_by_2(x):
    return x*2
n = int(input("Enter the number :"))
for i in range(n+1):
    value = multiply_by_2(i)
    print(value)

# ===============================================================================================
 
# 10.Program to find greatest of three numbers


def greatest_number(num4):
    greatest=num4[0]
    for i in num4:
        if i>greatest:
            greatest=i
    return greatest
num4=[5,9,2]
res7=greatest_number(num4)
print("10) GREATEST OF THREE NUMBERS")
print("given input is: ",num4 ,"Output is: ", res7)   

# #  11.Program to find factorial of number.

def factorial_of_num(num7):
    factorial=1
    for i in range(1,num7+1):
        factorial=factorial*i
    return factorial
num7=5
output=factorial_of_num(num7)
print("11) FACTORIAL OF NUMBER")
print("input is:",num7 ,"Output is:",output)

# =============================================================================

#  12.Calculate the Power of a Number(using loop only).

# def power_of_number(num8):
#     for i in range(1,num8+1):
#         i=i*i
#     return i
# num8=12
# output1=power_of_number(num8)
# print("11) POWER OF NUMBER")
# print("input is:",num8 ,"Output is:",output1)


def power_of_number(base,exponent):
    itarable=1
    for i in range(abs(exponent)):
        itarable*=base
    return itarable
base=int(input("Enter base value:")) 
exponent=int(input("Enter exponent value:"))
output2=power_of_number(base,exponent)
print("11) POWER OF NUMBER")
print("output is: ",output2)

# ====================================================================

#  13.Program to Check Whether a Number is Prime or Not

def is_prime(numb):
    if numb<=1:
        return "Not a prime"
    for i in range(2,int(numb**0.5)+1):
        if numb%i==0:
            return "Not a prime"
    return "Its a prime number"
numb=int(input("Enter a number: ")) 
output3=is_prime(numb)
print("13) CHECKING NUMBER IS PRIME OR NOT")
print("output is: ",output3)      

# ==================================================================================

#  14.Program to find a missing number in first n natural numbers

print("14) FINDING MISSING NUMBER IN NUMBERS")
def missing_num_finging(x10):
    n=len(x10)+1
    expected_sum=n*(n+1)//2
    actual_sum=sum(x10)
    missing=expected_sum-actual_sum
    return missing
x10=[1,3,4,5]
output4=missing_num_finging(x10)
print("given input is: ",x10  ,"output is: ",output4)

# ============================================================================

# 15.Program to insert an element in an array at a given index.

def array_element_insertion(element,array,index):
    if index<0 or index>len(array):
        return "Enter vallid index number...!"
    array.insert(index,element)
    return array
array=list(map(int,input("Enter Array: ").split()))
index=int(input("Enter Index number: "))
element=int(input("Enter element : "))
result=array_element_insertion(element,array,index)
print(result)

# =======================================================================================

# 16.Count occurrence of number

def count_occurrence(array1,element):
    count=0
    if element not in array1:
        return "Elemet Not There...!"
    for num in array1:
        if num==element:
            count+=1
    return count
array1=list(map(int,input("Enter Array seperated by spaces:").split()))  
element=int(input("Enter Element: "))
result5=count_occurrence(array1,element)
print("Occurances: ",result5)

# =================================================================================================
#  1. Print Pattern using loop.
n=5
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j, end=" ")
    print()

#  2. Create a function that takes an array of arrays with numbers. Return a new (single) array with the largest numbers of each.

def largest_in_subarray(numbers):
    found=[]
    for i in numbers:
        largest=max(i)
        found.append(largest)
    return found
numbers=[[7,5,9],[9,1,8],[7,8,9]]
result=largest_in_subarray(numbers)
print(result)

#  3. Create a function that takes an array of items, removes all duplicate items and returns a new
#  array in the same sequential order as the old array (minus duplicates).

def removes_duplicates(numbers):
    new_arr=[]
    for i in numbers:
        if i not in new_arr:
            new_arr.append(i)
    return new_arr
numbers=['hi','helloo','how are you','helloo']
result=removes_duplicates(numbers)
print("for input: ",numbers,"output: ",result)

#  4. Program to arrange numbers in ascending order

def ascending_order(numbers):
    order=sorted(numbers)
    return order
numbers=list(map(int,input("Enter numbers seperated by spaces: ").split()))
result=ascending_order(numbers)
print("for input:",numbers,"output:",result)

# 5. Program to count vowels and consonants in a given String.

def vowels_consonents_count(str):
    vowels=0
    consonents=0
    group="aeiouAEIOU"
    for i in str:
        if i in group:
            vowels+=1
        else:
            consonents+=1
    return "vowels is: ",vowels,"Consonents is:",consonents
str="eiouAEIOU"
result=vowels_consonents_count(str)
print(result)

#finding max min and sum in list
list=[1,2,-3,4,8,9]
min_ele=list[0]
max_ele=list[0]
sum=0
for i in range(0,len(list)):
    if min_ele<list[i]:
        min_ele=list[i]
    if max_ele>list[i]:
        max_ele=list[i]
    sum+=list[i]
print(min_ele)
print(max_ele)
print(sum)  


# Q) List=["Deeksha","ammu","random"]

# o/p={deeksha:{d:1,e:1,e:1,k:1,s:1,s:1,h:,a:1}}{ammu:.............}{random:............}}

# level1

str=(input("Enter a number: "))
res={}
for k in str:
    if k in res:
        res[k]+=1
    else:
        res[k]=1    
print(res)

# level2
list=["deeksha","ammu","random"]
final_res=[]
res={}
for str in list:
    for k in str:
        if k in res:

          res[k]+=1
        else:
           res[k]=1
    final_res.append({str:res})
print(final_res)

#second largest in array

def second_largest(arr):
    if len(arr) < 2:
        return "Array must have at least two elements"
    
    largest = secondLargest = float('-inf')

    for num in arr:
        if num > largest:
            secondLargest = largest
            largest = num
        elif num > secondLargest and num != largest:
            secondLargest = num

    return secondLargest if secondLargest != float('-inf') else "No second largest element"

arr = [10, 20, 4, 45, 99, 99, 38]
print(second_largest(arr))

# second largest in array in reverse array

def second_largest_reverse(arr):
    arr = list(reversed(arr))  # Reverse the array
    largest = secondLargest = float('-inf')

    for num in arr:
        if num > largest:
            secondLargest = largest
            largest = num
        elif num > secondLargest and num != largest:
            secondLargest = num

    return secondLargest if secondLargest != float('-inf') else "Threre is No second largest element"
arr = [10, 20, 3, 43, 75, 75, 38]
print(second_largest(arr))

#finding duplicates in array


def find_duplicates(arr):
    duplicates = []
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] == arr[j] and arr[i] not in duplicates:
                duplicates.append(arr[i])
    return duplicates


arr = [1, 2, 3, 4, 5, 2, 3, 6, 7, 8, 1]
print(find_duplicates(arr))

# find uniques in array

def find_duplicates_and_uniques(arr):
    duplicates = [] #for duplicates
    uniques = []  # for unique values

    for num in arr:
        if arr.count(num) > 1 and num not in duplicates:
            duplicates.append(num)
        elif arr.count(num) == 1:
            uniques.append(num)

    return duplicates, uniques
arr = [1, 2, 3, 4, 5, 2, 3, 6, 7, 8, 1]
duplicates, uniques = find_duplicates_and_uniques(arr)

print("Duplicates:", duplicates)
print("Uniques:", uniques)


# question to find highest number in each array in nested array

def find_max(my_list):
    max=float("-inf")
    for i in my_list:
        max=i if i>max else max
    return max
list1=[]    

res=[]
for j in list1:
    res.append(find_max(j))
print(res)


#binary search
search_ele=int(input("Enter element to search: "))
list1=[1,2,4,5,8,9]
low=0
high=len(list1)-1
while low>=high:
    mid=int((low+high)/2)
    if list1(mid)==search_ele:
        flag=True
        print(mid)
        break
    elif list1(mid)>search_ele:
        high=mid-1
    else:
        low=mid+1

#counting occurances in number

def count_digits(n):
    n = str(n)  
    counts = {str(i): n.count(str(i)) for i in range(10)}
    print(counts)

count_digits(11111234567890123) 

# def has_duplicate_digits(num):
#     num_str = str(num)
#     return len(num_str) != len(set(num_str))

# def check_duplicates(lst):
#     return [has_duplicate_digits(num) for num in lst]

# input_list = [202, 89, 112, 88]
# output_list = check_duplicates(input_list)
# print(output_list)

#  Wap to check if each number in an  list contains duplicate digits, returning true for duplicates and false for unique digits.
#         Input: [202,89,112,88]           Output:[true ,false ,true ,true]


def has_duplicate_digits(num):
    digits = str(num)
    return any(digits.count(d) > 1 for d in digits)

numbers = [202, 89, 112, 88]
result = [has_duplicate_digits(num) for num in numbers]

print(result)


# Wap that takes an array of integers as input and calculates the sum of the digits of each number in the list. 
#         Input: [202,89,112,88]           Output: [4,17,14,6]


def sum_of_digits(num):
    return sum(int(digit) for digit in str(num))

numbers = [202, 89, 112, 88]
result = [sum_of_digits(num) for num in numbers]

print(result)


# 8) Wap to check if the digits of each number in an list are in increasing order, returning true or false for each Increasing order or not
#  Input: [568,89,112,88,571]     Output: [true,true ,false,false ,false]


# max element in nested list



def max_ele_in_list(list):
    max=float("-inf")
    for i in list:
        max=i if i>max else max
    return max

my_list=[[9,-20,18],[14,29,26],[1,35,-18]]
res=[]
for j in my_list:
    res.append(max_ele_in_list(j))
print(res)   

#  19) check if array is subset of another array or not .if the arr2 contains elements which are there in arr1 then it is a subset of an array.
# arr1=[1,3,4,5,2]
# arr2=[2,4,3,1,7.5.15]
# output: arr1 is subset of arr2

def Subset_Check(arr1, arr2):
    for i in arr1:
        found=False
        for j in arr2:
            if i==j:
                found=True
                break
        if not found:
                return False
    return True
arr1=[1,2,3,4,5]
arr2=[1,2,3,4,5,6,7,8]
if Subset_Check(arr1,arr2):
    print("It is subset")
else:
    print("Not subset")    
        
# increasing order check in each digit in array

lst = [258, 369, 456, 546, 312]

for number in lst:
    str_num = str(number)
    increasing = True

    for i in range(len(str_num) - 1):
        if str_num[i] >= str_num[i + 1]:
            increasing = False
            break

    print(f"{number} → {increasing}")

     #increasing order check in each digit in array


lst = [258, 369, 456, 546, 312]

for number in lst:
    str_num = str(number)
    decreasing = True

    for i in range(len(str_num) - 1):
        if str_num[i] <= str_num[i + 1]:
            decreasing = False
            break

    print(f"{number} → {decreasing}")


    