Project Title: Tournament Results

Project Purpose: To complete the second project requirements for the Full Stack Web Developer Nanodegree as laid out by Udacity.

Project Description: This project creates a postgresql database entitled tournament with accompanying tables and views.  The 
purpose of this database is to keep track of a tournament where there is an even number of players who play in a Swiss style
tournament where the outcomes are either win or lose.  The accompanying python scripts are meant to create queries, add entries,
and delete tables to simulate and test the progression of this tournament.

Project Instructions: This project was originally created to be run on a virtual linux machine using VirtualBox while interaction
between the host machine and virtual machine occurred with Vagrant.  Below are the steps to set everything up:

1. You will complete this project within the Vagrant virtual machine we've provided and configured for you. If you would like to 
review that before moving on refer to the course materials (https://www.udacity.com/wiki/ud197/install-vagrant) for help with 
installing Vagrant and Virtual Box, and previously recorded office hours (https://www.youtube.com/watch?v=djnqoEO2rLc) 
where we'll show you how to use Vagrant.
2. Next clone the fullstack-nanodegree-vm repository (https://github.com/udacity/fullstack-nanodegree-vm) to your local machine. 
3. Now, lets explore the starter code for this project provided within the VM: cd into /vagrant/tournament where you will see 
there are 3 files you have to work with on this project:
	tournament.sql is where you will put the database schema, in the form of SQL create table commands
	tournament.py is where you will put the code for your tournament module.
	tournament_test.py contains test functions that will test the functions you’ve written in intournament.py
4. To run the Vagrant VM, in the terminal use the command vagrant up followed by vagrant ssh.  Remember, once you have executed 
the vagrant ssh command, you will want to execute cd /vagrant to change directory to the sync folders.
5. The Vagrant VM provided in the fullstack repo already has PostgreSQL server installed, as well as the psql command line interface (CLI).
6. The very first time we start working on this project, no database will exist - so first, we'll need to create the SQL database for our 
tournament project. We can do this using psql or in tournament.sql.
7. tournament.sql is where we'll create our database schema and views; we also have the option of creating the database and tables in this file.
8. With the  psql command line interface (cli), you can run any SQL statement using the tables in the connected database. Make sure to 
end SQL statements with a semicolon, which is not always required from Python.
9. To build and access the database we run psql followed by \i tournament.sql
10. Once you have your .sql and .py files set up, it’s a good idea to test them out against the testing file provided to you (tournament_test.py). 
To run the series of tests defined in this test suite, run the program from the command line >> python tournament_test.

Project Connections: tournament_test.py references tournament.py

Project Contents:
tournament.py
Description: This python script creates queries, adds entries, and deletes tables from the tournament database.

tournament_test.py
Description: This python script tests the accuracy of the tournament.py script.

tournament.sql
Description: This sql file creates the tournament database along with accompanying tables and views.
