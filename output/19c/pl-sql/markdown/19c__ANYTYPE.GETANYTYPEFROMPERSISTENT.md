---
id: 19c__ANYTYPE.GETANYTYPEFROMPERSISTENT
name: ANYTYPE.GETANYTYPEFROMPERSISTENT
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: ANYTYPE
tags: [anytype]
source_file: ANYTYPE-TYPE.html
---

# ANYTYPE.GETANYTYPEFROMPERSISTENT

This standalone function returns an ANYTYPE corresponding to a persistent type created earlier using the CREATE TYPE SQL statement. Starting with Oracle Database 19c, the GETANYTYPEFROMPERSISTENT function replaces the GETPERISTENT static function.

## Syntax

```sql
GETANYTYPEFROMPERSISTENT(
   schema_name      IN VARCHAR2,
   type_name        IN VARCHAR2)
RETURN           ANYTYPE;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| schema_name | VARCHAR2 | IN | Schema name of the type. |
| type_name | VARCHAR2) | IN | Type name. |

**Returns:** `ANYTYPE`

## Usage Notes

Syntax GETANYTYPEFROMPERSISTENT( schema_name IN VARCHAR2, type_name IN VARCHAR2) RETURN ANYTYPE; Parameters Table 282-9 GETANYTYPEFROMPERSISTENT Function Parameters Parameter Description schema_name Schema name of the type. type_name Type name. Return Values An ANYTYPE corresponding to a persistent type created earlier using the CREATE TYPE SQL statement.