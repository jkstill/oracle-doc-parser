---
id: 19c__DBMS_SYNC_REFRESH.PREPARE_STAGING_LOG
name: DBMS_SYNC_REFRESH.PREPARE_STAGING_LOG
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_SYNC_REFRESH
tags: [dbms_sync_refresh]
source_file: DBMS_SYNC_REFRESH.html
---

# DBMS_SYNC_REFRESH.PREPARE_STAGING_LOG

This procedure collects statistics on the data in the staging log of the base table and validates the data in the log.

## Syntax

```sql
DBMS_SYNC_REFRESH.PREPARE_STAGING_LOG (
   schema_name      IN VARCHAR2,
   base_table_name  IN VARCHAR2,
   psl_mode         IN NUMBER DEFAULT
   DBMS_SYNC_REFRESH.ENFORCED);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| schema_name | VARCHAR2 | IN | The name of the schema of the base table. |
| base_table_name | VARCHAR2 | IN | The name of the base table. |
| psl_mode | NUMBER | IN | The mode in which staging log preparation should be done. The possible values are: DBMS_SYNC_REFRESH.ENFORCED (the default) DBMS_SYNC_REFRESH.INSERT_TRUSTED DBMS_SYNC_REFRESH.DELETE_TRUSTED DBMS_SYNC_REFRESH.UPDATE_TRUSTED DBMS_SYNC_REFRESH.TRUSTED |

## Usage Notes

It can be run in several different modes ranging from the enforced mode in which strict checking of the data is done to trusted mode in which no checking is done. You should run this procedure after loading the staging log and before running PREPARE_REFRESH . In the enforced mode, which is the default, this procedure will fill in the missing values of the columns of the rows being deleted or updated. An error is thrown if any violations of the staging-log rules are found. You can query the view USER_SR_STLOG_EXCEPTIONS to get details on the exceptions. The notion of the staging log key is described in Oracle Database Data Warehousing Guide. In the enforced mode, this procedure processes each delete/update row in the staging log as follows: It verifies the existence of the row in the base table using the key. For the rows being deleted ( DMLTYPE$$ is 'D' ), it verifies a row with this key exists in the base table; if non-null non-key values are supplied in the staging log, it verifies the values match the corresponding columns in the base table; else an exception is logged in the exceptions table. If the values of any of the non-key columns are missing, it fills in those values from the row in the base table. For the rows being updated ( DMLTYPE$$ is 'UO' or 'UN' ), it verifies a row with this key exists in the base table. In the old values row ( DMLTYPE$$ is 'UO' ), it makes the same check and does the same processing as with rows being deleted. In the new values row ( DMLTYPE$$ is 'UN' ), it checks that at least the value of one the columns differs from its old value; else an exception is logged. In the new values row ( DMLTYPE$$ is 'UN' ), a null value in a column is interpreted as having the same value as the old value of the column except if the old value is non-null and the new value is null in which case, the new value of the column is interpreted as being null. This requires that the user must provide the old value of columns which are being updated to NULL . In the default enforced mode, this procedure verifies that each key is specified for at most once for a delete or update operation. This means that the user, when doing the change consolidation, must consolidate delete-insert of the same row into an update operation with rows 'UO' and 'UN ;' multiple updates must be consolidated into a single update; and null changes such as an insert-update-delete of the same row must not appear in the staging log. The checking done in the enforced mode can be time-consuming. If you are confident in the integrity of the data, you can choose a lower level of checking. You can choose to: trust all the insert rows ( DMLTYPE$$ is 'I') by choosing the psl_mode of DBMS_SYNC_REFRESH.INSERT_TRUSTED trust all the delete rows ( DMLTYPE$$ is 'D' ) by choosing the psl_mode of DBMS_SYNC_REFRESH.DELETE_TRUSTED trust all the update rows ( DMLTYPE$$ is 'UO ' or 'UN' ) by choosing the psl_mode of DBMS_SYNC_REFRESH.UPDATE_TRUSTED trust all three types of DMLs by choosing the psl_mode of DBMS_SYNC_REFRESH.TRUSTED . In addition, you can specify the psl_mode as a bitmask of the flags described above. For example, DBMS_SYNC_REFRESH.INSERT_TRUSTED + DBMS_SYNC_REFRESH_DELETE_TRUSTED will treat inserts and deletes to be trusted but not updates. Syntax DBMS_SYNC_REFRESH.PREPARE_STAGING_LOG ( schema_name IN VARCHAR2, base_table_name IN VARCHAR2, psl_mode IN NUMBER DEFAULT DBMS_SYNC_REFRESH.ENFORCED); Parameters Table 173-10 PREPARE_STAGING_LOG Procedure Parameters Parameter Description schema_name The name of the schema of the base table. base_table_name The name of the base table. psl_mode The mode in which staging log preparation should be done. The possible values are: DBMS_SYNC_REFRESH.ENFORCED (the default) DBMS_SYNC_REFRESH.INSERT_TRUSTED DBMS_SYNC_REFRESH.DELETE_TRUSTED DBMS_SYNC_REFRESH.UPDATE_TRUSTED DBMS_SYNC_REFRESH.TRUSTED