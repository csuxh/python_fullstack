# by luffycity.com
from redis import StrictRedis

conn = StrictRedis(host='127.0.0.1', port=6379)

# conn = redis.Redis(host='140.143.227.206',port=6379,password='1234')

print(conn.get('session:eyJ1c2VybmFtZSI6ImphY2t4aWEifQ.D4RGUw._AmdtO0cTStRjHN_o-mfy_021V4'))