CREATE DATABASE IF NOT EXISTS `RadRacoons`;
USE `RadRacoons`;

--
-- Table structure for table `people`
--

DROP TABLE IF EXISTS `People`;
CREATE TABLE `People` (
  `playerID` varchar(9) NOT NULL,
  `birthYear` int(12) DEFAULT NULL,
  `birthMonth` int(12) DEFAULT NULL,
  `birthDay` int(12) DEFAULT NULL,
  `birthCountry` varchar(255) DEFAULT NULL,
  `birthState` varchar(255) DEFAULT NULL,
  `birthCity` varchar(255) DEFAULT NULL,
  `deathYear` int(12) DEFAULT NULL,
  `deathMonth` int(12) DEFAULT NULL,
  `deathDay` int(12) DEFAULT NULL,
  `deathCountry` varchar(255) DEFAULT NULL,
  `deathState` varchar(255) DEFAULT NULL,
  `deathCity` varchar(255) DEFAULT NULL,
  `nameFirst` varchar(255) DEFAULT NULL,
  `nameLast` varchar(255) DEFAULT NULL,
  `nameGiven` varchar(255) DEFAULT NULL,
  `weight` int(10) DEFAULT NULL,
  `height` int(10) DEFAULT NULL,
  `bats` varchar(255) DEFAULT NULL,
  `throws` varchar(255) DEFAULT NULL,
  `debutDate` date DEFAULT NULL,
  `finalGameDate` date DEFAULT NULL,
  PRIMARY KEY (`playerID`)
);

--
-- Table structure for table `allstarfull`
--

DROP TABLE IF EXISTS `AllStarFull`;
CREATE TABLE `AllStarFull` (
  `ID` int(12) NOT NULL AUTO_INCREMENT,
  `playerID` varchar(9) NOT NULL,
  `lgID` char(2) DEFAULT NULL,
  `teamID` char(3) NOT NULL,
  `yearID` smallint(6) NOT NULL,
  `gameNum` smallint(6) DEFAULT NULL,
  `gameID` varchar(12) DEFAULT NULL,
  `GP` smallint(6) DEFAULT NULL,
  `startingPos` smallint(6) DEFAULT NULL,
  PRIMARY KEY (`ID`),
  KEY `fk_allstar_peo` (`playerID`),
  CONSTRAINT `fk_allstar_peo` FOREIGN KEY (`playerID`) REFERENCES `people` (`playerID`)
);

--
-- Table structure for table `appearances`
-- !!Does not contain league id

DROP TABLE IF EXISTS `Appearances`;
CREATE TABLE `Appearances` (
  `ID` int(12) NOT NULL AUTO_INCREMENT,
  `playerID` varchar(9) NOT NULL,
  `yearID` smallint(6) NOT NULL,
  `teamId` char(3) NOT NULL,
  `lgID` char(2) DEFAULT NULL,
  `G_all` smallint(6) DEFAULT NULL,
  `GS` smallint(6) DEFAULT NULL,
  `G_batting` smallint(6) DEFAULT NULL,
  `G_defense` smallint(6) DEFAULT NULL,
  `G_p` smallint(6) DEFAULT NULL,
  `G_c` smallint(6) DEFAULT NULL,
  `G_1b` smallint(6) DEFAULT NULL,
  `G_2b` smallint(6) DEFAULT NULL,
  `G_3b` smallint(6) DEFAULT NULL,
  `G_ss` smallint(6) DEFAULT NULL,
  `G_lf` smallint(6) DEFAULT NULL,
  `G_cf` smallint(6) DEFAULT NULL,
  `G_rf` smallint(6) DEFAULT NULL,
  `G_of` smallint(6) DEFAULT NULL,
  `G_dh` smallint(6) DEFAULT NULL,
  `G_ph` smallint(6) DEFAULT NULL,
  `G_pr` smallint(6) DEFAULT NULL,
  PRIMARY KEY (`ID`),
  KEY `k_app_team` (`teamId`)
);

--
-- Table structure for table `awards`
--

