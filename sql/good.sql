/*
Navicat MySQL Data Transfer

Source Server         : locallhost
Source Server Version : 50614
Source Host           : localhost:3306
Source Database       : vms

Target Server Type    : MYSQL
Target Server Version : 50614
File Encoding         : 65001

Date: 2018-08-09 17:06:12
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for good
-- ----------------------------
DROP TABLE IF EXISTS `good`;
CREATE TABLE `good` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(30) NOT NULL,
  `good_category_id` int(11) NOT NULL,
  `price` int(11) NOT NULL,
  `uploadtime` datetime DEFAULT NULL,
  `status` int(10) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of good
-- ----------------------------
INSERT INTO `good` VALUES ('1', '脉动', '1', '5', '2018-08-09 16:41:57', '0');
INSERT INTO `good` VALUES ('2', '酷儿', '1', '4', '2018-08-09 16:41:59', '11');
INSERT INTO `good` VALUES ('3', '雪花', '2', '3', '2018-08-09 16:58:36', '11');
INSERT INTO `good` VALUES ('4', '寿司', '3', '15', '2018-08-09 16:58:40', '13');
INSERT INTO `good` VALUES ('5', '牛肉', '4', '25', '2018-08-09 16:58:42', '21');
INSERT INTO `good` VALUES ('6', '土豆', '4', '6', '2018-08-09 16:41:54', '1');
