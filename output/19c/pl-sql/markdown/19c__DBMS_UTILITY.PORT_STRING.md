---
id: 19c__DBMS_UTILITY.PORT_STRING
name: DBMS_UTILITY.PORT_STRING
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_UTILITY
tags: [dbms_utility]
source_file: DBMS_UTILITY.html
---

# DBMS_UTILITY.PORT_STRING

This function returns a string that identifies the operating system and the TWO TASK PROTOCOL version of the database. For example, " VAX/VMX-7 . 1 . 0 . 0 "

## Syntax

```sql
DBMS_UTILITY.PORT_STRING 
   RETURN VARCHAR2;
```

**Returns:** `VARCHAR2`

## Usage Notes

The maximum length is port-specific. Syntax DBMS_UTILITY.PORT_STRING RETURN VARCHAR2; Pragmas pragma restrict_references(port_string, WNDS, RNDS, WNPS, RNPS);