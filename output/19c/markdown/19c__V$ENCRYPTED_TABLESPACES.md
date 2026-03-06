---
id: 19c__V$ENCRYPTED_TABLESPACES
name: V$ENCRYPTED_TABLESPACES
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: storage
tags: [dynamic_performance]
source_file: V-ENCRYPTED_TABLESPACES.html
---

# V$ENCRYPTED_TABLESPACES

V$ENCRYPTED_TABLESPACES displays information about tablespaces that are encrypted.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| TS# | NUMBER |  |
| ENCRYPTIONALG | VARCHAR2(7) |  |
| ENCRYPTEDTS | VARCHAR2(3) |  |
| ENCRYPTEDKEY | RAW(32) |  |
| MASTERKEYID | RAW(16) |  |
| BLOCKS_ENCRYPTED | NUMBER |  |
| BLOCKS_DECRYPTED | NUMBER |  |
| KEY_VERSION | NUMBER |  |
| STATUS | VARCHAR2(10) |  |
| CON_ID | NUMBER |  |

## Usage Notes

In a non-CDB, the information displayed by this view is meaningful only when the database is open. In a CDB, the information displayed by this view is meaningful only for tablespaces in open containers. This is because the information is derived after the file headers making up a tablespace have been examined during the open operation. See Also: " V$DATABASE_KEY_INFO " See Also: " V$DATABASE_KEY_INFO "