---
id: 19c__OWA_TEXT.ADD2MULTI
name: OWA_TEXT.ADD2MULTI
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: OWA_TEXT
tags: [owa_text]
source_file: OWA_TEXT.html
---

# OWA_TEXT.ADD2MULTI

This procedure adds content to an existing Multi_Line Data Type

## Syntax

```sql
OWA_TEXT.ADD2MULTI(
   stream         IN       VARCHAR2,
   mline          IN OUT   multi_line,
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| stream | VARCHAR2 | IN | The text to add. |
| mline | multi_line | IN OUT | The OWA_TEXT.MULTI_LINE DATA TYPE . The output of this parameter contains stream . |
| continue |  |  | If TRUE , the procedure appends stream within the previous final row (assuming it is less than 32K). If FALSE , the procedure places stream in a new row. |

## Usage Notes

Syntax OWA_TEXT.ADD2MULTI( stream IN VARCHAR2, mline IN OUT multi_line, continue IN BOOLEAN DEFAULT TRUE); Parameters Table 229-2 ADD2MULTI Procedure Parameters Parameter Description stream The text to add. mline The OWA_TEXT.MULTI_LINE DATA TYPE . The output of this parameter contains stream . continue If TRUE , the procedure appends stream within the previous final row (assuming it is less than 32K). If FALSE , the procedure places stream in a new row.