DROP TABLE IF EXISTS `Awards`;
CREATE TABLE `Awards` (
  `ID` int(12) NOT NULL AUTO_INCREMENT,
  `playerID` varchar(9) NOT NULL,
  `awardID` varchar(255) NOT NULL,
  `yearID` smallint(6) NOT NULL,
  `lgID` char(2) DEFAULT NULL,
  `tie`varchar(2) DEFAULT NULL,
  `notes` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`ID`),
  KEY `awards_player` (`playerID`)
  );

--
-- Table structure for table `awardsshare`
--
DROP TABLE IF EXISTS `AwardsShare`;
CREATE TABLE `AwardsShare` (
  `ID` int(12) NOT NULL AUTO_INCREMENT,
  `awardID` varchar(255) NOT NULL,
  `yearID` smallint(6) NOT NULL,
  `lgID` char(2) DEFAULT NULL,
  `playerID` varchar(9) NOT NULL,
  `pointsWon` double DEFAULT NULL,
  `pointsMax` smallint(6) DEFAULT NULL,
  `votesFirst` double DEFAULT NULL,
  PRIMARY KEY (`ID`),
  KEY `awardsshare_player` (`playerID`)
);

--
-- Table structure for table `batting`
--

DROP TABLE IF EXISTS `Batting`;
CREATE TABLE `Batting` (
  `ID` int(12) NOT NULL AUTO_INCREMENT,
  `playerID` varchar(9) NOT NULL,
  `yearID` smallint(6) NOT NULL,
  `teamID` char(3) NOT NULL,
  `lgID` char(2) DEFAULT NULL,
  `stint` smallint(4) NOT NULL,
  `b_G` smallint(6) DEFAULT NULL,
  `b_AB` smallint(6) DEFAULT NULL,
  `b_R` smallint(6) DEFAULT NULL,
  `b_H` smallint(6) DEFAULT NULL,
  `b_2B` smallint(6) DEFAULT NULL,
  `b_3B` smallint(6) DEFAULT NULL,
  `b_HR` smallint(6) DEFAULT NULL,
  `b_RBI` smallint(6) DEFAULT NULL,
  `b_SB` smallint(6) DEFAULT NULL,
  `b_CS` smallint(6) DEFAULT NULL,
  `b_BB` smallint(6) DEFAULT NULL,
  `b_SO` smallint(6) DEFAULT NULL,
  `b_IBB` smallint(6) DEFAULT NULL,
  `b_HBP` smallint(6) DEFAULT NULL,
  `b_SH` smallint(6) DEFAULT NULL,
  `b_SF` smallint(6) DEFAULT NULL,
  `b_GIDP` smallint(6) DEFAULT NULL,
  PRIMARY KEY (`ID`),
  KEY `k_bat_team` (`teamID`),
  KEY `k_bat_player` (`playerID`)
);

--
-- Table structure for table `battingpost`
--

DROP TABLE IF EXISTS `BattingPost`;
CREATE TABLE `BattingPost` (
  `ID` int(12) NOT NULL AUTO_INCREMENT,
  `playerID` varchar(9) NOT NULL,
  `yearID` smallint(6) NOT NULL,
  `teamID` char(3) NOT NULL,
  `round` varchar(10) DEFAULT NULL,
  `lgID` varchar(2) DEFAULT NULL,
  `bp_G` smallint(6) DEFAULT NULL,
  `bp_AB` smallint(6) DEFAULT NULL,
  `bp_R` smallint(6) DEFAULT NULL,
  `bp_H` smallint(6) DEFAULT NULL,
  `bp_2B` smallint(6) DEFAULT NULL,
  `bp_3B` smallint(6) DEFAULT NULL,
  `bp_HR` smallint(6) DEFAULT NULL,
  `bp_RBI` smallint(6) DEFAULT NULL,
  `bp_SB` smallint(6) DEFAULT NULL,
  `bp_CS` smallint(6) DEFAULT NULL,
  `bp_BB` smallint(6) DEFAULT NULL,
  `bp_SO` smallint(6) DEFAULT NULL,
  `bp_IBB` smallint(6) DEFAULT NULL,
  `bp_HBP` smallint(6) DEFAULT NULL,
  `bp_SH` smallint(6) DEFAULT NULL,
  `bp_SF` smallint(6) DEFAULT NULL,
  `bp_GIDP` smallint(6) DEFAULT NULL,
  PRIMARY KEY (`ID`),
  KEY `k_bp_team` (`teamID`),
  KEY `k_bp_player` (`playerID`)
);

