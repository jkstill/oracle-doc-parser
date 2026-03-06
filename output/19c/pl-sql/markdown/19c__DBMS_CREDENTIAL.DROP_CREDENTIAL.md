---
id: 19c__DBMS_CREDENTIAL.DROP_CREDENTIAL
name: DBMS_CREDENTIAL.DROP_CREDENTIAL
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_CREDENTIAL
tags: [dbms_credential]
source_file: DBMS_CREDENTIAL.html
---

# DBMS_CREDENTIAL.DROP_CREDENTIAL

This procedure drops an Oracle credential.

## Syntax

```sql
DBMS_CREDENTIAL.DROP_CREDENTIAL (
   credential_name   IN  VARCHAR2,
   force             IN  BOOLEAN DEFAULT FALSE);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| credential_name | VARCHAR2 | IN | Name of the credential. It can optionally be prefixed with a schema. This cannot be set to NULL . |
| force | BOOLEAN | IN | If set to FALSE , the credential must not be referenced by any EXTPROC alias library or an error is raised. If set to TRUE , the credential is dropped whether or not there are extproc alias libraries referencing it. EXTPROC alias libraries that reference the dropped credential become invalid. |

## Usage Notes

Syntax DBMS_CREDENTIAL.DROP_CREDENTIAL ( credential_name IN VARCHAR2, force IN BOOLEAN DEFAULT FALSE); Parameters Table 41-4 DROP_CREDENTIAL Procedure Parameters Parameter Description credential_name Name of the credential. It can optionally be prefixed with a schema. This cannot be set to NULL . force If set to FALSE , the credential must not be referenced by any EXTPROC alias library or an error is raised. If set to TRUE , the credential is dropped whether or not there are extproc alias libraries referencing it. EXTPROC alias libraries that reference the dropped credential become invalid. Usage Notes Only the owner of a credential or a user with the CREATE ANY CREDENTIAL system privilege may drop the credential. Examples EXEC DBMS_CREDENTIAL.DROP_CREDENTIAL('JAMES_SMITH_CREDENTIAL', FALSE); EXEC DBMS_CREDENTIAL.DROP_CREDENTIAL('JAMES_SMITH_WIN_CREDENTIAL', FALSE);