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

select * from wsl.continents;
select * from wsl.countries;
select * from wsl.regions;
select * from wsl.cities;
select * from wsl.breaks;