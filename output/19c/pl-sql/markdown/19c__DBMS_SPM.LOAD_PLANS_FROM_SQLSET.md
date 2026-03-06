---
id: 19c__DBMS_SPM.LOAD_PLANS_FROM_SQLSET
name: DBMS_SPM.LOAD_PLANS_FROM_SQLSET
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_SPM
tags: [dbms_spm]
source_file: DBMS_SPM.html
---

# DBMS_SPM.LOAD_PLANS_FROM_SQLSET

This function loads plans stored in a SQL tuning set (STS) into SQL plan baselines. The plans loaded from STS are not verified for performance but added as accepted plans to existing or new SQL plan baselines. This function can be used to seed SQL management base with new SQL plan baselines.

## Syntax

```sql
DBMS_SPM.LOAD_PLANS_FROM_SQLSET (
   sqlset_name      IN  VARCHAR2,
   sqlset_owner     IN  VARCHAR2 := NULL,
   basic_filter     IN  VARCHAR2 := NULL,
   fixed            IN  VARCHAR2 := 'NO',
   enabled          IN  VARCHAR2 := 'YES'
   commit_rows      IN  NUMBER   := 1000)
RETURN PLS_INTEGER;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| sqlset_name | VARCHAR2 | IN | Name of the STS from where the plans are loaded into SQL plan baselines |
| sqlset_owner | VARCHAR2 | IN | Owner of STS. NULL means current schema is the owner. |
| basic_filter | VARCHAR2 | IN | A filter applied to the STS to select only qualifying plans to be loaded. The filter can take the form of any WHERE clause predicate that can specified against the view DBA_SQLSET_STATEMENTS . For example basic_filter => ' sql_text like ''select /*LOAD_STS*/%''' or basic_filter => 'sql_id=''b62q7nc33gzwx''' . |
| fixed | VARCHAR2 | IN | Default ' NO ' means the loaded plans are used as non-fixed plans. Value ' YES ' means the loaded plans are used as fixed plans and the SQL plan baseline will not be evolved over time. |
| enabled | VARCHAR2 | IN | Default ' YES ' means the loaded plans are enabled for use by the optimizer |
| commit_rows | NUMBER | IN | Number of SQL plans to load before doing a periodic commit. This helps to shorten the undo log. |

**Returns:** `PLS_INTEGER`

## Usage Notes

Syntax DBMS_SPM.LOAD_PLANS_FROM_SQLSET ( sqlset_name IN VARCHAR2, sqlset_owner IN VARCHAR2 := NULL, basic_filter IN VARCHAR2 := NULL, fixed IN VARCHAR2 := 'NO', enabled IN VARCHAR2 := 'YES' commit_rows IN NUMBER := 1000) RETURN PLS_INTEGER; Parameters Table 161-20 LOAD_PLANS_FROM_SQLSET Function Parameters Parameter Description sqlset_name Name of the STS from where the plans are loaded into SQL plan baselines sqlset_owner Owner of STS. NULL means current schema is the owner. basic_filter A filter applied to the STS to select only qualifying plans to be loaded. The filter can take the form of any WHERE clause predicate that can specified against the view DBA_SQLSET_STATEMENTS . For example basic_filter => ' sql_text like ''select /*LOAD_STS*/%''' or basic_filter => 'sql_id=''b62q7nc33gzwx''' . fixed Default ' NO ' means the loaded plans are used as non-fixed plans. Value ' YES ' means the loaded plans are used as fixed plans and the SQL plan baseline will not be evolved over time. enabled Default ' YES ' means the loaded plans are enabled for use by the optimizer commit_rows Number of SQL plans to load before doing a periodic commit. This helps to shorten the undo log. Return Values The number of plans loaded Usage Notes To load plans from a remote system, first load the plans into an STS on the remote system, export/import the STS from remote to local system, and then use this function. To load plans from Automatic Workload Repository (AWR), first load the plans stored in AWR snapshots into an STS, and then use this procedure. The user can also capture plans resident in the cursor cache for one or more SQL statements into an STS, and then use this procedure.