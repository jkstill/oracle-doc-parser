---
id: 19c__DBMS_SPACE.CREATE_INDEX_COST
name: DBMS_SPACE.CREATE_INDEX_COST
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_SPACE
tags: [dbms_space]
source_file: DBMS_SPACE.html
---

# DBMS_SPACE.CREATE_INDEX_COST

This procedure determines the cost of creating an index on an existing table. The input is the DDL statement that will be used to create the index. The procedure will output the storage required to create the index.

## Syntax

```sql
DBMS_SPACE.CREATE_INDEX_COST (
   ddl             IN    VARCHAR2,
   used_bytes      OUT   NUMBER,
   alloc_bytes     OUT   NUMBER,
   plan_table      IN    VARCHAR2 DEFAULT NULL);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| ddl | VARCHAR2 | IN | The create index DDL statement |
| used_bytes | NUMBER | OUT | The number of bytes representing the actual index data |
| alloc_bytes | NUMBER | OUT | Size of the index when created in the tablespace |
| plan_table | VARCHAR2 | IN | Which plan table to use, default NULL |

## Usage Notes

Syntax DBMS_SPACE.CREATE_INDEX_COST ( ddl IN VARCHAR2, used_bytes OUT NUMBER, alloc_bytes OUT NUMBER, plan_table IN VARCHAR2 DEFAULT NULL); Pragmas pragma restrict_references(create_index_cost,WNDS); Parameters Table 158-6 CREATE_INDEX_COST Procedure Parameters Parameter Description ddl The create index DDL statement used_bytes The number of bytes representing the actual index data alloc_bytes Size of the index when created in the tablespace plan_table Which plan table to use, default NULL Usage Notes The table on which the index is created must already exist. The computation of the index size depends on statistics gathered on the segment. It is imperative that the table must have been analyzed recently. In the absence of correct statistics, the results may be inaccurate, although the procedure will not raise any errors.