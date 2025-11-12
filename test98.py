alice={"john","emma","olivia","liam","jack"}
bob={"john","stan","olivia","liam","noah","ava"}
unique=alice.union(bob)
common=alice.intersection(bob)
symmetricdifference=alice.symmetric_difference(bob)
print("all these freinds are unique")
print(unique)
print("total unique friends ",len(unique))
print("all these friends are common")
print(common)
print("total common friends ",len(common))
print("all these friends are different in both")
print(symmetricdifference)
print("total differencein both friends is",len(symmetricdifference))