import sys, argparse
from collections import defaultdict

parser = argparse.ArgumentParser(description="extracts data from multiple guppy.py runs")
parser.add_argument("-p", "--param", type=str, default="O' values", help="the parameter to summarize, defaults to O', should be the header label form the output files")
parser.add_argument('files', type=argparse.FileType('r'), nargs="+")

args = parser.parse_args()

small, medium, large = defaultdict(list), defaultdict(list), defaultdict(list)
for f in args.files:
    found = False
    for l in f:
        l = l.rstrip()
        if l == args.param:
            found = True
            continue
        sline = l.split()
        if len(sline) <= 2 and found:
            #done reading data
            break
        if found:
            context = sline[0]
            for i, item in enumerate(sline[1:]):
                if i%3 == 0:#small
                    small[context].append(float(item))
                elif i%3 == 1:#medium
                    medium[context].append(float(item))
                elif i%3 == 2:#large
                    large[context].append(float(item))

def avg(l):
    return sum(l)/float(len(l))
print("context small medium large")
for c in small.keys():
    print("%s %s %s %s" % (c, avg(small[c]), avg(medium[c]), avg(large[c])))

