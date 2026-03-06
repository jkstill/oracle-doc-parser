---
id: 19c__HTP.APPLETOPEN
name: HTP.APPLETOPEN
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: HTP
tags: [htp]
source_file: HTP.html
---

# HTP.APPLETOPEN

This procedure generates the <APPLET> tag which begins the invocation of a Java applet.

## Syntax

```sql
HTP.APPLETOPEN (
   ccode          IN       VARCHAR2,
   cheight        IN       NUMBER,
   cwidth         IN       NUMBER,
   cattributes    IN       VARCHAR2   DEFAULT NULL);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| ccode | VARCHAR2 | IN | The the value for the CODE attribute which specifies the name of the applet class. |
| cheight | NUMBER | IN | The value for the HEIGHT attribute. |
| cwidth | NUMBER | IN | The value for the WIDTH attribute. |
| cattributes | VARCHAR2 | IN | The other attributes to be included as-is in the tag. |

## Usage Notes

You close the applet invocation with APPLETCLOSE Procedure which generates the </APPLET> tag. Syntax HTP.APPLETOPEN ( ccode IN VARCHAR2, cheight IN NUMBER, cwidth IN NUMBER, cattributes IN VARCHAR2 DEFAULT NULL); Parameters Table 221-5 APPLETOPEN Procedure Parameters Parameter Description ccode The the value for the CODE attribute which specifies the name of the applet class. cheight The value for the HEIGHT attribute. cwidth The value for the WIDTH attribute. cattributes The other attributes to be included as-is in the tag. Examples This procedure generates <APPLET CODE= ccode HEIGHT= cheight WIDTH= cwidth cattributes > so that, for example, HTP.appletopen('testclass.class', 100, 200, 'CODEBASE="/ows-applets"') generates <APPLET CODE="testclass.class" height=100 width=200 CODEBASE="/ows-applets"> Usage Notes Specify parameters to the Java applet using the PARAM Procedure . Use the cattributes parameter to specify the CODEBASE attribute since the PL/SQL cartridge does not know where to find the class files. The CODEBASE attribute specifies the virtual path containing the class files.