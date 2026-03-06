---
id: 19c__HTF.OLISTOPEN
name: HTF.OLISTOPEN
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: HTF
tags: [htf]
source_file: HTF.html
---

# HTF.OLISTOPEN

This function generates the <OL> tag which marks the beginning of an ordered list. An ordered list presents a list of numbered items.

## Syntax

```sql
HTF.OLISTOPEN(
   cclear         IN       VARCHAR2   DEFAULT NULL,
   cwrap          IN       VARCHAR2   DEFAULT NULL,
   cattributes    IN       VARCHAR2   DEFAULT NULL)
  RETURN VARCHAR2;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| cclear | VARCHAR2 | IN | The value for the CLEAR attribute. |
| cwrap | VARCHAR2 | IN | The value for the WRAP attribute. |
| cattributes | VARCHAR2 | IN | The other attributes to be included as-is in the tag. |

**Returns:** `VARCHAR2`

## Usage Notes

To mark the end of a list of this kind, use the OLISTCLOSE Function . Numbered items are added using LISTITEM Function . Syntax HTF.OLISTOPEN( cclear IN VARCHAR2 DEFAULT NULL, cwrap IN VARCHAR2 DEFAULT NULL, cattributes IN VARCHAR2 DEFAULT NULL) RETURN VARCHAR2; Parameters Table 220-66 OLISTOPEN Function Parameters Parameter Description cclear The value for the CLEAR attribute. cwrap The value for the WRAP attribute. cattributes The other attributes to be included as-is in the tag. Examples This function generates <OL CLEAR="cclear" WRAP="cwrap" cattributes>