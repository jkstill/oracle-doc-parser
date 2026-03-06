---
id: 19c__DBMS_CREDENTIAL.CREATE_CREDENTIAL
name: DBMS_CREDENTIAL.CREATE_CREDENTIAL
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_CREDENTIAL
tags: [dbms_credential]
source_file: DBMS_CREDENTIAL.html
---

# DBMS_CREDENTIAL.CREATE_CREDENTIAL

This procedure creates a stored username/password pair in a database object called an Oracle credential. You can also use this procedure to manage the credentials used for accessing files stored in cloud object storage.

## Syntax

```sql
DBMS_CREDENTIAL.CREATE_CREDENTIAL (
   credential_name   IN  VARCHAR2,
   username          IN  VARCHAR2,
   password          IN  VARCHAR2,
   database_role     IN  VARCHAR2 DEFAULT NULL
   windows_domain    IN  VARCHAR2 DEFAULT NULL,
   comments          IN  VARCHAR2 DEFAULT NULL,
   enabled           IN  BOOLEAN DEFAULT TRUE);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| credential_name | VARCHAR2 | IN | Name of the credential. It can optionally be prefixed with a schema. This cannot be set to NULL . It is converted to upper case unless enclosed in double quotes. |
| username | VARCHAR2 | IN | User name to login to the operating system or remote database to run a job if this credential is chosen. This cannot be set to NULL . |
| password | VARCHAR2 | IN | Password to login to the remote operating system to run a job if this credential is chosen. It is case sensitive. |
| database_role | VARCHAR2 | IN | Whether a database job using this credential should attempt to log in with administrative privileges. Values: SYSDBA , SYSDG , SYSADMIN or SYSBACKUP . |
| windows_domain | VARCHAR2 | IN | For a Windows remote executable target, this is the domain that the specified user belongs to. The domain will be converted to uppercase automatically. |
| comments | VARCHAR2 | IN | A text string that can be used to describe the credential to the user. The Scheduler does not use this field. |
| enabled | BOOLEAN | IN | Determines whether the credential is enabled or not |

## Usage Notes

Syntax DBMS_CREDENTIAL.CREATE_CREDENTIAL ( credential_name IN VARCHAR2, username IN VARCHAR2, password IN VARCHAR2, database_role IN VARCHAR2 DEFAULT NULL windows_domain IN VARCHAR2 DEFAULT NULL, comments IN VARCHAR2 DEFAULT NULL, enabled IN BOOLEAN DEFAULT TRUE); Parameters Table 41-2 CREATE_CREDENTIAL Procedure Parameters Parameter Description credential_name Name of the credential. It can optionally be prefixed with a schema. This cannot be set to NULL . It is converted to upper case unless enclosed in double quotes. username User name to login to the operating system or remote database to run a job if this credential is chosen. This cannot be set to NULL . password Password to login to the remote operating system to run a job if this credential is chosen. It is case sensitive. database_role Whether a database job using this credential should attempt to log in with administrative privileges. Values: SYSDBA , SYSDG , SYSADMIN or SYSBACKUP . windows_domain For a Windows remote executable target, this is the domain that the specified user belongs to. The domain will be converted to uppercase automatically. comments A text string that can be used to describe the credential to the user. The Scheduler does not use this field. enabled Determines whether the credential is enabled or not Usage Notes Credentials reside in a particular schema and can be created by any user with the CREATE CREDENTIAL or CREATE ANY CREDENTIAL system privilege. To create a credential in a schema other than your own, you must have the CREATE CREDENTIAL or CREATE ANY CREDENTIAL privilege. The user name is case sensitive. It cannot contain double quotes or spaces. Attempting to create a credential with an existing credential name returns an error. To alter an existing credential, users must drop the existing credential first using the DROP_CREDENTIAL Procedure . Attempting to drop an existing credential, which is already referenced by alias libraries, returns an error. To drop an existing credential without any checking, users must set the force parameter of DROP_CREDENTIAL Procedure to TRUE . You may also alter a credential, by means of the UPDATE_CREDENTIAL Procedure . Examples Create a Basic Credential CONN scott Enter password: password BEGIN -- Basic credential. DBMS_CREDENTIAL.CREATE_CREDENTIAL( credential_name => 'JAMES_SMITH', username => 'james_smith', password => 'password'); END Create a Windows Credential CONN scott Enter password: password -- Credential including Windows domain BEGIN DBMS_CREDENTIAL.CREATE_CREDENTIAL( credential_name => 'JAMES_SMITH_WIN_CREDENTIAL', username => 'james_smith', password => 'password', windows_domain => 'localdomain'); END Display Information about Credentials Information about credentials is displayed using the [DBA|ALL|USER] _CREDENTIALS views. COLUMN credential_name FORMAT A25 COLUMN username FORMAT A20 COLUMN windows_domain FORMAT A20 SELECT credential_name, username, windows_domain FROM user_credentials ORDER BY credential_name; CREDENTIAL_NAME USERNAME WINDOWS_DOMAIN ------------------------- -------------------- -------------------- JAMES_SMITH_CREDENTIAL james_smith JAMES_SMITH_WIN_CREDENTIAL james_smith LOCALDOMAIN 2 rows selected. SQL>