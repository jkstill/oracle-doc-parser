---
id: 19c__V$GOLDENGATE_TRANSACTION
name: V$GOLDENGATE_TRANSACTION
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dynamic_performance]
source_file: V-GOLDENGATE_TRANSACTION.html
---

# V$GOLDENGATE_TRANSACTION

V$GOLDENGATE_TRANSACTION displays information about transactions that are being processed by Oracle GoldenGate capture processes, outbound servers, and inbound servers.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| COMPONENT_NAME | VARCHAR2(138) |  |
| COMPONENT_TYPE | VARCHAR2(20) |  |
| XIDUSN | NUMBER |  |
| XIDSLT | NUMBER |  |
| XIDSQN | NUMBER |  |
| BATCH_XIDUSN | NUMBER |  |
| BATCH_XIDSLT | NUMBER |  |
| BATCH_XIDSQN | NUMBER |  |
| CUMULATIVE_MESSAGE_COUNT | NUMBER |  |
| TOTAL_MESSAGE_COUNT | NUMBER |  |
| FIRST_MESSAGE_TIME | DATE |  |
| FIRST_MESSAGE_NUMBER | NUMBER |  |
| LAST_MESSAGE_TIME | DATE |  |
| LAST_MESSAGE_NUMBER | NUMBER |  |
| FIRST_MESSAGE_POSITION | RAW(64) |  |
| LAST_MESSAGE_POSITION | RAW(64) |  |
| TRANSACTION_ID | VARCHAR2(128) |  |
| CON_ID | NUMBER |  |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content This view can identify long running transactions and display how many LCRs are being processed in each transaction. This view only contains information about captured LCRs. It does not contain information about user-enqueued LCRs or user messages. This view only shows information about LCRs that are being processed because they satisfied the rule sets for the component at the time of the query. For capture processes, this view only shows information about changes in transactions that the capture process has converted into LCRs. It does not show information about all the active transactions present in the redo log. For outbound servers, this view only shows information about LCRs that the outbound server has dequeued. It does not show information about LCRs in the outbound server's queue. For outbound servers, information about a transaction remains in the view until the transaction is sent to the Oracle GoldenGate client application. For inbound servers, information about a transaction remains in the view until the transaction commits or until the entire transaction is rolled back.