---
id: 19c__DBMS_DBFS_CONTENT.TRACEENABLED
name: DBMS_DBFS_CONTENT.TRACEENABLED
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_DBFS_CONTENT
tags: [dbms_dbfs_content]
source_file: DBMS_DBFS_CONTENT.html
---

# DBMS_DBFS_CONTENT.TRACEENABLED

This function determines if the current trace "severity" set by the SETTRACE Procedure is at least as high as the given trace level.

## Syntax

```sql
DBMS_DBFS_CONTENT.TRACEENABLED(
   sev         IN              INTEGER)
  RETURN  INTEGER;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| sev | INTEGER) | IN | Severity at which trace message is output |

**Returns:** `INTEGER`

## Usage Notes

Syntax DBMS_DBFS_CONTENT.TRACEENABLED( sev IN INTEGER) RETURN INTEGER; Parameters Table 52-76 TRACEENABLED Procedure Parameters Parameter Description sev Severity at which trace message is output Return Values Returns 0 if the requested severity level is lower than the currently set trace severity level; 1 otherwise.