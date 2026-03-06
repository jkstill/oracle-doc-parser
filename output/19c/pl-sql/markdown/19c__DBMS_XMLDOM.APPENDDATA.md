---
id: 19c__DBMS_XMLDOM.APPENDDATA
name: DBMS_XMLDOM.APPENDDATA
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XMLDOM
tags: [dbms_xmldom]
source_file: DBMS_XMLDOM.html
---

# DBMS_XMLDOM.APPENDDATA

This procedure appends the string to the end of the character data of the node. Upon success, data provides access to the concatenation of data and the specified string argument.

## Syntax

```sql
DBMS_XMLDOM.APPENDDATA(
   cd      IN    DOMCHARACTERDATA, 
   arg     IN    VARCHAR2);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| cd | DOMCHARACTERDATA | IN | DOMCHARACTERDATA |
| arg | VARCHAR2) | IN | The data to append to the existing data |

## Usage Notes

See Also: DOMCharacterData Subprograms See Also: DOMCharacterData Subprograms Syntax DBMS_XMLDOM.APPENDDATA( cd IN DOMCHARACTERDATA, arg IN VARCHAR2); Parameters Table 204-24 APPENDDATA Procedure Parameters Parameter Description cd DOMCHARACTERDATA arg The data to append to the existing data