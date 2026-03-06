---
id: 19c__DBMS_RESUMABLE.SPACE_ERROR_INFO
name: DBMS_RESUMABLE.SPACE_ERROR_INFO
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_RESUMABLE
tags: [dbms_resumable]
source_file: DBMS_RESUMABLE.html
---

# DBMS_RESUMABLE.SPACE_ERROR_INFO

This function looks for space-related errors in the error stack.

## Syntax

```sql
DBMS_RESUMABLE.SPACE_ERROR_INFO
   error_type        OUT VARCHAR2, 
   object_type       OUT VARCHAR2, 
   object_owner      OUT VARCHAR2, 
   table_space_name  OUT VARCHAR2, 
   object_name       OUT VARCHAR2, 
   sub_object_name   OUT VARCHAR2) 
RETURN BOOLEAN;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| error_type | VARCHAR2 | OUT | The space error type. It will be one of the following: NO MORE SPACE MAX EXTENTS REACHED SPACE QUOTA EXCEEDED |
| object_type | VARCHAR2 | OUT | The object type. It will be one of the following: TABLE INDEX CLUSTER TABLE SPACE ROLLBACK SEGMENT UNDO SEGMENT LOB SEGMENT TEMP SEGMENT INDEX PARTITION TABLE PARTITION LOB PARTITION TABLE SUBPARTITION INDEX SUBPARTITION LOB SUBPARTITION The type can also be NULL if it does not apply. |
| object_owner | VARCHAR2 | OUT | The owner of the object. NULL if it cannot be determined. |
| table_space_name | VARCHAR2 | OUT | The table space where the object resides. NULL if it cannot be determined. |
| object_name | VARCHAR2 | OUT | The name of rollback segment, temp segment, table, index, or cluster. |
| sub_object_name | VARCHAR2) | OUT | The partition name or sub-partition name of LOB, TABLE, or INDEX. NULL if it cannot be determined. |

**Returns:** `BOOLEAN`

## Usage Notes

If it cannot find a space related error, it will return FALSE. Otherwise, TRUE is returned and information about the particular object that causes the space error is returned. Syntax DBMS_RESUMABLE.SPACE_ERROR_INFO error_type OUT VARCHAR2, object_type OUT VARCHAR2, object_owner OUT VARCHAR2, table_space_name OUT VARCHAR2, object_name OUT VARCHAR2, sub_object_name OUT VARCHAR2) RETURN BOOLEAN; Parameters Table 145-8 SPACE_ERROR_INFO Function Parameters Parameter Description error_type The space error type. It will be one of the following: NO MORE SPACE MAX EXTENTS REACHED SPACE QUOTA EXCEEDED object_type The object type. It will be one of the following: TABLE INDEX CLUSTER TABLE SPACE ROLLBACK SEGMENT UNDO SEGMENT LOB SEGMENT TEMP SEGMENT INDEX PARTITION TABLE PARTITION LOB PARTITION TABLE SUBPARTITION INDEX SUBPARTITION LOB SUBPARTITION The type can also be NULL if it does not apply. object_owner The owner of the object. NULL if it cannot be determined. table_space_name The table space where the object resides. NULL if it cannot be determined. object_name The name of rollback segment, temp segment, table, index, or cluster. sub_object_name The partition name or sub-partition name of LOB, TABLE, or INDEX. NULL if it cannot be determined.