注册：
curl -i -X POST \
   -H "Content-Type: application/json; indent=4" \
   -d '{
   "jsonrpc": "2.0",
    "method": "user.register",
    "params": {
      "username": "test",
      "password": "123456"
      },
      "id": "cde5749c-de2f-46ea-b9c5-824cf1f3fc92"
}' http://127.0.0.1:2001/api

登录：
curl -i -X POST \
   -H "Content-Type: application/json; indent=4" \
   -d '{
   "jsonrpc": "2.0",
    "method": "user.verify",
    "params": {
      "username": "test",
      "password": "123456"
      },
      "id": "36d8d630-4092-4add-abfc-55a257dae7d9"
}' http://127.0.0.1:2001/api

token:
eyJhbGciOiJIUzI1NiIsImlhdCI6MTU1MzY5Mjg2MCwiZXhwIjoxNTUzNjkzNDYwfQ.eyJpZCI6MX0.RKR83ZzNs3lgz9jixDUiUuKYrWwKwvZPEiXoXFRwq98

请求资源：
curl -i -X POST \
   -H "Content-Type: application/json; indent=4" \
   -d '{
    "jsonrpc": "2.0",
    "method": "App.hello",
    "params": {
      "token": "eyJhbGciOiJIUzI1NiIsImlhdCI6MTUyMTYxNzMzMywiZXhwIjoxNTIxNjE3OTMzfQ.eyJpZCI6M30.pswj1Sbny8EM2u8T01s7gizS02LQ-RS2PSvme2jQQLs",
      "name": "jack"
    },
    "id": "61a746df-21c5-485c-9aa5-b7c9b3a938e6"
}' http://127.0.0.1:2001/api

pip3.6 install -U flask-sqlalchemy marshmallow-sqlalchemy

初始化： python3.6 manage.py db init
创建数据库： python3.6 manage.py db migrate -m ‘first’



