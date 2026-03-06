---
id: 19c__DBMS_CREDENTIAL.ENABLE_CREDENTIAL
name: DBMS_CREDENTIAL.ENABLE_CREDENTIAL
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_CREDENTIAL
tags: [dbms_credential]
source_file: DBMS_CREDENTIAL.html
---

# DBMS_CREDENTIAL.ENABLE_CREDENTIAL

This procedure enables an Oracle credential.

## Syntax

```sql
DBMS_CREDENTIAL.ENABLE_CREDENTIAL (
   credential_name   IN  VARCHAR2);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| credential_name | VARCHAR2) | IN | Name of the credential. It can optionally be prefixed with a schema. This cannot be set to NULL . It is converted to upper case unless enclosed in double quotes. |

## Usage Notes

Syntax DBMS_CREDENTIAL.ENABLE_CREDENTIAL ( credential_name IN VARCHAR2); Parameters Table 41-5 ENABLE_CREDENTIAL Procedure Parameters Parameter Description credential_name Name of the credential. It can optionally be prefixed with a schema. This cannot be set to NULL . It is converted to upper case unless enclosed in double quotes. Usage Notes Credentials reside in a particular schema and can be disabled by any user with the CREATE CREDENTIAL OR CREATE ANY CREDENTIAL system privilege. To disable a credential in a schema other than your own, you must have the CREATE CREDENTIAL OR CREATE ANY CREDENTIAL privilege. A credential for an OS user can be viewed as an entry point into an operating system as a particular user. Allowing a credential to be disabled would allow an administrator (or credential owner) to quickly, easily and reversibly disallow all logins from the database to the OS as a particular user (external jobs, file transfers, external procedures, file watching). To disable an existing credential, you need to use the DISABLE_CREDENTIAL Procedure . A library can become invalid if the properties of the credential – windows domain, username, password, its enable/disable bit – are changed.