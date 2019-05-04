from crawl_guazi import *

pool = redis.ConnectionPool(host='172.17.0.2', port=6379, decode_responses=True, db=1, password='De32wsxC')
redis_con = redis.Redis(connection_pool=pool)

