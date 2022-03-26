--------------------------------------------------------------
-- Continent Table
-- DROP TABLE wsl.continents;
CREATE TABLE wsl.continents
(
	ID			INT unsigned NOT NULL AUTO_INCREMENT,
    continent	VARCHAR(20) NOT NULL,
    PRIMARY KEY (ID)
);

-- delete from wsl.continents where id = ;

-- select * from wsl.continents;

/*
INSERT INTO	wsl.continents (continent) VALUES
	('Africa'),
    ('Asia'),
    ('Europe'),
    ('North America'),
    ('Oceania'),
    ('South America');
*/

-----------------------------------------------------------
-- Countries Table
-- DROP TABLE wsl.countries;
CREATE TABLE wsl.countries
(
	ID				INT unsigned NOT NULL AUTO_INCREMENT,
    country			VARCHAR(50) NOT NULL,
	continent_id	INT unsigned NOT NULL,
    PRIMARY KEY (ID)
);

/*
INSERT INTO wsl.countries (country, continent_id) VALUES
	('South Africa', 1);
*/

-- delete from wsl.countries where id = ;

-- select * from wsl.countries;

-------------------------------------------------------------
-- Region Table
-- DROP TABLE wsl.regions;
CREATE TABLE wsl.regions
(
	ID INT unsigned NOT NULL AUTO_INCREMENT,
    region			VARCHAR(50) NOT NULL,
    country_id		INT unsigned NOT NULL,
    PRIMARY KEY		(ID)
);

/*
INSERT INTO wsl.regions (region, country_id) VALUES
	('Eastern Cape', 5);
*/

-- delete from wsl.regions where id =  ;

-- select * from wsl.regions;

-------------------------------------------------------------
-- City Table
-- DROP TABLE wsl.cities;
CREATE TABLE wsl.cities
(
	ID INT unsigned NOT NULL AUTO_INCREMENT,
    city			VARCHAR(50) NOT NULL,
    region_id		INT unsigned NOT NULL,
    PRIMARY KEY		(ID)
);

/*
INSERT INTO wsl.cities (city, region_id) VALUES
	('Eastern Cape', 5);
*/

-- delete from wsl.cities where id =  ;

-- select * from wsl.cities;

-------------------------------------------------------------
-- City Table
-- DROP TABLE wsl.breaks;
CREATE TABLE wsl.breaks
(
	ID 				INT unsigned NOT NULL AUTO_INCREMENT,
    break			VARCHAR(50) NOT NULL,
    region_id		INT unsigned NOT NULL,
    break_type		VARCHAR(50),
    reliability		VARCHAR(50),
    ability			VARCHAR(20),
    shoulder_burn	VARCHAR(20),
    clean_waves		INT unsigned,
    blown_waves		INT unsigned,
    small_waves		INT unsigned,
    PRIMARY KEY		(ID)
);

/*
INSERT INTO wsl.breaks (break, region_id, break_type,
						reliability, ability, shoulder_burn,
                        clean_waves, blown_waves, small_waves) VALUES
	();
*/

-- delete from wsl.breaks where id =  ;

-- select * from wsl.breaks;

----------------------------------------------------------------------------
-- Surfer Bio TABLE
-- DROP TABLE wsl.surfers
CREATE TABLE wsl.surfers
(
	ID						INT unsigned NOT NULL AUTO_INCREMENT,
	gender				VARCHAR(5),
	first_name		VARCHAR(50) NOT NULL,
	last_name			VARCHAR(50) NOT NULL,
	stance				VARCHAR(7),
	country_id		INT,
	birthday			VARCHAR(32),
	height				INT,
	weight				INT,
	first_season	CHAR(4),
	first_tour		VARCHAR(32)
	home_city_id	INT,
	PRIMARY KEY   (ID)
);

----------------------------------------------------------------------------
-- Tour Type TABLE
-- drop table wsl.tour_type;
CREATE TABLE wsl.tour_type
(
	ID					INT unsigned NOT NULL AUTO_INCREMENT,
	gender			VARCHAR(6),
	year				CHAR(4) NOT NULL,
	tour_type		VARCHAR(50) NOT NULL,
    tour_name		VARCHAR(50) NOT NULL,
	Primary Key (ID)
);

----------------------------------------------------------------------------
-- Event TABLE
-- DROP TABLE wsl.events
CREATE TABLE wsl.events
(
	ID						INT unsigned NOT NULL AUTO_INCREMENT,
	tour_type_id	INT NOT NULL,
	event_name		VARCHAR(50),
	stop_num			INT,
	open_date			VARCHAR(32),
	close_date		VARCHAR(32),
	break_id			INT,
	Primary KEY		(ID)
);


----------------------------------------------------------------------------

select * from wsl.continents;
select * from wsl.countries;
select * from wsl.regions;
select * from wsl.cities;
select * from wsl.breaks;
select * from wsl.surfers;
select * from wsl.tour_type;
select * from wsl.events;
