---
id: 19c__HTP.ADDRESS
name: HTP.ADDRESS
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: HTP
tags: [htp]
source_file: HTP.html
---

# HTP.ADDRESS

This procedure generates the <ADDRESS> and </ADDRESS> tags which specify the address, author and signature of a document.

## Syntax

```sql
HTP.ADDRESS (
   cvalue         IN       VARCHAR2
   cnowrap        IN       VARCHAR2   DEFAULT NULL
   cclear         IN       VARCHAR2   DEFAULT NULL
   cattributes    IN       VARCHAR2   DEFAULT NULL);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| cvalue | VARCHAR2 | IN | The string that goes between the <ADDRESS> and </ADDRESS> tags. |
| cnowrap | VARCHAR2 | IN | If the value for this parameter is not NULL , the NOWRAP attribute is included in the tag |
| cclear | VARCHAR2 | IN | The value for the CLEAR attribute. |
| cattributes | VARCHAR2 | IN | The other attributes to be included as-is in the tag |

## Usage Notes

Syntax HTP.ADDRESS ( cvalue IN VARCHAR2 cnowrap IN VARCHAR2 DEFAULT NULL cclear IN VARCHAR2 DEFAULT NULL cattributes IN VARCHAR2 DEFAULT NULL); Parameters Table 221-2 ADDRESS Procedure Parameters Parameter Description cvalue The string that goes between the <ADDRESS> and </ADDRESS> tags. cnowrap If the value for this parameter is not NULL , the NOWRAP attribute is included in the tag cclear The value for the CLEAR attribute. cattributes The other attributes to be included as-is in the tag Examples This procedure generates <ADDRESS CLEAR=" cclear " NOWRAP cattributes > cvalue </ADDRESS>