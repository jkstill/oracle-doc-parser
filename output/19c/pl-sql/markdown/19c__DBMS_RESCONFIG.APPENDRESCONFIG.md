---
id: 19c__DBMS_RESCONFIG.APPENDRESCONFIG
name: DBMS_RESCONFIG.APPENDRESCONFIG
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_RESCONFIG
tags: [dbms_resconfig]
source_file: DBMS_RESCONFIG.html
---

# DBMS_RESCONFIG.APPENDRESCONFIG

This procedure appends the resource configuration specified by rcpath to the target resource's configuration list if it is not already included in the list.

## Syntax

```sql
DBMS_RESCONFIG.ADDRESCONFIG(
   respath       IN   VARCHAR2, 
   rcpath        IN   VARCHAR2, 
   appendOption  IN   PLS_INTEGER);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| respath | VARCHAR2 | IN | Absolute path of the target resource |
| rcpath | VARCHAR2 | IN | Absolute path of the resource configuration to be appended at the end of the target's configuration list. If rcpath already exists in the list then nothing is appended. |
| appendOption | PLS_INTEGER) | IN | Either APPEND_RESOURCE or APPEND_RECURSIVE . If APPEND_RESOURCE is specified then only the target resource is affected. If APPEND_RECURSIVE is specified then the target resource and all its descendents will be affected. |

## Usage Notes

Syntax DBMS_RESCONFIG.ADDRESCONFIG( respath IN VARCHAR2, rcpath IN VARCHAR2, appendOption IN PLS_INTEGER); Parameters Table 141-4 ADDRESCONFIG Function Parameters Parameter Description respath Absolute path of the target resource rcpath Absolute path of the resource configuration to be appended at the end of the target's configuration list. If rcpath already exists in the list then nothing is appended. appendOption Either APPEND_RESOURCE or APPEND_RECURSIVE . If APPEND_RESOURCE is specified then only the target resource is affected. If APPEND_RECURSIVE is specified then the target resource and all its descendents will be affected. Usage Notes An error is raised if the document referenced by rcpath is not based on XDBResConfig .xsd schema. Users must have WRITE -CONFIG privilege on all affected resources and required read privilege on the resource configuration to be inserted; otherwise, an error is returned.