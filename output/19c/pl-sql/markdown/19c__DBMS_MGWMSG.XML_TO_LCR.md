---
id: 19c__DBMS_MGWMSG.XML_TO_LCR
name: DBMS_MGWMSG.XML_TO_LCR
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_MGWMSG
tags: [dbms_mgwmsg]
source_file: DBMS_MGWMSG.html
---

# DBMS_MGWMSG.XML_TO_LCR

This function converts a SYS . XMLTYPE object to a SYS . ANYDATA object encapsulating a row LCR ( LCR$_ROW_RECORD ) or a DDL LCR ( LCR$_DDL_RECORD ).

## Syntax

```sql
DBMS_MGWMSG.XML_TO_LCR (
   p_xmldata IN SYS.XMLTYPE )
 RETURN SYS.ANYDATA;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| p_xmldata | SYS.XMLTYPE | IN | An XMLTYPE object representing an LCR |

**Returns:** `SYS.ANYDATA`

## Usage Notes

See Also: LCR_TO_XML Function See Also: LCR_TO_XML Function Syntax DBMS_MGWMSG.XML_TO_LCR ( p_xmldata IN SYS.XMLTYPE ) RETURN SYS.ANYDATA; Parameters Table 111-37 XML_TO_LCR Function Parameters Parameter Description p_xmldata An XMLTYPE object representing an LCR Return Values Returns a SYS . ANYDATA object.