--
-- Table structure for table `fielding`
--  

DROP TABLE IF EXISTS `Fielding`;
CREATE TABLE `Fielding` (
  `ID` int(12) NOT NULL AUTO_INCREMENT,
  `playerID` varchar(9) NOT NULL,
  `yearID` smallint(6) NOT NULL,
  `teamID` char(3) NOT NULL,
  `stint` smallint(4) NOT NULL,
  `lgID` char(2) DEFAULT NULL,
  `position` varchar(2) DEFAULT NULL,
  `f_G` smallint(6) DEFAULT NULL,
  `f_GS` smallint(6) DEFAULT NULL,
  `f_InnOuts` smallint(6) DEFAULT NULL,
  `f_PO` smallint(6) DEFAULT NULL,
  `f_A` smallint(6) DEFAULT NULL,
  `f_E` smallint(6) DEFAULT NULL,
  `f_DP` smallint(6) DEFAULT NULL,
  `f_PB` smallint(6) DEFAULT NULL,
  `f_WP` smallint(6) DEFAULT NULL,
  `f_SB` smallint(6) DEFAULT NULL,
  `f_CS` smallint(6) DEFAULT NULL,
  `f_ZR` double DEFAULT NULL,
  PRIMARY KEY (`ID`),
  KEY `k_fie_team` (`teamID`),
  KEY `k_fie_player` (`playerID`)
);

-- 
-- Table structure for table `fieldingpost`
--

DROP TABLE IF EXISTS `FieldingPost`;
CREATE TABLE `FieldingPost` (
  `ID` int(12) NOT NULL AUTO_INCREMENT,
  `playerID` varchar(9) NOT NULL,
  `yearID` smallint(6) NOT NULL,
  `teamID` char(3) NOT NULL,
  `lgID` char(2) DEFAULT NULL,
  `round` varchar(10) DEFAULT NULL,
  `position` varchar(2) DEFAULT NULL,
  `fp_G` smallint(6) DEFAULT NULL,
  `fp_GS` smallint(6) DEFAULT NULL,
  `fp_InnOuts` smallint(6) DEFAULT NULL,
  `fp_PO` smallint(6) DEFAULT NULL,
  `fp_A` smallint(6) DEFAULT NULL,
  `fp_E` smallint(6) DEFAULT NULL,
  `fp_DP` smallint(6) DEFAULT NULL,
  `fp_PB` smallint(6) DEFAULT NULL,
  `fp_WP` smallint(6) DEFAULT NULL,
  `fp_SB` smallint(6) DEFAULT NULL,
  `fp_CS` smallint(6) DEFAULT NULL,
  `fp_ZR` double DEFAULT NULL,
  PRIMARY KEY (`ID`),
  KEY `k_fp_team` (`teamID`),
  KEY `k_fp_player` (`playerID`)
);

--
-- Table structure for table `franchises`
--

DROP TABLE IF EXISTS `Franchises`;
CREATE TABLE `Franchises` (
  `franchID` varchar(3) NOT NULL,
  `franchName` varchar(50) DEFAULT NULL,
  `active` char(2) DEFAULT NULL,
  `NAassoc` varchar(3) DEFAULT NULL,
  PRIMARY KEY (`franchID`)
);

--
-- Table structure for table `halloffame`
--

DROP TABLE IF EXISTS `HallOfFame`;
CREATE TABLE `HallOfFame` (
  `ID` int(12) NOT NULL AUTO_INCREMENT,
  `playerID` varchar(9) NOT NULL,
  `yearID` smallint(6) NOT NULL,
  `votedBy` varchar(64) NOT NULL,
  `ballots` smallint(6) DEFAULT NULL,
  `needed` smallint(6) DEFAULT NULL,
  `votes` smallint(6) DEFAULT NULL,
  `inducted` char(1) DEFAULT NULL,
  `category` varchar(64) DEFAULT NULL,
  PRIMARY KEY (`ID`),
  KEY `fk_people` (`playerID`),
  CONSTRAINT `fk_people` FOREIGN KEY (`playerID`) REFERENCES `people` (`playerID`)
);

