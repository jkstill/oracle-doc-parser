---
id: 19c__DBMS_RESCONFIG.ADDRESCONFIG
name: DBMS_RESCONFIG.ADDRESCONFIG
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_RESCONFIG
tags: [dbms_resconfig]
source_file: DBMS_RESCONFIG.html
---

# DBMS_RESCONFIG.ADDRESCONFIG

This procedure inserts the resource configuration specified by the absolute path of the resource configuration at the given position in the target resource's configuration list. It shifts the element currently at that position (if any) and any subsequent elements to the right.

## Syntax

```sql
DBMS_RESCONFIG.ADDRESCONFIG(
   respath    IN   VARCHAR2, 
   rcpath     IN   VARCHAR2, 
   pos        IN   PLS_INTEGER := NULL);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| respath | VARCHAR2 | IN | Absolute path of the target resource |
| rcpath | VARCHAR2 | IN | Absolute path of the resource configuration to be inserted. An exception is raised if rcpath already exists in the target's configuration list. |
| pos | PLS_INTEGER | IN | Index at which the new configuration is to be inserted. If this parameter is not specified then the new configuration is appended to the end of the list. An exception is raised if the index is out of range ( pos < 0 or pos > the size of the target resource's configuration list). |

## Usage Notes

Syntax DBMS_RESCONFIG.ADDRESCONFIG( respath IN VARCHAR2, rcpath IN VARCHAR2, pos IN PLS_INTEGER := NULL); Parameters Table 141-3 ADDRESCONFIG Function Parameters Parameter Description respath Absolute path of the target resource rcpath Absolute path of the resource configuration to be inserted. An exception is raised if rcpath already exists in the target's configuration list. pos Index at which the new configuration is to be inserted. If this parameter is not specified then the new configuration is appended to the end of the list. An exception is raised if the index is out of range ( pos < 0 or pos > the size of the target resource's configuration list). Usage Notes An error is raised if the document referenced by rcpath is not based on XDBResConfig . xsd schema. Users must have WRITE -CONFIG privilege on the target resource and read privilege on the resource configuration to be inserted; otherwise, an error is returned.