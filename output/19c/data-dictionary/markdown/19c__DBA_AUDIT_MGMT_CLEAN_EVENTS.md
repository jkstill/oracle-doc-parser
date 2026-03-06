---
id: 19c__DBA_AUDIT_MGMT_CLEAN_EVENTS
name: DBA_AUDIT_MGMT_CLEAN_EVENTS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: auditing
tags: [dba]
source_file: DBA_AUDIT_MGMT_CLEAN_EVENTS.html
---

# DBA_AUDIT_MGMT_CLEAN_EVENTS

DBA_AUDIT_MGMT_CLEAN_EVENTS displays information about the history of audit trail cleanup or purge events.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| AUDIT_TRAIL | VARCHAR2(28) | Audit trail that was cleaned at the time of the event: STANDARD AUDIT TRAIL FGA AUDIT TRAIL STANDARD AND FGA AUDIT TRAIL OS AUDIT TRAIL XML AUDIT TRAIL OS AND XML AUDIT TRAIL ALL AUDIT TRAILS |
| RAC_INSTANCE | NUMBER | Instance number indicating the Oracle RAC instance that was cleaned up at the time of the event; 0 implies not applicable |
| CLEANUP_TIME | TIMESTAMP(6) WITH TIME ZONE | Timestamp when the cleanup event completed |
| DELETE_COUNT | NUMBER | Number of audit records or audit files that were deleted at the time of the event |
| WAS_FORCED | VARCHAR2(3) | Indicates whether a forced cleanup occurred ( YES ) or not ( NO ); forced cleanup bypasses the last archive timestamp set |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content Periodically, you should delete the contents of this view so that it will not grow too large. Note: This view is intended for use with traditional auditing (pre-Oracle Database 12c auditing) only, not for unified auditing. See Oracle Database Security Guide for more information about unified auditing. See Oracle Database Upgrade Guide for more information about migrating to unified auditing. Note: This view is intended for use with traditional auditing (pre-Oracle Database 12c auditing) only, not for unified auditing. See Oracle Database Security Guide for more information about unified auditing. See Oracle Database Upgrade Guide for more information about migrating to unified auditing. Note: In a read-only database, including an Oracle Active Data Guard physical standby database, this view is not populated. Instead, a summary of cleanup events is written to the respective database instance's alert log file. Note: In a read-only database, including an Oracle Active Data Guard physical standby database, this view is not populated. Instead, a summary of cleanup events is written to the respective database instance's alert log file.