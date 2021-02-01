import math

def hanning(M):
    values = []
    for n in range(0, M):       # 0 <= n <= M-1
        han = ( 1 - math.cos((2*math.pi*n) / (M-1)) )/2
        values.append(round(han,3))
    # print(values)
    return values

def hamming(M):
    values = []
    for n in range(0, M):       # 0 <= n <= M-1
        cos_term = math.cos((2*math.pi*n) / (M-1))      #cos(2πn/M-1)
        ham = 0.54 - (0.46 * cos_term)
        values.append(round(ham,3))
    # print(values)
    return values

def blackman(M):
    values = []
    for n in range(0, M):       # 0 <= n <= M-1
        cos_term1 = math.cos((2*math.pi*n) / (M-1))     #cos(2πn/M-1)
        cos_term2 = math.cos((4*math.pi*n) / (M-1))     #cos(4πn/M-1)
        black = 0.42 - (0.5 * cos_term1) + (0.08 * cos_term2)
        values.append(round(black,3))
    # print(values)
    return values

def bartlett(M):
    values = []
    m = M-1
    for n in range(0, M):       # 0 <= n <= M-1
        bart = 1 - ((2 * math.fabs(n - m/2))/m)
        values.append(round(bart,3))
    # print(values)
    return values

def list_padding(lis):
    padded_list = []
    col_width = max(len(str(li)) for li in lis) + 1
    for x in lis:
        x = str(x)
        pad = " "
        padding = col_width - len(x)
        pad = pad*padding
        x = x+pad+"|"
        padded_list.append(x)
    return padded_list


hd_n = [0.075, -0.159, 0.225, 0.75, 0.225, -0.159, 0.075]      #Hd(n) values, symmetrical

windows = [hanning, hamming, blackman, bartlett]
win = 2     #choose the window function to be used

h_n = []
order = len(hd_n)
window = windows[win-1](order)
for x in range(0, order):
    val = hd_n[x] * window[x]
    h_n.append(val)

print("M = {}".format(order))
print("{} window values (0 <= n <= M-1): {}".format(windows[win-1].__name__, window))
print("Result after multiplication: {}".format(h_n))
print("\nDETAILED")

points = [pt for pt in range(0, order)]
n = list_padding(["n", " "]+points)
hd_n = list_padding(["hd(n)", " "] + hd_n)
window = list_padding(["w(n)", " "] + window)
h_n = list_padding(["h(n)", " "] + h_n)

for x in range(0, len(n)):
    print("{}{}{}{}".format(n[x], hd_n[x], window[x], h_n[x]))
