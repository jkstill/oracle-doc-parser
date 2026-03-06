---
id: 19c__DBA_ADVISOR_DEFINITIONS
name: DBA_ADVISOR_DEFINITIONS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: configuration
tags: [dba]
source_file: DBA_ADVISOR_DEFINITIONS.html
---

# DBA_ADVISOR_DEFINITIONS

DBA_ADVISOR_DEFINITIONS displays the properties of all advisors in the database.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| ADVISOR_ID | NUMBER | Unique identifier for the advisor |
| ADVISOR_NAME | VARCHAR2(128) | Name of the advisor |
| PROPERTY | NUMBER | Properties: Bit 0: - Indicates whether the advisor runs in COMPREHENSIVE mode ( 1 ) or not ( 0 ) Bit 1: - Indicates whether the advisor runs in LIMITED mode ( 1 ) or not ( 0 ) Bit 2: - Indicates whether the advisor is resumable ( 1 ) or not ( 0 ) Bit 3: - Indicates whether the advisor accepts user directives ( 1 ) or not ( 0 ) |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content The view contains one row for each task, representing the current state of the task as well as execution-specific data such as progress monitoring and completion status.