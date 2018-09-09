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

 Date: 04/09/2018 00:18:29
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
) ENGINE = InnoDB AUTO_INCREMENT = 18 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Compact;

-- ----------------------------
-- Records of good
-- ----------------------------
INSERT INTO `good` VALUES (2, '雪碧', 1, 3.0, 2.0, '2018-08-09 23:33:44', 16);
INSERT INTO `good` VALUES (4, '凉皮', 3, 7.0, 3.5, '2018-08-09 23:34:40', 8);
INSERT INTO `good` VALUES (5, '雪花', 2, 3.0, 2.1, '2018-08-09 23:35:01', 8);
INSERT INTO `good` VALUES (6, '黑啤', 2, 4.0, 2.8, '2018-08-09 23:35:15', 12);
INSERT INTO `good` VALUES (7, '牛奶', 1, 8.0, 6.0, '2018-08-09 23:35:36', 7);
INSERT INTO `good` VALUES (9, '自制酸梅汤', 1, 8.0, 1.0, '2018-08-09 23:53:02', 25);
INSERT INTO `good` VALUES (10, '自制柳橙汁', 1, 8.0, 1.0, '2018-08-09 23:53:15', 29);
INSERT INTO `good` VALUES (11, '自制橙汁', 1, 8.0, 1.0, '2018-08-09 23:53:27', 7);
INSERT INTO `good` VALUES (14, '加多宝', 1, 5.5, 4.5, '2018-08-31 01:02:50', 10);
INSERT INTO `good` VALUES (15, '红牛', 1, 6.0, 4.8, '2018-08-22 10:29:28', 17);
INSERT INTO `good` VALUES (16, '茶π', 1, 6.0, 3.8, '2018-08-22 10:48:00', 26);
INSERT INTO `good` VALUES (17, '阿萨姆', 1, 5.0, 3.0, '2018-09-02 23:26:56', 20);

-- ----------------------------
-- Table structure for good_category
-- ----------------------------
DROP TABLE IF EXISTS `good_category`;
CREATE TABLE `good_category`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(30) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 5 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Compact;

-- ----------------------------
-- Records of good_category
-- ----------------------------
INSERT INTO `good_category` VALUES (1, '饮料');
INSERT INTO `good_category` VALUES (2, '酒水');
INSERT INTO `good_category` VALUES (3, '简餐');
INSERT INTO `good_category` VALUES (4, '火锅');

-- ----------------------------
-- Table structure for manager
-- ----------------------------
DROP TABLE IF EXISTS `manager`;
CREATE TABLE `manager`  (
  `id` int(10) NOT NULL AUTO_INCREMENT,
  `username` varchar(30) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `password` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `type` tinyint(1) NULL DEFAULT NULL,
  `name` varchar(30) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `photo` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `phone` varchar(11) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `email` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `note` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 3 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Compact;

-- ----------------------------
-- Records of manager
-- ----------------------------
INSERT INTO `manager` VALUES (1, 'zyt', '7630508tong', 1, '张运通', NULL, '17629298189', '707150586@qq.com', NULL);
INSERT INTO `manager` VALUES (2, 'wn', '111111', 0, '温娜', NULL, '15353775130', 'wenna2@huawei .com', NULL);

-- ----------------------------
-- Table structure for order_category
-- ----------------------------
DROP TABLE IF EXISTS `order_category`;
CREATE TABLE `order_category`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(30) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `price` float(10, 1) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 6 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Compact;

-- ----------------------------
-- Records of order_category
-- ----------------------------
INSERT INTO `order_category` VALUES (1, '299轰趴', 299.0);
INSERT INTO `order_category` VALUES (2, '399轰趴', 399.0);
INSERT INTO `order_category` VALUES (3, '521轰趴', 521.0);
INSERT INTO `order_category` VALUES (4, '麻将', 88.0);
INSERT INTO `order_category` VALUES (5, '狼人杀包场', 300.0);

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
) ENGINE = InnoDB AUTO_INCREMENT = 133 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Compact;

-- ----------------------------
-- Table structure for order_server_item
-- ----------------------------
DROP TABLE IF EXISTS `order_server_item`;
CREATE TABLE `order_server_item`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `order_id` int(11) NOT NULL,
  `server_id` int(11) NOT NULL,
  `server_count` int(11) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 4 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Compact;

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
) ENGINE = InnoDB AUTO_INCREMENT = 82 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Compact;

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
INSERT INTO `person` VALUES (31, '牛龙13', 1, '18778882243', '1', '2018-08-08 15:56:55', NULL);
INSERT INTO `person` VALUES (32, '牛龙14', 1, '18778882244', '1', '2018-08-08 15:56:55', NULL);
INSERT INTO `person` VALUES (33, '牛龙15', 1, '18778882245', '1', '2018-08-08 15:56:55', NULL);
INSERT INTO `person` VALUES (34, '牛龙16', 1, '18778882246', '1', '2018-08-08 15:56:55', NULL);
INSERT INTO `person` VALUES (35, '牛龙17', 1, '18778882247', '1', '2018-08-08 15:56:55', NULL);
INSERT INTO `person` VALUES (36, '牛龙18', 1, '18778882248', '1', '2018-08-08 15:56:55', NULL);
INSERT INTO `person` VALUES (37, '牛龙19', 1, '18778882249', '1', '2018-08-19 15:54:16', NULL);
INSERT INTO `person` VALUES (71, '牛牛1', 1, '12222222223', '1', '2018-08-19 00:58:18', NULL);
INSERT INTO `person` VALUES (72, '小马佩德罗', 1, '15349246114', '', '2018-08-22 10:27:56', NULL);
INSERT INTO `person` VALUES (73, '找份', 1, '14747475454', '', '2018-09-02 21:08:28', NULL);
INSERT INTO `person` VALUES (74, '正数', 1, '15455554554', '', '2018-09-02 21:11:39', NULL);
INSERT INTO `person` VALUES (75, '负数', 1, '15444448787', '1', '2018-09-02 21:13:04', NULL);
INSERT INTO `person` VALUES (76, '1', 1, '17544445888', '1', '2018-09-02 21:21:56', NULL);
INSERT INTO `person` VALUES (77, '1', 1, '15411111111', '1', '2018-09-02 21:25:32', NULL);
INSERT INTO `person` VALUES (81, '张运通', 1, '17629298189', '', '2018-09-02 23:45:14', NULL);

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
) ENGINE = InnoDB AUTO_INCREMENT = 50 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Compact;

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
) ENGINE = InnoDB AUTO_INCREMENT = 16 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Compact;

