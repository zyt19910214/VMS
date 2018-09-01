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

 Date: 01/09/2018 18:20:03
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for server_category
-- ----------------------------
DROP TABLE IF EXISTS `server_category`;
CREATE TABLE `server_category`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(30) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 6 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Compact;

-- ----------------------------
-- Records of server_category
-- ----------------------------
INSERT INTO `server_category` VALUES (1, '团建活动');
INSERT INTO `server_category` VALUES (2, '生日趴');
INSERT INTO `server_category` VALUES (3, '求婚趴');
INSERT INTO `server_category` VALUES (4, '交友趴');
INSERT INTO `server_category` VALUES (5, '家庭趴');

SET FOREIGN_KEY_CHECKS = 1;
