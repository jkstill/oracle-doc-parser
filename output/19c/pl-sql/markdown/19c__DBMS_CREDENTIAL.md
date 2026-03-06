---
id: 19c__DBMS_CREDENTIAL
name: DBMS_CREDENTIAL
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_CREDENTIAL
tags: [dbms_credential]
source_file: DBMS_CREDENTIAL.html
---

# DBMS_CREDENTIAL

As the existing CREATE OR REPLACE LIBRARY statement and CREATE OR REPLACE FUNCTION/PROCEDURE do not support a CREDENTIAL clause, this model requires syntax and semantic changes in CREATE OR REPLACE LIBRARY and CCREATE OR REPLACE FUNCTION/PROCEDUREREATE statement.

## Syntax

```sql
CREATE OR REPLACE LIBRARY test 
  AS '$ORACLE_HOME/bin/test.so' CREDENTIAL ricky_cred;
CREATE OR REPLACE FUNCTION ftest1
  (x VARCHAR2, y BINARY_INTEGER)
RETURN BINARY_INTEGER
AS LANGUAGE C
LIBRARY test
NAME "negative"
PARAMETERS(x STRING, y INT);
```

**Returns:** `BINARY_INTEGER`

## Usage Notes

For example: CREATE OR REPLACE LIBRARY test AS '$ORACLE_HOME/bin/test.so' CREDENTIAL ricky_cred; CREATE OR REPLACE FUNCTION ftest1 (x VARCHAR2, y BINARY_INTEGER) RETURN BINARY_INTEGER AS LANGUAGE C LIBRARY test NAME "negative" PARAMETERS(x STRING, y INT); The credential name defined in the CREDENTIAL clause is a name of a database object. Therefore, do not enclose the credential name with single or double quotes. An example of a credential being used on an external job: BEGIN DBMS_SCHEDULER.CREATE_JOB( job_name => 'example_job', job_type => 'EXECUTABLE', job_action => '/bin/ls', credential_name => 'ricky_cred'); END; /