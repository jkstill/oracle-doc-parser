---
id: 19c__DBMS_SQLTUNE.REMOVE_SQLSET_REFERENCE
name: DBMS_SQLTUNE.REMOVE_SQLSET_REFERENCE
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_SQLTUNE
tags: [dbms_sqltune]
source_file: DBMS_SQLTUNE.html
---

# DBMS_SQLTUNE.REMOVE_SQLSET_REFERENCE

This procedure deactivates a SQL tuning set to indicate that it is no longer used by the client.

## Syntax

```sql
DBMS_SQLTUNE.REMOVE_SQLSET_REFERENCE (
   sqlset_name   IN  VARCHAR2,
   reference_id  IN  NUMBER,
   sqlset_owner  IN  VARCHAR2 := NULL,
   force_remove  IN  NUMBER   := 0);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| sqlset_name | VARCHAR2 | IN | Specifies the name of the SQL tuning set. |
| reference_id | NUMBER | IN | Specifies the identifier of the reference to remove. |
| sqlset_owner | VARCHAR2 | IN | Specifies the owner of the SQL tuning set (or NULL for the current schema owner). |
| force_remove | NUMBER | IN | Specifies whether references can be removed for other users ( 1 ) or whether they cannot be removed ( 0 ). Setting this parameter to 1 only takes effect when the user has the ADMINISTER ANY SQL TUNING SET privilege. Otherwise, the database only removes references owned by the user. |

## Usage Notes

See Also: DBMS_SQLTUNE SQL Tuning Set Subprograms for other subprograms in this group See Also: DBMS_SQLTUNE SQL Tuning Set Subprograms for other subprograms in this group Syntax DBMS_SQLTUNE.REMOVE_SQLSET_REFERENCE ( sqlset_name IN VARCHAR2, reference_id IN NUMBER, sqlset_owner IN VARCHAR2 := NULL, force_remove IN NUMBER := 0); Parameters The parameters are identical for the DBMS_SQLTUNE.REMOVE_SQLSET_REFERENCE and DBMS_SQLSET.REMOVE_REFERENCE procedures. Table 169-30 REMOVE_SQLSET_REFERENCE and REMOVE_REFERENCE Procedure Parameters Parameter Description sqlset_name Specifies the name of the SQL tuning set. reference_id Specifies the identifier of the reference to remove. sqlset_owner Specifies the owner of the SQL tuning set (or NULL for the current schema owner). force_remove Specifies whether references can be removed for other users ( 1 ) or whether they cannot be removed ( 0 ). Setting this parameter to 1 only takes effect when the user has the ADMINISTER ANY SQL TUNING SET privilege. Otherwise, the database only removes references owned by the user. Examples You can remove references on a given SQL tuning set when you finish using it and want to make it writable again. The following example removes the reference to my_workload : EXEC DBMS_SQLTUNE.REMOVE_SQLSET_REFERENCE( - sqlset_name => 'my_workload', - reference_id => :rid, sqlset_owner => NULL, force_remove => 0); To find all references to a given SQL tuning set, query the DBA_SQLSET_REFERENCES view.