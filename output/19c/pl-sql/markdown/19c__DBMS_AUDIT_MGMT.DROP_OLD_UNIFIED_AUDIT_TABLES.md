---
id: 19c__DBMS_AUDIT_MGMT.DROP_OLD_UNIFIED_AUDIT_TABLES
name: DBMS_AUDIT_MGMT.DROP_OLD_UNIFIED_AUDIT_TABLES
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_AUDIT_MGMT
tags: [dbms_audit_mgmt]
source_file: DBMS_AUDIT_MGMT.html
---

# DBMS_AUDIT_MGMT.DROP_OLD_UNIFIED_AUDIT_TABLES

This procedure drops old unified audit tables following the cloning of a pluggable database (PDB).

## Syntax

```sql
DBMS_AUDIT_MGMT.DROP_OLD_UNIFIED_AUDIT_TABLES(
   container_guid    IN VARCHAR2) ;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| container_guid | VARCHAR2) | IN | Container GUID of the old unified audit tables |

## Usage Notes

Syntax DBMS_AUDIT_MGMT.DROP_OLD_UNIFIED_AUDIT_TABLES( container_guid IN VARCHAR2) ; Parameters Table 27-14 DROP_OLD_UNIFIED_AUDIT_TABLES Procedure Parameters Parameter Description container_guid Container GUID of the old unified audit tables Usage Notes When a pluggable database gets cloned, the unified audit tables get newly created in the new pluggable database. To drop the old unified audit tables, use the DROP_OLD_UNIFIED_AUDIT_TABLES by specifying the old GUID of the PDB from which the clone was created. You can query the historical GUIDs from the DBA_PDB_HISTORY view for the given PDB. Examples BEGIN DBMS_AUDIT_MGMT.DROP_OLD_UNIFIED_AUDIT_TABLES ( container_guid => 'E4721865A9321CB5E043EFA9E80A2D77'); END;