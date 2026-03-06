---
id: 19c__DBMS_XDBRESOURCE.SETCUSTOMMETADATA
name: DBMS_XDBRESOURCE.SETCUSTOMMETADATA
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XDBRESOURCE
tags: [dbms_xdbresource]
source_file: DBMS_XDBRESOURCE.html
---

# DBMS_XDBRESOURCE.SETCUSTOMMETADATA

This procedure sets the custom metadata specified by the xpath and namespace to new data.

## Syntax

```sql
DBMS_XDBRESOURCE.SETCUSTOMMETADATA (
   res          IN OUT  XDBResource, 
   xpath        IN      VARCHAR2,
   namespace    IN      VARCHAR2, 
   newMetadata  IN      XMLType);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| res | XDBResource | IN OUT | XDBResource |
| xpath | VARCHAR2 | IN | XPath to change |
| namespace | VARCHAR2 | IN | Namespace to use |
| newMetadata | XMLType) | IN | New data that should replace the metadata at the given XPath |

## Usage Notes

Syntax DBMS_XDBRESOURCE.SETCUSTOMMETADATA ( res IN OUT XDBResource, xpath IN VARCHAR2, namespace IN VARCHAR2, newMetadata IN XMLType); Parameters Table 200-51 SETCUSTOMMETADATA Procedure Parameters Parameter Description res XDBResource xpath XPath to change namespace Namespace to use newMetadata New data that should replace the metadata at the given XPath Usage Notes The first component of the XPath expression must be "Resource".