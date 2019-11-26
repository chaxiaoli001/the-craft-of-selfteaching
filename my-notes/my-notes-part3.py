Part.3.A.conquering-difficulties
1.战胜难点
	a.类，以及面向对象编程（Class，OOP）
	b.迭代器、生成器、装饰器（Iterators、Generators、Decorators）
	c.正则表达式（Regular Expressions）
	d.巴科斯-诺尔范式（Backus Normal Form）
1.1
读不懂也要读完，读完之后再读很多遍
不断自己动手归纳总结整理
1.2
知识就是知识，它没有任何义务去具备幽默生动的属性；
手艺就是手艺，它没有任何义务去具备有趣欢乐的属性。
1.3 耐心学习
首先，平静地接受了它枯燥的本质；其次，就是经过多次实践已然明白，无论多枯燥，总能读完；无论多难，多读几遍总能读懂

Part.3.B.1.classes-1
1 类 —— 面向对象编程
1.1 面向对象编程
	a.本节内容，不专属于哪个编程语言（比如 Python、JavaScript 或者 Golang）。
	面向对象编程（Object Oriented Programming, OOP）是一种编程的范式（Paradigm），或者说，是一种方法论（Methodology）
1.2 基本术语
	a.面向对象编程（OOP），是使用对象（Objects）作为核心的编程方式。进而就可以把对象（Objects）的数据和运算过程封装（Encapsulate）在内部，
		而外部仅能根据事先设计好的界面（Interface）与之沟通。
	b.在程序设计过程中，需要对标现实世界创造对象——最直接手段就是 抽象（Abstract）。
	c.从用编程语言创造对象的角度去看，所谓的界面，就由这两样东西构成：
		属性（Attributes） —— 用自然语言描述，通常是名词（Nouns）。 “必要的特征”，叫做对象的属性
		方法（Methods） —— 用自然语言描述，通常是动词（Verbs）。 “必要的行为”，叫做对象的方法。
	d.程序里创建对象，做法常是：
		先创建最抽象的类（Class），然后再创建子类（Subclass）
		它们之间是从属关系是：Class ⊃ Subclass，在 OOP 中，这叫继承（Inheritance）关系，Subclass继承故拥有Class的所有属性
		创建好一个类之后，可以根据它创建它的许多个实例（Instances）。
	e.小结
		对象，封装，抽象
		界面，属性，方法
		继承，类，子类，实例
1.3 对象和类的理解
	你创造了一个类（Class），这时候你是创作者，从你眼里望过去，那就是个类（Class）；
	而后你根据这个类的定义，创建了很多实例（Instances）；
	接下来一旦你开始使用这些实例的时候，你就成了使用者，从使用者角度望过去，手里正在操作的，就是各种对象（Objects）

# Part.3.B.2.classes-2
1 类 —— Python 的实现
1.1 Defining Class
	定义：Class 使用 class 关键字，如"class A："
	注：与函数定义不同的地方在于，Class 接收参数不是在 class Classname(): 的括号里完成；继承新class如："class A_i(A):"
1.2 初始函数、系统默认变量；继承（Inherite）
举例：
import datetime
class Golem:   # Golem:一个被赋予了生命的泥人
    def __init__(self, name=None): #初始化函数“__init__()”名称是强制指定的，Class的代码中，系统会在Instance创建后初始化这个函数
			# self是个变量，区别于程序中其它变量，它是系统默认可以识别的变量，指代将来用这个 Class 创建的 Instance。
        self.name = name # d.self.name 接收了一个参数，'Clay'，并将其保存了下来；
        self.built_year = datetime.date.today().year # e.生成了一个self.built_year 的变量，保存的是g这个 Object 被创建时的年份
    
    def say_hi(self):
        print('Hi!')
class Running_Golem(Golem): # 用Golem Class去Inherite一个新的Subclass，比如Running_Golem，有Golem的Attributes和Methods。
    def run(self):
    	print("Can't you see? I'm running...")
    def say_hi(self):                            # 不再使用 Parent Class 中的定义，而是新的……
        print('Hey! Nice day, Huh?') # 重写（Overrides）在Parent Class 中的 Methods
        
g = Golem('Clay') # a.创建了Golem这个Class的一个Instance，即为g，对使用者来说，就是个Object；
	# b.因为Golem这个Class中有 __init__()，所以当 g 被创建的时候，g就被初始化
	# c.在 g 所在的变量目录中，出现了一个叫做 self 的用来指代 g 本身的变量；
