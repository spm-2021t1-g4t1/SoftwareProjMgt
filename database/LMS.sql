-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:3306
-- Generation Time: Sep 27, 2021 at 05:15 PM
-- Server version: 8.0.21
-- PHP Version: 7.3.21

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `lms`
--
CREATE DATABASE IF NOT EXISTS `lms` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci;
USE `lms`;

-- --------------------------------------------------------

--
-- Table structure for table `classes`
--

DROP TABLE IF EXISTS `classes`;
CREATE TABLE IF NOT EXISTS `classes` (
  `course_id` int NOT NULL,
  `class_no` int NOT NULL AUTO_INCREMENT,
  `start_date` date NOT NULL,
  `end_date` date NOT NULL,
  `start_time` time NOT NULL,
  `end_time` time NOT NULL,
  `class_size` int NOT NULL,
  `trainer_name` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL,
  PRIMARY KEY (`class_no`,`course_id`) USING BTREE,
  KEY `fk_1` (`course_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;

--
-- Dumping data for table `classes`
--

INSERT INTO `classes` (`course_id`, `class_no`, `start_date`, `end_date`, `start_time`, `end_time`, `class_size`, `trainer_name`) VALUES
(1, 2, '2021-09-01', '2021-09-30', '10:01:40', '19:01:40', 40, NULL);

-- --------------------------------------------------------

--
-- Table structure for table `class_assignment`
--

DROP TABLE IF EXISTS `class_assignment`;
CREATE TABLE IF NOT EXISTS `class_assignment` (
  `course_id` int NOT NULL,
  `class_no` int NOT NULL,
  `staff_email` varchar(255) NOT NULL,
  PRIMARY KEY (`course_id`,`class_no`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `course`
--

DROP TABLE IF EXISTS `course`;
CREATE TABLE IF NOT EXISTS `course` (
  `course_id` int NOT NULL AUTO_INCREMENT,
  `course_name` text NOT NULL,
  `description` text NOT NULL,
  PRIMARY KEY (`course_id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8;

--
-- Dumping data for table `course`
--

INSERT INTO `course` (`course_id`, `course_name`, `description`) VALUES
(1, 'Fundamentals of Xerox WorkCentre 784', 'Fundamentals of Xerox WorkCentre FIRST PART'),
(2, 'Programming for Xerox WorkCentre with CardAccess and Integration', 'CardAccess and integration to Xerox -- basics'),
(3, 'Embedded Systems Essentials with ARM: Getting Started', 'Introduction of embedded systems'),
(4, 'IoT System Design, Software and hardware integration', 'Introduction to IoT basics'),
(5, 'IT Fundamentals for Business ', 'Hardware IT Fundamentals bassic course'),
(6, 'Hardware and Operating Systems for Canon', 'Canon Hardware HW and OS ');

-- --------------------------------------------------------

--
-- Table structure for table `course_enrolment`
--

DROP TABLE IF EXISTS `course_enrolment`;
CREATE TABLE IF NOT EXISTS `course_enrolment` (
  `staff_email` varchar(255) NOT NULL,
  `course_id` int NOT NULL,
  KEY `fk4` (`course_id`),
  KEY `staff_email` (`staff_email`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `learning_objective`
--

DROP TABLE IF EXISTS `learning_objective`;
CREATE TABLE IF NOT EXISTS `learning_objective` (
  `course_id` int NOT NULL,
  `learning_objective` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  PRIMARY KEY (`course_id`,`learning_objective`),
  KEY `fk6` (`course_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `learning_objective`
--

INSERT INTO `learning_objective` (`course_id`, `learning_objective`) VALUES
(1, 'Create complete Angular applications'),
(1, 'Fundamentals of working with Angular'),
(1, 'Testing with Angular'),
(1, 'Understanding Dependency Injection'),
(1, 'Working with the Angular CLI');

-- --------------------------------------------------------

--
-- Table structure for table `lesson`
--

DROP TABLE IF EXISTS `lesson`;
CREATE TABLE IF NOT EXISTS `lesson` (
  `course_id` int NOT NULL,
  `class_no` int NOT NULL,
  `lesson_no` int NOT NULL,
  `section_description` varchar(255) NOT NULL,
  PRIMARY KEY (`course_id`,`class_no`,`lesson_no`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `lesson`
--

INSERT INTO `lesson` (`course_id`, `class_no`, `lesson_no`, `section_description`) VALUES
(1, 2, 1, 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis eget ante nulla. Cras eget metus vitae est cursus sagittis et mollis dolor. Sed imperdiet est vitae justo ultrices, et finibus felis suscipit. Phasellus scelerisque lacus tincidunt facilisis ul');

-- --------------------------------------------------------

--
-- Table structure for table `lesson_completion`
--

DROP TABLE IF EXISTS `lesson_completion`;
CREATE TABLE IF NOT EXISTS `lesson_completion` (
  `course_id` int NOT NULL,
  `class_no` int NOT NULL,
  `lesson_no` int NOT NULL,
  `staff_email` varchar(255) NOT NULL,
  `quiz_score` int NOT NULL,
  PRIMARY KEY (`course_id`,`class_no`,`lesson_no`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `lesson_materials`
--

DROP TABLE IF EXISTS `lesson_materials`;
CREATE TABLE IF NOT EXISTS `lesson_materials` (
  `course_id` int NOT NULL,
  `class_no` int NOT NULL,
  `lesson_no` int NOT NULL,
  `course_material_title` varchar(255) NOT NULL,
  `link` text NOT NULL,
  PRIMARY KEY (`course_id`,`class_no`,`lesson_no`,`course_material_title`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `lesson_materials`
--

INSERT INTO `lesson_materials` (`course_id`, `class_no`, `lesson_no`, `course_material_title`, `link`) VALUES
(1, 2, 1, 'material 1', 'material1.txt');

-- --------------------------------------------------------

--
-- Table structure for table `materials_viewed`
--

DROP TABLE IF EXISTS `materials_viewed`;
CREATE TABLE IF NOT EXISTS `materials_viewed` (
  `course_id` int NOT NULL,
  `class_no` int NOT NULL,
  `lesson_no` int NOT NULL,
  `course_material_title` varchar(255) NOT NULL,
  `staff_email` varchar(255) NOT NULL,
  PRIMARY KEY (`course_id`,`class_no`,`lesson_no`,`course_material_title`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `quiz`
--

DROP TABLE IF EXISTS `quiz`;
CREATE TABLE IF NOT EXISTS `quiz` (
  `quiz_id` int NOT NULL AUTO_INCREMENT,
  `quiz_name` varchar(255) NOT NULL DEFAULT 'Untitiled',
  `description` text NOT NULL,
  `uploader` varchar(255) NOT NULL,
  `duration` time NOT NULL,
  PRIMARY KEY (`quiz_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;

--
-- Dumping data for table `quiz`
--

INSERT INTO `quiz` (`quiz_id`, `quiz_name`, `description`, `uploader`, `duration`) VALUES
(1, 'AWS_CP1', 'SECTION 1', 'BAKAYARO', '00:00:00'),
(2, 'AWS_CP2', 'SECTION 2', 'BAKAYARO', '00:00:00');

-- --------------------------------------------------------

--
-- Table structure for table `quiz_options`
--

DROP TABLE IF EXISTS `quiz_options`;
CREATE TABLE IF NOT EXISTS `quiz_options` (
  `qid` int DEFAULT NULL,
  `ques_id` int DEFAULT NULL,
  `optionz` text,
  `is_right` tinyint(1) DEFAULT NULL,
  KEY `qid` (`qid`,`ques_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `quiz_questions`
--

DROP TABLE IF EXISTS `quiz_questions`;
CREATE TABLE IF NOT EXISTS `quiz_questions` (
  `qid` int NOT NULL,
  `ques_id` int NOT NULL,
  `question` text NOT NULL,
  `question_type` varchar(255) NOT NULL,
  PRIMARY KEY (`qid`,`ques_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `staff`
--

DROP TABLE IF EXISTS `staff`;
CREATE TABLE IF NOT EXISTS `staff` (
  `staff_email` varchar(255) NOT NULL,
  `years_of_service` int NOT NULL,
  PRIMARY KEY (`staff_email`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `staff`
--

INSERT INTO `staff` (`staff_email`, `years_of_service`) VALUES
('bakayaro@lms.aio.sg', 3),
('bambooo@lms.aio.sg', 7),
('jackma@lms.aio.sg', 8),
('juniornew@lms.aio.sg', 2),
('seniortest@lms.aio.sg', 11),
('stevejobs@lms.aio.sg', 4),
('test111@lms.aio.sg', 5),
('test123@lms.aio.sg', 5);

--
-- Constraints for dumped tables
--

--
-- Constraints for table `classes`
--
ALTER TABLE `classes`
  ADD CONSTRAINT `fk_1` FOREIGN KEY (`course_id`) REFERENCES `course` (`course_id`);

--
-- Constraints for table `class_assignment`
--
ALTER TABLE `class_assignment`
  ADD CONSTRAINT `fk3` FOREIGN KEY (`course_id`,`class_no`) REFERENCES `classes` (`course_id`, `class_no`);

--
-- Constraints for table `course_enrolment`
--
ALTER TABLE `course_enrolment`
  ADD CONSTRAINT `fk4` FOREIGN KEY (`course_id`) REFERENCES `course` (`course_id`),
  ADD CONSTRAINT `staff_email` FOREIGN KEY (`staff_email`) REFERENCES `staff` (`staff_email`);

--
-- Constraints for table `learning_objective`
--
ALTER TABLE `learning_objective`
  ADD CONSTRAINT `fk6` FOREIGN KEY (`course_id`) REFERENCES `course` (`course_id`);

--
-- Constraints for table `lesson`
--
ALTER TABLE `lesson`
  ADD CONSTRAINT `fk7` FOREIGN KEY (`course_id`,`class_no`) REFERENCES `classes` (`course_id`, `class_no`);

--
-- Constraints for table `lesson_completion`
--
ALTER TABLE `lesson_completion`
  ADD CONSTRAINT `fk8` FOREIGN KEY (`course_id`,`class_no`,`lesson_no`) REFERENCES `lesson` (`course_id`, `class_no`, `lesson_no`);

--
-- Constraints for table `lesson_materials`
--
ALTER TABLE `lesson_materials`
  ADD CONSTRAINT `fk9` FOREIGN KEY (`course_id`,`class_no`,`lesson_no`) REFERENCES `lesson` (`course_id`, `class_no`, `lesson_no`);

--
-- Constraints for table `materials_viewed`
--
ALTER TABLE `materials_viewed`
  ADD CONSTRAINT `fk10` FOREIGN KEY (`course_id`,`class_no`,`lesson_no`) REFERENCES `lesson` (`course_id`, `class_no`, `lesson_no`);

--
-- Constraints for table `quiz_options`
--
ALTER TABLE `quiz_options`
  ADD CONSTRAINT `quiz_options_ibfk_1` FOREIGN KEY (`qid`,`ques_id`) REFERENCES `quiz_questions` (`qid`, `ques_id`);

--
-- Constraints for table `quiz_questions`
--
ALTER TABLE `quiz_questions`
  ADD CONSTRAINT `quiz` FOREIGN KEY (`qid`) REFERENCES `quiz` (`quiz_id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
