---
id: 19c__DBA_WALLET_ACLS
name: DBA_WALLET_ACLS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dba]
source_file: DBA_WALLET_ACLS.html
---

# DBA_WALLET_ACLS

DBA_WALLET_ACLS displays the access control lists assigned to restrict access to wallets through PL/SQL network utility packages.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| WALLET_PATH | VARCHAR2(1000) | Wallet path |
| ACL | VARCHAR2(4000) | Path of the access control list |
| ACLID | RAW(8) | Object ID of the access control list |
| ACL_OWNER | VARCHAR2(128) | Owner of the access control list |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content