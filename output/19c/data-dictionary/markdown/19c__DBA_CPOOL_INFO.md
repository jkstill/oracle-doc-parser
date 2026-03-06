---
id: 19c__DBA_CPOOL_INFO
name: DBA_CPOOL_INFO
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dba]
source_file: DBA_CPOOL_INFO.html
---

# DBA_CPOOL_INFO

DBA_CPOOL_INFO displays configuration information about all Database Resident Connection Pools in the database.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| CONNECTION_POOL | VARCHAR2(128) | Name of the connection pool |
| STATUS | VARCHAR2(16) | Status of the pool: ACTIVE INACTIVE |
| MINSIZE | NUMBER | Minimum number of pooled servers that are always alive in the pool |
| MAXSIZE | NUMBER | Maximum number of pooled servers in the pool |
| INCRSIZE | NUMBER | Number of pooled servers by which the pool is incremented if servers are unavailable when a client application request is received |
| SESSION_CACHED_CURSORS | NUMBER | Number of session cursors to cache in each pooled server |
| INACTIVITY_TIMEOUT | NUMBER | Maximum time (in seconds) that the pooled server can stay idle in the pool. After this time, the server is terminated. |
| MAX_THINK_TIME | NUMBER | Maximum time of inactivity (in seconds) for a client after obtaining a pooled server from the pool. After obtaining a pooled server from the pool, if the client application does not issue a database call for the time specified by this column, then the pooled server is freed and the client connection is terminated. |
| MAX_USE_SESSION | NUMBER | Number of times a pooled server can be taken and released to the pool |
| MAX_LIFETIME_SESSION | NUMBER | Time (in seconds) for a pooled server to live in the pool |
| NUM_CBROK | NUMBER | Number of connection brokers spawned per instance |
| MAXCONN_CBROK | NUMBER | Maximum number of connections per connection broker |
| MAX_TXN_THINK_TIME | NUMBER | Maximum time of inactivity (in seconds) for a client after it obtains a pooled server from the pool and starts a transaction. If the client application does not issue a database call for the time specified by MAX_TXN_THINK_TIME while in a transaction, the pooled server is freed, the transaction is rolled back, and the client connection is terminated. The default value is 0 , which means MAX_THINK_TIME applies for all connections, irrespective of transactions being open or not in those connections. Care should be taken while setting the two parameters MAX_THINK_TIME and MAX_TXN_THINK_TIME to higher values, as it would mean the servers are not released to the pool for a longer time, even if clients are not responding for any reason, thereby making other users wait unnecessarily. |
| CON_ID | NUMBER | The ID of the container to which the data pertains. Possible values include: 0 : This value is used for rows containing data that pertain to the entire multitenant container database (CDB). This value is also used for rows in non-CDBs. 1 : This value is used for rows containing data that pertain to only the root n : Where n is the applicable container ID for the rows containing data |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content See Also: Oracle Database Administrator’s Guide for more information about the configuration parameters for Database Resident Connection Pooling Oracle Database PL/SQL Packages and Types Reference for more information on the DBMS_CONNECTION_POOL package See Also: Oracle Database Administrator’s Guide for more information about the configuration parameters for Database Resident Connection Pooling Oracle Database PL/SQL Packages and Types Reference for more information on the DBMS_CONNECTION_POOL package