g.name 
g.built_year 
g.say_hi
g.say_hi()
type(g)
type(g.name)
type(g.built_year)
type(g.__init__)
type(g.say_hi)
1.3 重写（Overrides）
	创建一个 Inherited Class时，可以重写（Overriding）Parent Class 中的 Methods。
1.4 Inspecting A Class
	作为用户了解一个Class的Interface，即它的属性Attributes和方法Methods时，常用的有三种方式：
	(1) help(object) #待查
	(2) dir(object)
	(3) object.__dict__
1.5 变量的作用域(Scope)
	每个变量都属于某一个 Scope（变量的作用域），在同一个 Scope 中，变量可以被引用被操作
(1)三个 Python 的内建函数：
hasattr(object, attr) 查询这个 object 中有没有这个 attr，返回布尔值
getattr(object, attr) 获取这个 object 中这个 attr 的值
setattr(object, attr, value) 将这个 object 中的 attr 值设置为 value
(2) 私有变量（Private Variables）:Python中，变量名前面加上一个以上下划线（Underscore）_ 。不能被外部引用
	按照Python惯例，会使用两个下划线起始，去命名私有变量，如：__life_span，使其成为私有变量，外部不能触达（不能引用 Golem.__life_span）
1.6 Encapsulation
	在 def population(self): 之前的一行加上一句 @property，则：
	a.外部能够像获得Class的属性那样，直接写 g.population，而不是必须加上括号g.population()传递参数（实际上传递了一个隐含的self参数）
	b.可以直接引用 g.population，但在外部不能再直接给 g.population 赋值了，否则会报错
	若希望从外部可以设置这个值，那就得再写个函数，并且在函数之前加上一句@population.setter
	a..population 这个 Attribute 就可以从外部被设定其值了
1.7 本节没看太懂
补充——字符串和布尔值转换：
	false、0、空字符串、null、undefined被划分为两类：假值、空值。
	0、空字符串和false归为一类，称为“假值”；把null和undefined归为一类，称为“空值”。
	假值还算一个有效的对象，因此可以对其使用toString等类型相关的方法，而空值则将会抛出异常：xxx hash no properties。
	
# Part.3.B.3.decorator-iterator-generator
1 函数工具
	装饰器、迭代器和生成器，这些都是函数工具。有人把它们称为 DIG（Decorator，Iterator，Generator）
		—— 它们都是真正掌握 Python 的关键。
2 迭代器（Iterator）
	Python 中的所有容器，都是可迭代的 —— 即可以通过迭代遍历每一个元素
2.1 内建函数iter()
	把一个 “可迭代对象”（Iterable）转换成 “迭代器”（Iterator）
	如：i = iter("Python")
	    type(i) # str_iterator
	    next(i) # "P"，调到最后一个元素，再调用就会有 StopIteration 错误提示。
2.2 迭代器函数
	迭代器是个 Object，所以写迭代器的时候写的是 Class，比如，我们写一个数数的迭代器，Counter：
class Counter(object):
    def __init__(self, start, stop):
        self.current = start
        self.stop = stop
    def __iter__(self): # 关键(1)这两句是约定俗成的写法，有它们Counter 这个类就被会被识别为 Iterator 类型
        return self     
    def __next__(self): # 关键(2)加上这个，整个class就是个完整的迭代器
        if self.current > self.stop:
            raise StopIteration
        else:
            c = self.current
            self.current += 1
        return c

for c in Counter(101, 103):
    print(c, sep=', ') # 可以用for loop或者while loop去遍历所有元素
3 生成器（Generator）
3.1 生成器函数
	用函数（而不是 Class）写一个Counter ，用生成器（Generator）
def counter(start, stop):
    while start <= stop:
        yield start # yield语句不同于return，在它之后的语句依然会被执行，而return之后的语句就被忽略了
        start += 1
	
for i in counter(101, 105):
    print(i)
# 生成器函数被 next() 调用后，执行到 yield 生成一个值返回（然后继续执行 next() 外部剩余的语句）；
# 下次再被 next() 调用的时候，从上次生成返回值的 yield 语句处继续执行
3.2 生成器表达式
举例如：even = (e for e in range(10) if not e % 2)
	# 圆括号（），even就是用生成器创造的迭代器（Iterator）
	# 若是用了方括号，那就是用生成器创造的列表（List）；用花括号 {} 生成的就是集合（Set）
	# 生成器表达式必须在括号内使用，包括函数的参数括号——没理解
