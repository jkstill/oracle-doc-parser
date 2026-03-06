---
id: 19c__DBMS_XMLDOM.SETDATA
name: DBMS_XMLDOM.SETDATA
object_type: plsql_subprogram
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XMLDOM
tags: [dbms_xmldom]
source_file: DBMS_XMLDOM.html
---

# DBMS_XMLDOM.SETDATA

This overloaded procedure sets character data or DOMPROCESSINGINSTRUCTION content data. The specific functionality is described in the syntax declarations.

## Syntax

```sql
DBMS_XMLDOM.SETDATA(
   cd       IN     DOMCHARACTERDATA,
   data     IN     VARCHAR2);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| cd | DOMCHARACTERDATA | IN | DOMCHARACTERDATA |
| data | VARCHAR2) | IN | The data to which the node is set |
| pi |  |  | DOMPROCESSINGINSTRUCTION |
| data | VARCHAR2) | IN | New processing instruction content data |

## Usage Notes

Syntax Sets the character data of the node that implements this interface (See Also: DOMCharacterData Subprograms ): DBMS_XMLDOM.SETDATA( cd IN DOMCHARACTERDATA, data IN VARCHAR2); Sets the content data of the DOMPROCESSINGINSTRUCTION (See Also: DOMProcessingInstruction Subprograms ): DBMS_XMLDOM.SETDATA( pi IN DOMPROCESSINGINSTRUCTION, data IN VARCHAR2); Parameters Table 204-122 SETDATA Procedure Parameters Parameter Description cd DOMCHARACTERDATA data The data to which the node is set pi DOMPROCESSINGINSTRUCTION data New processing instruction content data