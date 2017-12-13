-- phpMyAdmin SQL Dump
-- version 4.4.10
-- http://www.phpmyadmin.net
--
-- Host: localhost:9092
-- Generation Time: Dec 09, 2017 at 07:22 PM
-- Server version: 5.5.42
-- PHP Version: 7.0.0

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";

--
-- Database: `accent_classifier`
--

-- --------------------------------------------------------

--
-- Table structure for table `apiLookup`
--

CREATE TABLE `apiLookup` (
  `Country` varchar(12) DEFAULT NULL,
  `number` int(1) DEFAULT NULL,
  `Country_wikipedia` varchar(14) DEFAULT NULL,
  `Country_restaurants` varchar(8) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `apiLookup`
--

INSERT INTO `apiLookup` (`Country`, `number`, `Country_wikipedia`, `Country_restaurants`) VALUES
('USA', 0, 'United_States', 'american'),
('UK', 1, 'United_Kingdom', 'british'),
('Spain', 2, 'Spain', 'spanish'),
('France', 3, 'France', 'french'),
('Russia', 4, 'Russia', 'russian'),
('Saudi Arabia', 5, 'Saudi_Arabia', 'arabic'),
('China', 6, 'China', 'chinese'),
('South Korea', 7, 'South_Korea', 'korean'),
('Japan', 8, 'Japan', 'japanese');

-- --------------------------------------------------------

--
-- Table structure for table `audioFiles`
--

CREATE TABLE `audioFiles` (
  `number` int(11) NOT NULL,
  `mfcc` blob NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `graduate`
--

CREATE TABLE `graduate` (
  `number` int(1) DEFAULT NULL,
  `2016-graduate` int(5) DEFAULT NULL,
  `2015-graduate` int(5) DEFAULT NULL,
  `2014-graduate` int(4) DEFAULT NULL,
  `2013-graduate` int(4) DEFAULT NULL,
  `2012-graduate` int(4) DEFAULT NULL,
  `2011-graduate` int(4) DEFAULT NULL,
  `2010-graduate` int(4) DEFAULT NULL,
  `2009-graduate` int(4) DEFAULT NULL,
  `2008-graduate` int(4) DEFAULT NULL,
  `2007-graduate` int(4) DEFAULT NULL,
  `2006-graduate` int(4) DEFAULT NULL,
  `2005-graduate` int(4) DEFAULT NULL,
  `2004-graduate` int(4) DEFAULT NULL,
  `2003-graduate` int(4) DEFAULT NULL,
  `2002-graduate` int(4) DEFAULT NULL,
  `2001-graduate` int(4) DEFAULT NULL,
  `2000-graduate` int(4) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `graduate`
--

INSERT INTO `graduate` (`number`, `2016-graduate`, `2015-graduate`, `2014-graduate`, `2013-graduate`, `2012-graduate`, `2011-graduate`, `2010-graduate`, `2009-graduate`, `2008-graduate`, `2007-graduate`, `2006-graduate`, `2005-graduate`, `2004-graduate`, `2003-graduate`, `2002-graduate`, `2001-graduate`, `2000-graduate`) VALUES
(0, 446, 502, 408, 429, 388, 373, 407, 371, 300, 315, 306, 300, 273, 268, 217, 183, 167),
(1, 12746, 12373, 7655, 7137, 6694, 6389, 6119, 5795, 5305, 4985, 4596, 4536, 4617, 4501, 4009, 4009, 3964),
(2, 131, 126, 91, 89, 70, 68, 76, 54, 50, 44, 43, 30, 55, 49, 51, 45, 72),
(3, 205, 200, 181, 168, 135, 149, 128, 126, 110, 88, 88, 79, 75, 71, 59, 70, 82),
(4, 33, 37, 36, 38, 37, 27, 30, 33, 30, 23, 16, 8, 13, 14, 11, 12, 18),
(5, 141, 132, 108, 93, 75, 60, 59, 57, 39, 22, 26, 30, 31, 28, 29, 21, 19),
(6, 2217, 1935, 1379, 1262, 904, 625, 478, 425, 309, 296, 267, 262, 247, 217, 137, 65, 49),
(7, 146, 160, 109, 104, 88, 97, 83, 73, 52, 47, 42, 46, 49, 50, 51, 40, 47),
(8, 97, 117, 98, 74, 59, 64, 61, 59, 49, 53, 66, 73, 92, 82, 84, 82, 79);

-- --------------------------------------------------------

--
-- Table structure for table `total`
--

CREATE TABLE `total` (
  `number` int(1) DEFAULT NULL,
  `2016-total` int(5) DEFAULT NULL,
  `2015-total` int(5) DEFAULT NULL,
  `2014-total` int(5) DEFAULT NULL,
  `2013-total` int(5) DEFAULT NULL,
  `2012-total` int(5) DEFAULT NULL,
  `2011-total` int(5) DEFAULT NULL,
  `2010-total` int(5) DEFAULT NULL,
  `2009-total` int(5) DEFAULT NULL,
  `2008-total` int(5) DEFAULT NULL,
  `2007-total` int(5) DEFAULT NULL,
  `2006-total` int(5) DEFAULT NULL,
  `2005-total` int(5) DEFAULT NULL,
  `2004-total` int(5) DEFAULT NULL,
  `2003-total` int(5) DEFAULT NULL,
  `2002-total` int(5) DEFAULT NULL,
  `2001-total` int(5) DEFAULT NULL,
  `2000-total` int(5) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `total`
--

INSERT INTO `total` (`number`, `2016-total`, `2015-total`, `2014-total`, `2013-total`, `2012-total`, `2011-total`, `2010-total`, `2009-total`, `2008-total`, `2007-total`, `2006-total`, `2005-total`, `2004-total`, `2003-total`, `2002-total`, `2001-total`, `2000-total`) VALUES
(0, 769, 925, 870, 867, 804, 786, 791, 685, 605, 632, 663, 595, 612, 589, 525, 538, 461),
(1, 23059, 22717, 17394, 16529, 15710, 14951, 14860, 14485, 13981, 13563, 13258, 13627, 13958, 13833, 12963, 12963, 12836),
(2, 398, 352, 260, 208, 188, 157, 162, 134, 122, 124, 110, 109, 123, 118, 113, 107, 121),
(3, 725, 681, 560, 457, 371, 354, 351, 334, 309, 267, 237, 228, 180, 174, 163, 176, 208),
(5, 162, 156, 144, 120, 106, 98, 90, 96, 68, 47, 43, 41, 44, 43, 35, 24, 20),
(6, 3681, 3226, 2480, 2311, 1851, 1468, 1204, 1015, 828, 779, 672, 590, 496, 412, 242, 130, 93),
(7, 314, 303, 237, 240, 246, 250, 217, 190, 156, 139, 135, 139, 128, 111, 102, 75, 101),
(8, 156, 171, 159, 129, 113, 125, 116, 121, 105, 118, 138, 166, 174, 186, 141, 138, 162);

-- --------------------------------------------------------

--
-- Table structure for table `undergraduate`
--

CREATE TABLE `undergraduate` (
  `number` int(1) DEFAULT NULL,
  `2016-undergrad` int(5) DEFAULT NULL,
  `2015-undergrad` int(5) DEFAULT NULL,
  `2014-undergrad` int(4) DEFAULT NULL,
  `2013-undergrad` int(4) DEFAULT NULL,
  `2012-undergrad` int(4) DEFAULT NULL,
  `2011-undergrad` int(4) DEFAULT NULL,
  `2010-undergrad` int(4) DEFAULT NULL,
  `2009-undergrad` int(4) DEFAULT NULL,
  `2008-undergrad` int(4) DEFAULT NULL,
  `2007-undergrad` int(4) DEFAULT NULL,
  `2006-undergrad` int(4) DEFAULT NULL,
  `2005-undergrad` int(4) DEFAULT NULL,
  `2004-undergrad` int(4) DEFAULT NULL,
  `2003-undergrad` int(4) DEFAULT NULL,
  `2002-undergrad` int(4) DEFAULT NULL,
  `2001-undergrad` int(4) DEFAULT NULL,
  `2000-undergrad` int(4) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `undergraduate`
--

INSERT INTO `undergraduate` (`number`, `2016-undergrad`, `2015-undergrad`, `2014-undergrad`, `2013-undergrad`, `2012-undergrad`, `2011-undergrad`, `2010-undergrad`, `2009-undergrad`, `2008-undergrad`, `2007-undergrad`, `2006-undergrad`, `2005-undergrad`, `2004-undergrad`, `2003-undergrad`, `2002-undergrad`, `2001-undergrad`, `2000-undergrad`) VALUES
(0, 323, 423, 462, 438, 416, 413, 384, 314, 305, 317, 357, 295, 339, 321, 308, 355, 294),
(1, 10313, 10344, 9739, 9392, 9016, 8562, 8741, 8690, 8676, 8578, 8662, 9091, 9341, 9332, 8954, 8954, 8872),
(2, 267, 226, 169, 119, 118, 89, 86, 80, 72, 80, 67, 79, 68, 69, 62, 62, 49),
(3, 520, 481, 379, 289, 236, 205, 223, 208, 199, 179, 149, 149, 105, 103, 104, 106, 126),
(4, 140, 150, 148, 136, 119, 100, 83, 65, 62, 62, 51, 14, 51, 55, 43, 28, 41),
(5, 21, 24, 36, 27, 31, 38, 31, 39, 29, 25, 17, 11, 13, 15, 6, 3, 1),
(6, 1456, 1291, 1101, 1049, 947, 843, 726, 590, 519, 483, 405, 328, 249, 195, 105, 65, 44),
(7, 168, 143, 128, 136, 158, 153, 134, 117, 104, 92, 93, 93, 79, 61, 51, 35, 54),
(8, 59, 54, 61, 55, 54, 61, 55, 62, 56, 65, 72, 93, 82, 104, 57, 56, 83);
