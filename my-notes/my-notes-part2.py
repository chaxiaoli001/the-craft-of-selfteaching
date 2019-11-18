Part.2.A.clumsy-and-patience笨拙与耐心
  预算观念非常重要 —— 这个观念的存在与否，成熟与否，基本上决定一个人未来的盈利能力。
  
Part.2.B.deliberate-practicing刻意练习
  所谓 “刻意练习”，其实是 “刻意思考哪里需要刻意练习” 之后最自然不过的事情 —— 所以，“刻意思考” 才是关键。
    准备个专门的地方记录

Part.2.C.why-start-from-writing-functions
1 从函数开始写起:
  因为结构化编程的核心就是拆分任务，把任务拆分到不能再拆分为止 —— 什么时候不能再拆分了呢？就是当一个函数只完成一个功能的时候
    参数的传递
    多参数的传递
    匿名函数以及函数的别称
    递归函数
    函数文档
    模块
    测试驱动编程
    可执行程序
    
# Part.2.D.1-args.ipynb
1 关于参数（上）
	结构上来看，每个函数都是一个完整的程序，因为一个程序，核心构成部分就是输入、处理、输出
2 为函数取名
	定义函数： def XXX():
	取名规则（同变量取名）：
	a.名称不能以数字开头。能用在名称开头的有，大小写字母和下划线 _；
	b.名称中不能有空格，要么使用下划线连接词汇，如，do_nothing，要么使用驼峰式(Camel Case)，如 doNothing —— 更推荐使用下划线；
	c.名称不能与关键字重合
	Python的Keyword List查询：
		import keyword
		keyword.kwlist #列出所有关键字
		keyword.iskeyword("as") #查询某个词是不是关键字
3 不接收任何参数的函数
	定义函数的时候，可以定义成不接收任何参数；但调用函数的时候，依然需要写上函数名后面的圆括号 ()
4 没有 return 语句的函数
	函数内部没有 return 语句：未定义返回值，那么该函数的返回值是 None，布尔值相当于是 False。
	使得函数调用总是可以在条件语句中被当作判断依据：if XXX():,if not XXX():
5 接收外部传递进来的值
	闰年：四年一闰，百年不闰，四百年再闰
	斐波那契数列：这个数列从第3项开始，每一项都等于前两项之和。F[n]=F[n-1]+F[n-2](n>=3,F[1]=1,F[2]=1)
6 变量的作用域
6.1 程序执行过程中，变量有全局变量（Global Variables）和局域变量（Local Variables）之分。
	全局变量：函数外的变量；局域变量：某函数内部所有的变量
	a.每次某个函数被调用，这个函数内部所有的变量，都是局域变量。
	  即便那个函数内部某个变量的名称与它外部的某个全局变量名称相同，它们也不是同一个变量，只是名称相同而已。
	b.更为重要的是，当外部调用一个函数的时候，准确地讲，传递的不是变量，而是那个变量的值。
6.2 函数内部处理被传递进来的值是可变容器（比如列表）的时候，值会全局变化，那么在函数内部对其操作之前，先创建一个它的拷贝。

# Part.2.D.2-aargs.ipynb
1 关于参数（下）
1.1 可以接收一系列值的位置参数（Positional Arguments）
	a.位置参数（Positional Arguments）
	b.*位置参数（Arbitrary Positional Arguments），姑且翻译为 “随意的位置参数”
		可以接收一系列值，在函数内部可以对这一系列值当做容器，用 for ... in ... 循环进行逐一的处理。调用函数时在参数前面加*，如XX(*X)
		注1：_在定义可以接收一系列值的位置参数时，建议在函数内部为该变量命名时总是用复数_，
		注2：一个函数中，可以接收一系列值的位置参数只能有一个；
			并且若是还有其它位置参数存在，那就必须把这个可以接收一系列值的位置参数排在所有其它位置参数之后。
2 为函数的某些参数设定默认值
	关键字参数（Keyword Arguments）：在定义函数的时候，为某些参数设定默认值
	可选参数：这些设定了默认值的参数
2.1 可以接收一系列值的关键字参数
	a.**关键字参数（Arbitrary Keyword Argument），姑且翻译为 “随意的关键字参数”
	b.在函数内部，处理接收到的 Arbitrary Keyword Argument 时，用的是对字典的迭代方式
	c.在调用函数的时候，也可以直接使用字典的形式
3 函数定义时各种参数的排列顺序
	Order of Arguments：
	Positional
	Arbitrary Positional
	Keyword
	Arbitrary Keyword
	位置参数>任意位置参数>关键字参数>任意关键字参数

# Part.2.D.3-lambda.ipynb匿名函数
1 化名（alias）——为了提高代码可读性
	eg:
	def _is_leap(year):
    	return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
	year_leap_bool = _is_leap # 给 _is_leap() 这个函数取了个化名
	补：id() 这个函数可以查询某对象的内存地址，同一个地址说明是同一个对象
2 lambda关键字写的函数——匿名函数
	语法结构：lambda_expr ::= "lambda" [parameter_list] ":" expression
	lambda x, y: x + y # 没有名字，所以被称为 “匿名函数”。
	注1：: 之前是参数，之后是表达式；这个表达式的值，就是这个函数的返回值
	注2：: 之后有且只能有一个表达式
