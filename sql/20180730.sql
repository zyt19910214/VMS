/*
* @Author: Marte
* @Date:   2018-07-30 23:57:46
* @Last Modified by:   Marte
* @Last Modified time: 2018-07-31 00:33:29
*/
CREATE DATABASE vms;

CREATE TABLE vms.vip_person(
   id INT NOT NULL AUTO_INCREMENT,
   vip_name VARCHAR(20) NOT NULL,
   vip_sex TINYINT(1) NOT NULL,
   vip_phone NUMERIC(11) NOT NULL,
   vip_note VARCHAR(100),
   vip_add_date DATETIME,

   PRIMARY KEY ( id )
);

CREATE TABLE vms.vip_person_point(
   id INT NOT NULL AUTO_INCREMENT,
   vip_point FLOAT(6,1) NOT NULL,
   last_update_time DATETIME,
   reset_time DATETIME,
   PRIMARY KEY ( id )
);