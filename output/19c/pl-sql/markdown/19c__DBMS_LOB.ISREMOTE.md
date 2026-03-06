---
id: 19c__DBMS_LOB.ISREMOTE
name: DBMS_LOB.ISREMOTE
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_LOB
tags: [dbms_lob]
source_file: DBMS_LOB.html
---

# DBMS_LOB.ISREMOTE

This function checks to see if the LOB is local to the database or if it belongs to a remote database.

## Syntax

```sql
DBMS_LOB.ISREMOTE (
   lob_loc IN BLOB)
  RETURN BOOLEAN;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| lob_loc | BLOB) | IN | Locator for the LOB . |

**Returns:** `BOOLEAN`

## Usage Notes

Syntax DBMS_LOB.ISREMOTE ( lob_loc IN BLOB) RETURN BOOLEAN; DBMS_LOB.ISREMOTE ( lob_loc IN CLOB CHARACTER SET ANY_CS) RETURN BOOLEAN; Pragmas PRAGMA RESTRICT_REFERENCES(isremote, WNDS, RNDS, WNPS, RNPS); Parameters Table 99-71 ISREMOTE Function Parameter Parameter Description lob_loc Locator for the LOB . Return Values BOOLEAN : TRUE for remote LOBs obtained over a database link; FALSE for LOBs obtained from local database See Also: Distributed LOBs chapter in Database SecureFiles and Large Objects Developer's Guide for more details on the usage of this procedure. See Also: Distributed LOBs chapter in Database SecureFiles and Large Objects Developer's Guide for more details on the usage of this procedure.