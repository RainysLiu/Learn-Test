import time

import redis   # 导入redis 模块


# 连接
"""
r = redis.Redis(host='localhost', port=6379, decode_responses=True, db=15)
r.set('name', 'runoob')  # 设置 name 对应的值
print(r['name'])
print(r.get('name'))  # 取出键 name 对应的值
print(type(r.get('name')))  # 查看类型
"""

# 连接池
pool = redis.ConnectionPool(host='localhost', port=6379, decode_responses=True, db=15)
r = redis.Redis(connection_pool=pool)


# 1.string类型的操作
"""
r.set('name1', 'runoob1')  # 设置 name 对应的值
print(r.get('name1'))  # 取出键 name 对应的值
"""

# 设置超时时间
"""
r.setex('name2', 'runoob1', 5)  # 设置 name 对应的值
print(r.get('name2'))  # 取出键 name 对应的值
time.sleep(10)
print(r.get('name2'))  # 取出键 name 对应的值
"""

# 批量设置键值对
"""
r.mget({'k1': 'v1', 'k2': 'v2'})
r.mset(k1="v1", k2="v2") # 这里k1 和k2 不能带引号 一次设置对个键值对
print(r.mget("k1", "k2"))   # 一次取出多个键对应的值
print(r.mget("k1"))
"""


"""
# 设置自增
r.set("visit:12306:totals", 34634)
print(r.get("visit:12306:totals"))
# 每当有一个页面点击，则使用INCR增加点击数即可。

r.incr("visit:12306:totals")
r.incr("visit:12306:totals")
# 页面载入的时候则可直接获取这个值

print(r.get("visit:12306:totals"))
"""

# 2.hash数据类型

"""
r.hset("hash1", "k1", "v1")
r.hset("hash1", "k2", "v2")
print(r.hkeys("hash1")) # 取hash中所有的key
print(r.hget("hash1", "k1"))    # 单个取hash的key对应的值
print(r.hmget("hash1", "k1", "k2")) # 多个取hash的key对应的值
r.hsetnx("hash1", "k2", "v3") # 只能新建
print(r.hget("hash1", "k2"))
"""


# 3list数据类型
"""
r.lpush("list1", 11, 22, 33)
print(r.lrange('list1',0, -1))
"""


# 4集合类型操作
"""
r.sadd("set1", 33, 44, 55, 66)  # 往集合中添加元素
print(r.scard("set1"))  # 集合的长度是4
print(r.smembers("set1"))   # 获取集合中所有的成员
r.zadd("zset1", n1=11, n2=22)
"""

# 5有序集合类型操作
r.zadd("zset1", n1=11, n2=22)
r.zadd("zset2", 'm1', 22, 'm2', 44)
print(r.zcard("zset1")) # 集合长度
print(r.zcard("zset2")) # 集合长度
print(r.zrange("zset1", 0, -1))   # 获取有序集合中所有元素
print(r.zrange("zset2", 0, -1, withscores=True))   # 获取有序集合中所有元素和分数