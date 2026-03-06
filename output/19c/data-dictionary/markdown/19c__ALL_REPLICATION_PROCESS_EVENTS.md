---
id: 19c__ALL_REPLICATION_PROCESS_EVENTS
name: ALL_REPLICATION_PROCESS_EVENTS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [all]
source_file: ALL_REPLICATION_PROCESS_EVENTS.html
---

# ALL_REPLICATION_PROCESS_EVENTS

ALL_REPLICATION_PROCESS_EVENTS provides information about the replication processes events accessible to the current user.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| STREAMS_TYPE | VARCHAR2(10) | Streams type: XStream GoldenGate |
| PROCESS_TYPE | VARCHAR2(27) | Process type: Capture Capture server Apply Coordinator Apply Server Apply Network Receiver Apply Reader Apply Hash server |
| STREAMS_NAME | VARCHAR2(128) | Streams name |
| EVENT_NAME | VARCHAR2(128) | Event name: START STOP ABORT CREATE DROP PARAMETER CHANGE HANDLER CREATE HANDLER REMOVE ALTER |
| DESCRIPTION | VARCHAR2(2000) | Event description |
| EVENT_TIME | TIMESTAMP(6) | Time when the event occurred |
| ERROR_NUMBER | NUMBER | Error number (valid when event is Error) |
| ERROR_MESSAGE | VARCHAR2(2000) | Error Message (valid when event is an error) |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content Related View DBA_REPLICATION_PROCESS_EVENTS provides information about the replication processes events in the database. See Also: " DBA_REPLICATION_PROCESS_EVENTS " See Also: " DBA_REPLICATION_PROCESS_EVENTS "