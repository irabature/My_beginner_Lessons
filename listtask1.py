guests =  ["adam", "betty", "cole", "danile", "emma", "freddy"]
#print(guests)

# d cannot make it to the dinner

#guests.insert(3, "zoe")

#print(guests)

#guests[3] = "zoe"

#print(guests)

#name = guests[3].title()

#print(name)

#print(guests)

guests.insert(0, "Ubong")

#print(guests)

guests.insert(3, "Ira")

#print (guests)

guests.append("Erico Belleti")

print(guests)

#message = f"Thank you for honoring my learning invitation, {guests[1].title()}"

#print(message)

# message = f"{guests[0].title()}, Thank you for honoring my learning invitation."
# message2 = f"{guests[1].title()}, Thank you for honoring my learning invitation."
# message3 = f"{guests[2].title()}, Thank you for honoring my learning invitation."
# message4 = f"{guests[3].title()}, Thank you for honoring my learning invitation."
# message5 = f"{guests[4].title()}, Thank you for honoring my learning invitation."
# message6 = f"{guests[5].title()}, Thank you for honoring my learning invitation."
# message7 = f"{guests[6].title()}, Thank you for honoring my learning invitation."
# message8 = f"{guests[7].title()}, Thank you for honoring my learning invitation."

# print(message)
# print(message2)
# print(message3)
# print(message4)
# print(message5)
# print(message6)
# print(message7)
# print(message8)

for guest in guests:
    print(f"{guest.title()}, Thank you for honoring my learning invitation.")


