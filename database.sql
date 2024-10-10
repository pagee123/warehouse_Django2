INSERT INTO myapp_producttype (name) VALUES 
('電子產品'),
('家具'),
('運動用品'),
('食品');

INSERT INTO myapp_supplier (name, contact_info) VALUES
('Apple', 'apple@support.com'),
('IKEA', 'service@ikea.com'),
('Nike', 'support@nike.com');

-- 電子產品類型的商品
INSERT INTO myapp_product (barcode, product_name, arrival_date, quantity, product_type_id, description, supplier_id)
VALUES 
('1234567890', 'iPhone', '2023-10-01', 100, 1, '蘋果手機', 1),
('1234567891', 'MacBook', '2023-09-25', 50, 1, '蘋果筆電', 1),
('1234567892', 'AirPods', '2023-09-30', 200, 1, '蘋果無線耳機', 1),
('1234567893', 'iPad', '2023-10-03', 75, 1, '蘋果平板', 1),
('1234567894', 'Apple Watch', '2023-10-05', 80, 1, '蘋果智慧手錶', 1),
('1234567895', 'iMac', '2023-09-20', 20, 1, '蘋果桌上型電腦', 1),
('1234567896', 'Mac Mini', '2023-09-22', 40, 1, '蘋果迷你電腦', 1),
('1234567897', 'HomePod', '2023-09-27', 60, 1, '蘋果智能音箱', 1),
('1234567898', 'Magic Mouse', '2023-10-01', 120, 1, '蘋果滑鼠', 1),
('1234567899', 'Magic Keyboard', '2023-09-15', 110, 1, '蘋果鍵盤', 1);

-- 家具類型的商品
INSERT INTO myapp_product (barcode, product_name, arrival_date, quantity, product_type_id, description, supplier_id)
VALUES 
('2234567890', '桌子', '2023-09-10', 30, 2, 'IKEA 木製桌子', 2),
('2234567891', '椅子', '2023-09-12', 100, 2, 'IKEA 金屬椅子', 2),
('2234567892', '沙發', '2023-09-14', 25, 2, 'IKEA 布藝沙發', 2),
('2234567893', '衣櫃', '2023-09-16', 15, 2, 'IKEA 木製衣櫃', 2),
('2234567894', '床', '2023-09-18', 20, 2, 'IKEA 雙人床', 2),
('2234567895', '書架', '2023-09-20', 40, 2, 'IKEA 書架', 2),
('2234567896', '茶几', '2023-09-22', 50, 2, 'IKEA 小茶几', 2),
('2234567897', '電視櫃', '2023-09-24', 35, 2, 'IKEA 電視櫃', 2),
('2234567898', '鞋櫃', '2023-09-26', 60, 2, 'IKEA 鞋櫃', 2),
('2234567899', '床頭櫃', '2023-09-28', 25, 2, 'IKEA 床頭櫃', 2);

-- 運動用品類型的商品
INSERT INTO myapp_product (barcode, product_name, arrival_date, quantity, product_type_id, description, supplier_id)
VALUES 
('3234567890', '跑鞋', '2023-10-01', 150, 3, 'Nike 跑鞋', 3),
('3234567891', '籃球', '2023-09-30', 100, 3, 'Nike 籃球', 3),
('3234567892', '運動手環', '2023-09-28', 120, 3, 'Nike 運動手環', 3),
('3234567893', '運動短褲', '2023-09-25', 80, 3, 'Nike 運動短褲', 3),
('3234567894', '運動T恤', '2023-09-24', 90, 3, 'Nike 運動T恤', 3),
('3234567895', '籃球鞋', '2023-09-23', 130, 3, 'Nike 籃球鞋', 3),
('3234567896', '足球鞋', '2023-09-22', 110, 3, 'Nike 足球鞋', 3),
('3234567897', '健身包', '2023-09-20', 60, 3, 'Nike 健身包', 3),
('3234567898', '運動帽', '2023-09-18', 200, 3, 'Nike 運動帽', 3),
('3234567899', '運動背心', '2023-09-15', 85, 3, 'Nike 運動背心', 3);

-- 食品類型的商品
INSERT INTO myapp_product (barcode, product_name, arrival_date, quantity, product_type_id, description, supplier_id)
VALUES 
('4234567890', '蘋果', '2023-10-02', 300, 4, '新鮮蘋果', 2),
('4234567891', '香蕉', '2023-09-30', 200, 4, '新鮮香蕉', 2),
('4234567892', '橙子', '2023-09-28', 150, 4, '新鮮橙子', 2),
('4234567893', '牛奶', '2023-09-25', 100, 4, '全脂牛奶', 2),
('4234567894', '雞蛋', '2023-09-24', 400, 4, '自由放養雞蛋', 2),
('4234567895', '牛排', '2023-09-22', 75, 4, '牛肉排', 2),
('4234567896', '魚', '2023-09-20', 50, 4, '新鮮魚類', 2),
('4234567897', '雞肉', '2023-09-18', 100, 4, '有機雞肉', 2),
('4234567898', '面包', '2023-09-15', 200, 4, '全麥面包', 2),
('4234567899', '巧克力', '2023-09-12', 120, 4, '黑巧克力', 2);


INSERT INTO myapp_productimage (product_id, image)
VALUES 
(1, 'images/iPhone.png'),
(2, 'images/macbook.png'),
(3, 'images/Airpods.png'),
(4, 'images/ipad.png'),
(5, 'images/apple_watch.png'),
(6, 'images/iMac.png'),
(7, 'images/macmini.png'),
(8, 'images/HomePod.png'),
(9, 'images/Apple_Magic_Mouse.png'),
(10, 'images/Apple_Magic_Keyboard.png'),
(11, 'images/桌子.png'),
(12, 'images/椅子.png'),
(13, 'images/沙發.png'),
(14, 'images/衣櫃.png'),
(15, 'images/床.png'),
(16, 'images/書架.png'),
(17, 'images/茶几.png'),
(18, 'images/電視櫃.png'),
(19, 'images/鞋櫃.png'),
(20, 'images/床頭櫃.png'),
(21, 'images/跑鞋.png'),
(22, 'images/籃球.png'),
(23, 'images/運動手環.png'),
(24, 'images/運動短褲.png'),
(25, 'images/運動T恤.png'),
(26, 'images/籃球鞋.png'),
(27, 'images/足球鞋.png'),
(28, 'images/健身包.png'),
(29, 'images/運動帽.png'),
(30, 'images/運動背心.png'),
(31, 'images/蘋果.png'),
(32, 'images/香蕉.png'),
(33, 'images/柳橙.png'),
(34, 'images/牛奶.png'),
(35, 'images/雞蛋.png'),
(36, 'images/牛排.png'),
(37, 'images/食用魚.png'),
(38, 'images/雞肉.png'),
(39, 'images/麵包.png'),
(40, 'images/巧克力.png'),
