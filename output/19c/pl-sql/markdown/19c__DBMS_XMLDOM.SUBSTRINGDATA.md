---
id: 19c__DBMS_XMLDOM.SUBSTRINGDATA
name: DBMS_XMLDOM.SUBSTRINGDATA
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XMLDOM
tags: [dbms_xmldom]
source_file: DBMS_XMLDOM.html
---

# DBMS_XMLDOM.SUBSTRINGDATA

This function extracts a range of data from the node.

## Syntax

```sql
DBMS_XMLDOM.SUBSTRINGDATA(
   cd        IN     DOMCHARACTERDATA,
   offset    IN     NUMBER,
   cnt       IN     NUMBER)
 RETURN VARCHAR2;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| cd | DOMCHARACTERDATA | IN | DOMCHARACTERDATA |
| offset | NUMBER | IN | The starting offset of the data from which to get the data |
| cnt | NUMBER) | IN | The number of characters (from the offset) of the data to get |

**Returns:** `VARCHAR2`

## Usage Notes

See Also: DOMCharacterData Subprograms See Also: DOMCharacterData Subprograms Syntax DBMS_XMLDOM.SUBSTRINGDATA( cd IN DOMCHARACTERDATA, offset IN NUMBER, cnt IN NUMBER) RETURN VARCHAR2; Parameters Table 204-133 SUBSTRINGDATA Function Parameters Parameter Description cd DOMCHARACTERDATA offset The starting offset of the data from which to get the data cnt The number of characters (from the offset) of the data to get