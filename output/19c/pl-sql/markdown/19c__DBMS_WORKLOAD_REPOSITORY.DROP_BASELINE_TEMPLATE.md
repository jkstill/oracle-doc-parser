---
id: 19c__DBMS_WORKLOAD_REPOSITORY.DROP_BASELINE_TEMPLATE
name: DBMS_WORKLOAD_REPOSITORY.DROP_BASELINE_TEMPLATE
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_WORKLOAD_REPOSITORY
tags: [dbms_workload_repository]
source_file: DBMS_WORKLOAD_REPOSITORY.html
---

# DBMS_WORKLOAD_REPOSITORY.DROP_BASELINE_TEMPLATE

This procedure removes a template that is no longer needed.

## Syntax

```sql
DBMS_WORKLOAD_REPOSITORY.DROP_BASELINE_TEMPLATE(
   template_name    IN VARCHAR2,   
   dbid             IN NUMBER   DEFAULT NULL);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| template_name | VARCHAR2 | IN | Name of the template to remove |
| dbid | NUMBER | IN | Database ID for which the baseline template needs to be dropped. If NULL , this takes the database identifier of the local database. Defaults to NULL . |

## Usage Notes

Syntax DBMS_WORKLOAD_REPOSITORY.DROP_BASELINE_TEMPLATE( template_name IN VARCHAR2, dbid IN NUMBER DEFAULT NULL); Parameters Table 192-32 DROP_BASELINE_TEMPLATE Procedure Parameters Parameter Description template_name Name of the template to remove dbid Database ID for which the baseline template needs to be dropped. If NULL , this takes the database identifier of the local database. Defaults to NULL .