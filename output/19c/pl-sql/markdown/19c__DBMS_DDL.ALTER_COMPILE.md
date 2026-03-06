---
id: 19c__DBMS_DDL.ALTER_COMPILE
name: DBMS_DDL.ALTER_COMPILE
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_DDL
tags: [dbms_ddl]
source_file: DBMS_DDL.html
---

# DBMS_DDL.ALTER_COMPILE

This procedure is equivalent to the SQL statement: ALTER PROCEDURE|FUNCTION|PACKAGE [<schema>.] <name> COMPILE [BODY]

## Syntax

```sql
DBMS_DDL.ALTER_COMPILE (
   type             VARCHAR2, 
   schema           VARCHAR2, 
   name             VARCHAR2
   reuse_settings   BOOLEAN := FALSE);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| type | VARCHAR2 | IN | Must be either PROCEDURE , FUNCTION , PACKAGE , PACKAGE BODY or TRIGGER |
| schema | VARCHAR2 | IN | Schema name If NULL , then use current schema (case-sensitive) |
| name | VARCHAR2 | IN | Name of the object (case-sensitive) |
| reuse_settings | BOOLEAN | IN | Indicates whether the session settings in the objects should be reused, or whether the current session settings should be adopted instead |

## Usage Notes

Note: This procedure is deprecated in Oracle Database 10 g Release 2 (10.2) While the procedure remains available in the package for reasons of backward compatibility, Oracle recommends using the DDL equivalent in a dynamic SQL statement. Note: This procedure is deprecated in Oracle Database 10 g Release 2 (10.2) While the procedure remains available in the package for reasons of backward compatibility, Oracle recommends using the DDL equivalent in a dynamic SQL statement. Syntax DBMS_DDL.ALTER_COMPILE ( type VARCHAR2, schema VARCHAR2, name VARCHAR2 reuse_settings BOOLEAN := FALSE); Parameters Table 56-2 ALTER_COMPILE Procedure Parameters Parameter Description type Must be either PROCEDURE , FUNCTION , PACKAGE , PACKAGE BODY or TRIGGER schema Schema name If NULL , then use current schema (case-sensitive) name Name of the object (case-sensitive) reuse_settings Indicates whether the session settings in the objects should be reused, or whether the current session settings should be adopted instead Exceptions Table 56-3 ALTER_COMPILE Procedure Exceptions Exception Description ORA-20000: Insufficient privileges or object does not exist ORA-20001: Remote object, cannot compile ORA-20002: Bad value for object type: should be either PACKAGE , PACKAGE BODY , PROCEDURE , FUNCTION , or TRIGGER