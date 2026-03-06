---
id: 19c__DBMS_SCHEDULER.CREATE_CREDENTIAL
name: DBMS_SCHEDULER.CREATE_CREDENTIAL
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_SCHEDULER
tags: [dbms_scheduler]
source_file: DBMS_SCHEDULER.html
---

# DBMS_SCHEDULER.CREATE_CREDENTIAL

This deprecated procedure creates a stored username/password pair. Credentials are assigned to jobs so that they can authenticate with a local or remote host operating system or a remote Oracle database.

## Syntax

```sql
DBMS_SCHEDULER.CREATE_CREDENTIAL (
   credential_name         IN VARCHAR2,
   username                IN VARCHAR2,
   password                IN VARCHAR2,
   database_role           IN VARCHAR2 DEFAULT NULL,
   windows_domain          IN VARCHAR2 DEFAULT NULL,
   comments                IN VARCHAR2 DEFAULT NULL);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| credential_name | VARCHAR2 | IN | The name to assign to the credential. It can optionally be prefixed with a schema name. It cannot be set to NULL . It is converted to uppercase unless enclosed in double quotation marks. |
| username | VARCHAR2 | IN | The user name for logging into to the host operating system or remote Oracle database. This cannot be set to NULL and is case-sensitive. It cannot contain double quotes or spaces. Maximum length is 64. |
| password | VARCHAR2 | IN | The password for the user name. This cannot be set to NULL and is case sensitive. The password is stored obfuscated and is not displayed in the Scheduler dictionary views. Maximum length is 128. |
| database_role | VARCHAR2 | IN | The value of the database_role attribute is used as the system privilege for logging into a remote database to run a remote database job. Valid values are: SYSDBA and SYSOPER |
| windows_domain | VARCHAR2 | IN | For a Windows remote executable target, this is the domain that the specified user belongs to. The domain is converted to uppercase automatically. Maximum length is 64. |
| comments | VARCHAR2 | IN | A text string that can be used to describe the credential. Scheduler does not use this parameter. Maximum length is 240. |

## Usage Notes

Note: This procedure is deprecated with Oracle Database 12 c Release 1 (12.1). While the procedure remains available in this package, for reasons of backward compatibility, Oracle recommends using the alternative enhanced functionality provided in the DBMS_CREDENTIAL package, specifically the CREATE_CREDENTIAL Procedure . Note: This procedure is deprecated with Oracle Database 12 c Release 1 (12.1). While the procedure remains available in this package, for reasons of backward compatibility, Oracle recommends using the alternative enhanced functionality provided in the DBMS_CREDENTIAL package, specifically the CREATE_CREDENTIAL Procedure . Syntax DBMS_SCHEDULER.CREATE_CREDENTIAL ( credential_name IN VARCHAR2, username IN VARCHAR2, password IN VARCHAR2, database_role IN VARCHAR2 DEFAULT NULL, windows_domain IN VARCHAR2 DEFAULT NULL, comments IN VARCHAR2 DEFAULT NULL); Parameters Table 151-22 CREATE_CREDENTIAL Procedure Parameters Parameter Description credential_name The name to assign to the credential. It can optionally be prefixed with a schema name. It cannot be set to NULL . It is converted to uppercase unless enclosed in double quotation marks. username The user name for logging into to the host operating system or remote Oracle database. This cannot be set to NULL and is case-sensitive. It cannot contain double quotes or spaces. Maximum length is 64. password The password for the user name. This cannot be set to NULL and is case sensitive. The password is stored obfuscated and is not displayed in the Scheduler dictionary views. Maximum length is 128. database_role The value of the database_role attribute is used as the system privilege for logging into a remote database to run a remote database job. Valid values are: SYSDBA and SYSOPER windows_domain For a Windows remote executable target, this is the domain that the specified user belongs to. The domain is converted to uppercase automatically. Maximum length is 64. comments A text string that can be used to describe the credential. Scheduler does not use this parameter. Maximum length is 240. Usage Notes Credentials reside in a particular schema and can be created by any user with the CREATE JOB system privilege. To create a credential in a schema other than your own, you must have the CREATE ANY JOB privilege.