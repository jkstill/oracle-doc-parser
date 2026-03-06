---
id: 19c__DBMS_AUDIT_MGMT.GET_
name: DBMS_AUDIT_MGMT.GET_
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_AUDIT_MGMT
tags: [dbms_audit_mgmt]
source_file: DBMS_AUDIT_MGMT.html
---

# DBMS_AUDIT_MGMT.GET_

This procedure returns the property value set by the SET_AUDIT_TRAIL_PROPERTY Procedure.

## Syntax

```sql
DBMS_AUDIT_MGMT.GET_AUDIT_TRAIL_PROPERTY_VALUE(
   audit_trail_type         IN PLS_INTEGER,
   audit_trail_property     IN PLS_INTEGER)
 RETURN NUMBER;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| audit_trail_type | PLS_INTEGER | IN | The audit trail type for the timestamp to be retrieved. Audit trail types are listed in Table 27-1 . |
| audit_trail_property | PLS_INTEGER) | IN | The audit trail property that is being queried. Audit trail properties are listed in Table 27-2 . |

**Returns:** `NUMBER`

## Usage Notes

Syntax DBMS_AUDIT_MGMT.GET_AUDIT_TRAIL_PROPERTY_VALUE( audit_trail_type IN PLS_INTEGER, audit_trail_property IN PLS_INTEGER) RETURN NUMBER; Parameters Table 27-17 GET_ AUDIT_TRAIL_PROPERTY_VALUE Function Parameters Parameter Description audit_trail_type The audit trail type for the timestamp to be retrieved. Audit trail types are listed in Table 27-1 . audit_trail_property The audit trail property that is being queried. Audit trail properties are listed in Table 27-2 . Return Values If the property value is cached in SGA memory, this function will return the value set by the SET_AUDIT_TRAIL_PROPERTY Procedure . Else it will return NULL . The GET_AUDIT_TRAIL_PROPERTY_VALUE function may return an ORA-46250 error if the audit trail property value has been set to DBMS_AUDIT_MGMT.CLEAN_UP_INTERVAL . To find the cleanup interval of the purge job, query SYS.DAM_CLEANUP_JOBS$ . Examples The following example prints the property value of OS_FILE_MAX_AGE set by the SET_AUDIT_TRAIL_PROPERTY Procedure . SET_AUDIT_TRAIL_PROPERTY. SET SERVEROUTPUT ON DECLARE OS_MAX_AGE_VAL NUMBER; BEGIN OS_MAX_AGE_VAL := DBMS_AUDIT_MGMT.GET_AUDIT_TRAIL_PROPERTY_VALUE( audit_trail_type => DBMS_AUDIT_MGMT.AUDIT_TRAIL_OS, audit_trail_property => DBMS_AUDIT_MGMT. OS_FILE_MAX_AGE); IF OS_MAX_AGE_VAL is not NULL THEN DBMS_OUTPUT.PUT_LINE('The Maximum Age configured for OS Audit files is: ' || OS_MAX_AGE_VAL); END IF; END;