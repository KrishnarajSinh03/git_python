from array import array
arr=array('i',[10,20,30,40])
print(arr)
print(type(arr))

#append
arr=array('i',[10,20,30])
arr.append(40)
print(arr)

#insert
arr=array('i',[10,20,40])
arr.insert(2,30)
print(arr)

#remove
arr=array('i',[10,20,30,40])
arr.remove(20)
print(arr)

#pop
arr=array('i',[10,20,30,40])
x=arr.pop()
print("removed:",x)
print(arr)

#index
arr=array('i',[10,20,30,40])
print(arr.index(30))

#count
arr=array('i',[10,20,30,20,40])
print(arr.count(20))

#reverse
arr=array('i',[10,20,30,40])
arr.reverse()
print(arr)
#basic slicing
arr = array('i',[10,20,30,50,60,50])
print(arr[1:6])
print(arr[3:])
print(arr[:4])
#step slicing
arr = array ('i',[10,20,30,50,60,50])
print(arr[1::2])
print(arr[3::])
print(arr[::4])
#negative slicing
arr=array('i',[10,20,30,50,60,50])
print(arr[-4:-1])
print(arr[-3:])
print(arr[-5:])
#reverse
arr = array('i',[10,20,30,50,60,50])
print(arr[::-1])
#modifying
arr = array('i',[10,20,30,50,60,50])
arr[1:3]=array('i',[77,88])
print(arr)