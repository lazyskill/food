#coding:utf-8
import db
import msgpack
from food import Food
from food_mgr import FoodMgr
import uuid as libuuid

class User:
	def __init__(self, name='jun'):
		self.name = name
		self.food_mgr = FoodMgr(name)

	def add_black(self, store, name, price):
		food_obj = self.food_mgr.get(store, name, add=True, price = price, tag='black')
		food_obj.set_tag('black')

	def add_delicious(self, store, name, price):
		food_obj = self.food_mgr.get(store, name, add=True, price = price, tag='delicious')
		food_obj.set_tag('delicious')

	def recommend(self):
		foods = self.food_mgr.get_delicious()
		result = {}
		for i in range(0, len(foods)):
			result[foods[i].store+" "+foods[i].name] = True
		if result:
			return sorted(result.keys())
user = User()
user.add_black("大鸭梨烤鸭（八角店）", "酸辣土豆丝", 19)
user.add_black("湘鑫源湘菜馆", "小炒腊肠盖饭", 22.99)
user.add_black("好嫂子（八角店）", "香辣鱼块", 20.8)

user.add_delicious("大鸭梨烤鸭", "小炒肉", 36)
r = user.recommend()
if r:
	for i in range(0, len(r)):
		print(r[i])
