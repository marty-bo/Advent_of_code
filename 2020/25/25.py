import time

# ####### MAIN #######
f = 'input.txt'
file = open(f)
pk1 = int(file.readline().replace('\n', ''))
pk2 = int(file.readline().replace('\n', ''))

print(pk1, pk2)


# Part 1
start_time = time.time()

val = 1
loop1 = 0
while val != pk1:
    val *= 7
    val %= 20201227
    loop1 += 1
print(loop1)

val = 1
loop2 = 0
while val != pk2:
    val = (val * 7) % 20201227
    loop2 += 1
print(loop2)


encryption_key1 = pk1
for i in range(loop2-1):
    encryption_key1 *= pk1
    encryption_key1 %= 20201227

encryption_key2 = pk2
for i in range(loop1-1):
    encryption_key2 *= pk2
    encryption_key2 %= 20201227

print(encryption_key1, encryption_key2)
print(encryption_key1 == encryption_key2)


print("--- %s seconds ---" % (time.time() - start_time))

