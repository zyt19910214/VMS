/*
Navicat MySQL Data Transfer

Source Server         : locallhost
Source Server Version : 50614
Source Host           : localhost:3306
Source Database       : vms

Target Server Type    : MYSQL
Target Server Version : 50614
File Encoding         : 65001

Date: 2018-08-16 17:48:42
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for vip_order
-- ----------------------------
DROP TABLE IF EXISTS `vip_order`;
CREATE TABLE `vip_order` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `phone` varchar(11) NOT NULL,
  `order_serial_number` varchar(20) NOT NULL,
  `order_status` tinyint(1) NOT NULL,
  `order_category_id` int(11) NOT NULL,
  `create_time` datetime NOT NULL,
  `notes` varchar(255) DEFAULT NULL,
  `lay_value` float(11,1) NOT NULL,
  `free_value` float(11,1) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8 ROW_FORMAT=COMPACT;

-- ----------------------------
-- Records of vip_order
-- ----------------------------
