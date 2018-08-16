CREATE DATABASE `Python`;
USE Python;
GRANT ALL ON *.* TO python@localhost IDENTIFIED BY '1234';

CREATE TABLE employee(
       ID int(10) NOT NULL auto_increment,
       FirstName varchar(12),
       LastName varchar(12),
       Gender char(1),
       Email varchar(60),
       Tel varchar(12),
       PRIMARY KEY ID(ID)
);

INSERT INTO employee (
       ID, FirstName, LastName, Gender, Email, Tel)
       VALUES (
       null, 'SIN YI', 'LIN', 'F', 'sinyi@gmail.com', '23456789'
       );
INSERT INTO employee (
       ID, FirstName, LastName, Gender, Email, Tel)
       VALUES (
       null, 'JHIH WEI', 'GUO', 'M', 'jhihwel@gmail.com', '22334455'
       );
INSERT INTO employee (
       ID, FirstName, LastName, Gender, Email, Tel)
       VALUES (
       null, 'JIAN HONG', 'WANG', 'M', 'jianhong@gmail.com', '23456677'
       );
INSERT INTO employee (
       ID, FirstName, LastName, Gender, Email, Tel)
       VALUES (
       null, 'PEI JYUN', 'CHEN', 'F', 'peijyun@gmail.com', '22345678'
       );
INSERT INTO employee (
       ID, FirstName, LastName, Gender, Email, Tel)
       VALUES (
       null, 'JIA YING', 'HU', 'F', 'jiaying@gmail.com', '23875432'
       );