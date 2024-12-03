-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 03-12-2024 a las 11:02:52
-- Versión del servidor: 10.4.32-MariaDB
-- Versión de PHP: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `concedb`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_group`
--

CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL,
  `name` varchar(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `auth_group`
--

INSERT INTO `auth_group` (`id`, `name`) VALUES
(1, 'Clientes'),
(2, 'Empleados');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_group_permissions`
--

CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `auth_group_permissions`
--

INSERT INTO `auth_group_permissions` (`id`, `group_id`, `permission_id`) VALUES
(1, 1, 1),
(2, 1, 2),
(3, 1, 3),
(4, 1, 4),
(5, 1, 13),
(6, 1, 14),
(7, 1, 15),
(8, 1, 16),
(9, 1, 21),
(10, 1, 22),
(11, 1, 23),
(12, 1, 24),
(13, 1, 29),
(14, 1, 30),
(15, 1, 31),
(16, 1, 32),
(17, 1, 33),
(18, 1, 34),
(19, 1, 35),
(20, 1, 36),
(21, 2, 1),
(22, 2, 2),
(23, 2, 3),
(24, 2, 4),
(25, 2, 13),
(26, 2, 14),
(27, 2, 15),
(28, 2, 16),
(29, 2, 25),
(30, 2, 26),
(31, 2, 27),
(32, 2, 28),
(33, 2, 29),
(34, 2, 30),
(35, 2, 31),
(36, 2, 32),
(37, 2, 33),
(38, 2, 34),
(39, 2, 35),
(40, 2, 36);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_permission`
--

CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `auth_permission`
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
(25, 'Can add empleado', 7, 'add_empleado'),
(26, 'Can change empleado', 7, 'change_empleado'),
(27, 'Can delete empleado', 7, 'delete_empleado'),
(28, 'Can view empleado', 7, 'view_empleado'),
(29, 'Can add cliente', 8, 'add_cliente'),
(30, 'Can change cliente', 8, 'change_cliente'),
(31, 'Can delete cliente', 8, 'delete_cliente'),
(32, 'Can view cliente', 8, 'view_cliente'),
(33, 'Can add vehiculo', 9, 'add_vehiculo'),
(34, 'Can change vehiculo', 9, 'change_vehiculo'),
(35, 'Can delete vehiculo', 9, 'delete_vehiculo'),
(36, 'Can view vehiculo', 9, 'view_vehiculo'),
(37, 'Can add boleta', 10, 'add_boleta'),
(38, 'Can change boleta', 10, 'change_boleta'),
(39, 'Can delete boleta', 10, 'delete_boleta'),
(40, 'Can view boleta', 10, 'view_boleta');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_user`
--

CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `auth_user`
--

INSERT INTO `auth_user` (`id`, `password`, `last_login`, `is_superuser`, `username`, `first_name`, `last_name`, `email`, `is_staff`, `is_active`, `date_joined`) VALUES
(1, 'pbkdf2_sha256$216000$lG5ApW9BDgio$5IyD5VLYnC6DwNPeI88WV7HcY5bCWOITznQ+bev6S8c=', NULL, 0, '12', '', '', '', 0, 1, '2024-12-03 09:31:01.000000'),
(3, 'pbkdf2_sha256$216000$t8hd0yfyIeQc$NwLRn/TZC10d1J8PRmrDrMnvs23cNTvmQRq271WTvZU=', '2024-12-03 09:35:47.000000', 0, '34', '', '', '', 0, 1, '2024-12-03 09:33:01.000000'),
(4, 'pbkdf2_sha256$216000$qQ06FHputIfz$I9AbVzotZbSfpY6tNB4W/yxGdq3/QHqs9kvedJM/fR8=', '2024-12-03 09:49:56.000000', 1, 'qwe', '', '', 'qwe@gmail.com', 1, 1, '2024-12-03 09:34:04.000000'),
(5, 'pbkdf2_sha256$216000$yfyGZG6tbGf5$YMoAADLRGppltyBE4zGT/pW8lDRfmAX3fKefBwdb3+I=', '2024-12-03 09:50:49.000000', 0, '55', '', '', '', 0, 1, '2024-12-03 09:48:11.000000'),
(6, 'pbkdf2_sha256$216000$s1TGYTHJquTw$yHlzxAGOXU7KPG6CEDACoQJjfDVTOlZeJ3tqU9nK8Zo=', '2024-12-03 09:57:05.000000', 0, '66', '', '', '', 0, 1, '2024-12-03 09:56:59.000000');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_user_groups`
--

CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `auth_user_groups`
--

INSERT INTO `auth_user_groups` (`id`, `user_id`, `group_id`) VALUES
(1, 3, 1),
(2, 5, 2),
(3, 6, 1);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_user_user_permissions`
--

CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `boleta`
--

CREATE TABLE `boleta` (
  `folio` int(10) UNSIGNED NOT NULL,
  `monto` int(10) UNSIGNED NOT NULL,
  `direccion` varchar(50) NOT NULL,
  `fecha` datetime(6) NOT NULL,
  `fono` int(10) UNSIGNED NOT NULL,
  `FonoCliente_id` int(10) UNSIGNED NOT NULL,
  `FonoEmpleado_id` int(10) UNSIGNED NOT NULL,
  `vendedor_id` int(10) UNSIGNED NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `cliente`
--

CREATE TABLE `cliente` (
  `rut` int(10) UNSIGNED NOT NULL,
  `nombre` varchar(50) NOT NULL,
  `apellido` varchar(50) NOT NULL,
  `direccion` varchar(50) NOT NULL,
  `FonoCliente` int(10) UNSIGNED NOT NULL,
  `gmail` varchar(50) NOT NULL,
  `password_cliente` varchar(50) NOT NULL,
  `FechaNacimiento` date NOT NULL,
  `user_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `cliente`
--

INSERT INTO `cliente` (`rut`, `nombre`, `apellido`, `direccion`, `FonoCliente`, `gmail`, `password_cliente`, `FechaNacimiento`, `user_id`) VALUES
(34, '34', '34', '34', 34, '34@gmail.com', '', '3333-03-31', 3),
(66, '66', '66', '66', 66, '66@gmail.com', '', '6666-06-06', 6);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `django_admin_log`
--

CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext DEFAULT NULL,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) UNSIGNED NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `django_admin_log`
--

INSERT INTO `django_admin_log` (`id`, `action_time`, `object_id`, `object_repr`, `action_flag`, `change_message`, `content_type_id`, `user_id`) VALUES
(1, '2024-12-03 09:35:21.000000', '1', 'Clientes', 2, '[{\"changed\": {\"fields\": [\"Permissions\"]}}]', 3, 4),
(2, '2024-12-03 09:50:39.000000', '2', 'Empleados', 2, '[{\"changed\": {\"fields\": [\"Permissions\"]}}]', 3, 4);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `django_content_type`
--

CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(1, 'admin', 'logentry'),
(3, 'auth', 'group'),
(2, 'auth', 'permission'),
(4, 'auth', 'user'),
(10, 'boleta', 'boleta'),
(8, 'cliente', 'cliente'),
(5, 'contenttypes', 'contenttype'),
(7, 'empleado', 'empleado'),
(6, 'sessions', 'session'),
(9, 'vehiculo', 'vehiculo');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `django_migrations`
--

CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2024-12-03 09:30:29.000000'),
(2, 'auth', '0001_initial', '2024-12-03 09:30:29.000000'),
(3, 'admin', '0001_initial', '2024-12-03 09:30:30.000000'),
(4, 'admin', '0002_logentry_remove_auto_add', '2024-12-03 09:30:30.000000'),
(5, 'admin', '0003_logentry_add_action_flag_choices', '2024-12-03 09:30:30.000000'),
(6, 'contenttypes', '0002_remove_content_type_name', '2024-12-03 09:30:30.000000'),
(7, 'auth', '0002_alter_permission_name_max_length', '2024-12-03 09:30:31.000000'),
(8, 'auth', '0003_alter_user_email_max_length', '2024-12-03 09:30:31.000000'),
(9, 'auth', '0004_alter_user_username_opts', '2024-12-03 09:30:31.000000'),
(10, 'auth', '0005_alter_user_last_login_null', '2024-12-03 09:30:31.000000'),
(11, 'auth', '0006_require_contenttypes_0002', '2024-12-03 09:30:31.000000'),
(12, 'auth', '0007_alter_validators_add_error_messages', '2024-12-03 09:30:31.000000'),
(13, 'auth', '0008_alter_user_username_max_length', '2024-12-03 09:30:31.000000'),
(14, 'auth', '0009_alter_user_last_name_max_length', '2024-12-03 09:30:31.000000'),
(15, 'auth', '0010_alter_group_name_max_length', '2024-12-03 09:30:31.000000'),
(16, 'auth', '0011_update_proxy_permissions', '2024-12-03 09:30:31.000000'),
(17, 'auth', '0012_alter_user_first_name_max_length', '2024-12-03 09:30:31.000000'),
(18, 'empleado', '0001_initial', '2024-12-03 09:30:31.000000'),
(19, 'cliente', '0001_initial', '2024-12-03 09:30:31.000000'),
(20, 'boleta', '0001_initial', '2024-12-03 09:30:31.000000'),
(21, 'sessions', '0001_initial', '2024-12-03 09:30:31.000000'),
(22, 'vehiculo', '0001_initial', '2024-12-03 09:30:31.000000'),
(23, 'cliente', '0002_cliente_user', '2024-12-03 09:32:02.000000'),
(24, 'vehiculo', '0002_auto_20241203_0330', '2024-12-03 09:32:02.000000'),
(25, 'empleado', '0002_empleado_user', '2024-12-03 09:47:10.000000');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `django_session`
--

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('zw2iqsabx5qq2gbktxk7d63fpvrsih1e', '.eJxVjEEOwiAQRe_C2hAGLAWX7nsGMsyAVA0kpV0Z765NutDtf-_9lwi4rSVsPS1hZnERVpx-t4j0SHUHfMd6a5JaXZc5yl2RB-1yapye18P9OyjYy7f2YI0ZvXaGszWeckZNAMnRMGSvdFaagSLjGf0QDcWRyKCLGTwDKxDvD-KkOFw:1tIPeT:JkTUuEgcMbuHyZorYA5hxfGDHKPBNJpvFw0gh9GCGlg', '2024-12-17 09:57:05.000000');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `empleado`
--

CREATE TABLE `empleado` (
  `rut` int(10) UNSIGNED NOT NULL,
  `nombre` varchar(50) NOT NULL,
  `apellido` varchar(50) NOT NULL,
  `direccion` varchar(50) NOT NULL,
  `FonoEmpleado` int(10) UNSIGNED NOT NULL,
  `gmail` varchar(50) NOT NULL,
  `area` varchar(50) NOT NULL,
  `contraseña` varchar(16) NOT NULL,
  `FechaNacimiento` date NOT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `empleado`
--

INSERT INTO `empleado` (`rut`, `nombre`, `apellido`, `direccion`, `FonoEmpleado`, `gmail`, `area`, `contraseña`, `FechaNacimiento`, `user_id`) VALUES
(55, '123', '55', '55', 55, '55@gmail.com', '55', '', '5555-05-05', 5);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `vehiculo`
--

CREATE TABLE `vehiculo` (
  `id` int(11) NOT NULL,
  `descripcion` varchar(255) NOT NULL,
  `marca` varchar(50) NOT NULL,
  `modelo` varchar(50) NOT NULL,
  `año` int(10) UNSIGNED NOT NULL,
  `precio` int(10) UNSIGNED NOT NULL,
  `propietario_id` int(10) UNSIGNED NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `auth_group`
--
ALTER TABLE `auth_group`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Indices de la tabla `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  ADD KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`);

--
-- Indices de la tabla `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`);

--
-- Indices de la tabla `auth_user`
--
ALTER TABLE `auth_user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- Indices de la tabla `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  ADD KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`);

--
-- Indices de la tabla `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  ADD KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`);

