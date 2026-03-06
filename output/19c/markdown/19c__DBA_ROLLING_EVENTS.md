---
id: 19c__DBA_ROLLING_EVENTS
name: DBA_ROLLING_EVENTS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dba]
source_file: DBA_ROLLING_EVENTS.html
---

# DBA_ROLLING_EVENTS

DBA_ROLLING_EVENTS lists all the events reported from the DBMS_ROLLING PL/SQL package.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| EVENTID | NUMBER | Event identifier which identifies event order |
| EVENT_TIME | TIMESTAMP(6) | Time associated with the event |
| TYPE | VARCHAR2(7) | Type of event: INFO , NOTICE , WARNING , or ERROR |
| MESSAGE | VARCHAR2(256) | Text describing the event details |
| STATUS | NUMBER | Status code associated with an event |
| INSTID | NUMBER | Instruction ID associated with an event |
| REVISION | NUMBER | Plan revision number associated with an event |

## Usage Notes

See Also: Oracle Data Guard Concepts and Administration for more information about rolling operations. Oracle Database PL/SQL Packages and Types Reference for more information about the DBMS_ROLLING package See Also: Oracle Data Guard Concepts and Administration for more information about rolling operations. Oracle Database PL/SQL Packages and Types Reference for more information about the DBMS_ROLLING package