---
id: 19c__DBA_NETWORK_ACL_PRIVILEGES
name: DBA_NETWORK_ACL_PRIVILEGES
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: security
tags: [dba]
source_file: DBA_NETWORK_ACL_PRIVILEGES.html
---

# DBA_NETWORK_ACL_PRIVILEGES

DBA_NETWORK_ACL_PRIVILEGES describes the network privileges defined in all access control lists that are currently assigned to network hosts.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| ACL | VARCHAR2(4000) | Path of the access control list |
| ACLID | RAW(8) | Object ID of the access control list |
| PRINCIPAL | VARCHAR2(128) | Principal (database user or role) whom the privilege is granted to or denied from |
| PRIVILEGE | VARCHAR2(128) | Network privilege |
| IS_GRANT | VARCHAR2(5) | Indicates whether the privilege is granted ( true ) or denied ( false ) |
| INVERT | VARCHAR2(5) | Indicates whether the access control entry contains invert principal ( true ) or not ( false ) |
| START_DATE | TIMESTAMP(6) | Start date of the access control entry |
| END_DATE | TIMESTAMP(6) | End date of the access control entry |
| ACL_OWNER | VARCHAR2(128) | Owner of the access control list |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content Note: This DBA_NETWORK_ACL_PRIVILEGES view is deprecated in Oracle Database 12 c Release 1 (12.1). Oracle recommends that you use the DBA_HOST_ACES view, instead. Note: This DBA_NETWORK_ACL_PRIVILEGES view is deprecated in Oracle Database 12 c Release 1 (12.1). Oracle recommends that you use the DBA_HOST_ACES view, instead. See Also: " DBA_HOST_ACES " See Also: " DBA_HOST_ACES "