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

Part.3.B.1.classes-1.ipynb
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

# Part.3.B.2.classes-2.ipynb
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
	(1) help(object) #
	(2) dir(object)
	(3) object.__dict__
1.5 变量的作用域(Scope)
(1)三个 Python 的内建函数：
hasattr(object, attr) 查询这个 object 中有没有这个 attr，返回布尔值
getattr(object, attr) 获取这个 object 中这个 attr 的值
setattr(object, attr, value) 将这个 object 中的 attr 值设置为 value
(2)


Part.3.B.3.decorator-iterator-generator.ipynb


Part.3.B.4.regex.ipynb


Part.3.B.5.bnf-ebnf-pebnf.ipynb


Part.3.C.breaking-good-and-bad.ipynb


Part.3.D.indispensable-illusion.ipynb


Part.3.E.to-be-thorough.ipynb


Part.3.F.social-selfteaching.ipynb


Part.3.G.the-golden-age-and-google.ipynb


Part.3.H.prevent-focus-drifting.ipynb

