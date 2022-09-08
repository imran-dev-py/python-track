s = {3, 4, 5, 6, 7, 5}
l = list(s)
print(l)  # [3,4,5,6,7,5]
count_ = l.count(5)
print(count_)  # 1

d = {
    'Mon': 20,
    'Tue': 25,
    'Thu': 30
}

l = list(d.values())
print(l)  # [20,25,30]

d['''Wed''] = 40
print(d)  # Syntax error

sum = l[0] + l[1] + l[2] + l[3]
print(sum)  #index error

a = [0,1,2,3,4,5,6,7,8,9,10]
b = [0,5,10,15,20,25]
a = set(a) # {0,1,2,3,4,5,6,7,8,9,10}
b = set(b) # {0,5,10,15,20,25}
new_list = list(a & b) # [0,5,10]
print(new_list)

d = {
    0: 10,
    1: 20,
    2: 20,
    3: 30
}

x = d[0] + d[3]
print(x) # 40
