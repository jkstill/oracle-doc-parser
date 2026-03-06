---
id: 19c__DBMS_XMLDOM.MAKENODE
name: DBMS_XMLDOM.MAKENODE
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XMLDOM
tags: [dbms_xmldom]
source_file: DBMS_XMLDOM.html
---

# DBMS_XMLDOM.MAKENODE

This function is overloaded. The specific forms of functionality are described along with the syntax declarations.

## Syntax

```sql
DBMS_XMLDOM.MAKENODE(
   a        IN     DOMATTR)
 RETURN DOMNODE;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| a | DOMATTR) | IN | DOMATTR to cast |
| cds |  |  | DOMCDATASECTION to cast |
| cd |  |  | DOMCHARACTERDATA to cast |
| com |  |  | DOMCOMMENT to cast |
| doc |  |  | DOMDOCUMENT to cast |
| df |  |  | DOMDOCUMENTFRAGMENT to cast |
| dt |  |  | DOMDOCUMENTTYPE to cast |
| elem |  |  | DOMELEMENT to cast |
| ent |  |  | DOMENTITY to cast |
| eref |  |  | DOMENTITYREFERENCE to cast |
| n |  |  | DOMNOTATION to cast |
| pi |  |  | DOMPROCESSINGINSTRUCTION to cast |
| t |  |  | DOMTEXT to cast |

**Returns:** `DOMNODE`

## Usage Notes

Syntax Casts specified DOMATTR to a DOMNODE , and returns the DOMNODE (See Also: DOMAttr Subprograms ): DBMS_XMLDOM.MAKENODE( a IN DOMATTR) RETURN DOMNODE; Casts the DOMCDATASECTION to a DOMNODE , and returns that DOMNODE (See Also: DOMCDataSection Subprograms ): DBMS_XMLDOM.MAKENODE( cds IN DOMCDATASECTION) RETURN DOMNODE; Casts the specified DOMCHARACTERDATA as a DOMNODE , and returns that DOMNODE (See Also: DOMCharacterData Subprograms ): DBMS_XMLDOM.MAKENODE( cd IN DOMCHARACTERDATA) RETURN DOMNODE; Casts the specified DOMCOMMENT to a DOMNODE , and returns that DOMNODE (See Also: DOMComment Subprograms ): DBMS_XMLDOM.MAKENODE( com IN DOMCOMMENT) RETURN DOMNODE; Casts the DOMDOCUMENT to a DOMNODE , and returns that DOMNODE (See Also: DOMDocument Subprograms ): DBMS_XMLDOM.MAKENODE( doc IN DOMDOCUMENT) RETURN DOMNODE; Casts the specified DOMDOCUMENTFRAGMENT to a DOMNODE , and returns that DOMNODE (See Also: DOMDocumentFragment Subprograms ): DBMS_XMLDOM.MAKENODE( df IN DOMDOCUMENTFRAGMENT) RETURN DOMNode; Casts the specified DOMDOCUMENTTYPE to a DOMNODE , and returns that DOMNODE (See Also: DOMDocumentType Subprograms ): DBMS_XMLDOM.MAKENODE( dt IN DOMDOCUMENTTYPE) RETURN DOMNODE; Casts the specified DOMELEMENT to a DOMNODE , and returns that DOMNODE (See Also: DOMElement Subprograms ): DBMS_XMLDOM.MAKENODE( elem IN DOMELEMENT) RETURN DOMNODE; Casts specified DOMENTITY to a DOMNODE , and returns that DOMNODE (See Also: DOMEntity Subprograms ): DBMS_XMLDOM.MAKENODE( ent IN DOMENTITY) RETURN DOMNODE; Casts the DOMENTITYREFERENCE to a DOMNODE , and returns that DOMNODE (See Also: DOMEntityReference Subprograms ): DBMS_XMLDOM.MAKENODE( eref IN DOMENTITYREFERENCE) RETURN DOMNODE; Casts the DOMNOTATION to a DOMNODE , and returns that DOMNODE (See Also: DOMNotation Subprograms ): DBMS_XMLDOM.MAKENODE( n IN DOMNOTATION) RETURN DOMNODE; Casts the DOMPROCESSINGINSTRUCTION to a DOMNODE , and returns the DOMNODE (See Also: DOMProcessingInstruction Subprograms ): DBMS_XMLDOM.MAKENODE( pi IN DOMPROCESSINGINSTRUCTION) RETURN DOMNODE; Casts the DOMTEXT to a DOMNODE , and returns that DOMNODE (See Also: DOMText Subprograms ): DBMS_XMLDOM.MAKENODE( t IN DOMTEXT) RETURN DOMNODE; Parameters Table 204-106 MAKENODE Function Parameters Parameter Description a DOMATTR to cast cds DOMCDATASECTION to cast cd DOMCHARACTERDATA to cast com DOMCOMMENT to cast doc DOMDOCUMENT to cast df DOMDOCUMENTFRAGMENT to cast dt DOMDOCUMENTTYPE to cast elem DOMELEMENT to cast ent DOMENTITY to cast eref DOMENTITYREFERENCE to cast n DOMNOTATION to cast pi DOMPROCESSINGINSTRUCTION to cast t DOMTEXT to cast