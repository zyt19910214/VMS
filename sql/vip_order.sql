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

 Date: 13/08/2018 23:09:50
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for vip_order
-- ----------------------------
DROP TABLE IF EXISTS `vip_order`;
CREATE TABLE `vip_order`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `phone` varchar(11) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `order_serial_number` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `order_status` tinyint(1) NOT NULL,
  `order_category_id` int(11) NOT NULL,
  `create_time` datetime(0) NOT NULL,
  `notes` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 2 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Compact;

-- ----------------------------
-- Records of vip_order
-- ----------------------------
INSERT INTO `vip_order` VALUES (1, '17629298189', '20180731111111', 1, 1, '2018-07-31 15:28:23', '11');

SET FOREIGN_KEY_CHECKS = 1;
