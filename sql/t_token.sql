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

 Date: 03/09/2018 00:53:13
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

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

SET FOREIGN_KEY_CHECKS = 1;
