import traceback

try:
    x = int('ab')
    d = {}
    x = d[1]
except ValueError as e:
    print('Error')
    print(e)
    traceback.print_exc()
finally:
    print('Done')
y = int('10')
print(y)