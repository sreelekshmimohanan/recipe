-- phpMyAdmin SQL Dump
-- version 4.1.6
-- http://www.phpmyadmin.net
--
-- Host: 127.0.0.1
-- Generation Time: Mar 14, 2024 at 07:18 PM
-- Server version: 5.6.16
-- PHP Version: 5.5.9

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `recipe_db`
--

-- --------------------------------------------------------

--
-- Table structure for table `auth_group`
--

CREATE TABLE IF NOT EXISTS `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Table structure for table `auth_group_permissions`
--

CREATE TABLE IF NOT EXISTS `auth_group_permissions` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Table structure for table `auth_permission`
--

CREATE TABLE IF NOT EXISTS `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=93 ;

--
-- Dumping data for table `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add log entry', 1, 'add_logentry'),
(2, 'Can change log entry', 1, 'change_logentry'),
(3, 'Can delete log entry', 1, 'delete_logentry'),
(4, 'Can view log entry', 1, 'view_logentry'),
(5, 'Can add permission', 2, 'add_permission'),
(6, 'Can change permission', 2, 'change_permission'),
(7, 'Can delete permission', 2, 'delete_permission'),
(8, 'Can view permission', 2, 'view_permission'),
(9, 'Can add group', 3, 'add_group'),
(10, 'Can change group', 3, 'change_group'),
(11, 'Can delete group', 3, 'delete_group'),
(12, 'Can view group', 3, 'view_group'),
(13, 'Can add user', 4, 'add_user'),
(14, 'Can change user', 4, 'change_user'),
(15, 'Can delete user', 4, 'delete_user'),
(16, 'Can view user', 4, 'view_user'),
(17, 'Can add content type', 5, 'add_contenttype'),
(18, 'Can change content type', 5, 'change_contenttype'),
(19, 'Can delete content type', 5, 'delete_contenttype'),
(20, 'Can view content type', 5, 'view_contenttype'),
(21, 'Can add session', 6, 'add_session'),
(22, 'Can change session', 6, 'change_session'),
(23, 'Can delete session', 6, 'delete_session'),
(24, 'Can view session', 6, 'view_session'),
(25, 'Can add customer_reg', 7, 'add_customer_reg'),
(26, 'Can change customer_reg', 7, 'change_customer_reg'),
(27, 'Can delete customer_reg', 7, 'delete_customer_reg'),
(28, 'Can view customer_reg', 7, 'view_customer_reg'),
(29, 'Can add staff_reg', 8, 'add_staff_reg'),
(30, 'Can change staff_reg', 8, 'change_staff_reg'),
(31, 'Can delete staff_reg', 8, 'delete_staff_reg'),
(32, 'Can view staff_reg', 8, 'view_staff_reg'),
(33, 'Can add tbl_login', 9, 'add_tbl_login'),
(34, 'Can change tbl_login', 9, 'change_tbl_login'),
(35, 'Can delete tbl_login', 9, 'delete_tbl_login'),
(36, 'Can view tbl_login', 9, 'view_tbl_login'),
(37, 'Can add subcategory', 10, 'add_subcategory'),
(38, 'Can change subcategory', 10, 'change_subcategory'),
(39, 'Can delete subcategory', 10, 'delete_subcategory'),
(40, 'Can view subcategory', 10, 'view_subcategory'),
(41, 'Can add category', 11, 'add_category'),
(42, 'Can change category', 11, 'change_category'),
(43, 'Can delete category', 11, 'delete_category'),
(44, 'Can view category', 11, 'view_category'),
(45, 'Can add product_category', 12, 'add_product_category'),
(46, 'Can change product_category', 12, 'change_product_category'),
(47, 'Can delete product_category', 12, 'delete_product_category'),
(48, 'Can view product_category', 12, 'view_product_category'),
(49, 'Can add tbl_product', 13, 'add_tbl_product'),
(50, 'Can change tbl_product', 13, 'change_tbl_product'),
(51, 'Can delete tbl_product', 13, 'delete_tbl_product'),
(52, 'Can view tbl_product', 13, 'view_tbl_product'),
(53, 'Can add cart_child', 14, 'add_cart_child'),
(54, 'Can change cart_child', 14, 'change_cart_child'),
(55, 'Can delete cart_child', 14, 'delete_cart_child'),
(56, 'Can view cart_child', 14, 'view_cart_child'),
(57, 'Can add cart_master', 15, 'add_cart_master'),
(58, 'Can change cart_master', 15, 'change_cart_master'),
(59, 'Can delete cart_master', 15, 'delete_cart_master'),
(60, 'Can view cart_master', 15, 'view_cart_master'),
(61, 'Can add card', 16, 'add_card'),
(62, 'Can change card', 16, 'change_card'),
(63, 'Can delete card', 16, 'delete_card'),
(64, 'Can view card', 16, 'view_card'),
(65, 'Can add tbl_payment', 17, 'add_tbl_payment'),
(66, 'Can change tbl_payment', 17, 'change_tbl_payment'),
(67, 'Can delete tbl_payment', 17, 'delete_tbl_payment'),
(68, 'Can view tbl_payment', 17, 'view_tbl_payment'),
(69, 'Can add tbl_cassign', 18, 'add_tbl_cassign'),
(70, 'Can change tbl_cassign', 18, 'change_tbl_cassign'),
(71, 'Can delete tbl_cassign', 18, 'delete_tbl_cassign'),
(72, 'Can view tbl_cassign', 18, 'view_tbl_cassign'),
(73, 'Can add tbl_courier', 19, 'add_tbl_courier'),
(74, 'Can change tbl_courier', 19, 'change_tbl_courier'),
(75, 'Can delete tbl_courier', 19, 'delete_tbl_courier'),
(76, 'Can view tbl_courier', 19, 'view_tbl_courier'),
(77, 'Can add tbl_delivery', 20, 'add_tbl_delivery'),
(78, 'Can change tbl_delivery', 20, 'change_tbl_delivery'),
(79, 'Can delete tbl_delivery', 20, 'delete_tbl_delivery'),
(80, 'Can view tbl_delivery', 20, 'view_tbl_delivery'),
(81, 'Can add tbl_item', 21, 'add_tbl_item'),
(82, 'Can change tbl_item', 21, 'change_tbl_item'),
(83, 'Can delete tbl_item', 21, 'delete_tbl_item'),
(84, 'Can view tbl_item', 21, 'view_tbl_item'),
(85, 'Can add tbl_recipes', 22, 'add_tbl_recipes'),
(86, 'Can change tbl_recipes', 22, 'change_tbl_recipes'),
(87, 'Can delete tbl_recipes', 22, 'delete_tbl_recipes'),
(88, 'Can view tbl_recipes', 22, 'view_tbl_recipes'),
(89, 'Can add tbl_ingrediantcalc', 23, 'add_tbl_ingrediantcalc'),
(90, 'Can change tbl_ingrediantcalc', 23, 'change_tbl_ingrediantcalc'),
(91, 'Can delete tbl_ingrediantcalc', 23, 'delete_tbl_ingrediantcalc'),
(92, 'Can view tbl_ingrediantcalc', 23, 'view_tbl_ingrediantcalc');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user`
--

