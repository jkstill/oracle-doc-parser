---
id: 19c__V$AQ_NONDUR_REGISTRATIONS
name: V$AQ_NONDUR_REGISTRATIONS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dynamic_performance]
source_file: V-AQ_NONDUR_REGISTRATIONS.html
---

# V$AQ_NONDUR_REGISTRATIONS

V$AQ_NONDUR_REGISTRATIONS provides information about non-durable subscriptions.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| REG_ID | NUMBER |  |
| SUBSCRIPTION | VARCHAR2(128) |  |
| LOCATION | VARCHAR2(256) |  |
| USER# | NUMBER |  |
| USER_CONTEXT | RAW(32) |  |
| CONTEXT_SIZE | NUMBER |  |
| NAMESPACE | NUMBER |  |
| VERSION | NUMBER |  |
| STATE | NUMBER |  |
| QOS | NUMBER |  |
| REG_TIME | TIMESTAMP(3) WITH TIME ZONE |  |
| CON_ID | NUMBER |  |

## Usage Notes

See Also: Oracle Database Advanced Queuing User's Guide for more information about Oracle Database Advanced Queueing See Also: Oracle Database Advanced Queuing User's Guide for more information about Oracle Database Advanced Queueing