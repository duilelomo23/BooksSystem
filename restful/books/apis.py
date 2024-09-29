from flask import Blueprint, request, json, g
from dacite import from_dict
from dacite_config import config
from books import dataclasses, datahelper, errors
from results import make_data_result
from datetime import datetime

blueprint = Blueprint("books", import_name = "books")


#查詢所有資料
@blueprint.route('', methods=["GET"])
def get_books():
    #1. 取得產品
    s = datahelper.get_books()
   #2. 回傳產品
    return json.jsonify(make_data_result(s))

#查詢單筆資料
@blueprint.route('/<book_id>', methods=["GET"])
def get_book(book_id):
    #1. 解析book_id為int
    try:
        book_id = int(book_id)
    except:
        pass
    #2. 驗證資料
    #2.1. 驗證book_id是否存在
    if  isinstance(book_id, int) == False or \
          datahelper.is_book_id_existed(book_id) == False:
        return json.jsonify(errors.e2001)
    #3. 取得產品
    s = datahelper.get_book(book_id)
   #4. 回傳產品
    return json.jsonify(make_data_result(s))

#新增
@blueprint.route('', methods=["POST"])
def create_book():  
    #1. 解析JSON或參數
    x = json.loads(request.data)
    obj = from_dict(dataclasses.CreateBooks, x, config=config)
    #2. 驗證資料
    #2.1. title, author不可為空白
    if obj.title == None  or len(obj.author) == 0:
        return json.jsonify(errors.e1001)
    #3. 建立產品
    #3.1. 新增資料
    s = datahelper.create_book(obj.title, obj.author, datetime.now())
    # title存在回傳false
    if s == False:
        return json.jsonify(errors.e1002)
    #3.2. 提交
    g.cursor().connection.commit()
   #4. 回傳產品
    return json.jsonify(make_data_result(s))

#修改
@blueprint.route('/<book_id>', methods=["PUT"])
def update_book(book_id):
    #1. 解析JSON或參數
    #1.1. 解析JSON
    x = json.loads(request.data)
    obj = from_dict(dataclasses.UpdateBooks, x, config=config)
    #1.2. 解析todo_id為int
    try:
        book_id = int(book_id)
    except:
        pass

    #2. 驗證資料
    #2.1. 驗證todo_id是否存在
    if  isinstance(book_id, int) == False or \
          datahelper.is_book_id_existed(book_id) == False:
        return json.jsonify(errors.e3001) 
    #2.2. title不可為空白
    if obj.title == None or len(obj.author.strip()) == 0:
        return json.jsonify(errors.e3002)
    #3. 更新產品
    #3.1. 更新產品
    s = datahelper.update_book(book_id, obj.title, obj.author, datetime.now())
    if s == False:
        return json.jsonify(errors.e3001)
    #3.2. 提交
    g.cursor().connection.commit()
   #4. 回傳產品
    return json.jsonify(make_data_result(s))

#刪除
@blueprint.route('/<book_id>', methods=["DELETE"])
def delete_book(book_id):

    #1. 解析JSON
    #1.1. 解析todo_id為int
    try:
        book_id = int(book_id)
    except:
        pass
    #2. 驗證資料
    #2.1. 驗證todo_id是否存在
    if  isinstance(book_id, int) == False or \
          datahelper.is_book_id_existed(book_id) == False:
        return json.jsonify(errors.e4001) 
    #3. 刪除資料
    #3.1. 刪除資料
    success = datahelper.delete_book(book_id)
    #3.2. 提交
    g.cursor().connection.commit()
    #4. 回傳是否成功刪除
    return json.jsonify(make_data_result({"success":success}))



#------------------------------------------------------------------------------------------------------
#user_book api

#搜索 user_id 是否擁有 book_id
@blueprint.route('/<user_id>/book/<book_id>', methods=["GET"])
def get_user_updata_book_record(user_id, book_id):

    #1. 解析JSON或參數
    #1.1. 解析todo_id為int
    try:
        book_id = int(book_id)
        user_id = int(user_id)
        print(book_id, user_id,'*------------------------------')
    except:
        pass
        
    #2. 驗證資料
    #2.1. 驗證todo_id是否存在
    if  isinstance(book_id, int) == False or \
        isinstance(user_id, int) == False:
        return json.jsonify(errors.e2002)
    if datahelper.serch_book_and_user_id_update_existed(user_id, book_id) == 0:
        return json.jsonify(errors.e2002)

    #3. 取得產品
    s = datahelper.serch_user_book_date(user_id ,book_id)
   #4. 回傳產品

    return json.jsonify(make_data_result(s))


#搜索user_id 購買所有紀錄
@blueprint.route('/<user_id>/book/get_all', methods=["GET"])
def get_user_all_book_record(user_id):

    #1. 解析JSON或參數
    #1.1. 解析todo_id為int
    try:
        user_id = int(user_id)
    except:
        pass

    #2. 驗證資料
    #2.1. 驗證todo_id是否存在
    if  isinstance(user_id, int) == False or \
        datahelper.serch_book_and_user_id_update_existed(user_id) == False:
        return json.jsonify(errors.e2002)
    #3. 取得產品
    s = datahelper.serch_user_all_book(user_id)
   #4. 回傳產品
    return json.jsonify(make_data_result(s))


#新增購買紀錄  
@blueprint.route('/<user_id>/book/<book_id>', methods=["POST"])
def create_update_book_record(user_id, book_id):
    #1. 解析JSON或參數
    # x = json.loads(request.data)
    # obj = from_dict(dataclasses.CreateUser, x, config=config)
    #2. 驗證資料
    #1.1. 解析todo_id為int
    try:
        user_id = int(user_id)
        book_id = int(book_id)
    except:
        pass
    #3. 建立產品
    #3.1. 建立產品
    s = datahelper.create_update_book_record(user_id, book_id, datetime.now())


    #3.2. 提交
    g.cursor().connection.commit()
   #4. 回傳產品
    return json.jsonify(make_data_result(s))

