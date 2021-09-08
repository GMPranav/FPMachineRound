## Coding Assessment (Machine Round)

## By - Pranav G (2018AAPS0334H, BITS-Pilani)

## Pre-Requisites:

* mysql

* The following databases and tables are expected to be created before running the server:

	CREATE DATABASE users;
	CREATE TABLE users.users(name varchar(255),username varchar(255),passw varchar(255));
	CREATE TABLE users.json_file(User_Id int, Id int, Title varchar(511), Body varchar(1023));

* Flask module with mysql for python:

	pip install flask-mysql 

## Running the application: 

* Go to the download directory and run 'python3 main.py' in cmd

* Open another cmd window and open mysql

* Open http://localhost:5000/

## Video Demonstration:

Video Link : 