4 装饰器（Decorator）
	a.关键：函数本身也是对象（即，Python 定义的某个 Class 的一个 Instance）
	b.因此，函数本身其实可以与其它的数据类型一样，作为其它函数的参数或者返回值
	c. wrapper() :返回的一个函数的调用，wrapper:返回的这个函数本身
4.1 装饰器操作符
（1）Python 提供了一个针对函数的操作符 @，举例：
def a_decorator(func): # 被 @ 调用的函数，叫做 “装饰器”（Decorator），比如代码中的 a_decorator(func)
    def wrapper():
        print('We can do sth. before calling a_func...')
        func()
        print('... and we can do sth. after it was called...')
    return wrapper # wrapper 这个函数本身

@a_decorator #每次a_func()在被调用的时候，因为它之前有一句 @a_decorator，所以它会先被当作参数传递到 a_decorator(func) 这个函数中。
		 # 而后，真正的执行，是在 a_decorator() 里被完成的。
def a_func():
    print("Hi, I'm a_func!")
    
a_func()
（2）装饰器的作用
@a_decorator		等价于	def a_func():
def a_func():				...
    ...				   a_func = a_decorator(a_func)

就是用 a_decorator 的调用结果替换掉原来的函数。
（3）装饰器的用途
最常用的场景：用来改变其它函数的行为
（4）执行顺序
@uppercase # “自下而上”—— “由里到外” 更为准确。这里是先strong后uppercase
@strong
def an_output():
...
（5）装饰带有参数函数
装饰器函数本身这么写：
def a_decorator(func):
    def wrapper(*args, **kwargs):
        return original_result
    # ...   
    return wrapper
# (*args, **kwargs) 非常强大，它可以匹配所有函数传进来的所有参数；
# 准确地讲，*args接收并处理所有传递进来的位置参数，**kwargs 接收并处理所有传递进来的关键字参数。

# Part.3.B.4.regex
1 正则表达式
正则表达式(Regular Expression):常简写为regex、regexp或RE，又称正规表示式、正规表示法、正规运算式、规则运算式、常规表示法。
	正则表达式使用单个字符串来描述、匹配一系列符合某个句法规则的字符串。
	在很多文本编辑器里，正则表达式通常被用来检索、替换那些符合某个模式的文本。许多程序设计语言都支持利用正则表达式进行字符串操作。
一个正则表达式（Regular Expression）通常被称为一个模式（Pattern）
我们可以用书写特定的规则，用来在文本中捕获与规则一致的字符串，而后对其进行操作
1.1 总结
（1）规则表达式（Regular Expressions，通常缩写为 Regex）是最强大且不可或缺的文本处理工具————
	它的用处就是在文本中扫描/搜索（Scan/Search）与某一规则（Pattern）匹配（Match，即，与规则一致）的所有实例，
	并且还可以按照规则捕获（Capture）其中的部分或者全部，对它们进行替换（Replace）。
（2）用处
a.替换Replace
b.检查格式：用Regex检查用户输入的密码是否过于简单（如：全部都由数字构成），用来验证用户输入的电话号码、证件号码是否符合特定格式等等。

ps:
	a. '...': 不用 raw string,每个转义符号都要写成 \\
	  r'...': 用 raw string，转义符号就可以直接使用 \ 本身，如果搜索 \ 这个符号本身，是得写 \\
	b. re.findall(pttn, str) 的意思是说，把 str中所有与 pttn 这个规则一致的字符串都找出来
2 优先级
	编程语言是用来运算的。运算，就有操作符（Operators）和操作元（Operands）。
	在 Regex 中，操作符也有优先级。它的操作元有个专门的名称，原子（Atom）
3 原子（Atom）
	在 Regex 的 Pattern 中，操作元，即，被运算的 “值”，被称为原子（Atom）
3.1 本义字符
	最基本的原子，就是本义字符，它们都是单个字符。
	本义字符包括从 a 到 z，A 到 Z，0 到 9，还有 _ —— 它们所代表的就是它们的字面值。
	即，相当于string.ascii_letters 和 string.digits 以及 _。
3.2 特殊字符
	\ + * . ? - ^ $ | ( ) [ ] { } < >
	写Regex时，搜索以上这些特殊字符时，直接加上转义符号 \ 来表示
	（注：# 并不是 Regex 的特殊符号，所以它之前的转义符号可有可无，但建议写为\#）
