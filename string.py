# a="prasanna"
# print(type(a))
# b='hello'
# print(type(b))
# c="'python'"
# print(type(c))
# s="hello"
# #Access
# b=s[0]
# print(b)
# #Slicing
# c=s[0:3]
# print(c)
# #Concatenation
# d=s+"$"
# print(d)
# #Repetition
# z=s*2
# print(z)
# #upper()
# a=s.upper()
# print(a)
# #lower()
# f=s.lower()
# print(f)
# #replace()
# k=s.replace("h","t")
# print(k)
# #strip(),lstrip(),rstrip()
# g="         hello      "
# w=g.lstrip()
# print(w)
# f=g.rstrip()
# print(f)
# r=g.strip()
# print(r)
# #split()
# d="a,b,c"
# print(d.split(','))
# #find
# a="apple"
# print(a.find('p'))
# #isalpha
# c="potato"
# print(c.isalpha())
# #capitalize()
# s="owl"
# print(s.capitalize())
# #Title
# x="the apple"
# print(x.title())
# #swapcase
# q="hello WORLD"
# print(q.swapcase())
# #Removeprefix and Removesuffix
# a="banana"
# print(a.removeprefix('b'))
# print(a.removesuffix('a'))
# a="hello"
# print(a.isalpha())
# b="123"
# print(b.isnumeric())
# c="abc123"
# print(c.isalnum())
# d="123"
# print(d.isdigit())
# e="2"
# print(e.isdecimal())
# f="HELLO"
# print(f.isupper())
# g="wow"
# print(g.islower())
# h="The Apple"
# print(h.istitle())
# i="  " 
# print(i.isspace())
# a="python is great"
# print(a.splitlines())
# #String Slicing
# s="kiet students"
# print(s[0:5])
# print(s[1::])
# print(s[:5:])
# print(s[::2])
# print(s[1:9:2])
# #Negative Indexing in Slicing
# s="python"
# print(s[-1::])
# print(s[:-3:])
# print(s[::-1])
# print(s[-1:-5:-1])
# #String Functions
# s="PrasannaKuchipudi"
# print(len(s))
# print(max(s))
# print(min(s))
# print(type(s))
# print(list(enumerate(s)))
# print(sorted(s))
# #Task-1
# a="python"
# b="     hello"
# print(a.upper())
# print(a.lower())
# print(a.capitalize())
# print(a.title())
# print(a.count('p'))
# print(a.replace('p','h'))
# print(a.startswith('p'))
# print(a.endswith("n"))
# print(a.find('p'))
# print(b.strip())
# print(b)
# print("-".join(a))
#Task-2
n="PYTHON"
if n.isupper():
    print("UPPER")
else:
    print("LOWER")
#Palindrome
a="amma"
if a==a[::-1]:
    print("True")
else:
    print("False")

