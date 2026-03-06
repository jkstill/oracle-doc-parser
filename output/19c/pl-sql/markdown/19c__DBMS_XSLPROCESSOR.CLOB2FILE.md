---
id: 19c__DBMS_XSLPROCESSOR.CLOB2FILE
name: DBMS_XSLPROCESSOR.CLOB2FILE
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XSLPROCESSOR
tags: [dbms_xslprocessor]
source_file: DBMS_XSLPROCESSOR.html
---

# DBMS_XSLPROCESSOR.CLOB2FILE

This procedure writes content of a CLOB into a file. This procedure has moved to the DBMS_LOB package, starting in Oracle Database 12 c release 12.2.

## Syntax

```sql
DBMS_XSLPROCESSOR.CLOB2FILE(
  cl          IN  CLOB,
  flocation   IN  VARCHAR2,
  fname       IN  VARCHAR2,
  csid        IN  NUMBER := 0);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| c1 |  |  | CLOB |
| flocation | VARCHAR2 | IN | File directory |
| fname | VARCHAR2 | IN | File name |
| csid | NUMBER | IN | Character set id of the file Must be a valid Oracle id; otherwise returns an error If 0 , content of the output file will be in the database character set |

## Usage Notes

Syntax DBMS_XSLPROCESSOR.CLOB2FILE( cl IN CLOB, flocation IN VARCHAR2, fname IN VARCHAR2, csid IN NUMBER := 0); Parameters Table 216-2 CLOB2FILE Procedure Parameters Parameter Description c1 CLOB flocation File directory fname File name csid Character set id of the file Must be a valid Oracle id; otherwise returns an error If 0 , content of the output file will be in the database character set