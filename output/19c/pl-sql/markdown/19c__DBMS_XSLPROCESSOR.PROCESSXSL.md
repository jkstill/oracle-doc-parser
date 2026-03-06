---
id: 19c__DBMS_XSLPROCESSOR.PROCESSXSL
name: DBMS_XSLPROCESSOR.PROCESSXSL
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XSLPROCESSOR
tags: [dbms_xslprocessor]
source_file: DBMS_XSLPROCESSOR.html
---

# DBMS_XSLPROCESSOR.PROCESSXSL

This function transforms input XMLDocument .

## Syntax

```sql
DBMS_XSLPROCESSOR.PROCESSXSL(
   p      IN   Processor,
   ss     IN   Stylesheet,
   xmldoc IN   DOMDOCUMENT), 
 RETURN DOMDOCUMENTFRAGMENT;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| p | Processor | IN | Processor instance |
| ss | Stylesheet | IN | Stylesheet instance |
| xmldoc | DOMDOCUMENT) | IN | XML document being transformed |
| url |  |  | URL for the information being transformed |
| clb |  |  | CLOB containing information to be transformed |
| dir |  |  | Directory where processing output file is saved |
| filename |  |  | Processing output file |
| cl |  |  | CLOB to which the processing output is saved |
| xmldf |  |  | XMLDocumentFragment being transformed |

**Returns:** `DOMDOCUMENTFRAGMENT`

## Usage Notes

Any changes to the default processor behavior should be effected before calling this procedure. An application error is raised if processing fails. Syntax Transforms input XMLDocument using given DOMDocument and stylesheet, and returns the resultant document fragment: DBMS_XSLPROCESSOR.PROCESSXSL( p IN Processor, ss IN Stylesheet, xmldoc IN DOMDOCUMENT), RETURN DOMDOCUMENTFRAGMENT; Transforms input XMLDocument using given document as URL and the Stylesheet , and returns the resultant document fragment: DBMS_XSLPROCESSOR.PROCESSXSL( p IN Processor, ss IN Stylesheet, url IN VARCHAR2, RETURN DOMDOCUMENTFRAGMENT; Transforms input XMLDocument using given document as CLOB and the Stylesheet , and returns the resultant document fragment: DBMS_XSLPROCESSOR.PROCESSXSL( p IN Processor, ss IN Stylesheet, clb IN CLOB) RETURN DOMDOCUMENTFRAGMENT; Transforms input XMLDocument using given DOMDOCUMENT and the stylesheet, and writes the output to the specified file: DBMS_XSLPROCESSOR.DBMS_XSLPROCESSOR.( p IN Processor, ss IN Stylesheet, xmldoc IN DOMDOCUMENT, dir IN VARCHAR2, fileName IN VARCHAR2); Transforms input XMLDocument using given URL and the stylesheet, and writes the output to the specified file in a specified directory: DBMS_XSLPROCESSOR.PROCESSXSL( p IN Processor, ss IN Stylesheet, url IN VARCHAR2, dir IN VARCHAR2, fileName IN VARCHAR2); Transforms input XMLDocument using given DOMDOCUMENT and the stylesheet, and writes the output to a CLOB : DBMS_XSLPROCESSOR.PROCESSXSL( p IN Processor, ss IN Stylesheet, xmldoc IN DOMDOCUMENT, cl IN OUT CLOB); Transforms input XMLDocument using given DOMDOCUMENTFRAGMENT and the stylesheet, and returns the resultant document fragment: DBMS_XSLPROCESSOR.PROCESSXSL( p IN Processor, ss IN Stylesheet, xmldf IN DOMDOCUMENTFRAGMENT) RETURN DOMDOCUMENTFRAGMENT; Transforms input XMLDocumentFragment using given DOMDocumentFragment and the stylesheet, and writes the output to the specified file in a specified directory: DBMS_XSLPROCESSOR.PROCESSXSL( p IN Processor, ss IN Stylesheet, xmldf IN DOMDOCUMENTFRAGMENT, dir IN VARCHAR2, filename IN VARCHAR2); Transforms input XMLDocumentFragment using given DOMDOCUMENTFRAGMENT and the stylesheet, and writes the output to a buffer: DBMS_XSLPROCESSOR.PROCESSXSL( p IN Processor, ss IN Stylesheet, xmldf IN DOMDOCUMENTFRAGMENT, buf IN OUT VARCHAR2); Transforms input XMLDocumentFragment using given DOMDOCUMENTFRAGMENT and the stylesheet, and writes the output to a CLOB : DBMS_XSLPROCESSOR.PROCESSXSL( p IN Processor, ss IN Stylesheet, xmldf IN DOMDOCUMENTFRAGMENT, cl IN OUT CLOB); Parameters Table 216-6 PROCESSXSL Function and Procedure Parameters Parameter Description p Processor instance ss Stylesheet instance xmldoc XML document being transformed url URL for the information being transformed clb CLOB containing information to be transformed dir Directory where processing output file is saved filename Processing output file cl CLOB to which the processing output is saved xmldf XMLDocumentFragment being transformed