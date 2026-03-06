---
id: 19c__DBMS_RESCONFIG.ADDREPOSITORYRESCONFIG
name: DBMS_RESCONFIG.ADDREPOSITORYRESCONFIG
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_RESCONFIG
tags: [dbms_resconfig]
source_file: DBMS_RESCONFIG.html
---

# DBMS_RESCONFIG.ADDREPOSITORYRESCONFIG

This procedure inserts the resource configuration specified by absolute path of the resource configuration at the specified position of the repository's configuration list. It shifts the element currently at that position (if any) and any subsequent elements to the right.

## Syntax

```sql
DBMS_RESCONFIG.ADDREPOSITORYRESCONFIG(
   rcpath     IN   VARCHAR2, 
   pos        IN   PLS_INTEGER := NULL);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| rcpath | VARCHAR2 | IN | Absolute path of the resource configuration to be inserted. An exception is raised if rcpath already exists in the target's configuration list. |
| pos | PLS_INTEGER | IN | Index at which the new configuration is to be inserted. If this parameter is not specified then the new configuration is appended to the end of the list. An exception is raised if the index is out of range ( pos < 0 or pos > the size of the target resource's configuration list). |

## Usage Notes

Syntax DBMS_RESCONFIG.ADDREPOSITORYRESCONFIG( rcpath IN VARCHAR2, pos IN PLS_INTEGER := NULL); Parameters Table 141-2 ADDREPOSITORYRESCONFIG Function Parameters Parameter Description rcpath Absolute path of the resource configuration to be inserted. An exception is raised if rcpath already exists in the target's configuration list. pos Index at which the new configuration is to be inserted. If this parameter is not specified then the new configuration is appended to the end of the list. An exception is raised if the index is out of range ( pos < 0 or pos > the size of the target resource's configuration list). Usage Notes An error is raised if the document referenced by rcpath is not based on XDBResConfig . xsd schema. Users must have XDBADMIN role and READ privilege on the resource configuration to be inserted; otherwise, an error is returned.