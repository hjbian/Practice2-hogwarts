"""
1.注册自己的github，以及在pycharm配置好git。
2.下面这个函数，分别使用关键字参数，以及默认参数的方式传参
3.并说明在函数中有return和没有return的区别。（代码需要格式化）
4.自己写一下冒泡排序
def func(letter):
    print(letter) 
"""
lista=[6,3,9,4,5,2,7]

for i in range(len(lista)-1):
    for j in range(len(lista)-1):
        if lista[j]>lista[j+1]:
            lista[j],lista[j+1] = lista[j+1],lista[j]

print(lista)
