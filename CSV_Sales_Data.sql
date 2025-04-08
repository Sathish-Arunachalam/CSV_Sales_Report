CREATE DATABASE  P2_sales_db;

USE P2_sales_db;
show P2_sales_db;

CREATE TABLE P2_sales_data (
    id INT AUTO_INCREMENT PRIMARY KEY,
    product VARCHAR(50),
    region VARCHAR(50),
    sales_rep VARCHAR(50),
    quantity INT,
    price DECIMAL(10,2),
    sale_date DATE
);

select * from P2_sales_data