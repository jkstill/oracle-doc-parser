---
id: 19c__DBMS_DATA_MINING.DROP_ALGORITHM
name: DBMS_DATA_MINING.DROP_ALGORITHM
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_DATA_MINING
tags: [dbms_data_mining]
source_file: DBMS_DATA_MINING.html
---

# DBMS_DATA_MINING.DROP_ALGORITHM

This function is used to drop the registered algorithm information.

## Syntax

```sql
DBMS_DATA_MINING.DROP_ALGORITHM (algorithm_name  IN  VARCHAR2(30),
                                 cascade         IN  BOOLEAN default FALSE)
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| algorithm_name | VARCHAR2(30) | IN | Name of the algorithm. |
| cascade | BOOLEAN | IN | If the cascade option is TRUE , all the models with this algorithms are forced to drop. There after, the algorithm is dropped. The default value is FALSE . |

## Usage Notes

Syntax DBMS_DATA_MINING.DROP_ALGORITHM (algorithm_name IN VARCHAR2(30), cascade IN BOOLEAN default FALSE) Parameters Table 47-64 DROP_ALGORITHM Procedure Parameters Parameter Description algorithm_name Name of the algorithm. cascade If the cascade option is TRUE , all the models with this algorithms are forced to drop. There after, the algorithm is dropped. The default value is FALSE . Usage Note To drop a mining model, you must be the owner or you must have the RQADMIN privilege. See Oracle Data Mining User's Guide for information about privileges for data mining. Make sure a model is not built on the algorithm, then drop the algorithm from the system table. If you try to drop an algorithm with a model built on it, then an error is displayed.