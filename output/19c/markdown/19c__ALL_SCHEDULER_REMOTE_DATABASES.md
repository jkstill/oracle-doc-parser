---
id: 19c__ALL_SCHEDULER_REMOTE_DATABASES
name: ALL_SCHEDULER_REMOTE_DATABASES
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [all]
source_file: ALL_SCHEDULER_REMOTE_DATABASES.html
---

# ALL_SCHEDULER_REMOTE_DATABASES

ALL_SCHEDULER_REMOTE_DATABASES displays information about the remote databases accessible to the current user that have been registered as sources and destinations for remote database jobs.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| DATABASE_NAME | VARCHAR2(512) | Global name of the remote database |
| REGISTERED_AS | VARCHAR2(11) | Indicates whether the database is registered as a source ( SOURCE ) or as a destination ( DESTINATION ) |
| DATABASE_LINK | VARCHAR2(512) | Name of a valid database link to the remote database |

## Usage Notes

Related View DBA_SCHEDULER_REMOTE_DATABASES displays information about all remote databases that have been registered as sources and destinations for remote database jobs. See Also: " DBA_SCHEDULER_REMOTE_DATABASES " See Also: " DBA_SCHEDULER_REMOTE_DATABASES "