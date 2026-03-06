---
id: 19c__DBMS_CREDENTIAL.UPDATE_CREDENTIAL
name: DBMS_CREDENTIAL.UPDATE_CREDENTIAL
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_CREDENTIAL
tags: [dbms_credential]
source_file: DBMS_CREDENTIAL.html
---

# DBMS_CREDENTIAL.UPDATE_CREDENTIAL

This procedure updates an existing Oracle credential.

## Syntax

```sql
DBMS_CREDENTIAL.UPDATE_CREDENTIAL (
   credential_name   IN   VARCHAR2,
   attribute         IN   VARCHAR2, 
   value             IN   VARCHAR2);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| credential_name | VARCHAR2 | IN | Name of the credential. It can optionally be prefixed with a schema. This cannot be set to NULL . It is converted to upper case unless enclosed in double quotation marks. |
| attribute | VARCHAR2 | IN | Name of attribute to update: USERNAME , PASSWORD , WINDOWS_DOMAIN , DATABASE_ROLE or COMMENTS |
| value | VARCHAR2) | IN | New value for the selected attribute |

## Usage Notes

Syntax DBMS_CREDENTIAL.UPDATE_CREDENTIAL ( credential_name IN VARCHAR2, attribute IN VARCHAR2, value IN VARCHAR2); Parameters Table 41-6 UPDATE_CREDENTIAL Procedure Parameters Parameter Description credential_name Name of the credential. It can optionally be prefixed with a schema. This cannot be set to NULL . It is converted to upper case unless enclosed in double quotation marks. attribute Name of attribute to update: USERNAME , PASSWORD , WINDOWS_DOMAIN , DATABASE_ROLE or COMMENTS value New value for the selected attribute Usage Notes Credentials reside in a particular schema and can be created by any user with the CREATE CREDENTIAL or CREATE ANY CREDENTIAL system privilege. To create a credential in a schema other than your own, you must have the CREATE ANY CREDENTIAL privilege. The user name is case sensitive. It cannot contain double quotes or spaces. EXTPROC alias libraries that reference the updated credential will become invalid. A library becomes invalid if the properties of the credential – windows domain, username, password, its enable/disable bit – are changed. Examples Update a Basic Credential CONN scott Enter password: password BEGIN -- Basic credential. DBMS_CREDENTIAL.UPDATE_CREDENTIAL ( credential_name => 'JAMES_SMITH_CREDENTIAL', attribute => 'password', value => 'password2'); DBMS_CREDENTIAL.UPDATE_CREDENTIAL ( credential_name => 'JAMES_SMITH_CREDENTIAL', attribute => 'username', value => 'james_smith'); END; Update a Windows Credential CONN scott Enter password: password -- Credential including Windows domain BEGIN DBMS_CREDENTIAL.UPDATE_CREDENTIAL( credential_name => 'JAMES_SMITH_WIN_CREDENTIAL', username => 'james_smith', password => 'password', windows_domain => 'localdomain'); END Display Information about Credentials Information about credentials is displayed using the [DBA|ALL|USER] _CREDENTIALS views. COLUMN credential_name FORMAT A25 COLUMN username FORMAT A20 COLUMN windows_domain FORMAT A20 SELECT credential_name, username, windows_domain FROM all_credentials ORDER BY credential_name; CREDENTIAL_NAME USERNAME WINDOWS_DOMAIN ------------------------- -------------------- -------------------- JAMES_SMITH_CREDENTIAL james_smith JAMES_SMITH_WIN_CREDENTIAL james_smith LOCALDOMAIN 2 rows selected. SQL>