---
id: 19c__DBMS_FLASHBACK
name: DBMS_FLASHBACK
object_type: plsql_subprogram
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_FLASHBACK
tags: [dbms_flashback]
source_file: DBMS_FLASHBACK.html
---

# DBMS_FLASHBACK

The following example illustrates how Flashback can be used when the deletion of a senior employee triggers the deletion of all the personnel reporting to him. Using the Flashback feature, you can recover and re-insert the missing employees.

## Syntax

```sql
DROP TABLE employee;
DROP TABLE keep_scn;

REM -- Keep_scn is a temporary table to store scns that we are interested in

CREATE TABLE keep_scn (scn number); 
SET ECHO ON 
CREATE TABLE employee ( 
   employee_no   number(5) PRIMARY KEY, 
   employee_name varchar2(20), 
   employee_mgr  number(5) 
      CONSTRAINT mgr_fkey REFERENCES EMPLOYEE ON DELETE CASCADE, 
   salary        number, 
   hiredate      date 
); 

REM -- Populate the company with employees
INSERT INTO employee VALUES (1, 'John Doe', null, 1000000, '5-jul-81'); 
INSERT INTO employee VALUES (10, 'Joe Johnson', 1, 500000, '12-aug-84'); 
INSERT INTO employee VALUES (20, 'Susie Tiger', 10, 250000, '13-dec-90'); 
INSERT INTO employee VALUES (100, 'Scott Tiger', 20, 200000, '3-feb-86'); 
INSERT INTO employee VALUES (200, 'Charles Smith', 100, 150000, '22-mar-88'); 
INSERT INTO employee VALUES (210, 'Jane Johnson', 100, 100000, '11-apr-87'); 
INSERT INTO employee VALUES (220, 'Nancy Doe', 100, 100000, '18-sep-93'); 
INSERT INTO employee VALUES (300, 'Gary Smith', 210, 75000, '4-nov-96'); 
INSERT INTO employee VALUES (310, 'Bob Smith', 210, 65000, '3-may-95'); 
COMMIT; 

REM -- Show the entire org
SELECT lpad(' ', 2*(level-1)) || employee_name Name 
FROM employee 
CONNECT BY PRIOR employee_no = employee_mgr 
START WITH employee_no = 1 
ORDER BY LEVEL; 

REM -- Sleep for a short time (approximately 10 to 20  seconds) to avoid 
REM -- querying close to table creation

EXECUTE DBMS_LOCK.SLEEP(10);

REM -- Store this snapshot for later access through Flashback
DECLARE 
I NUMBER; 
BEGIN 
I := DBMS_FLASHBACK.GET_SYSTEM_CHANGE_NUMBER; 
INSERT INTO keep_scn VALUES (I); 
COMMIT; 
END;
/

REM -- Scott decides to retire but the transaction is done incorrectly
DELETE FROM EMPLOYEE WHERE employee_name = 'Scott Tiger'; 
COMMIT; 

REM -- notice that all of scott's employees are gone 
SELECT lpad(' ', 2*(level-1)) || employee_name Name 
FROM EMPLOYEE 
CONNECT BY PRIOR employee_no = employee_mgr 
START WITH employee_no = 1 
ORDER BY LEVEL; 

REM -- Flashback to see Scott's organization
DECLARE 
   restore_scn number; 
BEGIN 
   SELECT  scn INTO restore_scn FROM keep_scn; 
   DBMS_FLASHBACK.ENABLE_AT_SYSTEM_CHANGE_NUMBER (restore_scn); 
END; 
/ 

REM -- Show Scott's org.
SELECT lpad(' ', 2*(level-1)) || employee_name Name 
FROM employee 
CONNECT BY PRIOR employee_no = employee_mgr 
START WITH employee_no = 
   (SELECT employee_no FROM employee WHERE employee_name = 'Scott Tiger') 
ORDER BY LEVEL; 

REM -- Restore scott's organization.
DECLARE 
   scotts_emp NUMBER; 
   scotts_mgr NUMBER; 
   CURSOR c1 IS 
      SELECT employee_no, employee_name, employee_mgr, salary, hiredate 
      FROM employee 
      CONNECT BY PRIOR employee_no = employee_mgr 
      START WITH employee_no = 
         (SELECT employee_no FROM employee WHERE employee_name = 'Scott Tiger'); 
   c1_rec c1 % ROWTYPE; 
BEGIN 
   SELECT employee_no, employee_mgr INTO scotts_emp, scotts_mgr FROM employee 
   WHERE employee_name = 'Scott Tiger'; 
   /* Open c1 in flashback mode */
   OPEN c1; 
   /* Disable Flashback */
   DBMS_FLASHBACK.DISABLE; 
 LOOP 
   FETCH c1 INTO c1_rec; 
   EXIT WHEN c1%NOTFOUND; 
   /*
     Note that all the DML operations inside the loop are performed
     with Flashback disabled
   */
   IF (c1_rec.employee_mgr = scotts_emp) then 
      INSERT INTO employee VALUES (c1_rec.employee_no, 
         c1_rec.employee_name, 
         scotts_mgr, 
         c1_rec.salary, 
         c1_rec.hiredate); 
   ELSE 
   IF (c1_rec.employee_no != scotts_emp) THEN 
   INSERT INTO employee VALUES (c1_rec.employee_no, 
         c1_rec.employee_name, 
         c1_rec.employee_mgr, 
         c1_rec.salary, 
         c1_rec.hiredate); 
      END IF; 
    END IF; 
 END LOOP; 
END; 
/ 

REM -- Show the restored organization.
select lpad(' ', 2*(level-1)) || employee_name Name 
FROM employee 
CONNECT BY PRIOR employee_no = employee_mgr 
START WITH employee_no = 1 
ORDER BY LEVEL;
```

