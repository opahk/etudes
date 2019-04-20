maximum = 15

for i in range(maximum):
  unique_string = str(bytes([65 + s for s in range(i)]), encoding='ascii')
  for j in range(maximum + 2):
    print(unique_string)
    print(j)
