import re
import sys

q = sys.argv[1]
s = sys.argv[2]
print(re.split(s, q,flags=re.IGNORECASE))
#print(re.match('Hello','Hello'))

#print("Hello {}. Welcome to {} tutorial".format(sys.argv[1], sys.argv[2]))