CREATE TABLE IF NOT EXISTS `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_groups`
--

CREATE TABLE IF NOT EXISTS `auth_user_groups` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_user_permissions`
--

CREATE TABLE IF NOT EXISTS `auth_user_user_permissions` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Table structure for table `django_admin_log`
--

CREATE TABLE IF NOT EXISTS `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Table structure for table `django_content_type`
--

CREATE TABLE IF NOT EXISTS `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=24 ;

--
-- Dumping data for table `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(1, 'admin', 'logentry'),
(3, 'auth', 'group'),
(2, 'auth', 'permission'),
(4, 'auth', 'user'),
(5, 'contenttypes', 'contenttype'),
(16, 'recipe', 'card'),
(14, 'recipe', 'cart_child'),
(15, 'recipe', 'cart_master'),
(11, 'recipe', 'category'),
(7, 'recipe', 'customer_reg'),
(12, 'recipe', 'product_category'),
(8, 'recipe', 'staff_reg'),
(10, 'recipe', 'subcategory'),
(18, 'recipe', 'tbl_cassign'),
(19, 'recipe', 'tbl_courier'),
(20, 'recipe', 'tbl_delivery'),
(23, 'recipe', 'tbl_ingrediantcalc'),
(21, 'recipe', 'tbl_item'),
(9, 'recipe', 'tbl_login'),
(17, 'recipe', 'tbl_payment'),
(13, 'recipe', 'tbl_product'),
(22, 'recipe', 'tbl_recipes'),
(6, 'sessions', 'session');

-- --------------------------------------------------------

--
-- Table structure for table `django_migrations`
--

CREATE TABLE IF NOT EXISTS `django_migrations` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=34 ;

