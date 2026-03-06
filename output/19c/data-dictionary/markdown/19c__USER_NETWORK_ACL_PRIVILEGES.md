---
id: 19c__USER_NETWORK_ACL_PRIVILEGES
name: USER_NETWORK_ACL_PRIVILEGES
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: security
tags: [user]
source_file: USER_NETWORK_ACL_PRIVILEGES.html
---

# USER_NETWORK_ACL_PRIVILEGES

USER_NETWORK_ACL_PRIVILEGES describes the status of the network privileges for the current user to access network hosts.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| HOST | VARCHAR2(1000) | Network host |
| LOWER_PORT | NUMBER(5) | Lower bound of the port range |
| UPPER_PORT | NUMBER(5) | Upper bound of the port range |
| PRIVILEGE | CHAR(128) | Network privilege |
| STATUS | VARCHAR2(7) | Privilege status: DENIED GRANTED |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content Note: This USER_NETWORK_ACL_PRIVILEGES view is deprecated in Oracle Database 12 c Release 1 (12.1). Oracle recommends that you use the USER_HOST_ACES view, instead. Note: This USER_NETWORK_ACL_PRIVILEGES view is deprecated in Oracle Database 12 c Release 1 (12.1). Oracle recommends that you use the USER_HOST_ACES view, instead. See Also: " USER_HOST_ACES " See Also: " USER_HOST_ACES "