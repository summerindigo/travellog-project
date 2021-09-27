# 테스트 샘플 _ github 작동유무 확인 (한준희)

from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

from pymongo import MongoClient


# client = MongoClient('localhost', 27017)
client = MongoClient('mongodb://test:test@localhost', 27017)
db = client.dbhomework


## HTML 화면 보여주기
@app.route('/')
def homework():
    return render_template('homework_02week_junhee_Han.html')


# 주문하기(POST) API
@app.route('/order', methods=['POST'])
def save_order():
    name_receive = request.form['name_give']
    quantity_receive = request.form['quantity_give']
    address_receive = request.form['address_give']
    phone_receive = request.form['phone_give']

    doc = {
        'name':name_receive,
        'quantity':quantity_receive,
        'address':address_receive,
        'phone':phone_receive
    }
    db.chuseokoder.insert_one(doc)
    return jsonify({'result': 'success', 'msg': '해당주문이 정상적으로 등록됐습니다!'})


# 주문 목록보기(Read) API
@app.route('/order', methods=['GET'])
def view_orders():
    orders = list(db.chuseokoder.find({},{'_id':False}))

    return jsonify({'result': 'success', 'orders': orders})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
