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
	a.每次某个函数被调用，这个函数内部所有的变量，都是局域变量。即便那个函数内部某个变量的名称与它外部的某个全局变量名称相同，它们也不是同一个变量，只是名称相同而已。
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

# Part.2.D.4-recursion.ipynb



# Part.2.D.5-docstrings.ipynb
