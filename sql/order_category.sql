/*
Navicat MySQL Data Transfer

Source Server         : locallhost
Source Server Version : 50614
Source Host           : localhost:3306
Source Database       : vms

Target Server Type    : MYSQL
Target Server Version : 50614
File Encoding         : 65001

Date: 2018-08-16 17:48:33
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for order_category
-- ----------------------------
DROP TABLE IF EXISTS `order_category`;
CREATE TABLE `order_category` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(30) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of order_category
-- ----------------------------
INSERT INTO `order_category` VALUES ('1', '轰趴');
INSERT INTO `order_category` VALUES ('2', '麻将');
INSERT INTO `order_category` VALUES ('3', '狼人杀包场');
