#coding:utf-8
from food_mgr import FoodMgr
import msgpack
mgr = FoodMgr('jun')

store = '好嫂子（八角店）'
discounts=[]
discounts.append({'full': 40, 'sub':7})
discounts.append({'full': 65, 'sub':12})
store_info = {'travelling': 5.5, 'min_cost': 20, 'discounts': discounts}
mgr.redis_server.hset('stores', store, msgpack.packb(store_info))
mgr.redis_server.hset('stores', store, msgpack.packb(store_info))

tag = '盖饭'
mgr.create(store, '酸菜鱼饭', 28, tag)
mgr.create(store, '毛血旺饭', 32, tag)
mgr.create(store, '红烧肉饭', 21, tag)
mgr.create(store, '排骨饭', 28, tag)
mgr.create(store, '猪手饭', 28, tag)
mgr.create(store, '宫保鸡丁饭', 19, tag)
mgr.create(store, '茄子扁豆饭', 18, tag)
mgr.create(store, '西红柿鸡蛋饭', 18, tag)

tag = '菜'
mgr.create(store, '私房酱猪手', 9.8, tag)
mgr.create(store, '香辣猪手', 59, tag)
mgr.create(store, '炖排骨', 9, tag)
mgr.create(store, '农家红烧肉', 39, tag)

tag = '面'
mgr.create(store, '黑椒牛柳面（橄榄油）', 36, tag)
mgr.create(store, '茄汁牛肉炒面（橄榄油）', 36, tag)
mgr.create(store, '私房牛肉面', 20, tag)
mgr.create(store, '精品排骨面', 26, tag)
mgr.create(store, '炖肉面', 18, tag)
mgr.create(store, '炸酱面', 20, tag)
mgr.create(store, '茄红慢煨牛肉面', 22, tag)
mgr.create(store, '麻辣牛肉面', 21, tag)
mgr.create(store, '西红柿鸡蛋面', 16, tag)
mgr.create(store, '茄子扁豆面', 16, tag)
mgr.create(store, '雪菜面', 15, tag)
mgr.create(store, '榨菜肉丝面', 15, tag)

tag = '饮'
mgr.create(store, '黑椒牛柳面（橄榄油）', 36, tag)
mgr.create(store, '茄汁牛肉炒面（橄榄油）', 36, tag)
mgr.create(store, '私房牛肉面', 20, tag)
mgr.create(store, '精品排骨面', 26, tag)
mgr.create(store, '炖肉面', 18, tag)
mgr.create(store, '炸酱面', 20, tag)
mgr.create(store, '茄红慢煨牛肉面', 22, tag)
mgr.create(store, '麻辣牛肉面', 21, tag)
mgr.create(store, '西红柿鸡蛋面', 16, tag)
mgr.create(store, '茄子扁豆面', 16, tag)
mgr.create(store, '雪菜面', 15, tag)
mgr.create(store, '榨菜肉丝面', 15, tag)

tag='汤'
mgr.create(store, '酸辣汤', 22, tag)
mgr.create(store, '疙瘩汤', 22, tag)

tag='主食'
mgr.create(store, '白米饭',3, tag)
mgr.create(store, '绿茶饼',10, tag)
mgr.create(store, '紫米糕',10, tag)
mgr.create(store, '炸窝头',8, tag)

tag='炒饭'
mgr.create(store, '扬州炒饭',26, tag)
mgr.create(store, '酱油炒饭',18, tag)
mgr.create(store, '海鲜炒饭',29, tag)
mgr.create(store, '鸡蛋炒饭',16, tag)
mgr.create(store, '香肠炒饭',24, tag)

tag= '饮'
mgr.create(store, '银耳莲子炖雪梨', 8, tag)
mgr.create(store,'酸梅汤', 7, tag)
mgr.create(store,'山楂汁', 7, tag)
mgr.create(store,'自制酸牛奶', 9, tag)
mgr.create(store,'绿豆沙', 8, tag)
mgr.create(store,'现磨豆浆', 5, tag)
mgr.create(store,'果粒橙', 15, tag)
mgr.create(store,'燕京绿纯', 12, tag)
mgr.create(store,'雪花勇闯天涯', 7, tag)
mgr.create(store,'燕京鲜啤', 8, tag)
mgr.create(store,'大可乐', 10, tag)
mgr.create(store,'大雪碧', 10, tag)
mgr.create(store,'露露',   6, tag)
mgr.create(store,'冰绿茶', 6 , tag)
mgr.create(store,'冰红茶', 6 , tag)
mgr.create(store,'矿泉水', 3 , tag)
mgr.create(store,'听雪碧', 5 , tag)
mgr.create(store,'听可乐', 5 , tag)

tag='烤串'
mgr.create(store,'烤肠',3, tag, 5)
mgr.create(store,'鱼豆腐',3, tag, 5)
mgr.create(store,'鸡翅',7, tag, 5)
mgr.create(store,'大腰子',22, tag, 5)
mgr.create(store,'板筋',3, tag, 5)
mgr.create(store,'肉筋',3, tag, 5)
mgr.create(store,'骨肉相连',4, tag, 5)
mgr.create(store,'羊肉串', 3, tag, 5)

mgr.load()
mgr.echo()
