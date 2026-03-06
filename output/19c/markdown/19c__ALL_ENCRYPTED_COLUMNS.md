---
id: 19c__ALL_ENCRYPTED_COLUMNS
name: ALL_ENCRYPTED_COLUMNS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: tables
tags: [all]
source_file: ALL_ENCRYPTED_COLUMNS.html
---

# ALL_ENCRYPTED_COLUMNS

ALL_ENCRYPTED_COLUMNS displays encryption algorithm information for the encrypted columns in the tables accessible to the current user.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| OWNER | VARCHAR2(128) | Owner of the table |
| TABLE_NAME | VARCHAR2(128) | Name of the table |
| COLUMN_NAME | VARCHAR2(128) | Name of the column |
| ENCRYPTION_ALG | VARCHAR2(29) | Encryption algorithm used to protect secrecy of data in this column: 3 Key Triple DES 168 bits key AES 128 bits key AES 192 bits key AES 256 bits key |
| SALT | VARCHAR2(3) | Indicates whether the column is encrypted with SALT ( YES ) or not ( NO ) |
| INTEGRITY_ALG | VARCHAR2(12) | Integrity algorithm used for the column: SHA-1 NOMAC |

## Usage Notes

Related Views DBA_ENCRYPTED_COLUMNS displays encryption algorithm information for all encrypted columns in the database. USER_ENCRYPTED_COLUMNS displays encryption algorithm information for the encrypted columns in the tables owned by the current user. This view does not display the OWNER column. See Also: " DBA_ENCRYPTED_COLUMNS " " USER_ENCRYPTED_COLUMNS " See Also: " DBA_ENCRYPTED_COLUMNS " " USER_ENCRYPTED_COLUMNS "