--
-- Dumping data for table `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2024-02-20 10:51:55.646811'),
(2, 'auth', '0001_initial', '2024-02-20 10:51:56.269276'),
(3, 'admin', '0001_initial', '2024-02-20 10:51:56.432080'),
(4, 'admin', '0002_logentry_remove_auto_add', '2024-02-20 10:51:56.439606'),
(5, 'admin', '0003_logentry_add_action_flag_choices', '2024-02-20 10:51:56.454082'),
(6, 'contenttypes', '0002_remove_content_type_name', '2024-02-20 10:51:56.521541'),
(7, 'auth', '0002_alter_permission_name_max_length', '2024-02-20 10:51:56.553868'),
(8, 'auth', '0003_alter_user_email_max_length', '2024-02-20 10:51:56.591050'),
(9, 'auth', '0004_alter_user_username_opts', '2024-02-20 10:51:56.608806'),
(10, 'auth', '0005_alter_user_last_login_null', '2024-02-20 10:51:56.640949'),
(11, 'auth', '0006_require_contenttypes_0002', '2024-02-20 10:51:56.648339'),
(12, 'auth', '0007_alter_validators_add_error_messages', '2024-02-20 10:51:56.660787'),
(13, 'auth', '0008_alter_user_username_max_length', '2024-02-20 10:51:56.692115'),
(14, 'auth', '0009_alter_user_last_name_max_length', '2024-02-20 10:51:56.727278'),
(15, 'auth', '0010_alter_group_name_max_length', '2024-02-20 10:51:56.769190'),
(16, 'auth', '0011_update_proxy_permissions', '2024-02-20 10:51:56.779634'),
(17, 'auth', '0012_alter_user_first_name_max_length', '2024-02-20 10:51:56.806474'),
(18, 'recipe', '0001_initial', '2024-02-20 10:51:57.228526'),
(19, 'sessions', '0001_initial', '2024-02-20 10:51:57.280348'),
(20, 'recipe', '0002_category_subcategory', '2024-02-20 11:31:55.340524'),
(21, 'recipe', '0003_product_category', '2024-02-20 11:52:31.077285'),
(22, 'recipe', '0004_tbl_product', '2024-02-20 13:41:36.466158'),
(23, 'recipe', '0005_cart_child_cart_master', '2024-02-21 04:26:37.445545'),
(24, 'recipe', '0006_card', '2024-02-21 04:50:47.881039'),
(25, 'recipe', '0007_tbl_payment', '2024-02-21 05:05:18.218192'),
(26, 'recipe', '0008_tbl_cassign_tbl_courier_tbl_delivery', '2024-02-21 05:17:35.718159'),
(27, 'recipe', '0009_tbl_item', '2024-02-23 07:35:00.925697'),
(28, 'recipe', '0010_alter_tbl_item_item_desc', '2024-02-23 07:48:48.342806'),
(29, 'recipe', '0011_auto_20240223_1513', '2024-02-23 09:44:17.510613'),
(30, 'recipe', '0012_alter_tbl_recipes_recipe_desc', '2024-02-23 09:52:32.947554'),
(31, 'recipe', '0013_tbl_ingrediantcalc', '2024-02-23 10:40:33.326529'),
(32, 'recipe', '0014_staff_reg_status', '2024-03-14 14:58:11.928997'),
(33, 'recipe', '0015_alter_tbl_payment_pay_date', '2024-03-14 18:09:39.392192');

-- --------------------------------------------------------

--
-- Table structure for table `django_session`
--

CREATE TABLE IF NOT EXISTS `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('3win2a2g5zluyxzepel9rnc5m5794ad3', '.eJyrVsrJT8_MK0lJLUnMzFGyUkpMyc3Mc0jPBfL0kvNzlXQgIjAZpVoAy3IRew:1rch9o:qAGb7cMkhxaPbUeMLq7rpfuXe0iP_JTW3SB6pb10ngY', '2024-03-06 07:36:44.771344'),
('62kq5f31vq691b9gij08omd6faax2dmq', 'e30:1rkpZu:k3znFRh7AHcG9mJR1NddGZ_fIwMspw1R-FetFb3SkNA', '2024-03-28 18:13:18.341645'),
('dzwt6k8ea75xq9akc00xcb0qmxxxka1t', 'eyJjdWlkIjoxLCJjdW5hbWUiOiJKZXJpbiIsImN1ZW1haWwiOiJqQGdtYWlsLmNvbSJ9:1rcgq0:NgLg96u7s59o4byEA3AlTcBe_ItL0nQ4A3gOsmSBREY', '2024-03-06 07:16:16.878600'),
('fgahdaw9q15i0ls7ruixjphcmhv4dwxm', 'e30:1rhRql:eIzIIo-KFrHMYpoDA6EnZ9A_2scehBeyp2-lpdRdbVg', '2024-03-19 10:16:43.246746'),
('k47lea6ctldy33xvd8ereiftik666mz8', '.eJyrVsrJT8_MK0lJLUnMzFGyUkpMyc3Mc0jPBfL0kvNzlXQgIjAZpVoAy3IRew:1rkmdq:snRBL_NvUYLGONCP9RCc3B1xiNTdRHPhKWq01f6weDw', '2024-03-28 15:05:10.629231'),
('qqpjppc28hu07bz878hbujssm2ldcp7l', 'e30:1rdXRu:mswq9rdA_IiT-THPRTgbmAx6iT-9YLoahNmXc_3quNQ', '2024-03-08 15:26:54.357271'),
('sb1lyd36l6oyseqwbtq8iez2m7mxuryh', 'eyJjdWlkIjoxLCJjdW5hbWUiOiJKZXJpbiIsImN1ZW1haWwiOiJqQGdtYWlsLmNvbSJ9:1rh4hd:LOWZG6WCRiCtnbQ9Qi70FPiRmKAthXunp1Ofh-_8I6Q', '2024-03-18 09:33:45.990649'),
('vdoqsrpjby2jzzy4mqk3hoy5c3gjrv75', 'e30:1rhSK8:qVJOmGICmx5ljd-jWtmo6QrEb7ou1y1X0BIQZiJNDFM', '2024-03-19 10:47:04.551820'),
('wap62ydg21slmyr3g3nsf4px5arfvdh4', '.eJyrVsrJT8_MK0lJLUnMzFGyUkpMyc3Mc0jPBfL0kvNzlXQgIjAZpVoAy3IRew:1rd01L:XRAecctSVQxEIDZ5BMuFLBSzrFOot8IE8X9YThS8z8E', '2024-03-07 03:45:15.651732');

