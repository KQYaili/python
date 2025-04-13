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
#   print(type(MyClass))  # 输出: &lt;class 'type'&gt;
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
#   MyClass.my_cls_method()  # 输出: &lt;class '__main__.MyClass'&gt;
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
#   print(type(cat))  # 输出: &lt;class '__main__.Cat'&gt;
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
#         attrs['registry'] = []
#         new_class = super().__new__(cls, name, bases, attrs)
#         return new_class
#
# class User(metaclass=AutoRegisterMeta):
#     @classmethod
#     def register(cls, name):
#         cls.registry.append(name)
#
# User.register("Alice")
# print(User.registry)  # 输出: ['Alice']
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
# print(type(child))      # 输出: &lt;class '__main__.Child'&gt;
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
# # 子类方法: &lt;class '__main__.Child'&gt;
# # 父类方法: &lt;class '__main__.Child'&gt;
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
# file.flush() 刷新文件内部缓冲，直接把内部缓存的数据立刻写入文件，而不是被动的等待输出缓冲区写入
# file.readline()
# 多线程共享内存
# from multiprocessing import Process
# from multiprocessing import Manager
# from multiprocessing import Lock
# from multiprocessing import Value
# from multiprocessing import Array
# from multiprocessing import Queue
# from multiprocessing import Pool
# from multiprocessing import cpu_count
# from multiprocessing import Event
# from multiprocessing import Condition
# from multiprocessing import Semaphore
# from multiprocessing import shared_memory
# shared_nums=shared_memory.ShareableList(range(10))
# def do_work1(nums1):
#     for i in range(len(nums1)):
#         nums1[i] = nums1[i] * 2
#     print("Process 1:", nums1)
# def do_wokr2(nums2):
#     for i in range(len(nums2)):
#         nums2[i] = nums2[i] + 1
#     print("Process 2:", nums2)
# if __name__ == '__main__':
#     p1=Process(target=do_work1, args=(shared_nums,))
#     p2 = Process(target=do_wokr2, args=(shared_nums,))
#     p1.start()
#     p1.join()
#
#     p2.start()
#     # p2.join()
# asyncio异步交互模式
# import asyncio
# async def main():
#     print("Hello")
#     await asyncio.sleep(1)
#     print("World")
#     return "Hello World"
# asyncio.run(main())
# import asyncio
#
#
# async def main():
#     await asyncio.sleep(10)
#     return 42
#
# # new_event_loop() 创建一个新的事件循环
# loop = asyncio.new_event_loop()
# asyncio.set_event_loop(loop)
# try:
#     loop.run_until_complete(main())
# finally:
#     asyncio.set_event_loop(None)
#     loop.close()
# is和==的区别：
# is比较的是对象的内存地址，==比较的是对象的值
# run和start的区别:
# run是直接调用函数，start是创建一个新的线程并执行
# import multiprocessing
# import time
#
# def func(msg):
#     print("start:", msg)
#     time.sleep(3)
#     print("end：",msg)
# if __name__ == "__main__":
#     pool = multiprocessing.Pool(processes = 3)
#     for i in range(5):
#         msg = "hello %d" %(i)
#         #维持执行的进程总数为 processes，当一个进程执行完毕后会添加新的进程进去
#         pool.apply_async(func, (msg, ))
#     pool.close()#进程池关闭之后不再接收新的请求
#     #调用 join 之前
#     # ，先调用 close 函数，否则会出错。
#     # 执行完 close 后不会有新的进程加入到 pool,join 函数等待所有子进程结束
#     pool.join()
# import multiprocessing
# import time
# def func(msg):
#     print("start:", msg)
#     time.sleep(3)
#     print("end",msg)
# if __name__ == "__main__":
#     pool = multiprocessing.Pool(processes = 3)
#     for i in range(5):
#         msg = "hello %d" %(i)
#         #维持执行的进程总数为 processes，当一个进程执行完毕后会添加新的进程进去
#         # apply与apply_async的区别：
#         # apply是阻塞的，apply_async是非阻塞的
#         pool.apply(func, (msg, ))
#     pool.close()
#     #调用 join 之前，先调用 close 函数，否则会出错。
#     # 执行完 close 后不会有新的进程加入到 pool,join 函数等待所有子进程结束
#     pool.join()
# ### **问题解答：`def convert` 是接口回调吗？**
#
# #### **结论：是的，`convert` 是典型的接口回调应用。**
# 其核心逻辑通过**将函数作为参数传递**，实现灵活的类型转换功能。以下是详细分析：
#
# ---
#
# ### **1. 代码逻辑拆解**
# 假设视频中的 `convert` 函数如下：
# ```python
# def convert(func, seq):
#     """将序列中的每个元素通过 func 转换类型"""
#     converted = []
#     for item in seq:
#         converted.append(func(item))  # 关键点：调用传入的 func
#     return converted
# ```
#
# #### **使用示例**：
# ```python
# # 将字符串列表转为整数
# str_list = ["1", "2", "3"]
# int_list = convert(int, str_list)  # 输出: [1, 2, 3]
#
# # 将数字列表转为字符串
# num_list = [10, 20, 30]
# str_list = convert(str, num_list)  # 输出: ['10', '20', '30']
# ```
#
# ---
#
# ### **2. 接口回调的定义**
# - **接口回调**（Callback）的本质：**将函数作为参数传递，并在需要时调用它**。
# - 核心特征：
#   1. **函数作为参数**（如 `func`）。
#   2. **延迟执行**（在 `convert` 内部调用 `func`）。
#
# ---
#
# ### **3. 为什么说 `convert` 是接口回调？**
# | **关键点**          | **解释**                                                                 |
# |---------------------|--------------------------------------------------------------------------|
# | **参数传入函数**    | `func` 参数接受一个函数（如 `int`, `str`），符合回调的“传递行为”特性。 |
# | **动态调用逻辑**    | `convert` 不关心 `func` 的具体实现，只需调用它完成类型转换。            |
# | **解耦与扩展性**    | 更换 `func` 即可改变转换逻辑（如 `float`、自定义函数），无需修改 `convert`。 |
#
# ---
#
# ### **4. 对比其他常见回调示例**
# #### **(1) Python 内置函数 `map`**
# ```python
# # map 函数与 convert 逻辑类似
# ### **答案：是的，`convert` 是接口回调的典型实现。**
#
# ---
#
# ### **核心解释**
# 1. **接口回调的定义**
#    接口回调（Callback）指**将一个函数（A）作为参数传递给另一个函数（B）**，并在 B 中根据逻辑调用 A。其核心目的是**将控制权交给调用方**，让调用方自定义某些行为。
#
# 2. **代码分析**
#    根据描述，`convert` 函数接收两个参数：
#    - `func`: 一个函数（如类型转换函数 `int()`, `str()`）
#    - `seq`: 一个序列（如列表 `[1, 2, 3]`）
#
#    ```python
#    def convert(func, seq):
#        # 对 seq 中的每个元素应用 func
#        return [func(x) for x in seq]
#    ```
#
# 3. **为什么是接口回调？**
#    - `convert` **不关心 `func` 的具体实现**，只负责调用它。
#    - 调用方通过传递不同的 `func`，**动态控制转换逻辑**（如转整数、转字符串）。
#    - 符合回调的核心理念：**“定义与执行分离”**。
#
# ---
#
# ### **示例演示**
# ```python
# # 定义 convert 函数
# def convert(func, seq):
#     return [func(x) for x in seq]
#
# # 调用方自定义转换逻辑
# numbers = ["1", "2", "3"]
# converted = convert(int, numbers)  # 将字符串转整数
# print(converted)  # 输出: [1, 2, 3]
#
# # 另一种回调函数
# converted_str = convert(str.upper, ["a", "b", "c"])
# print(converted_str)  # 输出: ['A', 'B', 'C']
# ```
#
# ---
#
# ### **关键总结**
# | **概念**       | **说明**                                                                 |
# |----------------|--------------------------------------------------------------------------|
# | **接口回调**   | `convert` 接收函数参数 `func`，并在内部调用它，属于典型的回调设计。       |
# | **灵活扩展**   | 调用方通过传递不同函数（如 `int`, `str.upper`），实现不同功能，无需修改 `convert`。 |
# | **Python特性** | Python 中函数是一等公民，可直接作为参数传递，无需接口类（如 Java 的 Interface）。 |
#
# ---
#
# ### **类比理解**
# 想象你去餐厅点餐：
# - **厨师（`convert`函数）**：负责烹饪，但不知道具体做什么菜。
# - **你（调用方）**：通过传递“菜谱（`func`参数）”告诉厨师做什么。
# - **回调本质**：厨师按
# ### 进程池与线程池的阻塞与非阻塞详解
#
# #### **1. 核心概念**
# - **进程池（Process Pool）**：预先创建多个进程，用于处理 CPU 密集型任务（如数学计算、图像处理）。
# - **线程池（Thread Pool）**：预先创建多个线程，用于处理 I/O 密集型任务（如网络请求、文件读写）。
# - **阻塞（Blocking）**：任务提交后，主程序等待任务执行完成，期间无法执行其他操作。
# - **非阻塞（Non-Blocking）**：任务提交后，主程序继续执行后续代码，通过回调或轮询获取结果。
#
# ---
#
# #### **2. 阻塞模式（同步执行）**
# ##### **特点**：
# - **顺序执行**：任务逐个处理，主程序等待当前任务完成后再提交下一个。
# - **资源利用率低**：任务队列空闲时，进程/线程可能闲置。
# - **代码简单**：逻辑直观，适合简单任务流。
#
# ##### **代码示例（进程池阻塞）**：
# ```python
# from multiprocessing import Pool
#
# def task(n):
#     return n * n
#
# if __name__ == '__main__':
#     with Pool(4) as pool:  # 创建4个进程的进程池
#         results = []
#         for i in range(10):
#             # 使用 apply 方法（阻塞模式）
#             res = pool.apply(task, (i,))  # 主程序在此等待任务完成
#             results.append(res)
#         print(results)  # 所有任务完成后输出结果
# ```
#
# ##### **适用场景**：
# - 任务之间有强依赖，需按顺序执行。
# - 需要严格控制任务执行时序。
#
# ---
#
# #### **3. 非阻塞模式（异步执行）**
# ##### **特点**：
# - **并行执行**：任务提交后立即返回，主程序继续执行。
# - **资源利用率高**：进程/线程始终处理任务队列，减少空闲。
# - **需结果管理**：通过回调函数或 `get()` 方法获取结果。
#
# ##### **代码示例（线程池非阻塞）**：
# ```python
# from concurrent.futures import ThreadPoolExecutor
# import time
#
# def io_task(n):
#     time.sleep(1)  # 模拟I/O操作
#     return f"Task {n} completed"
#
# if __name__ == '__main__':
#     with ThreadPoolExecutor(max_workers=4) as executor:  # 创建4个线程的线程池
#         futures = []
#         for i in range(10):
#             # 使用 submit 方法（非阻塞模式）
#             future = executor.submit(io_task, i)  # 立即返回Future对象
#             futures.append(future)
#
#         # 主程序可在此执行其他操作
#         print("主程序继续运行...")
#
#         # 获取结果（此时可能阻塞）
#         results = [future.result() for future in futures]
#         print(results)
# ```
#
# ##### **关键方法**：
# - **`submit()`**：提交任务，返回 `Future` 对象。
# - **`Future.result()`**：获取任务结果（若未完成则阻塞）。
# - **回调函数**：任务完成后自动触发。
#
# ##### **适用场景**：
# - 高并发I/O操作（如Web服务器处理请求）。
# - 任务独立无依赖，可并行处理。
#
# ---
#
# #### **4. 阻塞与非阻塞对比**
# | **特性**         | **阻塞模式**                        | **非阻塞模式**                      |
# |------------------|-----------------------------------|-----------------------------------|
# | **执行方式**      | 同步（顺序执行）                    | 异步（并行执行）                    |
# | **资源利用率**    | 低（存在空闲等待）                  | 高（持续处理任务）                  |
# | **代码复杂度**    | 简单                              | 较高（需管理Future或回调）          |
# | **结果获取**      | 立即获得                          | 延迟获取（需显式调用`result()`）    |
# | **适用场景**      | 任务少、依赖性强                    | 任务多、独立性强                    |
#
# ---
#
# #### **5. 实战技巧**
# ##### **混合使用阻塞与非阻塞**：
# ```python
# from concurrent.futures import as_completed
#
# with ThreadPoolExecutor(max_workers=4) as executor:
#     futures = {executor.submit(io_task, i): i for i in range(10)}
#
#     # 非阻塞处理已完成的任务
#     for future in as_completed(futures):
#         task_id = futures[future]
#         result = future.result()
#         print(f"任务 {task_id} 结果: {result}")
# ```
#
# ##### **回调函数处理结果**：
# ```python
# def callback(future):
#     print(f"回调结果: {future.result()}")
#
# future = executor.submit(io_task, 5)
# future.add_done_callback(callback)  # 任务完成后自动触发回调
# ```
#
# ---
#
# #### **6. 性能优化建议**
# 1. **合理设置池大小**：
#    - **CPU密集型**：进程数 ≤ CPU核心数。
#    - **I/O密集型**：线程数可适当增加（如 2-4倍CPU核心数）。
# 2. **避免全局锁（GIL）**：CPU密集型任务优先使用进程池。
# 3. **任务分块**：将大任务拆分为多个子任务，充分利用并发。
#
# ---
#
# ### **总结**
# - **阻塞模式**：简单直接，适合小规模同步任务。
# - **非阻塞模式**：高效灵活，适合高并发异步场景。
# - **核心原则**：根据任务类型（CPU/I/O）和依赖关系选择执行模式，平衡性能与代码复杂度。
# 死锁
# import time
# import threading
#
# mutexA = threading.Lock()
# mutexB = threading.Lock()
#
#
# class Mythread1(threading.Thread):
#     def run(self):
#         if mutexA.acquire():
#             print(self.name, '执行')
#             time.sleep(1)
#             if mutexB.acquire():
#                 print(self.name, '执行')
#                 mutexB.release()
#             mutexA.release()
#
#
# class Mythread2(threading.Thread):
#     def run(self):
#         if mutexB.acquire():
#             print(self.name, '执行')
#             time.sleep(1)
#             if mutexA.acquire():
#                 print(self.name, '执行')
#                 mutexA.release()
#             mutexB.release()
#
#
# if __name__ == '__main__':
#     t1 = Mythread1()
#     t2 = Mythread2()
#     t1.start()
#     t2.start()
# 线程同步
# import time
# import threading
#
# lock1 = threading.Lock()
# lock2 = threading.Lock()
# lock3 = threading.Lock()
# lock2.acquire()
# lock3.acquire()
#
#
# class Task1(threading.Thread):
#     def run(self):
#         while True:
#             if lock1.acquire():
#                 print(".....task1....")
#                 time.sleep(1)
#                 lock2.release()
#
#
# class Task2(threading.Thread):
#     def run(self):
#         while True:
#             if lock2.acquire():
#                 print(".....task2....")
#                 time.sleep(1)
#                 lock3.release()
#
#
# class Task3(threading.Thread):
#     def run(self):
#         while True:
#             if lock3.acquire():
#                 print(".....task3....")
#                 time.sleep(1)
#                 lock1.release()
#
#
# if __name__ == '__main__':
#     t1 = Task1()
#     t2 = Task2()
#     t3 = Task3()
#     t1.start()
#     t2.start()
#     t3.start()
# 生产者消费者
# import time
# import threading
# from queue import Queue
# class Producer(threading.Thread):
#     def run(self):
#         global queue
#         count=0
#         while True:
#             if queue.qsize()<1000:
#                 for i in range(100):
#                     count+=1
#                     msg='生成产品'+str(count)
#                     queue.put(msg)
#                     print(msg)
#                 time.sleep(0.5)
# class Consumer(threading.Thread):
#     def run(self):
#         global queue
#         while True:
#             if queue.qsize()>100:
#                 for i in range(3):
#                     msg=self.name+'消费了'+queue.get()
#                     print(msg)
#             time.sleep(1)
# if __name__=='__main__':
#     queue=Queue()
#     p=Producer()
#     p.start()
#     time.sleep(1)
#     c=Consumer()
#     c.start()
# TFTP(trivial File Transfer Protocol)是简单文件传输协议，使用这个协议就可以实现简单文件的下载，tftp主要特点:
# 1、简单
# 2、占用资源少
# 3、适合传输小文件
# 4、适合在局域网内传递
# 端口号:69
# 基于UDP实现
# 1、TFTP协议的工作原理
# 搜索:当服务器找到现在需要的文件后，会立刻打开文件，把文件中的数据通过TFTP协议发送给客户端
# 分段：如果文件的大小比较大，那么就会把文件分成多个数据包进行传输512B
# 添加序号：因为发送的次数有可能很多，为了让客户端对接收的数据进行排序，所以在服务器发送那512字节数据的时候，会多发2个字节的数据，用来存放序号，并且放在512字节数据的前面，序号从1开始
# 添加操作吗：因为需要从服务器上下载数据时，文件可能不存在，那么此时服务器会的发送一个错误的信息过来，为了区分服务发送的是文件内容还是错误的提示信息，所以又用了2个字节
# 来表示这个数据包的功能（称为操作码），并且在序号前面
# 1 读请求，即下载
# 2 写请求，即上传
# 3 表示数据包，即DATA
# 4 确认码，即ACK
# 5 错误
# 发送确认码（ACK）
# 发送完毕
# 为了标记数据已经发送完毕，所以规定，当客户端接受的数据小于516（2字节操作码+2个字节的序号+512字节数据）时，就意味着服务器已经发送完毕了（如果恰好最后一次数
# 据长度为516，会再发一个长度为0的数据包）。
# 在 Socket 编程中，**TCP（传输控制协议）**和**UDP（用户数据报协议）**是两种最常用的传输层协议，它们的核心区别体现在**连接性、可靠性、数据传输方式**等方面。以下是两者的详细对比及对应的编程实现差异：
#
# ---
#
# ### **1. 核心特性对比**
# | **特性**               | **TCP**                            | **UDP**                            |
# |------------------------|-----------------------------------|-----------------------------------|
# | **连接性**             | 面向连接（需三次握手建立连接）        | 无连接（直接发送数据报）            |
# | **可靠性**             | 可靠传输（数据确认、重传、顺序保证）  | 不可靠传输（不保证到达、顺序或完整性）|
# | **传输方式**           | 流式传输（数据无明确边界）            | 数据报传输（每个包独立且有明确边界）  |
# | **速度**               | 较慢（因保证可靠性引入额外开销）      | 较快（无连接和确认机制）            |
# | **适用场景**           | 文件传输、Web 请求、邮件等需可靠传输的场景 | 实时音视频、在线游戏、DNS查询等实时性要求高的场景 |
#
# ---
#
# ### **2. 编程实现差异**
# #### **(1) Socket 创建**
# - **TCP**：使用 `SOCK_STREAM` 类型，需明确建立连接。
#   ```python
#   import socket
#   # 创建 TCP Socket
#   tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#   ```
#
# - **UDP**：使用 `SOCK_DGRAM` 类型，无需建立连接。
#   ```python
#   # 创建 UDP Socket
#   udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#   ```
#
# ---
#
# #### **(2) 服务端实现**
# - **TCP 服务端**：需监听连接并逐个处理客户端请求。
#   ```python
#   # TCP 服务端
#   tcp_socket.bind(('0.0.0.0', 8888))
#   tcp_socket.listen(5)  # 开始监听，设置最大等待连接数
#
#   while True:
#       client_socket, addr = tcp_socket.accept()  # 接受客户端连接
#       data = client_socket.recv(1024)            # 接收数据
#       client_socket.send(b'ACK')                 # 发送响应
#       client_socket.close()                      # 关闭连接
#   ```
#
# - **UDP 服务端**：直接接收数据报，无需维护连接状态。
#   ```python
#   # UDP 服务端
#   udp_socket.bind(('0.0.0.0', 8888))
#
#   while True:
#       data, addr = udp_socket.recvfrom(1024)  # 接收数据及客户端地址
#       udp_socket.sendto(b'ACK', addr)         # 向该地址发送响应
#   ```
#
# ---
#
# #### **(3) 客户端实现**
# - **TCP 客户端**：需显式连接服务端。
#   ```python
#   # TCP 客户端
#   tcp_socket.connect(('127.0.0.1', 8888))  # 连接服务端
#   tcp_socket.send(b'Hello TCP')
#   response = tcp_socket.recv(1024)
#   tcp_socket.close()
#   ```
#
# - **UDP 客户端**：直接发送数据报，无需连接。
#   ```python
#   # UDP 客户端
#   udp_socket.sendto(b'Hello UDP', ('127.0.0.1', 8888))  # 发送数据报
#   response, addr = udp_socket.recvfrom(1024)            # 接收响应
#   ```
#
# ---
#
# #### **(4) 数据传输差异**
# - **TCP 数据边界**：流式传输可能导致“粘包”（多条消息被合并接收）。
#   - 解决粘包：需自定义协议（如消息头声明数据长度）。
#   ```python
#   # TCP 发送端：添加数据长度头
#   data = b'Hello World'
#   header = len(data).to_bytes(4, byteorder='big')  # 4字节长度头
#   tcp_socket.send(header + data)
#
#   # TCP 接收端：解析长度头
#   header = tcp_socket.recv(4)
#   data_length = int.from_bytes(header, byteorder='big')
#   data = tcp_socket.recv(data_length)
#   ```
#
# - **UDP 数据边界**：每个 `sendto()` 对应一个独立数据报，接收端通过 `recvfrom()` 获取完整报文，无粘包问题。
#
# ---
#
# ### **3. 关键注意事项**
# - **TCP 连接管理**：需处理连接中断（如客户端异常断开），需使用 `try-except` 捕获异常。
#   ```python
#   try:
#       data = client_socket.recv(1024)
#   except ConnectionResetError:
#       print("客户端强制关闭连接")
#   ```
#
# - **UDP 丢包与重传**：需在应用层实现超时重传机制。
#   ```python
#   import time
#   udp_socket.settimeout(2.0)  # 设置超时时间
#   try:
#       response, addr = udp_socket.recvfrom(1024)
#   except socket.timeout:
#       print("响应超时，尝试重传...")
#   ```
#
# ---
#
# ### **4. 性能优化建议**
# - **TCP**：调整缓冲区大小、启用 Nagle 算法（减少小包）或禁用（实时性场景）。
#   ```python
#   tcp_socket.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)  # 禁用 Nagle
#   ```
#
# - **UDP**：使用多线程/协程处理高并发请求，避免主线程阻塞。
#   ```python
#   from threading import Thread
#
#   def handle_udp_request(data, addr):
#       udp_socket.sendto(b'ACK', addr)
#
#   while True:
#       data, addr = udp_socket.recvfrom(1024)
#       Thread(target=handle_udp_request, args=(data, addr)).start()
#   ```
#
# ---
#
# ### **总结**
# - **TCP**：适用于需可靠传输的场景，编程需处理连接、粘包和错误恢复。
# - **UDP**：适用于实时性优先的场景，编程更简单，但需自行处理丢包和乱序。
# - **选择依据**：根据应用的可靠性、延迟容忍度和数据传输特性选择协议。
# ### 协程与守护线程的理解及实现
#
# 在并发编程中，协程（Coroutine）和守护线程（Daemon Thread）是两种不同的机制，它们的核心目标都是实现任务的异步执行和资源的高效管理。但它们的实现方式和应用场景存在显著差异。以下从概念、实现到代码示例的详细解析：
#
# ---
#
# #### **1. 守护线程（Daemon Thread）的核心逻辑**
# - **定义**：守护线程是后台线程，其生命周期依赖于主线程。当主线程结束时，所有守护线程会立即终止（无论任务是否完成）。
# - **适用场景**：日志写入、心跳检测等无需等待的后台任务。
# - **Python 示例**：
#   ```python
#   import threading
#   import time
#
#   def daemon_task():
#       while True:
#           print("守护线程运行中...")
#           time.sleep(1)
#
#   daemon_thread = threading.Thread(target=daemon_task)
#   daemon_thread.daemon = True  # 设置为守护线程
#   daemon_thread.start()
#
#   time.sleep(3)
#   print("主线程退出，守护线程自动终止")
#   ```
#   **输出**：
#   ```
#   守护线程运行中...
#   守护线程运行中...
#   守护线程运行中...
#   主线程退出，守护线程自动终止
#   ```
#
# ---
#
# #### **2. 协程（Coroutine）的异步特性**
# - **定义**：协程是单线程内的并发任务，通过事件循环（Event Loop）调度，在遇到 I/O 阻塞时自动切换任务。
# - **适用场景**：高并发 I/O 操作（如网络请求、文件读写）。
# - **Python 示例（`asyncio`）**：
#   ```python
#   import asyncio
#
#   async def coroutine_task():
#       while True:
#           print("协程运行中...")
#           await asyncio.sleep(1)
#
#   async def main():
#       task = asyncio.create_task(coroutine_task())
#       await asyncio.sleep(3)
#       print("主协程退出，后台协程需手动取消")
#
#   asyncio.run(main())
#   ```
#   **输出**：
#   ```
#   协程运行中...
#   协程运行中...
#   协程运行中...
#   主协程退出，后台协程需手动取消
#   ```
#   &gt; **注意**：协程默认不会自动终止，需显式取消任务。
#
# ---
#
# #### **3. 协程的“守护”行为实现**
# 协程本身没有“守护”属性，但可通过以下方式模拟类似守护线程的行为：
#
# ##### **(1) 显式取消后台任务**
# 在退出主协程前，手动取消所有后台协程任务。
# ```python
# async def main():
#     task = asyncio.create_task(coroutine_task())
#     await asyncio.sleep(3)
#     task.cancel()  # 显式取消任务
#     try:
#         await task
#     except asyncio.CancelledError:
#         print("后台协程已取消")
#     print("主协程退出")
#
# asyncio.run(main())
# ```
# **输出**：
# ```
# 协程运行中...
# 协程运行中...
# 协程运行中...
# 后台协程已取消
# 主协程退出
# ```
#
# ##### **(2) 使用 `asyncio.shield()` 控制取消范围**
# 保护某些协程不被取消：
# ```python
# async def critical_task():
#     print("关键任务开始")
#     await asyncio.sleep(2)
#     print("关键任务完成")
#
# async def main():
#     shielded = asyncio.shield(critical_task())
#     normal_task = asyncio.create_task(coroutine_task())
#     await asyncio.sleep(1)
#     normal_task.cancel()  # 取消普通任务，但 shielded 任务继续执行
#     await asyncio.sleep(3)  # 等待 shielded 任务完成
#
# asyncio.run(main())
# ```
# **输出**：
# ```
# 关键任务开始
# 协程运行中...
# 关键任务完成
# ```
#
# ---
#
# #### **4. 协程与守护线程的对比**
# | **特性**            | **协程**                          | **守护线程**                      |
# |---------------------|----------------------------------|----------------------------------|
# | **并发模型**         | 单线程内异步（事件循环）            | 多线程并行（操作系统调度）          |
# | **资源占用**         | 极低（无线程切换开销）              | 较高（每个线程占用独立内存）        |
# | **任务取消**         | 需显式取消或通过事件循环控制          | 主线程退出时自动终止                |
# | **适用场景**         | I/O 密集型高并发（如 Web 服务器）   | 后台任务（如日志、监控）            |
# | **典型框架**         | `asyncio`、`Tornado`、`FastAPI`   | `threading`、`concurrent.futures` |
#
# ---
#
# #### **5. 协程守护模式的最佳实践**
# 1. **统一管理后台任务**：
#    ```python
#    async def main():
#        tasks = [asyncio.create_task(coroutine_task()) for _ in range(3)]
#        await asyncio.sleep(2)
#        for task in tasks:
#            task.cancel()
#        await asyncio.gather(*tasks, return_exceptions=True)
#    ```
#
# 2. **异常处理与资源释放**：
#    ```python
#    async def safe_task():
#        try:
#            while True:
#                await asyncio.sleep(1)
#        except asyncio.CancelledError:
#            print("清理资源...")
#            raise
#
#    async def main():
#        task = asyncio.create_task(safe_task())
#        await asyncio.sleep(2)
#        task.cancel()
#        await task  # 确保异常被处理
#    ```
#
# 3. **结合线程池处理阻塞操作**：
#    ```python
#    async def hybrid_task():
#        loop = asyncio.get_event_loop()
#        # 将阻塞函数放到线程池中执行
#        await loop.run_in_executor(None, time.sleep, 2)
#        print("混合任务完成")
#    ```
#
# ---
#
# ### **总结**
# - **协程无内置“守护”机制**：需通过任务取消或事件循环管理生命周期。
# - **灵活性与控制权**：协程的显式取消机制提供了更精细的控制，但需要开发者手动管理。
# - **设计原则**：根据任务类型（I/O 或 CPU 密集型）选择协程或线程，混合使用时可结合线程池和守护线程优化性能。
#
# 通过合理设计，协程可以模拟类似守护线程的行为，同时保持轻量级和高并发的优势。
#导入模块
# from tkinter import *
# from tkinter import messagebox
# #创建窗口对象
# root=Tk()
# #设置窗口的标题
# root.title("tkinter 的第一个程序")
# #设置窗口的大小
# #宽度 500，高度 400；距屏幕左边 100，距屏幕上边 200
# root.geometry("500x400+100+200")
# #创建组件
# button=Button(root)
# button['text']='点我有惊喜'
# button.pack()
# #定义事件函数
# def songhua(e):
#
#     messagebox.showerror('Message','送给你一朵玫瑰花')
#     print('送给你一朵玫瑰花')
# #给控件绑定事件
# button.bind('<Button-1>',songhua)
# #调用组件的 mainloop 方法，进入事件循环
# root.mainloop()
# 协程实现生产者消费者
# import time
#
#
# # 生产者
# def produce(c):
#     for i in range(1, 6):
#         print('生产者生产%d 产品' % i)
#         c.send(str(i))
#         time.sleep(1)
#
#
# # 消费者
# def customer():
#     res = ''
#     while True:
#         data = yield res
#         if not data:
#             return
#         print('消费者消费%s 产品' % data)
#
#
# if __name__ == '__main__':
#     c = customer()
#     c.send(None)  # Prime the coroutine
#     produce(c)
# import numpy as np
# x=np.linspace(1,9,10)
# print(x)
# import numpy as np
# x=np.logspace(0,9,9,base=2)
# print(x)
# 在Python中，切片操作用于从序列（如列表、元组、字符串）中提取子序列。其基本语法为 `sequence[start:end:step]`，其中参数含义如下：
#
# ---
#
# ### **1. 参数说明**
# - **`start`**：起始索引（包含），默认为序列的起始位置。
# - **`end`**：结束索引（不包含），默认为序列的结束位置。
# - **`step`**：步长（每隔多少个元素取一个），默认为1。
#
# ---
#
# ### **2. `::` 的作用**
# 双冒号 `::` 用于指定步长（`step`）：
# - **示例**：`sequence[::2]` 表示从头到尾，每隔一个元素取一个。
# - **默认值**：当 `start` 或 `end` 省略时，其值由 `step` 的正负决定：
#   - 若 `step &gt; 0`：`start` 默认为0，`end` 默认为序列长度。
#   - 若 `step &lt; 0`：`start` 默认为最后一个元素索引，`end` 默认为-1（即第一个元素前的位置）。
#
# ---
#
# ### **3. 常见用法**
# #### **（1）基本切片**
# ```python
# a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#
# # 取索引2到5（不包含5）
# print(a[2:5])       # 输出: [2, 3, 4]
#
# # 从头开始，每隔2个元素取一个
# print(a[::2])       # 输出: [0, 2, 4, 6, 8]
#
# # 反转整个序列
# print(a[::-1])      # 输出: [9, 8, 7, ..., 0]
# ```
#
# #### **（2）负数步长**
# ```python
# # 从索引5到2（不包含2），反向步长-1
# print(a[5:2:-1])    # 输出: [5, 4, 3]
#
# # 从倒数第三个元素到末尾
# print(a[-3::])      # 输出: [7, 8, 9]
#
# # 从末尾开始，每隔2个元素取一个
# print(a[::-2])      # 输出: [9, 7, 5, 3, 1]
# ```
#
# ---
#
# ### **4. 特殊情况**
# - **超出索引范围**：自动截断到有效范围。
#   ```python
#   a = [0, 1, 2, 3]
#   print(a[2:10])    # 输出: [2, 3]
#   ```
#
# - **空切片**：当 `start` 和 `end` 不符合步长方向时返回空列表。
#   ```python
#   print(a[2:5:-1])   # 输出: []
#   ```
#
# ---
#
# ### **5. 括号问题**
# - **方括号 `[]`**：切片操作必须使用方括号，如 `a[1:3]`。
# - **圆括号 `()`**：用于函数调用或元组，不可用于切片。
#
# ---
#
# ### **总结**
# - `start:end:step` 中的参数均可省略，默认值由 `step` 的正负决定。
# - 双冒号 `::` 用于指定步长，负数步长表示反向切片。
# - 切片操作必须使用方括号 `[]`，圆括号 `()` 无效。
#
# 通过理解参数的默认行为和步长方向的影响，可以灵活运用切片处理序列数据。
# import numpy as np
#
# x = np.arange(1, 13)
# a = x.reshape(4, 3)
# print('数组元素')
# print(a)
# #使用索引获取
# print('所有行的第二列')
# print(a[:, 1])
# print('奇数行的第一列')
# print(a[::2, 0])
# 这段代码演示了如何利用 **NumPy数组切片** 来提取特定行和列的数据。以下是对代码的逐行解释：
#
# ---
#
# ### **1. 创建二维数组**
# ```python
# import numpy as np
# x = np.arange(1, 13)         # 创建一维数组 [1, 2, 3, ..., 12]
# a = x.reshape(4, 3)          # 重塑为 4行3列 的二维数组
# print('数组元素')
# print(a)
# ```
# 输出结果为：
# ```
# [[ 1  2  3]
#  [ 4  5  6]
#  [ 7  8  9]
#  [10 11 12]]
# ```
#
# ---
#
# ### **2. 切片语法 `a[行操作, 列操作]`**
# 在 NumPy 中，二维数组的切片语法为 `a[row_slice, col_slice]`，其中：
# - **`row_slice`**：行的切片规则（如 `:` 表示所有行，`::2` 表示步长为2）。
# - **`col_slice`**：列的切片规则（如 `1` 表示第二列，`0` 表示第一列）。
#
# ---
#
# ### **3. 提取所有行的第二列**
# ```python
# print('所有行的第二列')
# print(a[:, 1])  # 输出: [2, 5, 8, 11]
# ```
# - **`[:, 1]`** 分解：
#   - `:` 表示选择所有行。
#   - `1` 表示选择第二列（索引从0开始）。
# - 结果：每一行的第二列元素组成的一维数组。
#
# ---
#
# ### **4. 提取奇数行的第一列**
# ```python
# print('奇数行的第一列')
# print(a[::2, 0])  # 输出: [1, 7]
# ```
# - **`[::2, 0]`** 分解：
#   - `::2` 表示从第0行开始，每隔一行取一次（步长为2），即选择索引为0、2的行（第一行和第三行）。
#   - `0` 表示选择第一列。
# - 结果：奇数行（第1行、第3行）的第一列元素组成的一维数组。
#
# ---
#
# ### **5. 关键概念**
# 1. **索引从0开始**：
#    - 第一列的索引是 `0`，第二列是 `1`，以此类推。
#    - 第一行的索引是 `0`，第二行是 `1`，以此类推。
#
# 2. **步长 `step` 的作用**：
#    - `::2` 中的 `2` 表示每隔一个元素取一次。
#    - 步长为正数时，从前往后取；为负数时，从后往前取。
#
# 3. **多维切片组合**：
#    - 行和列的切片规则用逗号分隔（如 `[行规则, 列规则]`）。
#    - 规则可以混合使用（如 `::2` 选行，`0` 选列）。
#
# ---
#
# ### **6. 扩展示例**
# ```python
# # 获取偶数行的最后一列
# print(a[1::2, -1])  # 输出: [6, 12]（索引1、3行的最后一列）
#
# # 反向所有行，取所有列
# print(a[::-1, :])   # 输出: 行逆序后的数组
# ```
#
# ---
#
# 通过灵活组合行和列的切片规则，可以高效提取多维数组中的任意子集。重点掌握索引规则、步长方向和多维切片的组合使用！
# 在 **NumPy 多维数组切片**中，**逗号 `,`** 用于分隔**不同维度**的切片参数。每个维度可以独立指定切片规则，语法为：
#
# ```python
# array[dim1_slice, dim2_slice, dim3_slice, ...]
# ```
#
# ---
#
# ### **1. 二维数组示例**
# 以二维数组为例，逗号后的参数表示对**列的操作**：
# ```python
# import numpy as np
# a = np.array([[1, 2, 3],
#               [4, 5, 6],
#               [7, 8, 9]])
#
# # 逗号前的参数操作行，逗号后的参数操作列
# print(a[:, 1])       # 所有行的第二列 → [2, 5, 8]
# print(a[::2, 0])     # 奇数行的第一列 → [1, 7]
# print(a[1:3, 1:3])   # 第2-3行，第2-3列 → [[5,6], [8,9]]
# ```
#
# ---
#
# ### **2. 参数规则**
# #### **(1) 单值索引**
# - 直接选取指定索引位置的元素（维度会减少）：
#   ```python
#   print(a[1, 2])     # 取第2行第3列 → 6
#   ```
#
# #### **(2) 切片语法 `start:end:step`**
# - 控制行或列的选取范围：
#   ```python
#   print(a[0:2, ::-1])  # 第1-2行，列反向 → [[3,2,1], [6,5,4]]
#   ```
#
# #### **(3) 布尔掩码或整数数组**
# - 高级索引（筛选特定元素）：
#   ```python
#   mask = np.array([True, False, True])
#   print(a[mask, :])    # 筛选第1、3行 → [[1,2,3], [7,8,9]]
#   ```
#
# ---
#
# ### **3. 三维数组示例**
# 逗号后的参数依次控制更高维度：
# ```python
# b = np.arange(24).reshape(2, 3, 4)  # 2层3行4列
# # 结构：
# # [
# #   [[ 0, 1, 2, 3], [4, 5, 6, 7], [8, 9,10,11]],
# #   [[12,13,14,15], [16,17,18,19], [20,21,22,23]]
# # ]
#
# # 逗号分隔三个维度：层、行、列
# print(b[0, :, 1])     # 第1层，所有行，第2列 → [1, 5, 9]
# print(b[:, 1::2, ::3])# 所有层，第2行开始步长2，列步长3 → [[[4,7]], [[16,19]]]
# ```
#
# ---
#
# ### **4. 省略参数时的默认行为**
# - 如果省略某个维度的参数，默认取该维度全部元素：
#   ```python
#   print(a[1])        # 等效于 a[1, :] → 第2行所有列 → [4,5,6]
#   print(a[:, 2])     # 所有行的第3列 → [3,6,9]
#   ```
#
# ---
#
# ### **5. 关键总结**
# - **逗号 `,`** 分隔不同维度，依次对应：`行 → 列 → 更高维度`。
# - 每个维度可单独使用**索引值**、**切片语法**或**高级索引**。
# - 参数省略时，默认取该维度全部元素（即 `:` 的简写）。
#
# 通过灵活组合逗号后的参数，可以精准控制多维数组的切片逻辑！
# Python中的切片操作 `sequence[start:stop:step]` 生成的索引序列可以理解为一种**等差数列**，但其终止条件和索引范围需要根据 `step` 的正负动态调整，并非简单的 `[start, stop-1)`。以下是详细分析：
#
# ---
#
# ### **1. 切片生成的索引序列**
# 切片的索引生成规则为：
# - **起始索引**：`start`（默认为 `0` 或 `len(sequence)-1`，取决于 `step` 正负）。
# - **终止条件**：当索引超过 `stop`（`step &gt; 0` 时）或低于 `stop`（`step &lt; 0` 时）时停止。
# - **步长**：`step` 控制索引增减的步幅。
#
# **数学表达式**：
# 生成的索引序列为：
# \[
# \text{indices} = \left[ \text{start}, \ \text{start} + \text{step}, \ \text{start} + 2\cdot\text{step}, \ \dots \ \right]
# \]
# 直到索引不符合终止条件。
#
# ---
#
# ### **2. 不同 `step` 的行为**
# #### **(1) 当 `step &gt; 0`（正向步长）**
# - **终止条件**：索引 &lt; `stop`。
# - **示例**：
#   ```python
#   a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#   print(a[2:7:2])  # 输出: [2, 4, 6]
#   ```
#   - 索引序列：`2 → 4 → 6`（下一步是 `8`，超过 `stop=7`，停止）。
#
# #### **(2) 当 `step &lt; 0`（反向步长）**
# - **终止条件**：索引 &gt; `stop`。
# - **示例**：
#   ```python
#   print(a[7:2:-2])  # 输出: [7, 5, 3]
#   ```
#   - 索引序列：`7 → 5 → 3`（下一步是 `1`，小于 `stop=2`，停止）。
#
# ---
#
# ### **3. 关键结论**
# 1. **等差数列的逻辑**：
#    切片生成的索引序列确实是等差数列，但**终止条件由 `step` 的方向决定**：
#    - `step &gt; 0`：索引严格小于 `stop`。
#    - `step &lt; 0`：索引严格大于 `stop`。
#
# 2. **为什么不是 `stop-1`？**
#    - `stop` 是切片的上限（不包含），但具体终止位置取决于 `step` 的步幅。
#    - 示例：`a[1:9:3]` 的索引序列是 `1 → 4 → 7`（下一步 `10` &gt;= `stop=9`，停止）。
#
# 3. **空切片的产生条件**：
#    - 当 `step` 方向与 `start`/`stop` 范围矛盾时，返回空列表。
#      例如：`a[2:5:-1]` 或 `a[5:2:1]`。
#
# ---
#
# ### **4. 验证示例**
# #### **示例 1：`step &gt; 0`**
# ```python
# a = [0, 1, 2, 3, 4, 5]
# print(a[1:5:2])  # 输出: [1, 3]
# ```
# - 索引序列：`1 → 3`（下一步 `5` &gt;= `stop=5`，停止）。
#
# #### **示例 2：`step &lt; 0`**
# ```python
# print(a[5:1:-1])  # 输出: [5, 4, 3, 2]
# ```
# - 索引序列：`5 → 4 → 3 → 2`（下一步 `1` &lt;= `stop=1`，停止）。
#
# ---
#
# ### **5. 总结**
# Python切片的索引生成规则是**基于等差数列的数学逻辑**，但需注意：
# - **终止条件由 `step` 的方向决定**，而非简单的 `stop-1`。
# - 理解 `start`、`stop` 和 `step` 的相互作用，才能精准预测切片结果。
#
# 通过具体示例和数学表达式，可以更清晰地掌握切片行为。
# import matplotlib.pyplot as plt
# import numpy as np
#
# # Draw 10 scatter plots with different sizes and colors
# cnt = 0
# alpha = np.random.rand()  # Generate a single alpha value for all plots
# while cnt < 10:
#     x = np.random.rand(1000)
#     y = np.random.rand(1000)
#     colors = np.random.rand(1000)
#     size = np.random.rand(1000) * 10000  # Ensure size matches x and y length
#     plt.scatter(x, y, c=colors, s=size, alpha=alpha)
#     cnt += 1
# plt.show()
# 这段代码使用Matplotlib和NumPy库生成一个包含10个散点图层的可视化图形。以下是对代码的逐步解释：
#
# 1. **导入库**：
#    ```python
#    import matplotlib.pyplot as plt
#    import numpy as np
#    ```
#    导入Matplotlib用于绘图，NumPy用于生成随机数据。
#
# 2. **初始化计数器和透明度**：
#    ```python
#    cnt = 0
#    alpha = np.random.rand()  # 生成一个0到1之间的随机透明度值
#    ```
#    - `cnt` 控制循环次数。
#    - `alpha` 是单个随机生成的透明度值（0为完全透明，1为不透明），所有散点图层共享此值。
#
# 3. **循环绘制散点图**：
#    ```python
#    while cnt &lt; 10:
#        x = np.random.rand(1000)  # 生成1000个0-1的随机数作为x坐标
#        y = np.random.rand(1000)  # 生成1000个0-1的随机数作为y坐标
#        colors = np.random.rand(1000)  # 生成1000个随机颜色值（0-1）
#        size = np.random.rand(1000) * 10000  # 生成1000个随机点大小（0-10000）
#        plt.scatter(x, y, c=colors, s=size, alpha=alpha)  # 绘制散点图
#        cnt += 1
#    ```
#    - **每次循环生成新数据**：
#      - `x` 和 `y`：各生成1000个0到1之间的随机数，确定点的位置。
#      - `colors`：1000个随机值，通过默认颜色映射（如viridis）映射为不同颜色。
#      - `size`：每个点的大小在0到10000之间随机生成，面积越大点越大。
#    - **叠加图层**：每次调用 `plt.scatter()` 会将新散点图叠加到当前坐标轴，共叠加10次。
#
# 4. **显示图形**：
#    ```python
#    plt.show()
#    ```
#    最终显示叠加了10个散点图层的图像。
#
# ---
#
# **效果分析**：
# - **点的位置**：所有点随机分布在0到1的区域内，因多次叠加显得密集。
# - **颜色**：每个点的颜色由随机值映射到颜色映射，不同图层的颜色混合。
# - **大小**：部分点可能因过大的尺寸（如接近10000）覆盖较大区域，导致重叠区域颜色混合明显。
# - **透明度**：所有图层共享相同透明度，叠加后颜色更饱和，可能形成斑驳效果。
#
# **潜在问题**：
# - **点尺寸过大**：`size` 乘以10000可能导致点远大于坐标范围（0-1），视觉效果可能被大点主导。
# - **性能影响**：绘制10000个点（10层×1000点）可能影响渲染速度，尤其在低配置设备上。
#
# **改进建议**：
# - 调整 `size` 的缩放因子（如改为 `*100`）以优化点的大小。
# - 使用 `plt.figure()` 或子图（`plt.subplots()`）分离不同图层，避免过度叠加。
# - 为每个图层生成独立 `alpha` 值以增加多样性。
#
# 通过这段代码，可以观察到随机数据在多层叠加后的复杂视觉效果，适合探索数据分布或艺术化呈现。
# # 不使用循环填充列平均值的Pandas方法
# 
# **解决方案：** 使用`df.fillna(df.mean())`即可一步完成列平均值填充
# 
# **实现原理：**
# 1. `df.mean()` 会自动计算每列的算术平均值
# 2. `fillna()` 方法会将计算出的列平均值自动对齐到对应列的缺失位置
# 
# **代码示例：**
# ```python
# import pandas as pd
# #
# # # 创建示例数据
# df = pd.DataFrame({
#     'A': [1, 2, None, 4],
#     'B': [None, 5, 6, None],
#     'C': [7, 8, 9, 10]
# })
#
# # 用列均值填充缺失值
# df_filled = df.fillna(df.mean())
# print(df_filled)
# ```
# 
# **输出结果：**
# ```
#      A    B   C
# 0  1.0  5.5   7
# 1  2.0  5.0   8
# 2  2.333...  6.0   9  # A列均值(1+2+4)/3≈2.333
# 3  4.0  5.5  10       # B列均值(5+6)/2=5.5
# ```
# 
# **优势：**
# - 无需显式循环：向量化操作效率更高
# - 自动对齐列名：保证每列使用正确的平均值
# - 支持灵活扩展：可通过`df.mean(axis=1)`实现行方向填充（需注意数据合理性）
# ```
# ### `np.linalg` 模块核心解析
#
# ---
#
# #### 1. **核心功能分类**
# **线性方程与矩阵运算**
# | 函数/方法              | 功能描述                          | 数学表达式                |
# |------------------------|-----------------------------------|---------------------------|
# | `solve(A, b)`          | 解线性方程组 `Ax = b`            | `x = A⁻¹b` (直接求解)     |
# | `inv(A)`               | 计算方阵的逆矩阵                  | `A⁻¹`                     |
# | `det(A)`               | 计算方阵的行列式                  | `det(A)`                  |
# | `matrix_rank(A)`       | 计算矩阵秩                        | `rank(A)`                 |
#
# **矩阵分解**
# | 函数/方法              | 应用场景                          |
# |------------------------|-----------------------------------|
# | `cholesky(A)`          | 正定矩阵分解，用于优化和概率计算  |
# | `qr(A)`                | 正交三角分解，最小二乘问题        |
# | `svd(A)`               | 奇异值分解，降维/推荐系统         |
# | `eig(A)`               | 特征值分解，动态系统分析          |
#
# **范数与误差分析**
# | 函数/方法              | 说明                              |
# |------------------------|-----------------------------------|
# | `norm(A, ord)`         | 计算矩阵/向量的范数（1范数、2范数等） |
# | `cond(A)`              | 计算矩阵的条件数（病态程度）      |
#
# ---
#
# #### 2. **关键应用场景**
# - **机器学习**
#   - 特征降维：`svd` 分解提取主成分
#   - 正则化：`solve` 处理带L2正则的线性回归
# - **物理仿真**
#   - 刚体运动：`eig` 分析惯性张量
#   - 波动方程：`cholesky` 分解加速求解
# - **金融工程**
#   - 协方差矩阵：`inv` 计算投资组合权重
#   - 风险评估：`cond` 检测模型敏感性
#
# ---
#
# #### 3. **实战代码示例**
# **解线性方程组**（优先使用 `solve` 而非直接求逆）
# ```python
# import numpy as np
# A = np.array([[3, 1], [1, 2]])
# b = np.array([9, 8])
# x = np.linalg.solve(A, b)  # 输出：array([2., 3.])
# ```
#
# **奇异值分解（SVD）**
# ```python
# U, S, Vt = np.linalg.svd(A)
# # 重构矩阵（截断奇异值可降维）
# k = 1  # 保留前1个奇异值
# A_approx = U[:, :k] @ np.diag(S[:k]) @ Vt[:k, :]
# ```
#
# ---
#
# #### 4. **致命陷阱与规避方法**
# - **不可逆矩阵**
#   - 现象：调用 `inv` 时触发 `LinAlgError: Singular matrix`
#   - 对策：改用伪逆 `np.linalg.pinv` 或添加正则化项
#
# - **病态矩阵**
#   - 检测：`cond(A)` &gt; 1e12 时数据微小变化会导致解剧烈波动
#   - 方案：数据标准化 + 增加样本量
#
# - **复数运算**
#   - 注意：`eig` 分解可能返回复数，需用 `np.real_if_close` 处理
#
# ---
#
# #### 5. **性能优化指南**
# - **大矩阵处理**
#   - 避免 `inv`：复杂度 O(n³)，改用 `solve` 直接求解（节省内存）
#   - 分块计算：对超大规模矩阵使用 `svd(..., full_matrices=False)`
#
# - **GPU加速**
#   - 结合 `cupy` 库：将NumPy数组转换为CuPy数组后调用 `cupy.linalg`
#
# ---
#
# **总结**：
# `np.linalg` 是 **数值计算的核心武器库**：
# - **优先选择分解而非求逆**（稳定性↑ 误差↓）
# - **掌握 `solve` 和 `svd` 两大神器**可解决90%的工程问题
# - 警惕矩阵病态性，条件数超过 `1e6` 时必须数据预处理
# ### 主对角线开根号的核心意义与应用场景
#
# ---
#
# #### **1. 协方差矩阵标准化**
# - **操作对象**：协方差矩阵的主对角线元素（方差值）
# - **数学表达**：若协方差矩阵为 $\Sigma$，其对角线元素 $\sigma_i^2$ 代表第 $i$ 个变量的方差
# - **开根号意义**：
#   - **得到标准差**：$\sqrt{\sigma_i^2} = \sigma_i$
#   - **标准化数据**：将协方差矩阵转换为相关系数矩阵
#     ```python
#     # 协方差矩阵 → 相关系数矩阵
#     std_dev = np.sqrt(np.diag(cov_matrix))  # 提取标准差
#     corr_matrix = cov_matrix / np.outer(std_dev, std_dev)
#     ```
#
# ---
#
# #### **2. Cholesky分解中的必要性**
# - **分解条件**：仅适用于正定矩阵（所有对角线元素为正）
# - **分解过程**：将矩阵 $A$ 分解为下三角矩阵 $L$，满足 $A = LL^T$
# - **操作逻辑**：
#   - **对角线开根号**：确保分解后的 $L$ 对角线元素为实数
#   - **分解步骤示例**：
#     ```python
#     L = np.linalg.cholesky(A)  # 自动处理对角线开根号
#     ```
#
# ---
#
# #### **3. 数据预处理中的归一化**
# - **应用场景**：机器学习特征缩放
# - **核心目的**：消除量纲差异，加速模型收敛
# - **具体操作**：
#   - **计算标准差**：对数据集每一列（特征）的方差开根号
#   - **标准化公式**：
#     $$
#     X_{\text{标准化}} = \frac{X - \mu}{\sigma}
#     $$
#   - **代码实现**：
#     ```python
#     std = np.sqrt(np.diag(X.T @ X / n_samples))  # 主对角线开根号得标准差
#     X_normalized = (X - mean) / std
#     ```
#
# ---
#
# #### **4. 几何解释**
# - **矩阵空间变换**：主对角线元素控制各坐标轴的缩放比例
# - **开根号作用**：
#   - 若原矩阵表示缩放变换（如放大2倍），开根号后变为放大$\sqrt{2}$倍
#   - 在正交变换中保持变换的稳定性（如旋转矩阵的平方根变换）
#
# ---
#
# **总结**：
# 主对角线开根号的本质是 **标度转换**，核心意义包括：
# 1. **方差→标准差**：量化数据波动幅度
# 2. **矩阵分解基础**：确保分解有效性（如Cholesky分解）
# 3. **特征归一化**：消除量纲影响，提升算法性能
# 4. **空间缩放控制**：调整多维空间中的坐标轴伸缩比例
#
# （注：具体应用需结合场景，如协方差矩阵处理、优化算法等）
