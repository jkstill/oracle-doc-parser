---
id: 19c__DBMS_LOB.ISSECUREFILE
name: DBMS_LOB.ISSECUREFILE
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_LOB
tags: [dbms_lob]
source_file: DBMS_LOB.html
---

# DBMS_LOB.ISSECUREFILE

This function returns TRUE if the LOB locator passed to it is for a SecureFile LOB. It returns FALSE otherwise.

## Syntax

```sql
DBMS_LOB ISSECUREFILE(
    lob_loc    IN      BLOB)
  RETURN BOOLEAN;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| lob_loc | BLOB) | IN | LOB locator. For more information, see Operational Notes . |

**Returns:** `BOOLEAN`

## Usage Notes

Syntax DBMS_LOB ISSECUREFILE( lob_loc IN BLOB) RETURN BOOLEAN; Pragmas PRAGMA RESTRICT_REFERENCES(issecurefile, WNDS, RNDS, WNPS, RNPS); Parameters Table 99-72 ISSECUREFILE Function Parameter Parameter Description lob_loc LOB locator. For more information, see Operational Notes . Return Values This function returns TRUE if the LOB locator passed to it is for a SecureFile LOB. It returns FALSE otherwise.