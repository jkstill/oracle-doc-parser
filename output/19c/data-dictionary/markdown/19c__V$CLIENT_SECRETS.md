---
id: 19c__V$CLIENT_SECRETS
name: V$CLIENT_SECRETS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dynamic_performance]
source_file: V-CLIENT_SECRETS.html
---

# V$CLIENT_SECRETS

V$CLIENT_SECRETS lists the secrets that are present in the keystore.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| CLIENT | VARCHAR2(2000) |  |
| SECRET_TAG | VARCHAR2(4000) |  |
| CREATION_TIME | TIMESTAMP(6) WITH TIME ZONE |  |
| ACTIVATION_TIME | TIMESTAMP(6) WITH TIME ZONE |  |
| OWNER | VARCHAR2(128) |  |
| OWNER_ID | NUMBER |  |
| KEYSTORE_TYPE | VARCHAR2(17) |  |
| BACKED_UP | VARCHAR2(9) |  |
| OWNER_DBNAME | VARCHAR2(128) |  |
| OWNER_DBID | NUMBER |  |
| OWNER_INSTANCE_NAME | VARCHAR2(30) |  |
| OWNER_INSTANCE_NUMBER | NUMBER |  |
| OWNER_INSTANCE_SERIAL | NUMBER |  |
| OWNER_PDBNAME | VARCHAR2(128) |  |
| OWNER_PDBID | NUMBER |  |
| OWNER_PDBUID | NUMBER |  |
| OWNER_PDBGUID | RAW(16) |  |
| CON_ID | NUMBER |  |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content Only SYS , SYSKM , and users with the ADMINISTER KEY MANAGEMENT privilege can access this view. See Also: Oracle Database Advanced Security Guide for information about keystore management See Also: Oracle Database Advanced Security Guide for information about keystore management