---
id: 19c__V$DATABASE_KEY_INFO
name: V$DATABASE_KEY_INFO
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dynamic_performance]
source_file: V-DATABASE_KEY_INFO.html
---

# V$DATABASE_KEY_INFO

V$DATABASE_KEY_INFO provides the information of the default database key used to encrypt data blocks. Oracle uses the database key to encrypt sensitive information in SYSTEM, UNDO, and TEMP tablespaces when such data has dependency from encrypted tablespaces or encrypted columns

## Columns

| Column | Type | Description |
|--------|------|-------------|
| ENCRYPTIONALG | VARCHAR2(7) |  |
| ENCRYPTEDKEY | RAW(48) |  |
| MASTERKEYID | RAW(16) |  |
| MASTER_ACTIVATED | VARCHAR2(3) |  |
| CON_ID | NUMBER |  |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content V$DATABASE_KEY_INFO reflects the database key information stored in the control file. Generally it is the same as the system tablespace key recorded in the system tablespace. If the system tablespace is encrypted, it will also appear in V$ENCRYPTED_TABLESPACES . If the system tablespace is not encrypted, this is the only view providing this information. See Also: " V$ENCRYPTED_TABLESPACES " See Also: " V$ENCRYPTED_TABLESPACES "