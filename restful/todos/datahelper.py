from flask import g

# def add_customer(c):
#     db.append(c)




#搜索所有資料
def get_todos():
    cur = g.cursor()
    cur.execute(
        '''
        select * from todo
        '''
    )
    ret_dicts = cur.fetchall()

    return ret_dicts


#獲取單筆user_id todo資料
def get_todo(todo_id):
    cur = g.cursor()
    cur.execute(
        '''
        select * from todo where todo_id=%s
        ''',
        (todo_id)
    )
    ret_dict = cur.fetchone()

    return ret_dict


#新增
def create_todo(user_id, title, description):
    cur = g.cursor()
    cur.execute(
        '''
        insert into todo
        (user_id , title, description)
        values
        (%s, %s, %s)  
        ''',
        (user_id, title, description)
    )
    new_id = cur.lastrowid
    cur.execute(
        '''
        select * from todo where todo_id = %s
        ''',
        (new_id)
    )
    ret_dict = cur.fetchone()

    return ret_dict


#更新todo title description
def update_todo(todo_id, user_id, title, description):
    cur = g.cursor()
    cur.execute(
        '''
        update todo
        set user_id=%s, title=%s, description=%s 
        where todo_id=%s 
        ''',
        (user_id, title, description, todo_id)
    )
    cur.execute(
        '''
        select * from todo where todo_id = %s
        ''',
        (todo_id)
    )
    ret_dict = cur.fetchone()

    return ret_dict


#todo_id刪除資料
def delete_todo(todo_id):
    cur = g.cursor()
    cur.execute(
            '''
            delete from todo where todo_id = %s
            ''',
            (todo_id)
        )
 
    rowcount = cur.rowcount
    
    return rowcount > 0



#-------------------------------------------------


#搜索todo_id是否存在tood表
def is_todo_id_existed(todo_id):
    cur = g.cursor()
    cur.execute(
        '''
        select * from todo where todo_id=%s
        ''',
        (todo_id)
    )
    ret_dict = cur.fetchone()

    return ret_dict != None


#todos表  user_id 是否存在 不存在return false
def is_user_id_existed_todos(user_id):
    cur = g.cursor()
    cur.execute(
        '''
        select * from todo where user_id=%s
        ''',
        (user_id)
    )
    ret_dict = cur.fetchone()

    return ret_dict != None


#獲取user_id所有待辦事項
def get_user_todo_id(user_id):
    cur = g.cursor()
    cur.execute(
        '''
        select user.username, user.user_id, todo.title, todo.description
        from todo 
        inner join user on user.user_id = todo.user_id 
        where todo.user_id=%s
        ''',
        (user_id)
    )
    
    ret_dict = cur.fetchall()

    return ret_dict