--
-- Table structure for table `homegames`
--

DROP TABLE IF EXISTS `HomeGames`;
CREATE TABLE `HomeGames` (
  `ID` int(12) NOT NULL AUTO_INCREMENT,
  `teamID` char(3) NOT NULL,
  `parkID` varchar(255) NOT NULL,
  `yearID` smallint(6) NOT NULL,
  `lgID` char(2) DEFAULT NULL,
  `firstGame` date DEFAULT NULL,
  `lastGame` date DEFAULT NULL,
  `games` int(11) DEFAULT NULL,
  `openings` int(11) DEFAULT NULL,
  `attendance` int(11) DEFAULT NULL,
  PRIMARY KEY (`ID`),
  KEY `k_hg_park` (`parkID`)
);

--
-- Table structure for table `manager`
--

DROP TABLE IF EXISTS `Manager`;
CREATE TABLE `Manager` (
  `ID` int(12) NOT NULL AUTO_INCREMENT,
  `playerID` varchar(9) NOT NULL,
  `yearID` smallint(6) NOT NULL,
  `teamID` char(3) NOT NULL,
  `lgID` char(2) DEFAULT NULL,
  `inSeason` smallint(6) NOT NULL,
  `manager_G` smallint(6) DEFAULT NULL,
  `manager_W` smallint(6) DEFAULT NULL,
  `manager_L` smallint(6) DEFAULT NULL,
  `teamRank` smallint(6) DEFAULT NULL,
  `plyrMgr` varchar(1) DEFAULT NULL,
  PRIMARY KEY (`ID`),
  KEY `fk_man_person` (`playerID`),
  CONSTRAINT `fk_man_person` FOREIGN KEY (`playerID`) REFERENCES `people` (`playerID`)
);

--
-- Table structure for table `park`
--

DROP TABLE IF EXISTS `Park`;
CREATE TABLE `Park` (
  `ID` int(12) NOT NULL AUTO_INCREMENT,
  `parkID` varchar(255) NOT NULL,
  `park_alias` varchar(255) DEFAULT NULL,
  `park_name` varchar(255) DEFAULT NULL,
  `city` varchar(255) DEFAULT NULL,
  `state` varchar(255) DEFAULT NULL,
  `country` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`ID`)
);



--
-- Table structure for table `pitching`
--

DROP TABLE IF EXISTS `Pitching`;
CREATE TABLE `Pitching` (
  `ID` int(12) NOT NULL AUTO_INCREMENT,
  `playerID` varchar(9) NOT NULL,
  `yearID` smallint(6) NOT NULL,
  `teamID` char(3) NOT NULL,
  `lgID` char(2) DEFAULT NULL,
  `stint` smallint(4) NOT NULL,
  `p_W` smallint(6) DEFAULT NULL,
  `p_L` smallint(6) DEFAULT NULL,
  `p_G` smallint(6) DEFAULT NULL,
  `p_GS` smallint(6) DEFAULT NULL,
  `p_CG` smallint(6) DEFAULT NULL,
  `p_SHO` smallint(6) DEFAULT NULL,
  `p_SV` smallint(6) DEFAULT NULL,
  `p_IPOuts` int(11) DEFAULT NULL,
  `p_H` smallint(6) DEFAULT NULL,
  `p_ER` smallint(6) DEFAULT NULL,
  `p_HR` smallint(6) DEFAULT NULL,
  `p_BB` smallint(6) DEFAULT NULL,
  `p_SO` smallint(6) DEFAULT NULL,
  `p_BAOpp` double DEFAULT NULL,
  `p_ERA` double DEFAULT NULL,
  `p_IBB` smallint(6) DEFAULT NULL,
  `p_WP` smallint(6) DEFAULT NULL,
  `p_HBP` smallint(6) DEFAULT NULL,
  `p_BK` smallint(6) DEFAULT NULL,
  `p_BFP` smallint(6) DEFAULT NULL,
  `p_GF` smallint(6) DEFAULT NULL,
  `p_R` smallint(6) DEFAULT NULL,
  `p_SH` smallint(6) DEFAULT NULL,
  `p_SF` smallint(6) DEFAULT NULL,
  `p_GIDP` smallint(6) DEFAULT NULL,
  PRIMARY KEY (`ID`),
  KEY `k_pit_team` (`teamID`),
  KEY `k_pit_player` (`playerID`)
);

