from collections import deque
n = int(input())
x = deque()
count = 0
while(count<n):
    a=[a for a in input().split()]
    if(a[0]=='append'):
        x.append(int(a[1]))
    if(a[0]=='pop'):
        x.pop()
    if(a[0]=='popleft'):
        x.popleft()
    if(a[0]== 'appendleft'):
        x.appendleft(int(a[1]))
    count = count+1
countnew=0
while(countnew<len(x)):
    print(x[countnew],end =' ')
    countnew = countnew+1


#NOTE(COMMENT) :
''' Some Functions of deque ----------
    ----------------------------------
    >>> from collections import deque
>>> d = deque()
>>> d.append(1)
>>> print d
deque([1])
>>> d.appendleft(2)
>>> print d
deque([2, 1])
>>> d.clear()
>>> print d
deque([])
>>> d.extend('1')
>>> print d
deque(['1'])
>>> d.extendleft('234')
>>> print d
deque(['4', '3', '2', '1'])
>>> d.count('1')
1
>>> d.pop()
'1'
>>> print d
deque(['4', '3', '2'])
>>> d.popleft()
'4'
>>> print d
deque(['3', '2'])
>>> d.extend('7896')
>>> print d
deque(['3', '2', '7', '8', '9', '6'])
>>> d.remove('2')
>>> print d
deque(['3', '7', '8', '9', '6'])
>>> d.reverse()
>>> print d
deque(['6', '9', '8', '7', '3'])
>>> d.rotate(3)
>>> print d
deque(['8', '7', '3', '6', '9']) '''
