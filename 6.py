# python特点:
# 可读性强
# 语法简介
# 入门级语言
# 解释性与交互性
# 优秀的模块化思维
# 开源软件和丰富的第三方库
# 标准脚本语言
# python应用场景
#  web应用开发
# 自动化脚本
# 科学计算
# 桌面软件
# 网络编程
# 游戏
# ....
# 海龟绘图
# import turtle # 导入turtle模块
# turtle.showturtle() # 显示箭头
# turtle.write("hello world") # 写入hello world
# turtle.forward(100) # 向前走100步
# turtle.color("red") # 设置颜色为红色
# turtle.left(90) # 向左转90度
# turtle.forward(100) # 向前走100步
# turtle.goto(0,50) # 移动到坐标(0,50)
# turtle.goto(0,0)
# turtle.penup() # 抬起画笔
# turtle.goto(0,50) # 移动到坐标(0,0)
# turtle.pendown() # 放下画笔
# turtle.circle(50) # 画一个半径为50的圆
# import turtle
# turtle.width(10)
# turtle.color("red")
# turtle.circle(50)
# turtle.color("blue")
# turtle.penup()
# turtle.goto(150,0)
# turtle.pendown()
# turtle.circle(50)
# turtle.color("green")
# turtle.penup()
# turtle.goto(300,0)
# turtle.pendown()
# turtle.circle(50)
# turtle.color("yellow")
# turtle.penup()
# turtle.goto(450,0)
# turtle.pendown()
# turtle.circle(50)
# turtle.color("purple")
# turtle.penup()
# turtle.goto(600,0)
# turtle.pendown()
# turtle.circle(50)
# 不能以数字开头
# 不能含有#这样的特殊字符
# 不能使用保留字
"""
对象与引用
1 标识(identity)用于唯一标识一个对象，通常对应于对象在计算机内存中的地址，使用内置函数id(obj)可返回对象obj的标识
2 类型(type)用于描述对象的类型，使用内置函数type(obj)可返回对象obj的类型
3 值(value)用于描述对象的值，使用内置函数print(obj)可返回对象obj的值
变量是对象的引用，因为变量存储的是对象的地址，而不是对象的值
变量位于栈中，对象位于堆中
python得益于存储大类型浮点数从底层上来讲是因为:
与IEE754标准关系
"""
# print(2 ** 3000)
"""
Python 可以处理非常大的整数，因为它对整数使用了任意精度的算术运算。然而，这与用于浮点数的 IEEE 754 标准无关。`2 ** 3000` 的计算之所以可行，是因为 Python 的 `int` 类型可以根据内存的限制增长到任意大小，而不像其他语言中的固定精度类型。
- **任意精度整数**：Python 的 `int` 类型可以表示任意大小的数字，仅受可用内存的限制。
- **IEEE 754**：该标准适用于浮点数，而不是整数。Python 的 `float` 类型遵循此标准。
`2 ** 3000` 的结果将是一个非常大的整数，而不是浮点数。如果尝试将其转换为浮点数，可能会导致精度丢失或溢出。
"""
# #字符串拼接
# a = 'Hello'
# b = 'World'
# c = a + b  #使用加号进行字符串拼接
# print(c)
# c = 'Hello''World'  #将多个字面字符串直接放到一起实现拼接,'' ''实现拼接
# print(c)
# c = 'Hello' 'World'  #将多个字面字符串直接放到一起实现拼接
# print(c)
"""
字符串的截取
字符串的截取是实际应用中经常使用的技术
string[start:end:step]
start: 截取的起始位置，包含该位置的字符
end: 截取的结束位置，不包含该位置的字符
[:]提取整个字符
[start:]提取从start到最后的字符
[:end]提取从开始到end的字符
[start:end]提取从start到end-1的字符
[start:end:step]提取从start到end-1的字符，步长为step
"""
# a = 'Hello, World!'
# print(a[:])  # 提取整个字符串,Hello, World!
# print(a[2:])  # 提取从索引2到最后的字符,llo, World!
# print(a[:5])  # 提取从开始到索引5的字符,Hello
# print(a[7:12])  # 提取从索引7到索引11的字符,World
# print(a[1:5:2])  # 提取从索引1到索引4的字符，步长为2,el
"""
split() and join()
split()方法用于将字符串分割成列表，默认以空格、制表符、换行符为分隔符
join()方法用于将列表中的元素连接成字符串，默认以空格为分隔符
"""
# a = 'Hello,  World!'
# b = a.split(' ', 2)  # 将字符串分割成列表,maxsplit=2,其意义是分割成2个元素
# print(b)  # ['Hello', ' World!']
"""
可变字符串
Python中字符串是不可变的，不支持原地修改,如需要修改字符串，可以使用可变字符串，但是经常需要原地修改字符串，可以使用io.StringIO模块
或array模块"""

