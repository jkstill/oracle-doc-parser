---
id: 19c__V$ASM_QUOTAGROUP
name: V$ASM_QUOTAGROUP
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dynamic_performance]
source_file: V-ASM_QUOTAGROUP.html
---

# V$ASM_QUOTAGROUP

V$ASM_QUOTAGROUP displays one row for every Oracle Automatic Storage Management (Oracle ASM) quota group discovered by the Oracle ASM instance on the node.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| GROUP_NUMBER | NUMBER |  |
| QUOTAGROUP_NUMBER | NUMBER |  |
| INCARNATION | NUMBER |  |
| NAME | VARCHAR2(30) |  |
| USED_QUOTA_MB | NUMBER |  |
| QUOTA_LIMIT_MB | NUMBER |  |
| CON_ID | NUMBER |  |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content