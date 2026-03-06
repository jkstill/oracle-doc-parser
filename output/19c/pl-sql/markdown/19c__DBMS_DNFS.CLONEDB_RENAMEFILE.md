---
id: 19c__DBMS_DNFS.CLONEDB_RENAMEFILE
name: DBMS_DNFS.CLONEDB_RENAMEFILE
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_DNFS
tags: [dbms_dnfs]
source_file: DBMS_DNFS.html
---

# DBMS_DNFS.CLONEDB_RENAMEFILE

This procedure is used to rename datafiles that were pointing to the backup set to the actual file name in cloned database.

## Syntax

```sql
DBMS_DNFS.CLONEDB_RENAMEFILE (
   srcfile        IN         VARCHAR2,
   destfile       IN         VARCHAR2);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| srcfile | VARCHAR2 | IN | Source datafile name in the control file |
| destfile | VARCHAR2) | IN | New datafile name |

## Usage Notes

The srcfile is the file name that represents the data file in the backup image copy or a read-only storage snapshot. The destfile destination file path must point to a NFS volume where cloneDB datafiles will be created. When the procedure is run successfully, the control file record is updated with the new datafile name. Syntax DBMS_DNFS.CLONEDB_RENAMEFILE ( srcfile IN VARCHAR2, destfile IN VARCHAR2); Parameters Table 64-2 CLONEDB_RENAMEFILE Procedure Parameters Parameter Description srcfile Source datafile name in the control file destfile New datafile name