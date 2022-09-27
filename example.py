# Code to show the databases list
show databases;

# Code to create new database
create database maatram;

# Code to use that database
use maatram;

# Code to show the tables list
show tables;  

# Code to create a table
create table students(roll_no int primary key auto_increment,
                      name varchar(50) not null,
                      dept varchar(20) not null,
                      age integer not null,
                      phonenumber varchar(10) unique
                      );
 
 # Code to insert a table
 insert into students values(1,'kowsi','EEE',19,9219113729),
                            (2,'Meena','BioMed',19,8358256789),
                            (3,'praba','EEE',20, 9901182812),
                            (4,'kamali','EEE',19, 9927328120),
                            (5,'Keerthi','MicroBiology',21,8237348992);
                            
 # Code to describe a table
 describe students;
 
 # Code to read a table
 select * from students;
 select name,dept from students;
 
 # Code to delete a table
 drop table students;
 
 # Code to update a table
 update students set age = 20 where roll_no=5;
 
 # Code to alter a table
 alter table students rename column dept to course;
 
 # Code to add column in a table
 alter table students ADD column joined_date date not null;
 
 # Code to modify column 
 alter table students modify column joined_date datetime not null default now();