# import io
# import array
# # # 创建一个可变字符串
# mutable_string = io.StringIO()
# # # 向可变字符串中写入数据
# mutable_string.write("Hello, ")
# mutable_string.write("World!")
# # # 获取可变字符串的内容
# content = mutable_string.getvalue()
# print(content)  # Hello, World!
# mutable_string.seek(7)
# mutable_string.write("Python!")
# # # 获取修改后的内容
# content = mutable_string.getvalue()
# print(content)  # Hello, Python!
# # # 关闭可变字符串
# mutable_string.close()
# # # 创建一个可变字符串
# mutable_string = array.array('u', 'Hello, ')
# # # 向可变字符串中写入数据
# mutable_string.extend(array.array('u', 'World!'))
# # # 获取可变字符串的内容
# content = mutable_string.tounicode()
# print(content)  # Hello, World!
# mutable_string[7:12] = array.array('u', 'Python!')
# # # 获取修改后的内容
# content = mutable_string.tounicode()
# print(content)  # Hello, Python!
# 进制转换
# print(int('0b111', 2))  # 二进制转换为十进制
# print(int('0o7', 8))  # 八进制转换为十进制
# print(int('0x7', 16))  # 十六进制转换为十进制
# range([start],end,[step])
# print(list(range(1, 10, 2)))  # [1, 3, 5, 7, 9]
# print(list(range(19, 2, -1)))  # [19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3]
# print(list(range(3, -10, -1)))  #  [3, 2, 1, 0, -1, -2, -3, -4, -5, -6, -7, -8, -9]
# 推导式生成列表
# print([x for x in range(1, 10)])  # [1, 2, 3, 4, 5, 6, 7, 8, 9]
# print([x*2 for x in range(1, 10) if x % 2 == 0])  # [4, 8, 12, 16]
# print([x for x in "range(1, 10) if x % 2 == 0"])  # ['r', 'a', 'n', 'g', 'e', '(', '1', ',', ' ', '1', '0', ')', ' ', 'i', 'f', ' ', 'x', ' ', '%', ' ', '2', ' ', '=', '=', ' ', '0']
# append与+:+运算符并不是真正的拼接，而是创建了一个新的列表，将原来的列表和新添加的元素组合成一个新的列表，这样，会涉及到内存的重新分配和复制，对于大列表来说，性能开销较大
# a= [1, 2, 3]
# print(id(a))
# b= a + [4]
# print(id(b))
# entend()方法，将目标列表的所有元素添加到原列表中，属于原地操作，不会创建新的列表
# a= [1, 2, 3]
# print(id(a))
# a.extend([4])
# print(id(a))
# find与index:
# find()方法用于查找子字符串在字符串中的位置，如果找到则返回第一个匹配的索引，否则返回-1
# index()方法用于查找子字符串在字符串中的位置，如果找到则返回第一个匹配的索引，否则引发ValueError异常
# a = 'Hello, World!'
# print(a.find('o'))  # 4
# print(a.index('o'))  # 4
# enumerate()函数用于将一个可遍历的数据对象（如列表、元组、字符串等）组合为一个索引序列，同时列出数据和数据下标
# enumertae(sequence, [start=0])
# a = ['a', 'b', 'c']
# for index, value in enumerate(a, start=1):
#     print(index, value)
# 字典的底层式散列表，集合的底层是散列表，列表的底层是动态数组
# 函数也是对象的底层分析
# def add(a, b):
#     return a + b
#
#
# print(add(1, 2))
# print(add.__name__)  # add
# print(add.__doc__)  # None
# print(add.__module__)  # __main__
# print(add.__code__)  # <code object add at 0x7f8c4c4d8e40, file "<stdin>", line 1>
# print(add.__defaults__)  # None
# print(add.__closure__)  # None
# print(
#     add.__globals__)  # {'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <_frozen_importlib_external.SourceFileLoader object at 0x7f8c4c4d8e40>, '__spec__': ModuleSpec(name='__main__', loader=<_frozen_importlib_external.SourceFileLoader object at 0x7f8c4c4d8e40>, origin='stdin')}
# print(add.__annotations__)  # {}
# print(add.__dict__)  # {}
# print(add.__class__)  # <class 'function'>
# print(add.__sizeof__())  # 128
# print(add.__code__.co_argcount)  # 2
# print(add.__code__.co_varnames)  # ('a', 'b')
# print(add.__code__.co_freevars)  # ()
# print(add.__code__.co_cellvars)  # ()
# print(add.__code__.co_filename)  # <stdin>
# print(add.__code__.co_name)  # add
# print(add.__code__.co_firstlineno)  # 1
# print(add.__code__.co_lnotab)  # <code object at 0x7f8c4c4d8e40, file "<stdin>", line 1>
# print(add.__code__.co_flags)  # 67
# print(add)
# print(id(add))  # 140694123456064
# c = add
# print(id(c))  # 140694123456064
# print(c(1, 2))  # 3
# global关键字
# x = 5  # 全局变量x
# def outer_function():
#     global x  # 声明x为全局变量
#     x = 10  # 修改全局变量x的值
#
#     def inner_function():
#         # nonlocal x  # 声明x为外层函数的变量nonlocal x  # 声明x为外层函数的变量
#     # ^^^^^^^^^^
# # SyntaxError: no binding for nonlocal 'x' found
#         x = 20  # 修改外层函数的变量x的值
#         print("Inner function:", x)  # 输出内层函数的变量x的值
#
#     inner_function()
#     print("Outer function:", x)  # 输出外层函数的变量x的值
#
#
# outer_function()
# print("Global variable:", x)  # 输出全局变量x的值 报错 nonlocal x  # 声明x为外层函数的变量
# 默认参数
# def fun1(a, b, c=1, d=2):
#     return a + b + c + d
# 
# 
# print(fun1(1, 2))  # 6
# print(fun1(1, 2, 3))  # 8
# print(fun1(1, 2, 3, 4))  # 10
# 可变参数
# def fun2(*args):  # 可变参数, args是一个元组
#     return sum(args)  # 返回所有参数的和
#
#
# print(fun2(1, 2, 3))  # 6
#
#
# def fun3(**kwargs):  # 可变参数, kwargs是一个字典
#     return kwargs  # 返回所有参数的字典
#
#
# print(fun3(a=1, b=2, c=3))  # {'a': 1, 'b': 2, 'c': 3}
# python中的参数传递都是引用传递，不是值传递
# 传递参数是可变对象，实际传递的是对象的引用，例如列表、字典等
# b=[1,2,3]
# def fun4(a):
#     print(id(a))
#     a.append(4)
# fun4(b)
# print(id(b))
# print(b)
#传递参数时不可变对象，例如字符串、元组等
# b='123'
# def fun5(a):
#     print(id(a))
#     a='456'
#     print(id(a))
# fun5(b)
# print(id(b))
# print(b)
# 传递不可变对象包含的子对象是可变的情况
# a = (1, 2, [3, 4])
#
#
# def fun6(a):
#     print(id(a))
#     a[2].append(5)
#
#
# fun6(a)
# print(id(a))
# print(a)
# eval(expression, globals, [locals])
# 实现原理:`eval()` 函数的实现原理如下：
#
# ### 实现步骤：
# 1. **解析（Parsing）**：将输入的字符串解析为合法的 Python 表达式。
# 2. **编译（Compilation）**：使用 `compile()` 函数将解析后的表达式编译为字节码，模式为 `eval`。
# 3. **执行（Execution）**：在指定的全局和局部命名空间中执行编译后的字节码，并返回结果。
#
# ### 示例代码：
# ```python
# # 示例：使用 eval() 计算表达式
# expression = "2 + 3 * 4"
# result = eval(expression)  # 计算表达式
# print(result)  # 输出：14
#
# # eval() 的底层实现
# # 第一步：编译表达式
# code = compile(expression, '<string>', 'eval')
#
# # 第二步：执行编译后的代码
# result = eval(code, globals(), locals())
# print(result)  # 输出：14
# ```
#
# ### 安全性问题：
# - `eval()` 可以执行任意代码，因此如果输入不受信任，可能会带来安全风险。
# - 为了降低风险，可以限制 `globals` 和 `locals` 的命名空间。
#
# ### 示例：限制命名空间
# ```python
# safe_globals = {"__builtins__": None}
# safe_locals = {"x": 10, "y": 20}
# expression = "x + y"
# result = eval(expression, safe_globals, safe_locals)
# print(result)  # 输出：30
# ```
# 类方法通过装饰器@ classmethod定义
"""
@classmethod
def class_method(cls, *args, **kwargs): cls必须有，cls是类本身，不需要也不能给cls传值
    pass    类方法中访问实例属性和实例方法会导致错误
    因为cls是类本身，不是实例对象，所以不能访问实例属性和实例方法
    只能访问类属性和类方法
    子类继承父类方法时，传入的cls是子类本身，而非父类对象
"""


class MyClass:
    class_attr = 0

    def __init__(self, value):
        self.instance_attr = value

    @classmethod
    def class_method(cls, *args, **kwargs):
        print("Class method called")
        print(f"Class attribute: {cls.class_attr}")
        # print(f"Instance attribute: {self.instance_attr}")  # 会导致错误


