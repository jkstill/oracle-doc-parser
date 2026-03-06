---
id: 19c__DBMS_XMLSCHEMA_ANNOTATE.ADDXDBNAMESPACE
name: DBMS_XMLSCHEMA_ANNOTATE.ADDXDBNAMESPACE
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XMLSCHEMA_ANNOTATE
tags: [dbms_xmlschema_annotate]
source_file: DBMS_XMLSCHEMA_ANNOTATE.html
---

# DBMS_XMLSCHEMA_ANNOTATE.ADDXDBNAMESPACE

This procedure adds the XDB namespace required for XDB annotation.

## Syntax

```sql
DBMS_XMLSCHEMA_ANNOTATE.ADDXDBNAMESPACE (
   xmlschema      IN OUT XMLTYPE);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| xmschema |  |  | Gets an XML Schema as XMLTYPE , performs the annotation and returns it |

## Usage Notes

Syntax DBMS_XMLSCHEMA_ANNOTATE.ADDXDBNAMESPACE ( xmlschema IN OUT XMLTYPE); Parameters Table 211-2 ADDXDBNAMESPACE Procedure Parameters Parameter Description xmschema Gets an XML Schema as XMLTYPE , performs the annotation and returns it Usage Notes This procedure is called implicitly by any other procedure that adds a schema annotation. Since there is no reason to add an XDB namespace without other annotations, this procedure is most likely called by other annotations procedures and not by the user directly.