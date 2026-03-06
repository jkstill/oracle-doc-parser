---
id: 19c__DBMS_LOB.FREETEMPORARY
name: DBMS_LOB.FREETEMPORARY
object_type: plsql_subprogram
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_LOB
tags: [dbms_lob]
source_file: DBMS_LOB.html
---

# DBMS_LOB.FREETEMPORARY

This procedure frees the temporary BLOB or CLOB in the default temporary tablespace.

## Syntax

```sql
DBMS_LOB.FREETEMPORARY (
   lob_loc  IN OUT  NOCOPY BLOB); 

DBMS_LOB.FREETEMPORARY (
   lob_loc  IN OUT  NOCOPY CLOB CHARACTER SET ANY_CS);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| lob_loc | NOCOPY | IN OUT | LOB locator.For more information, see Operational Notes . |

## Usage Notes

Syntax DBMS_LOB.FREETEMPORARY ( lob_loc IN OUT NOCOPY BLOB); DBMS_LOB.FREETEMPORARY ( lob_loc IN OUT NOCOPY CLOB CHARACTER SET ANY_CS); Parameters Table 99-53 FREETEMPORARY Procedure Parameters Parameter Description lob_loc LOB locator.For more information, see Operational Notes . Usage Notes When a new temporary LOB is created, and there is currently no temporary LOB in use with the same duration (session, call), a new temporary LOB segment is created. When the temporary LOB is freed, the space it consumed is released to the temporary segment. If there are no other temporary LOBs for the same duration, the temporary segment is also freed. After the call to FREETEMPORARY , the LOB locator that was freed is marked as invalid. If an invalid LOB locator is assigned to another LOB locator using OCILobLocatorAssign in OCI or through an assignment operation in PL/SQL, then the target of the assignment is also freed and marked as invalid. See Also: Oracle Database SecureFiles and Large Objects Developer's Guide for additional details on usage of this procedure See Also: Oracle Database SecureFiles and Large Objects Developer's Guide for additional details on usage of this procedure