# coding: utf-8

import sys
import datetime
import itertools
import msgpack

import redis

REDIS_CLIENT_DICT = {}	# 每个db都有一个pool

def make_redis_client(redis_config):
	"""# make_redis_client: docstring
	args:
		redis_config:	 ---	arg
	returns:
		0	 ---
	"""
	try:
		if cmp(redis.VERSION, (2, 10, 1)) >= 0:
			pool = redis.BlockingConnectionPool(retry_on_timeout=True, **redis_config)
		else:
			pool = redis.BlockingConnectionPool(**redis_config)
	except:
		pool = redis.BlockingConnectionPool(**redis_config)

	redis_client = redis.Redis(connection_pool=pool)

	return redis_client


def get_redis_client_key(redis_config):
	"""
	组装 Redis 客户端在 pool 中的 Key
	"""

	return '_'.join([redis_config['host'], str(redis_config['port']), str(redis_config['db'])])


def init_client_dict():
	"""# init_pool: 每个redis库一个client，放在
	args:
		:	 ---	arg
	returns:
		0	 ---
	"""
	for server_name, server_config in settings.SERVERS.iteritems():
		for redis_config in server_config['cache_list']:
			client_key = get_redis_client_key(redis_config)
			REDIS_CLIENT_DICT[client_key] = make_redis_client(redis_config)

def get_redis_client(redis_config=None):
	"""
	args:
		redis_config:
				{'db': 4,
				 'host': '10.6.7.25',
				 'password': 'F8974044A778',
				 'port': 40100,
				 'socket_timeout': 5}
	"""
	if redis_config == None:
		redis_config = {}
		redis_config['host'] = "10.144.89.160"																							   
		redis_config['port'] = "9876"																				 
		redis_config['db'] = 10																					
		redis_config['password'] = "@BeiJing" 

	client_key = get_redis_client_key(redis_config)
	if client_key not in REDIS_CLIENT_DICT:
		client = make_redis_client(redis_config)
		REDIS_CLIENT_DICT[client_key] = client

	return REDIS_CLIENT_DICT[client_key]