MyClass.class_method()  # 调用类方法
# 类方法与类中定义普通方法的区别：
# ### 分析用户提出的4条区别：
#
# #### **正确的描述（3条）**：
# 1. **类方法可以通过类名直接调用，而普通方法需要实例化对象才能调用**
#    - ✅ 正确
#    - 类方法用 `@classmethod` 装饰器，可直接通过 `ClassName.method()` 调用；普通方法必须通过实例对象调用。
#
# 2. **类方法的第一个参数是 `cls`，表示类本身，而普通方法的第一个参数是 `self`，表示实例对象**
#    - ✅ 正确
#    - 这是语法约定（参数名可任意修改，但约定俗成用 `cls` 和 `self`）。
#
# 4. **类方法不能访问实例属性和实例方法**
#    - ✅ 正确
#    - 类方法没有 `self` 参数，无法直接访问实例属性或方法（需通过实例对象间接访问）。
#
# ---
#
# #### **部分错误（1条）**：
# 3. **类方法可以访问类属性和类方法，而普通方法可以访问实例属性和实例方法**
#    - ⚠️ **部分错误**
#    - **正确部分**：
#      - 类方法确实可以访问类属性和其他类方法（通过 `cls`）。
#      - 普通方法可以访问实例属性和实例方法（通过 `self`）。
#    - **错误部分**：
#      - 普通方法**也可以访问类属性和类方法**（例如通过 `self.__class__.class_attribute` 或直接调用类名）。
#      - 类方法**不能直接访问实例属性或方法**（除非传递实例对象进去）。
#
# ---
#
# ### **修正后的完整结论**：
# | 序号 | 原描述                                                       | 正确性       | 修正说明                                                     |
# |------|------------------------------------------------------------|-------------|------------------------------------------------------------|
# | 1    | 类方法可通过类名直接调用，普通方法需实例化对象调用             | ✅ 正确      | 无                                                         |
# | 2    | 类方法参数是 `cls`，普通方法参数是 `self`                     | ✅ 正确      | 无                                                         |
# | 3    | 类方法访问类属性和类方法，普通方法访问实例属性和实例方法         | ⚠️ 部分错误 | 普通方法也能访问类属性，类方法不能访问实例属性                |
# | 4    | 类方法不能访问实例属性和实例方法                               | ✅ 正确      | 无                                                         |
#
# ---
#
# ### **代码验证**：
# ```python
# class MyClass:
#     class_attr = "类属性"  # 类属性
#
#     def __init__(self):
#         self.instance_attr = "实例属性"  # 实例属性
#
#     @classmethod
#     def class_method(cls):
#         print(f"类方法访问类属性: {cls.class_attr}")  # ✅ 正确
#         # print(cls.instance_attr)  # ❌ 报错，无法直接访问实例属性
#
#     def instance_method(self):
#         print(f"实例方法访问实例属性: {self.instance_attr}")  # ✅ 正确
#         print(f"实例方法访问类属性: {self.__class__.class_attr}")  # ✅ 正确
#
# # 测试调用
# MyClass.class_method()          # 类方法直接通过类名调用
# obj = MyClass()
# obj.instance_method()           # 普通方法通过实例调用
# ```
#
# ---
#
# ### **总结**：
# - **3条正确**（1、2、4），**1条部分错误**（3）。
# - 关键区别在于：
#   - 类方法操作类层级的属性和逻辑，不依赖实例。
#   - 普通方法操作实例层级的属性和逻辑，但可间接访问类层级内容。
#
# **答案：假的**。
# 无论是类方法还是普通方法（实例方法），**子类都可以重写父类的方法**。关键在于方法的定义方式和调用逻辑：
#
# ---
#
# #### **核心区别**
# | **方法类型**    | **定义方式**                 | **调用对象**       | **能否被重写** |
# |------------------|----------------------------|--------------------|----------------|
# | **类方法**       | 使用 `@classmethod` 装饰器 | 类或实例均可调用   | ✅ 可以         |
# | **普通方法**     | 无装饰器                   | 必须通过实例调用   | ✅ 可以         |
#
# ---
#
# #### **示例代码**
# ```python
# class Parent:
#     # 普通方法（实例方法）
#     def normal_method(self):
#         print("父类普通方法")
#
#     # 类方法
#     @classmethod
#     def class_method(cls):
#         print("父类类方法")
#
# class Child(Parent):
#     # 重写父类普通方法
#     def normal_method(self):
#         print("子类重写普通方法")
#
#     # 重写父类类方法
#     @classmethod
#     def class_method(cls):
#         print("子类重写类方法")
#
# # 测试调用
# child = Child()
# child.normal_method()  # 输出：子类重写普通方法
# Child.class_method()   # 输出：子类重写类方法
# ```
#
# ---
#
# #### **注意事项**
# 1. **装饰器一致性**
#    重写类方法时需保持 `@classmethod` 装饰器，否则会变成普通方法。
#
# 2. **静态方法特殊规则**
#    静态方法（`@staticmethod`）也可被重写，但与类方法/普通方法无关。
#
# 3. **调用优先级**
#    子类重写方法后，调用时优先使用子类实现。若需调用父类方法，使用 `super()`：
#    ```python
#    class Child(Parent):
#        def normal_method(self):
#            super().normal_method()  # 调用父类方法
#    ```
#
# ---
#
# #### **总结**
# - **普通方法、类方法、静态方法均可被子类重写**。
# - 用户提到的“普通方法不能重写”是错误观点。
# - 区别在于方法的调用逻辑（类方法可通过类直接调用），而非能否被重写。
# __init__(self,...)方法 初始化对象，在创建对象时调用
# __del__(self)方法 销毁对象时调用
# __str__(self)方法 返回对象的字符串表示
# __repr__(self)方法 返回对象的正式字符串表示
# __len__(self)方法 返回对象的长度
# __getitem__(self, key)方法 获取对象的元素
# __setitem__(self, key, value)方法 设置对象的元素
# __delitem__(self, key)方法 删除对象的元素
# __iter__(self)方法 返回对象的迭代器
# __next__(self)方法 返回对象的下一个元素
# __contains__(self, item)方法 判断对象是否包含某个元素
# __call__(self, *args, **kwargs)方法 调用对象
# __eq__(self, other)方法 判断对象是否相等
# __ne__(self, other)方法 判断对象是否不相等
# __lt__(self, other)方法 判断对象是否小于另一个对象
# __le__(self, other)方法 判断对象是否小于等于另一个对象
# __gt__(self, other)方法 判断对象是否大于另一个对象
# __ge__(self, other)方法 判断对象是否大于等于另一个对象
# __add__(self, other)方法 对象相加
# __sub__(self, other)方法 对象相减
# __mul__(self, other)方法 对象相乘
# __truediv__(self, other)方法 对象相除
# __floordiv__(self, other)方法 对象取整除
# __mod__(self, other)方法 对象取模
# __pow__(self, other)方法 对象取幂
# __and__(self, other)方法 对象按位与
# __or__(self, other)方法 对象按位或
# __xor__(self, other)方法 对象按位异或
# __invert__(self)方法 对象按位取反
# __enter__(self)方法 进入上下文管理器
# __exit__(self, exc_type, exc_value, traceback)方法 退出上下文管理器
# __bool__(self)方法 判断对象是否为真
# __hash__(self)方法 返回对象的哈希值
# __sizeof__(self)方法 返回对象的大小
# __format__(self, format_spec)方法 返回对象的格式化字符串
# __index__(self)方法 返回对象的索引值
# __reversed__(self)方法 返回对象的反向迭代器
# __new__(cls, *args, **kwargs)方法 创建对象
# __reduce__(self)方法 返回对象的可序列化表示
# __reduce_ex__(self, protocol)方法 返回对象的可序列化表示
# __getstate__(self)方法 返回对象的状态
# __setstate__(self, state)方法 设置对象的状态
# __cmp__(stc,dst)方法 比较对象
# __getattr__(self, name)方法 获取对象的属性
# __setattr__(self, name, value)方法 设置对象的属性
# __delattr__(self, name)方法 删除对象的属性
# __getattribute__(self, name)方法 获取对象的属性
# __call__(self, *args, **kwargs)方法 调用对象,可调用对象，对象可像函数一样被调用
# __contains__(self, item)方法 判断对象是否包含某个元素
# class Salary:
#     def __init__(self, base_salary, bonus):
#         self.base_salary = base_salary
#         self.bonus = bonus
#
#     def __add__(self, other):
#         return Salary(self.base_salary + other.base_salary, self.bonus + other.bonus)
#
#     def __str__(self):
#         return f"Base Salary: {self.base_salary}, Bonus: {self.bonus}"
#     def __repr__(self):
#         return f"Salary({self.base_salary}, {self.bonus})"
#     def __len__(self):
#         return self.base_salary + self.bonus
#     def __getitem__(self, key):
#         if key == 'base_salary':
#             return self.base_salary
#         elif key == 'bonus':
#             return self.bonus
#         else:
#             raise KeyError(f"Invalid key: {key}")
#     def __setitem__(self, key, value):
#         if key == 'base_salary':
#             self.base_salary = value
#         elif key == 'bonus':
#             self.bonus = value
#         else:
#             raise KeyError(f"Invalid key: {key}")
#     def __delitem__(self, key):
#         if key == 'base_salary':
#             del self.base_salary
#         elif key == 'bonus':
#             del self.bonus
#         else:
#             raise KeyError(f"Invalid key: {key}")
#     def __iter__(self):
#         return iter([self.base_salary, self.bonus])
#     def __next__(self):
#         return next(iter(self))
#     def __contains__(self, item):
#         return item in [self.base_salary, self.bonus]
#     def __call__(self, *args, **kwargs):
#         return dict(base_salary=self.base_salary, bonus=self.bonus)
# s=Salary(1000, 200)
# print(s.base_salary)  # 1000
# print(s.bonus)  # 200
# print(s)  # Base Salary: 1000, Bonus: 200
# print(len(s))  # 1200
# print(s['base_salary'])  # 1000
# print(s['bonus'])  # 200
# s['base_salary'] = 1500
# print(s['base_salary'])  # 1500
# del s['base_salary']
# # print(s['base_salary'])  # KeyError: 'base_salary'
# # print('base_salary' in s)  # False
# # print('bonus' in s)  # True
# # print(s())  # {'base_salary': 1500, 'bonus': 200}
# print(s.__dict__)  # {'base_salary': 1500, 'bonus': 200}
"""
两个下划线开头的属性是私有的，其他为公共的
类内部可以访问私有属性（方法）
类外部不能访问私有属性（方法）
类外部可以通过类名._类名__私有属性（方法）访问私有属性（方法）
dir()函数不带参数，返回当前范围内的变量、方法和定义的类型列表；带参数时。返回参数的属性和方法列表，如果参数包含__dir()__,该方法被调用。如果不包含__dir()__，该方法将最大限度的收集参数信息
"""
# print(dir())  # 返回当前范围内的变量、方法和定义的类型列表
"""
@Property装饰器：再绑定属性时，如果直接把属性暴露出去，虽然写起来简单，但是，没办法检查属性的合法性"""

