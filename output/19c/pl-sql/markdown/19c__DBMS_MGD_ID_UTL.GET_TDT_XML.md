---
id: 19c__DBMS_MGD_ID_UTL.GET_TDT_XML
name: DBMS_MGD_ID_UTL.GET_TDT_XML
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_MGD_ID_UTL
tags: [dbms_mgd_id_utl]
source_file: DBMS_MGD_ID_UTL.html
---

# DBMS_MGD_ID_UTL.GET_TDT_XML

This function returns the Oracle Database tag data translation XML for the specified scheme.

## Syntax

```sql
DBMS_MGD_ID_UTL.GET_TDT_XML (
   category_id  IN VARCHAR2,
   scheme_name  IN VARCHAR2)
 RETURN CLOB;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| category_id | VARCHAR2 | IN | Category ID |
| scheme_name | VARCHAR2) | IN | Name of scheme |

**Returns:** `CLOB`

## Usage Notes

Syntax DBMS_MGD_ID_UTL.GET_TDT_XML ( category_id IN VARCHAR2, scheme_name IN VARCHAR2) RETURN CLOB; Parameters Table 109-12 GET_TDT_XML Function Parameters Parameter Description category_id Category ID scheme_name Name of scheme Usage Notes The return value contains the Oracle Database tag data translation XML for the specified scheme. Examples The following example gets the Oracle Database TDT XML for the specified scheme: --Contents of get_tdtxml.sql DECLARE gettdtxml CLOB; BEGIN gettdtxml := DBMS_MGD_ID_UTL.get_tdt_xml(1,'SGTIN-64'); dbms_output.put_line('Length of tdt XML is '||DBMS_LOB.GETLENGTH(gettdtxml)); dbms_output.put_line(DBMS_LOB.SUBSTR(gettdtxml, DBMS_LOB.GETLENGTH(gettdtxml), 1)); END; / SHOW ERRORS; SQL> @get_tdtxml.sql . . . Length of tdt XML is 22884 <?xml version = '1.0' encoding = "UTF-8"?> <TagDataTranslation version="0.04" date="2005-04-18T16:05:00Z" xmlns:xsi="http://www.w3.org/2001/XMLSchema" xmlns="oracle.mgd.idcode"><scheme name="SGTIN-64" optionKey="companyprefixlength" xmlns=""> <level type="BINARY" prefixMatch="10" requiredFormattingParameters="filter"> <option optionKey="12" pattern="10([01]{3})([01]{14})([01]{20})([01]{25})" grammar="'10' filter companyprefixindex itemref serial"> <field seq="1" decimalMinimum="0" decimalMaximum="7" characterSet="[01]*" bitLength="3" length="1" padChar="0" padDir="LEFT" name="filter"/> <field seq="2" decimalMinimum="0" decimalMaximum="16383" characterSet="[01]*" bitLength="14" name="companyprefixindex"/> <field seq="3" decimalMinimum="0" decimalMaximum="9" characterSet="[01]*" bitLength="20" length="1" padChar="0" padDir="LEFT" name="itemref"/> <field seq="4" decimalMinimum="0" decimalMaximum="33554431" characterSet="[01]*" bitLength="25" name="serial"/> . . . <field seq="1" decimalMinimum="0" decimalMaximum="9999999" characterSet="[0-9]*" length="7" padChar="0" padDir="LEFT" name="itemref"/> <field seq="2" decimalMinimum="0" decimalMaximum="999999" characterSet="[0-9]*" length="6" padChar="0" padDir="LEFT" name="companyprefix"/> </option> </level> </scheme></TagDataTranslation> PL/SQL procedure successfully completed. . . .