-- --------------------------------------------------------

--
-- Table structure for table `recipe_card`
--

CREATE TABLE IF NOT EXISTS `recipe_card` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `card_holder` varchar(150) NOT NULL,
  `card_no` varchar(150) NOT NULL,
  `exp_date` varchar(150) NOT NULL,
  `cvv` varchar(150) NOT NULL,
  `customer_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `recipe_card_customer_id_9b2d3aeb_fk_recipe_customer_reg_id` (`customer_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=3 ;

--
-- Dumping data for table `recipe_card`
--

INSERT INTO `recipe_card` (`id`, `card_holder`, `card_no`, `exp_date`, `cvv`, `customer_id`) VALUES
(1, 'Jerin', '8978234423424244', '3023-02-04', '234', 1),
(2, 'Jerin 1', '8297428365653243', '2043-04-23', '124', 1);

-- --------------------------------------------------------

--
-- Table structure for table `recipe_cart_child`
--

CREATE TABLE IF NOT EXISTS `recipe_cart_child` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `cart_master_id` varchar(150) NOT NULL,
  `item_id` varchar(150) NOT NULL,
  `cart_qty` int(10) unsigned NOT NULL,
  `cart_price` decimal(10,2) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=8 ;

--
-- Dumping data for table `recipe_cart_child`
--

INSERT INTO `recipe_cart_child` (`id`, `cart_master_id`, `item_id`, `cart_qty`, `cart_price`) VALUES
(1, '1', '1', 2, '400.00'),
(2, '1', '4', 1, '300.00'),
(4, '2', '4', 1, '300.00'),
(5, '3', '4', 2, '600.00'),
(7, '4', '4', 2, '600.00');

-- --------------------------------------------------------

--
-- Table structure for table `recipe_cart_master`
--

CREATE TABLE IF NOT EXISTS `recipe_cart_master` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `customert_id` varchar(150) NOT NULL,
  `cart_tot_amt` decimal(10,2) NOT NULL,
  `cart_status` varchar(150) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=5 ;

--
-- Dumping data for table `recipe_cart_master`
--

INSERT INTO `recipe_cart_master` (`id`, `customert_id`, `cart_tot_amt`, `cart_status`) VALUES
(1, '1', '700.00', 'Deactive'),
(2, '1', '300.00', 'Deactive'),
(3, '1', '600.00', 'Deactive'),
(4, '1', '600.00', 'Active');

