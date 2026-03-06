---
id: 19c__DBMS_RESCONFIG.DELETERESCONFIG
name: DBMS_RESCONFIG.DELETERESCONFIG
object_type: plsql_subprogram
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_RESCONFIG
tags: [dbms_resconfig]
source_file: DBMS_RESCONFIG.html
---

# DBMS_RESCONFIG.DELETERESCONFIG

This procedure removes the configuration at the given position in the target resource's configuration list. It shifts any subsequent elements to the left. Users can use the overloaded for recursive deletion.

## Syntax

```sql
DBMS_RESCONFIG.DELETERESCONFIG(
   respath       IN   VARCHAR2, 
   pos           IN   PLS_INTEGER);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| respath | VARCHAR2 | IN | Absolute path of the target resource |
| pos | PLS_INTEGER) | IN | The index of the configuration to be removed. An exception is raised if the index is out of range ( pos < 0 or pos >= the size of the target resource's configuration list). |
| rcpath |  |  | Absolute path of the resource configuration to be deleted if found in list. |
| deleteOption |  |  | Either DELETE_RESOURCE or DELETE_RECURSIVE . If DELETE_RESOURCE is specified then only the configuration list of the target resource is affected. If DELETE_RECURSIVE is specified then the configuration list of the target resource and all its descendents will be affected. |

## Usage Notes

Syntax DBMS_RESCONFIG.DELETERESCONFIG( respath IN VARCHAR2, pos IN PLS_INTEGER); DBMS_RESCONFIG.DELETERESCONFIG( respath IN VARCHAR2, rcpath IN VARCHAR2, deleteOption IN PLS_INTEGER); Parameters Table 141-6 DELETERESCONFIG Procedure Parameters Parameter Description respath Absolute path of the target resource pos The index of the configuration to be removed. An exception is raised if the index is out of range ( pos < 0 or pos >= the size of the target resource's configuration list). rcpath Absolute path of the resource configuration to be deleted if found in list. deleteOption Either DELETE_RESOURCE or DELETE_RECURSIVE . If DELETE_RESOURCE is specified then only the configuration list of the target resource is affected. If DELETE_RECURSIVE is specified then the configuration list of the target resource and all its descendents will be affected. Usage Notes Users must have WRITE-CONFIG privilege on the target resource to execute this.