create table bank_accounts
(
	id varchar(36) primary key,
	full_name varchar(60),
	birthdate date,
	account_number  text COLLATE "C" NOT NULL,
	user_password char(32),
	user_cash numeric(10,2)
)