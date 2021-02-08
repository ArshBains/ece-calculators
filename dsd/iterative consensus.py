import itertools


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def term_generation(row1, row2):
    new_row = []
    single_match = False
    more_match = False
    for x in range(0, len(row1)):
        i = row1[x]
        j = row2[x]
        if i==j:
            new_row.append(i)
            continue
        if i==2 or j==2:
            e = i if i!=2 else j
            new_row.append(e)
            continue
        new_row.append(2) 
        if single_match==True:
            more_match = True 
        else: single_match = True
    # new_row = map(term_gen_output, row1, row2)
    if single_match==True and more_match==False:
        return new_row 
    else: return None


def term_elimination(full_row1, full_row2):
    stack = []
    row1 = full_row1[1]
    row2 = full_row2[1]
    for x in range(0, len(row1)):
        i = row1[x]
        j = row2[x]
        if i==j:
            continue
        if i==2 and j!=2:
            stack.append("i")
            continue
        if i!=2 and j==2:
            stack.append("j")
            continue
        if i != j:
            return None
    stack = list(set(stack))
    if len(stack) == 1:
        return full_row1 if stack[0]=="j" else full_row2
    return None 


# create initial iterative consensus table in SOP from 
# use '2' instead of '-'
# '0' and '1' for corresponding vairable
# ["term_name":, [representation] ,itereted, deleted]
terms = [
    ["A", [2, 1, 0, 0], False, False],
    ["B", [1, 1, 2, 1], False, False],
    ["C", [2, 1, 1, 0], False, False],
    ["D", [2, 0, 1, 0], False, False],
]
cycle = 1
completed = False

while completed == False:
    last_index = len(terms)
    for index in range(0, len(terms)):
        completed = True
        if terms[index][2] == True:
            continue    #skip row if already iterated
        print(bcolors.WARNING + "Cycle {}:".format(cycle) + bcolors.ENDC)
        for x in range(index+1, last_index):
            # print(index, x)
            expression1 = terms[index][1]
            expression2 = terms[x][1]
            new_row = term_generation(expression1, expression2)
            if new_row != None:
                completed = False
                terms.append(["{}{}".format(terms[index][0], terms[x][0]) ,new_row,False, False])
                # print(terms[index][0], terms[x][0])
            else: continue
        terms[index][2] = True      #set to true because we have iterated this row
        cycle = cycle+1
        for term in terms:
            print("{} -> {}".format(term[0], term[1]))
        rows_to_delete = []
        for comb in itertools.combinations(terms, 2):
            # print(comb[0], comb[1])
            subsume = term_elimination(comb[0], comb[1])
            if subsume != None:
                # print(subsume[0])
                rows_to_delete.append(subsume)
        r_t_d = []
        [r_t_d.append(x) for x in rows_to_delete if x not in r_t_d]
        for row in r_t_d:
            print(bcolors.FAIL + row[0] + bcolors.ENDC)
            terms.remove(row)
        break
