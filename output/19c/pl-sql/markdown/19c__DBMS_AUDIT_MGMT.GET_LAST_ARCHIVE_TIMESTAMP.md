---
id: 19c__DBMS_AUDIT_MGMT.GET_LAST_ARCHIVE_TIMESTAMP
name: DBMS_AUDIT_MGMT.GET_LAST_ARCHIVE_TIMESTAMP
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_AUDIT_MGMT
tags: [dbms_audit_mgmt]
source_file: DBMS_AUDIT_MGMT.html
---

# DBMS_AUDIT_MGMT.GET_LAST_ARCHIVE_TIMESTAMP

This procedure returns the timestamp set by the SET_LAST_ARCHIVE_TIMESTAMP Procedure in that database instance.

## Syntax

```sql
DBMS_AUDIT_MGMT.GET_LAST_ARCHIVE_TIMESTAMP(
   audit_trail_type     IN PLS_INTEGER)
 RETURN TIMESTAMP;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| audit_trail_type | PLS_INTEGER) | IN | The audit trail type for the timestamp to be retrieved. Supported Audit trail types for this procedure are AUDIT_TRAIL_OS , AUDIT_TRAIL_XML and AUDIT_TRAIL_UNIFIED . All Audit trail types are listed in Table 27-1 . |

**Returns:** `TIMESTAMP`

## Usage Notes

Syntax DBMS_AUDIT_MGMT.GET_LAST_ARCHIVE_TIMESTAMP( audit_trail_type IN PLS_INTEGER) RETURN TIMESTAMP; Parameters Table 27-18 GET_LAST_ARCHIVE_TIMESTAMP Function Parameters Parameter Description audit_trail_type The audit trail type for the timestamp to be retrieved. Supported Audit trail types for this procedure are AUDIT_TRAIL_OS , AUDIT_TRAIL_XML and AUDIT_TRAIL_UNIFIED . All Audit trail types are listed in Table 27-1 . Return Values In a database that is opened for READ WRITE , since there will no timestamp stored in SGA memory, this function will return NULL . But in a database that is opened for READ ONLY , if a timestamp is set by the SET_LAST_ARCHIVE_TIMESTAMP Procedure, the timestamp will be returned. Else it will return NULL . Usage Notes This function will return NULL on a database that is opened READ WRITE . Use DBA_AUDIT_MGMT_LAST_ARCH_TS view to check the timestamp set in such a case. Examples The following example prints the timestamp set by the SET_LAST_ARCHIVE_TIMESTAMP Procedure on a READ ONLY database. SET SERVEROUTPUT ON DECLARE LAT_TS TIMESTAMP; BEGIN LAT_TS := DBMS_AUDIT_MGMT.GET_LAST_ARCHIVE_TIMESTAMP( audit_trail_type => DBMS_AUDIT_MGMT.AUDIT_TRAIL_OS); IF LAT_TS is not NULL THEN DBMS_OUTPUT.PUT_LINE('The Last Archive Timestamp is: ' || to_char(LAT_TS)); END IF; END;