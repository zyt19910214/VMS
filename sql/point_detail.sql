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

 Date: 01/09/2018 18:19:31
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for point_detail
-- ----------------------------
DROP TABLE IF EXISTS `point_detail`;
CREATE TABLE `point_detail`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `person_id` int(11) NOT NULL,
  `order_id` int(11) NOT NULL,
  `type` tinyint(1) NOT NULL,
  `point` float(6, 1) NOT NULL,
  `create_time` datetime(0) NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 24 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Compact;

-- ----------------------------
-- Records of point_detail
-- ----------------------------
INSERT INTO `point_detail` VALUES (18, 72, 79, 0, 555.0, '2018-08-31 00:54:37');
INSERT INTO `point_detail` VALUES (19, 72, 80, 1, -555.0, '2018-08-31 00:55:05');
INSERT INTO `point_detail` VALUES (20, 72, 80, 0, 32.5, '2018-08-31 00:55:05');
INSERT INTO `point_detail` VALUES (21, 37, 81, 0, 312.0, '2018-08-31 01:01:24');
INSERT INTO `point_detail` VALUES (22, 37, 82, 0, 299.0, '2018-08-31 01:02:16');
INSERT INTO `point_detail` VALUES (23, 72, 83, 0, 299.0, '2018-09-01 13:16:52');

SET FOREIGN_KEY_CHECKS = 1;
