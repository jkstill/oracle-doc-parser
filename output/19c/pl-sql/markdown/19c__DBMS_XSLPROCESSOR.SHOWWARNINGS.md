---
id: 19c__DBMS_XSLPROCESSOR.SHOWWARNINGS
name: DBMS_XSLPROCESSOR.SHOWWARNINGS
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XSLPROCESSOR
tags: [dbms_xslprocessor]
source_file: DBMS_XSLPROCESSOR.html
---

# DBMS_XSLPROCESSOR.SHOWWARNINGS

This procedure turns warnings on (TRUE) or off (FALSE) .

## Syntax

```sql
DBMS_XSLPROCESSOR.SHOWWARNINGS(
   p     IN   Processor,
   yes   IN   BOOLEAN);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| p | Processor | IN | Processor instance |
| yes | BOOLEAN) | IN | Mode to set: TRUE to show warnings, FALSE otherwise |

## Usage Notes

Syntax DBMS_XSLPROCESSOR.SHOWWARNINGS( p IN Processor, yes IN BOOLEAN); Parameters Table 216-14 SHOWWARNINGS Procedure Parameters Parameter Description p Processor instance yes Mode to set: TRUE to show warnings, FALSE otherwise