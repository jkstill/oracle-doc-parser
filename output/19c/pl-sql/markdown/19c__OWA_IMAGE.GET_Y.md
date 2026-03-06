---
id: 19c__OWA_IMAGE.GET_Y
name: OWA_IMAGE.GET_Y
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: OWA_IMAGE
tags: [owa_image]
source_file: OWA_IMAGE.html
---

# OWA_IMAGE.GET_Y

This function returns the Y coordinate of the point where the user clicked on an image map.

## Syntax

```sql
OWA_IMAGE.GET_Y(
   p        IN        point)
 RETURN INTEGER;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| p | point) | IN | The point where the user clicked. |

**Returns:** `INTEGER`

## Usage Notes

Syntax OWA_IMAGE.GET_Y( p IN point) RETURN INTEGER; Parameters Table 225-3 GET_Y Function Parameters Parameter Description p The point where the user clicked. Return Values The Y coordinate as an integer.