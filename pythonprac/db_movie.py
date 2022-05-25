from pymongo import MongoClient

client = MongoClient('mongodb+srv://test:sparta@cluster0.qi22a.mongodb.net/Cluster0?retryWrites=true&w=majority')
db = client.dbsparta

# 여러개 찾기 - 예시 ( _id 값은 제외하고 출력)
# all_movies = list(db.movies.find({},{'title':'가버나움'}))
# print(all_movies)
# 한 개 찾기 - 예시
# movie = db.movies.find_one({'title':'가버나움'})
# print(movie)
# print(movie['star'])

# #평점이 가버나움 평점과 같은 영화 다 찾기
# star = db.movies.find_one({'title':'가버나움'})['star']
# movies = list(db.movies.find({'star':star},{'_id':False}))
# for m in movies:
#     print(m, m['title'])

# 가버나움 평점 0으로 만들기
# db.movies.update_one({'title':'가버나움'},{'$set':{'star':'0'}})
movie = db.movies.find_one({'title':'가버나움'})
print(movie)

