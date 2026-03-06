---
id: 19c__DBMS_XMLDOM.ISNULL
name: DBMS_XMLDOM.ISNULL
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XMLDOM
tags: [dbms_xmldom]
source_file: DBMS_XMLDOM.html
---

# DBMS_XMLDOM.ISNULL

This function is overloaded. The specific forms of functionality are described along with the syntax declarations.

## Syntax

```sql
DBMS_XMLDOM.ISNULL(
  n        IN     DOMNODE) 
 RETURN BOOLEAN;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| n | DOMNODE) | IN | DOMNODE to check |
| a |  |  | DOMATTR to check |
| cds |  |  | DOMCDATASECTION to check |
| cd |  |  | DOMCHARACTERDATA to check |
| com |  |  | DOMCOMMENT to check |
| doc |  |  | DOMDOCUMENT to check |
| dF |  |  | DOMDOCUMENTFRAGMENT to check |
| dt |  |  | DOMDOCUMENTTYPE to check |
| elem |  |  | DOMELEMENT to check |
| ent |  |  | DOMENTITY to check |
| eref |  |  | DOMENTITYREFERENCE to check |
| di |  |  | DOMIMPLEMENTATION to check |
| nnm |  |  | DOMNAMENODEMAP to check |
| nl |  |  | DOMNODELIST to check |
| n | DOMNODE) | IN | DOMNOTATION to check |
| pi |  |  | DOMPROCESSINGINSTRUCTION to check |
| t |  |  | DOMTEXT to check |

**Returns:** `BOOLEAN`

## Usage Notes

Syntax Checks if the specified DOMNODE is NULL . Returns TRUE if it is NULL , FALSE otherwise (See Also: DOMNode Subprograms ): DBMS_XMLDOM.ISNULL( n IN DOMNODE) RETURN BOOLEAN; Checks that the specified DOMATTR is NULL ; returns TRUE if it is NULL , FALSE otherwise (See Also: DOMAttr Subprograms ): DBMS_XMLDOM.ISNULL( a IN DOMATTR) RETURN BOOLEAN; Checks that the specified DOMCDATASECTION is NULL ; returns TRUE if it is NULL , FALSE otherwise (See Also: DOMCDataSection Subprograms ): DBMS_XMLDOM.ISNULL( cds IN DOMCDATASECTION) RETURN BOOLEAN; Checks that the specified DOMCHARACTERDATA is NULL ; returns TRUE if it is NULL , FALSE otherwise (See Also: DOMCharacterData Subprograms ): DBMS_XMLDOM.ISNULL( cd IN DOMCHARACTERDATA) RETURN BOOLEAN; Checks that the specified DOMCOMMENT is NULL ; returns TRUE if it is NULL , FALSE otherwise (See Also: DOMComment Subprograms ): DBMS_XMLDOM.ISNULL( com IN DOMCOMMENT) RETURN BOOLEAN; Checks that the specified DOMDOCUMENT is NULL ; returns TRUE if it is NULL , FALSE otherwise (See Also: DOMDocument Subprograms ): DBMS_XMLDOM.ISNULL( doc IN DOMDOCUMENT) RETURN BOOLEAN; Checks that the specified DOMDOCUMENTFRAGMENT is NULL ; returns TRUE if it is NULL , FALSE otherwise (See Also: DOMDocumentFragment Subprograms ): DBMS_XMLDOM.ISNULL( df IN DOMDOCUMENTFRAGMENT) RETURN BOOLEAN; Checks that the specified DOMDOCUMENTTYPE is NULL ; returns TRUE if it is NULL , FALSE otherwise (See Also: DOMDocumentType Subprograms ): DBMS_XMLDOM.ISNULL( dt IN DOMDOCUMENTTYPE) RETURN BOOLEAN; Checks that the specified DOMELEMENT is NULL ; returns TRUE if it is NULL , FALSE otherwise (See Also: DOMElement Subprograms ): DBMS_XMLDOM.ISNULL( elem IN DOMELEMENT) RETURN BOOLEAN; Checks that the specified DOMENTITY is NULL ; returns TRUE if it is NULL , FALSE otherwise (See Also: DOMEntity Subprograms ): DBMS_XMLDOM.ISNULL( ent IN DOMENTITY) RETURN BOOLEAN; Checks that the specified DOMENTITYREFERENCE is NULL ; returns TRUE if it is NULL , FALSE otherwise (See Also: DOMEntityReference Subprograms ): DBMS_XMLDOM.ISNULL( EREF IN DOMENTITYREFERENCE) RETURN BOOLEAN; Checks that the specified DOMIMPLEMENTATION is NULL ; returns TRUE if it is NULL (See Also: DOMImplementation Subprograms ): DBMS_XMLDOM.ISNULL( di IN DOMIMPLEMENTATION) RETURN BOOLEAN; Checks that the specified DOMNAMEDNODEMAP is NULL ; returns TRUE if it is NULL , FALSE otherwise (See Also: DOMNamedNodeMap Subprograms ): DBMS_XMLDOM.ISNULL( nnm IN DOMNAMEDNODEMAP) RETURN BOOLEAN; Checks that the specified DOMNODELIST is NULL ; returns TRUE if it is NULL , FALSE otherwise (See Also: DOMNodeList Subprograms ): DBMS_XMLDOM.ISNULL( nl IN DOMNODELIST) RETURN BOOLEAN; Checks that the specified DOMNOTATION is NULL ; returns TRUE if it is NULL , FALSE otherwise (See Also: DOMNotation Subprograms ): DBMS_XMLDOM.ISNULL( n IN DOMNOTATION) RETURN BOOLEAN; Checks that the specified DOMPROCESSINGINSTRUCTION is NULL ; returns TRUE if it is NULL, FALSE otherwise (See Also: DOMProcessingInstruction Subprograms ): DBMS_XMLDOM.ISNULL( pi IN DOMPROCESSINGINSTRUCTION) RETURN BOOLEAN; Checks that the specified DOMTEXT is NULL ; returns TRUE if it is NULL , FALSE otherwise (See Also: DOMText Subprograms ): DBMS_XMLDOM.ISNULL( t IN DOMTEXT) RETURN BOOLEAN; Parameters Table 204-94 ISNULL Function Parameters Parameter Description n DOMNODE to check a DOMATTR to check cds DOMCDATASECTION to check cd DOMCHARACTERDATA to check com DOMCOMMENT to check doc DOMDOCUMENT to check dF DOMDOCUMENTFRAGMENT to check dt DOMDOCUMENTTYPE to check elem DOMELEMENT to check ent DOMENTITY to check eref DOMENTITYREFERENCE to check di DOMIMPLEMENTATION to check nnm DOMNAMENODEMAP to check nl DOMNODELIST to check n DOMNOTATION to check pi DOMPROCESSINGINSTRUCTION to check t DOMTEXT to check