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
| POST | \<user\_id>/book/\<book\_id> | 添加購買紀錄 (user\\\_id 購買了 book\\\_id) |
| PUT | /books/\<book\_id> | 更新書籍（傳入 \`title\`不可重複、\`author\`）的詳細信息。 |
| DELETE | /books/\<book\_id> | 刪除特定書籍。 |

## 4\. MYSQL

### 1.資料庫結構

![](https://33333.cdn.cke-cs.com/kSW7V9NHUXugvhoQeFaf/images/32bafc8c0b8b6240a3ad6ccdb4fd927528a6324bf03dd1e5.png)

## 5 呼叫api範例

### 5.1.註冊

![](https://33333.cdn.cke-cs.com/kSW7V9NHUXugvhoQeFaf/images/c4bdac17b26fef4c510a9b406af7548d379cfbd7a1afd4ce.png)

### 5.2. 重複註冊

![](https://33333.cdn.cke-cs.com/kSW7V9NHUXugvhoQeFaf/images/73dc68a082b57cda15873726290d9f982c89698b3cf5bddc.png)

### 5.3.登入

![](https://33333.cdn.cke-cs.com/kSW7V9NHUXugvhoQeFaf/images/3f86ef9a5eb01be95ff8a76e6ccf2e70f689f7c72f2f82f0.png)

### 5.4.呼叫 get /users api   獲取所有使用者資料

![](https://33333.cdn.cke-cs.com/kSW7V9NHUXugvhoQeFaf/images/6906b05c94e05c28a9cb430acefbe1baf9c90a5a09f50d76.png)

### 5.5. 呼叫 get /user\_id/get\_all  獲取user\_id所有購買紀錄資料

![](https://33333.cdn.cke-cs.com/kSW7V9NHUXugvhoQeFaf/images/2e8c259b6af745231161f99a33af83786a02eddd94bea0f6.png)

### 5.6.登出

![](https://33333.cdn.cke-cs.com/kSW7V9NHUXugvhoQeFaf/images/66fe9004b6f3af85909b093dbf33784950597520c047c25a.png)

### 5.7.未登入呼叫API retrun error

![](https://33333.cdn.cke-cs.com/kSW7V9NHUXugvhoQeFaf/images/5f99e8a1a26cb45ecb364bbf782e4430d365bcb8b6828bec.png)

## 6.安裝和執行

### 6.1  mysql

### 1.下載sql檔案後開啟

![](https://33333.cdn.cke-cs.com/kSW7V9NHUXugvhoQeFaf/images/4bcd8c6a77005479265c2c0be3a2609699f671bd1517668b.png)

### 2\. 開啟MYSQL Workbench並登入

![](https://33333.cdn.cke-cs.com/kSW7V9NHUXugvhoQeFaf/images/01efcfbc01abe3234a25e25bd50e9f3b245d94f3927ca52e.png)

### 3.複製todo\_db.sql所有sql碼

![](https://33333.cdn.cke-cs.com/kSW7V9NHUXugvhoQeFaf/images/108f934c7380e16653935e57fcc58f76c016a19540a380c7.png)

### 4.創建todo\_db資料庫

![](https://33333.cdn.cke-cs.com/kSW7V9NHUXugvhoQeFaf/images/dbcdb6d6a11c24745d3fb3b98e053d1cb567c523bd011a0c.png)

### 5.在資料庫空白處點右鍵刷新

![](https://33333.cdn.cke-cs.com/kSW7V9NHUXugvhoQeFaf/images/ba182017252a986edf1e0aee91df2d55670d2bfaf20c1363.png)

### 6\. 對資料表點選右鍵選擇Select Rows獲取測試資料

![](https://33333.cdn.cke-cs.com/kSW7V9NHUXugvhoQeFaf/images/2d6a95ef494ded18b1aaf4ada8e97189d76eb5eff5252e27.png)

### 6.2 Python套件安裝

```plaintext
pip install   Flask==3.0.3
 pip install PyMySQL==1.1.0  
 pip install dacite==1.8.1
```
### 6.2 執行api服務 執行restful目錄下的run.py
        python run.py
