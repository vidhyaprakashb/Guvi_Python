# Task 5

#Program 1:
data1 = [10,501,22,37,100, 999,87,351]
result1 = filter(lambda x: x >4, data1)
print("Program 1 Result: ",list(result1))

#Program 2:
data2 = [10, "hello", 42, "world"]
result2 = list(map(lambda x: "Integer" if isinstance(x, int) else "String", data2))
print("\nProgram 2 Result: ",result2)

#Program 3:
# Lambda function
fibonacci = lambda n: [0, 1] + [0] * (n - 2) if n > 2 else [0, 1][:n]

# Function to update the Fibonacci series in-place
def generate_fibonacci(n):
    fib = fibonacci(n)
    for i in range(2, n):
        fib[i] = fib[i - 1] + fib[i - 2]  # Update the series
    return fib

fibonacci_series = generate_fibonacci(50)
print("\nProgram 3 Result: ",fibonacci_series)



#Program 4:
import re #importing Regular Expression

def validate_email_list(email_list):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$' #to find the email with this format
    return [email for email in email_list if re.match(pattern, email)]

def validate_bangladesh_numbers_list(number_list):
    pattern = r'^(\+880|880|0)1[3-9]\d{8}$' # to find Mobile Numbers of Bangladesh with this format
    return [number for number in number_list if re.match(pattern, number)]

def validate_usa_numbers_list(usa_number_list):
    pattern = r'^\+1[-.\s]?(\d{3}[-.\s]?\d{3}[-.\s]?\d{4})$' # to find Telephone Numbers of USA with this format
    return [number for number in usa_number_list if re.match(pattern, number)]

def validate_password_list(password_list):
    pattern = r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{16}$' #to find 16-Character Alpha-Numeric Password with this format
    return [password for password in password_list if re.match(pattern, password)]

emails = ["test@example.com", "invalid-email", "user@domain.org"]
bangladesh_numbers = ["+8801712345678", "01712345678", "1234567890"]
usa_numbers = ["+1 123-456-7890", "1234567890", "+1 987 654 3210"]
passwords = ["Abcdef12@3456789", "InvalidPassword1", "Password@12345678"]

valid_emails = validate_email_list(emails)
valid_bd_numbers = validate_bangladesh_numbers_list(bangladesh_numbers)
valid_usa_numbers = validate_usa_numbers_list(usa_numbers)
valid_passwords = validate_password_list(passwords)

print("\nProgram 4 Results: ",)
print("Valid Emails:", valid_emails)
print("Valid Bangladesh Numbers:", valid_bd_numbers)
print("Valid USA Numbers:", valid_usa_numbers)
print("Valid Passwords:", valid_passwords)