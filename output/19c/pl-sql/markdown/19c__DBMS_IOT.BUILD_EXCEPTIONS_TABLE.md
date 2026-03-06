---
id: 19c__DBMS_IOT.BUILD_EXCEPTIONS_TABLE
name: DBMS_IOT.BUILD_EXCEPTIONS_TABLE
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_IOT
tags: [dbms_iot]
source_file: DBMS_IOT.html
---

# DBMS_IOT.BUILD_EXCEPTIONS_TABLE

This procedure creates an exception table.

## Syntax

```sql
DBMS_IOT.BUILD_EXCEPTIONS_TABLE (
   owner                 IN VARCHAR2,
   iot_name              IN VARCHAR2,
   exceptions_table_name IN VARCHAR2 default 'IOT_EXCEPTIONS');
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| owner | VARCHAR2 | IN | Owner of the index-organized table. |
| iot_name | VARCHAR2 | IN | Index-organized table name. |
| exceptions_table_name | VARCHAR2 | IN | Intended name for exception-table. |

## Usage Notes

Rows of an index-organized table that violate a constraint can be placed into this table during the execution of the following SQL statements: ALTER TABLE ... ENABLE CONSTRAINT ... EXCEPTIONS INTO ALTER TABLE ... ADD CONSTRAINT ... EXCEPTIONS INTO Syntax DBMS_IOT.BUILD_EXCEPTIONS_TABLE ( owner IN VARCHAR2, iot_name IN VARCHAR2, exceptions_table_name IN VARCHAR2 default 'IOT_EXCEPTIONS'); Parameters Table 91-3 BUILD_EXCEPTIONS_TABLE Procedure Parameters Parameter Description owner Owner of the index-organized table. iot_name Index-organized table name. exceptions_table_name Intended name for exception-table. Usage Notes You should create a separate exception table for each index-organized table to accommodate its primary key. Examples EXECUTE DBMS_IOT.BUILD_EXCEPTIONS_TABLE('SYS','L','LE'); An exception table for the preceding index-organized table with the following columns: Column Name Null? Type ------------------------------ -------- ---- ROW_ID VARCHAR2(30) OWNER VARCHAR2(30) TABLE_NAME VARCHAR2(30) CONSTRAINT VARCHAR2(30) A CHAR(16) B CHAR(16) C CHAR(16)