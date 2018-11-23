import sys

MASTER_PASSWORD = 'petbab'
password = input("please enter the super secret password:  ")
attempt_count = 1
while password != MASTER_PASSWORD:
	if attempt_count > 2:
		sys.exit("Too many invailed password attempts")
	password = input("Invalid password, try again:  ")
	attempt_count += 1
print("Welcome to secret town")