-- ----------------------------
-- Records of server
-- ----------------------------
INSERT INTO `server` VALUES (2, '奶油打脸机', 1, 12.0);
INSERT INTO `server` VALUES (3, '生日布局', 2, 10.0);
INSERT INTO `server` VALUES (4, '求婚布局', 3, 15.0);
INSERT INTO `server` VALUES (5, '单身', 4, 10.0);
INSERT INTO `server` VALUES (8, '疯狂布局', 2, 12.0);
INSERT INTO `server` VALUES (9, '121', 2, 122.0);
INSERT INTO `server` VALUES (10, '23421', 1, 12.0);
INSERT INTO `server` VALUES (12, '活动', 1, 15.0);
INSERT INTO `server` VALUES (14, '212', 2, 1212.0);

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

-- ----------------------------
-- Table structure for t_token
-- ----------------------------
DROP TABLE IF EXISTS `t_token`;
CREATE TABLE `t_token`  (
  `id` int(10) NOT NULL AUTO_INCREMENT,
  `user_id` int(10) NULL DEFAULT NULL,
  `token` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `time` datetime(0) NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 59 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Compact;

-- ----------------------------
-- Records of t_token
-- ----------------------------
INSERT INTO `t_token` VALUES (56, 2, 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJtb3RoYW50eS5jb20iLCJpYXQiOjE1MzU5MDYxNzcsInVzZXJuYW1lIjoid24iLCJzY29wZXMiOlsib3BlbiJdfQ.g6SYgjWJQlDu0O_6oFEPCTJYkqIFmqYrRTGcVA9rJuE', '2018-09-03 00:51:28');
INSERT INTO `t_token` VALUES (57, 2, 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJtb3RoYW50eS5jb20iLCJpYXQiOjE1MzU5MDcxMzAsInVzZXJuYW1lIjoid24iLCJzY29wZXMiOlsib3BlbiJdfQ.okrp5hMbSjephdsBKMxvXOSOzIpNjqkKkFTO7b_Tgk4', '2018-09-03 00:52:21');
INSERT INTO `t_token` VALUES (58, 2, 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJtb3RoYW50eS5jb20iLCJpYXQiOjE1MzU5MDcxNDksInVzZXJuYW1lIjoid24iLCJzY29wZXMiOlsib3BlbiJdfQ.oWk4Y9gPtlxJMwLn4SntFZ0ht01gj3viLRM_7ukEBEc', '2018-09-03 00:52:29');

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
) ENGINE = InnoDB AUTO_INCREMENT = 102 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Compact;

-- ----------------------------
-- Records of vip_order
-- ----------------------------
INSERT INTO `vip_order` VALUES (95, 74, '20180902225717', 1, 1, '2018-09-02 22:57:17', '2018-09-02 22:57:25', '', 299.0, 0.0, 0.0, 0.0);
INSERT INTO `vip_order` VALUES (96, 74, '20180902225733', 1, 1, '2018-09-02 22:57:33', '2018-09-02 22:57:42', '', 269.0, 0.0, 0.0, 30.0);
INSERT INTO `vip_order` VALUES (97, 81, '20180902225839', 1, 4, '2018-09-02 22:58:39', '2018-09-02 23:10:35', '', 58.1, 0.0, 0.0, 29.9);
INSERT INTO `vip_order` VALUES (98, 81, '20180902233231', 1, 1, '2018-09-02 23:32:31', '2018-09-02 23:43:48', '', 294.0, 0.0, 0.0, 5.0);
INSERT INTO `vip_order` VALUES (99, 71, '20180902233543', 1, 1, '2018-09-02 23:35:43', '2018-09-02 23:35:51', '', 299.0, 0.0, 0.0, 0.0);
INSERT INTO `vip_order` VALUES (100, 71, '20180902233601', 1, 1, '2018-09-02 23:36:01', '2018-09-02 23:36:10', '', 270.0, 0.0, 0.0, 29.0);
INSERT INTO `vip_order` VALUES (101, 71, '20180902233909', 1, 1, '2018-09-02 23:39:09', '2018-09-02 23:39:46', '', 272.0, 0.0, 0.0, 27.0);

SET FOREIGN_KEY_CHECKS = 1;
