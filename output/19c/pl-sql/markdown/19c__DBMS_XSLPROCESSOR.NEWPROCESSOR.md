---
id: 19c__DBMS_XSLPROCESSOR.NEWPROCESSOR
name: DBMS_XSLPROCESSOR.NEWPROCESSOR
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XSLPROCESSOR
tags: [dbms_xslprocessor]
source_file: DBMS_XSLPROCESSOR.html
---

# DBMS_XSLPROCESSOR.NEWPROCESSOR

This function returns a new Processor instance.

## Syntax

```sql
DBMS_XSLPROCESSOR.NEWPROCESSOR
 RETURN Processor;
```

**Returns:** `Processor`

## Usage Notes

The function must be called before the default behavior of Processor can be changed and if other processor methods need to be used. Syntax DBMS_XSLPROCESSOR.NEWPROCESSOR RETURN Processor;