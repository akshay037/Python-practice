lucky_number = [4, 8, 15, 16, 23, 42]
friends = ["Kevin","Karan","Jim","Oscar","Toby"]
friends.extend(lucky_number)
friends.append("Creed")
friends.insert(1, "Kelly")
friends.remove("Jim")
friends.pop()
lucky_number.reverse()
lucky_number.sort()
print(friends)
print(lucky_number)