--
-- Indices de la tabla `boleta`
--
ALTER TABLE `boleta`
  ADD PRIMARY KEY (`folio`),
  ADD KEY `Boleta_FonoCliente_id_7909d925_fk_Cliente_rut` (`FonoCliente_id`),
  ADD KEY `Boleta_FonoEmpleado_id_7cf1b485_fk_Empleado_rut` (`FonoEmpleado_id`),
  ADD KEY `Boleta_vendedor_id_da9879a6_fk_Empleado_rut` (`vendedor_id`);

--
-- Indices de la tabla `cliente`
--
ALTER TABLE `cliente`
  ADD PRIMARY KEY (`rut`),
  ADD KEY `Cliente_user_id_8cdcf929_fk_auth_user_id` (`user_id`);

--
-- Indices de la tabla `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD PRIMARY KEY (`id`),
  ADD KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  ADD KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`);

--
-- Indices de la tabla `django_content_type`
--
ALTER TABLE `django_content_type`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`);

--
-- Indices de la tabla `django_migrations`
--
ALTER TABLE `django_migrations`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `django_session`
--
ALTER TABLE `django_session`
  ADD PRIMARY KEY (`session_key`),
  ADD KEY `django_session_expire_date_a5c62663` (`expire_date`);

--
-- Indices de la tabla `empleado`
--
ALTER TABLE `empleado`
  ADD PRIMARY KEY (`rut`),
  ADD UNIQUE KEY `user_id` (`user_id`);

--
-- Indices de la tabla `vehiculo`
--
ALTER TABLE `vehiculo`
  ADD PRIMARY KEY (`id`),
  ADD KEY `Vehiculo_propietario_id_395a1834_fk_Cliente_rut` (`propietario_id`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `auth_group`
--
ALTER TABLE `auth_group`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT de la tabla `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=41;

