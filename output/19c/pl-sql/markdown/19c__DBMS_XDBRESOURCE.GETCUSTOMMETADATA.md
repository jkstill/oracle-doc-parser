---
id: 19c__DBMS_XDBRESOURCE.GETCUSTOMMETADATA
name: DBMS_XDBRESOURCE.GETCUSTOMMETADATA
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XDBRESOURCE
tags: [dbms_xdbresource]
source_file: DBMS_XDBRESOURCE.html
---

# DBMS_XDBRESOURCE.GETCUSTOMMETADATA

This function returns the requested custom metadata given the xpath and namespace to the metadata.

## Syntax

```sql
DBMS_XDBRESOURCE.GETCUSTOMMETADATA (
   res        IN    XDBResource, 
   xpath      IN    VARCHAR2,    namespace  IN    VARCHAR2)
 RETURN XMLType;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| res | XDBResource | IN | XDBResource |
| xpath | VARCHAR2 | IN | XPath for custom metadata |
| namespace | VARCHAR2) | IN | Namespace |

**Returns:** `XMLType`

## Usage Notes

Syntax DBMS_XDBRESOURCE.GETCUSTOMMETADATA ( res IN XDBResource, xpath IN VARCHAR2, namespace IN VARCHAR2) RETURN XMLType; Parameters Table 200-16 GETCUSTOMMETADATA Function Parameters Parameter Description res XDBResource xpath XPath for custom metadata namespace Namespace Usage Notes The first component of the XPath expression must be "Resource".