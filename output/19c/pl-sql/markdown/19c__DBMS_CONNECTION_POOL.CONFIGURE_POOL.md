---
id: 19c__DBMS_CONNECTION_POOL.CONFIGURE_POOL
name: DBMS_CONNECTION_POOL.CONFIGURE_POOL
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_CONNECTION_POOL
tags: [dbms_connection_pool]
source_file: DBMS_CONNECTION_POOL.html
---

# DBMS_CONNECTION_POOL.CONFIGURE_POOL

This procedure configures the pool with advanced options.

## Syntax

```sql
DBMS_CONNECTION_POOL.CONFIGURE_POOL (
   pool_name                IN VARCHAR2 DEFAULT 'SYS_DEFAULT_CONNECTION_POOL',
   minsize                  IN NUMBER   DEFAULT 4,
   maxsize                  IN NUMBER   DEFAULT 40,
   incrsize                 IN NUMBER   DEFAULT 2,
   session_cached_cursors   IN NUMBER   DEFAULT 20,
   inactivity_timeout       IN NUMBER   DEFAULT 300,
   max_think_time           IN NUMBER   DEFAULT 120,
   max_use_session          IN NUMBER   DEFAULT 500000,
   max_lifetime_session     IN NUMBER   DEFAULT 86400,
   max_txn_think_time       IN NUMBER);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| pool_name | VARCHAR2 | IN | Pool to be configured. Currently only the default pool name is supported. |
| minsize | NUMBER | IN | Minimum number of pooled servers in the pool |
| maxsize | NUMBER | IN | Maximum allowed pooled servers in the pool |
| incrsize | NUMBER | IN | Pool would increment by this number of pooled server when pooled server are unavailable at application request time |
| session_cached_cursors | NUMBER | IN | Turn on SESSION_CACHED_CURSORS for all connections in the pool. This is an existing init . ora parameter |
| inactivity_timeout | NUMBER | IN | TTL (Time to live) for an idle session in the pool. This parameter helps to shrink the pool when it is not used to its maximum capacity. If a connection remains in the pool idle for this time, it is killed. |
| max_think_time | NUMBER | IN | The maximum time of inactivity, in seconds, for a client after it obtains a pooled server from the pool with no open transactions in it. After obtaining a pooled server from the pool, if the client application does not issue a database call for the time specified by MAX_THINK_TIME, the pooled server is freed and the client connection is terminated. |
| max_use_session | NUMBER | IN | Maximum number of times a connection can be taken and released to the pool |
| max_lifetime_session | NUMBER | IN | TTL (Time to live) for a pooled session |
| max_txn_think_time | NUMBER) | IN | The maximum time of inactivity, in seconds, for a client after it obtains a pooled server from the pool with an open transaction. After obtaining the pooled server from the pool, if the client application does not issue a database call for the time specified by MAX_TXN_THINK_TIME, then the pooled server is freed, and the client connection is terminated. The default value of this parameter is the value of the MAX_THINK_TIME parameter. Applications can set the value of the MAX_TXN_THINK_TIME parameter to a value higher than the MAX_THINK_TIME value to allow more time for the connections with open transactions. |

## Usage Notes

Syntax DBMS_CONNECTION_POOL.CONFIGURE_POOL ( pool_name IN VARCHAR2 DEFAULT 'SYS_DEFAULT_CONNECTION_POOL', minsize IN NUMBER DEFAULT 4, maxsize IN NUMBER DEFAULT 40, incrsize IN NUMBER DEFAULT 2, session_cached_cursors IN NUMBER DEFAULT 20, inactivity_timeout IN NUMBER DEFAULT 300, max_think_time IN NUMBER DEFAULT 120, max_use_session IN NUMBER DEFAULT 500000, max_lifetime_session IN NUMBER DEFAULT 86400, max_txn_think_time IN NUMBER); Parameters Table 39-4 CONFIGURE_POOL Procedure Parameters Parameter Description pool_name Pool to be configured. Currently only the default pool name is supported. minsize Minimum number of pooled servers in the pool maxsize Maximum allowed pooled servers in the pool incrsize Pool would increment by this number of pooled server when pooled server are unavailable at application request time session_cached_cursors Turn on SESSION_CACHED_CURSORS for all connections in the pool. This is an existing init . ora parameter inactivity_timeout TTL (Time to live) for an idle session in the pool. This parameter helps to shrink the pool when it is not used to its maximum capacity. If a connection remains in the pool idle for this time, it is killed. max_think_time The maximum time of inactivity, in seconds, for a client after it obtains a pooled server from the pool with no open transactions in it. After obtaining a pooled server from the pool, if the client application does not issue a database call for the time specified by MAX_THINK_TIME, the pooled server is freed and the client connection is terminated. max_use_session Maximum number of times a connection can be taken and released to the pool max_lifetime_session TTL (Time to live) for a pooled session max_txn_think_time The maximum time of inactivity, in seconds, for a client after it obtains a pooled server from the pool with an open transaction. After obtaining the pooled server from the pool, if the client application does not issue a database call for the time specified by MAX_TXN_THINK_TIME, then the pooled server is freed, and the client connection is terminated. The default value of this parameter is the value of the MAX_THINK_TIME parameter. Applications can set the value of the MAX_TXN_THINK_TIME parameter to a value higher than the MAX_THINK_TIME value to allow more time for the connections with open transactions. Exceptions Table 39-5 CONFIGURE_POOL Procedure Exceptions Exception Description ORA-56500 Connection pool not found ORA-56507 Connection pool alter configuration failed Usage Notes All expressions of time are in seconds All of the parameters should be set based on statistical request patterns. minsize should be set keeping in mind that it puts a lower bound on server resource consumption. This is to prevent the timeout from dragging the pool too low, because of a brief period of inactivity. maxsize should be set keeping in mind that it puts an upper bound on concurrency and response-times and also server resource consumption. session_cached_cursors is typically set to the number of most frequently used statements. It occupies cursor resource on the server In doubt, do not set the increment and inactivity_timeout . The pool will have reasonable defaults. max_use_session and max_lifetime_session allow for software rejuvenation or defensive approaches to potential bugs, leaks, accumulations, and like problems, by getting brand new sessions once in a while. The connection pool reserves 5% of the pooled servers for authentication, and at least one pooled server is always reserved for authentication. When setting the maxsize parameter, ensure that there are enough pooled servers for both authentication and connections.