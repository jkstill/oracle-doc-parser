---
id: 19c__DBMS_XMLDOM.DELETEDATA
name: DBMS_XMLDOM.DELETEDATA
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XMLDOM
tags: [dbms_xmldom]
source_file: DBMS_XMLDOM.html
---

# DBMS_XMLDOM.DELETEDATA

This procedure removes a range of characters from the node. Upon success, data and length reflect the change.

## Syntax

```sql
DBMS_XMLDOM.DELETEDATA(
   cd        IN     DOMCHARACTERDATA,
   offset    IN     NUMBER,
   cnt       IN     NUMBER);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| cd | DOMCHARACTERDATA | IN | DOMCHARACTERDATA |
| offset | NUMBER | IN | The offset from which to delete the data |
| cnt | NUMBER) | IN | The number of characters (starting from offset) to delete |

## Usage Notes

See Also: DOMCharacterData Subprograms See Also: DOMCharacterData Subprograms Syntax DBMS_XMLDOM.DELETEDATA( cd IN DOMCHARACTERDATA, offset IN NUMBER, cnt IN NUMBER); Parameters Table 204-35 DELETEDATA PROCEDURE Parameters Parameter Description cd DOMCHARACTERDATA offset The offset from which to delete the data cnt The number of characters (starting from offset) to delete