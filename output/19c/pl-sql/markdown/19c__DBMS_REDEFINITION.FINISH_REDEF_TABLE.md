---
id: 19c__DBMS_REDEFINITION.FINISH_REDEF_TABLE
name: DBMS_REDEFINITION.FINISH_REDEF_TABLE
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_REDEFINITION
tags: [dbms_redefinition]
source_file: DBMS_REDEFINITION.html
---

# DBMS_REDEFINITION.FINISH_REDEF_TABLE

This procedure completes the redefinition process.

## Syntax

```sql
DBMS_REDEFINITION.FINISH_REDEF_TABLE (
   uname                   IN   VARCHAR2,
   orig_table              IN   VARCHAR2,
   int_table               IN   VARCHAR2,
   part_name               IN   VARCHAR2 := NULL,
   dml_lock_timeout        IN   PLS_INTEGER := NULL,
   continue_after_errors   IN   BOOLEAN := FALSE,
   disable_rollback        IN   PLS_INTEGER := FALSE);
```

## Usage Notes

Before this step, you can create new indexes, triggers, grants, and constraints on the interim table. The referential constraints involving the interim table must be disabled. After completing this step, the original table is redefined with the attributes and data of the interim table. The original table is locked briefly during this procedure. Syntax DBMS_REDEFINITION.FINISH_REDEF_TABLE ( uname IN VARCHAR2, orig_table IN VARCHAR2, int_table IN VARCHAR2, part_name IN VARCHAR2 := NULL, dml_lock_timeout IN PLS_INTEGER := NULL, continue_after_errors IN BOOLEAN := FALSE, disable_rollback IN PLS_INTEGER := FALSE); Parameters Table 138-9 FINISH_REDEF_TABLE Procedure Parameters Parameters Description uname Schema name of the tables orig_table Name of the table to be redefined int_table Name of the interim table. Can take a comma-delimited list of interim table names. part_name Name of the partition being redefined. If redefining only a single partition of a table, specify the partition name in this parameter. NULL implies the entire table is being redefined. Can take a comma-delimited list of partition names to be redefined. dml_lock_timeout Specifies the number of seconds the procedure waits for its required locks before failing. The permissible range of values for timeout is 0 to 1,000,000. The default is NULL (wait mode). continue_after_errors When redefining multiple partitions allows operation execution to continue on the next partition (applies only to batched partition redefinition). disable_rollback When set to TRUE , disables the rollback option if it was enabled in the START_REDEF_TABLE procedure. Specifying TRUE cleans up the database objects that enable rollback. Examples Wait up to 600 seconds for required locks on SH.SALES : EXECUTE DBMS_REDEFINITION.FINISH_REDEF_TABLE ( 'SH', 'SALES', 'INT_SALES', 600);