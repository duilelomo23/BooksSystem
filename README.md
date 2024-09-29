### 練習題 1: Todo List API

**功能**：創建一個簡單的待辦事項（Todo List）API，允許用戶新增、更新、刪除及查詢待辦事項。

#### 要求：

1.  **GET** `**/<user_id>/todos**`：回傳所有待辦事項的列表。
2.  **GET** `**/<user_id>/todos/<todo_id>**`：查詢單個待辦事項的詳細信息。
3.  **POST** `**/<user_id>/todos**`：新增一個待辦事項（傳入 JSON 格式，包含 `title` 和 `description`）。
4.  **PUT** `**/<user_id>/todos**`：更新現有的待辦事項。
5.  **DELETE** `**//<user_id>/todos/<todo_id>**`：刪除特定的待辦事項。
    

### 練習題 2: 使用者管理系統 API

**功能**：建立一個簡單的使用者管理系統 API，實現使用者的註冊、查詢和更新。

#### 要求：

1.  **POST** `**/users/register**`：用戶註冊（傳入 `username` 和 `password`），儲存用戶資訊
2.  **POST** `**/users/login**`：用戶登入（傳入 `username` 和 `password`） username存入session['useranme']
3.  **POST** `**/users/register**`：用戶登出,移除session['username']
4.  **GET** `**/users**`：獲取所有註冊用戶的列表。
5.  **GET** `**/users/<int:id>**`：查詢特定使用者的資料。
6.  **PUT** `**/users/<int:id>**`：更新使用者資料（傳入 `username` 和 `password`）。
7.  **DELETE** `**/users/<int:id>**`：刪除使用者資料。

### 練習題 3: 簡易書籍管理 API

**功能**：創建一個書籍管理系統 API，管理書籍的基本信息。

#### 要求：

1.  **GET** `**/books**`：獲取所有書籍的列表。
2.  **GET** `**/books/<int:id>**`：查詢單本書籍的詳細信息。
3.  **POST** `**/books**`：新增書籍（傳入 `title`、`author`）。
4.  **PUT** `**/books/<int:id>**`：更新書籍（傳入 `title`不可重複、`author`）的詳細信息。
5.  **DELETE** `**/books/<int:id>**`：刪除特定書籍。
6.  **GET** `**/<user_id>/book/<book_id>**` 搜索 user\_id 是否擁有 book
7.  **GET** `**/<user_id>/book/get_all**`    搜索 user\_id 所有購買紀錄
8.  **POST** `**/<user_id>/book/<book_id>**` 添加購買紀錄 (user\_id 購買了 book\_id)
