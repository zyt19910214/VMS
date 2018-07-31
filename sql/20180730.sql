/*
* @Author: Marte
* @Date:   2018-07-30 23:57:46
* @Last Modified by:   Marte
* @Last Modified time: 2018-07-31 00:33:29
*/

CREATE DATABASE vms;

CREATE TABLE person(
   id INT NOT NULL AUTO_INCREMENT,
   name VARCHAR(20) NOT NULL,
   sex TINYINT(1) NOT NULL,
   phone NUMERIC(11) NOT NULL,
   note VARCHAR(100) default NULL,
   create_time DATETIME default NULL,
   resrver1 VARCHAR(50) default NULL,
   PRIMARY KEY ( id )
);

CREATE TABLE point_detail(
   id INT NOT NULL AUTO_INCREMENT,
   person_id INT NOT NULL,
   order_id INT NOT NULL,
   point FLOAT(6,1) NOT NULL,
   create_time DATETIME default NULL,
   PRIMARY KEY ( id )
);


CREATE TABLE good(
	id INT NOT NULL AUTO_INCREMENT,
	name VARCHAR(30) NOT NULL,
	good_category_id INT NOT NULL,
	price INT NOT NULL,
	PRIMARY KEY ( id )
);
CREATE TABLE good_category(
	id INT NOT NULL AUTO_INCREMENT,
	name VARCHAR(30) NOT NULL,
	PRIMARY KEY ( id )
);

CREATE TABLE server(
	id INT NOT NULL AUTO_INCREMENT,
	name VARCHAR(30) NOT NULL,
	server_category_id INT NOT NULL,
	price INT NOT NULL,
	PRIMARY KEY ( id )
);
CREATE TABLE server_category(
	id INT NOT NULL AUTO_INCREMENT,
	name VARCHAR(30) NOT NULL,
	PRIMARY KEY ( id )
);
CREATE TABLE order(
	id INT NOT NULL AUTO_INCREMENT,
	order_serial_number VARCHAR(20) NOT NULL,
	status  TINYINT(1) NOT NULL,
	order_category_id INT NOT NULL, 
	create_time DATETIME NOT NULL,
	all_value INT NOT NULL, 
	PRIMARY KEY ( id )
);

CREATE TABLE order_category(
	id INT NOT NULL AUTO_INCREMENT,
	name VARCHAR(30) NOT NULL,
	PRIMARY KEY ( id )
);

CREATE TABLE order_good_item(
	id INT NOT NULL AUTO_INCREMENT,
	order_id INT NOT NULL,
	person_id INT NOT NULL,
	good_id INT NOT NULL,
	good_count INT NOT NULL,
	PRIMARY KEY ( id )
);

CREATE TABLE order_server_item(
	id INT NOT NULL AUTO_INCREMENT,
	order_id INT NOT NULL,
	person_id INT NOT NULL,
	server_id INT NOT NULL,
	server_count INT NOT NULL,
	PRIMARY KEY ( id )
);