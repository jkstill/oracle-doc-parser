---
id: 19c__DBMS_XMLDOM.SETSTANDALONE
name: DBMS_XMLDOM.SETSTANDALONE
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XMLDOM
tags: [dbms_xmldom]
source_file: DBMS_XMLDOM.html
---

# DBMS_XMLDOM.SETSTANDALONE

This procedure sets the standalone property of the DOMDOCUMENT .

## Syntax

```sql
DBMS_XMLDOM.SETSTANDALONE(
   doc         IN     DOMDOCUMENT,
   newvalue    IN     VARCHAR2);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| doc | DOMDOCUMENT | IN | DOMDOCUMENT |
| newvalue | VARCHAR2) | IN | Value of the standalone property of the document |

## Usage Notes

See Also: DOMDocument Subprograms See Also: DOMDocument Subprograms Syntax DBMS_XMLDOM.SETSTANDALONE( doc IN DOMDOCUMENT, newvalue IN VARCHAR2); Parameters Table 204-129 SETSTANDALONE Procedure Parameters Parameter Description doc DOMDOCUMENT newvalue Value of the standalone property of the document