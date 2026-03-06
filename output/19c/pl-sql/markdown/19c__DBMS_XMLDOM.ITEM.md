---
id: 19c__DBMS_XMLDOM.ITEM
name: DBMS_XMLDOM.ITEM
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XMLDOM
tags: [dbms_xmldom]
source_file: DBMS_XMLDOM.html
---

# DBMS_XMLDOM.ITEM

This function is overloaded. The specific forms of functionality are described along with the syntax declarations.

## Syntax

```sql
DBMS_XMLDOM.ITEM(
   nnm       IN     DOMNAMEDNODEMAP,
   index     IN     NUMBER)
 RETURN DOMNODE;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| nnm | DOMNAMEDNODEMAP | IN | DOMNAMEDNODEMAP |
| index | NUMBER) | IN | The index in the node map at which the item is to be retrieved |
| nl |  |  | DOMNODELIST |
| index | NUMBER) | IN | The index in the NodeList used to retrieve the item |

**Returns:** `DOMNODE`

## Usage Notes

Syntax Returns the item in the map which corresponds to the INDEX parameter. If INDEX is greater than or equal to the number of nodes in this map, this returns NULL (See Also: DOMNamedNodeMap Subprograms ): DBMS_XMLDOM.ITEM( nnm IN DOMNAMEDNODEMAP, index IN NUMBER) RETURN DOMNODE; Returns the item in the collection which corresponds to the INDEX parameter. If index is greater than or equal to the number of nodes in the list, this returns NULL (See Also: DOMNodeList Subprograms ): DBMS_XMLDOM.ITEM( nl IN DOMNODELIST, index IN NUMBER) RETURN DOMNODE; Parameters Table 204-95 ITEM Function Parameters Parameter Description nnm DOMNAMEDNODEMAP index The index in the node map at which the item is to be retrieved nl DOMNODELIST index The index in the NodeList used to retrieve the item