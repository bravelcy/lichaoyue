# -*- coding:utf-8 -*-
def lookup(data,label,name):
    return data[label].get(name)
def init(data):
    data['first']={}
    data['middle']={}
    data['last']={}
storage={}
init(storage)
def store(data,full_name):
    names=full_name.split()
    if len(names)==2:names.insert(1,'')
    labels='first','middle','last'
    for label,name in zip(labels,names):
	   people=lookup(data,label,name)
	   if people:                      
	      people.append(full_name)
	   else:
	      data[label][name]=[full_name]
MyNames={}
init(MyNames)
store(MyNames,'Magnus Lie Hetland')
print lookup(MyNames,'middle','Lie')
store(MyNames,'Robin Hood')
store(MyNames,'Robin Locksley')
print lookup(MyNames,'first','Robin')
store(MyNames,'Li chao yue')
store(MyNames,'Li chao tian')
print lookup(MyNames,'first','Li')

#people是lookup返回值, 是一个列表或None值,
#if people: # 对应label (first, middle, last)的name 已经存在, 就把全名添加到列表
#否则就根据name加入这个全名
#例如:
#data['first'] = {'Ma': ['Ma Li He']}
如果新来一个叫Ma Li Zhang的就变成了data['first'] = {'Ma': ['Ma Li He', 'Ma Li Zhang']}
要是一个 San Zhang的, 因为San不在data['first']里, 所以要新添加一个San的key进去, 就变成了
data['first'] = {'Ma': ['Ma Li He', 'Ma Li Zhang'], 'San': ['San Zhang']}'
这个可以理解为拉链，将两个list拉到一起来，每个对应元素做一定操作后，合并成一个list.
比如：
zip([1,2,3],['a','b','c'])
结果是
[(1, 'a'), (2, 'b'), (3, 'c')]