跟过往一样，所有的细节都很重要，它们就是需要花时间逐步熟悉到牢记。
3.3 集合原子
	(1)标示：使用方括号 []
	举例：[abc] 的意思：abc 中的任意一个字符。
	(2)方括号中，可以使用两个操作符：-（区间）和 ^（非）。
		[a-z] ：表示从小写字母 a 到小写字母 z 中的任意一个字符。
		[^abc] ：表示abc以外的其它任意字符，即非[abc]。注：一个集合原子中，^符号只能用一次，且紧跟在[之后，否则不起作用。
3.4 类别原子
	(1)定义：指那些能够代表 “一类字符” 的原子
	(2)标示：使用转义符号再加上另外一个符号表达
	(3)d 是 digits、w 是 word characters、s 是 spaces；
		\d 任意数字；等价于 [0-9]
		\D 任意非数字；等价于 [^0-9]
		\w 任意本义字符；等价于 [a-zA-Z0-9_]
		\W 任意非本义字符；等价于 [^a-zA-Z0-9_]
		\s 任意空白；相当于 [ \f\n\r\t\v]（注意，方括号内第一个字符是空格符号）
		\S 任意非空白；相当于 [^ \f\n\r\t\v]（注意，紧随 ^ 之后的是一个空格符号）
		.  除 \r \n 之外的任意字符；相当于 [^\r\n]
		注：f 是 flip分页符、n 是 new line换行符、r 是 return换行符、t 是 tab制表符、v 是 vertical tab纵向制表符（很少用到）
3.5 边界原子
	(1)作用：可以用边界原子指定边界，也称“定位操作符”
	(2)举例：
		^  匹配被搜索字符串的开始位置；
		$  匹配被搜索字符串的结束位置；
		\b 匹配单词的边界；er\b，能匹配 coder 中的 er，却不能匹配 error 中的 er；
		\B 匹配非单词边界；er\B，能匹配 error 中的 er，却不能匹配 coder 中的 er。
	(3)^ 和 $ 在 Python 语言中被 \A 和 \Z 替代
3.6 组合原子
	(1)标识：用圆括号 () 将多个单字符原子组合成一个原子，() 内的字符串将被当作一整个原子，可以被随后我们要讲解的数量操作符操作
	(2)作用：() 操作符有两个作用：组合（Grouping），另外一个作用是捕获（Capturing)。
	(3)举例：
		er   是两个原子，'e' 和紧随其后的 'r'
		[er] 是一个原子，'e' 或者 'r'；
		(er) 是一个原子，'er'
4.1 数量操作符
	(1)作用：用来限定位于它们之前的原子允许出现的个数；不加数量限定则代表出现一次且仅出现一次。
	(2)定义：
		+ : # 前面的原子必须至少出现一次，即：出现次数 ≧ 1
		? : # 前面的原子最多只可以出现一次，即：0 ≦ 出现次数 ≦ 1
	        * : # 前面的原子可以不出现，也可以出现一次或者多次，即：出现次数 ≧ 0
	        {n, m} : # 之前的原子出现至少 n 次，至多 m 次
		{n}    : # 之前的原子出现确定的 n 次；、
		{n,}   : # 之前的原子出现至少 n 次；
4.2 或操作符 |
	所有操作符中优先级最低的，数量操作符的优先级比它高。在 | 前后的原子被数量操作符（如果有的话）操作之后才交给 | 操作。
	注：在集合原子中（即[] 内的原子）各个原子之间的关系，只有 “或” —— 相当于方括号中的每个原子之间都有一个被省略的 |。
	注：中括号的 | 不被当作特殊符号，而是被当作 | 这个符号本身。在中括号中的圆括号，也被当作圆括号 () 本身，而无分组含义。
4.3 匹配并捕获
	捕获（Capture），使用的是圆括号 ()，使用圆括号得到的匹配的值被暂存成一个带有索引的列表，第一个是 $1，第二个是 $2…… 以此类推。
	随后，我们可以在替换的过程中使用 $1 $2 中所保存的值。
	注：Python中调用 re 模块后，在 re.sub() 中调用被匹配的值，用的索引方法是 \1、\2…… 以此类推。
	注：re.sub(pttn, repl, str) # 在str中通过pttn规则获取的值，repl中用\1等调用
