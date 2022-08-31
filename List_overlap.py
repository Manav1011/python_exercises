from sqlalchemy import union


a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
A=set(a)
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
B=set(b)
z=A.intersection(B)
for i in z:
    print(i)