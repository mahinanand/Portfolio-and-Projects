from time_calculator import add_time
from unittest import main


print(add_time("11:06 PM", "2:02"))
print(add_time("8:16 PM", "466:02"))
print(add_time("11:59 PM", "24:05"))

# returns 1:08 AM

# 6:18 AM, Monday (20 days later)

# "12:04 AM (2 days later)"


# Run unit tests automatically
main(module='test_module', exit=False)