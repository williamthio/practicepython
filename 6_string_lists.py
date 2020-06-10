s = input("String: ")

if s == s[::-1]:
    print("'{}' is a palindrome".format(s))
else:
    print("'{}' is not a palindrome".format(s))
