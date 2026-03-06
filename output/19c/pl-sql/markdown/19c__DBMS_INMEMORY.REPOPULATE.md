---
id: 19c__DBMS_INMEMORY.REPOPULATE
name: DBMS_INMEMORY.REPOPULATE
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_INMEMORY
tags: [dbms_inmemory]
source_file: DBMS_INMEMORY.html
---

# DBMS_INMEMORY.REPOPULATE

This procedure forces repopulation of a table, partition, or subpartition that is currently populated in the IM column store.

## Syntax

```sql
DBMS_INMEMORY.REPOPULATE(
   schema_name      IN    VARCHAR2,
   table_name       IN    VARCHAR2,
   subobject_name   IN    VARCHAR2 DEFAULT NULL,
   force            IN    BOOLEAN DEFAULT FALSE);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| schema_name | VARCHAR2 | IN | Name of the schema that owns the object. |
| table_name | VARCHAR2 | IN | Name of the table requiring repopulation. |
| subobject_name | VARCHAR2 | IN | Name of the partition or subpartition. If null, then repopulate the entire table. |
| force | BOOLEAN | IN | Whether to repopulate all IMCUs in the segment, just as in initial population. The following values are possible for the force parameter: FALSE — The database repopulates only IMCUs containing modified rows. This is the default. TRUE — The database drops the segment, and then rebuilds it. The database increments the statistics and performs all other tasks related to initial population. For example, IMCU 1 contains rows 1 to 500,000, and IMCU 2 contains rows 500,001 to 1,000,000. A statement modifies row 600,000. When force is FALSE , the database only repopulates IMCU 2. When force is TRUE , the database repopulates both IMCUs. Consider further that the INMEMORY_VIRTUAL_COLUMNS initialization parameter is set to ENABLE , and an application creates a new virtual column. When force is FALSE , the database only repopulates IMCU 2 with the new column. When force is TRUE , the database repopulates both IMCUs with the new column. |

## Usage Notes

Syntax DBMS_INMEMORY.REPOPULATE( schema_name IN VARCHAR2, table_name IN VARCHAR2, subobject_name IN VARCHAR2 DEFAULT NULL, force IN BOOLEAN DEFAULT FALSE); Parameters Table 89-4 REPOPULATE Procedure Parameters Parameter Description schema_name Name of the schema that owns the object. table_name Name of the table requiring repopulation. subobject_name Name of the partition or subpartition. If null, then repopulate the entire table. force Whether to repopulate all IMCUs in the segment, just as in initial population. The following values are possible for the force parameter: FALSE — The database repopulates only IMCUs containing modified rows. This is the default. TRUE — The database drops the segment, and then rebuilds it. The database increments the statistics and performs all other tasks related to initial population. For example, IMCU 1 contains rows 1 to 500,000, and IMCU 2 contains rows 500,001 to 1,000,000. A statement modifies row 600,000. When force is FALSE , the database only repopulates IMCU 2. When force is TRUE , the database repopulates both IMCUs. Consider further that the INMEMORY_VIRTUAL_COLUMNS initialization parameter is set to ENABLE , and an application creates a new virtual column. When force is FALSE , the database only repopulates IMCU 2 with the new column. When force is TRUE , the database repopulates both IMCUs with the new column.