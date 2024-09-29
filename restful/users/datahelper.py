from flask import g

# def add_customer(c):
#     db.append(c)



#查詢user_id資料
def get_user(user_id):
    cur = g.cursor()
    cur.execute(
        '''
        select * from user where user_id=%s
        ''',
        (user_id)
    )
    ret_dict = cur.fetchone()

    return ret_dict


#新增資料
def create_user(username, password):
    cur = g.cursor()
    cur.execute(
        '''
        select * from user where username = %s
        ''',
        (username)
    )
    select_username = cur.fetchone()
    if select_username != None:
        return False

    cur.execute(
        '''
        insert into user
        (username, password)
        values
        (%s, %s)  
        ''',
        (username, password)
    )

    new_id = cur.lastrowid
    cur.execute(
        '''
        select * from user where user_id = %s
        ''',
        (new_id)
    )

    ret_dict = cur.fetchone()

    return ret_dict


#修改資料
def update_user(user_id, username, password):
    cur = g.cursor()
    cur.execute(
        
        '''
        update user
        set username=%s, password=%s
        where user_id=%s 
        ''',
        (username, password, user_id)
    )
    cur.execute(
        '''
        select * from user where user_id = %s
        ''',
        (user_id)
    )
    ret_dict = cur.fetchone()

    return ret_dict


#刪除user_id資料
def delete_user(user_id):

    cur = g.cursor()
    cur.execute(
            '''
            delete from user where user_id = %s
            ''',
            (user_id)
        )
 
    rowcount = cur.rowcount
    
    return rowcount > 0



#------------------------------------
#登入 usename pasword是否正確
def user_login(usename):
    cur = g.cursor()
    cur.execute(
        '''
        select * from user where username=%s
        ''',
        (usename)
    )
    ret_dict = cur.fetchone()

    return ret_dict

#查詢所有資料
def get_users():
    cur = g.cursor()
    cur.execute(
        '''
        select * from user
        '''
    )
    ret_dicts = cur.fetchall()

    return ret_dicts


#判斷user_id是否存在user表
def is_user_id_existed(user_id):
    cur = g.cursor()
    cur.execute(
        '''
        select * from user where user_id=%s
        ''',
        (user_id)
    )
    ret_dict = cur.fetchone()

    return ret_dict != None