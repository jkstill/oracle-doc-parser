---
id: 19c__DBMS_XMLPARSER.NEWPARSER
name: DBMS_XMLPARSER.NEWPARSER
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XMLPARSER
tags: [dbms_xmlparser]
source_file: DBMS_XMLPARSER.html
---

# DBMS_XMLPARSER.NEWPARSER

This function returns a new parser instance.

## Syntax

```sql
FUNCTION newParser 
RETURN Parser;
```

**Returns:** `Parser`

## Usage Notes

This function must be called before the default behavior of Parser can be changed and if other parse methods need to be used. FUNCTION newParser RETURN Parser;