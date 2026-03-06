---
id: 19c__V$DBLINK
name: V$DBLINK
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dynamic_performance]
source_file: V-DBLINK.html
---

# V$DBLINK

V$DBLINK describes all database links (links with IN_TRANSACTION = YES ) opened by the session issuing the query on V$DBLINK . These database links must be committed or rolled back before being closed.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| DB_LINK | VARCHAR2(128) |  |
| OWNER_ID | NUMBER |  |
| LOGGED_ON | VARCHAR2(3) |  |
| HETEROGENEOUS | VARCHAR2(3) |  |
| PROTOCOL | VARCHAR2(6) |  |
| OPEN_CURSORS | NUMBER |  |
| IN_TRANSACTION | VARCHAR2(3) |  |
| UPDATE_SENT | VARCHAR2(3) |  |
| COMMIT_POINT_STRENGTH | NUMBER |  |
| CON_ID | NUMBER |  |