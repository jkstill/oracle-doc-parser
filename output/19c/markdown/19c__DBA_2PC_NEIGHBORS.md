---
id: 19c__DBA_2PC_NEIGHBORS
name: DBA_2PC_NEIGHBORS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dba]
source_file: DBA_2PC_NEIGHBORS.html
---

# DBA_2PC_NEIGHBORS

DBA_2PC_NEIGHBORS describes incoming and outgoing connections for pending transactions.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| LOCAL_TRAN_ID | VARCHAR2(22) | Local identifier of a transaction |
| IN_OUT | VARCHAR2(3) | IN for incoming connections, OUT for outgoing |
| DATABASE | VARCHAR2(128) | IN for client database name, OUT for outgoing database link |
| DBUSER_OWNER | VARCHAR2(128) | IN for name of local user, OUT for owner of database link |
| INTERFACE | VARCHAR2(1) | C for request commit, otherwise N for prepare or request read only commit |
| DBID | VARCHAR2(16) | Database ID at the other end of the connection |
| SESS# | NUMBER(38) | Session number of the connection at this database |
| BRANCH | VARCHAR2(128) | Transaction branch ID of the connection at this database |