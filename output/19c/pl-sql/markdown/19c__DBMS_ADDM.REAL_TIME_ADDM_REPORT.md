---
id: 19c__DBMS_ADDM.REAL_TIME_ADDM_REPORT
name: DBMS_ADDM.REAL_TIME_ADDM_REPORT
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_ADDM
tags: [dbms_addm]
source_file: DBMS_ADDM.html
---

# DBMS_ADDM.REAL_TIME_ADDM_REPORT

This function produces a real-time ADDM report for ADDM-related activity for the last five minutes. In an Oracle Real Application Clusters (Oracle RAC) environment, the function assumes that executing SQL over GV$ is possible.

## Syntax

```sql
DBMS_ADDM.REAL_TIME_ADDM_REPORT ()
 RETURN CLOB;
```

**Returns:** `CLOB`

## Usage Notes

Syntax DBMS_ADDM.REAL_TIME_ADDM_REPORT () RETURN CLOB; Return Values CLOB containing a real-time ADDM report