'''
    Write a function that reverses a n-dim nested list. You can use the lecture experiments as a starting point.
    Even if you don't finish, still trying will improve your programming skills
'''

'''
import timeit
import matplotlib.pyplot as plt

a = [[2, 4, 6, 8, 10], [3,6,9,[1,2,[2,3,4,5,6],3],12,15], [4,8,12,16,20]]

print(a)

# This is the one way to do it
def rev(arr):
  if len(arr)==0:
      return
  if len(arr)==1:
      if isinstance(arr[0],list):
          return [rev(arr[0])]
      else:
          return arr
  else:
      return (rev(arr[1:])+rev(arr[:1]))

print("First way", rev(a))


# This is the other way to do it.
def reverselist(L):
    result = []
    for item in L:
        if isinstance(item,list):
            result.append(reverselist(item))
        else:
            result.append(item)
    result.reverse()
    return result

print("Second way", reverselist(a))

plt.plot(rev(a))
plt.show()

'''

arr=[[1,2],[3,4],[5,6,7]]
def rev(arr):
    if len(arr)==0:
        return
    if len(arr)==1:
        if isinstance(arr[0],list):
            return [rev(arr[0])]
        else:
            return arr
    else:
        return (rev(arr[1:])+rev(arr[:1]))
print(rev(arr))



dict1 = {1:'ram', 2:'shyam'}
dict2 = {'khai': 'red', 'hera': 'green'}
m = {'k':'a', 'L':'b'}
def someRandomfun(k,L):
    print(k)
    print(L)

someRandomfun(dict1,dict2)

def someRandomfun1(**m):
    return m

print(someRandomfun1(**m))


def trying(a, b , *args, **kwargs):
    if 'k' in kwargs:
        a = kwargs['k']
    return a
#print(trying())

def trying1(a, b = 1, *args, **kwargs:dict):
    if 'k' in kwargs:
        a = kwargs['k']
    return a
print(trying1([1,2],m))

#rint(trying1(a=2, *[1,2], **m))

def sum(a=2,b):
    return a+b
print(sum(3,5))
