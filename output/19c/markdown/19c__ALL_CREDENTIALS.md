---
id: 19c__ALL_CREDENTIALS
name: ALL_CREDENTIALS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [all]
source_file: ALL_CREDENTIALS.html
---

# ALL_CREDENTIALS

ALL_CREDENTIALS lists all credentials visible to the user.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| OWNER | VARCHAR2(128) | Owner of the credential |
| CREDENTIAL_NAME | VARCHAR2(128) | Name of the credential |
| USERNAME | VARCHAR2(128) | Name of the user that will be used to log in to the remote database or the remote or local operating system |
| WINDOWS_DOMAIN | VARCHAR2(30) | For a Windows target, the Windows domain to use when logging in |
| COMMENTS | VARCHAR2(4000) | Comments on the credential |
| ENABLED | VARCHAR2(5) | Indicates whether this credential is enabled ( TRUE ) or not ( FALSE ) |

## Usage Notes

Related Views DBA_CREDENTIALS lists all credentials in the database. USER_CREDENTIALS lists credentials owned by the current user. This view does not display the OWNER column. Note: DBMS_CREDENTIAL lists credentials that can be used to run external procedures, or by DBMS_SCHEDULER for remote or external jobs, or for storing or retrieving files from the operating system. If a credential is disabled, then any of the actions above that attempts to use the credential will fail. See Also: " DBA_CREDENTIALS " " USER_CREDENTIALS " Oracle Database PL/SQL Packages and Types Reference for more information about the DBMS_CREDENTIAL package Oracle Database PL/SQL Packages and Types Reference for more information about the DBMS_SCHEDULER package Note: DBMS_CREDENTIAL lists credentials that can be used to run external procedures, or by DBMS_SCHEDULER for remote or external jobs, or for storing or retrieving files from the operating system. If a credential is disabled, then any of the actions above that attempts to use the credential will fail. See Also: " DBA_CREDENTIALS " " USER_CREDENTIALS " Oracle Database PL/SQL Packages and Types Reference for more information about the DBMS_CREDENTIAL package Oracle Database PL/SQL Packages and Types Reference for more information about the DBMS_SCHEDULER package