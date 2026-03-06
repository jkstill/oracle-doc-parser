---
id: 19c__DBMS_ADVISOR.CREATE_OBJECT
name: DBMS_ADVISOR.CREATE_OBJECT
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_ADVISOR
tags: [dbms_advisor]
source_file: DBMS_ADVISOR.html
---

# DBMS_ADVISOR.CREATE_OBJECT

This procedure creates a new task object.

## Syntax

```sql
DBMS_ADVISOR.CREATE_OBJECT (
   task_name         IN VARCHAR2,
   object_type       IN VARCHAR2,
   attr1             IN VARCHAR2 :=  NULL,
   attr2             IN VARCHAR2 :=  NULL,
   attr3             IN VARCHAR2 :=  NULL,
   attr4             IN CLOB     :=  NULL,
   attr5             IN VARCHAR2 :=  NULL,
   object_id         OUT NUMBER,
   attr6             IN VARCHAR2 :=  NULL,
   attr7             IN VARCHAR2 :=  NULL,
   attr8             IN VARCHAR2 :=  NULL,
   attr9             IN VARCHAR2 :=  NULL,
   attr10            IN VARCHAR2 :=  NULL);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| task_name | VARCHAR2 | IN | A valid Advisor task name that uniquely identifies an existing task. |
| object_type | VARCHAR2 | IN | Specifies the external object type. |
| attr1 | VARCHAR2 | IN | Advisor-specific data. |
| attr2 | VARCHAR2 | IN | Advisor-specific data. |
| attr3 | VARCHAR2 | IN | Advisor-specific data. |
| attr4 | CLOB | IN | Advisor-specific data. |
| attr5 | VARCHAR2 | IN | Advisor-specific data. |
| object_id | NUMBER | OUT | The advisor-assigned object identifier. |
| attr6 | VARCHAR2 | IN | Advisor-specific data. |
| attr7 | VARCHAR2 | IN | Advisor-specific data. |
| attr8 | VARCHAR2 | IN | Advisor-specific data. |
| attr9 | VARCHAR2 | IN | Advisor-specific data. |
| attr10 | VARCHAR2 | IN | Advisor-specific data. |

## Usage Notes

Syntax DBMS_ADVISOR.CREATE_OBJECT ( task_name IN VARCHAR2, object_type IN VARCHAR2, attr1 IN VARCHAR2 := NULL, attr2 IN VARCHAR2 := NULL, attr3 IN VARCHAR2 := NULL, attr4 IN CLOB := NULL, attr5 IN VARCHAR2 := NULL, object_id OUT NUMBER, attr6 IN VARCHAR2 := NULL, attr7 IN VARCHAR2 := NULL, attr8 IN VARCHAR2 := NULL, attr9 IN VARCHAR2 := NULL, attr10 IN VARCHAR2 := NULL); Parameters Table 16-8 CREATE_OBJECT Procedure Parameters Parameter Description task_name A valid Advisor task name that uniquely identifies an existing task. object_type Specifies the external object type. attr1 Advisor-specific data. attr2 Advisor-specific data. attr3 Advisor-specific data. attr4 Advisor-specific data. attr5 Advisor-specific data. object_id The advisor-assigned object identifier. attr6 Advisor-specific data. attr7 Advisor-specific data. attr8 Advisor-specific data. attr9 Advisor-specific data. attr10 Advisor-specific data. The attribute parameters have different values depending upon the object type. See Oracle Database Administrator's Guide for details regarding these parameters and object types. Return Values Returns the new object identifier. Usage Notes Task objects are typically used as input data for a particular advisor. Segment advice can be generated at the object, segment, or tablespace level. If for the object level, advice is generated on all partitions of the object (if the object is partitioned). The advice is not cascaded to any dependent objects. If for the segment level, advice can be obtained on a single segment, such as the partition or subpartition of a table, index, or LOB column. If for a tablespace level, target advice for every segment in the tablespace will be generated. See Oracle Database Administrator's Guide for further information regarding the Segment Advisor. Examples DECLARE task_id NUMBER; task_name VARCHAR2(30); obj_id NUMBER; BEGIN task_name := 'My Task'; DBMS_ADVISOR.CREATE_TASK(DBMS_ADVISOR.SQLACCESS_ADVISOR, task_id, task_name); DBMS_ADVISOR.CREATE_OBJECT (task_name,'SQL',NULL,NULL,NULL, 'SELECT * FROM TEST_TAB',NULL,obj_id,NULL,NULL,NULL,NULL,NULL); END; /