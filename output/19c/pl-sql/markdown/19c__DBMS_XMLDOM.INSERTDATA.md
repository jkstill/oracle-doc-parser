---
id: 19c__DBMS_XMLDOM.INSERTDATA
name: DBMS_XMLDOM.INSERTDATA
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XMLDOM
tags: [dbms_xmldom]
source_file: DBMS_XMLDOM.html
---

# DBMS_XMLDOM.INSERTDATA

This procedure inserts a string at the specified character offset.

## Syntax

```sql
DBMS_XMLDOM.INSERTDATA(
   cd       IN     DOMCHARACTERDATA,
   offset   IN     NUMBER,
   arg      IN     VARCHAR2);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| cd | DOMCHARACTERDATA | IN | DOMCHARACTERDATA |
| offset | NUMBER | IN | The offset at which to insert the data |
| arg | VARCHAR2) | IN | The value to be inserted |

## Usage Notes

See Also: DOMCharacterData Subprograms See Also: DOMCharacterData Subprograms Syntax DBMS_XMLDOM.INSERTDATA( cd IN DOMCHARACTERDATA, offset IN NUMBER, arg IN VARCHAR2); Parameters Table 204-93 INSERTDATA Procedure Parameters Parameter Description cd DOMCHARACTERDATA offset The offset at which to insert the data arg The value to be inserted