-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:3306
-- Generation Time: Nov 29, 2021 at 01:02 PM
-- Server version: 10.4.21-MariaDB-log
-- PHP Version: 8.0.10

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `museum`
--

-- --------------------------------------------------------

--
-- Table structure for table `account`
--

CREATE TABLE `account` (
  `AccountId` int(4) NOT NULL,
  `displayName` varchar(100) NOT NULL,
  `email` varchar(50) NOT NULL,
  `Phone` varchar(50) NOT NULL,
  `Password` varchar(50) NOT NULL,
  `DOB` date NOT NULL,
  `RoleId` int(4) NOT NULL,
  `RecoverPasswordCode` varchar(50) DEFAULT NULL,
  `ExpiredTimeCode` date DEFAULT NULL,
  `FacebookId` varchar(50) DEFAULT NULL,
  `GoogleId` varchar(50) DEFAULT NULL,
  `CreateAt` date DEFAULT NULL,
  `UpdateAt` date DEFAULT NULL,
  `ImageId` int(4) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `accountfavoriteartifact`
--

CREATE TABLE `accountfavoriteartifact` (
  `AccountId` int(4) NOT NULL,
  `ArtifactId` int(4) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `accountfavoriteevent`
--

CREATE TABLE `accountfavoriteevent` (
  `AccountId` int(4) NOT NULL,
  `EventId` int(4) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `accounttest`
--

CREATE TABLE `accounttest` (
  `AccountId` int(4) NOT NULL,
  `email` varchar(50) NOT NULL,
  `Password` varchar(10000) NOT NULL,
  `RoleId` int(4) DEFAULT NULL,
  `isActivated` tinyint(4) NOT NULL,
  `confirmedAt` datetime DEFAULT NULL,
  `GoogleId` varchar(50) DEFAULT NULL,
  `CreateAt` datetime DEFAULT NULL,
  `UpdateAt` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `accounttest`
--

INSERT INTO `accounttest` (`AccountId`, `email`, `Password`, `RoleId`, `isActivated`, `confirmedAt`, `GoogleId`, `CreateAt`, `UpdateAt`) VALUES
(51, '19020204@vnu.edu.vn', 'sha256$sM58UADvQuaY8nS3$e93d9a4c4d65527f77a2632469176936f43af93ed48c62da488bd169d4e56818', NULL, 0, NULL, NULL, '2021-11-26 21:32:17', NULL),
(52, '19020484@vnu.edu.vn', 'sha256$TGnG37sWbuUlT8Ct$634bb2437318745d55b90e58972fdbf059e8e51545de0c5c06472b8f02d732d2', NULL, 0, NULL, NULL, '2021-11-26 21:32:32', NULL),
(53, 'trangco19621962@gmail.com', 'sha256$bx4zNfp9rPsQc289$5cea5819f71c66983a4ea1c798a087721d0ce89afc0ea2d9a524862cdcc23dc7', NULL, 1, '2021-11-28 18:40:44', NULL, '2021-11-28 18:40:08', NULL);

-- --------------------------------------------------------

--
-- Table structure for table `agegroup`
--

CREATE TABLE `agegroup` (
  `    GroupId` int(4) NOT NULL,
  `    Description` varchar(500) NOT NULL,
  `    Price` decimal(10,2) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `artifact`
--

CREATE TABLE `artifact` (
  `ArtifactId` int(4) NOT NULL,
  `Name` varchar(50) NOT NULL,
  `Description` varchar(1000) NOT NULL,
  `Level` int(1) NOT NULL,
  `ImageId` int(4) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `artifacttype`
--

CREATE TABLE `artifacttype` (
  `ArtifactTypeId` int(4) NOT NULL,
  `Name` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `artifacttypemapping`
--

CREATE TABLE `artifacttypemapping` (
  `ArtifactId` int(4) NOT NULL,
  `ArtifactTypeId` int(4) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `entrytiket`
--

CREATE TABLE `entrytiket` (
  `TicketId` int(4) NOT NULL,
  `OrderId` int(4) NOT NULL,
  `TiketDate` date NOT NULL,
  `TimeFrameId` int(4) NOT NULL,
  `NumberPerson` int(2) NOT NULL,
  `TicketType` int(4) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `image`
--

CREATE TABLE `image` (
  `ImageId` int(4) NOT NULL,
  `Name` varchar(22) NOT NULL,
  `Content` varchar(100) DEFAULT NULL,
  `Url` varchar(100) DEFAULT NULL,
  `Path` varchar(100) DEFAULT NULL,
  `MimeType` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `museumevent`
--

CREATE TABLE `museumevent` (
  `EventId` int(4) NOT NULL,
  `Description` varchar(300) NOT NULL,
  `OpenTime` date NOT NULL,
  `CloseTime` date NOT NULL,
  `EventDate` date NOT NULL,
  `Poster` int(4) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `notification`
--

CREATE TABLE `notification` (
  `NotificationId` int(4) NOT NULL,
  `AccountId` int(4) NOT NULL,
  `Title` varchar(50) NOT NULL,
  `Content` varchar(200) NOT NULL,
  `Time` date NOT NULL,
  `Unread` int(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `orders`
--

CREATE TABLE `orders` (
  `OrderId` int(4) NOT NULL,
  `OrderDate` date NOT NULL,
  `ToatlPrice` int(30) NOT NULL,
  `CreatedAt` date NOT NULL,
  `UpdateAt` date DEFAULT NULL,
  `deletedAt` date DEFAULT NULL,
  `AccountId` int(4) NOT NULL,
  `QRCode` varchar(100) DEFAULT NULL,
  `Discount` decimal(2,2) DEFAULT NULL,
  `IsActivated` int(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `orderssouvenirdetail`
--

CREATE TABLE `orderssouvenirdetail` (
  `OrderId` int(4) NOT NULL,
  `SouvenirId` int(4) NOT NULL,
  `Quantity` int(2) NOT NULL,
  `PriceEach` int(4) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `rattings`
--

CREATE TABLE `rattings` (
  `RattingId` int(4) NOT NULL,
  `Star` int(1) NOT NULL,
  `Description` varchar(500) DEFAULT NULL,
  `AccountId` int(4) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `revoked_tokens`
--

CREATE TABLE `revoked_tokens` (
  `id` int(11) NOT NULL,
  `jti` varchar(120) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `revoked_tokens`
--

INSERT INTO `revoked_tokens` (`id`, `jti`) VALUES
(1, '4a676677-9e77-4f21-8ce2-d9fec624180f'),
(2, 'f4c2cdea-7536-45a8-9356-0c095993fdbd');

-- --------------------------------------------------------

--
-- Table structure for table `souvenir`
--

CREATE TABLE `souvenir` (
  `SouvenirId` int(4) NOT NULL,
  `Description` varchar(500) NOT NULL,
  `Price` int(3) NOT NULL,
  `Discount` decimal(2,2) DEFAULT NULL,
  `ImageId` int(4) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `timeframe`
--

CREATE TABLE `timeframe` (
  `    TimeFrameId` int(4) NOT NULL,
  `    Description` varchar(500) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `account`
--
ALTER TABLE `account`
  ADD PRIMARY KEY (`AccountId`),
  ADD KEY `fk_account_image` (`ImageId`);

--
-- Indexes for table `accountfavoriteartifact`
--
ALTER TABLE `accountfavoriteartifact`
  ADD PRIMARY KEY (`ArtifactId`,`AccountId`) USING BTREE,
  ADD KEY `fk_AccountFavoriteArtifact_Account` (`AccountId`),
  ADD KEY `fk_AccountFavoriteArtifact_Artifact` (`ArtifactId`);

--
-- Indexes for table `accountfavoriteevent`
--
ALTER TABLE `accountfavoriteevent`
  ADD PRIMARY KEY (`AccountId`,`EventId`),
  ADD KEY `fk_AccountFavoriteEvent_Account` (`AccountId`),
  ADD KEY `fk_AccountFavoriteEvent_MuseumEvent` (`EventId`);

--
-- Indexes for table `accounttest`
--
ALTER TABLE `accounttest`
  ADD PRIMARY KEY (`AccountId`);

--
-- Indexes for table `agegroup`
--
ALTER TABLE `agegroup`
  ADD PRIMARY KEY (`    GroupId`);

--
-- Indexes for table `artifact`
--
ALTER TABLE `artifact`
  ADD PRIMARY KEY (`ArtifactId`),
  ADD KEY `fk_artifact_image` (`ImageId`);

--
-- Indexes for table `artifacttype`
--
ALTER TABLE `artifacttype`
  ADD PRIMARY KEY (`ArtifactTypeId`);

--
-- Indexes for table `artifacttypemapping`
--
ALTER TABLE `artifacttypemapping`
  ADD PRIMARY KEY (`ArtifactId`,`ArtifactTypeId`),
  ADD UNIQUE KEY `fk_artifacttypemapping_artifact` (`ArtifactId`),
  ADD KEY `fk_ArtifactTypeMapping_ArtifactType` (`ArtifactTypeId`);

--
-- Indexes for table `entrytiket`
--
ALTER TABLE `entrytiket`
  ADD PRIMARY KEY (`TicketId`),
  ADD KEY `fk_entryticket_TimeFrame` (`TimeFrameId`),
  ADD KEY `fk_entryticket_AgeGroup` (`TicketType`),
  ADD KEY `fk_entryticket_Orders` (`OrderId`);

--
-- Indexes for table `image`
--
ALTER TABLE `image`
  ADD PRIMARY KEY (`ImageId`);

--
-- Indexes for table `museumevent`
--
ALTER TABLE `museumevent`
  ADD PRIMARY KEY (`EventId`),
  ADD KEY `fk_museumevent_image` (`Poster`);

--
-- Indexes for table `notification`
--
ALTER TABLE `notification`
  ADD PRIMARY KEY (`NotificationId`),
  ADD KEY `fk_notification_account` (`AccountId`);

--
-- Indexes for table `orders`
--
ALTER TABLE `orders`
  ADD PRIMARY KEY (`OrderId`),
  ADD KEY `fk_orders_account` (`AccountId`);

--
-- Indexes for table `orderssouvenirdetail`
--
ALTER TABLE `orderssouvenirdetail`
  ADD PRIMARY KEY (`OrderId`,`SouvenirId`),
  ADD KEY `fk_OrdersSouvenirDetail_Orders` (`OrderId`),
  ADD KEY `fk_orderssouvenirdetail_souvenir` (`SouvenirId`);

--
-- Indexes for table `rattings`
--
ALTER TABLE `rattings`
  ADD PRIMARY KEY (`RattingId`),
  ADD KEY `fk_rattings_account` (`AccountId`);

--
-- Indexes for table `revoked_tokens`
--
ALTER TABLE `revoked_tokens`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `souvenir`
--
ALTER TABLE `souvenir`
  ADD PRIMARY KEY (`SouvenirId`),
  ADD KEY `fk_sou` (`ImageId`);

--
-- Indexes for table `timeframe`
--
ALTER TABLE `timeframe`
  ADD PRIMARY KEY (`    TimeFrameId`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `account`
--
ALTER TABLE `account`
  MODIFY `AccountId` int(4) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `accounttest`
--
ALTER TABLE `accounttest`
  MODIFY `AccountId` int(4) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=54;

--
-- AUTO_INCREMENT for table `agegroup`
--
ALTER TABLE `agegroup`
  MODIFY `    GroupId` int(4) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `artifact`
--
ALTER TABLE `artifact`
  MODIFY `ArtifactId` int(4) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `artifacttype`
--
ALTER TABLE `artifacttype`
  MODIFY `ArtifactTypeId` int(4) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `entrytiket`
--
ALTER TABLE `entrytiket`
  MODIFY `TicketId` int(4) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `image`
--
ALTER TABLE `image`
  MODIFY `ImageId` int(4) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `museumevent`
--
ALTER TABLE `museumevent`
  MODIFY `EventId` int(4) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `notification`
--
ALTER TABLE `notification`
  MODIFY `NotificationId` int(4) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `orders`
--
ALTER TABLE `orders`
  MODIFY `OrderId` int(4) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `rattings`
--
ALTER TABLE `rattings`
  MODIFY `RattingId` int(4) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `revoked_tokens`
--
ALTER TABLE `revoked_tokens`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `souvenir`
--
ALTER TABLE `souvenir`
  MODIFY `SouvenirId` int(4) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `timeframe`
--
ALTER TABLE `timeframe`
  MODIFY `    TimeFrameId` int(4) NOT NULL AUTO_INCREMENT;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `account`
--
ALTER TABLE `account`
  ADD CONSTRAINT `fk_account_image` FOREIGN KEY (`ImageId`) REFERENCES `image` (`ImageId`);

--
-- Constraints for table `accountfavoriteartifact`
--
ALTER TABLE `accountfavoriteartifact`
  ADD CONSTRAINT `fk_AccountFavoriteArtifact_Account` FOREIGN KEY (`AccountId`) REFERENCES `account` (`AccountId`),
  ADD CONSTRAINT `fk_AccountFavoriteArtifact_Artifact` FOREIGN KEY (`ArtifactId`) REFERENCES `artifact` (`ArtifactId`);

--
-- Constraints for table `accountfavoriteevent`
--
ALTER TABLE `accountfavoriteevent`
  ADD CONSTRAINT `fk_AccountFavoriteEvent_Account` FOREIGN KEY (`AccountId`) REFERENCES `account` (`AccountId`),
  ADD CONSTRAINT `fk_AccountFavoriteEvent_MuseumEvent` FOREIGN KEY (`EventId`) REFERENCES `museumevent` (`EventId`);

--
-- Constraints for table `artifact`
--
ALTER TABLE `artifact`
  ADD CONSTRAINT `fk_artifact_image` FOREIGN KEY (`ImageId`) REFERENCES `image` (`ImageId`);

--
-- Constraints for table `artifacttypemapping`
--
ALTER TABLE `artifacttypemapping`
  ADD CONSTRAINT `fk_ArtifactTypeMapping_ArtifactType` FOREIGN KEY (`ArtifactTypeId`) REFERENCES `artifacttype` (`ArtifactTypeId`),
  ADD CONSTRAINT `fk_artifacttypemapping_artifact` FOREIGN KEY (`ArtifactId`) REFERENCES `artifact` (`ArtifactId`);

--
-- Constraints for table `entrytiket`
--
ALTER TABLE `entrytiket`
  ADD CONSTRAINT `fk_entryticket_AgeGroup` FOREIGN KEY (`TicketType`) REFERENCES `agegroup` (`    GroupId`),
  ADD CONSTRAINT `fk_entryticket_Orders` FOREIGN KEY (`OrderId`) REFERENCES `orders` (`OrderId`),
  ADD CONSTRAINT `fk_entryticket_TimeFrame` FOREIGN KEY (`TimeFrameId`) REFERENCES `timeframe` (`    TimeFrameId`);

--
-- Constraints for table `museumevent`
--
ALTER TABLE `museumevent`
  ADD CONSTRAINT `fk_museumevent_image` FOREIGN KEY (`Poster`) REFERENCES `image` (`ImageId`);

--
-- Constraints for table `notification`
--
ALTER TABLE `notification`
  ADD CONSTRAINT `fk_notification_account` FOREIGN KEY (`AccountId`) REFERENCES `account` (`AccountId`);

--
-- Constraints for table `orders`
--
ALTER TABLE `orders`
  ADD CONSTRAINT `fk_orders_account` FOREIGN KEY (`AccountId`) REFERENCES `account` (`AccountId`);

--
-- Constraints for table `orderssouvenirdetail`
--
ALTER TABLE `orderssouvenirdetail`
  ADD CONSTRAINT `fk_OrdersSouvenirDetail_Orders` FOREIGN KEY (`OrderId`) REFERENCES `orders` (`OrderId`),
  ADD CONSTRAINT `fk_orderssouvenirdetail_souvenir` FOREIGN KEY (`SouvenirId`) REFERENCES `souvenir` (`SouvenirId`);

--
-- Constraints for table `rattings`
--
ALTER TABLE `rattings`
  ADD CONSTRAINT `fk_rattings_account` FOREIGN KEY (`AccountId`) REFERENCES `account` (`AccountId`);

--
-- Constraints for table `souvenir`
--
ALTER TABLE `souvenir`
  ADD CONSTRAINT `fk_sou` FOREIGN KEY (`ImageId`) REFERENCES `image` (`ImageId`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
