---
id: 19c__DBMS_CUBE_LOG.DEFAULT_NAME
name: DBMS_CUBE_LOG.DEFAULT_NAME
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_CUBE_LOG
tags: [dbms_cube_log]
source_file: DBMS_CUBE_LOG.html
---

# DBMS_CUBE_LOG.DEFAULT_NAME

This function returns the default table names of the various log types.

## Syntax

```sql
DBMS_CUBE_LOG.DEFAULT_NAME (
           LOG_TYPE       IN   BINARY_INTEGER  DEFAULT TYPE_OPERATIONS)
     RETURN VARCHAR2;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| log_type | BINARY_INTEGER | IN | One of the following log types: 1 : TYPE_OPERATIONS 2 : TYPE_REJECTED_RECORDS 3 : TYPE_DIMENSION_COMPILE 4 : TYPE_BUILD See " Logging Types " . |

**Returns:** `VARCHAR2`

## Usage Notes

Syntax DBMS_CUBE_LOG.DEFAULT_NAME ( LOG_TYPE IN BINARY_INTEGER DEFAULT TYPE_OPERATIONS) RETURN VARCHAR2; Parameters Table 46-2 DEFAULT_NAME Function Parameters Parameter Description log_type One of the following log types: 1 : TYPE_OPERATIONS 2 : TYPE_REJECTED_RECORDS 3 : TYPE_DIMENSION_COMPILE 4 : TYPE_BUILD See " Logging Types " . Returns The default table name of the specified log type. Examples This example returns the default name of the Cube Operations log: SELECT dbms_cube_log.default_name FROM dual; DEFAULT_NAME ------------------------------ CUBE_OPERATIONS_LOG The next example returns the default name of the Cube Rejected Records log: select dbms_cube_log.default_name(dbms_cube_log.type_rejected_records) - "Default Name" from dual; Default Name ------------------------- CUBE_REJECTED_RECORDS