

def is_palindrome(s):
    return s == s[::-1]

print(is_palindrome('лепсспел')) # True
print(is_palindrome('helloworld')) # False