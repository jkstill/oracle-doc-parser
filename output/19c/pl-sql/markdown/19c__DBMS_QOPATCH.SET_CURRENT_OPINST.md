---
id: 19c__DBMS_QOPATCH.SET_CURRENT_OPINST
name: DBMS_QOPATCH.SET_CURRENT_OPINST
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_QOPATCH
tags: [dbms_qopatch]
source_file: DBMS_QOPATCH.html
---

# DBMS_QOPATCH.SET_CURRENT_OPINST

This procedure sets the node name and instance to get the inventory details specific to it in an Oracle Real Application Clusters (RAC) environment.

## Syntax

```sql
DBMS_QOPATCH.SET_CURRENT_OPINST (
   node_name    IN VARCHAR2 DEFAULT NULL,
   inst_name    IN VARCHAR2 DEFAULT NULL);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| node_name | VARCHAR2 | IN | Name of node |
| inst_name | VARCHAR2 | IN | Name of instance |

## Usage Notes

Syntax DBMS_QOPATCH.SET_CURRENT_OPINST ( node_name IN VARCHAR2 DEFAULT NULL, inst_name IN VARCHAR2 DEFAULT NULL); Parameters Table 135-15 SET_CURRENT_OPINST Procedure Parameters Parameter Description node_name Name of node inst_name Name of instance