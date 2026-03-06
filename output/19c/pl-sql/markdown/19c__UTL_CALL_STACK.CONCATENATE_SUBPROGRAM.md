---
id: 19c__UTL_CALL_STACK.CONCATENATE_SUBPROGRAM
name: UTL_CALL_STACK.CONCATENATE_SUBPROGRAM
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: UTL_CALL_STACK
tags: [utl_call_stack]
source_file: UTL_CALL_STACK.html
---

# UTL_CALL_STACK.CONCATENATE_SUBPROGRAM

This function returns a concatenated form of a unit-qualified name.

## Syntax

```sql
UTL_CALL_STACK.CONCATENATE_SUBPROGRAM (
   qualified_name    IN    UNIT_QUALIFIED_NAME) 
 RETURN VARCHAR2;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| qualified_name | UNIT_QUALIFIED_NAME) | IN | A unit-qualified name |

**Returns:** `VARCHAR2`

## Usage Notes

Syntax UTL_CALL_STACK.CONCATENATE_SUBPROGRAM ( qualified_name IN UNIT_QUALIFIED_NAME) RETURN VARCHAR2; Parameters Table 259-6 CONCATENATE_SUBPROGRAM Function Parameters Parameter Description qualified_name A unit-qualified name Return Values A string of the form UNIT.SUBPROGRAM.LOCAL_SUBPROGRAM