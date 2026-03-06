---
id: 19c__DBMS_XDBRESOURCE.SETACL
name: DBMS_XDBRESOURCE.SETACL
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XDBRESOURCE
tags: [dbms_xdbresource]
source_file: DBMS_XDBRESOURCE.html
---

# DBMS_XDBRESOURCE.SETACL

This procedure sets the ACL of the given XDBResource to the path specified.

## Syntax

```sql
DBMS_XDBRESOURCE.SETACL (
   res      IN OUT  XDBResource, 
   ACLPath  IN      VARCHAR2);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| res | XDBResource | IN OUT | XDBResource |
| ACLPath | VARCHAR2) | IN | Absolute path of the new ACL |

## Usage Notes

Syntax DBMS_XDBRESOURCE.SETACL ( res IN OUT XDBResource, ACLPath IN VARCHAR2); Parameters Table 200-45 SETACL Procedure Parameters Parameter Description res XDBResource ACLPath Absolute path of the new ACL