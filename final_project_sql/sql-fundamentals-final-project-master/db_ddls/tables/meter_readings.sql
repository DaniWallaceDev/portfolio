CREATE TABLE meter_readings (
	meter_readings_id int GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
	meter_number varchar(250) NULL,
	account_id varchar(250) NOT NULL,
	connection_ean_code varchar(250) NOT NULL,
	energy_type public."energy_type_enum" NOT NULL,
	validation_status public."validation_status_enum" NOT NULL,
	reading_date date NOT NULL,
	reading_electricity json NULL,
	reading_gas json NULL,
	rejection json NULL,
	brand varchar(250) NOT NULL
);