# class Person:
#
#     def __init__(self, name, age):
#         self.__name = name
#         self.__age = age
#         self.__score = 0
#
#
# s = Person('Tom', 20)
# # print(s.__name)  # 报错
# s.__name = 'Jerry'  # 这不是修改私有属性，而是创建了一个新的属性
# s.score = 100
# print(s.score)  # 100
# get() and set()
# class Person:
#     def __init__(self, name, age):
#         self.__name = name
#         self.__age = age
#         self.__score = 0
#     def get_name(self):
#         return self.__name
#     def set_name(self, name):
#         self.__name = name
#     def get_age(self):
#         return self.__age
#     def set_age(self, age):
#         self.__age = age
#     def get_score(self):
#         return self.__score
#     def set_score(self, score):
#         self.__score = score
#     def __str__(self):
#         return f"Name: {self.__name}, Age: {self.__age}, Score: {self.__score}"
#     def __repr__(self):
#         return f"Person({self.__name}, {self.__age}, {self.__score})"
#     def __len__(self):
#         return self.__age
#     def __getitem__(self, key):
#         if key == 'name':
#             return self.__name
#         elif key == 'age':
#             return self.__age
#         elif key == 'score':
#             return self.__score
#         else:
#             raise KeyError(f"Invalid key: {key}")
#     def __setitem__(self, key, value):
#         if key == 'name':
#             self.__name = value
#         elif key == 'age':
#             self.__age = value
#         elif key == 'score':
#             self.__score = value
#         else:
#             raise KeyError(f"Invalid key: {key}")
#     def __delitem__(self, key):
#         if key == 'name':
#             del self.__name
#         elif key == 'age':
#             del self.__age
#         elif key == 'score':
#             del self.__score
#         else:
#             raise KeyError(f"Invalid key: {key}")
#     def __iter__(self):
#         return iter([self.__name, self.__age, self.__score])
#     def __next__(self):
#         return next(iter(self))
# s= Person('Tom', 20)
# print(s.get_name())  # Tom
# print(s.get_age())  # 20
# print(s.get_score())  # 0
# python中可以使用@property装饰器来实现属性的getter和setter方法
# class Person:
#     def __init__(self, name, age):
#         self.__name = name
#         self.__age = age
#         self.__score = 0
#     @property
#     def name(self):
#         return self.__name
#     @name.setter
#     def name(self, name):
#         self.__name = name
#     @property
#     def age(self):
#         return self.__age
#     @age.setter
#     def age(self, age):
#         self.__age = age
#     @property
#     def score(self):
#         return self.__score
#     @score.setter
#     def score(self, score):
#         self.__score = score
#     def __str__(self):
#         return f"Name: {self.__name}, Age: {self.__age}, Score: {self.__score}"
# s= Person('Tom', 20)
# print(s.name)  # Tom
# print(s.age)  # 20
# print(s.score)  # 0
# s.name = 'Jerry'
# print(s.name)  # Jerry
# s.age = 30
# print(s.age)  # 30
# s.score = 100
# print(s.score)  # 100
# mro() __mrio__方法返回类的继承顺序
# class A:
#     pass
# class B(A):
#     pass
# class C(A):
#     pass
# class D(B, C):
#     pass
# print(D.__mro__)
# (<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>)
# class A:
#     def say(self):
#         print("A")
# class B(A):
#     def say(self):
#         A.say(self)
#         super().say()
#         print("B")
# b=B()
# b.say()
# class Animal:
#     def speak(self):
#         print("Animal speaks")
# class Dog(Animal):
#     def speak(self):
#         print("Dog barks")
# class Cat(Animal):
#     def speak(self):
#         print("Cat meows")
# def animal_speak(animal):
#     if isinstance(animal, Animal):
#         animal.speak()
# animal_speak(Dog())  # Dog barks
# animal_speak(Cat())  # Cat meows
"""
对象的深浅拷贝：对象包含的子对象内容不拷贝，因此，源对象和拷贝对象会引用同一个子对象，如果想实现深拷贝，可以使用copy模块中的deepcopy()函数，
递归拷贝对象中包含的子对象，源对象和拷贝对象所有的子对象也不同"""
# import copy
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         self.hobbies = ['reading', 'sports']
# class Student(Person):
#     def __init__(self, name, age, student_id):
#         super().__init__(name, age)
#         self.student_id = student_id
#     def __str__(self):
#         return f"Name: {self.name}, Age: {self.age}, Student ID: {self.student_id}, Hobbies: {self.hobbies}"
# class ScholarshipStudent(Student):
#     def __init__(self, name, age, student_id, scholarship_amount):
#         super().__init__(name, age, student_id)
#         self.scholarship_amount = scholarship_amount
#     def __str__(self):
#         return f"Name: {self.name}, Age: {self.age}, Student ID: {self.student_id}, Scholarship Amount: {self.scholarship_amount}, Hobbies: {self.hobbies}"
# c=Student()
# s=ScholarshipStudent('Tom', 20, '123456', 1000)
# m=Person('Jerry', 25)
# print("浅拷贝")
# m2=copy.copy(m)
# m.hobbies.append('music')
# 设计模式：
# 1.单例模式
"""
模式的主要目的时确保一个类只有一个实例，并提供一个全局访问点
"""


