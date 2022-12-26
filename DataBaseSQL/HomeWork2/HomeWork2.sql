-- 1. Используя операторы языка SQL, создайте табличку “sales”. Заполните ее данными

CREATE TABLE sales 
(
	sale_id INT PRIMARY KEY AUTO_INCREMENT,
	phone_id INT NOT NULL,
	count INT NOT NULL,
	FOREIGN KEY (phone_id) REFERENCES phones (phone_id)
);

INSERT sales(phone_id, count)
VALUES (6, 30), (1, 16), (5, 100), (4, 11), (6, 70), (3, 1000), (4, 80), (2, 66), (4, 88), (6, 200);

-- 2. Сгруппируйте значений количества в 3 сегмента — меньше 100, 100-300 и больше 300.

SELECT sales_group, GROUP_CONCAT(model SEPARATOR ', ') AS models
FROM
	(SELECT phone_id, model, sales_total,
		(CASE
			WHEN sales_total<100 THEN "Мало продаж"
            WHEN sales_total>=100 AND sales_total<=300 THEN "Много продаж"
            ELSE "Очень много продаж"
        END) AS sales_group
	FROM
		(SELECT sales.phone_id, CONCAT(phones.vendor, " ", phones.model) AS model, SUM(sales.count) AS sales_total
		FROM sales, phones
		WHERE phones.phone_id = sales.phone_id
		GROUP BY phone_id) AS temp1) AS temp2
GROUP BY sales_group;


-- 3. Создайте таблицу “orders”, заполните ее значениями. Покажите “полный” статус заказа, используя оператор CASE

CREATE TABLE orders
(
	order_id INT PRIMARY KEY AUTO_INCREMENT,
	create_data TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
	update_data TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
	customer_name VARCHAR (100) NOT NULL,
	order_status INT NOT NULL DEFAULT 1 
);

INSERT orders(customer_name)
VALUES ("Вася Пупкин"), ("Билл Гейтс"), ("Иван Иванов"), ("Чингачгук"),
	("Карлсон"), ("Илон Маск"), ("Папа Карло"), ("Буратино"), ("Артемон");

UPDATE orders SET order_status=2 WHERE order_id=1;
UPDATE orders SET order_status=3 WHERE order_id=4;
UPDATE orders SET order_status=4 WHERE order_id=2;
UPDATE orders SET order_status=0 WHERE order_id=8;
UPDATE orders SET order_status=-1 WHERE order_id=6;

SELECT order_id, create_data, update_data, customer_name, 
(CASE
	WHEN order_status=1 THEN "Заказ формируется"
    WHEN order_status=0 THEN "Заказ завершен"
    WHEN order_status=2 THEN "Заказ подтвержден"
    WHEN order_status=3 THEN "Заказ оплачен"
    WHEN order_status=4 THEN "Заказ в доставке"
    WHEN order_status=-1 THEN "Заказ отменен"
    ELSE "Не верный статус"
END) AS full_status
FROM orders;

-- 4. Чем NULL отличается от 0?

-- NULL это пустое значение (в поле ничего не храниться), а 0 это конкретное значение полей числовых типов
