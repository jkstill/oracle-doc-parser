---
id: 19c__DBMS_LOGSTDBY.MAP_PRIMARY_SCN
name: DBMS_LOGSTDBY.MAP_PRIMARY_SCN
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_LOGSTDBY
tags: [dbms_logstdby]
source_file: DBMS_LOGSTDBY.html
---

# DBMS_LOGSTDBY.MAP_PRIMARY_SCN

This function returns an SCN on the standby that predates the supplied SCN from the primary database by at least 5 minutes.

## Syntax

```sql
DBMS_LOGSTDBY.MAP_PRIMARY_SCN(primary_scn NUMBER) RETURN NUMBER;
```

**Returns:** `NUMBER`

## Usage Notes

It can be used to determine a safe SCN to use in a compensating flashback database operation at the logical standby database, following a flashback database operation or a point-in-time recovery operation at the primary database. Syntax DBMS_LOGSTDBY.MAP_PRIMARY_SCN(primary_scn NUMBER) RETURN NUMBER; Exceptions Table 102-8 MAP_PRIMARY_SCN Function Exceptions Exception Description ORA-20001 Primary SCN is before mapped range ORA-20002 SCN mapping requires PRESERVE_COMMIT_ORDER to be TRUE Usage Notes Use this function to get a conservative SCN at the logical standby database that corresponds to an SCN at the primary database. This function is useful in the context of doing compensating flashback database operations at the logical standby following a flashback database or a point-in-time recovery operation done at the primary database.