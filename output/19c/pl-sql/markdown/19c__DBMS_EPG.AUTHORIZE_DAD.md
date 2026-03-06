---
id: 19c__DBMS_EPG.AUTHORIZE_DAD
name: DBMS_EPG.AUTHORIZE_DAD
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_EPG
tags: [dbms_epg]
source_file: DBMS_EPG.html
---

# DBMS_EPG.AUTHORIZE_DAD

This procedure authorizes a DAD to invoke procedures and access document tables with a database user's privileges. The invoker can always authorize the use of her/his own privileges.

## Syntax

```sql
DBMS_EPG.AUTHORIZE_DAD (
   dad_name  IN  VARCHAR2,
   path     IN  VARCHAR2 DEFAULT NULL);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| dad_name | VARCHAR2 | IN | The name of the DAD to create |
| user |  |  | The user whose privileges to deauthorize. If use, the invoker is assumed. |

## Usage Notes

See Also: Authorization Subprograms for other subprograms in this group See Also: Authorization Subprograms for other subprograms in this group Syntax DBMS_EPG.AUTHORIZE_DAD ( dad_name IN VARCHAR2, path IN VARCHAR2 DEFAULT NULL); Parameters Table 67-5 AUTHORIZE_DAD Procedure Parameters Parameter Description dad_name The name of the DAD to create user The user whose privileges to deauthorize. If use, the invoker is assumed. Usage Notes To authorize the use of another user's privileges, the invoker must have the ALTER USER system privilege. The DAD must exist but its "database-username" DAD attribute does not have to be set to user to authorize. Multiple users can authorize the same DAD and it is up to the DAD's "database-username" setting to decide which user's privileges to use.