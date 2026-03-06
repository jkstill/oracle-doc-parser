---
id: 19c__DBMS_SCHEDULER.DROP_CREDENTIAL
name: DBMS_SCHEDULER.DROP_CREDENTIAL
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_SCHEDULER
tags: [dbms_scheduler]
source_file: DBMS_SCHEDULER.html
---

# DBMS_SCHEDULER.DROP_CREDENTIAL

This deprecated procedure drops a credential.

## Syntax

```sql
DBMS_SCHEDULER.DROP_CREDENTIAL (
   credential_name         IN VARCHAR2,
   force                   IN BOOLEAN DEFAULT FALSE);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| credential_name | VARCHAR2 | IN | The name of the credential being dropped. This can optionally be prefixed with a schema name. This cannot be set to NULL . |
| force | BOOLEAN | IN | If set to FALSE , the credential must not be referenced by any job, or an error will occur. If set to TRUE , the credential is dropped whether or not there are jobs referencing it. Jobs that reference the credential will continue to point to a nonexistent credential and throw an error at runtime. |

## Usage Notes

Note: This procedure is deprecated with Oracle Database 12 c Release 1 (12.1). While the procedure remains available in this package, for reasons of backward compatibility, Oracle recommends using the alternative enhanced functionality provided in the DBMS_CREDENTIAL package, specifically the DROP_CREDENTIAL Procedure . Note: This procedure is deprecated with Oracle Database 12 c Release 1 (12.1). While the procedure remains available in this package, for reasons of backward compatibility, Oracle recommends using the alternative enhanced functionality provided in the DBMS_CREDENTIAL package, specifically the DROP_CREDENTIAL Procedure . Syntax DBMS_SCHEDULER.DROP_CREDENTIAL ( credential_name IN VARCHAR2, force IN BOOLEAN DEFAULT FALSE); Parameters Table 151-47 DROP_CREDENTIAL Procedure Parameters Parameter Description credential_name The name of the credential being dropped. This can optionally be prefixed with a schema name. This cannot be set to NULL . force If set to FALSE , the credential must not be referenced by any job, or an error will occur. If set to TRUE , the credential is dropped whether or not there are jobs referencing it. Jobs that reference the credential will continue to point to a nonexistent credential and throw an error at runtime. Usage Notes Only the owner of a credential or a user with the CREATE ANY JOB system privilege may drop the credential. Running jobs that point to the credential are not affected by this procedure and are allowed to continue.