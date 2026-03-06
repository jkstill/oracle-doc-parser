---
id: 19c__DBMS_UTILITY.ANALYZE_PART_OBJECT
name: DBMS_UTILITY.ANALYZE_PART_OBJECT
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_UTILITY
tags: [dbms_utility]
source_file: DBMS_UTILITY.html
---

# DBMS_UTILITY.ANALYZE_PART_OBJECT

This procedure is equivalent to SQL: "ANALYZE TABLE|INDEX [<schema>.]<object_name> PARTITION <pname> [<command_type>] [<command_opt>] [<sample_clause>]

## Syntax

```sql
DBMS_UTILITY.ANALYZE_PART_OBJECT (
   schema        IN VARCHAR2 DEFAULT NULL,
   object_name   IN VARCHAR2 DEFAULT NULL,
   object_type   IN CHAR     DEFAULT 'T',
   command_type  IN CHAR     DEFAULT 'E',
   command_opt   IN VARCHAR2 DEFAULT NULL,
   sample_clause IN VARCHAR2 DEFAULT 'sample 5 percent ');
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| schema | VARCHAR2 | IN | Schema of the object_name |
| object_name | VARCHAR2 | IN | Name of object to be analyzed, must be partitioned |
| object_type | CHAR | IN | Type of object, must be T (table) or I (index) |
| command_type | CHAR | IN | Must be V (validate structure) |
| command_opt | VARCHAR2 | IN | Other options for the command type. For C , E it can be FOR table, FOR all LOCAL indexes, FOR all columns or combination of some of the 'for' options of analyze statistics (table). For V , it can be CASCADE when object_type is T. |
| sample_clause | VARCHAR2 | IN | Sample clause to use when command_type is ' E ' |

## Usage Notes

Note: This subprogram has been deprecated and replaced by improved technology. It is maintained only for purposes of backward compatibility. As an alternative, you can use DBMS_STATS to gather statistics. Note: This subprogram has been deprecated and replaced by improved technology. It is maintained only for purposes of backward compatibility. As an alternative, you can use DBMS_STATS to gather statistics. Syntax DBMS_UTILITY.ANALYZE_PART_OBJECT ( schema IN VARCHAR2 DEFAULT NULL, object_name IN VARCHAR2 DEFAULT NULL, object_type IN CHAR DEFAULT 'T', command_type IN CHAR DEFAULT 'E', command_opt IN VARCHAR2 DEFAULT NULL, sample_clause IN VARCHAR2 DEFAULT 'sample 5 percent '); Parameters Table 187-7 ANALYZE_PART_OBJECT Procedure Parameters Parameter Description schema Schema of the object_name object_name Name of object to be analyzed, must be partitioned object_type Type of object, must be T (table) or I (index) command_type Must be V (validate structure) command_opt Other options for the command type. For C , E it can be FOR table, FOR all LOCAL indexes, FOR all columns or combination of some of the 'for' options of analyze statistics (table). For V , it can be CASCADE when object_type is T. sample_clause Sample clause to use when command_type is ' E ' Usage Notes For each partition of the object, run in parallel using job queues.