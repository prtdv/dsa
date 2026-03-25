arr=['Pete', 'Jones', 'Lisa', 'Bob', 'Siri']

hash=[[None] for i in range(10)]

def hashf(inp):
    sumofchar=0
    for i in inp:
        sumofchar=sumofchar+ord(i)

    return sumofchar%10

print(hashf("Bob"))

def put(val):
    index=hashf(val)
    bucket=hash[index]
    if val not in bucket:
        bucket.append(val)
        if None in bucket:
            bucket.remove(None)


for i in arr:
    put(i)
print(hash)

put("Stuart")
print(hash)

def contain(name):
    key=hashf(name)
    return name in hash[key]

print(contain("Stuart"))