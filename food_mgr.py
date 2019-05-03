import db
import msgpack
from food import Food
import uuid as libuuid

class FoodMgr:
	def __init__(self, uid):
		self.redis_server = db.get_redis_client()
		self.uid = uid
		self.r_save_name = 'foodids'
		self._foods = {}


	def save(self):
		food_ids = self._foods.keys()
		if food_ids:
			self.redis_server.hset(self.r_save_name, self.uid, msgpack.packb(food_ids))

	def load(self):
		food_ids_b = self.redis_server.hget(self.r_save_name, self.uid)
		if food_ids_b is None:
			return
		food_ids = msgpack.unpackb(food_ids_b)
		for i in range(0, len(food_ids)):
			uuid = food_ids[i]
			self._foods[uuid] = Food.load(uuid)

	def create(self, store, name, price, tag, min_count=1):
		if self.get_id(store, name) is None:
			food = Food(store, name, price, None, min_count)
			food.set_tag(tag)
			self._foods[food.uuid] = food
			self.save()
			return food

	def get_id(self, store, name):
		for uuid in self._foods:
			food = self._foods[uuid]
			if food.store == store and food.name == name:
				return uuid
		return None

	def get(self, store, name, add=True, price = None, tag=None):
		uuid = self.get_id(store, name)
		food = None
		if uuid == None and add == True:
			return self.create(store, name, price, tag)
		return self._foods[uuid]

	def get_delicious(self):
		foods = []
		for key in self._foods:
			food = self._foods[key]
			if 'delicious' in food.tags.keys() and food.tags['delicious'] == True:
				foods.append(food)
		return foods
	
	def echo(self):
		for key in self._foods:
			print(self._foods[key])
