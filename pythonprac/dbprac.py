from pymongo import MongoClient
client = MongoClient('mongodb+srv://test:sparta@cluster0.qi22a.mongodb.net/Cluster0?retryWrites=true&w=majority')
db = client.dbsparta

# doc = {
#     'name':'bob2',
#     'age':30
# }
# db.users.insert_one(doc)

# 삽입
# db.users.insert_one({'name':'bobby2','age':32})
# db.users.insert_one({'name':'john2','age':22})
# db.users.insert_one({'name':'ann2','age':25})

# doc = {'name':'ann3','age':22}
# db.users.insert_one(doc)

# 리스트 조회
# all_users = list(db.users.find({}))
# {'_id': ObjectId('62751ee3e611a2ef39fb3650'), 'name': 'bob', 'age': 27}
# all_users = list(db.users.find({},{'_id':False}))
# {'name': 'bob2', 'age': 30}

# for user in all_users:
#     print(user)

#조건 검색
# user = db.users.find_one({'name':'bobby2'})
# print(user)
#print(user['age'])

# 수정
#db.users.update_one({'name':'bobby2'},{'$set':{'age':19}})

# 삭제
# db.users.delete_one({'name':'bobby2'})

# 저장 - 예시
doc = {'name':'bobby','age':21}
db.users.insert_one(doc)

# 한 개 찾기 - 예시
user = db.users.find_one({'name':'bobby'})

# 여러개 찾기 - 예시 ( _id 값은 제외하고 출력)
all_users = list(db.users.find({},{'_id':False}))

# 바꾸기 - 예시
db.users.update_one({'name':'bobby'},{'$set':{'age':19}})

# 지우기 - 예시
db.users.delete_one({'name':'bobby'})