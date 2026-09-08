# logical operator = evaluate multiple conditons (or, and, not)
#                   or = at least one condition must be True
#                   and = both condition must be True
#                   not = inverts the condition (not False, not True)

temp = 20
is_sunny = True

if temp>= 28 and is_sunny:
    print("It is HOT outside")
    print("It is SUNNY")
elif temp <= 0 and is_sunny:
    print("It is COLD outside")
    print("It is SUNNY")
elif 28 > temp > 0 and is_sunny:
    print("It is WARM outside")
    print("It is SUNNY")