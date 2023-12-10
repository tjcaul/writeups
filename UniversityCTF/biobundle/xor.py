import sys

lines = sys.stdin.readlines()

for line in lines:
    nums = line.split(' ')
    for num in nums:
        x = int(num, 16)
        x ^= 0x37
        print(f'{x:02x}', end='')
print()
