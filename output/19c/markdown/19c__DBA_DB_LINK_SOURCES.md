---
id: 19c__DBA_DB_LINK_SOURCES
name: DBA_DB_LINK_SOURCES
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dba]
source_file: DBA_DB_LINK_SOURCES.html
---

# DBA_DB_LINK_SOURCES

DBA_DB_LINK_SOURCES identifies all unique source databases that opened database links to the local database.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| SOURCE_ID | NUMBER | Unique ID that identifies an incoming database link |
| DB_NAME | VARCHAR2(256) | Global name of the source database |
| DBID | NUMBER | Database identifier of the source database. Maps to the DBID of the source database in V$DATABASE . |
| DB_UNIQUE_NAME | VARCHAR2(256) | Unique database name of the source database. Maps to the DB_UNIQUE_NAME of the source database in V$DATABASE . Null for source databases that do not provide this information. |
| HOST_NAME | VARCHAR2(256) | Resolved host name. Null if not available. |
| IP_ADDRESS | VARCHAR2(128) | IP address of source machine. Null if not available. |
| PROTOCOL | VARCHAR2(64) | One of supported protocols such as ipc , sdp , tcp , or tcps . Null if not available. |
| USERNAME | VARCHAR2(128) | Oracle username of the user who logged into the local database. Maps to the USERNAME column in V$SESSION . |
| USER# | NUMBER | Oracle user id of the user who logged into the local database. Maps to the USER# column in V$SESSION . |
| FIRST_LOGON_TIME | TIMESTAMP(6) | The timestamp of the first connection on this database link in UTC |
| LAST_LOGON_TIME | TIMESTAMP(6) | The timestamp of the last connection on this database link in UTC |
| LOGON_COUNT | NUMBER | Number of times connection has been established through this database link |

## Usage Notes

By default, only a DBA has access to this view. However, a DBA can grant access to this view to others. This view is based on a persistent table that resides in the same system tablespace that is used by Database Auditing. In a multitenant container database (CDB) environment, for every DBA_ view, there is a corresponding CDB_ view that contains data for all the pluggable databases (PDBs) in the CDB. A query on the CDB_DB_LINK_SOURCES view done in the CDB$ROOT container will show sources of all the database links recorded in all PDBs. A query on the corresponding DBA_DB_LINK_SOURCES view done in a PDB show information corresponding to that PDB only (that is, where that specific PDB was the target of an inbound database link). Note that the CDB_ views would only show data from PDBs that are open at the time the query is issued. Therefore, when you are diagnosing sources of database links, Oracle recommends that you keep open any or all PDBs that might contain useful information for the diagnosis. See Also: " V$DATABASE " " V$SESSION " " DBA_EXTERNAL_SCN_ACTIVITY " " DBA_DB_LINKS " See Also: " V$DATABASE " " V$SESSION " " DBA_EXTERNAL_SCN_ACTIVITY " " DBA_DB_LINKS "