## Usage Notes

DROP TABLE employee; DROP TABLE keep_scn; REM -- Keep_scn is a temporary table to store scns that we are interested in CREATE TABLE keep_scn (scn number); SET ECHO ON CREATE TABLE employee ( employee_no number(5) PRIMARY KEY, employee_name varchar2(20), employee_mgr number(5) CONSTRAINT mgr_fkey REFERENCES EMPLOYEE ON DELETE CASCADE, salary number, hiredate date ); REM -- Populate the company with employees INSERT INTO employee VALUES (1, 'John Doe', null, 1000000, '5-jul-81'); INSERT INTO employee VALUES (10, 'Joe Johnson', 1, 500000, '12-aug-84'); INSERT INTO employee VALUES (20, 'Susie Tiger', 10, 250000, '13-dec-90'); INSERT INTO employee VALUES (100, 'Scott Tiger', 20, 200000, '3-feb-86'); INSERT INTO employee VALUES (200, 'Charles Smith', 100, 150000, '22-mar-88'); INSERT INTO employee VALUES (210, 'Jane Johnson', 100, 100000, '11-apr-87'); INSERT INTO employee VALUES (220, 'Nancy Doe', 100, 100000, '18-sep-93'); INSERT INTO employee VALUES (300, 'Gary Smith', 210, 75000, '4-nov-96'); INSERT INTO employee VALUES (310, 'Bob Smith', 210, 65000, '3-may-95'); COMMIT; REM -- Show the entire org SELECT lpad(' ', 2*(level-1)) || employee_name Name FROM employee CONNECT BY PRIOR employee_no = employee_mgr START WITH employee_no = 1 ORDER BY LEVEL; REM -- Sleep for a short time (approximately 10 to 20 seconds) to avoid REM -- querying close to table creation EXECUTE DBMS_LOCK.SLEEP(10); REM -- Store this snapshot for later access through Flashback DECLARE I NUMBER; BEGIN I := DBMS_FLASHBACK.GET_SYSTEM_CHANGE_NUMBER; INSERT INTO keep_scn VALUES (I); COMMIT; END; / REM -- Scott decides to retire but the transaction is done incorrectly DELETE FROM EMPLOYEE WHERE employee_name = 'Scott Tiger'; COMMIT; REM -- notice that all of scott's employees are gone SELECT lpad(' ', 2*(level-1)) || employee_name Name FROM EMPLOYEE CONNECT BY PRIOR employee_no = employee_mgr START WITH employee_no = 1 ORDER BY LEVEL; REM -- Flashback to see Scott's organization DECLARE restore_scn number; BEGIN SELECT scn INTO restore_scn FROM keep_scn; DBMS_FLASHBACK.ENABLE_AT_SYSTEM_CHANGE_NUMBER (restore_scn); END; / REM -- Show Scott's org. SELECT lpad(' ', 2*(level-1)) || employee_name Name FROM employee CONNECT BY PRIOR employee_no = employee_mgr START WITH employee_no = (SELECT employee_no FROM employee WHERE employee_name = 'Scott Tiger') ORDER BY LEVEL; REM -- Restore scott's organization. DECLARE scotts_emp NUMBER; scotts_mgr NUMBER; CURSOR c1 IS SELECT employee_no, employee_name, employee_mgr, salary, hiredate FROM employee CONNECT BY PRIOR employee_no = employee_mgr START WITH employee_no = (SELECT employee_no FROM employee WHERE employee_name = 'Scott Tiger'); c1_rec c1 % ROWTYPE; BEGIN SELECT employee_no, employee_mgr INTO scotts_emp, scotts_mgr FROM employee WHERE employee_name = 'Scott Tiger'; /* Open c1 in flashback mode */ OPEN c1; /* Disable Flashback */ DBMS_FLASHBACK.DISABLE; LOOP FETCH c1 INTO c1_rec; EXIT WHEN c1%NOTFOUND; /* Note that all the DML operations inside the loop are performed with Flashback disabled */ IF (c1_rec.employee_mgr = scotts_emp) then INSERT INTO employee VALUES (c1_rec.employee_no, c1_rec.employee_name, scotts_mgr, c1_rec.salary, c1_rec.hiredate); ELSE IF (c1_rec.employee_no != scotts_emp) THEN INSERT INTO employee VALUES (c1_rec.employee_no, c1_rec.employee_name, c1_rec.employee_mgr, c1_rec.salary, c1_rec.hiredate); END IF; END IF; END LOOP; END; / REM -- Show the restored organization. select lpad(' ', 2*(level-1)) || employee_name Name FROM employee CONNECT BY PRIOR employee_no = employee_mgr START WITH employee_no = 1 ORDER BY LEVEL;