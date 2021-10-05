-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:3306
-- Generation Time: Oct 04, 2021 at 01:18 PM
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
  KEY `fk_1` (`course_id`),
  KEY `class_fk_2` (`trainer_name`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8;

--
-- Dumping data for table `classes`
--

INSERT INTO `classes` (`course_id`, `class_no`, `start_date`, `end_date`, `start_time`, `end_time`, `class_size`, `trainer_name`) VALUES
(1, 1, '2021-09-01', '2021-09-30', '08:00:00', '11:00:00', 40, 'stevejobs'),
(2, 1, '2021-09-01', '2021-09-30', '08:00:00', '11:00:00', 40, 'jackma'),
(3, 1, '2021-09-01', '2021-09-30', '08:00:00', '11:00:00', 40, NULL),
(4, 1, '2021-09-01', '2021-09-30', '08:00:00', '11:00:00', 40, NULL),
(5, 1, '2021-09-01', '2021-09-30', '08:00:00', '11:00:00', 40, NULL),
(6, 1, '2021-09-01', '2021-09-30', '08:00:00', '11:00:00', 40, NULL),
(1, 2, '2021-09-01', '2021-09-30', '12:00:00', '15:00:00', 40, 'stevejobs'),
(2, 2, '2021-09-01', '2021-09-30', '12:00:00', '15:00:00', 40, 'jackma'),
(3, 2, '2021-09-01', '2021-09-30', '12:00:00', '15:00:00', 40, NULL),
(4, 2, '2021-09-01', '2021-09-30', '12:00:00', '15:00:00', 40, NULL),
(5, 2, '2021-09-01', '2021-09-30', '12:00:00', '15:00:00', 40, NULL),
(6, 2, '2021-09-01', '2021-09-30', '12:00:00', '15:00:00', 40, NULL);

-- --------------------------------------------------------

--
-- Table structure for table `class_enrolment`
--

DROP TABLE IF EXISTS `class_enrolment`;
CREATE TABLE IF NOT EXISTS `class_enrolment` (
  `staff_username` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `course_id` int NOT NULL,
  `class_no` int NOT NULL,
  PRIMARY KEY (`staff_username`,`course_id`,`class_no`),
  KEY `staff_email` (`staff_username`),
  KEY `fk4` (`class_no`,`course_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `class_enrolment`
--

INSERT INTO `class_enrolment` (`staff_username`, `course_id`, `class_no`) VALUES
('coreyroberts', 1, 1),
('darrelwilde', 1, 1),
('hananhyde', 1, 1),
('jackma', 1, 1),
('rojinclark', 1, 1),
('sallieeast', 1, 1),
('sannahrossi', 1, 1),
('stevejobs', 1, 1),
('coreyroberts', 2, 1),
('darrelwilde', 2, 1),
('hananhyde', 2, 1),
('jackma', 2, 1),
('rojinclark', 2, 1),
('sallieeast', 2, 1),
('sannahrossi', 2, 1),
('stevejobs', 2, 1);

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
(1, 'Fundamentals of Xerox WorkCentre 784', 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis eget ante nulla. Cras eget metus vitae est cursus sagittis et mollis dolor. Sed imperdiet est vitae justo ultrices, et finibus felis suscipit. Phasellus scelerisque lacus tincidunt facilisis ul'),
(2, 'Programming for Xerox WorkCentre with CardAccess and Integration', 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis eget ante nulla. Cras eget metus vitae est cursus sagittis et mollis dolor. Sed imperdiet est vitae justo ultrices, et finibus felis suscipit. Phasellus scelerisque lacus tincidunt facilisis ul'),
(3, 'Embedded Systems Essentials with ARM: Getting Started', 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis eget ante nulla. Cras eget metus vitae est cursus sagittis et mollis dolor. Sed imperdiet est vitae justo ultrices, et finibus felis suscipit. Phasellus scelerisque lacus tincidunt facilisis ul'),
(4, 'IoT System Design, Software and hardware integration', 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis eget ante nulla. Cras eget metus vitae est cursus sagittis et mollis dolor. Sed imperdiet est vitae justo ultrices, et finibus felis suscipit. Phasellus scelerisque lacus tincidunt facilisis ul'),
(5, 'IT Fundamentals for Business ', 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis eget ante nulla. Cras eget metus vitae est cursus sagittis et mollis dolor. Sed imperdiet est vitae justo ultrices, et finibus felis suscipit. Phasellus scelerisque lacus tincidunt facilisis ul'),
(6, 'Hardware and Operating Systems for Canon', 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis eget ante nulla. Cras eget metus vitae est cursus sagittis et mollis dolor. Sed imperdiet est vitae justo ultrices, et finibus felis suscipit. Phasellus scelerisque lacus tincidunt facilisis ul');

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
(1, 'Working with the Angular CLI'),
(2, 'Create complete Angular applications'),
(2, 'Fundamentals of working with Angular'),
(2, 'Working with the Angular CLI'),
(3, 'Create complete Angular applications'),
(3, 'Fundamentals of working with Angular'),
(3, 'Working with the Angular CLI'),
(4, 'Create complete Angular applications'),
(4, 'Fundamentals of working with Angular'),
(4, 'Working with the Angular CLI'),
(5, 'Create complete Angular applications'),
(5, 'Fundamentals of working with Angular'),
(5, 'Working with the Angular CLI'),
(6, 'Create complete Angular applications'),
(6, 'Fundamentals of working with Angular'),
(6, 'Working with the Angular CLI');

-- --------------------------------------------------------

--
-- Table structure for table `lesson`
--

DROP TABLE IF EXISTS `lesson`;
CREATE TABLE IF NOT EXISTS `lesson` (
  `course_id` int NOT NULL,
  `class_no` int NOT NULL,
  `lesson_no` int NOT NULL,
  `lesson_name` varchar(255) NOT NULL,
  `lesson_description` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  PRIMARY KEY (`course_id`,`class_no`,`lesson_no`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `lesson`
--

INSERT INTO `lesson` (`course_id`, `class_no`, `lesson_no`, `lesson_name`, `lesson_description`) VALUES
(1, 2, 1, 'Fundamentals of Xerox WorkCentre 784 101', 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis eget ante nulla. Cras eget metus vitae est cursus sagittis et mollis dolor. Sed imperdiet est vitae justo ultrices, et finibus felis suscipit. Phasellus scelerisque lacus tincidunt facilisis ul'),
(1, 2, 2, 'Lorem ipsum dolor', 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis eget ante nulla. Cras eget metus vitae est cursus sagittis et mollis dolor. Sed imperdiet est vitae justo ultrices, et finibus felis suscipit. Phasellus scelerisque lacus tincidunt facilisis ul'),
(1, 2, 3, 'Lorem ipsum dolor', 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis eget ante nulla. Cras eget metus vitae est cursus sagittis et mollis dolor. Sed imperdiet est vitae justo ultrices, et finibus felis suscipit. Phasellus scelerisque lacus tincidunt facilisis ul'),
(2, 1, 1, 'Lorem ipsum dolor', 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis eget ante nulla. Cras eget metus vitae est cursus sagittis et mollis dolor. Sed imperdiet est vitae justo ultrices, et finibus felis suscipit. Phasellus scelerisque lacus tincidunt facilisis ul'),
(2, 1, 2, 'Lorem ipsum dolor', 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis eget ante nulla. Cras eget metus vitae est cursus sagittis et mollis dolor. Sed imperdiet est vitae justo ultrices, et finibus felis suscipit. Phasellus scelerisque lacus tincidunt facilisis ul'),
(2, 1, 3, 'Lorem ipsum dolor', 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis eget ante nulla. Cras eget metus vitae est cursus sagittis et mollis dolor. Sed imperdiet est vitae justo ultrices, et finibus felis suscipit. Phasellus scelerisque lacus tincidunt facilisis ul');

-- --------------------------------------------------------

--
-- Table structure for table `quiz_attempts`
--

DROP TABLE IF EXISTS `quiz_attempts`;
CREATE TABLE IF NOT EXISTS `quiz_attempts` (
  `course_id` int NOT NULL,
  `class_no` int NOT NULL,
  `lesson_no` int NOT NULL,
  `staff_username` varchar(255) NOT NULL,
  `quiz_score` int NOT NULL,
  PRIMARY KEY (`course_id`,`class_no`,`lesson_no`,`staff_username`,`quiz_score`)
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
  `staff_username` varchar(255) NOT NULL,
  PRIMARY KEY (`course_id`,`class_no`,`lesson_no`,`course_material_title`,`staff_username`)
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

--
-- Dumping data for table `quiz_questions`
--

INSERT INTO `quiz_questions` (`qid`, `ques_id`, `question`, `question_type`) VALUES
(1, 1, 'A Company is migrating an application to its AWS environment. The implementation requires the company to deploy up to 40 m4.4xlarge instances. What should a Cloud engineer do prior to launching the instances? ', 'mcq'),
(1, 2, 'An organization recently expanded its AWS infrastructure for its public website into two regions. US East (Ohio) and ASIA Pacific (Mumbai), to better serve growing demand in Asia. What should the SysOps administrator implement to ensure that users are consistently directed to the best performing region?', 'mcq'),
(1, 3, 'A SysOps administrator has an Amazon EC2 instance using IPv6. Which VPC feature allows the instance to communicate with the internet but prevents inbound traffic?', 'mcq'),
(1, 4, 'An Organization has implemented a file gateway to keep copies of users’ home drives in Amazon S3. Which conducting an analysis, an Administrator notice that most files are no longer accessed after 45 days. What is the BEST way for the Administrator to reduce storage costs while continuing to provide access to the files for the users?', 'mcq');

-- --------------------------------------------------------

--
-- Table structure for table `staff`
--

DROP TABLE IF EXISTS `staff`;
CREATE TABLE IF NOT EXISTS `staff` (
  `staff_username` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `staff_name` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL,
  `role` varchar(255) NOT NULL DEFAULT 'Learner',
  `department` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `current_designation` varchar(255) NOT NULL,
  PRIMARY KEY (`staff_username`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `staff`
--

INSERT INTO `staff` (`staff_username`, `staff_name`, `role`, `department`, `current_designation`) VALUES
('coreyroberts', 'Corey Roberts', 'Learner', 'Operation', 'Engineer'),
('darrelwilde', 'Darrel Wilde', 'Learner', 'Development', 'Engineer'),
('hananhyde', 'Hanan Hyde', 'Administrator', 'Human Resources', 'Executive'),
('jackma', 'Jack Ma', 'Trainer', 'Development', 'Engineer'),
('rojinclark', 'Rojin Clark', 'Learner', 'Operation', 'Engineer'),
('sallieeast', 'Sallie East', 'Learner', 'Operation', 'Engineer'),
('sannahrossi', 'Sannah Rossi', 'Learner', 'Development', 'Engineer'),
('stevejobs', 'Steve Jobs', 'Trainer', 'Operation', 'Engineer');

--
-- Constraints for dumped tables
--

--
-- Constraints for table `classes`
--
ALTER TABLE `classes`
  ADD CONSTRAINT `class_fk_2` FOREIGN KEY (`trainer_name`) REFERENCES `staff` (`staff_username`) ON DELETE RESTRICT ON UPDATE CASCADE,
  ADD CONSTRAINT `classes_fk_1` FOREIGN KEY (`course_id`) REFERENCES `course` (`course_id`) ON DELETE RESTRICT ON UPDATE CASCADE;

--
-- Constraints for table `class_enrolment`
--
ALTER TABLE `class_enrolment`
  ADD CONSTRAINT `fk4` FOREIGN KEY (`class_no`,`course_id`) REFERENCES `classes` (`class_no`, `course_id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  ADD CONSTRAINT `staff_email` FOREIGN KEY (`staff_username`) REFERENCES `staff` (`staff_username`);

--
-- Constraints for table `learning_objective`
--
ALTER TABLE `learning_objective`
  ADD CONSTRAINT `fk6` FOREIGN KEY (`course_id`) REFERENCES `course` (`course_id`);

--
-- Constraints for table `lesson`
--
ALTER TABLE `lesson`
  ADD CONSTRAINT `lesson_fk1` FOREIGN KEY (`course_id`,`class_no`) REFERENCES `classes` (`course_id`, `class_no`) ON DELETE RESTRICT ON UPDATE RESTRICT;

--
-- Constraints for table `quiz_attempts`
--
ALTER TABLE `quiz_attempts`
  ADD CONSTRAINT `fk8` FOREIGN KEY (`course_id`,`class_no`,`lesson_no`) REFERENCES `lesson` (`course_id`, `class_no`, `lesson_no`),
  ADD CONSTRAINT `staff_username_fk1` FOREIGN KEY (`staff_username`) REFERENCES `staff` (`staff_username`);

--
-- Constraints for table `lesson_materials`
--
ALTER TABLE `lesson_materials`
  ADD CONSTRAINT `fk9` FOREIGN KEY (`course_id`,`class_no`,`lesson_no`) REFERENCES `lesson` (`course_id`, `class_no`, `lesson_no`);

--
-- Constraints for table `materials_viewed`
--
ALTER TABLE `materials_viewed`
  ADD CONSTRAINT `fk10` FOREIGN KEY (`course_id`,`class_no`,`lesson_no`,`course_material_title`) REFERENCES `lesson_materials` (`course_id`, `class_no`, `lesson_no`, `course_material_title`),
  ADD CONSTRAINT `fk11` FOREIGN KEY (`staff_username`) REFERENCES `staff` (`staff_username`);

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
