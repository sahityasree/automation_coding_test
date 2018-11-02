MySQL with python
Ref python programs:  mysql_connection.py--MYSQL connection using python 
tables_query_from_schema.py--Creating tables and query in mysql.
Below are the tables and table contents in mysql which are created from schema:
mysql> desc employees;
+------------+---------------+------+-----+---------+-------+
| Field      | Type          | Null | Key | Default | Extra |
+------------+---------------+------+-----+---------+-------+
| emp_no     | int(11)       | NO   | PRI | 0       |       |
| birth_date | date          | YES  |     | NULL    |       |
| first_name | varchar(14)   | YES  |     | NULL    |       |
| last_name  | varchar(16)   | YES  |     | NULL    |       |
| gender     | enum('M','F') | YES  |     | NULL    |       |
| hire_date  | date          | YES  |     | NULL    |       |
+------------+---------------+------+-----+---------+-------+
6 rows in set (0.06 sec)
mysql> desc departments;
+-----------+-------------+------+-----+---------+-------+
| Field     | Type        | Null | Key | Default | Extra |
+-----------+-------------+------+-----+---------+-------+
| dept_no   | char(4)     | NO   | PRI |         |       |
| dept_name | varchar(40) | YES  |     | NULL    |       |
+-----------+-------------+------+-----+---------+-------+
2 rows in set (0.03 sec)
mysql> desc  titles;
ERROR 6 (HY000): Error on delete of 'C:\Windows\TEMP\#sql748_30_6.MYI' (Errcode: 13)
mysql> desc titles;
+-----------+-------------+------+-----+------------+-------+
| Field     | Type        | Null | Key | Default    | Extra |
+-----------+-------------+------+-----+------------+-------+
| emp_no    | int(11)     | YES  | MUL | NULL       |       |
| title     | varchar(50) | NO   | PRI |            |       |
| from_date | date        | NO   | PRI | 0000-00-00 |       |
| to_date   | date        | YES  |     | NULL       |       |
+-----------+-------------+------+-----+------------+-------+
4 rows in set (0.01 sec)
mysql> desc dept_manager;
ERROR 1036 (HY000): Table 'C:\Windows\TEMP\#sql748_30_8' is read only
mysql> desc dept_manager;
+-----------+---------+------+-----+---------+-------+
| Field     | Type    | Null | Key | Default | Extra |
+-----------+---------+------+-----+---------+-------+
| emp_no    | int(11) | YES  | MUL | NULL    |       |
| dept_no   | char(4) | YES  | MUL | NULL    |       |
| from_date | date    | YES  |     | NULL    |       |
| to_date   | date    | YES  |     | NULL    |       |
+-----------+---------+------+-----+---------+-------+
mysql> desc dept_emp;
+-----------+---------+------+-----+---------+-------+
| Field     | Type    | Null | Key | Default | Extra |
+-----------+---------+------+-----+---------+-------+
| emp_no    | int(11) | YES  | MUL | NULL    |       |
| dept_no   | char(4) | YES  | MUL | NULL    |       |
| from_date | date    | YES  |     | NULL    |       |
| to_date   | date    | YES  |     | NULL    |       |
+-----------+---------+------+-----+---------+-------+
4 rows in set (0.01 sec)
mysql> desc salaries;
+-----------+---------+------+-----+------------+-------+
| Field     | Type    | Null | Key | Default    | Extra |
+-----------+---------+------+-----+------------+-------+
| emp_no    | int(11) | YES  | MUL | NULL       |       |
| salary    | int(11) | YES  |     | NULL       |       |
| from_date | date    | NO   | PRI | 0000-00-00 |       |
| to_date   | date    | YES  |     | NULL       |       |
+-----------+---------+------+-----+------------+-------+
4 rows in set (0.07 sec)
table contents:
mysql> select * from employees;
+--------+------------+------------+-----------+--------+------------+
| emp_no | birth_date | first_name | last_name | gender | hire_date  |
+--------+------------+------------+-----------+--------+------------+
|    101 | 1991-05-12 | navya      | sree      | M      | 2017-08-12 |
|    102 | 1990-01-12 | sree       | sara      | F      | 2016-07-12 |
|    103 | 1993-08-02 | ravi       | shankar   | M      | 2017-09-01 |
|    104 | 1991-06-26 | arun       | deep      | M      | 2012-04-25 |
|    105 | 1988-05-25 | siva       | deepa     | F      | 2013-04-25 |
|    106 | 1992-04-21 | sai        | krupa     | F      | 2015-05-25 |
|    107 | 1986-04-21 | naveen     | kumar     | M      | 2011-06-01 |
|    108 | 1993-04-21 | sravani    | begum     | F      | 2016-06-07 |
|    109 | 1992-08-18 | swetha     | kumari    | F      | 2017-06-17 |
|    110 | 1990-07-19 | raman      | choudari  | M      | 2015-07-15 |
+--------+------------+------------+-----------+--------+------------+
10 rows in set (0.00 sec)
mysql> select * from titles
--------+------------------+------------+------------+
 emp_no | title            | from_date  | to_date    |
