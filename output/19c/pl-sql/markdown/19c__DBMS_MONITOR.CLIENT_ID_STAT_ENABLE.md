---
id: 19c__DBMS_MONITOR.CLIENT_ID_STAT_ENABLE
name: DBMS_MONITOR.CLIENT_ID_STAT_ENABLE
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_MONITOR
tags: [dbms_monitor]
source_file: DBMS_MONITOR.html
---

# DBMS_MONITOR.CLIENT_ID_STAT_ENABLE

This procedure enables statistic gathering for a given Client Identifier.

## Syntax

```sql
DBMS_MONITOR.CLIENT_ID_STAT_ENABLE(
   client_id            IN   VARCHAR2);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| client_id | VARCHAR2) | IN | Client Identifier for which statistic aggregation is enabled |

## Usage Notes

Statistics gathering is global for the database and persistent across instance starts and restarts. That is, statistics are enabled for all instances of the same database, including restarts. Statistics are viewable through V$CLIENT_STATS views. Syntax DBMS_MONITOR.CLIENT_ID_STAT_ENABLE( client_id IN VARCHAR2); Parameters Table 112-3 CLIENT_ID_STAT_ENABLE Procedure Parameters Parameter Description client_id Client Identifier for which statistic aggregation is enabled Examples To enable statistic accumulation for a client with a given client ID: EXECUTE DBMS_MONITOR.CLIENT_ID_STAT_ENABLE('janedoe');