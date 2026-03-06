---
id: 19c__DBMS_XMLDOM.REPLACEDATA
name: DBMS_XMLDOM.REPLACEDATA
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XMLDOM
tags: [dbms_xmldom]
source_file: DBMS_XMLDOM.html
---

# DBMS_XMLDOM.REPLACEDATA

This procedure changes a range of characters in the node. Upon success, data and length reflect the change.

## Syntax

```sql
DBMS_XMLDOM.REPLACEDATA(
   cd        IN     DOMCHARACTERDATA,
   offset    IN     NUMBER,
   cnt       IN     NUMBER,
   arg       IN     VARCHAR2);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| cd | DOMCHARACTERDATA | IN | DOMCHARACTERDATA |
| offset | NUMBER | IN | The offset at which to replace |
| cnt | NUMBER | IN | The number of characters to replace |
| arg | VARCHAR2) | IN | The value to replace with |

## Usage Notes

See Also: DOMCharacterData Subprograms See Also: DOMCharacterData Subprograms Syntax DBMS_XMLDOM.REPLACEDATA( cd IN DOMCHARACTERDATA, offset IN NUMBER, cnt IN NUMBER, arg IN VARCHAR2); Parameters Table 204-117 REPLACEDATA Procedure Parameters Parameter Description cd DOMCHARACTERDATA offset The offset at which to replace cnt The number of characters to replace arg The value to replace with