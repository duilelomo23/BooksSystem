from results import make_error_result

# #給unregister API使用的error
# e2001 = make_error_result("e2001","此客戶名字不存在")

#給create_product API使用的error
e1001 = make_error_result("e1001","title不可為空白")
e1002 = make_error_result("e1002","title已存在")
e1003 = make_error_result("e1003", "請輸入使用者ID")


#給get_todo API使用的error
e2001 = make_error_result("e2001","todo_id不存在")
e2002 = make_error_result("e2002", "user沒有購買紀錄")
#給update API使用的error
e3001 = make_error_result("e3001","title已存在")
e3002 = make_error_result("e3002","title不可為空白")

#給delete API使用的error
e4001 = make_error_result("e4001","todo_id不存在")