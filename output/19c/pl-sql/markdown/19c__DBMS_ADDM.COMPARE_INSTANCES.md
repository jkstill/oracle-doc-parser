---
id: 19c__DBMS_ADDM.COMPARE_INSTANCES
name: DBMS_ADDM.COMPARE_INSTANCES
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_ADDM
tags: [dbms_addm]
source_file: DBMS_ADDM.html
---

# DBMS_ADDM.COMPARE_INSTANCES

This function produces a Compare Period ADDM report comparing the performance of a single instance over two different time periods or the performance of two different instances over two different time periods.

## Syntax

```sql
DBMS_ADDM.COMPARE_INSTANCES (
   base_dbid             IN NUMBER := NULL,
   base_instance_id      IN NUMBER
   base_begin_snap_id    IN NUMBER,
   base_end_snap_id      IN NUMBER,
   comp_dbid             IN NUMBER := NULL,
   comp_instance_id      IN NUMBER,
   comp_begin_snap_id    IN NUMBER,
   comp_end_snap_id      IN  NUMBER,
   report_type           IN VARCHAR2 := 'HTML')
  RETURN CLOB;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| base_dbid | NUMBER | IN | Database id ( DBID ) of the base period. The base period is the baseline period that we compare to in order to determine improvement or regression. |
| base_instance_id | NUMBER | IN | Instance number of the database instance to include from the base period |
| base_begin_snap_id | NUMBER | IN | Begin AWR snapshot ID of the base period. |
| base_end_snap_id | NUMBER | IN | End AWR snapshot ID of the base period. |
| comp_dbid | NUMBER | IN | Database id ( DBID ) of the comparison period. The comparison period is the period we compare to the base period. |
| comp_instance_id | NUMBER | IN | Instance number of the database instance to include from the comparison period |
| comp_begin_snap_id | NUMBER | IN | Begin AWR snapshot ID of the comparison period |
| comp_end_snap_id | NUMBER | IN | End AWR snapshot ID of the comparison period |
| report_type | VARCHAR2 | IN | 'HTML' (the default) for an HTML active report, 'XML' for an XML report |

**Returns:** `CLOB`

## Usage Notes

The AWR data must reside in the same database, but it can originate from different databases. The function generates a report in either XML or HTML(Active Report) format. Syntax DBMS_ADDM.COMPARE_INSTANCES ( base_dbid IN NUMBER := NULL, base_instance_id IN NUMBER base_begin_snap_id IN NUMBER, base_end_snap_id IN NUMBER, comp_dbid IN NUMBER := NULL, comp_instance_id IN NUMBER, comp_begin_snap_id IN NUMBER, comp_end_snap_id IN NUMBER, report_type IN VARCHAR2 := 'HTML') RETURN CLOB; Parameters Table 14-7 COMPARE_INSTANCES Function Parameters Parameter Description base_dbid Database id ( DBID ) of the base period. The base period is the baseline period that we compare to in order to determine improvement or regression. base_instance_id Instance number of the database instance to include from the base period base_begin_snap_id Begin AWR snapshot ID of the base period. base_end_snap_id End AWR snapshot ID of the base period. comp_dbid Database id ( DBID ) of the comparison period. The comparison period is the period we compare to the base period. comp_instance_id Instance number of the database instance to include from the comparison period comp_begin_snap_id Begin AWR snapshot ID of the comparison period comp_end_snap_id End AWR snapshot ID of the comparison period report_type 'HTML' (the default) for an HTML active report, 'XML' for an XML report Return Values A CLOB containing a compare period ADDM report