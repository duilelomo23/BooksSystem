from flask import Blueprint, request, json, g, session
from dacite import from_dict
from dacite_config import config
from users import dataclasses, datahelper, errors
from results import make_data_result ,Result
from datetime import datetime
from functools import wraps
import bcrypt
import re

blueprint = Blueprint("users", import_name = "users")






#  掛載裝飾器才可呼叫API 檢查登入狀態
def login_status(func):
    @wraps(func)  # 保留原始函數的名稱和屬性
    def my_decorator(*args, **kwargs):
        # 檢查 session 中是否有 'username'，如果沒有，返回未登入的回應
        print(session.get('username'),'username ----------------------')
        if not session.get('username'):
             return json.jsonify(errors.e2002)
        # 已登入，執行被裝飾的函數
        return func(*args, **kwargs)
    return my_decorator




#登入
@blueprint.route('/signin', methods=["POST"])
def user_login():
    #1. 解析JSON或參數
    x = json.loads(request.data)
    # x json轉為obj
    obj = from_dict(dataclasses.CreateUser, x, config=config)
    #2. 驗證資料
    print('login api -----------')
    #2.1. 名稱 密碼 不可為空白
    if obj.username is None or not obj.password:
        return json.jsonify(errors.e1001)
    #3. 使用username獲取password
    s = datahelper.user_login(obj.username.strip())
    hashed_password = s['password']
    if bcrypt.checkpw(obj.password.encode('utf-8'), hashed_password.encode('utf-8')):
        session['username'] = str(obj.username)
        return json.jsonify('登入成功', session['username'])
    else:
        return json.jsonify(errors.e5001)


#登出
@blueprint.route('/signout', methods=["POST"])
def user_signout():
    #判斷使用者是否登入狀態
    if session.get('username'):
        session.pop('username', None)
        return json.jsonify('登出成功', session.get('username'))
    else:
        return json.jsonify('未登入', session.get('username'))

    
    



#查詢所有資料
@blueprint.route('', methods=["GET"])
@login_status
def get_users():
    #1. 取得產品
    s = datahelper.get_users()
   #2. 回傳產品
    return json.jsonify(make_data_result(s))


#新增資料  註冊 
@blueprint.route('/signup', methods=["POST"])
def create_user():
    #1. 解析JSON或參數
    x = json.loads(request.data)
    obj = from_dict(dataclasses.CreateUser, x, config=config)
    #2. 驗證資料
    #2.1. 名稱 密碼 不可為空白
    if obj.username is None or not obj.password:
        return json.jsonify(errors.e1001)
    #2.2 名稱最少2字最多10字  密碼最少6碼最多15碼
    if len(obj.username) < 2 or len(obj.username) > 20:
        return json.jsonify(errors.e1002)
    if len(obj.password) < 6 or len(obj.password) > 20:
        return json.jsonify(errors.e1003)
    #不可傳入特殊符號  缺少判斷是否為文字
    if not re.match("^[a-zA-Z0-9]*$", obj.username):
        return json.jsonify(errors.e1004), 400
    if not re.match("^[a-zA-Z0-9]*$", obj.password):
        return json.jsonify(errors.e1004), 400
    #3. 建立產品
    #3.1 密碼加密
    hashed_password = bcrypt.hashpw(obj.password.encode('utf-8'), bcrypt.gensalt())
    #3.2. 建立產品
    s = datahelper.create_user(obj.username, hashed_password.decode('utf-8'))
    if s == False:
        return json.jsonify(errors.e1005)
    #3.2. 提交
    g.cursor().connection.commit()
   #4. 回傳產品
    return json.jsonify(Result(data=s))


#修改資料  
@blueprint.route('/<user_id>', methods=["PUT"])

def update_todo(user_id):
    #1. 解析JSON或參數
    #1.1. 解析JSON
    x = json.loads(request.data)
    obj = from_dict(dataclasses.UpdateUser, x, config=config)
    #1.2. 解析todo_id為int
    try:
        user_id = int(user_id)
    except:
        pass

    #2. 驗證資料
    #2.1. 驗證user_id是否存在
    if  isinstance(user_id, int) == False or \
          datahelper.is_user_id_existed(user_id) == False:
        return json.jsonify(errors.e3001) 
    #2.2.  username password 不可為空白
    if obj.username is None or not obj.password:
        return json.jsonify(errors.e1001)
    #2.2 名稱最少2字最多10字  密碼最少6碼最多15碼
    if len(obj.username) < 2 or len(obj.username) > 20:
        return json.jsonify(errors.e1002)
    if len(obj.password) < 6 or len(obj.password) > 20:
        return json.jsonify(errors.e1003)
    #3.1. 更新產品
    hashed_password = bcrypt.hashpw(obj.password.encode('utf-8'), bcrypt.gensalt())
    # 3.1缺少未檢查username是否重複倒置sql error
    s = datahelper.update_user(user_id, obj.username, hashed_password.decode('utf-8'))
    #3.2. 提交
    g.cursor().connection.commit()
   #4. 回傳產品
    return json.jsonify(make_data_result(s))


#刪除資料
@blueprint.route('/<user_id>', methods=["DELETE"])
def delete_user(user_id):
    #1. 解析JSON
    #1.1. 解析todo_id為int
    try:
        user_id = int(user_id)
    except:
        pass
    #2. 驗證資料
    #2.1. 驗證user_id是否存在
    if  isinstance(user_id, int) == False or \
          datahelper.is_user_id_existed(user_id) == False:
        return json.jsonify(errors.e4001) 
    #3. 刪除資料
    #3.1. 刪除資料
    success = datahelper.delete_user(user_id)
    #3.2. 提交
    g.cursor().connection.commit()
    #4. 回傳是否成功刪除
    return json.jsonify(make_data_result({"success":success}))



#---------------------------------------------

#單筆搜尋
@blueprint.route('/<user_id>', methods=["GET"])
def get_user(user_id):
    #1. 解析JSON或參數
    #1.1. 解析user_id為int
    try:
        user_id = int(user_id)
    except:
        pass
    #2. 驗證資料
    #2.1. 驗證user_id是否存在
    if  isinstance(user_id, int) == False or \
          datahelper.is_user_id_existed(user_id) == False:
        return json.jsonify(errors.e2001)
    #3. 取的單筆搜索資料
    s = datahelper.get_user(user_id)
   #4. 回傳資料
    return json.jsonify(make_data_result(s))
