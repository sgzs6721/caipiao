-- phpMyAdmin SQL Dump
-- version 4.4.2
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: 2016-03-08 16:52:47
-- 服务器版本： 5.6.17
-- PHP Version: 5.5.21

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `lottery`
--

-- --------------------------------------------------------

--
-- 表的结构 `jx11x5`
--

CREATE TABLE IF NOT EXISTS `jx11x5` (
  `ID` int(32) NOT NULL,
  `num` varchar(16) COLLATE utf8_bin NOT NULL,
  `year` year(4) NOT NULL,
  `month` tinyint(4) NOT NULL,
  `day` tinyint(4) NOT NULL,
  `weekday` tinyint(4) NOT NULL,
  `time` time NOT NULL,
  `no` varchar(4) COLLATE utf8_bin NOT NULL,
  `first` varchar(2) COLLATE utf8_bin NOT NULL,
  `second` varchar(2) COLLATE utf8_bin NOT NULL,
  `third` varchar(2) COLLATE utf8_bin NOT NULL,
  `fourth` varchar(2) COLLATE utf8_bin NOT NULL,
  `last` varchar(2) COLLATE utf8_bin NOT NULL
) ENGINE=InnoDB AUTO_INCREMENT=106 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `jx11x5`
--
ALTER TABLE `jx11x5`
  ADD PRIMARY KEY (`ID`),
  ADD UNIQUE KEY `num` (`num`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `jx11x5`
--
ALTER TABLE `jx11x5`
  MODIFY `ID` int(32) NOT NULL AUTO_INCREMENT,AUTO_INCREMENT=106;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
