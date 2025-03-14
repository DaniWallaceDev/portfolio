CREATE TABLE mandate_data (
	mandate_id int PRIMARY KEY,
	business_partner_id varchar(250) NOT NULL,
	brand public."brand_enum" NOT NULL,
	mandate_status public."mandate_status_enum" NOT NULL,
	collection_frequency public."collection_frequency_status_enum" NOT NULL,
	row_update_datetime timestamp NOT NULL,
	row_create_datetime timestamp NOT NULL,
	changed_by public."changed_by_enum" NOT NULL,
	collection_type public."collection_type_enum" NOT NULL,
	metering_consent public."metering_consent_enum" NOT NULL
);