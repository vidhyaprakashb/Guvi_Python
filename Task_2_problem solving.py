# Task : 1
# def count_Vovels(input):
#     vovels = "auiouAEIOU"
#     # create a dictionary where each vowel is a key, and its initial value is set to 0:
#     counts = {vovel : 0 for vovel in vovels}
#     # Print all the vovels with keys and values
#     print(counts)
#     total = 0
#
#     for char in input: #iterate to all the char
#         if char in counts: #compare each char with dictionary variable counts
#             [char] += 1 #if the char is match, It will update the same in the compared key value
#             total += 1 #this will simply increase the count when if condition is executed
#
#     print(total) #print total number of vovels that find in the given input
#     print(counts) #print the count of each vovels that find in the given input
#
# input = "Guvi Out Geeks Network Private Limited"
# count_Vovels(input) #finction is called in this line
# from Day_6 import string


#Task 2:

# def pyramid_of_numbers(prymid):
#     for number in range(1, prymid+1):  # Loop through numbers from 1 to 20
#         # row = ""  # Start with an empty row
#         row = '' # initialize the variable to store the number
#         for i in range(number):  # Add the current number 'number' times
#             row += str(number) + " "  # Append the number and a space to the row
#         print(row.strip())  # Print the row, and remove any extra space at the end if any
#
# # Call the function
# pyramid_of_numbers(20)


#Task 3:

# def remove_vowels(string):
#     vowels = 'aeiouAEIOU'
#     result = ''
#     for letter in string:
#         if letter not in vowels:
#             result += letter
#     return result
#
# string = "Guvi Out Geeks Network Private Limited"
# result = remove_vowels(string)
# print("Original String: ", string)
# print("String after Remove All Vowels: ",result)


#Task 4:

# def unique_char(str):
#     get_unique_char_withSpace = set(str) #this set will remove the duplicate char in the given string value
#     get_unique_char = set(str.replace(" ", ""))     # this set will remove the duplicate char in the given string value
#                                                     # and the space also removed, only the unique char get counted
#     return get_unique_char, get_unique_char_withSpace
#
# str = 'Guvi Out Geeks Network Private Limited'
# get_unique_char, get_unique_char_withSpace = unique_char(str)
# get_unique_char_count = len(get_unique_char)
# get_unique_char_withSpace_count = len(get_unique_char_withSpace)
# print("Original String: ", str)
#
# print("Unique characters (without spaces): ", get_unique_char)
# print("Count of unique characters (without spaces): ", get_unique_char_count)
#
# print("Unique characters (with spaces): ", get_unique_char_withSpace)
# print("Count of unique characters (with spaces): ", get_unique_char_withSpace_count)


#Task 5:

def palindrome(string):
    processed_string = string.replace(" ","").lower() # Remove spaces and convert the string to lowercase for comparison
    return processed_string == processed_string[::-1] # Check if the given string is equal to its reverse
                                                      # When we use [::-1], it means:
                                                      # start and stop are lef empty, so the entire sequence is considered.
                                                      # step = -1 means the slicing moves backward, effectively reversing the sequence.

string = "A man a plan a canal Panama"
print(palindrome(string))
String2 = "world"
print(palindrome(String2))
