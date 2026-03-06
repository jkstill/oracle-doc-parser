---
id: 19c__DBMS_CUBE_LOG.VERSION
name: DBMS_CUBE_LOG.VERSION
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_CUBE_LOG
tags: [dbms_cube_log]
source_file: DBMS_CUBE_LOG.html
---

# DBMS_CUBE_LOG.VERSION

This function returns the version number of a specific log table or the current version number of a specific log type.

## Syntax

```sql
DBMS_CUBE_LOG.VERSION (
          LOG_TYPE       IN   BINARY_INTEGER  DEFAULT 1,
          TBLNAME        IN   VARCHAR2        DEFAULT NULL)
     RETURN BINARY_INTEGER;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| log_type | BINARY_INTEGER | IN | One of the following log types: 1 : TYPE_OPERATIONS 2 : TYPE_REJECTED_RECORDS 3 : TYPE_DIMENSION_COMPILE 4 : TYPE_BUILD See " Logging Types " . |
| tblname | VARCHAR2 | IN | The name of the log table whose version is returned. |

**Returns:** `BINARY_INTEGER`

## Usage Notes

Syntax DBMS_CUBE_LOG.VERSION ( LOG_TYPE IN BINARY_INTEGER DEFAULT 1, TBLNAME IN VARCHAR2 DEFAULT NULL) RETURN BINARY_INTEGER; Parameters Table 46-10 VERSION Function Parameters Parameter Description log_type One of the following log types: 1 : TYPE_OPERATIONS 2 : TYPE_REJECTED_RECORDS 3 : TYPE_DIMENSION_COMPILE 4 : TYPE_BUILD See " Logging Types " . tblname The name of the log table whose version is returned. Returns A version number Examples This example returns the current version of the Cube Operations log: SELECT dbms_cube_log.version FROM dual; VERSION ---------- 2 This example returns the version number of an existing Cube Rejected Records log named CUBE_REJECTED_RECORDS . SELECT dbms_cube_log.version(dbms_cube_log.type_rejected_records, - 'CUBE_REJECTED_RECORDS') version FROM dual; VERSION ---------- 2