---
id: 19c__DBA_HOST_ACES
name: DBA_HOST_ACES
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dba]
source_file: DBA_HOST_ACES.html
---

# DBA_HOST_ACES

DBA_HOST_ACES describes access control entries defined in host access control lists.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| HOST | VARCHAR2(1000) | Network host |
| LOWER_PORT | NUMBER(5) | Lower bound of the port range |
| UPPER_PORT | NUMBER(5) | Upper bound of the port range |
| ACE_ORDER | NUMBER | Order number of the access control entry |
| START_DATE | TIMESTAMP(6) | Start date of the access control entry |
| END_DATE | TIMESTAMP(6) | End date of the access control entry |
| GRANT_TYPE | VARCHAR2(5) | Indicates whether the access control entry grants or denies the privilege |
| INVERTED_PRINCIPAL | VARCHAR2(3) | Indicates whether the principal is inverted or not |
| PRINCIPAL | VARCHAR2(128) | Principal the privilege is applied to |
| PRINCIPAL_TYPE | VARCHAR2(16) | Type of the principal |
| PRIVILEGE | VARCHAR2(128) | Privilege |

## Usage Notes

Related View USER_HOST_ACES describes the status of access control entries for the current user to access network hosts through PL/SQL network utility packages. This view does not display the ACE_ORDER , START_DATE , END_DATE , GRANT_TYPE , INVERTED_PRINCIPAL , PRINCIPAL , or PRINCIPAL_TYPE columns. See Also: " USER_HOST_ACES " See Also: " USER_HOST_ACES "