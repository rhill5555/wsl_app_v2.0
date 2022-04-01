-- Continent Table
-- DROP TABLE wsl.continent;
CREATE TABLE wsl.continent
(
  continent_id    INT unsigned NOT NULL AUTO_INCREMENT,
  continent       VARCHAR(20)  NOT NULL,
  Primary Key     (continent_id)
);

-- insert continents since there are only a few
/*
INSERT INTO wsl.continent (continent) VALUES
('Africa'),
('Asia'),
('Europe'),
('North America'),
('Oceania'),
('South America');
*/

-----------------------------------------------------------
-- Country TABLE
-- DROP TABLE wsl.country;
CREATE TABLE wsl.country
(
  country_id      INT unsigned NOT NULL AUTO_INCREMENT,
  country         VARCHAR(50) NOT NULL,
  continent_id    INT NOT NULL,
  Primary Key     (country_id)
);

--------------------------------------------------------------
-- Region TABLE
-- DROP TABLE wsl.region;
CREATE table wsl.region
(
  region_id     INT unsigned NOT NULL AUTO_INCREMENT,
  region        VARCHAR(50) NOT NULL,
  country_id    INT NOT NULL,
  Primary Key   (region_id)
);

--------------------------------------------------------------
-- city TABLE
-- DROP TABLE wsl.city;
CREATE TABLE wsl.city
(
  city_id       INT unsigned NOT NULL AUTO_INCREMENT,
  city          VARCHAR(50) NOT NULL,
  region_id     INT NOT NULL,
  Primary Key   (city_id)
);

--------------------------------------------------------------
-- break table
-- DROP TABLE wsl.break;
CREATE TABLE wsl.break
(
  break_id      INT unsigned NOT NULL AUTO_INCREMENT,
  break         VARCHAR(50) NOT NULL,
  region_id     INT NOT NULL,
  break_type    VARCHAR(32),
  reliability   VARCHAR(32),
  ability       VARCHAR(32),
  shoulder_burn VARCHAR(32),
  clean         FLOAT,
  blown_out     FLOAT,
  too_small     FLOAT,
  Primary Key   (break_id)
);

---------------------------------------------------------------

select * from wsl.continent;
select * from wsl.country;
select * from wsl.region;
select * from wsl.city;
select * from wsl.break;

----------------------------------------------------------------
-- Surfer TABLE
-- DROP TABLE wsl.surfer;
CREATE TABLE wsl.surfers
(
  surfer_id       INT unsigned NOT NULL AUTO_INCREMENT,
  gender          VARCHAR(6) NOT NULL,
  first_name      VARCHAR(50) NOT NULL,
  last_name       VARCHAR(50) NOT NULL,
  stance          VARCHAR(10),
  rep_country_id  INT NOT NULL,
  birthday        DATE,
  height          INT,
  weight          INT,
  home_city_id    INT,
  Primary Key     (surfer_id)
);

----------------------------------------------------------------

select * from wsl.surfers;

----------------------------------------------------------------
-- tour TABLE
-- DROP TABLE wsl.tour;
CREATE TABLE wsl.tour
(
  tour_id       INT unsgined NOT NULL AUTO_INCREMENT,
  year          YEAR,
  gender        VARCHAR(6),
  tour_type     VARCHAR(50) NOT NULL,
  tour_name     VARCHAR(50) NOT NULL,
  Primary Key   (tour_id)
);

-----------------------------------------------------------------
-- event table
-- DROP TABLE wsl.event;
CREATE TABLE wsl.event
(
  event_id        INT unsigned NOT NULL AUTO_INCREMENT,
  event_name      VARCHAR(50) NOT NULL,
  tour_id         INT NOT NULL,
  stop_nbr        INT,
  break_id        INT NOT NULL,
  open_date       DATE,
  close_date      DATE,
  Primary Key     (event_id)
);

----------------------------------------------------------------
-- round TABLE
-- DROP TABLE wsl.round;
CREATE TABLE wsl.round
(
  round_id        INT unsigned NOT NULL AUTO_INCREMENT,
  round           VARCHAR(32) NOT NULL,
  Primary Key     (round_id)
);

-----------------------------------------------------------------
-- event by round TABLE
-- DROP TABLE wsl.event_round;
CREATE TABLE wsl.event_round
(
  event_round_id      INT unsigned NOT NULL AUTO_INCREMENT,
  round_id            INT NOT NULL,
  event_id            INT NOT NULL,
  Primary Key         (event_round_id)
);

-----------------------------------------------------------------
-- heat details TABLE
-- DROP TABLE wsl.heat_details;
CREATE TABLE wsl.heat_details
(
  heat_id         INT unsigned NOT NULL AUTO_INCREMENT,
  heat_nbr        VARCHAR(10) NOT NULL,
  event_round_id  INT NOT NULL,
  wind            VARCHAR(32),
  heat_date       DATE,
  duration        INT,
  wave_min        INT,
  wave_max        INT,
  Primary Key     (heat_id)
);

----------------------------------------------------------------
-- heat by surfer TABLE
-- DROP TABLE wsl.heat_surfers;
CREATE TABLE wsl.heat_surfers
(
  surfer_heat_id        INT unsigned NOT NULL AUTO_INCREMENT,
  heat_id               INT NOT NULL,
  surfer_id             INT NOT NULL,
  Primary Key           (surfer_heat_id)
);

----------------------------------------------------------------
-- heat results TABLE
-- DROP TABLE wsl.heat_results;
CREATE TABLE wsl.heat_results
(
  heat_result_id        INT unsigned NOT NULL AUTO_INCREMENT,
  heat_id               INT NOT NULL,
  surfer_in_heat_id     INT NOT NULL,
  pick_to_win_percent   FLOAT,
  jersey_color          VARCHAR(32),
  status                VARCHAR(12),
  wave_1                FLOAT,
  wave_2                FLOAT,
  wave_3                FLOAT,
  wave_4                FLOAT,
  wave_5                FLOAT,
  wave_6                FLOAT,
  wave_7                FLOAT,
  wave_8                FLOAT,
  wave_9                FLOAT,
  wave_10               FLOAT,
  wave_11               FLOAT,
  wave_12               FLOAT,
  wave_13               FLOAT,
  wave_14               FLOAT,
  wave_15               FLOAT,
  Primary Key           (heat_result_id)
);

-----------------------------------------------------------

select * from wsl.tour;
select * from wsl.event;
select * from wsl.round;
select * from wsl.event_round;
select * from wsl.heat_details;
select * from wsl.heat_surfers;
select * from wsl.heat_results;
