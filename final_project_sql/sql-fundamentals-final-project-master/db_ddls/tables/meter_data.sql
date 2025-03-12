CREATE TABLE public.meter_data (
	meter_number varchar(250) NOT NULL,
	business_partner_id varchar(250) NOT NULL,
	connection_ean_code varchar(250) NOT NULL,
	brand public."brand_enum" NOT NULL,
	grid_company_code varchar(250) NOT NULL,
	oda_code varchar(250) NOT NULL,
	smart_collectable public."smart_collectable_enum" NOT NULL,
	division public."division_enum" NOT NULL,
	sjv1 float8 NULL,
	sjv2 float8 NULL,
	move_in_date timestamp NOT NULL,
	move_out_date timestamp NOT NULL,
	row_create_date timestamp NOT NULL,
	CONSTRAINT meter_data_connection_ean_code_key UNIQUE (connection_ean_code),
	CONSTRAINT meter_data_pkey PRIMARY KEY (meter_number)
);