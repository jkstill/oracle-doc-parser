---
id: 19c__DBMS_PCLXUTIL.BUILD_PART_INDEX
name: DBMS_PCLXUTIL.BUILD_PART_INDEX
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_PCLXUTIL
tags: [dbms_pclxutil]
source_file: DBMS_PCLXUTIL.html
---

# DBMS_PCLXUTIL.BUILD_PART_INDEX

This procedure provides intra-partition parallelism for creating partition-wise local indexes.

## Syntax

```sql
DBMS_PCLXUTIL.BUILD_PART_INDEX ( 
   jobs_per_batch  IN NUMBER   DEFAULT 1,
   procs_per_job   IN NUMBER   DEFAULT 1, 
   tab_name        IN VARCHAR2 DEFAULT NULL, 
   idx_name        IN VARCHAR2 DEFAULT NULL, 
   force_opt       IN BOOLEAN  DEFAULT FALSE);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| jobs_per_batch | NUMBER | IN | The number of concurrent partition-wise "local index builds". |
| procs_per_job | NUMBER | IN | The number of parallel execution servers to be utilized for each local index build (1 <= procs_per_job <= max_slaves ). |
| tab_name | VARCHAR2 | IN | The name of the partitioned table (an exception is raised if the table does not exist or not partitioned). |
| idx_name | VARCHAR2 | IN | The name given to the local index (an exception is raised if a local index is not created on the table tab_name ). |
| force_opt | BOOLEAN | IN | If TRUE , then force rebuild of all partitioned indexes; otherwise, rebuild only the partitions marked ' UNUSABLE '. |

## Usage Notes

Syntax DBMS_PCLXUTIL.BUILD_PART_INDEX ( jobs_per_batch IN NUMBER DEFAULT 1, procs_per_job IN NUMBER DEFAULT 1, tab_name IN VARCHAR2 DEFAULT NULL, idx_name IN VARCHAR2 DEFAULT NULL, force_opt IN BOOLEAN DEFAULT FALSE); Parameters Table 123-2 BUILD_PART_INDEX Procedure Parameters Parameter Description jobs_per_batch The number of concurrent partition-wise "local index builds". procs_per_job The number of parallel execution servers to be utilized for each local index build (1 <= procs_per_job <= max_slaves ). tab_name The name of the partitioned table (an exception is raised if the table does not exist or not partitioned). idx_name The name given to the local index (an exception is raised if a local index is not created on the table tab_name ). force_opt If TRUE , then force rebuild of all partitioned indexes; otherwise, rebuild only the partitions marked ' UNUSABLE '. Usage Notes This utility can be run only as table owner, and not as any other user. Examples Suppose a table PROJECT is created with two partitions PROJ001 and PROJ002 , along with a local index IDX . A call to the procedure BUILD_PART_INDEX(2,4,'PROJECT','IDX',TRUE) produces the following output: SQLPLUS> EXECUTE dbms_pclxutil.build_part_index(2,4,'PROJECT','IDX',TRUE); Statement processed. INFO: Job #21 created for partition PROJ002 with 4 slaves INFO: Job #22 created for partition PROJ001 with 4 slaves