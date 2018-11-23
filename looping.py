

name = input("whats your name bro? ")
understand = input("{}, do you understand python while loops?\n(Enter yes/no)".format(name))
while understand.lower() != 'yes':
	print("Ok, {}, while loops in python repeat as long as certain Boolean condition is met.".format(name))
	understand = input("{}, do you understand python while loops?\n(Enter yes/no)".format(name))
print("That's great, {}. I'm please etc.".format(name))

