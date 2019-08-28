import re
# findall
# 返回所有满足匹配条件的结果，放在列表里,前面一个参数是正则，后面是待匹配字符串
# search
# 从前往后，找到一个就返回，返回的是结果的对象
# 需要.group才能获取结果，找不到就是返回None，调用group自然报错
# match
# 和search用法相同，也需要group找不到报错，返回None.
# 从头开始匹配，且必须从头开始，如果正则从头开始就匹配上，那就返回一个变量

#findall示例
ret=re.findall('[a-z]+','abnormol big %s please')
print(ret)
#返回 ['abnormol', 'big', 's', 'please']
#
#search 示例
ret2=re.search('[z]','abnormol big %s please')
print(ret2)    #None
if ret2:
    print(ret2.gruop)
ret3=re.search('[ab]','abnormol big %s please')
if ret3:
    print(ret3.group())

ret4=re.split('[ab]','abcd')
print(ret4)#先按a分割得到''和'bcd',再按b分割得到''和‘cd'
#['', '', 'cd']

ret5=re.sub('\d','H','sre3454rfdxzrt4rfdcs2',1)
#将第一个数字替换成'H’，如果没有参数1就全部替换
print(ret5)
#sreH454rfdxzrt4rfdcs2
ret6=re.subn('\d','H','sre3454rfdxzrt4rfdcs2')
#将数字替换成'H’，并且返回替换了几次
print(ret6)
#('sreHHHHrfdxzrtHrfdcsH', 6)


obj=re.compile('\d[a-z]')
#将正则表达式编译成为一个正则表达式对象，规则要匹配的是数字加小写字母
# 可以多次使用该正则
ret7=obj.search('saedtg1a2b')
ret8=obj.search('s366edm9tg1a2b')
print(ret7.group())   #1a
print(ret8.group())   #6e

ret9=re.finditer('\d','asdf32edf34fss3d')
print(ret9)
print(next(ret9).group())
print(next(ret9).group())
print([i.group()for i in ret9])   #迭代器中每一个元素都要使用.group才能拿到结果
print([i.group()for i in ret9])
# <callable_iterator object at 0x000002650C282240> 返回一个迭代器
# 3
# 2
# ['3', '4', '3']
# []





#1.search和match 都有的关于group和分组的
ret10=re.search('^[1-9](\d{14})(\d{2}[0-9x])?$','520202199910100236')
print(ret10.group())
print(ret10.group(1))
print(ret10.group(2))
# 520202199910100236
# 20202199910100  第一个括号括起来的分组，第二个括起来的分组
# 236


#2.findall的分组优先
#优先匹配分组里面的，如果正则中有()，就只匹配()里面的，不是''里的
#?:取消分组优先
ret11=re.findall('abc.(\d|[a-z]).cn','abc.5.cn')
print(ret11)
#5
ret12=re.findall('abc.(?:\d|[a-z]).cn','abc.5.cn')
print(ret12)
#['abc.5.cn']

#3.split的分组优先,如果正则有分组，就是保留切割字符
ret13=re.split('\d+',"sad23es233s21sed")
print(ret13)

ret14=re.split('(\d+)',"sad23es233s21sed")
print(ret14)
# ['sad', 'es', 's', 'sed']
# ['sad', '23', 'es', '233', 's', '21', 'sed']



# 示例：爬虫
# 1.url从网页上把代码down下来，url模块
# 2.bytes->utf-8，网页内容就是待匹配的字符串
# 3.ret=re.findall('正则',s,re.S)
# ret是所有匹配到的内容组成的列表，re.S是flag，就可以匹配换行符了，re模块

# 示例二：一个很复杂的计算式字符串，不允许用eval将a变成计算式
# 去掉所有的空格
# 加减乘除，括号
# 先算括号里的乘除，再算括号里的加减
# 从括号里乘除，从没有括号的部分中取乘除
# 元字符，量词

