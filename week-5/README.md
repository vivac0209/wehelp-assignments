
<img width="338" alt="test1" src="https://user-images.githubusercontent.com/71447545/150743372-33d080e4-c06d-4aa0-8778-217527665065.png">
<img width="364" alt="test2" src="https://user-images.githubusercontent.com/71447545/150743381-f2a51aab-b2a8-4a69-b7f8-3965ec8b0b84.png">

要求三：SQL CRUD

1.用 INSERT 指令新增一筆資料到 member 資料表中，這筆資料的 username 和
password 欄位必須是 test。接著繼續新增至少 4 筆隨意的資料。

INSERT INTO `member` (id,name,username,password) VALUES(1,'matt','test','test');

INSERT INTO `member` (name,username,password,follower_count) VALUES('david','dv0124a','qqqqq',180);

INSERT INTO `member` (name,username,password) VALUES('viva','vc0124a','12345');

INSERT INTO `member` (name,username,password,follower_count) VALUES('johndoe','jd0124a','taiwan@2022',35);

INSERT INTO `member` (name,username,password,follower_count) VALUES('chen','chen0124a','2022!4',22);

<img width="462" alt="3-1" src="https://user-images.githubusercontent.com/71447545/150743393-dac9642b-902e-4b3f-af96-55480a4cc74c.png">

====================================================================================

2. 使用 SELECT 指令取得所有在 member 資料表中的會員資料。

SELECT * FROM `member`;

<img width="462" alt="3-1" src="https://user-images.githubusercontent.com/71447545/150743393-dac9642b-902e-4b3f-af96-55480a4cc74c.png">

====================================================================================

3. 使用 SELECT 指令取得所有在 member 資料表中的會員資料，並按照 time 欄位，由
近到遠排序。

SELECT * FROM `member` ORDER BY `time`;

<img width="349" alt="3-3" src="https://user-images.githubusercontent.com/71447545/150744840-5ba84f99-40e2-4ec7-8318-94a52a09e7c6.png">

由遠到近

SELECT * FROM `member` ORDER BY `time` DESC;

<img width="332" alt="3-3-spec" src="https://user-images.githubusercontent.com/71447545/150744972-73557a3b-811f-4fcd-9128-925fda2eeeed.png">

==================================================================================

4. 使用 SELECT 指令取得 member 資料表中第 2 ~ 4 共三筆資料，並按照 time 欄位，
由近到遠排序。( 並非編號 2、3、4 的資料，而是排序後的第 2 ~ 4 筆資料 )

SELECT * FROM `member` ORDER BY `time` LIMIT 1,3;

<img width="371" alt="3-4" src="https://user-images.githubusercontent.com/71447545/150745638-367ea466-c873-498e-8613-60b858c6e106.png">

==================================================================================

5. 使用 SELECT 指令取得欄位 username 是 test 的會員資料。

SELECT * FROM `member` WHERE `username` = 'test';

<img width="323" alt="3-5" src="https://user-images.githubusercontent.com/71447545/150745987-6746b959-c72b-4846-8b86-2e71840b8c68.png">

=================================================================================

6. 使用 SELECT 指令取得欄位 username 是 test、且欄位 password 也是 test 的資料。

SELECT * FROM `member` WHERE `username` = 'test' AND `password` = 'test';

<img width="347" alt="3-6" src="https://user-images.githubusercontent.com/71447545/150746226-9abe682e-9047-4e43-b77a-7693d29d609a.png">

================================================================================

7. 使用 UPDATE 指令更新欄位 username 是 test 的會員資料，將資料中的 name 欄位
改成 test2。

UPDATE `member`
SET `name` = 'test2'
WHERE `username` = 'test';

<img width="351" alt="3-7" src="https://user-images.githubusercontent.com/71447545/150746684-d0291f9c-52d8-48a0-b64a-6fc1539caf8d.png">

===============================================================================


要求四：SQL Aggregate Functions

1. 取得 member 資料表中，總共有幾筆資料 ( 幾位會員 )。

SELECT COUNT(*) FROM `member`;

<img width="190" alt="4-1" src="https://user-images.githubusercontent.com/71447545/150747285-387301f1-b94a-4759-a842-7ffd4b276ab6.png">

==============================================================================

2. 取得 member 資料表中，所有會員 follower_count 欄位的總和。

SELECT SUM(follower_count) FROM `member`;

<img width="259" alt="4-2" src="https://user-images.githubusercontent.com/71447545/150747702-885bd3cb-9877-4c8a-a92e-13055b38d62a.png">

===============================================================================

3. 取得 member 資料表中，所有會員 follower_count 欄位的平均數。

SELECT AVG(follower_count) FROM `member`;

<img width="217" alt="4-3" src="https://user-images.githubusercontent.com/71447545/150747879-12f1a907-ce5d-4b08-a4d0-cbd37a144851.png">

===============================================================================

要求五：SQL JOIN (Optional)

1. 在資料庫中，建立新資料表，取名字為 message。
2. 
<img width="376" alt="5" src="https://user-images.githubusercontent.com/71447545/150760512-bbb8e232-b4da-49da-b685-42932522a74e.png">

2. 使用 SELECT 搭配 JOIN 語法，取得所有留言，結果須包含留言者會員的姓名。

SELECT member.id, name, content
FROM `member`
JOIN `message`
ON member.id = member_id;

<img width="217" alt="5-1" src="https://user-images.githubusercontent.com/71447545/150762167-14960118-0851-457c-a41d-10612d8d3ccc.png">

3.使用 SELECT 搭配 JOIN 語法，取得 member 資料表中欄位 username 是 test 的所有
留言，資料中須包含留言者會員的姓名。

SELECT name,content
FROM `member`
JOIN `message`
ON username='test' AND member.id = member_id;

<img width="221" alt="5-2" src="https://user-images.githubusercontent.com/71447545/150763446-55fef412-dd35-4ecd-8c23-a435f021dfe6.png">


