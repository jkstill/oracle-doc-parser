---
id: 19c__DBMS_AUDIT_MGMT.GET_AUDIT_COMMIT_DELAY
name: DBMS_AUDIT_MGMT.GET_AUDIT_COMMIT_DELAY
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_AUDIT_MGMT
tags: [dbms_audit_mgmt]
source_file: DBMS_AUDIT_MGMT.html
---

# DBMS_AUDIT_MGMT.GET_AUDIT_COMMIT_DELAY

This function returns the audit commit delay time as the number of seconds. audit commit delay time is the maximum time that it takes to COMMIT an audit record to the database audit trail. If it takes more time to COMMIT an audit record than defined by the audit commit delay time, then a copy of the audit record is written to the operating system (OS) audit trail.

## Syntax

```sql
DBMS_AUDIT_MGMT.GET_AUDIT_COMMIT_DELAY
  RETURN NUMBER;
```

**Returns:** `NUMBER`

## Usage Notes

The audit commit delay time value is useful when determining the last archive timestamp for database audit records. Syntax DBMS_AUDIT_MGMT.GET_AUDIT_COMMIT_DELAY RETURN NUMBER;