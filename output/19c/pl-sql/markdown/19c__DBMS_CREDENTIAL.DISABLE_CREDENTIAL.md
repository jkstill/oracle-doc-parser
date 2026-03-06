---
id: 19c__DBMS_CREDENTIAL.DISABLE_CREDENTIAL
name: DBMS_CREDENTIAL.DISABLE_CREDENTIAL
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_CREDENTIAL
tags: [dbms_credential]
source_file: DBMS_CREDENTIAL.html
---

# DBMS_CREDENTIAL.DISABLE_CREDENTIAL

This procedure disables an Oracle credential.

## Syntax

```sql
DBMS_CREDENTIAL.DISABLE_CREDENTIAL (
   credential_name   IN  VARCHAR2,
   force             IN  BOOLEAN DEFAULT FALSE);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| credential_name | VARCHAR2 | IN | Name of the credential. It can optionally be prefixed with a schema. This cannot be set to NULL . It is converted to upper case unless enclosed in double quotes. |
| force | BOOLEAN | IN | If FALSE , the credential is not disabled provided it has no dependency on any existing scheduler job or PL/SQL library. An error is returned if the dependency is observed.If TRUE , the credential is disabled whether or not there is any scheduler job or PL/SQL library referencing it. |

## Usage Notes

Syntax DBMS_CREDENTIAL.DISABLE_CREDENTIAL ( credential_name IN VARCHAR2, force IN BOOLEAN DEFAULT FALSE); Parameters Table 41-3 DISABLE_CREDENTIAL Procedure Parameters Parameter Description credential_name Name of the credential. It can optionally be prefixed with a schema. This cannot be set to NULL . It is converted to upper case unless enclosed in double quotes. force If FALSE , the credential is not disabled provided it has no dependency on any existing scheduler job or PL/SQL library. An error is returned if the dependency is observed.If TRUE , the credential is disabled whether or not there is any scheduler job or PL/SQL library referencing it. Usage Notes Credentials reside in a particular schema and can be disabled by any user with the CREATE CREDENTIAL or CREATE ANY CREDENTIAL system privilege. To disable a credential in a schema other than your own, you must have the CREATE ANY CREDENTIAL privilege. A credential for an OS user can be viewed as an entry point into an operating system as a particular user. Allowing a credential to be disabled lets an administrator (or credential owner) to quickly, easily and reversibly disallow all logins from the database to the OS as a particular user of external jobs, database jobs, file transfers, external procedures, and file watching. To enable an existing disabled credential, you need to use the ENABLE_CREDENTIAL Procedure . A library can become invalid if the properties of the credential – windows domain, username, password, its enable/disable bit – are changed.