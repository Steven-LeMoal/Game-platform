Drop database if exists `dbSQL`;
Create database if not exists `dbSQL`;
Use `dbSQL`;

DROP TABLE IF EXISTS Users;
CREATE TABLE IF NOT EXISTS Users (
  userId int AUTO_INCREMENT NOT NULL,
  username varchar(20) NOT NULL,
  user_password varchar(20) NOT NULL,
  py_path varchar(150) NOT NULL,
  user_type ENUM('admin','normal') Not NULL,
  PRIMARY KEY (userId)
);

DROP TABLE IF EXISTS Games;
CREATE TABLE IF NOT EXISTS Games (
  gameId int AUTO_INCREMENT NOT NULL,
  game_name varchar(20) NOT NULL,
  game_path varchar(150) NOT NULL,
  PRIMARY KEY (gameId)
);

INSERT INTO `dbSQL`.`Users` (`username`,`user_password`,`user_type`,`py_path`) VALUES ('admin','admin','admin','C:\Users\steve\AppData\Local\Microsoft\WindowsApps\PythonSoftwareFoundation.Python.3.8_qbz5n2kfra8p0\python.exe');