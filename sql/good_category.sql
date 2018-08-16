/*
Navicat MySQL Data Transfer

Source Server         : locallhost
Source Server Version : 50614
Source Host           : localhost:3306
Source Database       : vms

Target Server Type    : MYSQL
Target Server Version : 50614
File Encoding         : 65001

Date: 2018-08-16 17:48:25
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for good_category
-- ----------------------------
DROP TABLE IF EXISTS `good_category`;
CREATE TABLE `good_category` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(30) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of good_category
-- ----------------------------
INSERT INTO `good_category` VALUES ('1', '饮料');
INSERT INTO `good_category` VALUES ('2', '酒水');
INSERT INTO `good_category` VALUES ('3', '简餐');
INSERT INTO `good_category` VALUES ('4', '火锅');
