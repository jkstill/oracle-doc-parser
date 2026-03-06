---
id: 19c__V$SQL_TESTCASES
name: V$SQL_TESTCASES
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: sql
tags: [dynamic_performance]
source_file: V-SQL_TESTCASES.html
---

# V$SQL_TESTCASES

V$SQL_TESTCASES displays information about test cases exported by SQL Test Case Builder.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| TESTCASE_NAME | VARCHAR2(512) |  |
| SQL_ID | VARCHAR2(13) |  |
| SQL_TEXT | VARCHAR2(1000) |  |
| SQL_TEXT_FULL | CLOB |  |
| INCIDENT_ID | NUMBER |  |
| PROBLEM_TYPE | NUMBER |  |
| CREATION_DATE | TIMESTAMP(6) |  |
| STATUS | VARCHAR2(10) |  |
| CON_ID | NUMBER |  |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content You can use this view in conjunction with the V$DIAG_INCIDENT view. Join the INCIDENT_ID column in this view with the INCIDENT_ID column in V$DIAG_INCIDENT to view information about the test case associated with a particular incident. The V$SQL_TESTCASES view requires the existence of a TCB root directory named SQL_TCB_DIR . This view will not contain any rows if a TCB root directory does not exist, or if the TCB root directory exists with a name other than SQL_TCB_DIR . The operating system directory to which the TCB root directory refers must be writable by the owner of the Oracle Database binaries. In Oracle Autonomous Database environments, the TCB root directory is created automatically on each POD during provisioning. For on-premises databases, a user who has been granted the DBA role must explicitly create the TCB root directory. See Oracle Database Administrator’s Guide for more information. Note: This view is available starting with Oracle Database release 19c, version 19.1. See Also: " V$DIAG_INCIDENT " Note: This view is available starting with Oracle Database release 19c, version 19.1. See Also: " V$DIAG_INCIDENT "