2.1 lambda的使用场景
	a.作为某函数的返回值
	b.作为某函数的参数——更简洁
		eg: map(function, iterable, ...)
			函数的第一个参数，就是用来接收函数的。
			随后的参数是 iterable —— 就是可被迭代的对象，如各种容器：列表、元组、字典等
		eg:pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
		   pairs.sort(key=lambda p: p[1])
		eg:a_list = [1, 3, 5], b_list = [2, 4, 6]
		   list(map(lambda x, y: x * y, a_list, b_list))

# Part.2.D.4-recursion.ipynb 递归
1 递归函数（Recursive Functions）—— 那些在自身内部调用自身的函数
1.1 递归函数的执行过程
	eg:f(x)=x*f(x-1) x>1
1.2 递归的终点
	正常的递归函数一定有个退出条件
	死循环：无限循环的递归，函数里没有设置“中止自我调用”的条件，运行会报错
	补：Python 中，若是需要将某个值与 True 或者 False 进行比较，尤其是在条件语句中，推荐写法是：
	if condition: 等同于if condition is True:或者if condition == True:
1.3 递归函数的共同特征
	a.在return语句中返回的是自身的调用（或者是含有自身的表达式）
	b.为了避免死循环，一定要有至少一个条件下返回的不再是自身调用
1.4 变量的作用域
	a.根据作用域分为两种：全局变量（Global Variables）和局部变量（Local Variables）
	在函数内部被赋值而后使用的，都是局部变量，它们的作用域是局部，无法被函数外的代码调用；
	在所有函数之外被赋值而后开始使用的，是全局变量，它们的作用域是全局，在函数内外都可以被调用。
	b.原则：在函数内部绝对不调用全局变量。即便是必须改变全局变量，也只能通过函数的返回值在函数外改变全局变量。
1.5 递归函数三原则
	a.根据定义，递归函数必须在内部调用自己；
	b.必须设定一个退出条件；
	c.递归过程中必须能够逐步达到退出条件

# Part.2.D.5-docstrings.ipynb
1 函数的文档(Docstring)
	在函数定义内部，我们可以加上 Docstring；
	可以通过 help() 这个内建函数，或者 .__doc__ 这个 Method 去查看这个 Docstring，即该函数的 “产品说明书”
	a.Docstring 可以是多行字符串，也可以是单行字符串：
	b.Docstring 若存在，必须在函数定义的内部语句块的开头，也必须与其它语句一样保持相应的缩进（Indention）
	  Docstring 放在其它地方不起作用，查看时结果为None
1.1 书写 Docstring 的规范(https://www.python.org/dev/peps/pep-0257/)
	a.无论是单行还是多行的 Docstring，一概使用三个双引号扩起；
	b.在 Docstring 内部，文字开始之前，以及文字结束之后，都不要有空行；
	c.多行 Docstring，第一行是概要，随后空一行，再写其它部分；
	d.完善的 Docstring，应该概括清楚以下内容：参数、返回值、可能触发的错误类型、可能的副作用，以及函数的使用限制等等；
	e.每个参数的说明都使用单独的一行
1.2 Sphinx 版本的 Docstring 规范
	Sphinx 可以从 .py 文件里提取所有 Docstring，而后生成完整的 Documentation。
	它自己的一种标记语言，reStructureText，文件尾缀使用 .rst

# Part.2.D.6-modules.ipynb
1 保存到文件的函数
	保存起来，方便随时调用
1.1 模块（Module）
	a.定义：任何一个 A.py 文件都可以被称为模块，可以被外部调用
	b.用法：
	import A.py #引入模块
	A.__name__ # A模块的名称，即文件名A
	A.function_b() #引用模块中的方法
1.2 模块文件系统目录检索顺序
	import A.py # 先去看看内建模块里有没有指定的名称；如果没有，就按照 sys.path 所返回的目录列表顺序去找
	sys.path 所返回的目录列表中，当前的工作目录排在第一位
	指定检索目录，可以用 sys.path.append() 添加一个搜索位置
1.3 系统内建的模块
	import sys
	sys.builtin_module_names # 获取系统内建模块的列表
	"_sre" in sys.builtin_module_names # True
	注：跟变量名、函数名，不能与关键字重名一样，模块名称不能与系统内建模块名称重合
1.4 引入指定模块中的特定函数
	eg1:
	from mycode import is_prime
	is_prime(3) # 直接调用方法，不需要写成mycode.is_prime
	如果当前目录中并没有 mycode.py 这个文件，那mycode 会被当作目录名再被尝试一次。
	如果当前目录内，有个叫做 mycode 的目录（或称文件夹）且该目录下同时要存在一个 __init__.py 文件
	（通常为空文件，用于标识本目录形成一个包含多个模块的 包（packages），它们处在一个独立的 命名空间（namespace））
	eg2:
	from mycode import * # 把 mycode 这个文件夹中的所有 .py 文件全部导入
	eg3:导入 foo 这个目录中的 bar.py 这个模块文件
	import foo.bar 或者 from foo import bar
1.5 引入并使用化名（alias）——为了避免混淆，或为了避免输入太多字符
	from mycode import is_prime as isp
	import mycode as m
1.6 模块中不一定只有函数
	一个模块文件中，不一定只包含函数；它也可以包含函数之外的可执行代码
	注：在 import 语句执行的时候，模块中的非函数部分的可执行代码，只执行一次
1.7 dir() 函数
	用 dir() 函数查看模块中可触达的变量名称和函数名称

# Part.2.D.7-tdd.ipynb


# Part.2.D.8-main.ipynb

