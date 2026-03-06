---
id: 19c__DBMS_ILM.ARCHIVESTATENAME
name: DBMS_ILM.ARCHIVESTATENAME
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_ILM
tags: [dbms_ilm]
source_file: DBMS_ILM.html
---

# DBMS_ILM.ARCHIVESTATENAME

This function returns the value of the ORA_ARCHIVE_STATE column of a row-archival enabled table.

## Syntax

```sql
DBMS_ILM.ARCHIVESTATENAME (
   value      IN  VARCHAR2) 
 RETURN VARCHAR2;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| value | VARCHAR2) | IN | Value for which the archive state name is to be returned |

**Returns:** `VARCHAR2`

## Usage Notes

Syntax DBMS_ILM.ARCHIVESTATENAME ( value IN VARCHAR2) RETURN VARCHAR2; Parameters Table 86-5 ARCHIVESTATENAME Function Parameters Parameter Description value Value for which the archive state name is to be returned Usage Notes Returns ARCHIVE_STATE_ACTIVE for 0 , ARCHIVE_STATE_ARCHIVED for others See Also: "Using In-Database Archiving" in Oracle Database VLDB and Partitioning Guide See Also: "Using In-Database Archiving" in Oracle Database VLDB and Partitioning Guide