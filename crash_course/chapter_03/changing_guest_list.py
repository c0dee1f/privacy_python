guest_list = ['Edward Snowden', 'Julian Assange', 'John McAfee']
print(f"{guest_list[0]}, you are cordially invited to dinner.")
print(f"{guest_list[1]}, you are cordially invited to dinner.")
print(f"{guest_list[2]}, you are cordially invited to dinner.")

print(f"\nOh dear, it seems {guest_list[2]} is unable to attend.\n")

guest_list[2] = "Satoshi Nakamoto"
print(f"{guest_list[0]}, you are cordially invited to dinner.")
print(f"{guest_list[1]}, you are cordially invited to dinner.")
print(f"{guest_list[2]}, you are cordially invited to dinner.")