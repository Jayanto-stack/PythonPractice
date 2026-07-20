guests = ["Albert Einstein", "APJ Abdul Kalam", "Bill Gates"]
for guest in guests:
    print(f"Dear {guest} , you are invited for today inaugaration.")

print(f"\nSorry, {guests[1]} can't attend the inaugaration.")
guests[1] = "Elon Musk"
print("\nUpdated Guest List:")
for guest in guests:
    print(f"Dear {guest}, you are invited to inaugaration")

print("\n Good news! I found a bigger place")
guests.insert(0, "Linus Torvalds")
guests.append("Steve Jobs")
print("\nNew Guest List:")
for guest in guests:
    print(f"Dear {guest}, you are invited to inaugaration.")

print("\nSorry! I can invite only two guests.")
while len(guests) > 3:                          # len() function
    removed_guest = guests.pop()
    print(f"Sorry {removed_guest}, I can't invite you to inaugaration")

print("\nGuest still Invited:")
for guest in guests:
    print(f"{guest}, you are still invited.")

del guests[0]
del guests[0]

print("\nFinal Guest List:")
print(guests)