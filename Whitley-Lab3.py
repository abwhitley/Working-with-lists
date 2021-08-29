# Austin Whitley 08/27/2021
# Lab 3

# EXERCISE 5-4: Alien Colors #2

print("EXERCISE 5-4: Alien Colors #2\n")
# Runs If
alien_color = "green"

if alien_color == "green":
    print("You earned 5 points for shooting the alien")
else:
    print("You earned 10 points for shooting the alien")

# Runs Else
alien_color = "yellow"

if alien_color == "green":
    print("You earned 5 points for shooting the alien")
else:
    print("You earned 10 points for shooting the alien")


# EXERCISE 5-5: Alien Colors #3
print("\nEXERCISE 5-5: Alien Colors #3\n")
# Runs green alien
alien_color = "green"

if alien_color == "green":
    print("You earned 5 points")
elif alien_color == "yellow":
    print("You earned 10 points")
elif alien_color == "Red":
    print("You earned 15 points")
else:
    print("We dont have any other color for aliens")


# Runs yellow alien
alien_color = "yellow"

if alien_color == "green":
    print("You earned 5 points")
elif alien_color == "yellow":
    print("You earned 10 points")
elif alien_color == "Red":
    print("You earned 15 points")
else:
    print("We dont have any other color for aliens")


# Runs red alien
alien_color = "red"

if alien_color == "green":
    print("You earned 5 points")
elif alien_color == "yellow":
    print("You earned 10 points")
elif alien_color == "red":
    print("You earned 15 points")
else:
    print("We dont have any other color for aliens")

# EXERCISE 5-6: Stages of Life
print("\nEXERCISE 5-6: Stages of Life\n")
age = 27

if age >= 0 and age < 2:
    print("Person is a baby")
elif age >= 2 and age < 4:
    print("Person is a toddler")
elif age >= 4 and age < 13:
    print("Person is a kid")
elif age >= 13 and age < 20:
    print("Person is a teenager")
elif age >= 20 and age < 65:
    print("Person is an adult")
elif age >= 65:
    print("Person is an elder")
else:
    print("This person has not been born yet")

# EXERCISE 5-8: Hello Admin
print("\nEXERCISE 5-8: Hello Admin\n")
usernames = ["Austin", "Allen", "Maria", "Admin", "Kenzi", "Nathan", "Devon", "admin"]

for user in usernames:
    if user.lower() == "admin":
        print("Hello admin, would you like to see a status report?")
    else:
        print(f"Hello {user}, thank you for logging in again")

# EXERCISE 5-9: No Users
print("\nEXERCISE 5-9: No Users\n")
print(usernames)
usernames = []
print(usernames)
if len(usernames) == 0:
    print("We need to find some users")
else:
    print("We have users")

# EXERCISE 5-10: Checking Usernames
print("\nEXERCISE 5-10: Checking Usernames\n")

current_users = ["Austin", "Allen", "Maria", "Admin", "Kenzi", "Nathan", "Devon", "admin"]
new_users = ["Alec", "Austin", "Chayenne", "AJ", "kenzi"]

copy_current_users = current_users[:]
copy_new_users = new_users[:]

for i in range(len(copy_current_users)):
    copy_current_users[i] = copy_current_users[i].lower()
for i in range(len(copy_new_users)):
    copy_new_users[i] = copy_new_users[i].lower()

for new_user in copy_new_users:
    if new_user in copy_current_users:
        print(f"{new_user}, your username is not available")
    else:
        print(f"{new_user}, your username is available")

# EXERCISE 5-11: Ordinal Numbers
print("\nEXERCISE 5-11: Ordinal Numbers\n")

numbers = list(range(1,10))

for number in numbers:
    if number == 1:
        print("1st")
    elif number == 2:
        print("2nd")
    elif number == 3:
        print("3rd")
    elif number > 3:
        print(f"{number}th")
    else:
        print("For this exercise we should not reach this")