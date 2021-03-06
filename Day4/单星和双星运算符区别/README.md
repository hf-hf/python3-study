### \*和**区别
#### 1. 算数运算
\*  代表乘法  
** 代表乘方
```
>>> 2 * 5
10
>>> 2 ** 5
32
```

#### 2. 函数形参
*args 和 **kwargs 主要用于函数定义。

你可以将不定数量的参数传递给一个函数。
不定的意思是：预先并不知道, 函数使用者会传递多少个参数给你, 所以在这个场景下使用这两个关键字。
其实并不是必须写成 *args 和 **kwargs。  
*(星号) 才是必须的. 你也可以写成 *ar  和 **k 。而写成 *args 和**kwargs 只是一个通俗的命名约定。

python函数传递参数的方式有两种：

位置参数（positional argument）
关键词参数（keyword argument）
*args 与 **kwargs 的区别，两者都是 python 中的可变参数：

*args 表示任何多个无名参数，它本质是一个 tuple
**kwargs 表示关键字参数，它本质上是一个 dict

如果同时使用 *args 和 **kwargs 时，必须 *args 参数列要在 **kwargs 之前。

```
>>> def fun(*args, **kwargs):
...     print('args=', args)
...     print('kwargs=', kwargs)
... 
>>> fun(1, 2, 3, 4, A='a', B='b', C='c', D='d')
args= (1, 2, 3, 4)
kwargs= {'A': 'a', 'B': 'b', 'C': 'c', 'D': 'd'}
```

使用 *args
```
>>> def fun(name, *args):
...     print('你好:', name)
...     for i in args:
...         print("你的宠物有:", i)
... 
>>> fun("Geek", "dog", "cat")
你好: Geek
你的宠物有: dog
你的宠物有: cat
```

使用 **kwargs
```
>>> def fun(**kwargs):
...     for key, value in kwargs.items():
...         print("{0} 喜欢 {1}".format(key, value))
... 
>>> fun(Geek="cat", cat="box")
Geek 喜欢 cat
cat 喜欢 box
```

#### 3. 函数实参
如果函数的形参是定长参数，也可以使用 *args 和 **kwargs 调用函数，类似对元组和字典进行解引用：

```
>>> def fun(data1, data2, data3):
...     print("data1: ", data1)
...     print("data2: ", data2)
...     print("data3: ", data3)
... 
>>> args = ("one", 2, 3)
>>> fun(*args)
data1:  one
data2:  2
data3:  3
>>> kwargs = {"data3": "one", "data2": 2, "data1": 3}
>>> fun(**kwargs)
data1:  3
data2:  2
data3:  one
```

#### 4. 序列解包
```
>>> a, b, *c = 0, 1, 2, 3  
>>> a  
0  
>>> b  
1  
>>> c  
[2, 3]
```