/*
Navicat MySQL Data Transfer

Source Server         : locallhost
Source Server Version : 50614
Source Host           : localhost:3306
Source Database       : vms

Target Server Type    : MYSQL
Target Server Version : 50614
File Encoding         : 65001

Date: 2018-08-16 17:48:18
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
  `price` float(11,1) NOT NULL,
  `origin_price` float(11,1) NOT NULL,
  `uploadtime` datetime DEFAULT NULL,
  `status` int(10) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=30 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of good
-- ----------------------------
INSERT INTO `good` VALUES ('13', '可乐', '1', '3.0', '2.1', '2018-08-09 23:33:31', '24');
INSERT INTO `good` VALUES ('14', '雪碧', '1', '3.0', '2.1', '2018-08-09 23:33:44', '24');
INSERT INTO `good` VALUES ('15', '牛肉', '4', '25.0', '18.0', '2018-08-09 23:34:21', '0');
INSERT INTO `good` VALUES ('16', '凉皮', '3', '7.0', '3.5', '2018-08-09 23:34:40', '10');
INSERT INTO `good` VALUES ('17', '雪花', '2', '3.0', '2.0', '2018-08-09 23:35:01', '8');
INSERT INTO `good` VALUES ('18', '黑啤', '2', '4.0', '3.0', '2018-08-09 23:35:15', '12');
INSERT INTO `good` VALUES ('19', '牛奶', '1', '8.0', '6.0', '2018-08-09 23:35:36', '12');
INSERT INTO `good` VALUES ('20', '方便面', '3', '7.0', '4.0', '2018-08-09 23:52:33', '10');
INSERT INTO `good` VALUES ('25', '自制酸梅汤', '1', '8.0', '3.0', '2018-08-09 23:53:02', '30');
INSERT INTO `good` VALUES ('26', '自制柳橙汁', '1', '8.0', '3.0', '2018-08-09 23:53:15', '30');
INSERT INTO `good` VALUES ('27', '自制橙汁', '1', '8.0', '3.0', '2018-08-09 23:53:27', '30');
INSERT INTO `good` VALUES ('28', '自制草莓汁', '1', '8.0', '3.0', '2018-08-09 23:54:06', '30');
INSERT INTO `good` VALUES ('29', '豆皮', '4', '6.0', '2.0', '2018-08-09 23:54:41', '30');
