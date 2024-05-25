-- MySQL dump 10.13  Distrib 8.0.22, for Win64 (x86_64)
--
-- Host: localhost    Database: car_rental
-- ------------------------------------------------------
-- Server version	8.0.22

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `car`
--

DROP TABLE IF EXISTS `car`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `car` (
  `carID` int unsigned NOT NULL AUTO_INCREMENT,
  `availability` tinyint DEFAULT NULL,
  `colour` varchar(31) DEFAULT NULL,
  `power` int unsigned DEFAULT NULL,
  `makeFK_ID` int unsigned NOT NULL,
  `description` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`carID`),
  UNIQUE KEY `uuid_UNIQUE` (`carID`),
  KEY `carMakeFK_idx` (`makeFK_ID`),
  CONSTRAINT `makeFK` FOREIGN KEY (`makeFK_ID`) REFERENCES `make` (`makeID`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `car`
--

LOCK TABLES `car` WRITE;
/*!40000 ALTER TABLE `car` DISABLE KEYS */;
INSERT INTO `car` VALUES (1,1,'Yellow',112,1,'asd'),(2,1,'Blue',63,2,'asd'),(3,1,'Red',83,3,'asd'),(4,1,'Green',74,4,'asd'),(5,1,'Gray',107,5,'asd'),(6,1,'Black',82,6,'asd'),(7,1,'Red',61,7,'asd'),(8,1,'Gray',72,8,'asd'),(9,1,'Gray',109,9,'asd'),(10,1,'Gray',72,10,'asd');
/*!40000 ALTER TABLE `car` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `make`
--

DROP TABLE IF EXISTS `make`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `make` (
  `makeID` int unsigned NOT NULL AUTO_INCREMENT,
  `makeName` varchar(31) DEFAULT NULL,
  `modelFK_ID` int unsigned NOT NULL,
  PRIMARY KEY (`makeID`),
  UNIQUE KEY `uuid_UNIQUE` (`makeID`),
  KEY `modelFK_idx` (`modelFK_ID`),
  CONSTRAINT `modelFK` FOREIGN KEY (`modelFK_ID`) REFERENCES `model` (`modelID`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `make`
--

LOCK TABLES `make` WRITE;
/*!40000 ALTER TABLE `make` DISABLE KEYS */;
INSERT INTO `make` VALUES (1,'Toyota',1),(2,'Toyota',2),(3,'Toyota',3),(4,'Toyota',4),(5,'Honda',5),(6,'Honda',6),(7,'Honda',7),(8,'Nissan',8),(9,'Nissan',9),(10,'Nissan',10);
/*!40000 ALTER TABLE `make` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `model`
--

DROP TABLE IF EXISTS `model`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `model` (
  `modelID` int unsigned NOT NULL AUTO_INCREMENT,
  `modelName` varchar(31) NOT NULL,
  PRIMARY KEY (`modelID`),
  UNIQUE KEY `carModelID_UNIQUE` (`modelID`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `model`
--

LOCK TABLES `model` WRITE;
/*!40000 ALTER TABLE `model` DISABLE KEYS */;
INSERT INTO `model` VALUES (1,'Yaris'),(2,'Aygo'),(3,'Corolla'),(4,'Camry'),(5,'Civic'),(6,'HR-V'),(7,'Accord'),(8,'Altima'),(9,'Micra'),(10,'Juke');
/*!40000 ALTER TABLE `model` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `roles`
--

DROP TABLE IF EXISTS `roles`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `roles` (
  `roleID` int unsigned NOT NULL AUTO_INCREMENT,
  `roleName` varchar(31) NOT NULL,
  PRIMARY KEY (`roleID`),
  UNIQUE KEY `roleID_UNIQUE` (`roleID`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `roles`
--

LOCK TABLES `roles` WRITE;
/*!40000 ALTER TABLE `roles` DISABLE KEYS */;
INSERT INTO `roles` VALUES (1,'Admin'),(2,'Employee'),(3,'Customer');
/*!40000 ALTER TABLE `roles` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `subscription`
--

DROP TABLE IF EXISTS `subscription`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `subscription` (
  `subscriptionID` int unsigned NOT NULL AUTO_INCREMENT,
  `subscriptionStartDate` date NOT NULL,
  `subscriptionEndDate` date NOT NULL,
  `subscriptionDailyPrice` double NOT NULL,
  `carFK_ID` int unsigned NOT NULL,
  `userFK_ID` int unsigned NOT NULL,
  PRIMARY KEY (`subscriptionID`),
  UNIQUE KEY `subscriptionID_UNIQUE` (`subscriptionID`),
  KEY `carFK_idx` (`carFK_ID`),
  KEY `userFK_idx` (`userFK_ID`),
  CONSTRAINT `carFK` FOREIGN KEY (`carFK_ID`) REFERENCES `car` (`carID`),
  CONSTRAINT `userFK` FOREIGN KEY (`userFK_ID`) REFERENCES `users` (`userID`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `subscription`
--

LOCK TABLES `subscription` WRITE;
/*!40000 ALTER TABLE `subscription` DISABLE KEYS */;
INSERT INTO `subscription` VALUES (1,'2024-05-10','2024-05-14',45,1,1),(2,'2024-05-03','2024-05-09',65,2,2),(3,'2024-05-01','2024-05-03',65,3,3),(4,'2024-05-04','2024-05-06',44,4,4),(5,'2024-05-03','2024-05-06',63,5,5),(6,'2024-05-02','2024-05-04',75,6,6),(7,'2024-05-04','2024-05-10',46,7,7),(8,'2024-05-03','2024-05-05',85,8,8),(9,'2024-05-10','2024-05-11',82,9,9),(10,'2024-05-11','2024-05-13',53,10,10);
/*!40000 ALTER TABLE `subscription` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users` (
  `userID` int unsigned NOT NULL AUTO_INCREMENT,
  `firstName` varchar(31) DEFAULT NULL,
  `lastName` varchar(31) DEFAULT NULL,
  `roleFK_ID` int unsigned NOT NULL,
  PRIMARY KEY (`userID`),
  UNIQUE KEY `userID_UNIQUE` (`userID`),
  KEY `roleFK_idx` (`roleFK_ID`),
  CONSTRAINT `roleFK` FOREIGN KEY (`roleFK_ID`) REFERENCES `roles` (`roleID`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (1,'Emily','Patel',2),(2,'Ethan','Rodriguez',3),(3,'Sophia','Nguyen',3),(4,'Liam','Smith',1),(5,'Olivia','Brown',3),(6,'Noah','Garcia',2),(7,'Isabella','Taylor',3),(8,'Mason','Martinez',3),(9,'Ava','Anderson',3),(10,'Jacob','Thompson',3);
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping events for database 'car_rental'
--

--
-- Dumping routines for database 'car_rental'
--
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-05-21 11:04:55
