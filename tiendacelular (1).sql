-- phpMyAdmin SQL Dump
-- version 4.5.1
-- http://www.phpmyadmin.net
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 23-05-2016 a las 07:45:11
-- Versión del servidor: 10.1.10-MariaDB
-- Versión de PHP: 5.6.15

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `tiendacelular`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `celular`
--

CREATE TABLE `celular` (
  `idprod` int(10) UNSIGNED NOT NULL,
  `ce_marca` varchar(15) COLLATE utf8_spanish_ci DEFAULT NULL,
  `ce_model` varchar(15) COLLATE utf8_spanish_ci DEFAULT NULL,
  `ce_desc` varchar(30) COLLATE utf8_spanish_ci DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

--
-- Volcado de datos para la tabla `celular`
--

INSERT INTO `celular` (`idprod`, `ce_marca`, `ce_model`, `ce_desc`) VALUES
(1, 'Apple', 'Iphone 7', 'apple iphone 7 standart black'),
(2, 'Samsung', 'Galaxy S3', 'SSG s3 Camara frontal doble si'),
(3, 'Sony', 'Xperia x11', 'xperia x11 camara 1000 mpx'),
(4, 'Blackberry', 'z10', 'blackberry z10 4gb ram'),
(5, 'Nokia', 'Lumia ', 'Lumia G750 4gb ');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `cliente`
--

CREATE TABLE `cliente` (
  `dni` int(10) UNSIGNED NOT NULL,
  `c_nomb` varchar(20) COLLATE utf8_spanish_ci DEFAULT NULL,
  `c_telf` varchar(10) COLLATE utf8_spanish_ci DEFAULT NULL,
  `c_dir` varchar(15) COLLATE utf8_spanish_ci DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

--
-- Volcado de datos para la tabla `cliente`
--

INSERT INTO `cliente` (`dni`, `c_nomb`, `c_telf`, `c_dir`) VALUES
(2, 'Teemo Nel Sanchez', '563857452', 'calle 24 av 2'),
(3, 'Diana Luna', ' 86749385', 'calle 3 cra 4'),
(4, 'Pablo Diaz perez', '3746389500', 'calle 8 cra 6'),
(5, 'Azir Mohamed', '63564732', 'clle 4 av 15'),
(6, 'Maria DataBase', '13579864', 'calle90 cra 14');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `compra`
--

CREATE TABLE `compra` (
  `c_dni` int(10) UNSIGNED NOT NULL,
  `ce_idprod` int(10) UNSIGNED NOT NULL,
  `f_compra` date DEFAULT NULL,
  `c_num` int(10) UNSIGNED DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

--
-- Volcado de datos para la tabla `compra`
--

INSERT INTO `compra` (`c_dni`, `ce_idprod`, `f_compra`, `c_num`) VALUES
(4, 3, '2015-07-04', 3216865015);

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `celular`
--
ALTER TABLE `celular`
  ADD PRIMARY KEY (`idprod`);

--
-- Indices de la tabla `cliente`
--
ALTER TABLE `cliente`
  ADD PRIMARY KEY (`dni`);

--
-- Indices de la tabla `compra`
--
ALTER TABLE `compra`
  ADD PRIMARY KEY (`c_dni`,`ce_idprod`),
  ADD KEY `Cliente_has_Celular_FKIndex1` (`c_dni`),
  ADD KEY `Cliente_has_Celular_FKIndex2` (`ce_idprod`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `celular`
--
ALTER TABLE `celular`
  MODIFY `idprod` int(10) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;
--
-- AUTO_INCREMENT de la tabla `cliente`
--
ALTER TABLE `cliente`
  MODIFY `dni` int(10) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;
--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `compra`
--
ALTER TABLE `compra`
  ADD CONSTRAINT `compra_ibfk_1` FOREIGN KEY (`c_dni`) REFERENCES `cliente` (`dni`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `compra_ibfk_2` FOREIGN KEY (`ce_idprod`) REFERENCES `celular` (`idprod`) ON DELETE CASCADE ON UPDATE CASCADE;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
