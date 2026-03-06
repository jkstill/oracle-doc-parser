---
id: 19c__DBMS_LOGSTDBY.REBUILD
name: DBMS_LOGSTDBY.REBUILD
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_LOGSTDBY
tags: [dbms_logstdby]
source_file: DBMS_LOGSTDBY.html
---

# DBMS_LOGSTDBY.REBUILD

This procedure is used if a database that has recently changed its role to a primary database following a failover operation fails to record relevant metadata (including the LogMiner dictionary) in the redo stream required for other logical standby databases.

## Syntax

```sql
DBMS_LOGSTDBY.REBUILD;
```

## Usage Notes

In a CDB, the REBUILD procedure must be called from the root database. Syntax DBMS_LOGSTDBY.REBUILD; Usage Notes LogMiner dictionary information is logged in the redo log files.The standby redo log files (if present) are archived. Examples SQL> EXECUTE DBMS_LOGSTDBY.REBUILD;