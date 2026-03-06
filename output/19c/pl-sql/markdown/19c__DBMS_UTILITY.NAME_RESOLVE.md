---
id: 19c__DBMS_UTILITY.NAME_RESOLVE
name: DBMS_UTILITY.NAME_RESOLVE
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_UTILITY
tags: [dbms_utility]
source_file: DBMS_UTILITY.html
---

# DBMS_UTILITY.NAME_RESOLVE

This procedure resolves the given name, including synonym translation and authorization checking as necessary.

## Syntax

```sql
DBMS_UTILITY.NAME_RESOLVE (
   name          IN  VARCHAR2, 
   context       IN  NUMBER,
   schema        OUT VARCHAR2, 
   part1         OUT VARCHAR2, 
   part2         OUT VARCHAR2,
   dblink        OUT VARCHAR2, 
   part1_type    OUT NUMBER, 
   object_number OUT NUMBER);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| name | VARCHAR2 | IN | Name of the object. This can be of the form [[a.]b.]c[@d], where a, b, c are SQL identifier and d is a dblink. No syntax checking is performed on the dblink. If a dblink is specified, or if the name resolves to something with a dblink, then object is not resolved, but the schema , part1 , part2 and dblink OUT parameters are filled in. a, b and c may be delimited identifiers, and may contain Globalization Support (NLS) characters (single and multibyte). |
| context | NUMBER | IN | Must be an integer between 0 and 9. 0 - table 1 - PL/SQL (for 2 part names) 2 - sequences 3 - trigger 4 - Java Source 5 - Java resource 6 - Java class 7 - type 8 - Java shared data 9 - index |
| schema | VARCHAR2 | OUT | Schema of the object: c. If no schema is specified in name , then the schema is determined by resolving the name. |
| part1 | VARCHAR2 | OUT | First part of the name. The type of this name is specified part1_type (synonym or package). |
| part2 | VARCHAR2 | OUT | If this is non- NULL , then this is a subprogram name. If part1 is non- NULL , then the subprogram is within the package indicated by part1. If part1 is NULL , then the subprogram is a top-level subprogram. |
| dblink | VARCHAR2 | OUT | If this is non- NULL , then a database link was either specified as part of name or name was a synonym which resolved to something with a database link. In this case, if further name translation is desired, then you must call the DBMS_UTILITY.NAME_RESOLVE procedure on this remote node. |
| part1_type | NUMBER | OUT | Type of part1 is: 5 - synonym 7 - procedure (top level) 8 - function (top level) 9 - package |
| object_number | NUMBER) | OUT | Object identifier |

## Usage Notes

Syntax DBMS_UTILITY.NAME_RESOLVE ( name IN VARCHAR2, context IN NUMBER, schema OUT VARCHAR2, part1 OUT VARCHAR2, part2 OUT VARCHAR2, dblink OUT VARCHAR2, part1_type OUT NUMBER, object_number OUT NUMBER); Parameters Table 187-30 NAME_RESOLVE Procedure Parameters Parameter Description name Name of the object. This can be of the form [[a.]b.]c[@d], where a, b, c are SQL identifier and d is a dblink. No syntax checking is performed on the dblink. If a dblink is specified, or if the name resolves to something with a dblink, then object is not resolved, but the schema , part1 , part2 and dblink OUT parameters are filled in. a, b and c may be delimited identifiers, and may contain Globalization Support (NLS) characters (single and multibyte). context Must be an integer between 0 and 9. 0 - table 1 - PL/SQL (for 2 part names) 2 - sequences 3 - trigger 4 - Java Source 5 - Java resource 6 - Java class 7 - type 8 - Java shared data 9 - index schema Schema of the object: c. If no schema is specified in name , then the schema is determined by resolving the name. part1 First part of the name. The type of this name is specified part1_type (synonym or package). part2 If this is non- NULL , then this is a subprogram name. If part1 is non- NULL , then the subprogram is within the package indicated by part1. If part1 is NULL , then the subprogram is a top-level subprogram. dblink If this is non- NULL , then a database link was either specified as part of name or name was a synonym which resolved to something with a database link. In this case, if further name translation is desired, then you must call the DBMS_UTILITY.NAME_RESOLVE procedure on this remote node. part1_type Type of part1 is: 5 - synonym 7 - procedure (top level) 8 - function (top level) 9 - package object_number Object identifier Exceptions All errors are handled by raising exceptions. A wide variety of exceptions are possible, based on the various syntax error that are possible when specifying object names.