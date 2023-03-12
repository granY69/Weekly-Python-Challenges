"""
ATM machines allow 4 or 6 digit PIN codes and PIN codes cannot contain anything but exactly 4 digits or 
exactly 6 digits. Your task is to create a function that takes a string and returns True if the PIN is 
valid and False if it's not.
"""

def get_domains(clients : list) -> list:
    domains = [ item.split('@')[1] for item in clients ]
    return domains

clients = ['brucewayne@gotham.com', 'homer_simpson@springfieldnuclear.com', 'hank_hill@arlenpropane.com', 'petergriffin@pawtucketbrewery.com']

print(get_domains(clients))