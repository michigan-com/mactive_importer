-- MySQL dump 10.13  Distrib 5.5.16, for Linux (x86_64)
--
-- Host: localhost    Database: dbVerticals
-- ------------------------------------------------------
-- Server version	5.5.16-log

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `classifieds_live`
--

DROP TABLE IF EXISTS `classifieds_live`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `classifieds_live` (
  `adnum` varchar(50) NOT NULL DEFAULT '0',
  `subclassnum` int(4) NOT NULL DEFAULT '0',
  `text_of_ad` text NOT NULL,
  `email` varchar(65) DEFAULT NULL,
  `hyper_link` varchar(255) DEFAULT NULL,
  `date_posted` date NOT NULL DEFAULT '0000-00-00',
  `run_days` set('7','30') NOT NULL DEFAULT '7',
  `highlight` set('Y','N') NOT NULL DEFAULT 'N',
  `user_id` int(11) DEFAULT NULL,
  `start-date` date DEFAULT '0000-00-00',
  `end-date` date DEFAULT '0000-00-00',
  `image1` varchar(50) DEFAULT '',
  `image2` varchar(50) DEFAULT '',
  `image3` varchar(50) DEFAULT '',
  `image4` varchar(50) DEFAULT '',
  `image5` varchar(50) DEFAULT '',
  `street` varchar(50) DEFAULT '',
  `city` varchar(20) DEFAULT '',
  `state` char(2) DEFAULT '',
  `zip` varchar(5) DEFAULT '',
  `external_adnum` varchar(20) DEFAULT NULL,
  `source` varchar(10) DEFAULT NULL,
  `external_subclass` varchar(50) DEFAULT NULL,
  `mactiveimage` varchar(25) DEFAULT '',
  `onlinezip` varchar(15) DEFAULT NULL,
  `onlineprice` varchar(6) DEFAULT NULL,
  `onlinetitle` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`adnum`),
  KEY `subclassnum_idx` (`subclassnum`),
  FULLTEXT KEY `fulltext` (`text_of_ad`,`onlinetitle`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `classifieds_insert`
--

DROP TABLE IF EXISTS `classifieds_insert`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `classifieds_insert` (
  `adnum` varchar(50) NOT NULL DEFAULT '',
  `subclassnum` varchar(4) NOT NULL DEFAULT '',
  `text_of_ad` text NOT NULL,
  `email` varchar(65) DEFAULT NULL,
  `hyper_link` varchar(255) DEFAULT NULL,
  `date_posted` date NOT NULL DEFAULT '0000-00-00',
  `run_days` set('7','30') NOT NULL DEFAULT '7',
  `highlight` set('Y','N') NOT NULL DEFAULT 'N',
  `user_id` int(11) DEFAULT NULL,
  `start-date` date DEFAULT '0000-00-00',
  `end-date` date DEFAULT '0000-00-00',
  `image1` varchar(50) DEFAULT '',
  `image2` varchar(50) DEFAULT '',
  `image3` varchar(50) DEFAULT '',
  `image4` varchar(50) DEFAULT '',
  `image5` varchar(50) DEFAULT '',
  `street` varchar(50) DEFAULT '',
  `city` varchar(20) DEFAULT '',
  `state` char(2) DEFAULT '',
  `zip` varchar(5) DEFAULT '',
  `external_adnum` varchar(20) DEFAULT NULL,
  `source` varchar(10) DEFAULT NULL,
  `external_subclass` varchar(50) DEFAULT NULL,
  `mactiveimage` varchar(25) DEFAULT '',
  `onlinezip` varchar(15) DEFAULT NULL,
  `onlineprice` varchar(6) DEFAULT NULL,
  `onlinetitle` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `classifieds_images`
--

DROP TABLE IF EXISTS `classifieds_images`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `classifieds_images` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `adnum` varchar(50) NOT NULL,
  `imagename` varchar(100) NOT NULL,
  `time_stamp` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `vendor` varchar(10) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `adnum` (`adnum`)
) ENGINE=InnoDB AUTO_INCREMENT=2247 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2015-11-02  9:41:17
