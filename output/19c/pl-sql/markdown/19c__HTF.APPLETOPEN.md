---
id: 19c__HTF.APPLETOPEN
name: HTF.APPLETOPEN
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: HTF
tags: [htf]
source_file: HTF.html
---

# HTF.APPLETOPEN

This function generates the <APPLET> tag which begins the invocation of a Java applet.

## Syntax

```sql
HTF.APPLETOPEN (
   ccode          IN       VARCHAR2,
   cheight        IN       NUMBER,
   cwidth         IN       NUMBER,
   cattributes    IN       VARCHAR2   DEFAULT NULL)
  RETURN VARCHAR2;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| ccode | VARCHAR2 | IN | The value for the CODE attribute which specifies the name of the applet class. |
| cheight | NUMBER | IN | The value for the HEIGHT attribute. |
| cwidth | NUMBER | IN | The value for the WIDTH attribute. |
| cattributes | VARCHAR2 | IN | The other attributes to be included as-is in the tag. |

**Returns:** `VARCHAR2`

## Usage Notes

You close the applet invocation with APPLETCLOSE Function which generates the </APPLET> tag. Syntax HTF.APPLETOPEN ( ccode IN VARCHAR2, cheight IN NUMBER, cwidth IN NUMBER, cattributes IN VARCHAR2 DEFAULT NULL) RETURN VARCHAR2; Parameters Table 220-5 APPLETOPEN Function Parameters Parameter Description ccode The value for the CODE attribute which specifies the name of the applet class. cheight The value for the HEIGHT attribute. cwidth The value for the WIDTH attribute. cattributes The other attributes to be included as-is in the tag. Examples This function generates <APPLET CODE=ccode HEIGHT=cheight WIDTH=cwidth cattributes> so that, for example, HTF.appletopen('testclass.class', 100, 200, 'CODEBASE="/ows-applets"') generates <APPLET CODE="testclass.class" height=100 width=200 CODEBASE="/ows-applets"> Usage Notes Specify parameters to the Java applet using the PARAM Function function. Use the cattributes parameter to specify the CODEBASE attribute since the PL/SQL cartridge does not know where to find the class files. The CODEBASE attribute specifies the virtual path containing the class files.