-- --------------------------------------------------------

--
-- Table structure for table `recipe_category`
--

CREATE TABLE IF NOT EXISTS `recipe_category` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `category_name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=3 ;

--
-- Dumping data for table `recipe_category`
--

INSERT INTO `recipe_category` (`id`, `category_name`) VALUES
(1, 'Veg'),
(2, 'Non-Veg');

-- --------------------------------------------------------

--
-- Table structure for table `recipe_customer_reg`
--

CREATE TABLE IF NOT EXISTS `recipe_customer_reg` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `fname` varchar(150) NOT NULL,
  `lname` varchar(150) NOT NULL,
  `district` varchar(150) NOT NULL,
  `street` varchar(150) NOT NULL,
  `phone` varchar(150) NOT NULL,
  `gender` varchar(150) NOT NULL,
  `dob` varchar(150) NOT NULL,
  `email` varchar(150) NOT NULL,
  `password` varchar(150) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=3 ;

--
-- Dumping data for table `recipe_customer_reg`
--

INSERT INTO `recipe_customer_reg` (`id`, `fname`, `lname`, `district`, `street`, `phone`, `gender`, `dob`, `email`, `password`) VALUES
(1, 'Jerin', 'James', 'Pathanamthitta', 'Konni', '9809898987', 'male', '1998-01-09', 'j@gmail.com', '123'),
(2, 'sam', 's', 'Kollam', 'punalur', '9876543210', 'male', '1998-04-05', 's@gmail.com', '123');

-- --------------------------------------------------------

--
-- Table structure for table `recipe_product_category`
--

CREATE TABLE IF NOT EXISTS `recipe_product_category` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `category_name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=5 ;

--
-- Dumping data for table `recipe_product_category`
--

INSERT INTO `recipe_product_category` (`id`, `category_name`) VALUES
(1, 'Pickles'),
(4, 'Powders');

-- --------------------------------------------------------

--
-- Table structure for table `recipe_staff_reg`
--

CREATE TABLE IF NOT EXISTS `recipe_staff_reg` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `fname` varchar(150) NOT NULL,
  `lname` varchar(150) NOT NULL,
  `district` varchar(150) NOT NULL,
  `street` varchar(150) NOT NULL,
  `phone` varchar(150) NOT NULL,
  `gender` varchar(150) NOT NULL,
  `dob` varchar(150) NOT NULL,
  `email` varchar(150) NOT NULL,
  `password` varchar(150) NOT NULL,
  `status` varchar(150) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=2 ;

--
-- Dumping data for table `recipe_staff_reg`
--

INSERT INTO `recipe_staff_reg` (`id`, `fname`, `lname`, `district`, `street`, `phone`, `gender`, `dob`, `email`, `password`, `status`) VALUES
(1, 'Davood', 's', 'Pathanamthitta', 'Konni', '9809898987', 'Male', '1998-12-09', 'd@gmail.com', '123', 'Active');

-- --------------------------------------------------------

--
-- Table structure for table `recipe_subcategory`
--

CREATE TABLE IF NOT EXISTS `recipe_subcategory` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `subcat_name` varchar(150) NOT NULL,
  `category_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `recipe_subcategory_category_id_61721bca_fk_recipe_category_id` (`category_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=7 ;

--
-- Dumping data for table `recipe_subcategory`
--

INSERT INTO `recipe_subcategory` (`id`, `subcat_name`, `category_id`) VALUES
(1, 'Break Fast', 1),
(2, 'Lunch', 1),
(3, 'Dinner', 1),
(4, 'Break Fast', 2),
(5, 'Lunch', 2),
(6, 'Dinner', 2);

-- --------------------------------------------------------

--
-- Table structure for table `recipe_tbl_cassign`
--

CREATE TABLE IF NOT EXISTS `recipe_tbl_cassign` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `courier_id` varchar(150) NOT NULL,
  `cassign_date` varchar(150) NOT NULL,
  `cart_master_id` varchar(150) NOT NULL,
  `status` varchar(150) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=3 ;

--
-- Dumping data for table `recipe_tbl_cassign`
--

INSERT INTO `recipe_tbl_cassign` (`id`, `courier_id`, `cassign_date`, `cart_master_id`, `status`) VALUES
(1, '1', '2024-02-21', '1', 'delivered'),
(2, '3', '2024-02-20', '2', 'delivered');

