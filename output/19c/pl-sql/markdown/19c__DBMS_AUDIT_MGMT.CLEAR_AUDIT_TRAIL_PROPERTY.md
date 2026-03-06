---
id: 19c__DBMS_AUDIT_MGMT.CLEAR_AUDIT_TRAIL_PROPERTY
name: DBMS_AUDIT_MGMT.CLEAR_AUDIT_TRAIL_PROPERTY
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_AUDIT_MGMT
tags: [dbms_audit_mgmt]
source_file: DBMS_AUDIT_MGMT.html
---

# DBMS_AUDIT_MGMT.CLEAR_AUDIT_TRAIL_PROPERTY

This procedure clears the value for the specified audit trail property.

## Syntax

```sql
DBMS_AUDIT_MGMT.CLEAR_AUDIT_TRAIL_PROPERTY(
   audit_trail_type        IN PLS_INTEGER,
   audit_trail_property    IN PLS_INTEGER,
   use_default_values      IN BOOLEAN DEFAULT FALSE) ;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| audit_trail_type | PLS_INTEGER | IN | The audit trail type for which the property needs to be cleared. Audit trail types are listed in Table 27-1 |
| audit_trail_property | PLS_INTEGER | IN | The audit trail property whose value needs to be cleared. You cannot clear the value for the CLEANUP_INTERVAL property. Audit trail properties are listed in Table 27-2 |
| use_default_values | BOOLEAN | IN | Specifies whether the default value of the audit_trail_property should be used in place of the cleared value. A value of TRUE causes the default value of the parameter to be used. A value of FALSE causes the audit_trail_property to have no value. The default value for this parameter is FALSE . |

## Usage Notes

Audit trail properties are set using the SET_AUDIT_TRAIL_PROPERTY Procedure . The CLEAR_AUDIT_TRAIL_PROPERTY procedure can optionally reset the property value to it's default value through the use_default_values parameter. Syntax DBMS_AUDIT_MGMT.CLEAR_AUDIT_TRAIL_PROPERTY( audit_trail_type IN PLS_INTEGER, audit_trail_property IN PLS_INTEGER, use_default_values IN BOOLEAN DEFAULT FALSE) ; Parameters Table 27-10 CLEAR_AUDIT_TRAIL_PROPERTY Procedure Parameters Parameter Description audit_trail_type The audit trail type for which the property needs to be cleared. Audit trail types are listed in Table 27-1 audit_trail_property The audit trail property whose value needs to be cleared. You cannot clear the value for the CLEANUP_INTERVAL property. Audit trail properties are listed in Table 27-2 use_default_values Specifies whether the default value of the audit_trail_property should be used in place of the cleared value. A value of TRUE causes the default value of the parameter to be used. A value of FALSE causes the audit_trail_property to have no value. The default value for this parameter is FALSE . Usage Notes The following usage notes apply: You can use this procedure to clear the value for an audit trail property that you do not wish to use. For example, if you do not want a restriction on the operating system audit file size, then you can use this procedure to reset the OS_FILE_MAX_SIZE property. You can also use this procedure to reset an audit trail property to it's default value. You need to set use_default_values to TRUE when invoking the procedure. The DB_DELETE_BATCH_SIZE property needs to be individually cleared for the AUDIT_TRAIL_AUD_STD and AUDIT_TRAIL_FGA_STD audit trail types. You cannot clear this property collectively using the AUDIT_TRAIL_DB_STD and AUDIT_TRAIL_ALL audit trail types. If you clear the value of the DB_DELETE_BATCH_SIZE property with use_default_value set to FALSE , the default value of DB_DELETE_BATCH_SIZE is still assumed. This is because audit records are always deleted in batches. The FILE_DELETE_BATCH_SIZE property needs to be individually cleared for the AUDIT_TRAIL_OS and AUDIT_TRAIL_XML audit trail types. You cannot clear this property collectively using the AUDIT_TRAIL_FILES and AUDIT_TRAIL_ALL audit trail types. If you clear the value of the FILE_DELETE_BATCH_SIZE property with use_default_value set to FALSE , the default value of FILE_DELETE_BATCH_SIZE is still assumed. This is because audit files are always deleted in batches. You cannot clear the value for the CLEANUP_INTERVAL property. You cannot clear the value for the AUDIT_TRAIL_WRITE_MODE property. Examples The following example calls the CLEAR_AUDIT_TRAIL_PROPERTY procedure to clear the value for the audit trail property, OS_FILE_MAX_SIZE . The procedure uses a value of FALSE for the USE_DEFAULT_VALUES parameter. This means that there will be no maximum size threshold for operating system (OS) audit files. BEGIN DBMS_AUDIT_MGMT.CLEAR_AUDIT_TRAIL_PROPERTY( AUDIT_TRAIL_TYPE => DBMS_AUDIT_MGMT.AUDIT_TRAIL_OS, AUDIT_TRAIL_PROPERTY => DBMS_AUDIT_MGMT.OS_FILE_MAX_SIZE, USE_DEFAULT_VALUES => FALSE ); END;