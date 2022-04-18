-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema estate_db
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema estate_db
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `estate_db` DEFAULT CHARACTER SET utf8 ;
USE `estate_db` ;

-- -----------------------------------------------------
-- Table `estate_db`.`type`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `estate_db`.`type` (
  `idtype` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`idtype`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `estate_db`.`region`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `estate_db`.`region` (
  `idregion` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`idregion`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `estate_db`.`province`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `estate_db`.`province` (
  `idprovince` VARCHAR(100) NOT NULL,
  PRIMARY KEY (`idprovince`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `estate_db`.`zipcode`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `estate_db`.`zipcode` (
  `idzipcode` VARCHAR(5) NOT NULL,
  PRIMARY KEY (`idzipcode`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `estate_db`.`city`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `estate_db`.`city` (
  `idcity` VARCHAR(100) NOT NULL,
  PRIMARY KEY (`idcity`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `estate_db`.`coordinates`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `estate_db`.`coordinates` (
  `idcoordinates` INT NOT NULL AUTO_INCREMENT,
  `latitude` FLOAT NOT NULL,
  `longitude` FLOAT NOT NULL,
  `region_idregion` VARCHAR(45) NOT NULL,
  `province_idprovince` VARCHAR(100) NOT NULL,
  `zipcode_idzipcode` VARCHAR(5) NOT NULL,
  `city_idcity` VARCHAR(100) NOT NULL,
  PRIMARY KEY (`idcoordinates`),
  INDEX `fk_coordinates_region1_idx` (`region_idregion` ASC) VISIBLE,
  INDEX `fk_coordinates_province1_idx` (`province_idprovince` ASC) VISIBLE,
  INDEX `fk_coordinates_zipcode1_idx` (`zipcode_idzipcode` ASC) VISIBLE,
  INDEX `fk_coordinates_city1_idx` (`city_idcity` ASC) VISIBLE,
  CONSTRAINT `fk_coordinates_region1`
    FOREIGN KEY (`region_idregion`)
    REFERENCES `estate_db`.`region` (`idregion`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_coordinates_province1`
    FOREIGN KEY (`province_idprovince`)
    REFERENCES `estate_db`.`province` (`idprovince`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_coordinates_zipcode1`
    FOREIGN KEY (`zipcode_idzipcode`)
    REFERENCES `estate_db`.`zipcode` (`idzipcode`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_coordinates_city1`
    FOREIGN KEY (`city_idcity`)
    REFERENCES `estate_db`.`city` (`idcity`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `estate_db`.`feautures`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `estate_db`.`feautures` (
  `idFeautures` INT NOT NULL AUTO_INCREMENT,
  `id_vivienda` VARCHAR(45) NOT NULL,
  `date` DATE NOT NULL,
  `advertiser` VARCHAR(45) NULL,
  `descriptions` VARCHAR(45) NULL,
  `rooms` INT NOT NULL,
  `bathrooms` INT NOT NULL,
  `surface` INT NOT NULL,
  `energy_certificate` INT NOT NULL,
  `antiquity` INT NOT NULL,
  `floor` INT NOT NULL,
  `surfaceland` INT NOT NULL,
  `price` INT NOT NULL,
  `type_idtype` VARCHAR(45) NOT NULL,
  `coordinates_idcoordinates` INT NOT NULL,
  PRIMARY KEY (`idFeautures`),
  INDEX `fk_Feautures_type_idx` (`type_idtype` ASC) VISIBLE,
  INDEX `fk_Feautures_coordinates1_idx` (`coordinates_idcoordinates` ASC) VISIBLE,
  CONSTRAINT `fk_Feautures_type`
    FOREIGN KEY (`type_idtype`)
    REFERENCES `estate_db`.`type` (`idtype`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Feautures_coordinates1`
    FOREIGN KEY (`coordinates_idcoordinates`)
    REFERENCES `estate_db`.`coordinates` (`idcoordinates`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