-- --------------------------------------------------------

--
-- Table structure for table `recipe_tbl_courier`
--

CREATE TABLE IF NOT EXISTS `recipe_tbl_courier` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `staff_id` varchar(150) NOT NULL,
  `co_name` varchar(150) NOT NULL,
  `co_city` varchar(150) NOT NULL,
  `co_dist` varchar(150) NOT NULL,
  `co_pin` varchar(150) NOT NULL,
  `co_street` varchar(150) NOT NULL,
  `co_phone` varchar(150) NOT NULL,
  `email` varchar(150) NOT NULL,
  `password` varchar(150) NOT NULL,
  `co_status` varchar(150) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=4 ;

--
-- Dumping data for table `recipe_tbl_courier`
--

INSERT INTO `recipe_tbl_courier` (`id`, `staff_id`, `co_name`, `co_city`, `co_dist`, `co_pin`, `co_street`, `co_phone`, `email`, `password`, `co_status`) VALUES
(1, 'admin', 'Fast Track', 'Konni', 'Pathanamthitta', '679878', 'Konni', '8957666574', 'ft@gmail.com', '123', 'Active'),
(3, '1', 'DCL', 'Fort Kochi', 'Ernakulam', '679878', 'Palarivattom', '8756774887', 'dc@gmail.com', '123', 'Active');

-- --------------------------------------------------------

--
-- Table structure for table `recipe_tbl_delivery`
--

CREATE TABLE IF NOT EXISTS `recipe_tbl_delivery` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `cassign_id` varchar(150) NOT NULL,
  `del_date` varchar(150) NOT NULL,
  `cart_master_id` varchar(150) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=3 ;

--
-- Dumping data for table `recipe_tbl_delivery`
--

INSERT INTO `recipe_tbl_delivery` (`id`, `cassign_id`, `del_date`, `cart_master_id`) VALUES
(1, '1', '2024-02-22', '1'),
(2, '2', '2024-02-21', '2');

-- --------------------------------------------------------

--
-- Table structure for table `recipe_tbl_ingrediantcalc`
--

CREATE TABLE IF NOT EXISTS `recipe_tbl_ingrediantcalc` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `ing_unit` decimal(10,2) NOT NULL,
  `ingrediant` varchar(150) NOT NULL,
  `item_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `recipe_tbl_ingrediantcalc_item_id_8ababbef_fk_recipe_tbl_item_id` (`item_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=18 ;

--
-- Dumping data for table `recipe_tbl_ingrediantcalc`
--

INSERT INTO `recipe_tbl_ingrediantcalc` (`id`, `ing_unit`, `ingrediant`, `item_id`) VALUES
(1, '1.50', 'wholemeal flour', 1),
(2, '1.00', 'cup hot water', 1),
(3, '1.00', '(tbsp) salt', 1),
(4, '1.00', 'small onion, chopped', 3),
(5, '2.00', 'cloves garlic, minced', 3),
(6, '3.00', 'tablespoons curry powder', 3),
(7, '1.00', 'teaspoon ground cinnamon', 3),
(8, '1.00', 'bay leaf', 3),
(9, '2.00', 'skinless, boneless chicken breast halves - cut into bite-size pieces', 3),
(10, '1.00', 'tablespoon tomato paste', 3),
(11, '1.50', 'cup coconut milk', 3),
(12, '1.50', 'teaspoon cayenne pepper', 3),
(13, '1.00', 'Chicken', 4),
(14, '1.00', 'cup buttermilk', 4),
(15, '2.00', 'cups all-purpose flour for coating', 4),
(16, '2.00', 'quarts vegetable oil for frying', 4),
(17, '2.00', 'tbspn salt and pepper to taste', 4);

-- --------------------------------------------------------

--
-- Table structure for table `recipe_tbl_item`
--

