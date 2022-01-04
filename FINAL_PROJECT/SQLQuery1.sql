create database currencies

use currencies
create table world_cur(
	S_no int NOT NULL IDENTITY PRIMARY KEY,
	Currencies_Name varchar,
	Date date,
	Price_USD float
	);


select * from world_cur;


ALTER TABLE world_cur
ADD Price_USD float;

insert into world_cur values('btc','05/20/2020',55200);

 exec sp_help world_cur;

 ALTER TABLE world_cur
ALTER COLUMN Currencies_Name varchar (50);

SELECT GETDATE();


DELETE FROM world_cur;
Delete from world_cur where S_no=230;
