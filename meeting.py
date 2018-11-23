attendees = ["Ken", "Alena", "Pepi"]
attendees.append("ashley")
attendees.extend(["James", "Gull"])
optional_attendees = ["Ben 3", "Dave"]
potential_attendees = attendees + optional_attendees
print("There are", len(potential_attendees), "potential attendes curently")