--------+------------------+------------+------------+
    107 | test_manager     | 2011-06-01 | 2018-09-30 |
    104 | dev manager      | 2012-04-25 | 2018-09-30 |
    105 | senior tester    | 2013-04-25 | 2018-09-30 |
    106 | senior developer | 2015-05-25 | 2018-09-30 |
    110 | dev_lead         | 2015-07-15 | 2018-09-30 |
    108 | developer        | 2016-06-07 | 2018-09-30 |
    102 | Developer        | 2016-07-12 | 2018-08-12 |
    109 | sales_admin      | 2017-06-17 | 2018-09-30 |
    101 | Tester           | 2017-08-12 | 2018-07-01 |
    103 | Administrater    | 2017-09-01 | 2018-06-01 |
--------+------------------+------------+------------+
10 rows in set (0.00 sec)
mysql> select * from salaries
    -> ;
+--------+--------+------------+------------+
| emp_no | salary | from_date  | to_date    |
+--------+--------+------------+------------+
|    107 | 100000 | 2011-06-01 | 2018-09-30 |
|    104 | 100000 | 2012-04-25 | 2018-09-30 |
|    105 |  60000 | 2013-04-25 | 2018-09-30 |
|    106 |  70000 | 2015-05-25 | 2018-09-30 |
|    110 |  80000 | 2015-07-15 | 2018-09-30 |
|    108 |  40000 | 2016-06-07 | 2018-09-30 |
|    102 |  40000 | 2016-07-12 | 2018-08-12 |
|    109 |  35000 | 2017-06-17 | 2018-09-30 |
|    101 |  35000 | 2017-08-12 | 2018-07-01 |
|    103 |  30000 | 2017-09-01 | 2018-06-01 |
+--------+--------+------------+------------+
10 rows in set (0.00 sec)
mysql> select * from departments;
+---------+--------------+
| dept_no | dept_name    |
+---------+--------------+
| 1111    | Testing      |
| 1112    | Developement |
| 1113    | Admin        |
+---------+--------------+
3 rows in set (0.00 sec)
mysql> select * from dept_emp
| emp_no | dept_no | from_date  | to_date    |
+--------+---------+------------+------------+
|    102 | 1112    | 2017-09-01 | 2018-06-01 |
|    101 | 1111    | 2017-09-01 | 2018-06-01 |
|    103 | 1113    | 2017-09-01 | 2018-06-01 |
|    104 | 1112    | 2012-04-25 | 2018-09-30 |
|    105 | 1111    | 2013-04-25 | 2018-09-30 |
|    106 | 1112    | 2015-05-25 | 2018-09-30 |
|    107 | 1111    | 2011-06-01 | 2018-09-30 |
|    108 | 1112    | 2016-06-07 | 2018-09-30 |
|    109 | 1113    | 2017-06-17 | 2018-09-30 |
|    110 | 1112    | 2015-07-15 | 2018-09-30 |
Query:
mysql> select DISTINCT e.last_name,t.title,e.gender,e.hire_date,d.dept_name,concat(e.first_name, ' ',e.last_name) as dept_manager_name,t.title as manager_title from employees e,departments d,dept_manager dm,dept_emp ed,titles t where e.emp_no=t.emp_no AND e.emp_no=dm.emp_no AND d.dept_no=dm.dept_no AND d.dept_no=ed.dept_no;
+-----------+--------------+--------+------------+--------------+-------------------+---------------+
| last_name | title        | gender | hire_date  | dept_name    | dept_manager_name | manager_title |
+-----------+--------------+--------+------------+--------------+-------------------+---------------+
| kumar     | test_manager | M      | 2011-06-01 | Testing      | naveen kumar      | test_manager  |
| deep      | dev manager  | M      | 2012-04-25 | Developement | arun deep         | dev manager   |
+-----------+--------------+--------+------------+--------------+-------------------+---------------+
2 rows in set (0.06 sec)
