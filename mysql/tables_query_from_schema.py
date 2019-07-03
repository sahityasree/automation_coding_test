import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="123456",
  database="myprojects"
 
)

mycursor = mydb.cursor()


#mycursor.execute("CREATE DATABASE myprojects")
#mycursor.execute("CREATE TABLE employees (emp_no INT(11), birth_date DATE, first_name VARCHAR(14),last_name VARCHAR(16),gender ENUM('M','F'),hire_date DATE,PRIMARY KEY(emp_no))")
#mycursor.execute ("CREATE TABLE salaries(emp_no INT(11), salary INT(11),from_date DATE,to_date DATE,PRIMARY KEY(from_date),CONSTRAINT FOREIGN KEY (emp_no) REFERENCES employees(emp_no) )")

#mycursor.execute ("CREATE TABLE titles(emp_no INT(11), title VARCHAR(50),from_date DATE,to_date DATE,PRIMARY KEY(from_date,title),CONSTRAINT FOREIGN KEY (emp_no) REFERENCES employees(emp_no) )")
#mycursor.execute ("CREATE TABLE departments(dept_no CHAR(4), dept_name VARCHAR(40),PRIMARY KEY(dept_no))")
#mycursor.execute ("CREATE TABLE dept_manager(emp_no INT(11), dept_no CHAR(4),from_date DATE,to_date DATE,CONSTRAINT FOREIGN KEY (dept_no) REFERENCES departments(dept_no),CONSTRAINT FOREIGN KEY (emp_no) REFERENCES employees(emp_no) )")
#mycursor.execute ("CREATE TABLE dept_emp(emp_no INT(11), dept_no CHAR(4),from_date DATE,to_date DATE,CONSTRAINT FOREIGN KEY (dept_no) REFERENCES departments(dept_no),CONSTRAINT FOREIGN KEY (emp_no) REFERENCES employees(emp_no) )")
#mycursor.execute("show tables")
#mycursor.execute("select * from employees")

#mycursor.execute("select * from employees")
#print("")


mycursor.execute("select DISTINCT e.last_name,t.title,e.gender,e.hire_date,d.dept_name,concat(e.first_name, ' ',e.last_name) as dept_manager_name,t.title as manager_title from employees e,departments d,dept_manager dm,dept_emp ed,titles t where e.emp_no=t.emp_no AND e.emp_no=dm.emp_no AND d.dept_no=dm.dept_no AND d.dept_no=ed.dept_no");
myresult = mycursor.fetchall()

for x in myresult:
  print(x)
