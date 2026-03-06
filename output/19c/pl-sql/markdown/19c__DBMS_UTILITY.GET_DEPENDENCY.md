---
id: 19c__DBMS_UTILITY.GET_DEPENDENCY
name: DBMS_UTILITY.GET_DEPENDENCY
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_UTILITY
tags: [dbms_utility]
source_file: DBMS_UTILITY.html
---

# DBMS_UTILITY.GET_DEPENDENCY

This deprecated procedure shows the dependencies on the object passed in.

## Syntax

```sql
DBMS_UTILITY.GET_DEPENDENCY
   type      IN     VARCHAR2,
   schema    IN     VARCHAR2,
   name      IN     VARCHAR2);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| type | VARCHAR2 | IN | Type of the object, for example if the object is a table give the type as ' TABLE ' |
| schema | VARCHAR2 | IN | Schema name of the object |
| name | VARCHAR2) | IN | Name of the object |

## Usage Notes

Note: This subprogram has been deprecated and replaced in Oracle Database 12c release 12.2 and later. Oracle recommends that you do not use deprecated subprograms. It is maintained only for purposes of backward compatibility. Note: This subprogram has been deprecated and replaced in Oracle Database 12c release 12.2 and later. Oracle recommends that you do not use deprecated subprograms. It is maintained only for purposes of backward compatibility. Syntax DBMS_UTILITY.GET_DEPENDENCY type IN VARCHAR2, schema IN VARCHAR2, name IN VARCHAR2); Parameters Table 187-20 GET_DEPENDENCY Procedure Parameters Parameter Description type Type of the object, for example if the object is a table give the type as ' TABLE ' schema Schema name of the object name Name of the object Usage Notes This procedure uses the DBMS_OUTPUT package to display results, and so you must declare SET SERVEROUTPUT ON if you wish to view dependencies. Alternatively, any application that checks the DBMS_OUTPUT output buffers can invoke this subprogram and then retrieve the output by means of DBMS_OUTPUT subprograms such as GET_LINES .