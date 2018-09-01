/*
 Navicat Premium Data Transfer

 Source Server         : vms
 Source Server Type    : MySQL
 Source Server Version : 50614
 Source Host           : localhost:3306
 Source Schema         : vms

 Target Server Type    : MySQL
 Target Server Version : 50614
 File Encoding         : 65001

 Date: 01/09/2018 18:19:55
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for server
-- ----------------------------
DROP TABLE IF EXISTS `server`;
CREATE TABLE `server`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(30) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `server_category_id` int(11) NOT NULL,
  `price` float(10, 1) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 15 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Compact;

-- ----------------------------
-- Records of server
-- ----------------------------
INSERT INTO `server` VALUES (1, '木桶大叔', 1, 12.0);
INSERT INTO `server` VALUES (2, '奶油打脸机', 1, 12.0);
INSERT INTO `server` VALUES (3, '生日布局', 2, 10.0);
INSERT INTO `server` VALUES (4, '求婚布局', 3, 15.0);
INSERT INTO `server` VALUES (5, '单身', 4, 10.0);
INSERT INTO `server` VALUES (8, '1212', 2, 12.0);
INSERT INTO `server` VALUES (9, '121', 2, 122.0);
INSERT INTO `server` VALUES (10, '23421', 1, 12.0);
INSERT INTO `server` VALUES (12, '活动', 1, 15.0);
INSERT INTO `server` VALUES (13, '11', 2, 11.0);
INSERT INTO `server` VALUES (14, '212', 2, 1212.0);

SET FOREIGN_KEY_CHECKS = 1;
