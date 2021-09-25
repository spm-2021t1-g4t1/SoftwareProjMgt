-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: localhost:8889
-- Generation Time: Sep 25, 2021 at 12:31 PM
-- Server version: 5.7.34
-- PHP Version: 7.4.21

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `LMS`
--

-- --------------------------------------------------------

--
-- Table structure for table `class`
--

CREATE TABLE `class` (
  `course_id` int(11) NOT NULL,
  `class_no` int(11) NOT NULL,
  `start_date` date NOT NULL,
  `end_date` date NOT NULL,
  `start_time` time NOT NULL,
  `end_time` time NOT NULL,
  `class_size` int(11) NOT NULL,
  `trainer_name` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `class_assignment`
--

CREATE TABLE `class_assignment` (
  `course_id` int(11) NOT NULL,
  `class_no` int(11) NOT NULL,
  `staff_email` varchar(255) NOT NULL
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

CREATE TABLE `course_enrolment` (
  `staff_email` varchar(255) NOT NULL,
  `course_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `learning_objective`
--

CREATE TABLE `learning_objective` (
  `course_id` int(11) NOT NULL,
  `learning_objective` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `lesson`
--

CREATE TABLE `lesson` (
  `course_id` int(11) NOT NULL,
  `class_no` int(11) NOT NULL,
  `lesson_no` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

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

-- --------------------------------------------------------

--
-- Table structure for table `staff`
--

CREATE TABLE `staff` (
  `staff_email` varchar(255) NOT NULL,
  `years_of_service` int(11) NOT NULL
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
-- Indexes for table `class`
--
ALTER TABLE `class`
  ADD PRIMARY KEY (`class_no`,`course_id`) USING BTREE,
  ADD KEY `fk_1` (`course_id`);

--
-- Indexes for table `class_assignment`
--
ALTER TABLE `class_assignment`
  ADD PRIMARY KEY (`course_id`,`class_no`);

--
-- Indexes for table `course`
--
ALTER TABLE `course`
  ADD PRIMARY KEY (`course_id`);

--
-- Indexes for table `course_enrolment`
--
ALTER TABLE `course_enrolment`
  ADD KEY `fk4` (`course_id`),
  ADD KEY `staff_email` (`staff_email`);

--
-- Indexes for table `learning_objective`
--
ALTER TABLE `learning_objective`
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
  ADD PRIMARY KEY (`staff_email`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `class`
--
ALTER TABLE `class`
  MODIFY `class_no` int(11) NOT NULL AUTO_INCREMENT;

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
-- Constraints for table `class`
--
ALTER TABLE `class`
  ADD CONSTRAINT `fk_1` FOREIGN KEY (`course_id`) REFERENCES `course` (`course_id`);

--
-- Constraints for table `class_assignment`
--
ALTER TABLE `class_assignment`
  ADD CONSTRAINT `fk3` FOREIGN KEY (`course_id`,`class_no`) REFERENCES `class` (`course_id`, `class_no`);

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
  ADD CONSTRAINT `fk7` FOREIGN KEY (`course_id`,`class_no`) REFERENCES `class` (`course_id`, `class_no`);

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
