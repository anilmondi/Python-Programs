Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> l=[1,2,3]
>>> l.pop(1)
2
>>> l
[1, 3]
>>> l.reverse()
>>> l
[3, 1]
>>> l.insert(1,[1,2,3])
>>> l
[3, [1, 2, 3], 1]
>>> l.pop(1)
[1, 2, 3]
>>> l
[3, 1]
>>> q=l.copy()
>>> q
[3, 1]
>>> l
[3, 1]
>>> 