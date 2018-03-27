class student(object):


    #获取年龄
    def fget(self):
        return self._age

    #设置年龄
    def fset(self,age):
        self._age = int(age)

    #删除年龄属性
    def fdel(self,age):
        self._age = None

    age = property(fget,fset,fdel)

nhi = student()
nhi.age = 26.3

print(nhi.age)
