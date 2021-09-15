import sys

arguments = sys.argv[1:]
i = 0
argi = ''
while i < len(sys.argv)-1:
    argi += arguments[i] + ' '
    i += 1

print('args: ' + argi)
"""

sys.argv[1] - math function
sys.argv[2] - number
sys.argv[3] - another number

"""
sys.argv[2] = int(sys.argv[2])  # our args are stored in memory like strings, but we need type intreger for numbers
sys.argv[3] = int(sys.argv[3])
func = 'a = sys.argv[2]\nb=sys.argv[3]\nif sys.argv[1] == "sum": print("sum =", a+b)' \
          '\nif sys.argv[1] == "mul": print("multiplication =", a*b)' \
          '\nif sys.argv[1] == "div": print("division =", a/b)' \
          '\nif sys.argv[1] == "sub": print("subtraction =", a-b)'
exec(func)

# value = 'a = 90\nb = 7\nprint("Sum =", a + b)'
# exec(value)