--
-- Table structure for table `pitchingpost`
--

DROP TABLE IF EXISTS `PitchingPost`;
CREATE TABLE `PitchingPost` (
  `ID` int(12) NOT NULL AUTO_INCREMENT,
  `playerID` varchar(9) NOT NULL,
  `yearID` smallint(6) NOT NULL,
  `teamID` char(3) NOT NULL,
  `lgID` char(2) DEFAULT NULL,
  `round` varchar(10) DEFAULT NULL,
  `pp_W` smallint(6) DEFAULT NULL,
  `pp_L` smallint(6) DEFAULT NULL,
  `pp_G` smallint(6) DEFAULT NULL,
  `pp_GS` smallint(6) DEFAULT NULL,
  `pp_CG` smallint(6) DEFAULT NULL,
  `pp_SHO` smallint(6) DEFAULT NULL,
  `pp_SV` smallint(6) DEFAULT NULL,
  `pp_IPOuts` int(11) DEFAULT NULL,
  `pp_H` smallint(6) DEFAULT NULL,
  `pp_ER` smallint(6) DEFAULT NULL,
  `pp_HR` smallint(6) DEFAULT NULL,
  `pp_BB` smallint(6) DEFAULT NULL,
  `pp_SO` smallint(6) DEFAULT NULL,
  `pp_BAOpp` double DEFAULT NULL,
  `pp_ERA` double DEFAULT NULL,
  `pp_IBB` smallint(6) DEFAULT NULL,
  `pp_WP` smallint(6) DEFAULT NULL,
  `pp_HBP` smallint(6) DEFAULT NULL,
  `pp_BK` smallint(6) DEFAULT NULL,
  `pp_BFP` smallint(6) DEFAULT NULL,
  `pp_GF` smallint(6) DEFAULT NULL,
  `pp_R` smallint(6) DEFAULT NULL,
  `pp_SH` smallint(6) DEFAULT NULL,
  `pp_SF` smallint(6) DEFAULT NULL,
  `pp_GIDP` smallint(6) DEFAULT NULL,
  PRIMARY KEY (`ID`),
  KEY `k_pp_team` (`teamID`),
  KEY `k_pp_player` (`playerID`)
);

--
-- Table structure for table `Salary`
--

DROP TABLE IF EXISTS `Salary`;
CREATE TABLE `Salary` (
  `ID` int(12) NOT NULL AUTO_INCREMENT,
  `playerID` varchar(9) NOT NULL,
  `teamID` char(3) NOT NULL,
  `yearID` smallint(6) NOT NULL,
  `lgID` char(2) DEFAULT NULL,
  `salary` int(12) DEFAULT NULL, 
  PRIMARY KEY (`ID`),
  KEY `sal_team` (`teamID`)
);

--
-- Table structure for table `School`
--

DROP TABLE IF EXISTS `School`;
CREATE TABLE `School` (
  `schoolID` varchar(64) NOT NULL,
  `name_full` varchar(55) DEFAULT NULL,
  `city` varchar(55) DEFAULT NULL,
  `state` varchar(55) DEFAULT NULL, 
  `country` varchar(55) DEFAULT NULL,
  PRIMARY KEY (`schoolID`)
);

--
-- Table structure for table `seriespost`
--

DROP TABLE IF EXISTS `SeriesPost`;
CREATE TABLE `SeriesPost` (
  `ID` int(12) NOT NULL AUTO_INCREMENT,
  `teamIDwinner` char(3) NOT NULL,
  `teamIDloser` char(3) NOT NULL,
  `yearID` smallint(6) NOT NULL,
  `round` varchar(5) DEFAULT NULL,
  `wins` smallint(6) DEFAULT NULL,
  `loses` smallint(6) DEFAULT NULL,
  `ties` smallint(6) DEFAULT NULL,
  PRIMARY KEY (`ID`),
  KEY `k_sp_tw` (`teamIDwinner`),
  KEY `k_sp_tl` (`teamIDloser`)
);

