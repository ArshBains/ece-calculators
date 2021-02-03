#whatever rows the boat
def jk_ff(Qn,Qn_1):
    Qn = int(Qn)
    Qn_1 = int(Qn_1)
    if Qn==0 and Qn_1==0:
        return "0x"
    elif Qn==0 and Qn_1==1:
        return "1x"
    elif Qn==1 and Qn_1==0:
        return "x1"
    elif Qn==1 and Qn_1==1:
        return "x0"  


def sr_ff(Qn,Qn_1):
    Qn = int(Qn)
    Qn_1 = int(Qn_1)
    if Qn==0 and Qn_1==0:
        return "0x"
    elif Qn==0 and Qn_1==1:
        return "10"
    elif Qn==1 and Qn_1==0:
        return "01"
    elif Qn==1 and Qn_1==1:
        return "x0"  


def d_ff(Qn,Qn_1):
    return str(Qn_1)


def t_ff(Qn,Qn_1):
    if int(Qn) == int(Qn_1):
        return "0" 
    return "1"


input_state_table = []
print("Enter the state table row by row. Enter 'd' when done:\n")
done = False
while not done:
    state_row = input()
    if state_row.lower() == "d":
        done = True
        continue
    input_state_table.append(state_row)
state_table = []

ffs = [jk_ff, sr_ff, d_ff, t_ff]
for index, ff in enumerate(ffs):
    print("{} - {}".format(ff.__name__, index))
flip_flop = ffs[int(input("Choose the flip flop: "))]

#convert input state table format to list
print("\n\n State Table:")
for r in input_state_table:
    r = r.upper().strip().split()
    state_table.append(r)
    print(r)

#all the present states
PS = [s[0] for s in state_table]
max_bin_bits = len(bin(len(PS)-1).replace("0b", ""))

#state assignment based on index
state_assignment = {}
for ps in PS:
    index = PS.index(ps)
    binary_val = bin(index).replace("0b", "") 
    if len(binary_val) < max_bin_bits:
        #add zeros to left
        zero_padding = max_bin_bits - len(binary_val)
        binary_val = "0"*zero_padding + binary_val
    state_assignment[ps] = binary_val

print("\n\n State Assignment:")
for (key, val) in state_assignment.items():
    print(key + "-> " + val)

print("\n\n Excitation table:")
print(["PS", "x", "NS", "Excitation"])
for row in state_table:
    #x=0
    #from first and second column of 'state_table'
    x_0row = [state_assignment[row[0]], 0, state_assignment[row[1]]]        #also replace state with binary value
    x = map(flip_flop, x_0row[0], x_0row[2])
    x_0row = x_0row + list(x)
    print(x_0row)
    #x=1
    #from first and third column of 'state_table'
    x_1row = [state_assignment[row[0]], 1, state_assignment[row[2]]]        #also replace state with binary value
    x = map(flip_flop, x_1row[0], x_1row[2])
    x_1row = x_1row + list(x)
    print(x_1row)
