CREATE DATABASE IF NOT EXISTS coronatracking;
USE coronatracking;

CREATE TABLE IF NOT EXISTS kunden(`id` int(11) NOT NULL AUTO_INCREMENT,
								  `benutzername` varchar(16) NOT NULL,
                                  `passwort` varchar(32) NOT NULL,
                                  `vorname` varchar(20) NOT NULL,
                                  `nachname` varchar(20) NOT NULL,
                                  `email` varchar(50) NOT NULL,
                                  `geburtsdatum` date,
                                  `telefon` varchar(20),
                                  PRIMARY KEY(`id`));
                                  
CREATE TABLE IF NOT EXISTS eventsentry(`id` int(11) NOT NULL AUTO_INCREMENT,
									  `name` varchar(70) NOT NULL,
                                      `datum` date NOT NULL,
                                      `zeit` time NOT NULL,
                                      PRIMARY KEY(`id`));

CREATE TABLE IF NOT EXISTS kundenevents(`kID` int(11) NOT NULL,
										`eID` int(11) NOT NULL,
                                        `eventname` INT(11) NOT NULL,
                                        `datum` date NOT NULL,
                                        `zeit` time NOT NULL,
                                        PRIMARY KEY(kID, eID),
                                        FOREIGN KEY(`kID`) REFERENCES kunden(`id`),
                                        FOREIGN KEY(`eID`) REFERENCES eventsentry(`id`)); 