CREATE TABLE IF NOT EXISTS `recipe_tbl_item` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `item_desc` varchar(500) NOT NULL,
  `item_name` varchar(150) NOT NULL,
  `item_status` varchar(150) NOT NULL,
  `item_image` varchar(150) NOT NULL,
  `category_id` bigint(20) NOT NULL,
  `subcategory_id` bigint(20) NOT NULL,
  `recipe_status` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `recipe_tbl_item_category_id_62b621ac_fk_recipe_category_id` (`category_id`),
  KEY `recipe_tbl_item_subcategory_id_b0109bf4_fk_recipe_subcategory_id` (`subcategory_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=5 ;

--
-- Dumping data for table `recipe_tbl_item`
--

INSERT INTO `recipe_tbl_item` (`id`, `item_desc`, `item_name`, `item_status`, `item_image`, `category_id`, `subcategory_id`, `recipe_status`) VALUES
(1, 'Roti or Phulka or Chapati is an everyday staple Indian flatbread that is made in nearly every part of India. This roti or chapati recipe of an unleavened flatbread is made with basic ingredients – whole wheat flour, ghee, salt and water.', 'Chappathi (Roti)', 'Available', '111_eZ9AFQ9.jpg', 1, 1, 'added'),
(3, 'Chicken curry from the Indian subcontinent typically features chicken stewed in a tomato-based sauce seasoned with aromatic spices.', 'Chicken Curry', 'Available', 'nbj.jpg', 2, 6, 'added'),
(4, 'Chicken Fry | Indian Fried Chicken is a popular dry chicken preparation usually served as an appetizer | starter. This quick chicken fry is made with spices like chilli powder, turmeric, garam masala, ginger, garlic and curry leaves.', 'Chicken Fry', 'Available', 'Spicy-Chicken-Fry-Recipe.jpg', 2, 6, 'added');

-- --------------------------------------------------------

--
-- Table structure for table `recipe_tbl_login`
--

CREATE TABLE IF NOT EXISTS `recipe_tbl_login` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `email` varchar(150) NOT NULL,
  `password` varchar(150) NOT NULL,
  `user_type` varchar(150) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=7 ;

--
-- Dumping data for table `recipe_tbl_login`
--

INSERT INTO `recipe_tbl_login` (`id`, `email`, `password`, `user_type`) VALUES
(1, 'j@gmail.com', '123', 'customer'),
(2, 'd@gmail.com', '123', 'staff'),
(3, 'ft@gmail.com', 'Jdhhd@123', 'courier'),
(4, 'admin@gmail.com', 'wer323Sdfew@123', 'courier'),
(5, 'dc@gmail.com', 'Jdjjjj@1234', 'courier'),
(6, 's@gmail.com', '123', 'customer');

-- --------------------------------------------------------

--
-- Table structure for table `recipe_tbl_payment`
--

CREATE TABLE IF NOT EXISTS `recipe_tbl_payment` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `cart_master_id` varchar(150) NOT NULL,
  `card_id` varchar(150) NOT NULL,
  `pay_date` date NOT NULL,
  `status` varchar(150) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=4 ;

--
-- Dumping data for table `recipe_tbl_payment`
--

INSERT INTO `recipe_tbl_payment` (`id`, `cart_master_id`, `card_id`, `pay_date`, `status`) VALUES
(1, '1', '1', '2024-02-21', 'Assigned'),
(2, '2', '1', '2024-02-21', 'Assigned'),
(3, '3', '1', '2024-03-14', 'paid');

-- --------------------------------------------------------

--
-- Table structure for table `recipe_tbl_product`
--

CREATE TABLE IF NOT EXISTS `recipe_tbl_product` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `cat_id` varchar(150) NOT NULL,
  `item_name` varchar(150) NOT NULL,
  `item_desc` varchar(150) NOT NULL,
  `item_price` decimal(10,2) NOT NULL,
  `item_status` varchar(150) NOT NULL,
  `item_stock` decimal(10,2) NOT NULL,
  `item_image` varchar(150) NOT NULL,
  `customer_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `recipe_tbl_product_customer_id_081e1c64_fk_recipe_cu` (`customer_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=5 ;

--
-- Dumping data for table `recipe_tbl_product`
--

INSERT INTO `recipe_tbl_product` (`id`, `cat_id`, `item_name`, `item_desc`, `item_price`, `item_status`, `item_stock`, `item_image`, `customer_id`) VALUES
(1, '4', 'Chilly Powder', 'Red Chilli Powder (250 gm) ORGANIC', '200.00', 'Available', '8.00', 'image-Red_Chilli_Karam_Podi-1590824175448.jpg', 1),
(3, '4', 'Turmeric Powder', 'TURMERIC POWDER\r\n(GOLDEN SPICE)', '150.00', 'Available', '20.00', 'TURMERIC-Slides-V3_2-1-1.jpg', 1),
(4, '4', 'Coriander Powder', 'Coriander Powder 500g', '300.00', 'Available', '26.00', '11.jpg', 1);

-- --------------------------------------------------------

--
-- Table structure for table `recipe_tbl_recipes`
--

CREATE TABLE IF NOT EXISTS `recipe_tbl_recipes` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `recipe_desc` varchar(1000) NOT NULL,
  `recipe_name` varchar(150) NOT NULL,
  `pre_time` varchar(150) NOT NULL,
  `cook_time` varchar(150) NOT NULL,
  `item_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `recipe_tbl_recipes_item_id_94f59ca1_fk_recipe_tbl_item_id` (`item_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=4 ;

--
-- Dumping data for table `recipe_tbl_recipes`
--

INSERT INTO `recipe_tbl_recipes` (`id`, `recipe_desc`, `recipe_name`, `pre_time`, `cook_time`, `item_id`) VALUES
(1, 'Saute a diced onion in olive oil until lightly browned. Stir in the seasonings (garlic, curry powder, cinnamon, paprika, bay leaf, ginger, sugar and salt). Add the chicken pieces, tomato paste, yogurt, and coconut milk. Bring to a boil, reduce the heat, and simmer for 20 to 25 minutes. Remove the bay leaf and stir in the lemon juice and cayenne pepper. Continue simmering for about 5 more minutes.', 'Indian Chicken Curry ', '1/2 HR', '2 HR', 3),
(2, 'In a large bowl, stir together the flours and salt. Use a wooden spoon to stir in the olive oil and enough water to make a soft dough that is elastic but not sticky.Knead the dough on a lightly floured surface for 5-10 mins until it is smooth. Divide into 10 pieces, or less if you want bigger breads. Roll each piece into a ball. Let rest for a few mins.', 'Chappathi (Roti) (10 no)', '1 HR', '1 HR', 1),
(3, 'Marinating chicken pieces is key before frying. This helps soften the meat and adds tenderness to the final chicken fry pieces\r\nUse chicken thigh for better results than chicken breast, although, I have used a mix of both here. Chicken drumstick can give you good results too. This is because the thigh and drumstick pieces have more fat than chicken breast and lend themselves well to frying, without drying out.', 'EASY CHICKEN FRY RECIPE', '1 HR', '2 HR', 4);

--
-- Constraints for dumped tables
--

--
-- Constraints for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  ADD CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`);

--
-- Constraints for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- Constraints for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  ADD CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  ADD CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`);

--
-- Constraints for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  ADD CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `recipe_card`
--
ALTER TABLE `recipe_card`
  ADD CONSTRAINT `recipe_card_customer_id_9b2d3aeb_fk_recipe_customer_reg_id` FOREIGN KEY (`customer_id`) REFERENCES `recipe_customer_reg` (`id`);

--
-- Constraints for table `recipe_subcategory`
--
ALTER TABLE `recipe_subcategory`
  ADD CONSTRAINT `recipe_subcategory_category_id_61721bca_fk_recipe_category_id` FOREIGN KEY (`category_id`) REFERENCES `recipe_category` (`id`);

--
-- Constraints for table `recipe_tbl_ingrediantcalc`
--
ALTER TABLE `recipe_tbl_ingrediantcalc`
  ADD CONSTRAINT `recipe_tbl_ingrediantcalc_item_id_8ababbef_fk_recipe_tbl_item_id` FOREIGN KEY (`item_id`) REFERENCES `recipe_tbl_item` (`id`);

--
-- Constraints for table `recipe_tbl_item`
--
ALTER TABLE `recipe_tbl_item`
  ADD CONSTRAINT `recipe_tbl_item_category_id_62b621ac_fk_recipe_category_id` FOREIGN KEY (`category_id`) REFERENCES `recipe_category` (`id`),
  ADD CONSTRAINT `recipe_tbl_item_subcategory_id_b0109bf4_fk_recipe_subcategory_id` FOREIGN KEY (`subcategory_id`) REFERENCES `recipe_subcategory` (`id`);

--
-- Constraints for table `recipe_tbl_product`
--
ALTER TABLE `recipe_tbl_product`
  ADD CONSTRAINT `recipe_tbl_product_customer_id_081e1c64_fk_recipe_cu` FOREIGN KEY (`customer_id`) REFERENCES `recipe_customer_reg` (`id`);

--
-- Constraints for table `recipe_tbl_recipes`
--
ALTER TABLE `recipe_tbl_recipes`
  ADD CONSTRAINT `recipe_tbl_recipes_item_id_94f59ca1_fk_recipe_tbl_item_id` FOREIGN KEY (`item_id`) REFERENCES `recipe_tbl_item` (`id`);

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
