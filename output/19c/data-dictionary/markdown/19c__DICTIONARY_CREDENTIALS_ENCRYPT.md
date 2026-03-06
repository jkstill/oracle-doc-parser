---
id: 19c__DICTIONARY_CREDENTIALS_ENCRYPT
name: DICTIONARY_CREDENTIALS_ENCRYPT
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
source_file: DICTIONARY_CREDENTIALS_ENCRYPT.html
---

# DICTIONARY_CREDENTIALS_ENCRYPT

DICTIONARY_CREDENTIALS_ENCRYPT indicates whether encryption of dictionary credentials is enforced or not. You can encrypt sensitive credential information, such as passwords that are stored in the data dictionary.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| ENFORCEMENT | VARCHAR2(8) | Enforcement status for encryption of dictionary credentials. Possible values: ENABLED : Encryption of dictionary credentials is enforced DISABLED : Encryption of dictionary credentials is not enforced |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content See Also: Oracle Database Security Guide for information about encrypting sensitive credential information in the data dictionary See Also: Oracle Database Security Guide for information about encrypting sensitive credential information in the data dictionary