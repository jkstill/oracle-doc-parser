---
id: 19c__OWA_IMAGE.GET_X
name: OWA_IMAGE.GET_X
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: OWA_IMAGE
tags: [owa_image]
source_file: OWA_IMAGE.html
---

# OWA_IMAGE.GET_X

This function returns the X coordinate of the point where the user clicked on an image map.

## Syntax

```sql
OWA_IMAGE.GET_X(
   p        IN        point)
 RETURN INTEGER;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| p | point) | IN | The point where the user clicked. |

**Returns:** `INTEGER`

## Usage Notes

Syntax OWA_IMAGE.GET_X( p IN point) RETURN INTEGER; Parameters Table 225-2 GET_X Function Parameters Parameter Description p The point where the user clicked. Return Values The X coordinate as an integer.