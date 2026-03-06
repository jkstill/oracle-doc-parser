---
id: 19c__UTL_RECOMP.RECOMP_SERIAL
name: UTL_RECOMP.RECOMP_SERIAL
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: UTL_RECOMP
tags: [utl_recomp]
source_file: UTL_RECOMP.html
---

# UTL_RECOMP.RECOMP_SERIAL

This procedure recompiles invalid objects in a given schema or all invalid objects in the database.

## Syntax

```sql
UTL_RECOMP.RECOMP_SERIAL(
   schema   IN   VARCHAR2    DEFAULT NULL,
   flags    IN   PLS_INTEGER DEFAULT 0);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| schema | VARCHAR2 | IN | The schema in which to recompile invalid objects. If NULL , all invalid objects in the database are recompiled. |
| flags | PLS_INTEGER | IN | Flag values are intended for internal testing and diagnosability only. |

## Usage Notes

Syntax UTL_RECOMP.RECOMP_SERIAL( schema IN VARCHAR2 DEFAULT NULL, flags IN PLS_INTEGER DEFAULT 0); Parameters Table 273-3 RECOMP_SERIAL Procedure Parameters Parameter Description schema The schema in which to recompile invalid objects. If NULL , all invalid objects in the database are recompiled. flags Flag values are intended for internal testing and diagnosability only.