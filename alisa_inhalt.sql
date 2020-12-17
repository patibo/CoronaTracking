-- phpMyAdmin SQL Dump
-- version 4.9.3
-- https://www.phpmyadmin.net/
--
-- Host: localhost:8889
-- Erstellungszeit: 17. Dez 2020 um 07:14
-- Server-Version: 5.7.26
-- PHP-Version: 7.4.2

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";

--
-- Datenbank: `coronatracking`
--
CREATE DATABASE IF NOT EXISTS `coronatracking` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
USE `coronatracking`;

-- --------------------------------------------------------

--
-- Tabellenstruktur für Tabelle `eventsentry`
--

CREATE TABLE IF NOT EXISTS `eventsentry` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(70) NOT NULL,
  `datum` date NOT NULL,
  `zeit` time NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;

--
-- Daten für Tabelle `eventsentry`
--

INSERT INTO `eventsentry` (`id`, `name`, `datum`, `zeit`) VALUES(1, 'Love', '2020-12-14', '16:10:00');
INSERT INTO `eventsentry` (`id`, `name`, `datum`, `zeit`) VALUES(2, 'Harry Potter', '2020-12-15', '10:00:00');
INSERT INTO `eventsentry` (`id`, `name`, `datum`, `zeit`) VALUES(3, 'Haus', '2020-12-08', '11:33:00');

-- --------------------------------------------------------

--
-- Tabellenstruktur für Tabelle `kunden`
--

CREATE TABLE IF NOT EXISTS `kunden` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `benutzername` varchar(16) NOT NULL,
  `passwort` varchar(32) NOT NULL,
  `vorname` varchar(20) NOT NULL,
  `nachname` varchar(20) NOT NULL,
  `email` varchar(50) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8;

--
-- Daten für Tabelle `kunden`
--

INSERT INTO `kunden` (`id`, `benutzername`, `passwort`, `vorname`, `nachname`, `email`) VALUES(1, 'alisarieger', 'QWxpUmllZ2VyMTk=', 'Alisa', 'Rieger', 'alisa6rieger@gmail.com');
INSERT INTO `kunden` (`id`, `benutzername`, `passwort`, `vorname`, `nachname`, `email`) VALUES(2, 'maxipaulitsch', 'QmF0dGVsZmllbGQx', 'Maxi', 'Paulitsch', 'maximilianpaulitsch2002@gmail.com');
INSERT INTO `kunden` (`id`, `benutzername`, `passwort`, `vorname`, `nachname`, `email`) VALUES(3, 'patrickibounig', 'UGF0cmljazEyMzQ=', 'Patrick', 'Ibounig', 'patrick.ibounig@gmx.net');
INSERT INTO `kunden` (`id`, `benutzername`, `passwort`, `vorname`, `nachname`, `email`) VALUES(4, 'ilirjanmarkaj', 'SWxpcmphbjEyMzQ=', 'Ilirjan', 'Markaj', 'ilirjan1998markaj1998@gmail.com');
INSERT INTO `kunden` (`id`, `benutzername`, `passwort`, `vorname`, `nachname`, `email`) VALUES(5, 'CASUAL', 'TXVzbGltXzk5', 'Muslim', 'Ibragimov', 'muslimdzhamaldinov@gmail.com');
INSERT INTO `kunden` (`id`, `benutzername`, `passwort`, `vorname`, `nachname`, `email`) VALUES(6, 'maxi', 'QmF0dGVsZmllbGQx', 'maxi', 'paulitsch', 'maximilian@gmail.com');

-- --------------------------------------------------------

--
-- Tabellenstruktur für Tabelle `kundenevents`
--

CREATE TABLE IF NOT EXISTS `kundenevents` (
  `kID` int(11) NOT NULL,
  `eID` int(11) NOT NULL,
  PRIMARY KEY (`kID`,`eID`),
  KEY `eID` (`eID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Daten für Tabelle `kundenevents`
--

INSERT INTO `kundenevents` (`kID`, `eID`) VALUES(1, 1);
INSERT INTO `kundenevents` (`kID`, `eID`) VALUES(2, 1);
INSERT INTO `kundenevents` (`kID`, `eID`) VALUES(6, 1);
INSERT INTO `kundenevents` (`kID`, `eID`) VALUES(1, 2);
INSERT INTO `kundenevents` (`kID`, `eID`) VALUES(3, 2);
INSERT INTO `kundenevents` (`kID`, `eID`) VALUES(4, 2);
INSERT INTO `kundenevents` (`kID`, `eID`) VALUES(6, 2);
INSERT INTO `kundenevents` (`kID`, `eID`) VALUES(1, 3);

--
-- Constraints der exportierten Tabellen
--

--
-- Constraints der Tabelle `kundenevents`
--
ALTER TABLE `kundenevents`
  ADD CONSTRAINT `kundenevents_ibfk_1` FOREIGN KEY (`kID`) REFERENCES `kunden` (`id`),
  ADD CONSTRAINT `kundenevents_ibfk_2` FOREIGN KEY (`eID`) REFERENCES `eventsentry` (`id`);
