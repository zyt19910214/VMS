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

 Date: 19/08/2018 19:20:43
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for vip_order
-- ----------------------------
DROP TABLE IF EXISTS `vip_order`;
CREATE TABLE `vip_order`  (
  `id` int(11) UNSIGNED NOT NULL AUTO_INCREMENT,
  `person_id` int(11) UNSIGNED NOT NULL,
  `order_serial_number` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `order_status` tinyint(1) NOT NULL,
  `order_category_id` int(11) NOT NULL,
  `create_time` datetime(0) NOT NULL,
  `end_time` datetime(0) NULL DEFAULT NULL,
  `notes` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `all_value` float(10, 1) NULL DEFAULT NULL,
  `lay_value` float(10, 1) NULL DEFAULT NULL,
  `free_value` float(10, 1) NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 57 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Compact;

-- ----------------------------
-- Records of vip_order
-- ----------------------------
INSERT INTO `vip_order` VALUES (34, 71, '20180819005022', 0, 3, '2018-08-19 00:50:22', NULL, '', 521.0, 323.0, 53.0);
INSERT INTO `vip_order` VALUES (35, 37, '20180819012236', 1, 3, '2018-08-19 01:22:36', '2018-08-19 13:24:12', '', 521.0, 10.0, 10.0);
INSERT INTO `vip_order` VALUES (36, 30, '20180819143855', 0, 4, '2018-08-19 14:38:55', NULL, '', 88.0, 1.0, 1.0);
INSERT INTO `vip_order` VALUES (49, 31, '20180819152929', 0, 3, '2018-08-19 15:29:29', NULL, '', 521.0, 0.0, 0.0);
INSERT INTO `vip_order` VALUES (50, 34, '20180819153005', 0, 1, '2018-08-19 15:30:05', NULL, '', 299.0, 0.0, 0.0);
INSERT INTO `vip_order` VALUES (51, 26, '20180819153021', 0, 1, '2018-08-19 15:30:21', NULL, '', 299.0, 27.0, 25.0);
INSERT INTO `vip_order` VALUES (56, 1, '20180819185800', 0, 5, '2018-08-19 18:58:00', NULL, '', 300.0, 0.0, 0.0);

SET FOREIGN_KEY_CHECKS = 1;
