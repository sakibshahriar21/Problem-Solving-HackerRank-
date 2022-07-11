import os
import sys

#
# Complete the timeConversion function below.
#
def timeConversion(s):
    #
    # Write your code here.
    #
    t = s.split(":")
    if s[-2:] == "PM":
        if t[0] != "12":
            t[0] = str(int(t[0])+12)
    else:
        if t[0] == "12":
            t[0] = "00"
    x = ':'.join(t)
    return str(x[:-2])

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()