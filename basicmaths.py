a = 1+1
print(a)
a = 1 + 2 - 3 * 4 / 5
print(a)

a = 2
b = 2.002

c = 'This is string'

d = float(a)
# changing data type
d = int(d)
# Again changing data type from float to int


# some mathematical function on python

# lets us take any value on z
z = -123
# functions :
abs(z)

# its easy to deal with complex too
# complex(d, e)
print(complex(d, e))  # This will give " d + ej "
#  to find the conjugate
# let any number be x
x = 123 + 123j
y = x.conjugate  # This is it

# for real and imaginary
y = x.real
y = x.imag

# Some magic with power function

pow(a, b)  # This is a to the power b

# But when anything comes on 3rd place it helps to slice Like pow(a,b,c) then c used for slicing
# c acts as modulus

# Example :
# when pow(a,b)
# This returns a ** b
# when pow(a,b,c)
# This returns (a**b)%c