--
-- AUTO_INCREMENT de la tabla `auth_permission`
--
ALTER TABLE `auth_permission`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=41;

--
-- AUTO_INCREMENT de la tabla `auth_user`
--
ALTER TABLE `auth_user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT de la tabla `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT de la tabla `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `django_admin_log`
--
ALTER TABLE `django_admin_log`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT de la tabla `django_content_type`
--
ALTER TABLE `django_content_type`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT de la tabla `django_migrations`
--
ALTER TABLE `django_migrations`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=26;

--
-- AUTO_INCREMENT de la tabla `vehiculo`
--
ALTER TABLE `vehiculo`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- Filtros para la tabla `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- Filtros para la tabla `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  ADD CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Filtros para la tabla `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Filtros para la tabla `boleta`
--
ALTER TABLE `boleta`
  ADD CONSTRAINT `Boleta_FonoCliente_id_7909d925_fk_Cliente_rut` FOREIGN KEY (`FonoCliente_id`) REFERENCES `cliente` (`rut`),
  ADD CONSTRAINT `Boleta_FonoEmpleado_id_7cf1b485_fk_Empleado_rut` FOREIGN KEY (`FonoEmpleado_id`) REFERENCES `empleado` (`rut`),
  ADD CONSTRAINT `Boleta_vendedor_id_da9879a6_fk_Empleado_rut` FOREIGN KEY (`vendedor_id`) REFERENCES `empleado` (`rut`);

--
-- Filtros para la tabla `cliente`
--
ALTER TABLE `cliente`
  ADD CONSTRAINT `Cliente_user_id_8cdcf929_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Filtros para la tabla `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  ADD CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Filtros para la tabla `empleado`
--
ALTER TABLE `empleado`
  ADD CONSTRAINT `Empleado_user_id_6f1e7e22_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Filtros para la tabla `vehiculo`
--
ALTER TABLE `vehiculo`
  ADD CONSTRAINT `Vehiculo_propietario_id_395a1834_fk_Cliente_rut` FOREIGN KEY (`propietario_id`) REFERENCES `cliente` (`rut`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
