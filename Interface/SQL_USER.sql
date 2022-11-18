Drop database if exists `dbSQL`;
Create database if not exists `dbSQL`;
Use `dbSQL`;

DROP TABLE IF EXISTS Users;
CREATE TABLE IF NOT EXISTS Users (
  userId int AUTO_INCREMENT NOT NULL,
  username varchar(20) NOT NULL,
  user_password varchar(20) NOT NULL,
  user_type ENUM('admin','normal') Not NULL,
  PRIMARY KEY (userId)
);

INSERT INTO `dbSQL`.`Users` (`username`,`user_password`,`user_type`) VALUES ('admin','admin','admin');
INSERT INTO `dbSQL`.`Users` (`username`,`user_password`,`user_type`) VALUES ('tibo','tibo','normal');