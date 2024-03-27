v = int(input())
t = int(input())

length_mkad = 109

position = (0 + v * t) % length_mkad

print(position)
