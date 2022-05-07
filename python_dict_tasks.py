print("********1) Nested list*********")
x=[1,2,3,4,[5,6,7,8,9]]
for i in (x[4][::]):
    print(i)

print("********2) dict and count dict*********")
list2 = [{'l':1, 'm':2, 'n':{1:2, 2:{'o':5, 'p':7, "q":'SURYA'}}}]
print(list2[0]['n'][2]["q"])
x = list2[0]['n'][2]["q"]
print({i:x.count(i) for i in x})

print("********3) inverse matrix*********")
x=[[1,2,3],[4,5,6],[7,8,9]]
print((x[0][0]),(x[1][0]),(x[2][0]))
print((x[0][1]),(x[1][1]),(x[2][1]))
print((x[0][2]),(x[1][2]),(x[2][2]))

print("********4) sum of two lists*********")
x = [1,2,3]
y = [5,6,7]
total = []
for j in range(3):
    total.append(x[j] + y[j])
print(total)


print("********5) dict*********")
dict=[{}]
n=int(input("enter no of values:"))
for i in range(n):
    x=input("enter name:")
    y = input("enter id:")
    dict.append({x:y})
print(dict)

print("********6) dict values*********")

x={1:'surya','name':{'location':{'banglore':{'math','white'},'che':{1:{'hy','ra'}}}}}
y=[]
y.append(x[1])
y.append(x['name']['location']['banglore'])
y.append(x['name']['location']['che'][1])
print(y)

print("********7) dict duplicate keys*********")

x={10:12,10:2,20:1,30:23,20:11}
y={}
for i in x:
    if i in y:
        x[i]+=1
        x.key=lambda  x:x[1]
        print(y)
    else:
        x[i]=1
print(x)