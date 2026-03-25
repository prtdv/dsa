class HashMap: #(key,value)
    def __init__(self, size=100):
        self.size=size
        self.buckets=[[] for i in range(size)]
    
    def hashf(self,key):
        sumof=0
        for i in str(key):
            sumof+=int(i)
        return sumof%self.size
    
    def put(self, key, value):
        index=self.hashf(key)
        bucket=self.buckets[index]
        for i,(k,v) in enumerate(bucket): #loops through each key value pair in the bucket (index, (key,value))
            if k==key:
                bucket[i]=(key,value)
                return
        bucket.append((key,value))

    def get(self, key):
        index=self.hashf(key)
        bucket=self.buckets[index]
        for i,(k,v) in enumerate(bucket):
            if k==key:
                print("found", v)
                return v
        print("not found")
    
    def rem(self,key):
        index=self.hashf(key)
        bucket=self.buckets[index]
        for i,(k,v) in enumerate(bucket):
            if k==key:
                del bucket[i]
                print(f"deleted at bucket {i}")
                return
        print("nothing to remove")

    def printall(self):
        for i,bucket in enumerate(self.buckets):
            print(f"{i}:{bucket}")

hashmap=HashMap(10)
hashmap.put(12335,("Ryan","10/7"))
hashmap.put(12336,("Jake","11/7"))
hashmap.put(12336,("prtdv","11/7"))
hashmap.put(5,("raze","12/3"))
hashmap.printall()
hashmap.get(5)
hashmap.rem(5)
hashmap.get(5)

#this was all bs, use the following in dsa.

hmap={}

hmap[1010]=("Ryan",10305,"Nehe")
hmap[1011]=("Raj",10115,"Neha")

print(hmap.get(1010))
del hmap[1010]
print(hmap)

for key,value in hmap.items():
    print(key,value)

