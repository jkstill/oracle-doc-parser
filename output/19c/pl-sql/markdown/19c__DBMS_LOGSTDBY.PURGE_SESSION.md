---
id: 19c__DBMS_LOGSTDBY.PURGE_SESSION
name: DBMS_LOGSTDBY.PURGE_SESSION
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_LOGSTDBY
tags: [dbms_logstdby]
source_file: DBMS_LOGSTDBY.html
---

# DBMS_LOGSTDBY.PURGE_SESSION

PURGE_SESSION identifies all archived redo log files that have been applied to the logical standby database and are no longer needed by SQL Apply.

## Syntax

```sql
DBMS_LOGSTDBY.PURGE_SESSION;
```

## Usage Notes

Once identified, you can issue operating system commands to delete some or all of the unnecessary archived redo log files. In a CDB, the PURGE_SESSION procedure must be called from the root database. Syntax DBMS_LOGSTDBY.PURGE_SESSION; Exceptions Table 102-11 PURGE_SESSION Procedure Exceptions Exception Description ORA-01309 Invalid session Usage Notes This procedure does not delete the archived redo log files. You must issue operating system commands to delete unneeded files. This procedure updates the DBA_LOGMNR_PURGED_LOG view that displays the archived redo log files that have been applied to the logical standby database. In Oracle Database 10 g Release 2, metadata related to the archived redo log files (and the actual archived redo log files) are purged automatically based on the default setting of the LOG_AUTO_DELETE parameter described in the DBMS_LOGSTDBY.APPLY_SET procedure described. Example To identify and remove unnecessary files: Enter the following statement on the logical standby database: SQL> EXECUTE DBMS_LOGSTDBY.PURGE_SESSION; Query the DBA_LOGMNR_PURGED_LOG view to list the archived redo log files that can be removed: SQL> SELECT * FROM DBA_LOGMNR_PURGED_LOG; FILE_NAME ------------------------------------ /boston/arc_dest/arc_1_40_509538672.log /boston/arc_dest/arc_1_41_509538672.log /boston/arc_dest/arc_1_42_509538672.log /boston/arc_dest/arc_1_43_509538672.log /boston/arc_dest/arc_1_44_509538672.log /boston/arc_dest/arc_1_45_509538672.log /boston/arc_dest/arc_1_46_509538672.log /boston/arc_dest/arc_1_47_509538672.log Use operating system-specific commands to delete archived redo log files from the file system.