DROP DATABASE IF EXISTS BeePlannerDB;
CREATE DATABASE BeePlannerDB;
USE BeePlannerDB;

CREATE TABLE User 
(
	user_id INT NOT NULL AUTO_INCREMENT,
	last_name NVARCHAR(25) NOT NULL,
	name NVARCHAR(20) NOT NULL,
	email NVARCHAR(30) NOT NULL,
	phone NVARCHAR(10) NOT NULL,
	password NVARCHAR(25) NOT NULL,
	PRIMARY KEY (user_id)

);



CREATE TABLE Activity
(
	activity_id INT NOT NULL AUTO_INCREMENT,
	name NVARCHAR(25) NOT NULL,
	priority INT NOT NULL,
	is_subject BOOLEAN NOT NULL,
	user_id INT NOT NULL REFERENCES User(user_id),
	PRIMARY KEY (activity_id)

);

CREATE TABLE Grade 
(
	grade_id INT NOT NULL AUTO_INCREMENT,
	name NVARCHAR(25) NOT NULL,
	consideration DECIMAL(2,2) NOT NULL,
	activity_id INT NOT NULL REFERENCES Activity(activity_id),
	PRIMARY KEY (grade_id)

);


CREATE TABLE Task
(
	task_id INT NOT NULL AUTO_INCREMENT,
	name NVARCHAR(20) NOT NULL,
	description NVARCHAR(30) NOT NULL,
	progress INT NOT NULL,	
	due_date DATE NOT NULL,
	create_date DATE NOT NULL,
	modified_date DATE NOT NULL,
	activity_id INT NOT NULL REFERENCES Activity(activity_id),
	PRIMARY KEY (task_id)

);


CREATE TABLE ListTask
(
	task_id INT NOT NULL REFERENCES Task(task_id),
	list_item NVARCHAR(20) NOT NULL,
	PRIMARY KEY (task_id, list_item)
);

CREATE TABLE ListGrade
(
	grade_id INT NOT NULL REFERENCES Grade(grade_id),
	name NVARCHAR(25) NOT NULL,
	grade DECIMAL(2,2) NOT NULL,
	PRIMARY KEY(grade_id, name, grade)

);

CREATE TABLE Schedule
(
	activity_id INT NOT NULL REFERENCES Activity(activity_id),
	time_init TIME NOT NULL,
    time_finish TIME NOT NULL,
	day NVARCHAR(10) NOT NULL,
	PRIMARY KEY(activity_day, activity_time)

);

CREATE TABLE Reminder
(
	reminder_id INT NOT NULL AUTO_INCREMENT,
	name NVARCHAR(25) NOT NULL,
	description NVARCHAR(25) NOT NULL,
	reminder_date DATETIME NOT NULL,
	activity_id INT NOT NULL REFERENCES Activity(activity_id),
	PRIMARY KEY (reminder_id)

);

CREATE TABLE Note
(
	note_id INT NOT NULL AUTO_INCREMENT,
	name NVARCHAR(25) NOT NULL,
	description NVARCHAR(30) NOT NULL,	
	note_date DATE NOT NULL,
	create_date DATETIME NOT NULL,
	modified_date DATETIME NOT NULL,
	activity_id INT NOT NULL REFERENCES Activity(activity_id),
	PRIMARY KEY(note_id)

);
