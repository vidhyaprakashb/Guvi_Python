# Task 1: Create separate lists for even and odd numbers
from multiprocessing.reduction import duplicate

print("\nTask 1: Create separate lists for even and odd numbers")
nums =[10, 501, 22, 37, 100, 999, 87, 351]

even_number = []
odd_number = []
for enum in nums:
    if enum % 2 == 0:
        even_number.append(enum)
    else:
        odd_number.append(enum)

print("Numbers in the list", nums)
print("Even Number : ",even_number)
print("Odd Number : ",odd_number)

# *******************************************************************************************

# Task 2: Count and create a list of prime numbers
print("\n\nTask 2: Count and create a list of prime numbers\n",)

#using function
print("using function")
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

numbers = [10, 105, 22, 37, 100, 999, 87, 351, 2, 5]
prime_numbers = []
for number in numbers:
    if is_prime(number):
        prime_numbers.append(number)

# Output the result
print("Prime numbers in the list:", prime_numbers)
print("Total count of prime numbers:", len(prime_numbers))

#without using the function
print("\nwithout using the function")
prime_numbers = []
number = [10, 105, 22, 37, 100, 999, 87, 351, 2, 5]
if len(number) < 2:
    print("Not a prime")
elif len(number) > 1:
    for num in number:
        if num % 2 == 0:
            prime_numbers.append(num)
print("Prime numbers from the given list: ",prime_numbers)
print("Count of Prime numbers in the list: ",len(prime_numbers))

# *******************************************************************************************

# Task 3: Find the count of happy numbers
print("\n\nTask 3: Find the count of happy numbers\n")


# Task 4: Sum of the first and last digit of an integer
print("\n\nTask 4: Sum of the first and last digit of an integer\n")

digit = ''
def Sum_of_FirstandLastDigitOf(numer):
    digit = str(numer)
    sum = int(digit[0]) + int(digit[-1])
    return sum

num = 12345
print(f"Sum of the ( {str(num)[0]} ) first and ( {str(num)[-1]} ) last digit of an integer is : ", Sum_of_FirstandLastDigitOf(num))


# Task 5: Distribute mangoes among students
print("\n\nTask 5: Distribute mangoes among students\n")



# Task 6: Find duplicates in three lists
print("\n\nTask 6: Find duplicates in three lists\n")

list1 = [1, 2, 3, 4]
list2 = [2, 3, 5, 6]
list3 = [3, 6, 7, 8]

duplicates = set(list1) & set(list2) & set(list3)
print("Duplicates in three lists:", list(duplicates))


# Task 7: First non-repeating element
print("\n\nTask 7: First non-repeating element\n")


#Finds the first non-repeating element in a given list

def first_non_repeating_element(arr):
    count = {}
    for num in arr:
        count[num] = count.get(num, 0) + 1

    for num in arr:
        if count[num] == 1:
            return num

    return None

# Example usage:
my_list = [1, 2, 3, 2, 1, 4, 5, 4]
result = first_non_repeating_element(my_list)

if result:
    print("The first non-repeating element is:", result)
else:
    print("All elements repeat.")



# Task 8: Find minimum element in a sorted list
print("\n\nTask 8: Find minimum element in a sorted list\n")

print("Using min method")
sorted_list = [10, 20, 30, 40, 50]
print("Minimum Element:", min(sorted_list))

print("\nUsing for loop")
min_val = sorted_list[0]  # Initialize with the first element
for num in sorted_list:
    if num < min_val:
        min_val = num
print("Minimum number in the list: ",min_val)


# Task 9: Find triplet with a given sum
print("\n\nTask 9: Find triplet with a given sum\n")
def find_triplet(nums, target):
    nums.sort()
    for i in range(len(nums) - 2):
        left, right = i + 1, len(nums) - 1
        while left < right:
            current_sum = nums[i] + nums[left] + nums[right]
            if current_sum == target:
                return (nums[i], nums[left], nums[right])
            elif current_sum < target:
                left += 1
            else:
                right -= 1
    return None

nums = [10, 20, 30, 9]
target = 59
print("Triplet:", find_triplet(nums, target))


# Task 10: Check for a sublist with a sum of zero
print("\n\nTask 10: Check for a sublist with a sum of zero\n")

def has_zero_sum_sublist(nums):

    seen_sums = set()
    current_sum = 0
    for num in nums:
        current_sum += num
        if current_sum == 0 or current_sum in seen_sums:
            return True  # Found a sublist with sum 0
        seen_sums.add(current_sum)
    return False


# Example list
nums = [4, 2, -3, 1, 6]

# Check and print if there is any sublist with sum 0
print("Sublist with sum 0 exists:", has_zero_sum_sublist(nums))



print("task done")