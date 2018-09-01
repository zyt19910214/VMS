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

 Date: 01/09/2018 18:20:18
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
  `point_offset` float(10, 1) NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 86 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Compact;

-- ----------------------------
-- Records of vip_order
-- ----------------------------
INSERT INTO `vip_order` VALUES (79, 72, '20180831005128', 1, 3, '2018-08-31 00:51:28', '2018-08-31 00:54:37', '', 555.0, 10.0, 0.0, 0.0);
INSERT INTO `vip_order` VALUES (80, 72, '20180831005453', 1, 4, '2018-08-31 00:54:53', '2018-08-31 00:55:05', '', 32.5, 0.0, 0.0, 55.5);
INSERT INTO `vip_order` VALUES (81, 37, '20180831010021', 1, 5, '2018-08-31 01:00:21', '2018-08-31 01:01:24', '', 312.0, 0.0, 0.0, 0.0);
INSERT INTO `vip_order` VALUES (82, 37, '20180831010149', 1, 1, '2018-08-31 01:01:49', '2018-08-31 01:02:16', '', 299.0, 0.0, 0.0, 0.0);
INSERT INTO `vip_order` VALUES (83, 72, '20180901131640', 1, 1, '2018-09-01 13:16:40', '2018-09-01 13:16:52', '', 299.0, 0.0, 0.0, 0.0);
INSERT INTO `vip_order` VALUES (84, 72, '20180901131718', 2, 1, '2018-09-01 13:17:18', '2018-09-01 13:17:30', '', 0.0, 0.0, 0.0, NULL);
INSERT INTO `vip_order` VALUES (85, 72, '20180901131737', 0, 1, '2018-09-01 13:17:37', NULL, '', NULL, 0.0, 0.0, NULL);

SET FOREIGN_KEY_CHECKS = 1;
