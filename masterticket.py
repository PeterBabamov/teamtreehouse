TICKET_PRICE = 10
SERVICE_CHARGE = 3
tickets_remaining = 100


def calculate_price(request_of_tickets):
	return (request_of_tickets * TICKET_PRICE) + SERVICE_CHARGE

while tickets_remaining >= 1:
	print("There are {} tickets remaining. :)".format(tickets_remaining))
	name = input("what is your name broski? ")
	num_tickets = input("How many tickets do you need, {}? ".format(name))
	try:
		num_tickets = int(num_tickets)
		if num_tickets > tickets_remaining:
			raise ValueError("There are only {} tickets remaining"
			.format(tickets_remaining))
	except ValueError as err:
		#errort
		print("fuck, we ran in to a problem, try again.".format(err))
	else:
		amount_due = calculate_price(num_tickets)
		print ("That would be {} bucks!".format(amount_due))
		should_proceed = input("Do you want to continue?\nyes or no? ")
		if should_proceed.lower() == "yes":
			print("SOLD!")
			tickets_remaining -= num_tickets
		else:
			print("Thank you for your time, {}. :)".format(name))
print("sorry, tickets are out!")
