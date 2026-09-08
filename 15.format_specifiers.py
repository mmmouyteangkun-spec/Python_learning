#format specifiers = {value:flags} format a value based on what flags are inserted

#.(number)f = round to that many decimal places (fixed point)
#:(number) = allocate that many spaces
#:03 = allocate that many spaces
#:< = left justify
#:> = right justify
#:^ = center align
#:+ = use a plus sign to indicate positive value 
#:= = place sign to leftmost position
#: = insert a space before positive numbers
#:, = comma separator

price1 = 3000.14
price2 = -9000.87
price3 = 120000.34

print(f"Price 1 is ${price1:+,.2f}")
print(f"Price 2 is ${price2:+,.2f}")
print(f"Price 3 is ${price3:+,.2f}")