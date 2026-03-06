---
id: 19c__ALL_APPLY_REPERROR_HANDLERS
name: ALL_APPLY_REPERROR_HANDLERS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [all]
source_file: ALL_APPLY_REPERROR_HANDLERS.html
---

# ALL_APPLY_REPERROR_HANDLERS

ALL_APPLY_REPERROR_HANDLERS provides details about apply reperror handlers on objects visible to the user.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| APPLY_NAME | VARCHAR2(128) | Name of the apply process |
| OBJECT_OWNER | VARCHAR2(128) | Owner of the object |
| OBJECT_NAME | VARCHAR2(128) | Name of the object |
| SOURCE_OBJECT_OWNER | VARCHAR2(128) | Source database owner of the source object |
| SOURCE_OBJECT_NAME | VARCHAR2(128) | Source database name of the object |
| ERROR_NUMBER | NUMBER | Error number for the handler |
| METHOD | VARCHAR2(18) | Error handling method: ABEND RECORD IGNORE RETRY RETRY_TRANSACTION RECORD_TRANSACTION |
| MAX_RETRIES | NUMBER | Maximum number of times to retry for the method RETRY and RETRY_TRANSACTION |
| DELAY_CSECS | NUMBER | Number of centiseconds to wait between retries for RETRY and RETRY_TRANSACTION |
| SET_BY | VARCHAR2(10) | Entity that set up the handler: USER GOLDENGATE |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content Related View DBA_APPLY_REPERROR_HANDLERS provides details about apply reperror handlers. See Also: " DBA_APPLY_REPERROR_HANDLERS " See Also: " DBA_APPLY_REPERROR_HANDLERS "