import sys
print(sys.argv)
arguments = sys.argv[1:] 
i = 0
argi = ''
while i < len(sys.argv)-1:
    argi += arguments[i]
    i += 1

ind_formula = True
#nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
for ind in argi:
    # if ind in nums:
    #    ind_formula = True
    if ind.isdigit():
        ind_formula = True
    elif ind != '+' or ind != '-':
       ind_formula = False
    else:
        ind_formula = False

if ind_formula:
    print(eval(argi))
else:
    print('not alright')
