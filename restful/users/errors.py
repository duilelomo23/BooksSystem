from results import make_error_result

# #給unregister API使用的error
# e2001 = make_error_result("e2001","此客戶名字不存在")

#給create_user API使用的error
e1001 = make_error_result("e1001","使用者名稱或密碼不可為空白")
e1002 = make_error_result("e1002","使用者名稱最少2個字或不可超過20個字")
e1003 = make_error_result("e1003","使用者密碼最少6碼最多20碼")
e1004 = make_error_result("e1004","密碼只可使用數字或英文")
e1005 = make_error_result("e1005", "username已存在")

#給get_user API使用的error
e2001 = make_error_result("e2001","user_id不存在")
e2002 = make_error_result("e2002", "登入才可呼叫API")

#給update API使用的error
e3001 = make_error_result("e3001","user_id不存在")
e3002 = make_error_result("e3002","username不可為空白")

#給delete API使用的error
e4001 = make_error_result("e4001","user_id不存在")

#給post 登入api
e5001 = make_error_result("e5001", "密碼錯誤")

