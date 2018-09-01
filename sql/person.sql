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

 Date: 01/09/2018 18:19:22
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for person
-- ----------------------------
DROP TABLE IF EXISTS `person`;
CREATE TABLE `person`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `sex` tinyint(1) NOT NULL,
  `phone` varchar(11) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `note` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `create_time` datetime(0) NULL DEFAULT NULL,
  `resrver1` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 73 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Compact;

-- ----------------------------
-- Records of person
-- ----------------------------
INSERT INTO `person` VALUES (1, '武通', 1, '17629298188', '', '2018-08-19 00:05:25', '');
INSERT INTO `person` VALUES (2, '温娜', 0, '15353775130', '活动会员', '2018-07-31 15:16:30', NULL);
INSERT INTO `person` VALUES (19, '牛龙1', 1, '18778882220', '1', '2018-08-08 15:56:55', NULL);
INSERT INTO `person` VALUES (20, '牛龙2', 1, '18778882222', '1', '2018-08-08 15:56:55', NULL);
INSERT INTO `person` VALUES (21, '牛龙3', 1, '18778882223', '1', '2018-08-08 15:56:55', NULL);
INSERT INTO `person` VALUES (22, '牛龙4', 1, '18778882224', '1', '2018-08-08 15:56:55', NULL);
INSERT INTO `person` VALUES (23, '牛龙5', 1, '18778882225', '1', '2018-08-08 15:56:55', NULL);
INSERT INTO `person` VALUES (24, '牛龙6', 1, '18778882226', '1', '2018-08-08 15:56:55', NULL);
INSERT INTO `person` VALUES (25, '牛龙7', 1, '18778882227', '1', '2018-08-08 15:56:55', NULL);
INSERT INTO `person` VALUES (26, '牛龙8', 1, '18778882228', '1', '2018-08-08 15:56:55', NULL);
INSERT INTO `person` VALUES (27, '牛龙9', 1, '18778882229', '1', '2018-08-08 15:56:55', NULL);
INSERT INTO `person` VALUES (28, '牛龙10', 1, '18778882240', '1', '2018-08-08 15:56:55', NULL);
INSERT INTO `person` VALUES (29, '牛龙11', 1, '18778882241', '1', '2018-08-08 15:56:55', NULL);
INSERT INTO `person` VALUES (30, '牛龙12', 1, '18778882242', '1', '2018-08-08 15:56:55', NULL);
INSERT INTO `person` VALUES (31, '牛龙13', 1, '18778882243', '1', '2018-08-08 15:56:55', NULL);
INSERT INTO `person` VALUES (32, '牛龙14', 1, '18778882244', '1', '2018-08-08 15:56:55', NULL);
INSERT INTO `person` VALUES (33, '牛龙15', 1, '18778882245', '1', '2018-08-08 15:56:55', NULL);
INSERT INTO `person` VALUES (34, '牛龙16', 1, '18778882246', '1', '2018-08-08 15:56:55', NULL);
INSERT INTO `person` VALUES (35, '牛龙17', 1, '18778882247', '1', '2018-08-08 15:56:55', NULL);
INSERT INTO `person` VALUES (36, '牛龙18', 1, '18778882248', '1', '2018-08-08 15:56:55', NULL);
INSERT INTO `person` VALUES (37, '牛龙19', 1, '18778882249', '1', '2018-08-19 15:54:16', NULL);
INSERT INTO `person` VALUES (71, '牛牛1', 1, '12222222223', '1', '2018-08-19 00:58:18', NULL);
INSERT INTO `person` VALUES (72, '小马佩德罗', 1, '15349246114', '', '2018-08-22 10:27:56', NULL);

SET FOREIGN_KEY_CHECKS = 1;
