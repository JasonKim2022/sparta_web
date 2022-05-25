from pymongo import MongoClient
client = MongoClient('mongodb+srv://test:sparta@cluster0.qi22a.mongodb.net/Cluster0?retryWrites=true&w=majority')
db = client.dbsparta

from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route("/homework", methods=["POST"])
def homework_post():
    name_receive = request.form['name_give']
    comment_receive = request.form['comment_give']
    doc = {
        'name':name_receive,
        'comment':comment_receive
    }

    db.homework.insert_one(doc)

    # print(sample_receive)
    return jsonify({'msg':'등록되었습니다. 감사합니다!'})

@app.route("/homework", methods=["GET"])
def homework_get():
    homeworks = list(db.homework.find({}, {'_id': False}).sort('_id',-1))

    return jsonify({'homeworks':homeworks})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)