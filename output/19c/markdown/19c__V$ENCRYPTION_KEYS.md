---
id: 19c__V$ENCRYPTION_KEYS
name: V$ENCRYPTION_KEYS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dynamic_performance]
source_file: V-ENCRYPTION_KEYS.html
---

# V$ENCRYPTION_KEYS

V$ENCRYPTION_KEYS displays master key description attributes.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| KEY_ID | VARCHAR2(78) |  |
| TAG | VARCHAR2(4000) |  |
| CREATION_TIME | TIMESTAMP(6) WITH TIME ZONE |  |
| ACTIVATION_TIME | TIMESTAMP(6) WITH TIME ZONE |  |
| CREATOR | VARCHAR2(128) |  |
| CREATOR_ID | NUMBER |  |
| USER | VARCHAR2(128) |  |
| USER_ID | NUMBER |  |
| KEY_USE | VARCHAR2(10) |  |
| KEYSTORE_TYPE | VARCHAR2(17) |  |
| ORIGIN | VARCHAR2(41) |  |
| BACKED_UP | VARCHAR2(9) |  |
| CREATOR_DBNAME | VARCHAR2(128) |  |
| CREATOR_DBID | NUMBER |  |
| CREATOR_INSTANCE_NAME | VARCHAR2(30) |  |
| CREATOR_INSTANCE_NUMBER | NUMBER |  |
| CREATOR_INSTANCE_SERIAL | NUMBER |  |
| CREATOR_PDBNAME | VARCHAR2(128) |  |
| CREATOR_PDBID | NUMBER |  |
| CREATOR_PDBUID | NUMBER |  |
| CREATOR_PDBGUID | RAW(16) |  |
| ACTIVATING_DBNAME | VARCHAR2(128) |  |
| ACTIVATING_DBID | NUMBER |  |
| ACTIVATING_INSTANCE_NAME | VARCHAR2(30) |  |
| ACTIVATING_INSTANCE_NUMBER | NUMBER |  |
| ACTIVATING_INSTANCE_SERIAL | NUMBER |  |
| ACTIVATING_PDBNAME | VARCHAR2(128) |  |
| ACTIVATING_PDBID | NUMBER |  |
| ACTIVATING_PDBUID | NUMBER |  |
| ACTIVATING_PDBGUID | RAW(16) |  |
| CON_ID | NUMBER |  |

## Usage Notes

See Also: Oracle Database Advanced Security Guide for information about keystore management See Also: Oracle Database Advanced Security Guide for information about keystore management