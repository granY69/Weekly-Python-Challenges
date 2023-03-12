"""
ATM machines allow 4 or 6 digit PIN codes and PIN codes cannot contain anything but exactly 4 digits or 
exactly 6 digits. Your task is to create a function that takes a string and returns True if the PIN is 
valid and False if it's not.
"""

def validatePin(pin : str) -> bool:
    if len(pin) == 4 or len(pin) == 6:
        return pin.isdecimal()
    return False

print(validatePin("a234"))
print(validatePin("1234"))
print(validatePin("12345"))
print(validatePin(""))