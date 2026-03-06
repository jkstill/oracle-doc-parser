---
id: 19c__V$PWFILE_USERS
name: V$PWFILE_USERS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: security
tags: [dynamic_performance]
source_file: V-PWFILE_USERS.html
---

# V$PWFILE_USERS

V$PWFILE_USERS lists all users in the password file, and indicates whether the user has been granted the SYSDBA , SYSOPER , SYSASM , SYSBACKUP , SYSDG , and SYSKM privileges.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| USERNAME | VARCHAR2(128) |  |
| SYSDBA | VARCHAR2(5) |  |
| SYSOPER | VARCHAR2(5) |  |
| SYSASM | VARCHAR2(5) |  |
| SYSBACKUP | VARCHAR2(5) |  |
| SYSDG | VARCHAR2(5) |  |
| SYSKM | VARCHAR2(5) |  |
| ACCOUNT_STATUS | VARCHAR2(30) |  |
| PASSWORD_PROFILE | VARCHAR2(128) |  |
| LAST_LOGIN | TIMESTAMP(9) WITH TIME ZONE |  |
| LOCK_DATE | DATE |  |
| EXPIRY_DATE | DATE |  |
| EXTERNAL_NAME | VARCHAR2(1024) |  |
| AUTHENTICATION_TYPE | VARCHAR2(8) |  |
| COMMON | VARCHAR2(3) |  |
| CON_ID | NUMBER |  |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content