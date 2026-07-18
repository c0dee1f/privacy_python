guest_list = ['Edward Snowden', 'Julian Assange', 'John McAfee']
print(f"{guest_list[0]}, you are cordially invited to dinner.")
print(f"{guest_list[1]}, you are cordially invited to dinner.")
print(f"{guest_list[2]}, you are cordially invited to dinner.")

print(f"\nOh dear, it seems {guest_list[2]} is unable to attend.\n")

guest_list[2] = "Satoshi Nakamoto"
print(f"{guest_list[0]}, you are cordially invited to dinner.")
print(f"{guest_list[1]}, you are cordially invited to dinner.")
print(f"{guest_list[2]}, you are cordially invited to dinner.")

print(f"\nA bigger dinner table for accommodating guests has been found!\n")

guest_list.insert(0, "Linus Torvalds")
guest_list.insert(2, "Alan Turing")
guest_list.append("Karlie Kloss")

print(f"{guest_list[0]}, you are cordially invited to dinner.")
print(f"{guest_list[1]}, you are cordially invited to dinner.")
print(f"{guest_list[2]}, you are cordially invited to dinner.")
print(f"{guest_list[3]}, you are cordially invited to dinner.")
print(f"{guest_list[4]}, you are cordially invited to dinner.")
print(f"{guest_list[5]}, you are cordially invited to dinner.")