---
id: 19c__DBMS_XMLDOM.GETDATA
name: DBMS_XMLDOM.GETDATA
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XMLDOM
tags: [dbms_xmldom]
source_file: DBMS_XMLDOM.html
---

# DBMS_XMLDOM.GETDATA

This function is overloaded. The specific forms of functionality are described along with the syntax declarations.

## Syntax

```sql
DBMS_XMLDOM.GETDATA(
   cd      IN    DOMCHARACTERDATA)
 RETURN VARCHAR2;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| cd | DOMCHARACTERDATA) | IN | DOMCHARACTERDATA |
| pi |  |  | The DOMPROCESSINGINSTRUCTION |

**Returns:** `VARCHAR2`

## Usage Notes

Syntax Gets the character data of the node that implements this interface (See Also: DOMCharacterData Subprograms ): DBMS_XMLDOM.GETDATA( cd IN DOMCHARACTERDATA) RETURN VARCHAR2; Returns the content data of the DOMProcessingInstruction (See Also: DOMProcessingInstruction Subprograms ): DBMS_XMLDOM.GETDATA( pi IN DOMPROCESSINGINSTRUCTION) RETURN VARCHAR2; Parameters Table 204-49 GETDATA Function Parameters Parameter Description cd DOMCHARACTERDATA pi The DOMPROCESSINGINSTRUCTION