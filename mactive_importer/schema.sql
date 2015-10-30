-- MySQL dump 10.15  Distrib 10.0.21-MariaDB, for Linux (x86_64)
--
-- Host: localhost    Database: death_notices
-- ------------------------------------------------------
-- Server version	10.0.21-MariaDB-log

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
-- Table structure for table `blocked_ip`
--

DROP TABLE IF EXISTS `blocked_ip`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `blocked_ip` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `ip` varchar(15) NOT NULL DEFAULT '',
  `keywords` text NOT NULL,
  `insdate` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `blocked_ip`
--

LOCK TABLES `blocked_ip` WRITE;
/*!40000 ALTER TABLE `blocked_ip` DISABLE KEYS */;
/*!40000 ALTER TABLE `blocked_ip` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `death_notices`
--

DROP TABLE IF EXISTS `death_notices`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `death_notices` (
  `recordID` int(11) NOT NULL AUTO_INCREMENT,
  `fname` varchar(50) DEFAULT NULL,
  `btext` text,
  `bdate` date DEFAULT '0000-00-00',
  `image` varchar(255) DEFAULT '',
  `multimedia` varchar(255) DEFAULT NULL,
  `siicode` varchar(35) DEFAULT '',
  `adnum` varchar(25) DEFAULT '',
  `subclass` varchar(7) DEFAULT NULL,
  `firstname` varchar(40) DEFAULT NULL,
  `lastname` varchar(80) DEFAULT NULL,
  `publication` varchar(25) DEFAULT NULL,
  PRIMARY KEY (`recordID`),
  UNIQUE KEY `recordID` (`recordID`),
  KEY `bdate_index` (`bdate`),
  FULLTEXT KEY `fname_index` (`fname`)
) ENGINE=MyISAM AUTO_INCREMENT=1000010864 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `death_notices`
--

LOCK TABLES `death_notices` WRITE;
/*!40000 ALTER TABLE `death_notices` DISABLE KEYS */;
INSERT INTO `death_notices` VALUES (1000010859,'JANKIEWICZ, WALTER T., JR.','JANKIEWICZ, WALTER T., JR. Passed Oct. 19, 2015. Mass of Resurrection Oct. 24, 2015 at 10&#58;30 a.m. at St. Patrick Catholic church. Visitation on Oct. 23, 2015 from 2-4 and 6-8 p.m. at Keehn Funeral Home.','2015-10-22','',NULL,'','0002514495-01','6320LOE','WALTER T., JR.','JANKIEWICZ','DPA'),(1000010860,'WILLIAMS-LANNING, MARGARET-ANN (Nee ST. PIERRE)','WILLIAMS-LANNING MARGARET ANN Margaret Ann (nee St. Pierre), passed away at her South Lyon home on October 21, 2015. She was the mother of seven children&#58; Margaret (Marvin) Van Gorden and George (Nancy) of South Lyon, Judy (Kenny) Sweat of Howell, Michael (Dawn) of Howell, Chris (JoAnn) and Becky (John) Hall, of South Lyon and Shawn (Suzette) of Boston, Massachusetts. She was blessed with nearly 50 grandchildren and great-grandchildren, as well as three great-great-grandchildren and four step-children from her second marriage. She was born to Irene Mary (Cummins) and Samuel Henry St. Pierre in St. Clair Shores, where she was raised along with six siblings&#58; Ray, Mary, Jim, Bob, Frank and Bill and on Jefferson Ave., before their house was moved to Nelson, off 10 Mile and Jefferson. Her grandfather, John St. Pierre worked at Jefferson Beach, where she spent her younger years. She graduated from St. Gertrude\'s Catholic School in early June, 1949, then married George Everett Williams on the 28th of that month. They moved to South Lyon, where they raised their family. As her children grew, Margaret took several retail jobs at Kmart, Dandy Drugs, and Cunningham\'s Drug Store. She also worked at Collum\'s Mini Market in Green Oak, as well Driver\'s Berry Farm. Margaret, (or Peg, as she was known to her friends back then) was a South Lyon Girl Scout leader, member of the Cold Country Wolverines CB club, and bowled on the Thursday Night Ladies league at Woodside Lanes. She enjoyed playing bingo and going to garage sales. She was a member of the Ladies Auxiliary at the Northville VFW Post 4012 for many years. She later became a Trustee at the Green Oak Historical Society. She was preceded in death by her husbands, George Everett Williams, as well as her second husband of 11 years, Louis Lanning. She will be fondly remembered by all of her grandchildren as \"Sam.\" For service information, please visit www.phillipsfuneral.com .','2015-10-22','',NULL,'','0002514550-01','6320LOE','MARGARET-ANN (Nee ST. PIERRE)','WILLIAMS-LANNING','DPA'),(1000010861,'GONZALEZ, CHERYAL ANN','GONZALEZ, CHERYAL ANN Age 53 of Howell, passed away at her home Sunday, October 18, 2015. She was born May 17, 1962 in Fort Wayne, Indiana, the daughter of Thomas P. and JoAnn L. (Burkley) Goggans. Dear mother of Jason (Jennifer) Gonzalez of Howell, Tim (Kandyce) Gonzalez of Savannah, Georgia and Chris Muench of Indianapolis, Indiana. Loving grandmother of Dusten, Emily and Levi Gonzalez; also survived by her parents, Thomas (Betty) Goggans and JoAnn Grunden and siblings, Tom Goggans, Ruby Shepherd, Tracey Thieme, Laura Goggans-Huff, Robin Urso, Pam Howard, Debbie Murray, Clinton Goggans and Rachael Hile; father and mother-in-law, Anibal and Bertilda Gonzalez, former husband and lifelong friend, Eugene Gonzalez, numerous nieces, nephews, aunts, uncles and other cherished family members. Cheryal was a very selfless person, her family was her greatest gift whom she took care of first and foremost. She worked for Spiral Industries in assembly for many years and the Dollar General. Cheryal attended Fowlerville United Brethern Church, 9300 W. Grand River, Fowlerville where a memorial service will be held Saturday, October 24, 2015 at 11&#58;00 a.m. Please sign the family\'s online guestbook at www.macdonaldsfuneralhome.com','2015-10-22','',NULL,'','0002514585-01','6320LOE','CHERYAL ANN','GONZALEZ','DPA'),(1000010862,'PROULX, ROBERT FRANCIS','PROULX, ROBERT FRANCIS Age 71 of Byron passed away on October 18, 2015, with his family by his side from an inoperable carcinoma of the brain. Born to Alfred and Helen (Kellogg) Proulx on October 10, 1944 in Detroit, Michigan. Bob served in the U.S. Navy. He married Catherine Munsell on June 6, 1981. Most of his working life he was a brick mason. He enjoyed salvaging wood and repurposing it into buildings for his family. He was preceded in death by his parents, brother-in-law Arthur, sister-in-law Carol. Bob is survived by&#58; his wife, Catherine of Byron; brother-in-law, Frank Munsell; brother-in-law Gordon (Teena) Munsell; Several nieces and nephews.The family requests no flowers. Memorials are requested to Great Lakes Caring Hospice. Donations may be made online at www.greatlakeshospice.com. Visitation will be held on Friday from 2-8 p.m. Funeral, Saturday 10&#58;00 a.m. at Herrmann Funeral Home, Niblack Chapel, with Rev. Meritt Bongard officiating. Burial will follow at Greenwood Cemetery. Pjherrmannfuneralhome.com ','2015-10-22','',NULL,'','0002514586-01','6320LOE','ROBERT FRANCIS','PROULX','DPA'),(1000010863,'GRIFFES, MARJORIE J.','GRIFFES, MARJORIE J. Age 75, October 19, 2015. Visitation Thursday, October 22, 11 am - 1pm. with Memorial Service at 1 pm at Herrmann Funeral Home Niblack Chapel, Fowlerville MI. pjherrmannfuneralhome.com','2015-10-22','',NULL,'','0002514604-01','6320LOE','MARJORIE J.','GRIFFES','DPA');
/*!40000 ALTER TABLE `death_notices` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `death_notices_guestbook`
--

DROP TABLE IF EXISTS `death_notices_guestbook`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `death_notices_guestbook` (
  `messageid` int(11) NOT NULL AUTO_INCREMENT,
  `recordid` int(11) NOT NULL DEFAULT '0',
  `firstname` varchar(50) DEFAULT '',
  `lastname` varchar(50) DEFAULT '',
  `message` text,
  `city` varchar(50) DEFAULT '',
  `state` char(3) DEFAULT NULL,
  `email` varchar(50) DEFAULT '',
  `date` datetime DEFAULT NULL,
  `ip` varchar(15) DEFAULT NULL,
  `approved` char(1) DEFAULT 'N',
  PRIMARY KEY (`messageid`)
) ENGINE=InnoDB AUTO_INCREMENT=267896 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `death_notices_guestbook`
--

LOCK TABLES `death_notices_guestbook` WRITE;
/*!40000 ALTER TABLE `death_notices_guestbook` DISABLE KEYS */;
/*!40000 ALTER TABLE `death_notices_guestbook` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `funeral_directors`
--

DROP TABLE IF EXISTS `funeral_directors`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `funeral_directors` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `funeral_director` varchar(35) NOT NULL DEFAULT '',
  `homepage_url` varchar(255) DEFAULT '',
  `insert_timestamp` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `city` varchar(20) DEFAULT '',
  `phone1` varchar(15) DEFAULT '',
  `address` varchar(40) NOT NULL DEFAULT '',
  PRIMARY KEY (`id`),
  KEY `funeral_director` (`funeral_director`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `funeral_directors`
--

LOCK TABLES `funeral_directors` WRITE;
/*!40000 ALTER TABLE `funeral_directors` DISABLE KEYS */;
INSERT INTO `funeral_directors` VALUES (1,'Howe-Peterson','http://HowePeterson.com','0000-00-00 00:00:00','Taylor','313-291-0900','9800 S. Telegraph.'),(2,'Howe-Peterson','http://HowePeterson.com','0000-00-00 00:00:00','Dearborn','313-561-1500','22546 Michigan Ave.'),(3,'Resurrection Funeral Home','http://www.mem.com','2009-04-30 19:38:37','Clinton Twp','586-412-3000','40800 Hayes Road');
/*!40000 ALTER TABLE `funeral_directors` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `funeralhomes`
--

DROP TABLE IF EXISTS `funeralhomes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `funeralhomes` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `address` varchar(255) NOT NULL,
  `city` varchar(255) NOT NULL,
  `state` varchar(255) NOT NULL,
  `zip` varchar(11) NOT NULL,
  `lng` varchar(25) NOT NULL,
  `lat` varchar(25) NOT NULL,
  `type` varchar(10) DEFAULT NULL,
  `url` varchar(255) DEFAULT NULL,
  `phone` varchar(25) DEFAULT NULL,
  `email` varchar(25) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=1333 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `funeralhomes`
--

LOCK TABLES `funeralhomes` WRITE;
/*!40000 ALTER TABLE `funeralhomes` DISABLE KEYS */;
/*!40000 ALTER TABLE `funeralhomes` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `new_obposts`
--

DROP TABLE IF EXISTS `new_obposts`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `new_obposts` (
  `obid` int(11) NOT NULL AUTO_INCREMENT,
  `client_name` varchar(25) DEFAULT NULL,
  `client_phone` varchar(15) DEFAULT NULL,
  `client_email` varchar(50) DEFAULT NULL,
  `client_address` varchar(255) DEFAULT NULL,
  `client_city` varchar(50) DEFAULT NULL,
  `client_state` char(2) DEFAULT NULL,
  `client_zip` varchar(11) DEFAULT NULL,
  `ob_fullname` varchar(50) DEFAULT NULL,
  `ob_firstname` char(25) NOT NULL,
  `ob_lastname` char(25) NOT NULL,
  `ob_text` text,
  `ob_dates` varchar(255) DEFAULT NULL,
  `ob_image` varchar(255) DEFAULT NULL,
  `ob_siicode` varchar(25) DEFAULT NULL,
  `fh_name` varchar(50) DEFAULT NULL,
  `fh_contact` varchar(50) DEFAULT NULL,
  `status` int(1) NOT NULL DEFAULT '0',
  `datetimestamp` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `posted_ip` varchar(15) NOT NULL DEFAULT '127.0.0.1',
  `fh_phone` varchar(25) DEFAULT '',
  `submitedby` varchar(25) DEFAULT NULL,
  `posted_date` varchar(10) DEFAULT 'now()',
  `browser_string` varchar(255) DEFAULT NULL,
  `appear` varchar(20) NOT NULL DEFAULT 'both',
  `publication` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`obid`)
) ENGINE=InnoDB AUTO_INCREMENT=104655 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `new_obposts`
--

LOCK TABLES `new_obposts` WRITE;
/*!40000 ALTER TABLE `new_obposts` DISABLE KEYS */;
/*!40000 ALTER TABLE `new_obposts` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2015-10-22 13:26:34
