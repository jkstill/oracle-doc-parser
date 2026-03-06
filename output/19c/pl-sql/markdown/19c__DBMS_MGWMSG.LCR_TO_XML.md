---
id: 19c__DBMS_MGWMSG.LCR_TO_XML
name: DBMS_MGWMSG.LCR_TO_XML
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_MGWMSG
tags: [dbms_mgwmsg]
source_file: DBMS_MGWMSG.html
---

# DBMS_MGWMSG.LCR_TO_XML

This function converts a SYS . ANYDATA object encapsulating a row LCR (Logical Change Record, in this case a LCR$_ROW_RECORD ) or a DDL LCR ( LCR$_DDL_RECORD ) to a SYS . XMLTYPE object.

## Syntax

```sql
DBMS_MGWMSG.LCR_TO_XML (
   p_anydata IN SYS.ANYDATA )
 RETURN SYS.XMLTYPE;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| p_anydata | SYS.ANYDATA | IN | An ANYDATA object to be converted |

**Returns:** `SYS.XMLTYPE`

## Usage Notes

See Also: XML_TO_LCR Function See Also: XML_TO_LCR Function Syntax DBMS_MGWMSG.LCR_TO_XML ( p_anydata IN SYS.ANYDATA ) RETURN SYS.XMLTYPE; Parameters Table 111-22 LCR_TO_XML Function Parameters Parameter Description p_anydata An ANYDATA object to be converted Return Values Returns a SYS . XMLTYPE object.