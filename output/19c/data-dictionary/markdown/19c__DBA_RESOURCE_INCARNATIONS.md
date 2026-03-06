---
id: 19c__DBA_RESOURCE_INCARNATIONS
name: DBA_RESOURCE_INCARNATIONS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dba]
source_file: DBA_RESOURCE_INCARNATIONS.html
---

# DBA_RESOURCE_INCARNATIONS

DBA_RESOURCE_INCARNATIONS lists all resource incarnations that are running or eligible for HA status notification.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| RESOURCE_TYPE | VARCHAR2(30) | Type of resource |
| RESOURCE_NAME | VARCHAR2(256) | Name of resource |
| DB_UNIQUE_NAME | VARCHAR2(30) | Database unique name |
| DB_DOMAIN | VARCHAR2(128) | Database domain |
| INSTANCE_NAME | VARCHAR2(30) | Name of instance at which resource is located |
| HOST_NAME | V ARCHAR2(512) | Name of host at which resource is located |
| STARTUP_TIME | TIMESTAMP(9) WITH TIME ZONE | Resource startup date and time |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content