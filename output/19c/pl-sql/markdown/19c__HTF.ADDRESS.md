---
id: 19c__HTF.ADDRESS
name: HTF.ADDRESS
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: HTF
tags: [htf]
source_file: HTF.html
---

# HTF.ADDRESS

This function generates the <ADDRESS> and </ADDRESS> tags which specify the address, author and signature of a document.

## Syntax

```sql
HTF.ADDRESS (
   cvalue         IN       VARCHAR2
   cnowrap        IN       VARCHAR2   DEFAULT NULL
   cclear         IN       VARCHAR2   DEFAULT NULL
   cattributes    IN       VARCHAR2   DEFAULT NULL)
 RETURN VARCHAR2;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| cvalue | VARCHAR2 | IN | The string that goes between the <ADDRESS> and </ADDRESS> tags. |
| cnowrap | VARCHAR2 | IN | If the value for this parameter is not NULL , the NOWRAP attribute is included in the tag |
| cclear | VARCHAR2 | IN | The value for the CLEAR attribute. |
| cattributes | VARCHAR2 | IN | The other attributes to be included as-is in the tag |

**Returns:** `VARCHAR2`

## Usage Notes

Syntax HTF.ADDRESS ( cvalue IN VARCHAR2 cnowrap IN VARCHAR2 DEFAULT NULL cclear IN VARCHAR2 DEFAULT NULL cattributes IN VARCHAR2 DEFAULT NULL) RETURN VARCHAR2; Parameters Table 220-2 ADDRESS Function Parameters Parameter Description cvalue The string that goes between the <ADDRESS> and </ADDRESS> tags. cnowrap If the value for this parameter is not NULL , the NOWRAP attribute is included in the tag cclear The value for the CLEAR attribute. cattributes The other attributes to be included as-is in the tag Examples This function generates <ADDRESS CLEAR="cclear" NOWRAP cattributes>cvalue</ADDRESS>