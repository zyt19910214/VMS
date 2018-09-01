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

 Date: 01/09/2018 18:19:04
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for order_good_item
-- ----------------------------
DROP TABLE IF EXISTS `order_good_item`;
CREATE TABLE `order_good_item`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `order_id` int(11) NOT NULL,
  `good_id` int(11) NOT NULL,
  `good_count` int(11) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 122 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Compact;

-- ----------------------------
-- Records of order_good_item
-- ----------------------------
INSERT INTO `order_good_item` VALUES (117, 79, 4, 2);
INSERT INTO `order_good_item` VALUES (118, 81, 15, 1);
INSERT INTO `order_good_item` VALUES (119, 81, 15, 1);
INSERT INTO `order_good_item` VALUES (120, 84, 16, 1);
INSERT INTO `order_good_item` VALUES (121, 85, 9, 1);

SET FOREIGN_KEY_CHECKS = 1;
