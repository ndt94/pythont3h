import os

# os.system('caja')

from subprocess import getoutput
result = getoutput('ping -c 4 google.com')
print(result)
lines = result.split('\n')
lines = [line for line in lines if 'ttl=' in line.lower()]
print(lines)