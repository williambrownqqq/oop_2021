from sys import argv

print(argv)
arguments = argv[1:]
i = 0
argi = ' '
while i < len(argv) - 1:
    argi += arguments[i]
    i += 1

ind = 1
ind_formula = True
if len(argv[1:]) < 3:
    print("error, we can't have less 3 arguments")
    ind_formula = False
else:
    while ind <= len(argv[1:]):

        if argv[ind].isdigit():
            # print(argv[ind])
            if ind + 1 <= len(argv[1:]):
                if argv[ind + 1] == '+' or argv[ind + 1] == '-' or argv[ind + 1] == '/' or argv[ind + 1] == '*':
                    # print(argv[ind+1])
                    ind += 1
                    if (argv[ind + 1] == '/' and argv[ind] == '0') or (argv[ind] == '/' and argv[ind + 1] == '0'):
                        print('error, we can\'t use division by zero')
                        ind_formula = False
                        break
                else:
                    print("error, we can't have num num")
                    ind_formula = False
                    break
        else:
            print("error, we can't have sign sign or first sign")
            ind_formula = False
            break
        ind += 1


if ind_formula:
    print('True', eval(argi))
else:
    print('False, not alright')


#print(eval('5 + 2 + (6 / 2)'))