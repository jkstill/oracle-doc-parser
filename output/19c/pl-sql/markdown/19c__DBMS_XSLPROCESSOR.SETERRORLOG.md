---
id: 19c__DBMS_XSLPROCESSOR.SETERRORLOG
name: DBMS_XSLPROCESSOR.SETERRORLOG
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XSLPROCESSOR
tags: [dbms_xslprocessor]
source_file: DBMS_XSLPROCESSOR.html
---

# DBMS_XSLPROCESSOR.SETERRORLOG

This deprecated procedure sets errors to be sent to the specified file.

## Syntax

```sql
DBMS_XSLPROCESSOR.SETERRORLOG(
   p         IN   Processor,
   fileName  IN   VARCHAR2);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| p | Processor | IN | Processor instance |
| fileName | VARCHAR2) | IN | Complete path of the file to use as the error log |

## Usage Notes

Note: This subprogram has been deprecated, and is included only for reasons of backward compatibility. Note: This subprogram has been deprecated, and is included only for reasons of backward compatibility. Syntax DBMS_XSLPROCESSOR.SETERRORLOG( p IN Processor, fileName IN VARCHAR2); Parameters Table 216-12 SETERRORLOG Procedure Parameters Parameter Description p Processor instance fileName Complete path of the file to use as the error log