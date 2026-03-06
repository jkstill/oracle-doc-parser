---
id: 19c__DBA_NETWORK_ACLS
name: DBA_NETWORK_ACLS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dba]
source_file: DBA_NETWORK_ACLS.html
---

# DBA_NETWORK_ACLS

DBA_NETWORK_ACLS describes the access control list assignments to network hosts.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| HOST | VARCHAR2(1000) | Network host |
| LOWER_PORT | NUMBER(5) | Lower bound of the port range |
| UPPER_PORT | NUMBER(5) | Upper bound of the port range |
| ACL | VARCHAR2(4000) | Path of the access control list |
| ACLID | RAW(8) | Object ID of the access control list |
| ACL_OWNER | VARCHAR2(128) | Owner of the access control list |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content Note: This DBA_NETWORK_ACLS view is deprecated in Oracle Database 12 c Release 1 (12.1). Oracle recommends that you use the DBA_HOST_ACLS view, instead. Note: This DBA_NETWORK_ACLS view is deprecated in Oracle Database 12 c Release 1 (12.1). Oracle recommends that you use the DBA_HOST_ACLS view, instead. See Also: " DBA_HOST_ACLS " See Also: " DBA_HOST_ACLS "