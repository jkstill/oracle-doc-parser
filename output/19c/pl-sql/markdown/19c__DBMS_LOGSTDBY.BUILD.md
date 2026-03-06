---
id: 19c__DBMS_LOGSTDBY.BUILD
name: DBMS_LOGSTDBY.BUILD
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_LOGSTDBY
tags: [dbms_logstdby]
source_file: DBMS_LOGSTDBY.html
---

# DBMS_LOGSTDBY.BUILD

Use this procedure on the primary database to record relevant metadata (LogMiner dictionary) information in the redo log, which will subsequently be used by SQL Apply. This procedure will enable database-wide primary- and unique-key supplemental logging, if necessary.

## Syntax

```sql
SQL>  ALTER DATABASE ADD SUPPLEMENTAL LOG DATA (PRIMARY KEY, UNIQUE INDEX) COLUMNS;
```

## Usage Notes

In a CDB, the BUILD procedure must be called from the root database on the primary. Additionally, you cannot add or remove PDBs from a CDB while this procedure is executing. Note: In databases created using Oracle Database 11 g release 2 (11.2) or later, supplemental logging information is automatically propagated to any existing physical standby databases. However, for databases in earlier releases, or if the database was created using an earlier release and then upgraded to 11.2, you must check whether supplemental logging is enabled at the physical standby(s) if it is also enabled at the primary database. If it is not enabled at the physical standby(s), then before performing a switchover or failover, you must enable supplemental logging on all existing physical standby databases. To do so, issue the following SQL command on each physical standby: SQL> ALTER DATABASE ADD SUPPLEMENTAL LOG DATA (PRIMARY KEY, UNIQUE INDEX) COLUMNS; If you do not do this, then any logical standby that is also in the same Data Guard configuration will be unusable if a switchover or failover is performed to one of the physical standby databases. If a switchover or failover has already occurred and supplemental logging was not enabled, then you must recreate all logical standby databases. Note: In databases created using Oracle Database 11 g release 2 (11.2) or later, supplemental logging information is automatically propagated to any existing physical standby databases. However, for databases in earlier releases, or if the database was created using an earlier release and then upgraded to 11.2, you must check whether supplemental logging is enabled at the physical standby(s) if it is also enabled at the primary database. If it is not enabled at the physical standby(s), then before performing a switchover or failover, you must enable supplemental logging on all existing physical standby databases. To do so, issue the following SQL command on each physical standby: SQL> ALTER DATABASE ADD SUPPLEMENTAL LOG DATA (PRIMARY KEY, UNIQUE INDEX) COLUMNS; If you do not do this, then any logical standby that is also in the same Data Guard configuration will be unusable if a switchover or failover is performed to one of the physical standby databases. If a switchover or failover has already occurred and supplemental logging was not enabled, then you must recreate all logical standby databases. Syntax DBMS_LOGSTDBY.BUILD; Usage Notes Supplemental log information includes extra information in the redo logs that uniquely identifies a modified row in the logical standby database, and also includes information that helps efficient application of changes to the logical standby database. LogMiner dictionary information allows SQL Apply to interpret data in the redo logs. DBMS_LOGSTDBY.BUILD should be run only once for each logical standby database you want to create. You do not need to use DBMS_LOGSTDBY.BUILD for each Oracle RAC instance. DBMS_LOGSTDBY.BUILD waits for all transactions (including distributed transactions) that are active at the time of the procedure invocation to complete before returning. See Oracle Database Administrator's Guide for information about how to handle in-doubt transactions. Examples To build the LogMiner dictionary in the redo stream of the primary database and to record additional information so that a logical standby database can be instantiated, issue the following SQL statement at the primary database SQL> EXECUTE DBMS_LOGSTDBY.BUILD;