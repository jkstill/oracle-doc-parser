---
id: 19c__DBMS_XSLPROCESSOR.READ2CLOB
name: DBMS_XSLPROCESSOR.READ2CLOB
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XSLPROCESSOR
tags: [dbms_xslprocessor]
source_file: DBMS_XSLPROCESSOR.html
---

# DBMS_XSLPROCESSOR.READ2CLOB

This function reads content of a file into a CLOB .

## Syntax

```sql
DBMS_XSLPROCESSOR.READ2CLOB(
   flocation     IN   VARCHAR2,
   fname         IN   VARCHAR2,
   csid          IN   NUMBER:=0)
 RETURN CLOB;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| flocation | VARCHAR2 | IN | File directory |
| fname | VARCHAR2 | IN | File name |
| csid | NUMBER | IN | Character set id of the file Must be a valid Oracle id; otherwise returns an error If 0 , input file is assumed to be in the database character set |

**Returns:** `CLOB`

## Usage Notes

Note: This procedure has moved to the DBMS_LOB package, starting in Oracle Database 12 c release 12.2. Note: This procedure has moved to the DBMS_LOB package, starting in Oracle Database 12 c release 12.2. Syntax DBMS_XSLPROCESSOR.READ2CLOB( flocation IN VARCHAR2, fname IN VARCHAR2, csid IN NUMBER:=0) RETURN CLOB; Parameters Table 216-7 READ2CLOB Function Parameters Parameter Description flocation File directory fname File name csid Character set id of the file Must be a valid Oracle id; otherwise returns an error If 0 , input file is assumed to be in the database character set