4.4 非捕获匹配
	标识：不捕获圆括号中的内容，使用括号的目的只是分组，而非捕获，那需要在圆括号内最开头加上 ?:，即(?:...)
	操作符：
	(?=pattern)：正向肯定预查（look ahead positive assert），在任何匹配规则的字符串开始处匹配查找字符串。
		这是一个非获取匹配，也就是说，该匹配不需要获取供以后使用。
	       例如，Windows(?=95|98|NT|2000) 能匹配 Windows2000 中的 Windows，但不能匹配 Windows3.1 中的 Windows。
	       预查不消耗字符，即在一个匹配发生后，在最后一次匹配之后立即开始下一次匹配的搜索，而不是从包含预查的字符之后开始。
	(?!pattern)：正向否定预查（negative assert），在任何不匹配规则的字符串开始处匹配查找字符串。
	       这是一个非获取匹配，也就是说，该匹配不需要获取供以后使用。
	       例如Windows(?!95|98|NT|2000) 能匹配 Windows3.1 中的 Windows，但不能匹配 Windows2000 中的 Windows。
	       预查不消耗字符，也就是说，在一个匹配发生后，在最后一次匹配之后立即开始下一次匹配的搜索，而不是从包含预查的字符之后开始。
	(?<=pattern)：反向（look behind）肯定预查，与正向肯定预查类似，只是方向相反。
	       例如，(?<=95|98|NT|2000)Windows 能匹配 2000Windows 中的 Windows，但不能匹配 3.1Windows 中的 Windows。
	(?<!pattern)：反向否定预查，与正向否定预查类似，只是方向相反。
	       例如 (?<!95|98|NT|2000)Windows 能匹配 3.1Windows 中的 Windows，但不能匹配 2000Windows 中的 Windows。
5 控制标记
	有几个全局控制标记（Flag）需要了解，其中最常默认指定的有 G 和 M：
(1)A/ASCII，默认为 False
	\d, \D, \w, \W, \s, \S, \b, 和 \B 等只限于 ASCII 字符
	行内写法：(?a)
	Python re 模块中的常量：re.A re.ASCII
(2)I/IGNORECASE，默认为 False
	忽略字母大小写
	行内写法：(?i)
	Python re 模块中的常量：re.I re.IGNORECASE
(3)G/GLOBAL，默认为 True
	找到第一个 match 之后不返回
	行内写法：(?g)
	Python re 模块中这个标记不能更改，默认为 TRUE
(4)L/LOCALE，默认为 False
	由本地语言设置决定 \d, \D, \w, \W, \s, \S, \b, 和 \B 等等的内容
	行内写法：(?L)
	Python re 模块中的常量：re.L re.LOCALE
(5)M/MULTILINE，默认为 True
	使用本标志后，^ 和 $ 匹配行首和行尾时，会增加换行符之前和之后的位置。
	行内写法：(?m)
	Python re 模块中的常量：re.M re.MULTILINE
(6)S/DOTALL，默认为 False
	使 . 完全匹配任何字符，包括换行；没有这个标志，. 匹配除了 n r 之外的任何字符。
	行内写法：(?s)
	Python re 模块中的常量：re.S re.DOTALL
(7)X/VERBOSE，默认为 False
	当该标志被指定时，Pattern 中的的空白符会被忽略，除非该空白符在圆括号或方括号中，或在反斜杠 \ 之后。这样做的结果是允许将注释写入 Pattern，这些注释会被 Regex 解析引擎忽略。注释用 # 号来标识，不过该符号不能在字符串或反斜杠之后。
	行内写法：(?x)
	Python re 模块中的常量：re.X re.VERBOSE
6 几个最常用的 Regex
(正则表达式的图形化示意图:https://regexper.com/)
(1)matching username：/^[a-z0-9_-]{3,16}$/
(2)matching password[3]：/^[a-z0-9_-]{6,18}$/
(3)matching a HEX value：/^#?([a-f0-9]{6}|[a-f0-9]{3})$/
(4)matching a slug：/^[a-z0-9-]+$/
(5)matching email address：/^([a-z0-9_\.-]+)@([\da-z\.-]+)\.([a-z\.]{2,6})$/
(6)matching a URL：/^(https?:\/\/)?([\da-z\.-]+)\.([a-z\.]{2,6})([\/\w \.-]*)*\/?$/
(7)matching an IP address：/^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$/
(8)matching a HTML tag：/^<([a-z]+)([^<]+)*(?:>(.*)<\/\1>|\s+\/>)$/

Part.3.B.5.bnf-ebnf-pebnf



Part.3.C.breaking-good-and-bad


Part.3.D.indispensable-illusion


Part.3.E.to-be-thorough


Part.3.F.social-selfteaching


Part.3.G.the-golden-age-and-google


Part.3.H.prevent-focus-drifting

