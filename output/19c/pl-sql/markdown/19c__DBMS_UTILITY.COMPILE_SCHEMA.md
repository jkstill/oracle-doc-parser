---
id: 19c__DBMS_UTILITY.COMPILE_SCHEMA
name: DBMS_UTILITY.COMPILE_SCHEMA
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_UTILITY
tags: [dbms_utility]
source_file: DBMS_UTILITY.html
---

# DBMS_UTILITY.COMPILE_SCHEMA

This procedure compiles all procedures, functions, packages, views and triggers in the specified schema.

## Syntax

```sql
DBMS_UTILITY.COMPILE_SCHEMA (
   schema          IN VARCHAR2,
   compile_all     IN BOOLEAN DEFAULT TRUE,
   reuse_settings  IN BOOLEAN DEFAULT FALSE);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| schema | VARCHAR2 | IN | Name of the schema |
| compile_all | BOOLEAN | IN | If TRUE , will compile everything within the schema regardless of whether it is VALID If FALSE , will compile only INVALID objects |
| reuse_settings | BOOLEAN | IN | Indicates whether the session settings in the objects should be reused, or whether the current session settings should be adopted instead |

## Usage Notes

Syntax DBMS_UTILITY.COMPILE_SCHEMA ( schema IN VARCHAR2, compile_all IN BOOLEAN DEFAULT TRUE, reuse_settings IN BOOLEAN DEFAULT FALSE); Parameters Table 187-11 COMPILE_SCHEMA Procedure Parameters Parameter Description schema Name of the schema compile_all If TRUE , will compile everything within the schema regardless of whether it is VALID If FALSE , will compile only INVALID objects reuse_settings Indicates whether the session settings in the objects should be reused, or whether the current session settings should be adopted instead Exceptions Table 187-12 COMPILE_SCHEMA Procedure Exceptions Exception Description ORA-20000 Insufficient privileges for some object in this schema ORA-20001 Cannot recompile SYS objects ORA-20002 Maximum iterations exceeded. Some objects may not have been recompiled. Usage Notes Note that this subprogram is a wrapper for the RECOMP_SERIAL Procedure included with the UTL_RECOMP package. After calling this procedure, you should select from view ALL_OBJECTS for items with status of INVALID to see if all objects were successfully compiled. To see the errors associated with INVALID objects, you may use the Enterprise Manager command: SHOW ERRORS <type> <schema>.<name>