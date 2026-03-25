class HashSet:
    def __init__(self,size=100):
        self.size=size
        self.buckets=[[] for _ in range(size)]
    
    def hashf(self,val):
        sumof=0
        for i in val:
            sumof+=ord(i)
        return sumof%self.size
    
    def add(self, val):
        index=self.hashf(val)
        bucket=self.buckets[index]
        if val not in bucket:
            bucket.append(val)

    def find(self, val):
        index=self.hashf(val)
        if val in self.buckets[index]:
            print(f"it's here at index {index}.")
        else:
            print("not found.")

    def remove(self, val):
        index=self.hashf(val)
        if val in self.buckets[index]:
            self.buckets[index].remove(val)
            print("removed.")
        else:
            print("nothing to remove.")

    def printset(self):
        for index,bucket in enumerate(self.buckets):
            print(f"{index}:{bucket}")

hash_set=HashSet(size=11)
print(hash_set.buckets)
set=["John","prtdv","Arpit","Saad","Harshil","prtdk","B"]
for i in set:
    hash_set.add(i)

hash_set.printset()

hash_set.remove("prtdk")
hash_set.printset()

