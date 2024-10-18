## **1: Todo List API**

\*\*功能\*\*：創建一個簡單的待辦事項（Todo List）API，允許用戶新增、更新、刪除及查詢待辦事項。

\#### 要求：

| method | path | Function |
| --- | --- | --- |
| GET | /users/\<user\_id>/todos | 回傳所有待辦事項的列表。 |
| GET | _/users/\<user\_id>/todos/\<todo\_id>_ | 查詢單個待辦事項的詳細信息。 |
| POST | /users`/<user_id>/todos` | 新增一個待辦事項（傳入 JSON 格式，包含 \`title\` 和 \`description\`）。 |
| PUT | /users/\<user\_id>/todos | 更新現有的待辦事項。 |
| DELETE | /users/\<user\_id>/todos/\<todo\_id> | 刪除特定的待辦事項。 |

## 2: 使用者管理系統 API

\*\*功能\*\*：建立一個簡單的使用者管理系統 API，實現使用者的註冊、查詢和更新。

\#### 要求：

| method | path | Function |
| --- | --- | --- |
| GET | /users | 獲取所有註冊用戶的列表,(裝飾器判斷登入狀態,登入帳號才可使用) |
| GET | /users/\<user\_id> | 查詢特定使用者的資料。 |
| POST | /users/signup | 用戶註冊 password使用hash加密，sql儲存用戶資訊（傳入 \`username\` 和 \`password\`） |
| POST | /users/signin | 用戶登入 username存入session\['useranme'\]  （傳入 \`username\` 和 \`password\`） |
| POST | /users/signout | 用戶登出,移除session\['username'\] |
| PUT | /users/\<user\_id> | 更新使用者資料（傳入 \`username\` 和 \`password\`）。 |
| DELETE | /users/\<user\_id> | 刪除使用者資料。 |

### 3: 簡易書籍管理 API

\*\*功能\*\*：創建一個書籍管理系統 API，管理書籍的基本信息。

\#### 要求：

| method | path | Function |
| --- | --- | --- |
| GET | /books | 獲取所有書籍的列表。 |
| GET | /books/\<book\_id> | 查詢單本書籍的詳細信息 |
| GET | /\<user\_id>/book/\<book\_id> | 搜索 user\_id 是否擁有 book |
| GET | /\<user\_id>/book/get\_all | 搜索 user\_id 所有購買紀錄 |
| POST | /books | 新增書籍（傳入 \`title\`、\`author\`）。 |
| POST | /\<user\_id>/book/\<book\_id> | 添加購買紀錄 (user\\\_id 購買了 book\\\_id) |
| PUT | /books/\<book\_id> | 更新書籍（傳入 \`title\`不可重複、\`author\`）的詳細信息。 |
| DELETE | /books/\<book\_id> | 刪除特定書籍。 |

## 4\. MYSQL

### 1.資料庫結構

![](https://github.com/duilelomo23/BooksSystem/blob/main/pictureSQL/%E5%A4%9A%E5%B0%8D%E5%A4%9A.png)

## 5 呼叫api範例

### 5.1.註冊

![](https://github.com/duilelomo23/BooksSystem/blob/main/picture/%E8%A8%BB%E5%86%8A.png)

### 5.2. 重複註冊

![](https://github.com/duilelomo23/BooksSystem/blob/main/picture/%E9%87%8D%E8%A4%87%E8%A8%BB%E5%86%8A.png)

### 5.3.登入

![](https://github.com/duilelomo23/BooksSystem/blob/main/picture/%E7%99%BB%E5%85%A5.png)

### 5.4.呼叫 get /users api   獲取所有使用者資料

![](https://33333.cdn.cke-cs.com/kSW7V9NHUXugvhoQeFaf/images/6906b05c94e05c28a9cb430acefbe1baf9c90a5a09f50d76.png)

### 5.5. 呼叫 get /user\_id/get\_all  獲取user\_id所有購買紀錄資料

![](https://github.com/duilelomo23/BooksSystem/blob/main/picture/%E7%8D%B2%E5%8F%96user%E6%89%80%E6%9C%89%E8%B3%BC%E8%B2%B7%E7%B4%80%E9%8C%84%E5%A4%9A%E5%B0%8D%E5%A4%9A%E9%97%9C%E8%81%AF.png)

### 5.6.登出

![](https://github.com/duilelomo23/BooksSystem/blob/main/picture/%E7%99%BB%E5%87%BA.png)

### 5.7.未登入呼叫API retrun error

![](https://github.com/duilelomo23/BooksSystem/blob/main/picture/%E6%9C%AA%E7%99%BB%E5%85%A5%E5%91%BC%E5%8F%ABAPI.png)

## 6.安裝和執行

### 6.1  mysql

### 1.下載sql檔案後開啟

![](https://33333.cdn.cke-cs.com/kSW7V9NHUXugvhoQeFaf/images/4bcd8c6a77005479265c2c0be3a2609699f671bd1517668b.png)

### 2\. 開啟MYSQL Workbench並登入

![](https://github.com/duilelomo23/BooksSystem/blob/main/pictureSQL/%E7%99%BB%E5%85%A5workbench.png)

### 3.複製todo\_db.sql所有sql碼

![](https://github.com/duilelomo23/BooksSystem/blob/main/pictureSQL/%E8%A4%87%E8%A3%BD%E6%89%80%E6%9C%89sql%E7%A2%BC.png)

### 4.創建todo\_db資料庫

![](https://github.com/duilelomo23/BooksSystem/blob/main/pictureSQL/%E6%96%B0%E5%A2%9Etodo_db.png)

### 5.在資料庫空白處點右鍵刷新

![](https://github.com/duilelomo23/BooksSystem/blob/main/pictureSQL/%E5%88%B7%E6%96%B0.png)

### 6\. 對資料表點選右鍵選擇Select Rows獲取測試資料

![](https://github.com/duilelomo23/BooksSystem/blob/main/pictureSQL/%E7%8D%B2%E5%8F%96%E6%B8%AC%E8%A9%A6%E8%B3%87%E6%96%99.png)

### 6.2 Python套件安裝

```plaintext
 pip install   Flask==3.0.3
 pip install PyMySQL==1.1.0  
 pip install dacite==1.8.1
```
### 6.2 執行api服務 執行restful目錄下的run.py
 python run.py
