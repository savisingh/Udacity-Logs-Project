# Project: Logs Analysis - Savneet Singh

README for a Logs Analysis project using PSQL queries.
Running the Python code will execute queries that will return the answers to the specific 
questions (listed below). The python file to be executed in the virtual machine is called
 `newsdata.py`

## Required Libraries and Dependencies

- Python
  - Install **Python 2.7.14** at https://www.python.org/downloads/ 
- Vagrant
  - Install **Vagrant** at https://www.vagrantup.com/downloads.html
- Virtual Box 
  - Install **Virtual Box 5.1** at https://www.virtualbox.org/wiki/Download_Old_Builds_5_1
  
## How to Run the Project

- Bring the virtual machine up using the commands `vagrant up` followed by `vagrant ssh`
- `cd` into the `vagrant` directory
- Run the command `python newsdata.py` to get the results to the questions

## Views Used

- I used **views** in my work so the PSQL queries were simpler to read and understand. 
  I have listed the views for each question below:
   
- **What are the most popular three articles of all time?** 
  - contains the **view populararticles** 
  ```
    create view populararticles as
    SELECT log.path, count(*), REPLACE(path, '/article/', '') FROM log GROUP BY log.path 
    ORDER BY count desc;`
    ```

- **Who are the most popular article authors of all time?** 
  - contains the **view authorarticlecount** 
    ```
    create view authorarticlecount as
    select authors.name, populararticles.count from populararticles, articles, authors 
    where articles.slug = populararticles.replace and articles.author = authors.id;
    ```
 
- **On which days did more than 1% of requests lead to errors?** 
  - contains the **view okdate**
    ```
	create view okdate as select date(log.time), count(*) 
	from log where log.status='200 OK' group by date(log.time);
	```
  - contains the **view errordate**
    ```
	create view errordate as select date(log.time), count(*) 
	from log where log.status!='200 OK' group by date(log.time);
	```
  - contains the **view okdate**
    ```
	create view errorpercentages as select errordate.date as errordate, okdate.date as okdate,
	errordate.count as errorcount, okdate.count as okcount, 
	(errordate.count*100/(okdate.count+errordate.count)) as percentage 
	from errordate, okdate where okdate.date=errordate.date;
	```
 
