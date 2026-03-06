---
id: 19c__ALL_PROCEDURES
name: ALL_PROCEDURES
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: objects
tags: [all]
source_file: ALL_PROCEDURES.html
---

# ALL_PROCEDURES

DBA_PROCEDURES lists all functions and procedures available in the database, along with associated properties.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| OWNER | VARCHAR2(128) | Owner of the procedure |
| OBJECT_NAME | VARCHAR2(128) | Name of the object: top-level function, procedure, or package name |
| PROCEDURE_NAME | VARCHAR2(128) | Name of the procedure |
| OBJECT_ID | NUMBER | Object number of the object |
| SUBPROGRAM_ID | NUMBER | Unique subprogram identifier |
| OVERLOAD | VARCHAR2(40) | Overload unique identifier |
| OBJECT_TYPE | VARCHAR2(13) | The typename of the object |
| AGGREGATE | VARCHAR2(3) | Indicates whether the procedure is an aggregate function ( YES ) or not ( NO ) |
| PIPELINED | VARCHAR2(3) | Indicates whether the procedure is a pipelined table function ( YES ) or not ( NO ) |
| IMPLTYPEOWNER | VARCHAR2(128) | Owner of the implementation type, if any |
| IMPLTYPENAME | VARCHAR2(128) | Name of the implementation type, if any |
| PARALLEL | VARCHAR2(3) | Indicates whether the procedure or function is parallel-enabled ( YES ) or not ( NO ) |
| INTERFACE | VARCHAR2(3) | YES , if the procedure/function is a table function implemented using the ODCI interface; otherwise NO |
| DETERMINISTIC | VARCHAR2(3) | YES , if the procedure/function is declared to be deterministic; otherwise NO |
| AUTHID | VARCHAR2(12) | Indicates whether the procedure/function is declared to execute as DEFINER or CURRENT_USER (invoker) |
| RESULT_CACHE | VARCHAR2(3) | Indicates whether the function is result–cached ( YES ) or not ( NO ) |
| ORIGIN_CON_ID | VARCHAR2(256) | The ID of the container where the data originates. Possible values include: 0 : This value is used for rows in non-CDBs. This value is not used for CDBs. n : This value is used for rows containing data that originate in the container with container ID n ( n = 1 if the row originates in root) |
| POLYMORPHIC | VARCHAR2(5) | The type of polymorphic table function: ROW TABLE LEAF NULL |

## Usage Notes

Related Views DBA_PROCEDURES lists all functions and procedures available in the database, along with associated properties. USER_PROCEDURES lists all functions and procedures owned by the current user, along with associated properties. It does not contain the OWNER column. Note: SQL macros for table expressions are supported starting with Oracle Database release 19c, version 19.7. In future releases, the ALL_ , DBA_ , and USER_PROCEDURES data dictionary views contain a column called SQL_MACRO , which enables you to identify the SQL macros in your database. However, this column is not available in Oracle Database 19c. Instead, refer to My Oracle Support note 2678637.1 "How To Identify the SQL Macros in Oracle Data Dictionary 19.7 Onwards" at the following URL to learn how to identify SQL macros in Oracle Database 19c: https://support.oracle.com/rs?type=doc&id=2678637.1 See Also: " DBA_PROCEDURES " " USER_PROCEDURES " " ALL_ARGUMENTS " for information about the arguments of the functions and procedures that are accessible to the current user Note: SQL macros for table expressions are supported starting with Oracle Database release 19c, version 19.7. In future releases, the ALL_ , DBA_ , and USER_PROCEDURES data dictionary views contain a column called SQL_MACRO , which enables you to identify the SQL macros in your database. However, this column is not available in Oracle Database 19c. Instead, refer to My Oracle Support note 2678637.1 "How To Identify the SQL Macros in Oracle Data Dictionary 19.7 Onwards" at the following URL to learn how to identify SQL macros in Oracle Database 19c: https://support.oracle.com/rs?type=doc&id=2678637.1 See Also: " DBA_PROCEDURES " " USER_PROCEDURES " " ALL_ARGUMENTS " for information about the arguments of the functions and procedures that are accessible to the current user