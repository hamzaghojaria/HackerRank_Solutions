  #Solution:
  
  n = input()
set_n = set(map(int, input().split()))
b = input()
set_b = set(map(int, input().split()))
print(len(set_n.union(set_b)))
