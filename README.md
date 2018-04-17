# Log Analysis

This is a Python program to analyze a database and print out reports based on the data in the database. The pyscopg2 module is used.
Developed and tested with Python 2.7.12.

This is a command line program, that is, it should be run from a terminal or command prompt/cmd/PowerShell. Linux/Unix is recommended, though. It requires Python and Postgresql.

A database named "news" must be created. Then tables must be created and populated by using the file from this url: https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip

Once the file has been downloaded, this commands should be run (assuming Unix-like system, such as Linux, and Postgresql installed and configured):

`psql -d news -f newsdata.sql`

Then go into the database with

`psql news`

to run the commands you will see below to create these views:

**View to count articles views relating them to their authors:**

`create view authors_views as
      select au.id, count(l.*) as views
      from articles ar, authors au, log l where au.id = ar.author
      and ar.slug =substr(l.path, 10)
      group by au.id, l.path, ar.author;`

**View to count errors:**

`create view req_errors as
      select substr(time::text,0,11) as day, count(*) as errors
      from log where status not like '20%'
      group by day;`

**View to count all requests**

`create view req_totals as
      select substr(time::text,0,11) as day, count(*) as requests
      from log where status like '20%'
      group by day;`

Once you have created the database, tables, inserted the data and created the required views, you may run the Python program with this command:

`python run_analysis.py`

There are three questions the program must answer.

**1. What are the most popular three articles of all time? Which articles have been accessed the most?**

**2. Who are the most popular article authors of all time?
That is, when you sum up all of the articles each author has written, which authors get the most page views?**

**3. On which days did more than 1% of requests lead to errors?**
