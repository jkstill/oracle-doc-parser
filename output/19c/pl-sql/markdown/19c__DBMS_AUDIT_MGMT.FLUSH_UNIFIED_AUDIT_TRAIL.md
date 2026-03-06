---
id: 19c__DBMS_AUDIT_MGMT.FLUSH_UNIFIED_AUDIT_TRAIL
name: DBMS_AUDIT_MGMT.FLUSH_UNIFIED_AUDIT_TRAIL
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_AUDIT_MGMT
tags: [dbms_audit_mgmt]
source_file: DBMS_AUDIT_MGMT.html
---

# DBMS_AUDIT_MGMT.FLUSH_UNIFIED_AUDIT_TRAIL

This deprecated procedure writes the unified audit trail records in the SGA queue to disk.

## Syntax

```sql
DBMS_AUDIT_MGMT.FLUSH_UNIFIED_AUDIT_TRAIL (
   flush_type      IN BINARY_INTEGER   DEFAULT FLUSH_CURRENT_INSTANCE,
   container       IN BINARY_INTEGER   DEFAULT CONTAINER_CURRENT);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| flush_type | BINARY_INTEGER | IN | Takes one of the following two arguments: FLUSH_CURRENT_INSTANCE - Flushes the audit records from SGA queues in that particular RAC instance FLUSH_ALL_INSTANCES - Flushes the audit records from SGA queues in all the RAC instances |
| container | BINARY_INTEGER | IN | The containers where the SGA queues should be flushed. It takes one of the following two arguments: CONTAINER_CURRENT - Flushes the audit records from SGA queues in that particular PDB CONTAINER_ALL - Flushes the audit records from SGA queues in all the active PDBs. |

## Usage Notes

Note: This procedure has been deprecated starting in Oracle Database 12 c release 12.2. Note: This procedure has been deprecated starting in Oracle Database 12 c release 12.2. Syntax DBMS_AUDIT_MGMT.FLUSH_UNIFIED_AUDIT_TRAIL ( flush_type IN BINARY_INTEGER DEFAULT FLUSH_CURRENT_INSTANCE, container IN BINARY_INTEGER DEFAULT CONTAINER_CURRENT); Parameters Table 27-16 FLUSH_UNIFIED_AUDIT_TRAIL Procedure Parameters Parameter Description flush_type Takes one of the following two arguments: FLUSH_CURRENT_INSTANCE - Flushes the audit records from SGA queues in that particular RAC instance FLUSH_ALL_INSTANCES - Flushes the audit records from SGA queues in all the RAC instances container The containers where the SGA queues should be flushed. It takes one of the following two arguments: CONTAINER_CURRENT - Flushes the audit records from SGA queues in that particular PDB CONTAINER_ALL - Flushes the audit records from SGA queues in all the active PDBs.