from flask import Blueprint, request, json, g
from dacite import from_dict
from dacite_config import config
from todos import dataclasses, datahelper, errors
from results import make_data_result

blueprint = Blueprint("todos", import_name = "todos")


#獲取所有todo
@blueprint.route('/<user_id>/todos', methods=["GET"])
def get_todos(user_id):
    #1. 取得產品
    s = datahelper.get_todos()
   #2. 回傳產品
    return json.jsonify(make_data_result(s))


#新增todo
@blueprint.route('/<user_id>/todos', methods=["POST"])
def create_todo(user_id):
    #1. 解析JSON或參數
    x = json.loads(request.data)
    #1.1 x json轉成obj
    obj = from_dict(dataclasses.CreateTodo, x, config=config)
    #2. 驗證資料
    #2.1. title不可為空白
    if not obj.title:
        return json.jsonify(errors.e1001)
    #3. 建立產品
    #3.1. 建立產品
    s = datahelper.create_todo(user_id, obj.title, obj.description)
    #3.2. 提交sql
    g.cursor().connection.commit()
   #4. 回傳產品
    return json.jsonify(make_data_result(s))

#更新todo
@blueprint.route('/<user_id>/todos/<todo_id>', methods=["PUT"])
def update_todo(user_id, todo_id):
    #1. 解析JSON或參數
    #1.1. 解析JSON
    x = json.loads(request.data)
    obj = from_dict(dataclasses.UpdateTodo, x, config=config)
    #1.3. 解析todo_id為int
    try:
        todo_id = int(todo_id)
    except:
        pass

    #2. 驗證資料
    #2.1. 驗證todo_id是否存在
    if  isinstance(todo_id, int) == False or \
          datahelper.is_todo_id_existed(todo_id) == False:
        return json.jsonify(errors.e3001) 
    #2.2. title不可為空白
    if obj.title == None or len(obj.title) == 0:
        return json.jsonify(errors.e3002)
    #3. 更新產品
    #3.1. 更新產品
    s = datahelper.update_todo(todo_id, user_id, obj.title, obj.description)
    #3.2. 提交sql
    g.cursor().connection.commit()
   #4. 回傳產品
    return json.jsonify(make_data_result(s))

#刪除todo
@blueprint.route('/<user_id>/todos/<todo_id>', methods=["DELETE"])
def delete_todo(user_id, todo_id):

    #1.1. 解析todo_id為int
    try:
        todo_id = int(todo_id)
    except:
        pass
    #2. 驗證資料
    #2.1. 驗證todo_id是否存在
    if  isinstance(todo_id, int) == False or \
          datahelper.is_todo_id_existed(todo_id) == False:
        return json.jsonify(errors.e4001) 
    #3. 刪除資料
    #3.1. 刪除資料
    success = datahelper.delete_todo(todo_id)
    #3.2. 提交
    g.cursor().connection.commit()
    #4. 回傳是否成功刪除
    return json.jsonify(make_data_result({"success":success}))




#------------------------------------------------------------

#獲取單筆todo
@blueprint.route('/<user_id>/todos/<todo_id>', methods=["GET"])
def get_todo(user_id, todo_id):
    #1. 解析JSON或參數
    #1.1. 解析todo_id為int
    try:
        todo_id = int(todo_id)
    except:
        pass
    #2. 驗證資料
    #2.1. 驗證todo_id是否存在
    if  isinstance(todo_id, int) == False or \
          datahelper.is_todo_id_existed(todo_id) == False:
        return json.jsonify(errors.e2001)
    #3. 取得產品
    s = datahelper.get_todo(todo_id)
   #4. 回傳產品
    return json.jsonify(make_data_result(s))


#列出指定user_id所有待辦事項 
@blueprint.route('/<user_id>/todos/<todo_id>/get_user_todos', methods=["GET"])
def is_user_id_existed_todos(user_id, todo_id):
    #1. 解析JSON或參數
    #1.1. 解析user_id為int
    try:
        user_id = int(user_id)
    except:
        pass
    #2. 驗證資料
    #2.1. 驗證user_id是否存在
    if  isinstance(user_id, int) == False or \
          datahelper.is_user_id_existed_todos(user_id) == False:
        return json.jsonify(errors.e2002)
    #3. 取得產品
    s = datahelper.get_user_todo_id(user_id)
   #4. 回傳產品
    return json.jsonify(make_data_result(s))