--
-- Table structure for table `strikes`
--

DROP TABLE IF EXISTS `Strikes`;
CREATE TABLE `Strikes` (
  `ID` int(12) NOT NULL AUTO_INCREMENT,
  `name` varchar(64) NOT NULL,
  `start_date` date DEFAULT NULL,
  `end_date` date DEFAULT NULL,
  `games_cancelled` smallint(6) DEFAULT NULL,
  `schedule_effects` varchar(255) DEFAULT NULL,
  `issues_of_contention` varchar(255) DEFAULT NULL,
  `commissioner` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`ID`),
  KEY `k_strikes_n` (`name`)
);

--
-- Table structure for table `team`
--

DROP TABLE IF EXISTS `Team`;
CREATE TABLE `Team` (
  `ID` int(12) NOT NULL AUTO_INCREMENT,
  `teamID` char(3) NOT NULL,
  `yearID` smallint(6) NOT NULL,
  `lgID` char(2) DEFAULT NULL,
  `divID` char(1) DEFAULT NULL,
  `franchID` varchar(3) DEFAULT NULL,
  `name` varchar(50) DEFAULT NULL,
  `teamRank` smallint(6) DEFAULT NULL,
  `team_G` smallint(6) DEFAULT NULL,
  `team_G_home` smallint(6) DEFAULT NULL,
  `team_W` smallint(6) DEFAULT NULL,
  `team_L` smallint(6) DEFAULT NULL,
  `DivWin` varchar(1) DEFAULT NULL,
  `WCWin` varchar(1) DEFAULT NULL,
  `LgWin` varchar(1) DEFAULT NULL,
  `WSWin` varchar(1) DEFAULT NULL,
  `team_R` smallint(6) DEFAULT NULL,
  `team_AB` smallint(6) DEFAULT NULL,
  `team_H` smallint(6) DEFAULT NULL,
  `team_2B` smallint(6) DEFAULT NULL,
  `team_3B` smallint(6) DEFAULT NULL,
  `team_HR` smallint(6) DEFAULT NULL,
  `team_BB` smallint(6) DEFAULT NULL,
  `team_SO` smallint(6) DEFAULT NULL,
  `team_SB` smallint(6) DEFAULT NULL,
  `team_CS` smallint(6) DEFAULT NULL,
  `team_HBP` smallint(6) DEFAULT NULL,
  `team_SF` smallint(6) DEFAULT NULL,
  `team_RA` smallint(6) DEFAULT NULL,
  `team_ER` smallint(6) DEFAULT NULL,
  `team_ERA` double DEFAULT NULL,
  `team_CG` smallint(6) DEFAULT NULL,
  `team_SHO` smallint(6) DEFAULT NULL,
  `team_SV` smallint(6) DEFAULT NULL,
  `team_IPouts` int(11) DEFAULT NULL,
  `team_HA` smallint(6) DEFAULT NULL,
  `team_HRA` smallint(6) DEFAULT NULL,
  `team_BBA` smallint(6) DEFAULT NULL,
  `team_SOA` smallint(6) DEFAULT NULL,
  `team_E` smallint(6) DEFAULT NULL,
  `team_DP` smallint(6) DEFAULT NULL,
  `team_FP` double DEFAULT NULL,
  `park` varchar(255) DEFAULT NULL,
  `attendance` double DEFAULT NULL,
  `team_BFP` smallint(6) DEFAULT NULL,
  PRIMARY KEY (`ID`)
);

--
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `User`;
CREATE TABLE `User` (
  `ID` int(12) NOT NULL AUTO_INCREMENT,
  `username` varchar(50) NOT NULL,
  `password` varchar(200) NOT NULL,
  `team_fav` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`username`),
  KEY `k_id` (`ID`)
);

--
-- Table structure for table `logs`
--

DROP TABLE IF EXISTS `Logs`;
CREATE TABLE `Logs` (
  `ID` int(12) NOT NULL AUTO_INCREMENT,
  `username` varchar(50) NOT NULL,
  `team_name` varchar(50) NOT NULL,
  `yearID` smallint(6) NOT NULL,
  `time` datetime(6) NOT NULL,
  PRIMARY KEY (`ID`),
  KEY `k_username` (`username`)
);