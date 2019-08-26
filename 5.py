# method1
class solution:
    def function(self,string):
        new=string.replace(' ','%20')
        print(new)

solution().function(input('please input a string'))


#method2
class solution:
    def function(self,string):
        new='%20'.join(string.split(' '))
        print(new)

solution().function(input('please input a string'))

#method3

x=input('please input:')
x=list(x)
m=len(x)
for i in range(m):
    #print(type(x[i]))
    if x[i]==' ':
        x[i]='%20'
x=''.join(x)   #join()可以用来将元组、列表、字典转化为字符，以‘’内的内容来连接各个元素
print(x)