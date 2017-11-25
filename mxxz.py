from operator import itemgetter

# TIME = -2
# NAME = 0
# TYPE = 1
# INTEREST = -1
# PRICE = 2

def get_interest_list(itemDict, mytype):
	l = []
	for key,value in itemDict.items():
		if value[0] == mytype:
			l.append((key, value[-1]))
	l.sort(key=itemgetter(1), reverse=True)
	print(l)

def max_list(l, time, number):
	# print(l)
	if number==1:		
		for item in l:
			if item[-1] <= time:
				return ([item[0]], item[1])
		return ([], 0)
	else:
		rl = []
		for item in l:
			productList, price = max_list(l, time-item[-1], number-1)
			productList.append(item)
			price += item[1]
			rl.append((productList, price))
		rl.sort(key=itemgetter(1), reverse=True)
		return (rl[0])

def get_best_product_list(itemDict, mytype, time, number):
	l = []
	for key,value in itemDict.items():
		if value[0] == mytype:
			value = (key, value[1]-value[2], value[-2])
			l.append(value)
	l.sort(key=itemgetter(1), reverse=True)
	print("attention", l)
	rl = max_list(l, time, number)
	print(rl)


itemDict = {}
#普通：类别，名称，售价，成本，时间，单位时间收益
#矿物：类别，名称，售价
#制成品：类别，名称，售价，成本，制成列表，时间，单位时间收益
plants = [
("作物","小麦",1,0,2),
("作物","玉米",3,1,5),
("作物","胡萝卜",5,2,10),
("作物","甘蔗",7,3,20),
("作物","棉花",9,4,30),
("作物","草莓",11,5,60),
("作物","番茄",13,6,120),
("作物","松树",15,7,180),
("作物","土豆",17,8,240),
("作物","可可树",19,9,480),
("作物","橡胶树",30,15,720),
("作物","丝绸",33,20,900),
("作物","辣椒",20,11,300),
("作物","水稻",14,7,80),
("作物","玫瑰",28,18,150)
# ("作物","茉莉", 210),
# ("作物","咖啡树", 360)
]

milks = [
("牛奶", 7),
("鸡蛋", 10),
("羊毛", 15),
("培根", 32),
("蜂巢", 22),
("羽绒", 12),
("彩色羽毛", 31),
("黄桃", 34)
]


milkFactory = [
("奶油", 12, [("牛奶",1)], 11.25),
("奶酪", 25, [("牛奶",2)], 22.5),
("黄油",  39, [("牛奶",3)], 45),
("酸奶", 53, [("牛奶",4)], 67),
("黄桃酸奶",157, [("牛奶",2), ["黄桃", 2]], 90)
]

for item in plants:
	interest = round((item[2] - item[3])/item[4],2)
	value = (item[0], item[2], item[3], item[4], interest)
	itemDict[item[1]] = value

for item in milks:
	itemDict[item[0]] = ("畜牧产品", item[1])

for item in milkFactory:
	name = item[0]
	ingredients = item[2]
	cost = 0
	for igrdt in ingredients:
		cost += igrdt[1] * itemDict[igrdt[0]][1]
	itemDict[name] = ("乳品厂", item[1], cost, ingredients, item[-1], 
		round((item[1]-cost)/item[-1], 2))


print(itemDict)
# get_interest_list(itemDict, "作物")
get_best_product_list(itemDict, "乳品厂", 480, 7)
		
		