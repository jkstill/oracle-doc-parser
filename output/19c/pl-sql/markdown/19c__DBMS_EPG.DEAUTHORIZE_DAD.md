---
id: 19c__DBMS_EPG.DEAUTHORIZE_DAD
name: DBMS_EPG.DEAUTHORIZE_DAD
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_EPG
tags: [dbms_epg]
source_file: DBMS_EPG.html
---

# DBMS_EPG.DEAUTHORIZE_DAD

This procedure deauthorizes a DAD with regard to invoking procedures and accessing document tables with a database user's privileges. The invoker can always deauthorize the use of his own privileges.

## Syntax

```sql
DBMS_EPG.DEAUTHORIZE_DAD (
   dad_name  IN  VARCHAR2,
   path      IN  VARCHAR2 DEFAULT NULL);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| dad_name | VARCHAR2 | IN | The name of the DAD for which to deauthorize use |
| user |  |  | The user whose privileges to deauthorize. If use, the invoker is assumed. |

## Usage Notes

See Also: Authorization Subprograms for other subprograms in this group See Also: Authorization Subprograms for other subprograms in this group Syntax DBMS_EPG.DEAUTHORIZE_DAD ( dad_name IN VARCHAR2, path IN VARCHAR2 DEFAULT NULL); Parameters Table 67-7 DEAUTHORIZE_DAD Procedure Parameters Parameter Description dad_name The name of the DAD for which to deauthorize use user The user whose privileges to deauthorize. If use, the invoker is assumed. Usage Notes To deauthorize the use of another user's privileges, the invoker must have the ALTER USER system privilege.