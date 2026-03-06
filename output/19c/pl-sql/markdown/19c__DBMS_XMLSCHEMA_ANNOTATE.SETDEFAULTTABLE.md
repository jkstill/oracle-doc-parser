---
id: 19c__DBMS_XMLSCHEMA_ANNOTATE.SETDEFAULTTABLE
name: DBMS_XMLSCHEMA_ANNOTATE.SETDEFAULTTABLE
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XMLSCHEMA_ANNOTATE
tags: [dbms_xmlschema_annotate]
source_file: DBMS_XMLSCHEMA_ANNOTATE.html
---

# DBMS_XMLSCHEMA_ANNOTATE.SETDEFAULTTABLE

This procedure sets the name of the table for the specified global element. This is equivalent to using the schema annotation xdb:defaultTable="<default_table_name>" for the top-level element.

## Syntax

```sql
DBMS_XMLSCHEMA_ANNOTATE.SETDEFAULTTABLE (
   xmlschema           IN  OUT  XMLTYPE,
   globalElementName   IN       VARCHAR2, 
   tableName           IN       VARCHAR2, 
   overwrite           IN       BOOLEAN   DEFAULT TRUE);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| xmlschema | XMLTYPE | IN  OUT | XML schema to be annotated |
| globalElementName | VARCHAR2 | IN | Name of the global element in the schema |
| tableName | VARCHAR2 | IN | Name being assigned to the table |
| overwrite | BOOLEAN | IN | Boolean that indicates whether or not the procedure overwrites element attributes. The default is TRUE . |

## Usage Notes

Syntax DBMS_XMLSCHEMA_ANNOTATE.SETDEFAULTTABLE ( xmlschema IN OUT XMLTYPE, globalElementName IN VARCHAR2, tableName IN VARCHAR2, overwrite IN BOOLEAN DEFAULT TRUE); Parameters Table 211-21 SETDEFAULTTABLE Procedure Parameters Parameter Description xmlschema XML schema to be annotated globalElementName Name of the global element in the schema tableName Name being assigned to the table overwrite Boolean that indicates whether or not the procedure overwrites element attributes. The default is TRUE .