import db
import msgpack
import uuid as libuuid

class Food:
	def __init__(self, store, name, price, uuid = None,  min_count=1):
		self.redis_server = db.get_redis_client()
		self.uuid = uuid
		if self.uuid == None:
			self.uuid = str(libuuid.uuid4())
		self.store = store
		self.name = name
		self.latest_eat_time = 0
		self.min_count = min_count
		self.price = 0
		self.tags = {}

	def save(self):
		data = {
			'uuid': self.uuid,
			'store':self.store,
			'name': self.name,
			'latest_eat_time': self.latest_eat_time,
			'price': self.price,
			'min_count': self.min_count,
		}
		if self.tags:
			data['tagsb'] = msgpack.packb(self.tags)
		self.redis_server.hset('foods', self.uuid, msgpack.packb(data))

	@staticmethod
	def load(uuid):
		redis_server = db.get_redis_client()
		db_food = msgpack.unpackb(redis_server.hget('foods', uuid))
		food = Food(db_food['store'], db_food['name'], db_food['price'], db_food['uuid'])
		if 'min_count' in db_food.keys():
			food.min_count = db_food['min_count']
		else:
			food.min_count = 1
		food.latest_eat_time = db_food['latest_eat_time']
		if db_food['tagsb']:
			food.set_tag(None, db_food['tagsb'])
		return food

	def set_tag(self, tag=None, db_data = False):
		if db_data is False:
			self.tags[tag] = True
			if tag == 'delicious':
				self.unset_tag('black')
			elif tag == 'black':
				self.unset_tag('delicious')
			self.save()
		else:
			self.tags = msgpack.unpackb(db_data)

	def unset_tag(self, tag):
		if tag in self.tags.keys():
			self.tags[tag] = None
			self.save()
