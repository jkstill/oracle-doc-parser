---
id: 19c__DBMS_ADVISOR.UPDATE_OBJECT
name: DBMS_ADVISOR.UPDATE_OBJECT
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_ADVISOR
tags: [dbms_advisor]
source_file: DBMS_ADVISOR.html
---

# DBMS_ADVISOR.UPDATE_OBJECT

This procedure updates an existing task object.

## Syntax

```sql
DBMS_ADVISOR.UPDATE_OBJECT (
   task_name       IN VARCHAR2
   object_id       IN NUMBER,
   attr1           IN VARCHAR2 := NULL,
   attr2           IN VARCHAR2 := NULL,
   attr3           IN VARCHAR2 := NULL,
   attr4           IN CLOB := NULL,
   attr5           IN VARCHAR2 := NULL);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| task_name | VARCHAR2 | IN | A valid advisor task name that uniquely identifies an existing task. |
| object_id | NUMBER | IN | The advisor-assigned object identifier. |
| attr1 | VARCHAR2 | IN | Advisor-specific data. If set to NULL , there will be no effect on the target object. |
| attr2 | VARCHAR2 | IN | Advisor-specific data. If set to NULL , there will be no effect on the target object. |
| attr3 | VARCHAR2 | IN | Advisor-specific data. If set to NULL , there will be no effect on the target object. |
| attr4 | CLOB | IN | Advisor-specific data. If set to NULL , there will be no effect on the target object. |
| attr5 | VARCHAR2 | IN | Advisor-specific data. If set to null, there will be no effect on the target object. |

## Usage Notes

Task objects are typically used as input data for a particular advisor. Segment advice can be generated at the object, segment, or tablespace level. Syntax DBMS_ADVISOR.UPDATE_OBJECT ( task_name IN VARCHAR2 object_id IN NUMBER, attr1 IN VARCHAR2 := NULL, attr2 IN VARCHAR2 := NULL, attr3 IN VARCHAR2 := NULL, attr4 IN CLOB := NULL, attr5 IN VARCHAR2 := NULL); Parameters Table 16-41 UPDATE_OBJECT Procedure Parameters Parameter Description task_name A valid advisor task name that uniquely identifies an existing task. object_id The advisor-assigned object identifier. attr1 Advisor-specific data. If set to NULL , there will be no effect on the target object. attr2 Advisor-specific data. If set to NULL , there will be no effect on the target object. attr3 Advisor-specific data. If set to NULL , there will be no effect on the target object. attr4 Advisor-specific data. If set to NULL , there will be no effect on the target object. attr5 Advisor-specific data. If set to null, there will be no effect on the target object. The attribute parameters have different values depending upon the object type. See Oracle Database Administrator's Guide for details regarding these parameters and object types. Usage Notes If for the object level, advice is generated on all partitions of the object (if the object is partitioned). The advice is not cascaded to any dependent objects. If for the segment level, advice can be obtained on a single segment, such as the partition or subpartition of a table, index, or lob column. If for a tablespace level, target advice for every segment in the tablespace will be generated. Examples DECLARE task_id NUMBER; task_name VARCHAR2(30); obj_id NUMBER; BEGIN task_name := 'My Task'; DBMS_ADVISOR.CREATE_TASK(DBMS_ADVISOR.SQLACCESS_ADVISOR, task_id, task_name); DBMS_ADVISOR.CREATE_OBJECT (task_name,'SQL',NULL,NULL,NULL, 'SELECT * FROM SH.SALES',obj_id); DBMS_ADVISOR.UPDATE_OBJECT (task_name, obj_id,NULL,NULL,NULL, 'SELECT count(*) FROM SH.SALES'); END; / See Also: Oracle Database Administrator’s Guide for further information regarding the Segment Advisor