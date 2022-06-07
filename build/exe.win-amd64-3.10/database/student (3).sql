-- phpMyAdmin SQL Dump
-- version 4.6.4
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jun 04, 2022 at 08:28 AM
-- Server version: 5.7.14
-- PHP Version: 5.6.25

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `face_recognizer`
--

-- --------------------------------------------------------

--
-- Table structure for table `student`
--

CREATE TABLE `student` (
  `dep` varchar(45) NOT NULL,
  `course` varchar(45) NOT NULL,
  `year` varchar(45) NOT NULL,
  `semester` varchar(45) NOT NULL,
  `student_id` int(45) NOT NULL,
  `name` varchar(45) NOT NULL,
  `division` varchar(45) NOT NULL,
  `roll` varchar(45) NOT NULL,
  `gender` varchar(45) NOT NULL,
  `dob` varchar(45) NOT NULL,
  `email` varchar(45) NOT NULL,
  `phone` varchar(45) NOT NULL,
  `address` varchar(45) NOT NULL,
  `teacher` varchar(45) NOT NULL,
  `photosample` varchar(45) NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Dumping data for table `student`
--

INSERT INTO `student` (`dep`, `course`, `year`, `semester`, `student_id`, `name`, `division`, `roll`, `gender`, `dob`, `email`, `phone`, `address`, `teacher`, `photosample`) VALUES
('Computer', 'FE', '2020-21', 'Semester-1', 1, 'Sejal', 'A', '4', 'Female', '12-03-2001', 'sejal@gmail.com', '8798653453', 'Delhi', 'Sami', 'Yes'),
('IT', 'FE', '2020-21', 'Semester-1', 2, 'Sejal', 'A', '2', 'Female', '02-04-2001', 'sejal@gmail.com', '8795464326', 'Simla', 'Sami', 'No'),
('Mechnical', 'BE', '2021-22', 'Semester-1', 3, 'Zozo', 'C', '12', 'Male', '12-03-2003', 'zozo@gmail.com', '9896754563', 'kashmir', 'Sami', 'No'),
('Computer', 'FE', '2021-22', 'Semester-1', 4, 'Samo', 'C', '14', 'Female', '12-02-2005', 'samo@gmail.com', '7684563256', 'delhi', 'Rana', 'Yes'),
('Computer', 'FE', '2020-21', 'Semester-1', 121, 'sheetal', 'B', '34', 'Male', '27-06-1995', 'mk@gmail.com', '6202445148', 'nnnnn', 'memo', 'Yes');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `student`
--
ALTER TABLE `student`
  ADD PRIMARY KEY (`student_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `student`
--
ALTER TABLE `student`
  MODIFY `student_id` int(45) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=122;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
