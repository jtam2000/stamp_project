CREATE TABLE `Stamps` (
  `Stamp_ID` int(11) NOT NULL AUTO_INCREMENT,
  `Issue_Date` date DEFAULT NULL,
  `Set_ID` varchar(180) NOT NULL COMMENT 'Foreign key to the Set Table',
  `Set_Member_ID` int(11) NOT NULL DEFAULT '1',
  `Name` varchar(200) NOT NULL,
  `Description` varchar(1000) DEFAULT NULL,
  PRIMARY KEY (`Stamp_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;



CREATE TABLE `Sets` (
  `Internal_ID` int(11) NOT NULL AUTO_INCREMENT,
  `ID` varchar(180) NOT NULL,
  `Country` varchar(3) NOT NULL,
  `Name` varchar(200) NOT NULL,
  `Description` varchar(1000) DEFAULT NULL,
  `Ordinality` int(11) NOT NULL DEFAULT '1',
  PRIMARY KEY (`Internal_ID`,`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;


CREATE TABLE `Valuation` (
  `ID` INT(11) NOT NULL AUTO_INCREMENT,
  `Stamp_ID` INT(11) NULL,
  `Market_Value` FLOAT NULL,
  `Value_Date` DATE NULL,
  `Valuation_Source` INT(11) NULL,
  PRIMARY KEY (`ID`),
  UNIQUE INDEX `Value_Date_UNIQUE` (`Value_Date` ASC) VISIBLE);


CREATE TABLE `Valuation_Source` (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `Name` varchar(200) NOT NULL,
  `Description` varchar(1000) DEFAULT NULL,
  PRIMARY KEY (`ID`,`Name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;



CREATE TABLE `Valuation` (
  `ID` INT(11) NOT NULL AUTO_INCREMENT,
  `Stamp_ID` INT(11) NULL,
  `Market_Value` FLOAT NULL,
  `Value_Date` DATE NULL,
  `Valuation_Source` INT(11) NULL,
  PRIMARY KEY (`ID`),
  UNIQUE INDEX `Value_Date_UNIQUE` (`Value_Date` ASC) VISIBLE);


CREATE TABLE `Inventory` (
  `ID` int(11) NOT NULL,
  `Stamp_ID` int(11) NOT NULL,
  `count` int(11) NOT NULL DEFAULT '0',
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;



CREATE TABLE `Tags` (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `Stamp_ID` int(11) NOT NULL,
  `Tag_ID` varchar(200) NOT NULL COMMENT 'Foreign key into Tag_List Table',
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;


CREATE TABLE `Tag_List` (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `Tag` varchar(200) NOT NULL,
  `Description` varchar(1000) DEFAULT NULL,
  PRIMARY KEY (`ID`,`Tag`),
  UNIQUE KEY `Tag_UNIQUE` (`Tag`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
