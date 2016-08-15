#authour : sad-
import sys
from itertools import izip
argmax = lambda array: max(izip(array, xrange(len(array))))[1]

def convert_to_decimal(inp, base):
    if base == '10':
        return int(inp)
    length = len(inp)-1
    place_val = [int(val)*int(base)**(length - i) for i, val in enumerate(inp)]
    return sum(place_val)

def convert_from_decimal(inp, base):
    ans = ''
    if inp == 0:
        return 0
    while inp > 0:
        rem = inp%base
        inp = inp/base
        ans = str(rem) + ans
    return ans

def valid(inp, base):
    if int(max(inp)) >= int(base):
        return False
    return True

def fourier(inp, base):
    decimal = convert_to_decimal(inp, base)
    numbers = [convert_from_decimal(decimal, x) for x in xrange(5, 10)] + [str(decimal)]
    counts = [number.count('4') for number in numbers]
    return (argmax(counts), numbers[argmax(counts)])

def main(argv):
    if len(argv) > 2 or len(argv) < 1:
        print "ERROR! usage: python fourier_transform.py number [base]"
    else:
        if len(argv) == 1:
            argv += ['10']
        if not valid(argv[0], argv[1]):
            print "Invalid number: %s for base %s"%(argv[0], argv[1])
        else:
            result = fourier(argv[0], argv[1])
            print "The fourier tranform of %s is %s in base %d"%(argv[0], result[1], result[0]+5)

if __name__ == '__main__':
    main(sys.argv[1:])