# class Singleton:
#     _instance = None
#
#     def __new__(cls, *args, **kwargs):
#         if not cls._instance:
#             cls._instance = super().__new__(cls)
#         return cls._instance
# singleton1 = Singleton()
# singleton2 = Singleton()
# print(singleton1 is singleton2)  # True
# 在 Python 中，`__new__` 是一个特殊的**静态方法**（虽然通常用 `@staticmethod` 装饰，但实际由解释器隐式处理），它是**对象实例化的第一入口**。理解 `__new__` 是掌握 Python 对象创建机制的关键。以下是详细解析：
#
# ---
#
# ### **核心作用**
# `__new__` **负责创建并返回类的实例**，而 `__init__` 负责初始化实例。
# 执行顺序：`__new__` → `__init__`（若 `__new__` 返回正确类型的实例）。
#
# ---
#
# ### **方法签名**
# ```python
# def __new__(cls, *args, **kwargs) -&gt; instance:
#     # 必须返回一个实例对象（通常是 cls 的实例）
# ```
#
# - **`cls`**：当前正在被实例化的类（不是实例！）
# - **`*args, **kwargs`**：传递给 `__init__` 的参数（如果 `__new__` 返回实例）
#
# ---
#
# ### **与 `__init__` 的关键区别**
# | **`__new__`**                | **`__init__`**              |
# |------------------------------|-----------------------------|
# | 创建实例                      | 初始化实例                   |
# | 必须返回实例对象              | 无返回值 (`None`)            |
# | 控制是否创建新实例            | 每次实例化必执行             |
# | 可修改实例类型（返回其他类实例）| 只能修改当前实例的属性        |
#
# ---
#
# ### **典型应用场景**
#
# #### **1. 单例模式（Singleton）**
# ```python
# class Singleton:
#     _instance = None
#
#     def __new__(cls, *args, **kwargs):
#         if not cls._instance:
#             cls._instance = super().__new__(cls)  # 首次创建实例
#         return cls._instance  # 后续直接返回已存在的实例
#
# # 测试
# a = Singleton()
# b = Singleton()
# print(a is b)  # 输出: True
# ```
#
# #### **2. 不可变类型的子类化**
# ```python
# class MyStr(str):
#     def __new__(cls, value):
#         # 在实例化前修改值
#         modified_value = value.upper() + "!"
#         return super().__new__(cls, modified_value)
#
# s = MyStr("hello")
# print(s)  # 输出: HELLO!
# ```
#
# #### **3. 对象池（复用实例）**
# ```python
# class ConnectionPool:
#     _pool = []
#
#     def __new__(cls, *args, **kwargs):
#         if not cls._pool:
#             new_conn = super().__new__(cls)
#             new_conn._init_conn(*args, **kwargs)  # 自定义初始化方法
#             cls._pool.append(new_conn)
#         return cls._pool.pop()
#
#     def _init_conn(self, host, port):
#         self.host = host
#         self.port = port
#
#     def close(self):
#         self._pool.append(self)  # 放回池中
# ```
#
# ---
#
# ### **注意事项**
# 1. **必须返回实例**
#    如果 `__new__` 未返回实例（或返回其他类的实例），则 `__init__` 不会执行：
#    ```python
#    class Broken:
#        def __new__(cls):
#            return "字符串实例"  # 错误！返回非实例对象
#
#    obj = Broken()  # obj 是字符串，不会触发 __init__
#    ```
#
# 2. **父类调用**
#    必须通过 `super().__new__` 调用父类的 `__new__`，否则可能破坏继承链：
#    ```python
#    class Base: pass
#
#    class Child(Base):
#        def __new__(cls):
#            # 错误！直接调用 object.__new__ 会跳过 Base 的逻辑
#            return object.__new__(cls)
#    ```
#
# 3. **元类冲突**
#    如果类定义了元类（`__metaclass__`），则 `__new__` 的执行可能受元类控制。
#
# ---
#
# ### **执行流程示例**
# ```python
# class Demo:
#     def __new__(cls, *args, **kwargs):
#         print("__new__ 执行，参数:", args, kwargs)
#         instance = super().__new__(cls)
#         return instance
#
#     def __init__(self, x):
#         print("__init__ 执行，x=", x)
#         self.x = x
#
# # 实例化过程
# obj = Demo(42)
# # 输出:
# # __new__ 执行，参数: (42,) {}
# # __init__ 执行，x= 42
# ```
#
# ---
#
# ### **总结**
# - `__new__` 是**对象创建的起点**，控制实例的生成逻辑。
# - 适用于需要**定制实例创建过程**的场景（如单例、不可变类型、对象池等）。
# - 必须谨慎处理返回值，并确保与 `__init__` 的协作。
# ### 关于 `cls` 的底层本质剖析
#
# #### **1. `cls` 是什么？**
# - **表面含义**：`cls` 是类方法（`@classmethod`）的第一个参数，**指向当前类本身**（类似 `self` 指向实例）。
# - **底层本质**：在 Python 中，**类本身也是一个对象**（称为“类对象”），而 `cls` 就是这个类对象的引用。它是通过**元类（metaclass）**创建的实例。
#
# ---
#
# #### **2. `cls` 的底层运行机制**
# ##### **(1) 类的本质**
# - **类 = 元类的实例**
#   Python 中所有类（如 `class MyClass`）本质上是**元类（默认是 `type`）的实例**。元类负责生成类对象，类对象负责生成实例对象。
#   ```python
#   # 类对象 MyClass 是 type 的实例
#   class MyClass: pass
#   print(type(MyClass))  # 输出: &lt;class &apos;type&apos;&gt;
#   ```
#
# ##### **(2) `cls` 的绑定逻辑**
# - **动态绑定**
#   当通过类或实例调用类方法时，Python 自动将类对象传给 `cls` 参数：
#   ```python
#   class MyClass:
#       @classmethod
#       def my_cls_method(cls):
#           print(cls)  # cls 是当前类对象
#
#   MyClass.my_cls_method()  # 输出: &lt;class &apos;__main__.MyClass&apos;&gt;
#   obj = MyClass()
#   obj.my_cls_method()      # 输出同上（仍绑定类对象）
#   ```
#
# ---
#
# #### **3. `cls` 的核心作用**
# ##### **(1) 访问类级资源**
# - **直接操作类属性/方法**
#   ```python
#   class Dog:
#       total = 0  # 类属性
#
#       def __init__(self, name):
#           self.name = name
#           Dog.total += 1  # 直接写 Dog.total 会硬编码类名
#
#       @classmethod
#       def get_total(cls):
#           return cls.total  # 用 cls 动态获取类属性（支持继承）
#   ```
#
# ##### **(2) 多态与继承**
# - **动态识别子类**
#   ```python
#   class Animal:
#       @classmethod
#       def create(cls, name):
#           return cls(name)  # 若子类调用，自动创建子类实例
#
#   class Cat(Animal): pass
#
#   cat = Cat.create("Mimi")  # 实际调用的是 Cat 的类方法
#   print(type(cat))  # 输出: &lt;class &apos;__main__.Cat&apos;&gt;
#   ```
#
# ##### **(3) 元类编程**
# - **在元类中控制类创建**
#   ```python
#   class Meta(type):
#       def __new__(cls, name, bases, attrs):
#           # cls 是元类自身（这里是 Meta）
#           # 此处可动态修改类定义
#           return super().__new__(cls, name, bases, attrs)
#
#   class MyClass(metaclass=Meta): pass
#   ```
#
# ---
#
# #### **4. 与 `self` 的对比**
# | **特性**       | **`cls`**                     | **`self`**                   |
# |----------------|------------------------------|------------------------------|
# | **指向对象**    | 类对象（如 `MyClass`）        | 实例对象（如 `obj = MyClass()`） |
# | **方法类型**    | 类方法（`@classmethod`）      | 实例方法                      |
# | **访问范围**    | 类属性、其他类方法            | 实例属性、类属性（通过 `self.__class__`） |
# | **多态支持**    | 自动绑定子类（继承时）         | 绑定当前实例的类              |
#
# ---
#
# #### **5. 关键结论**
# - `cls` **是类方法中动态绑定的类对象引用**，其本质是元类创建的实例。
# - 使用 `cls` 而非硬编码类名，能确保代码在继承时**自动适配子类**。
# - 在元类编程中，`cls` 指向元类自身，用于控制类的生成逻辑。
#
# ---
#
# **示例：动态工厂模式**
# ```python
# class Vehicle:
#     def __init__(self, name):
#         self.name = name
#
#     @classmethod
#     def from_config(cls, config):
#         # 根据配置动态创建子类实例
#         if config["type"] == "car":
#             return Car(config["name"])
#         elif config["type"] == "bike":
#             return Bike(config["name"])
#
# class Car(Vehicle): pass
# class Bike(Vehicle): pass
#
# # 使用类方法创建不同子类
# config = {"type": "car", "name": "Tesla"}
# vehicle = Vehicle.from_config(config)  # 实际返回 Car 实例
# ```
# ### `cls` 与类加载机制的深度关联
#
# 在 Python 中，`cls` 参数与类加载机制的关系体现在**类的创建、初始化、实例化全流程**中。以下是逐层剖析：
#
# ---
#
# #### **1. 类加载的核心流程**
# Python 的类加载分为三个阶段：
# 1. **类定义解析**：解释器读取类代码，生成类命名空间。
# 2. **元类介入**：调用元类的 `__new__` 和 `__init__` 方法，生成类对象。
# 3. **实例化**：通过类对象的 `__new__` 和 `__init__` 创建实例。
#
# **`cls` 参数在不同阶段扮演不同角色**。
#
# ---
#
# #### **2. 元类阶段：`cls` 是元类的操作对象**
# 当定义类时，Python 隐式调用元类的 `__new__` 方法生成类对象：
# ```python
# # 元类的 __new__ 方法签名
# def __new__(cls, name, bases, attrs) -&gt; 类对象:
# ```
# - **这里的 `cls` 是元类自身**（如 `type` 或其子类）。
# - **返回的类对象**会成为后续类方法中 `cls` 的值。
#
# ##### **示例：自定义元类控制类生成**
# ```python
# class Meta(type):
#     def __new__(cls, name, bases, attrs):
#         # cls 是 Meta 类对象
#         print(f"[元类阶段] 创建类: {name}")
#         return super().__new__(cls, name, bases, attrs)
#
# class MyClass(metaclass=Meta):
#     @classmethod
#     def method(cls):
#         print(f"[类方法] cls={cls}")
#
# # 输出: [元类阶段] 创建类: MyClass
# ```
# - **元类的 `cls`**：指向元类自身（`Meta`）。
# - **类方法中的 `cls`**：指向生成的类对象（`MyClass`）。
#
# ---
#
# #### **3. 类对象阶段：`cls` 是动态绑定的类引用**
# 当类加载完成后，`cls` 在类方法中动态绑定到当前类对象：
# ```python
# class Parent:
#     @classmethod
#     def create(cls):
#         print(f"创建 {cls.__name__} 的实例")
#         return cls()
#
# class Child(Parent): pass
#
# Child.create()  # 输出: 创建 Child 的实例
# ```
# - **动态绑定机制**：通过方法调用时的隐式参数传递，`cls` 自动绑定到实际调用者所属的类（如 `Child`）。
#
# ---
#
# #### **4. 实例化阶段：`cls` 控制对象生成**
# 在实例化过程中，`__new__` 方法的 `cls` 参数是类对象，决定实例类型：
# ```python
# class Singleton:
#     _instance = None
#
#     def __new__(cls, *args, **kwargs):
#         if not cls._instance:
#             # cls 是类对象，控制实例生成
#             cls._instance = super().__new__(cls)
#         return cls._instance
#
# a = Singleton()  # cls=Singleton
# b = Singleton()
# print(a is b)  # True
# ```
#
# ---
#
# #### **5. 类加载与 `cls` 的交互总结**
# | **阶段**       | **操作主体**   | **`cls` 含义**              | **关键行为**                     |
# |----------------|---------------|----------------------------|----------------------------------|
# | **元类阶段**   | 元类（如 `type`） | 元类自身                    | 生成类对象，定义类结构            |
# | **类对象阶段** | 类方法         | 当前类对象（如 `MyClass`）  | 动态绑定，支持继承和多态           |
# | **实例化阶段** | `__new__`     | 类对象                      | 控制实例的创建逻辑                |
#
# ---
#
# #### **6. 底层原理：描述符协议与方法绑定**
# Python 通过描述符协议实现 `cls` 的自动绑定：
# - **类方法**本质上是**类级别绑定**的描述符。
# - 当调用 `MyClass.method()` 时：
#   1. 查找 `method` 属性，发现是类方法。
#   2. 触发 `__get__` 方法，将 `MyClass` 绑定为 `cls` 参数。
#   3. 执行方法体。
#
# ---
#
# #### **7. 实战：动态修改类加载行为**
# 通过元类和 `cls` 参数，可动态注入类属性：
# ```python
# class AutoRegisterMeta(type):
#     def __new__(cls, name, bases, attrs):
#         # 自动添加 registry 属性
#         attrs[&apos;registry&apos;] = []
#         new_class = super().__new__(cls, name, bases, attrs)
#         return new_class
#
# class User(metaclass=AutoRegisterMeta):
#     @classmethod
#     def register(cls, name):
#         cls.registry.append(name)
#
# User.register("Alice")
# print(User.registry)  # 输出: [&apos;Alice&apos;]
# ```
#
# ---
#
# ### **总结**
# - **类加载机制**定义了类从代码到内存对象的转化过程。
# - **`cls` 参数**在不同阶段分别代表元类、类对象，是控制类生成和方法绑定的核心枢纽。
# - 理解 `cls` 与类加载的关系，可深入掌握 Python 的面向对象设计哲学。
# ** 工厂模式的实质是**“将对象的创建与使用解耦”**，而“配置类”是其可能依赖的一种辅助手段，并非核心目的。以下是详细分析：
#
# ---
#
# ### **1. 工厂模式的核心目标**
# 工厂模式属于**创建型设计模式**，其核心价值在于：
# - **封装对象创建逻辑**：将 `new` 操作隐藏，避免客户端直接依赖具体类。
# - **支持扩展与多态**：通过工厂动态生成不同子类或实现类。
# - **统一创建入口**：集中管理对象初始化过程（如配置参数、依赖注入）。
#
# **示例**：
# ```python
# # 简单工厂：根据参数决定创建哪种对象
# class LoggerFactory:
#     @staticmethod
#     def get_logger(log_type):
#         if log_type == "file":
#             return FileLogger()
#         elif log_type == "console":
#             return ConsoleLogger()
# ```
#
# ---
#
# ### **2. 配置类的作用**
# 配置类通常用于**集中管理应用程序的运行时参数**，例如：
# - 读取配置文件（如 `config.ini`、`settings.yaml`）。
# - 存储数据库连接字符串、API密钥等。
# - 提供全局访问点，避免硬编码。
#
# **示例**：
# ```python
# class AppConfig:
#     def __init__(self):
#         self.db_url = os.getenv("DB_URL")
#         self.api_key = os.getenv("API_KEY")
# ```
#
# ---
#
# ### **3. 工厂模式与配置类的关系**
# #### **可能结合的场景**
# - 工厂根据配置参数创建特定对象：
#   ```python
#   class DatabaseFactory:
#       @classmethod
#       def create(cls):
#           config = AppConfig()  # 依赖配置类
#           if config.db_type == "mysql":
#               return MySQLAdapter(config.db_url)
#           elif config.db_type == "postgres":
#               return PostgresAdapter(config.db_url)
#   ```
# - **此时配置类仅为工厂提供参数**，工厂仍是创建逻辑的掌控者。
#
# #### **本质区别**
# | **维度**       | **工厂模式**                     | **配置类**                     |
# |----------------|----------------------------------|--------------------------------|
# | **核心职责**   | 创建对象                         | 管理配置数据                   |
# | **设计目标**   | 解耦创建与使用                   | 统一参数管理                   |
# | **典型方法**   | `create()`, `get_instance()`     | `load()`, `get(key)`           |
# | **依赖方向**   | 可能依赖配置类                    | 独立存在，被其他组件依赖         |
#
# ---
#
# ### **4. 为何说“实质是配置类”不准确？**
# - **场景局限性**：并非所有工厂都需要配置类（如硬编码参数的简单工厂）。
# - **逻辑主体性**：工厂的核心是**创建逻辑**，配置只是其输入数据。
# - **模式独立性**：配置类可独立存在，无需工厂模式配合（如直接读取配置）。
#
# **反例**：不依赖配置的工厂：
# ```python
# class ShapeFactory:
#     @staticmethod
#     def create_shape(shape_type):
#         if shape_type == "circle":
#             return Circle()
#         elif shape_type == "square":
#             return Square()
# ```
#
# ---
#
# ### **5. 正确理解工厂模式的实质**
# - **核心思想**：**“对象创建的抽象化”**。
# - **关键实现**：
#   - 定义接口（如 `Factory` 类或方法）。
#   - 让子类或具体实现决定实例化哪个类。
# - **设计价值**：
#   - 符合开闭原则（扩展时无需修改客户端代码）。
#   - 提高代码可测试性（可通过 Mock 工厂替换真实对象）。
#
# ---
#
# ### **总结**
# - **工厂模式的实质是对象创建逻辑的封装与抽象**，而非单纯配置管理。
# - 配置类可为工厂提供参数，但只是辅助角色。
# - 将两者等同会模糊工厂模式的核心价值，降低设计清晰度。
# ### 关于 `cls` 与子类关系的深度解析
#
# 在 Python 中，`cls` 是类方法（`@classmethod`）的第一个参数，**动态绑定到当前调用者的类对象**。它与子类的关系体现了面向对象设计中**继承**与**多态**的核心机制。以下从底层逻辑到实际场景逐步剖析：
#
# ---
#
# ### **1. `cls` 在继承中的动态绑定**
# #### **关键特性**：
# - **动态性**：无论通过父类还是子类调用类方法，`cls` 始终指向实际调用者的类对象。
# - **多态支持**：子类继承父类的类方法时，方法内的 `cls` 会自动绑定到子类，无需显式修改。
#
# #### **示例**：
# ```python
# class Parent:
#     @classmethod
#     def create(cls):
#         print(f"创建 {cls.__name__} 的实例")
#         return cls()  # 返回当前类的实例
#
# class Child(Parent): pass  # 继承父类的类方法
#
# # 通过子类调用父类方法
# child = Child.create()  # 输出: 创建 Child 的实例
# print(type(child))      # 输出: &lt;class &apos;__main__.Child&apos;&gt;
# ```
# - **逻辑**：
#   `Child` 没有重写 `create` 方法，但调用 `Child.create()` 时，`cls` 自动绑定到 `Child` 类对象，因此返回的是 `Child` 的实例。
#
# ---
#
# ### **2. `cls` 与类属性的访问**
# #### **类属性的继承规则**：
# - 子类可以**直接访问父类的类属性**（除非覆盖）。
# - 通过 `cls` 访问类属性时，会**动态解析当前类的属性值**。
#
# #### **示例**：
# ```python
# class Animal:
#     category = "生物"  # 父类属性
#
#     @classmethod
#     def show_category(cls):
#         print(f"类别: {cls.category}")
#
# class Dog(Animal):
#     category = "犬科"  # 覆盖父类属性
#
# Animal.show_category()  # 输出: 类别: 生物
# Dog.show_category()     # 输出: 类别: 犬科
# ```
# - **关键点**：
#   `Dog` 类覆盖了 `category` 属性，通过 `cls.category` 访问时，`cls` 指向子类，因此输出子类的属性值。
#
# ---
#
# ### **3. `cls` 在工厂模式中的应用**
# #### **动态创建子类实例**：
# 通过 `cls` 参数，父类方法可以**统一管理子类对象的创建**，实现多态工厂。
#
# #### **示例**：
# ```python
# class Shape:
#     @classmethod
#     def factory(cls, shape_type):
#         if shape_type == "circle":
#             return Circle()  # 返回子类实例
#         elif shape_type == "square":
#             return Square()
#         else:
#             return cls()     # 默认返回当前类实例
#
# class Circle(Shape): pass
# class Square(Shape): pass
#
# # 通过子类调用工厂方法
# circle = Circle.factory("circle")  # 返回 Circle 实例
# square = Square.factory("square")  # 返回 Square 实例
# ```
#
# ---
#
# ### **4. `cls` 与元类（Metaclass）的交互**
# #### **元类中的 `cls` 参数**：
# 在元类的 `__new__` 或 `__init__` 方法中，`cls` 参数指向**当前正在创建的类对象**（包括子类）。
#
# #### **示例**：
# ```python
# class Meta(type):
#     def __new__(cls, name, bases, attrs):
#         print(f"元类创建类: {name}")
#         return super().__new__(cls, name, bases, attrs)
#
# class Base(metaclass=Meta): pass  # 输出: 元类创建类: Base
# class Sub(Base): pass             # 输出: 元类创建类: Sub
# ```
# - **逻辑**：
#   子类 `Sub` 继承父类 `Base` 的元类 `Meta`，因此在创建 `Sub` 时，元类的 `__new__` 方法被调用，`cls` 参数指向元类自身（`Meta`），但生成的类对象是 `Sub`。
#
# ---
#
# ### **5. 覆盖类方法时的 `cls` 行为**
# #### **子类重写父类方法**：
# 如果子类覆盖了父类的类方法，方法内的 `cls` 绑定到子类，但仍可通过 `super()` 调用父类逻辑。
#
# #### **示例**：
# ```python
# class Parent:
#     @classmethod
#     def setup(cls):
#         print(f"父类方法: {cls}")
#
# class Child(Parent):
#     @classmethod
#     def setup(cls):
#         print(f"子类方法: {cls}")
#         super().setup()  # 调用父类方法，此时父类方法中的 cls 仍是 Child
#
# Child.setup()
# # 输出:
# # 子类方法: &lt;class &apos;__main__.Child&apos;&gt;
# # 父类方法: &lt;class &apos;__main__.Child&apos;&gt;
# ```
# - **关键点**：
#   即使父类方法被调用，`super().setup()` 中的 `cls` 仍指向子类，确保继承链的连贯性。
#
# ---
#
# ### **总结：`cls` 与子类关系的核心逻辑**
# | **场景**               | **`cls` 的指向**             | **设计意义**                     |
# |------------------------|-----------------------------|----------------------------------|
# | **子类调用父类方法**   | 子类对象 (`Child`)           | 支持多态，避免硬编码父类名        |
# | **访问类属性**         | 子类属性（若覆盖）            | 动态解析属性，提高灵活性          |
# | **工厂模式**           | 动态创建子类实例              | 统一入口，解耦创建逻辑            |
# | **元类生成子类**       | 元类自身 (`Meta`)            | 控制子类的生成行为                |
#
# **核心结论**：
# - `cls` 的**动态绑定**机制是 Python 继承和多态的基石。
# - 通过 `cls`，父类方法能感知子类的存在，无需提前知道子类的具体类型。
# - 这一特性广泛应用于工厂模式、ORM 框架、插件系统等需要灵活扩展的场景。
# 2.工厂模式
# class CarFactory:
#     def careteCar(self, brand):
#         if brand == "BMW":
#             return BMW()
#         elif brand == "Benz":
#             return Benz()
#         else:
#             raise ValueError("Unknown car brand")
#
#
# class Car:
#     def drive(self):
#         pass
#
#
# class BMW(Car):
#     def drive(self):
#         print("Driving a BMW")
#
#
# class Benz(Car):
#     def drive(self):
#         print("Driving a Benz")
#
#
# factory = CarFactory()
# car = factory.careteCar("BMW")
# car.drive()
# c2 = factory.careteCar("Benz")
# c2.drive()
# 3.观察者模式
# class Subject:
#     def __init__(self):
#         self._observers = []
#
#     def attach(self, observer):
#         self._observers.append(observer)
#
#     def detach(self, observer):
#         self._observers.remove(observer)
#
#     def notify(self, message):
#         for observer in self._observers:
#             observer.update(message)
# class Observer:
#     def update(self, message):
#         pass
# class ConcreteObserverA(Observer):
#     def update(self, message):
#         print(f"ConcreteObserverA received: {message}")
# class ConcreteObserverB(Observer):
#     def update(self, message):
#         print(f"ConcreteObserverB received: {message}")
# subject = Subject()
# observer_a = ConcreteObserverA()
# observer_b = ConcreteObserverB()
# subject.attach(observer_a)
# subject.attach(observer_b)
# subject.notify("Hello, Observers!")
# 4.策略模式
# 5.命令模式
# 一个模块无论导入多少次，这个模块在整个解释器
