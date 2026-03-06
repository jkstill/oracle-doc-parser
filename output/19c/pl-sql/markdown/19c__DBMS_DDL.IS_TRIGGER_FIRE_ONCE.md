---
id: 19c__DBMS_DDL.IS_TRIGGER_FIRE_ONCE
name: DBMS_DDL.IS_TRIGGER_FIRE_ONCE
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_DDL
tags: [dbms_ddl]
source_file: DBMS_DDL.html
---

# DBMS_DDL.IS_TRIGGER_FIRE_ONCE

This function returns TRUE if the specified DML or DDL trigger is set to fire once. Otherwise, it returns FALSE .

## Syntax

```sql
DBMS_DDL.IS_TRIGGER_FIRE_ONCE
   trig_owner         IN  VARCHAR2,
   trig_name          IN  VARCHAR2)
 RETURN BOOLEAN;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| trig_owner | VARCHAR2 | IN | Schema of trigger |
| trig_name | VARCHAR2) | IN | Name of trigger |

**Returns:** `BOOLEAN`

## Usage Notes

A fire once trigger fires in a user session but does not fire in the following cases: For changes made by a Streams apply process For changes made by executing one or more Streams apply errors using the EXECUTE_ERROR or EXECUTE_ALL_ERRORS procedure in the DBMS_APPLY_ADM package For changes made by a Logical Standby apply process Note: Only DML and DDL triggers can be fire once. All other types of triggers always fire. See Also: " SET_TRIGGER_FIRING_PROPERTY Procedures " Note: Only DML and DDL triggers can be fire once. All other types of triggers always fire. See Also: " SET_TRIGGER_FIRING_PROPERTY Procedures " Syntax DBMS_DDL.IS_TRIGGER_FIRE_ONCE trig_owner IN VARCHAR2, trig_name IN VARCHAR2) RETURN BOOLEAN; Parameters Table 56-7 IS_TRIGGER_FIRE_ONCE Function Parameters Parameter Description trig_owner Schema of trigger trig_name Name of trigger