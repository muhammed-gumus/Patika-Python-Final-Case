# Proje 1

l = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]
l1 = []
def flatten(n):
    for i in n :
        if isinstance(i,list):
            flatten(i)
        else:
            l1.append(i)

flatten(l)
print(l1)

# Proje 2

lst = [[1, 2], [3, 4], [5, 6, 7]]
l2 = []
def Reverse(lst): 
    for j in lst:
        if isinstance(j,list):
            j.reverse()
            l2.append(j)
        else:
            Reverse(j)
      
Reverse(lst)
l2.reverse()
print(l2)