-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: Sep 10, 2020 at 05:13 PM
-- Server version: 10.4.14-MariaDB
-- PHP Version: 7.4.9

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `codingthunder`
--

-- --------------------------------------------------------

--
-- Table structure for table `contacts`
--

CREATE TABLE `contacts` (
  `sno` int(11) NOT NULL,
  `name` text DEFAULT NULL,
  `phone_num` varchar(40) DEFAULT NULL,
  `email` varchar(50) DEFAULT NULL,
  `msg` text DEFAULT NULL,
  `date` datetime DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `contacts`
--

INSERT INTO `contacts` (`sno`, `name`, `phone_num`, `email`, `msg`, `date`) VALUES
(1, 'praven', '234234', 'dsfsdfdsff', 'sdfsdfdsfdfs', '2020-09-06 20:23:47'),
(2, 'asdfsdf', 'sdfdsf', 'sdfdsf', 'sdfsdf', '2020-09-06 20:50:16'),
(3, 'Vybhav Gupta ', '3315359944', 'Habib@gmail.com', 'Hi', '2020-09-06 21:02:14'),
(4, 'sdfsdf', 'sddsfd', 'sddsf', 'sdfsdf', '2020-09-06 21:08:00'),
(5, 'matka', '7883833', 'matka', 'sdfsdf', '2020-09-07 11:14:43'),
(6, 'Praveen Test', '72765511710', 'praveen.gupta141@gmail.com', 'Hi ', '2020-09-07 11:56:17'),
(7, 'desi', '32432', 'darru', 'dfsdfdf', '2020-09-07 12:15:33'),
(8, 'Rajni Gupta', '+917972546140', 'guptarajni69@gmail.com', 'hi', '2020-09-07 12:31:13'),
(9, 'Himanshu Pandey', '9760626248', 'hphimpandey@gmail.com', 'hehe', '2020-09-07 12:43:31'),
(10, 'Rajneesh', '7276551170', 'praveen.gupta141@gmail.com', 'I am using your blog', '2020-09-08 11:41:15'),
(11, 'raja', '838383838', 'desi@gmail.com', 'Hi this i youy blog', '2020-09-08 11:43:19'),
(12, 'dont know', '88484884', 'praveen.gupta139@gmail.com', 'Hi sorry finaly got it', '2020-09-08 11:46:39'),
(13, NULL, NULL, NULL, NULL, '2020-09-09 15:43:09'),
(14, 'Ramesh', '788878878', 'ramesh', 'Hi Good evinig', '2020-09-09 19:12:48'),
(15, 'Ramesh', '788878878', 'ramesh', 'Hi Good evinig', '2020-09-09 19:13:56'),
(16, 'Ramesh', '788878878', 'ramesh', 'Hi Good evinig', '2020-09-09 19:15:19'),
(17, 'praveen', '899300330', 'pg@gmail.com', 'call ture', '2020-09-10 09:55:34'),
(18, 'Ramesh', '788878878', 'ramesh', 'HI I am here', '2020-09-10 16:04:57');

-- --------------------------------------------------------

--
-- Table structure for table `posts`
--

CREATE TABLE `posts` (
  `sno` int(11) NOT NULL,
  `title` varchar(80) DEFAULT NULL,
  `slug` varchar(21) NOT NULL,
  `author` varchar(50) DEFAULT NULL,
  `content` text DEFAULT NULL,
  `date` datetime NOT NULL DEFAULT current_timestamp(),
  `img_file` varchar(12) NOT NULL,
  `tagline` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `posts`
--

INSERT INTO `posts` (`sno`, `title`, `slug`, `author`, `content`, `date`, `img_file`, `tagline`) VALUES
(1, 'Stocks Update', 'first-post', 'admin', 'This is very much awesome feature. We can get stock knowledge from here This is hectic session', '2020-09-09 17:01:19', 'about-bg.jpg', 'stocks'),
(2, 'Laptops Future', 'laptops', 'Prajwal', 'Future of laptops are very bright and shop will go on without having loss. Please do invest.', '2020-09-08 16:58:21', 'about-bg.jpg', 'Second Post'),
(3, 'Sugar is poison', 'sugar', 'Praveen Gupta', 'Avoid Sugar. I think no explanation is required here.', '2020-09-08 17:19:12', 'about-bg.jpg', 'Sugar Free'),
(5, 'Clay Pots', 'clay', 'Praveen Gupta', 'Clay pots are very god thing if you can afford it. It is the secret to be healthy in this world. and no need to worry for water you are getting from tap, vegetables full of pesticide. etc.', '2020-09-08 17:21:58', 'about-bg.jpg', 'mud pots are life'),
(6, 'Air conditioners are hell', 'air-conditioners', 'Praveen Gupta', 'Air conditioners are hell . You know why. It absorb mositure from body and leave you with pain. and then you become old quickly. Please avoid as much as possible.', '2020-09-08 17:23:44', 'about-bg.jpg', 'Blood Sucker'),
(7, 'Why IPO are risky', 'ipo', NULL, 'future is bright', '2020-09-09 16:58:28', 'post-bg.jpg', 'ipo'),
(8, 'Oiling Hair and Massage', 'oil-hair', NULL, 'Massage let you full fill with lots of postive vibes\r\n1. you feel energetic\r\n2. it test the strength of hair. lol\r\n3. You feel like naughty.', '2020-09-09 19:20:29', 'me.jpg', 'oil'),
(9, 'Friend', 'dost', NULL, 'THis is frinedx', '2020-09-09 21:00:02', 'me.jpg', 'Dosti'),
(10, 'Daily Routine', 'routine', NULL, 'Routine is boring and change is better.', '2020-09-09 21:09:05', 'me.jpg', 'Routine'),
(11, 'Mobile is Hell or Heaven', 'mobile', 'Vybhav', 'This is a very intersting topic ', '2020-09-09 21:32:44', 'me.jpg', 'Mobile PostMartum'),
(12, 'Hostel Life Is Boon', 'hostel', 'Praveen Gupta', 'Hostel life is very much different from home. But make a complete man/woman in all aspect of life.', '2020-09-10 09:46:51', 'friends.jpg', 'Hostel'),
(13, 'Table Chair important or not', 'table', 'Praveen Gupta', 'Table chair are very important to make body posture at right angle.\r\nYou much be very much concious of all this.', '2020-09-10 09:58:49', 'me.jpg', 'table chair'),
(14, 'Rajni , My Wife', 'rajni', 'Praveen Gupta', 'Rajni is very very cool teacher and my wife. She loves to cook and teach.\r\nMany things are waiting to learn from her.', '2020-09-10 10:06:31', 'rajni2.jpg', 'Rajni Gupta'),
(15, 'Teaching', 'teach', 'Rajni Gupta', 'Teching is a art .every body can\'t teach students .', '2020-09-10 12:59:14', '', 'Teachers Life'),
(16, 'Water TDS awareness', 'water', 'Prajwal Gupta', 'You should be aware of things about TDS. wanna see it see it in youtube.\r\nIt should be between 200-400. Otherwise you will fall ill very easily.\r\nLink is posted here.\r\nhttps://www.youtube.com/watch?v=yR8X1RBTjbM&t=247s\r\n\r\nhttps://compressimage.toolur.com/', '2020-09-10 16:18:04', 'prajwal.jpg', 'TDS, Water , Coconut');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `contacts`
--
ALTER TABLE `contacts`
  ADD PRIMARY KEY (`sno`);

--
-- Indexes for table `posts`
--
ALTER TABLE `posts`
  ADD PRIMARY KEY (`sno`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `contacts`
--
ALTER TABLE `contacts`
  MODIFY `sno` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=19;

--
-- AUTO_INCREMENT for table `posts`
--
ALTER TABLE `posts`
  MODIFY `sno` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=17;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
