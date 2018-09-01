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

 Date: 01/09/2018 18:18:29
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for good
-- ----------------------------
DROP TABLE IF EXISTS `good`;
CREATE TABLE `good`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(30) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `good_category_id` int(11) NOT NULL,
  `price` float(10, 1) NOT NULL,
  `origin_price` float(10, 1) NULL DEFAULT NULL,
  `uploadtime` datetime(0) NULL DEFAULT NULL,
  `status` int(10) NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 17 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Compact;

-- ----------------------------
-- Records of good
-- ----------------------------
INSERT INTO `good` VALUES (1, '可乐', 1, 3.0, 2.0, '2018-08-09 23:33:31', 3);
INSERT INTO `good` VALUES (2, '雪碧', 1, 3.0, 2.0, '2018-08-09 23:33:44', 18);
INSERT INTO `good` VALUES (4, '凉皮', 3, 7.0, 3.5, '2018-08-09 23:34:40', 8);
INSERT INTO `good` VALUES (5, '雪花', 2, 3.0, 2.1, '2018-08-09 23:35:01', 8);
INSERT INTO `good` VALUES (6, '黑啤', 2, 4.0, 2.8, '2018-08-09 23:35:15', 12);
INSERT INTO `good` VALUES (7, '牛奶', 1, 8.0, 6.0, '2018-08-09 23:35:36', 7);
INSERT INTO `good` VALUES (8, '方便面', 3, 7.0, 4.0, '2018-08-09 23:52:33', 10);
INSERT INTO `good` VALUES (9, '自制酸梅汤', 1, 8.0, 1.0, '2018-08-09 23:53:02', 28);
INSERT INTO `good` VALUES (10, '自制柳橙汁', 1, 8.0, 1.0, '2018-08-09 23:53:15', 29);
INSERT INTO `good` VALUES (11, '自制橙汁', 1, 8.0, 1.0, '2018-08-09 23:53:27', 7);
INSERT INTO `good` VALUES (12, '自制草莓汁', 1, 8.0, 1.0, '2018-08-09 23:54:06', 0);
INSERT INTO `good` VALUES (13, '酸梅汤', 1, 4.0, 3.5, '2018-08-14 23:27:59', 0);
INSERT INTO `good` VALUES (14, '加多宝', 1, 5.5, 4.5, '2018-08-31 01:02:50', 10);
INSERT INTO `good` VALUES (15, '红牛', 1, 6.0, 4.8, '2018-08-22 10:29:28', 25);
INSERT INTO `good` VALUES (16, '茶π', 1, 6.0, 3.8, '2018-08-22 10:48:00', 26);

SET FOREIGN_KEY_CHECKS = 1;
