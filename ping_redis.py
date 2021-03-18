import redis

r = redis.Redis(host="localhost",port=6379,db=0)
settr = r.set('foo','bar')
gettr = r.get('foo')

print(f"printing getter and setter -> {settr}, {gettr}")