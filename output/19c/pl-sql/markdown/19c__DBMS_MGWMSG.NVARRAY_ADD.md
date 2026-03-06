---
id: 19c__DBMS_MGWMSG.NVARRAY_ADD
name: DBMS_MGWMSG.NVARRAY_ADD
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_MGWMSG
tags: [dbms_mgwmsg]
source_file: DBMS_MGWMSG.html
---

# DBMS_MGWMSG.NVARRAY_ADD

This procedure appends a name-value element to the end of a name-value array.

## Syntax

```sql
DBMS_MGWMSG.NVARRAY_ADD (
   p_array  IN OUT SYS.MGW_NAME_VALUE_ARRAY_T,
   p_value  IN     SYS.MGW_NAME_VALUE_T );
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| p_array | SYS.MGW_NAME_VALUE_ARRAY_T | IN OUT | On input, the name-value array instance to modify. If NULL, then a new array is created. On output, the modified name-value array instance. |
| p_value | SYS.MGW_NAME_VALUE_T | IN | The value to add. If NULL , then p_array is not changed. |

## Usage Notes

Syntax DBMS_MGWMSG.NVARRAY_ADD ( p_array IN OUT SYS.MGW_NAME_VALUE_ARRAY_T, p_value IN SYS.MGW_NAME_VALUE_T ); Parameters Table 111-23 NVARRAY_ADD Procedure Parameters Parameter Description p_array On input, the name-value array instance to modify. If NULL, then a new array is created. On output, the modified name-value array instance. p_value The value to add. If NULL , then p_array is not changed.