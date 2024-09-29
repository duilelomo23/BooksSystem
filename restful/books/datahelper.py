from flask import g

# def add_customer(c):
#     db.append(c)

#查詢所有
def get_books():
    cur = g.cursor()
    cur.execute(
        '''
        select * from book
        '''
    )
    ret_dicts = cur.fetchall()

    return ret_dicts

#查詢book_id單筆
def get_book(book_id):
    cur = g.cursor()
    cur.execute(
        '''
        select * from book where book_id=%s
        ''',
        (book_id)
    )
    ret_dict = cur.fetchone()

    return ret_dict

#新增
def create_book(title, author, year):
    cur = g.cursor()
    cur.execute(
        '''
        select * from book where title = %s
        ''',
        (title)
    )
    books_title = cur.fetchone()
    if books_title != None:
        return False


    cur.execute(
        '''
        insert into book
        (title, author, year)
        values
        (%s, %s, %s)  
        ''',
        (title, author, year)
    )
    new_id = cur.lastrowid
    cur.execute(
        '''
        select * from book where book_id = %s
        ''',
        (new_id)
    )
    ret_dict = cur.fetchone()

    return ret_dict

#修改
def update_book(book_id, title, author, year):
    cur = g.cursor()
    cur.execute(
        '''
        select * from book where title = %s
        ''',
        (title)
    )
    books_title = cur.fetchone()
    if books_title != None:
        return False
    

    cur.execute(
        '''
        update book
        set title=%s, author=%s, year=%s
        where book_id=%s 
        ''',
        (title, author, year, book_id)
    )
    cur.execute(
        '''
        select * from book where book_id = %s
        ''',
        (book_id)
    )
    ret_dict = cur.fetchone()

    return ret_dict

#刪除
def delete_book(book_id):

    cur = g.cursor()
    cur.execute(
            '''
            delete from book where book_id = %s
            ''',
            (book_id)
        )
 
    rowcount = cur.rowcount
    
    return rowcount > 0


#判斷 book_id 是否存在 不存在return false
def is_book_id_existed(book_id):
    cur = g.cursor()
    cur.execute(
        '''
        select * from book where book_id=%s
        ''',
        (book_id)
    )
    ret_dict = cur.fetchone()

    return ret_dict != None

#搜尋update_book_record是否存在user id and book id
def serch_book_and_user_id_update_existed(user_id):
    cur = g.cursor()
    # cur.execute(
    #     '''
    #     select * from update_book_record where user_id=%s
    #     ''',
    #     (user_id)
    # )
    # if cur.fetchone() == None:
    #     return False

    cur.execute(
        '''
        SELECT COUNT(*) AS record_count
        FROM update_book_record
        WHERE user_id = %s;
        ''',
        (user_id)
    )
    ret_dict = cur.fetchone()

    return ret_dict['record_count']

#搜索 user_id 所有購買紀錄
def serch_user_all_book(user_id):
    cur = g.cursor()
    cur.execute(
        '''
        select user.user_id, user.username, book.title, book.author, update_book_record.update_date
        from update_book_record 
        inner join user on user.user_id = update_book_record.user_id 
        inner join book on book.book_id = update_book_record.book_id
        where update_book_record.user_id=%s
        ''',
        (user_id)
    )
    ret_dict = cur.fetchall()
    return ret_dict

#新增購買紀錄
def create_update_book_record(user_id, book_id, year):
    cur = g.cursor()

    cur.execute(
        '''
        insert into update_book_record
        (user_id, book_id, update_date)
        values
        (%s, %s, %s)  
        ''',
        (user_id, book_id, year)
    )

    new_id = cur.lastrowid
    cur.execute(
        '''
        select user.user_id ,user.username, book.title, book.author, book.year, update_book_record.update_date
        from update_book_record 
        inner join user on user.user_id=update_book_record.user_id
        inner join book on book.book_id=update_book_record.book_id
        where update_book_record.user_book_id = %s
        ''',
        (new_id)
    )

    ret_dict = cur.fetchone()

    return ret_dict

#搜尋指定 user_id 所有購買紀錄
def serch_user_book_date(user_id ,book_id):
    cur = g.cursor()
    cur.execute(
        '''
        select user.user_id ,user.username , book.title ,book.author ,book.year ,update_book_record.book_id, update_book_record.update_date 
        from update_book_record 
        inner join user on user.user_id = update_book_record.user_id 
        inner join book on book.book_id = update_book_record.book_id
        where update_book_record.user_id=%s and update_book_record.book_id=%s
        ''',
        (user_id, book_id)
    )
    ret_dict = cur.fetchall()
    return ret_dict