-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:3306
-- Generation Time: Oct 28, 2021 at 12:22 AM
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
CREATE DATABASE IF NOT EXISTS `lms` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
USE `lms`;

-- --------------------------------------------------------

--
-- Table structure for table `classenrollment_queue`
--

DROP TABLE IF EXISTS `classenrollment_queue`;
CREATE TABLE IF NOT EXISTS `classenrollment_queue` (
  `staff_username` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `course_id` int NOT NULL,
  `class_no` int NOT NULL,
  PRIMARY KEY (`staff_username`,`course_id`,`class_no`),
  KEY `CE_Queue_fk_1` (`course_id`,`class_no`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

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
(1, 'Fundamentals of Xerox WorkCentre 784', 'This course is a basic introduction to the Fundamentals of Xerox WorkCentre printer course.'),
(2, 'Programming for Xerox WorkCentre with CardAccess and Integration', 'This course will equip you with basic programming skills as well as software integration.'),
(3, 'Embedded Systems Essentials with ARM: Getting Started', 'Get practical without hardware. Quickly prototype and build microcontroller projects using industry-standard APIs.'),
(4, 'IoT System Design, Software and hardware integration', 'This course is designed to teach you how systems are developed using IoT technology.\r\n'),
(5, 'IT Fundamentals for Business ', 'This introductory program is designed to give business professionals the basic background on Information Technology (IT) to let them get the most in their interaction with IT professionals, either from their company or from external corporation, as they will have a deeper understanding when identifying requirements, evaluating workloads or supervising results in the IT field.\r\n\r\n'),
(6, 'Hardware and Operating Systems for Canon', 'This is a hardware course centered around the Canon printer system. You will learn the different hardware components that make up the Canon printer and the operating system.');

-- --------------------------------------------------------

--
-- Table structure for table `course_completion`
--

DROP TABLE IF EXISTS `course_completion`;
CREATE TABLE IF NOT EXISTS `course_completion` (
  `course_id` int NOT NULL,
  `staff_username` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  PRIMARY KEY (`course_id`,`staff_username`),
  KEY `course_completion_fk2` (`staff_username`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `course_completion`
--

INSERT INTO `course_completion` (`course_id`, `staff_username`) VALUES
(1, 'darrelwilde'),
(3, 'darrelwilde');

-- --------------------------------------------------------

--
-- Table structure for table `course_prerequisite`
--

DROP TABLE IF EXISTS `course_prerequisite`;
CREATE TABLE IF NOT EXISTS `course_prerequisite` (
  `course_id` int NOT NULL,
  `prerequisite_course_id` int NOT NULL,
  PRIMARY KEY (`course_id`,`prerequisite_course_id`),
  KEY `course_prerequisite_fk2` (`prerequisite_course_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `course_prerequisite`
--

INSERT INTO `course_prerequisite` (`course_id`, `prerequisite_course_id`) VALUES
(2, 1),
(5, 2),
(4, 3),
(5, 3),
(5, 4);

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
(1, 2, 1, 'The beginning - Fundamentals of Xerox WorkCentre 784', 'The first lesson of Fundamentals of Xerox WorkCentre 784.'),
(1, 2, 2, 'The advanced - Fundamentals of Xerox WorkCentre 784', 'The second lesson of Fundamentals of Xerox WorkCentre 784. '),
(1, 2, 3, 'Putting it together - Fundamentals of Xerox WorkCentre 784', 'The final lesson of Fundamentals of Xerox WorkCentre 784. '),
(2, 1, 1, 'The beginning - Programming for Xerox WorkCentre with CardAccess and Integration', 'The first lesson of Programming for Xerox WorkCentre with CardAccess and Integration'),
(2, 1, 2, 'The advanced - Programming for Xerox WorkCentre with CardAccess and Integration', 'The second lesson of Programming for Xerox WorkCentre with CardAccess and Integration'),
(2, 1, 3, 'Putting it together - Programming for Xerox WorkCentre with CardAccess and Integration', 'The last lesson of Programming for Xerox WorkCentre with CardAccess and Integration');

-- --------------------------------------------------------

--
-- Table structure for table `lesson_completion`
--

DROP TABLE IF EXISTS `lesson_completion`;
CREATE TABLE IF NOT EXISTS `lesson_completion` (
  `course_id` int NOT NULL,
  `class_no` int NOT NULL,
  `lesson_no` int NOT NULL,
  `staff_username` varchar(255) NOT NULL,
  PRIMARY KEY (`course_id`,`class_no`,`lesson_no`,`staff_username`),
  KEY `fk11` (`staff_username`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `lesson_completion`
--

INSERT INTO `lesson_completion` (`course_id`, `class_no`, `lesson_no`, `staff_username`) VALUES
(2, 1, 1, 'darrelwilde');

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
(1, 2, 1, '121A', 'www.121a.com'),
(1, 2, 1, '121B', 'www.121b.com'),
(1, 2, 2, '122A', 'www.122a.com'),
(1, 2, 2, '122B', 'www.122b.com'),
(1, 2, 2, '123A', 'www.123a.com'),
(1, 2, 2, '123B', 'www.123b.com'),
(2, 1, 1, '211A', 'www.google.com'),
(2, 1, 1, '211B', 'www.yahoo.com'),
(2, 1, 2, '212A', 'www.youtube.com'),
(2, 1, 2, '212B', 'www.amazon.com'),
(2, 1, 3, '213A', 'www.hardwarezone.com'),
(2, 1, 3, '213B', 'www.reddit.com');

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
-- Table structure for table `quiz_attempts`
--

DROP TABLE IF EXISTS `quiz_attempts`;
CREATE TABLE IF NOT EXISTS `quiz_attempts` (
  `course_id` int NOT NULL,
  `class_no` int NOT NULL,
  `lesson_no` int NOT NULL,
  `staff_username` varchar(255) NOT NULL,
  `quiz_score` int NOT NULL,
  PRIMARY KEY (`course_id`,`class_no`,`lesson_no`,`staff_username`,`quiz_score`),
  KEY `staff_username_fk1` (`staff_username`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `quiz_attempts`
--

INSERT INTO `quiz_attempts` (`course_id`, `class_no`, `lesson_no`, `staff_username`, `quiz_score`) VALUES
(2, 1, 1, 'darrelwilde', 89);

-- --------------------------------------------------------

--
-- Table structure for table `quiz_options`
--

DROP TABLE IF EXISTS `quiz_options`;
CREATE TABLE IF NOT EXISTS `quiz_options` (
  `quiz_id` int NOT NULL,
  `ques_id` int NOT NULL,
  `opts_id` int NOT NULL,
  `qopt` text NOT NULL,
  `is_right` tinyint(1) NOT NULL,
  PRIMARY KEY (`quiz_id`,`ques_id`,`opts_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `quiz_options`
--

INSERT INTO `quiz_options` (`quiz_id`, `ques_id`, `opts_id`, `qopt`, `is_right`) VALUES
(1, 1, 1, 'Increase service limit from AWS Trusted Advisor before launching new instances', 0),
(1, 1, 2, 'Submit a service limit increase to AWS Support specifying the instance type and region. ', 1),
(1, 1, 3, 'BOOOOOP', 0),
(1, 2, 1, 'Load Balancing', 1),
(1, 2, 2, 'Auto Scaling', 0),
(1, 2, 3, 'Not sure', 0),
(1, 3, 1, 'Not sure', 0),
(1, 3, 2, 'Security Group', 1),
(1, 3, 3, 'Key Management', 0),
(1, 4, 1, 'Archive the file', 0),
(1, 4, 2, 'Delete the file from S3', 0),
(1, 4, 3, 'Store it in EBS', 1);

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
-- Constraints for table `classenrollment_queue`
--
ALTER TABLE `classenrollment_queue`
  ADD CONSTRAINT `CE_Queue_fk_1` FOREIGN KEY (`course_id`,`class_no`) REFERENCES `classes` (`course_id`, `class_no`) ON DELETE RESTRICT ON UPDATE CASCADE,
  ADD CONSTRAINT `CE_Queue_fk_2` FOREIGN KEY (`staff_username`) REFERENCES `staff` (`staff_username`) ON DELETE RESTRICT ON UPDATE CASCADE;

--
-- Constraints for table `classes`
--
ALTER TABLE `classes`
  ADD CONSTRAINT `classes_fk_1` FOREIGN KEY (`course_id`) REFERENCES `course` (`course_id`) ON DELETE RESTRICT ON UPDATE CASCADE,
  ADD CONSTRAINT `classes_fk_2` FOREIGN KEY (`trainer_name`) REFERENCES `staff` (`staff_username`) ON DELETE RESTRICT ON UPDATE RESTRICT;

--
-- Constraints for table `class_enrolment`
--
ALTER TABLE `class_enrolment`
  ADD CONSTRAINT `fk4` FOREIGN KEY (`class_no`,`course_id`) REFERENCES `classes` (`class_no`, `course_id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  ADD CONSTRAINT `staff_email` FOREIGN KEY (`staff_username`) REFERENCES `staff` (`staff_username`);

--
-- Constraints for table `course_completion`
--
ALTER TABLE `course_completion`
  ADD CONSTRAINT `course_completion_fk` FOREIGN KEY (`course_id`) REFERENCES `course` (`course_id`),
  ADD CONSTRAINT `course_completion_fk2` FOREIGN KEY (`staff_username`) REFERENCES `staff` (`staff_username`);

--
-- Constraints for table `course_prerequisite`
--
ALTER TABLE `course_prerequisite`
  ADD CONSTRAINT `course_prerequisite_fk` FOREIGN KEY (`course_id`) REFERENCES `course` (`course_id`),
  ADD CONSTRAINT `course_prerequisite_fk2` FOREIGN KEY (`prerequisite_course_id`) REFERENCES `course` (`course_id`);

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
-- Constraints for table `lesson_completion`
--
ALTER TABLE `lesson_completion`
  ADD CONSTRAINT `fk10` FOREIGN KEY (`course_id`,`class_no`,`lesson_no`) REFERENCES `lesson` (`course_id`, `class_no`, `lesson_no`),
  ADD CONSTRAINT `fk11` FOREIGN KEY (`staff_username`) REFERENCES `staff` (`staff_username`);

--
-- Constraints for table `lesson_materials`
--
ALTER TABLE `lesson_materials`
  ADD CONSTRAINT `fk9` FOREIGN KEY (`course_id`,`class_no`,`lesson_no`) REFERENCES `lesson` (`course_id`, `class_no`, `lesson_no`);

--
-- Constraints for table `quiz_attempts`
--
ALTER TABLE `quiz_attempts`
  ADD CONSTRAINT `fk8` FOREIGN KEY (`course_id`,`class_no`,`lesson_no`) REFERENCES `lesson` (`course_id`, `class_no`, `lesson_no`),
  ADD CONSTRAINT `staff_username_fk1` FOREIGN KEY (`staff_username`) REFERENCES `staff` (`staff_username`);

--
-- Constraints for table `quiz_questions`
--
ALTER TABLE `quiz_questions`
  ADD CONSTRAINT `quiz` FOREIGN KEY (`qid`) REFERENCES `quiz` (`quiz_id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
