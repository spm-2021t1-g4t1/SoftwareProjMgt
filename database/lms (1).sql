-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
<<<<<<< Updated upstream:database/LMS.sql
-- Host: 127.0.0.1:3306
-- Generation Time: Sep 27, 2021 at 05:15 PM
-- Server version: 8.0.21
-- PHP Version: 7.3.21
=======
-- Host: localhost:8889
-- Generation Time: Oct 02, 2021 at 05:59 PM
-- Server version: 5.7.34
-- PHP Version: 7.4.21
>>>>>>> Stashed changes:database/lms (1).sql

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

-- --------------------------------------------------------

--
-- Table structure for table `classes`
--

CREATE TABLE `classes` (
  `course_id` int(11) NOT NULL,
  `class_no` int(11) NOT NULL,
  `start_date` date NOT NULL,
  `end_date` date NOT NULL,
  `start_time` time NOT NULL,
  `end_time` time NOT NULL,
<<<<<<< Updated upstream:database/LMS.sql
  `class_size` int NOT NULL,
  `trainer_name` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL,
  PRIMARY KEY (`class_no`,`course_id`) USING BTREE,
  KEY `fk_1` (`course_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;
=======
  `class_size` int(11) NOT NULL,
  `trainer_name` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
>>>>>>> Stashed changes:database/lms (1).sql

--
-- Dumping data for table `classes`
--

INSERT INTO `classes` (`course_id`, `class_no`, `start_date`, `end_date`, `start_time`, `end_time`, `class_size`, `trainer_name`) VALUES
(1, 2, '2021-09-01', '2021-09-30', '10:01:40', '19:01:40', 40, NULL);

-- --------------------------------------------------------

--
-- Table structure for table `class_assignment`
--

<<<<<<< Updated upstream:database/LMS.sql
DROP TABLE IF EXISTS `class_assignment`;
CREATE TABLE IF NOT EXISTS `class_assignment` (
  `course_id` int NOT NULL,
  `class_no` int NOT NULL,
  `staff_email` varchar(255) NOT NULL,
  PRIMARY KEY (`course_id`,`class_no`)
=======
CREATE TABLE `class_enrolment` (
  `staff_username` varchar(255) NOT NULL,
  `course_id` int(11) NOT NULL,
  `class_no` int(11) NOT NULL
>>>>>>> Stashed changes:database/lms (1).sql
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `course`
--

CREATE TABLE `course` (
  `course_id` int(11) NOT NULL,
  `course_name` text NOT NULL,
  `description` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

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

CREATE TABLE `learning_objective` (
  `course_id` int(11) NOT NULL,
  `learning_objective` varchar(255) NOT NULL
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

<<<<<<< Updated upstream:database/LMS.sql
DROP TABLE IF EXISTS `lesson`;
CREATE TABLE IF NOT EXISTS `lesson` (
  `course_id` int NOT NULL,
  `class_no` int NOT NULL,
  `lesson_no` int NOT NULL,
  `section_description` varchar(255) NOT NULL,
  PRIMARY KEY (`course_id`,`class_no`,`lesson_no`)
=======
CREATE TABLE `lesson` (
  `course_id` int(11) NOT NULL,
  `class_no` int(11) NOT NULL,
  `lesson_no` int(11) NOT NULL,
  `lesson_name` varchar(255) NOT NULL,
  `lesson_description` varchar(255) NOT NULL
>>>>>>> Stashed changes:database/lms (1).sql
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

CREATE TABLE `lesson_completion` (
  `course_id` int(11) NOT NULL,
  `class_no` int(11) NOT NULL,
  `lesson_no` int(11) NOT NULL,
  `staff_email` varchar(255) NOT NULL,
  `quiz_score` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `lesson_materials`
--

CREATE TABLE `lesson_materials` (
  `course_id` int(11) NOT NULL,
  `class_no` int(11) NOT NULL,
  `lesson_no` int(11) NOT NULL,
  `course_material_title` varchar(255) NOT NULL,
  `link` text NOT NULL
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

CREATE TABLE `materials_viewed` (
  `course_id` int(11) NOT NULL,
  `class_no` int(11) NOT NULL,
  `lesson_no` int(11) NOT NULL,
  `course_material_title` varchar(255) NOT NULL,
  `staff_email` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `quiz`
--

CREATE TABLE `quiz` (
  `quiz_id` int(11) NOT NULL,
  `quiz_name` varchar(255) NOT NULL DEFAULT 'Untitiled',
  `description` text NOT NULL,
  `uploader` varchar(255) NOT NULL,
  `duration` time NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

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

CREATE TABLE `quiz_options` (
  `qid` int(11) DEFAULT NULL,
  `ques_id` int(11) DEFAULT NULL,
  `optionz` text,
  `is_right` tinyint(1) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `quiz_questions`
--

CREATE TABLE `quiz_questions` (
  `qid` int(11) NOT NULL,
  `ques_id` int(11) NOT NULL,
  `question` text NOT NULL,
  `question_type` varchar(255) NOT NULL
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

<<<<<<< Updated upstream:database/LMS.sql
DROP TABLE IF EXISTS `staff`;
CREATE TABLE IF NOT EXISTS `staff` (
  `staff_email` varchar(255) NOT NULL,
  `years_of_service` int NOT NULL,
  PRIMARY KEY (`staff_email`)
=======
CREATE TABLE `staff` (
  `staff_username` varchar(255) NOT NULL,
  `staff_name` varchar(255) DEFAULT NULL,
  `role` varchar(255) NOT NULL DEFAULT 'Learner',
  `department` varchar(255) NOT NULL,
  `current_designation` varchar(255) NOT NULL
>>>>>>> Stashed changes:database/lms (1).sql
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
-- Indexes for dumped tables
--

--
-- Indexes for table `classes`
--
ALTER TABLE `classes`
  ADD PRIMARY KEY (`class_no`,`course_id`) USING BTREE,
  ADD KEY `fk_1` (`course_id`),
  ADD KEY `class_fk_2` (`trainer_name`);

--
-- Indexes for table `class_enrolment`
--
ALTER TABLE `class_enrolment`
  ADD PRIMARY KEY (`staff_username`,`course_id`,`class_no`),
  ADD KEY `staff_email` (`staff_username`),
  ADD KEY `fk4` (`class_no`,`course_id`);

--
-- Indexes for table `course`
--
ALTER TABLE `course`
  ADD PRIMARY KEY (`course_id`);

--
-- Indexes for table `learning_objective`
--
ALTER TABLE `learning_objective`
  ADD PRIMARY KEY (`course_id`,`learning_objective`),
  ADD KEY `fk6` (`course_id`);

--
-- Indexes for table `lesson`
--
ALTER TABLE `lesson`
  ADD PRIMARY KEY (`course_id`,`class_no`,`lesson_no`);

--
-- Indexes for table `lesson_completion`
--
ALTER TABLE `lesson_completion`
  ADD PRIMARY KEY (`course_id`,`class_no`,`lesson_no`);

--
-- Indexes for table `lesson_materials`
--
ALTER TABLE `lesson_materials`
  ADD PRIMARY KEY (`course_id`,`class_no`,`lesson_no`,`course_material_title`);

--
-- Indexes for table `materials_viewed`
--
ALTER TABLE `materials_viewed`
  ADD PRIMARY KEY (`course_id`,`class_no`,`lesson_no`,`course_material_title`);

--
-- Indexes for table `quiz`
--
ALTER TABLE `quiz`
  ADD PRIMARY KEY (`quiz_id`);

--
-- Indexes for table `quiz_options`
--
ALTER TABLE `quiz_options`
  ADD KEY `qid` (`qid`,`ques_id`);

--
-- Indexes for table `quiz_questions`
--
ALTER TABLE `quiz_questions`
  ADD PRIMARY KEY (`qid`,`ques_id`);

--
-- Indexes for table `staff`
--
ALTER TABLE `staff`
  ADD PRIMARY KEY (`staff_username`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `classes`
--
ALTER TABLE `classes`
  MODIFY `class_no` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT for table `course`
--
ALTER TABLE `course`
  MODIFY `course_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `quiz`
--
ALTER TABLE `quiz`
  MODIFY `quiz_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `classes`
--
ALTER TABLE `classes`
<<<<<<< Updated upstream:database/LMS.sql
  ADD CONSTRAINT `fk_1` FOREIGN KEY (`course_id`) REFERENCES `course` (`course_id`);

--
-- Constraints for table `class_assignment`
--
ALTER TABLE `class_assignment`
  ADD CONSTRAINT `fk3` FOREIGN KEY (`course_id`,`class_no`) REFERENCES `classes` (`course_id`, `class_no`);
=======
  ADD CONSTRAINT `class_fk_2` FOREIGN KEY (`trainer_name`) REFERENCES `staff` (`staff_username`),
  ADD CONSTRAINT `classes_fk_1` FOREIGN KEY (`course_id`) REFERENCES `course` (`course_id`);
>>>>>>> Stashed changes:database/lms (1).sql

--
-- Constraints for table `course_enrolment`
--
<<<<<<< Updated upstream:database/LMS.sql
ALTER TABLE `course_enrolment`
  ADD CONSTRAINT `fk4` FOREIGN KEY (`course_id`) REFERENCES `course` (`course_id`),
  ADD CONSTRAINT `staff_email` FOREIGN KEY (`staff_email`) REFERENCES `staff` (`staff_email`);
=======
ALTER TABLE `class_enrolment`
  ADD CONSTRAINT `fk4` FOREIGN KEY (`class_no`,`course_id`) REFERENCES `classes` (`class_no`, `course_id`),
  ADD CONSTRAINT `staff_email` FOREIGN KEY (`staff_username`) REFERENCES `staff` (`staff_username`);
>>>>>>> Stashed changes:database/lms (1).sql

--
-- Constraints for table `learning_objective`
--
ALTER TABLE `learning_objective`
  ADD CONSTRAINT `fk6` FOREIGN KEY (`course_id`) REFERENCES `course` (`course_id`);

--
-- Constraints for table `lesson`
--
ALTER TABLE `lesson`
<<<<<<< Updated upstream:database/LMS.sql
  ADD CONSTRAINT `fk7` FOREIGN KEY (`course_id`,`class_no`) REFERENCES `classes` (`course_id`, `class_no`);
=======
  ADD CONSTRAINT `lesson_fk1` FOREIGN KEY (`course_id`,`class_no`) REFERENCES `classes` (`course_id`, `class_no`);
>>>>>>> Stashed changes:database/lms (1).sql

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
