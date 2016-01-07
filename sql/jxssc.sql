-- phpMyAdmin SQL Dump
-- version 4.0.10deb1
-- http://www.phpmyadmin.net
--
-- 主机: localhost
-- 生成日期: 2015-12-19 21:33:45
-- 服务器版本: 5.5.41-0ubuntu0.14.04.1
-- PHP 版本: 5.5.9-1ubuntu4.7

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- 数据库: `caipiao`
--

-- --------------------------------------------------------

--
-- 表的结构 `cqssc`
--

CREATE TABLE IF NOT EXISTS `jxssc` (
  `ID` int(32) NOT NULL AUTO_INCREMENT,
  `date` varchar(16) COLLATE utf8_bin NOT NULL,
  `time` datetime NOT NULL,
  `number` varchar(8) COLLATE utf8_bin NOT NULL,
  `front3` tinyint(4) NOT NULL,
  `end3` tinyint(4) NOT NULL,
  `front4` tinyint(4) NOT NULL,
  `end4` tinyint(4) NOT NULL,
  `all` tinyint(4) NOT NULL,
  PRIMARY KEY (`ID`),
  UNIQUE KEY `date` (`date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin AUTO_INCREMENT=1 ;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
