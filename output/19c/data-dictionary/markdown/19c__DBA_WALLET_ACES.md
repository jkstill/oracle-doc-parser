---
id: 19c__DBA_WALLET_ACES
name: DBA_WALLET_ACES
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dba]
source_file: DBA_WALLET_ACES.html
---

# DBA_WALLET_ACES

DBA_WALLET_ACES describes access control entries defined in wallet access control lists.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| WALLET_PATH | VARCHAR2(1000) | Wallet path |
| ACE_ORDER | NUMBER | Order number of the access control entry |
| START_DATE | TIMESTAMP(6) | Start date of the access control entry |
| END_DATE | TIMESTAMP(6) | End date of the access control entry |
| GRANT_TYPE | VARCHAR2(5) | Indicates whether the access control entry grants or denies the privilege |
| INVERTED_PRINCIPAL | VARCHAR2(3) | Indicates whether the principal is inverted or not |
| PRINCIPAL | VARCHAR2(128) | Principal the privilege is applied to |
| PRINCIPAL_TYPE | VARCHAR2(16) | Type of the principal |
| PRIVILEGE | VARCHAR2(128) | Privilege |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content Related View USER_WALLET_ACES describes the status of access control entries for the current user to access wallets through PL/SQL network utility packages. This view does not display the ACE_ORDER , START_DATE , END_DATE , GRANT_TYPE , INVERTED_PRINCIPAL , PRINCIPAL , or PRINCIPAL_TYPE columns. See Also: " USER_WALLET_ACES " See Also: " USER_WALLET_ACES "