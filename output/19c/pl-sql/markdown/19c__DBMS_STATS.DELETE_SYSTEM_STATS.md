---
id: 19c__DBMS_STATS.DELETE_SYSTEM_STATS
name: DBMS_STATS.DELETE_SYSTEM_STATS
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_STATS
tags: [dbms_stats]
source_file: DBMS_STATS.html
---

# DBMS_STATS.DELETE_SYSTEM_STATS

This procedure deletes workload statistics (collected using the ' INTERVAL ' or ' START ' and ' STOP ' options) and resets the default to noworkload statistics (collected using ' NOWORKLOAD ' option), if stattab is not specified. If stattab is specified, the subprogram deletes all system statistics with the associated statid from the stattab .

## Syntax

```sql
DBMS_STATS.DELETE_SYSTEM_STATS (
   stattab       VARCHAR2 DEFAULT NULL, 
   statid        VARCHAR2 DEFAULT NULL,
   statown       VARCHAR2 DEFAULT NULL);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| stattab | VARCHAR2 | IN | Identifier of the user statistics table where the statistics will be saved |
| statid | VARCHAR2 | IN | Optional identifier associated with the statistics saved in the stattab |
| statown | VARCHAR2 | IN | Schema containing stattab (if different from current schema) |

## Usage Notes

Syntax DBMS_STATS.DELETE_SYSTEM_STATS ( stattab VARCHAR2 DEFAULT NULL, statid VARCHAR2 DEFAULT NULL, statown VARCHAR2 DEFAULT NULL); Parameters Table 171-29 DELETE_SYSTEM_STATS Procedure Parameters Parameter Description stattab Identifier of the user statistics table where the statistics will be saved statid Optional identifier associated with the statistics saved in the stattab statown Schema containing stattab (if different from current schema) Exceptions ORA-20000 : Object does not exist or insufficient privileges ORA-20002 : Bad user statistics table; may need to be upgraded Usage Notes To run this procedure, you need the GATHER_SYSTEM_STATISTICS role.