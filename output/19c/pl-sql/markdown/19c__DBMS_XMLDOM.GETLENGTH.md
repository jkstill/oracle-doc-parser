---
id: 19c__DBMS_XMLDOM.GETLENGTH
name: DBMS_XMLDOM.GETLENGTH
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XMLDOM
tags: [dbms_xmldom]
source_file: DBMS_XMLDOM.html
---

# DBMS_XMLDOM.GETLENGTH

This function is overloaded. The specific forms of functionality are described along with the syntax declarations.

## Syntax

```sql
DBMS_XMLDOM.GETLENGTH(
   cd     IN     DOMCHARACTERDATA)
 RETURN NUMBER;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| cd | DOMCHARACTERDATA) | IN | DOMCHARACTERDATA |
| nnm |  |  | DOMNAMEDNODEMAP |
| nl |  |  | DOMNODELIST |

**Returns:** `NUMBER`

## Usage Notes

Syntax Gets the number of characters in the data. This may have the value zero, because CharacterData nodes may be empty (See Also: DOMCharacterData Subprograms ): DBMS_XMLDOM.GETLENGTH( cd IN DOMCHARACTERDATA) RETURN NUMBER; Gets the number of nodes in this map. The range of valid child node indexes is 0 to length-1 , inclusive (See Also: DOMNamedNodeMap Subprograms ): DBMS_XMLDOM.GETLENGTH( nnm IN DOMNAMEDNODEMAP) RETURN NUMBER; Gets the number of nodes in the list. The range of valid child node indexes is 0 to length-1 , inclusive (See Also: DOMNodeList Subprograms ): DBMS_XMLDOM.GETLENGTH( nl IN DOMNODELIST) RETURN NUMBER; Parameters Table 204-58 GETLENGTH Function Parameters Parameter Description cd DOMCHARACTERDATA nnm DOMNAMEDNODEMAP nl DOMNODELIST