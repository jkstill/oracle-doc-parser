---
id: 19c__DBMS_XMLSCHEMA_ANNOTATE.SETTIMESTAMPWITHTIMEZONE
name: DBMS_XMLSCHEMA_ANNOTATE.SETTIMESTAMPWITHTIMEZONE
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XMLSCHEMA_ANNOTATE
tags: [dbms_xmlschema_annotate]
source_file: DBMS_XMLSCHEMA_ANNOTATE.html
---

# DBMS_XMLSCHEMA_ANNOTATE.SETTIMESTAMPWITHTIMEZONE

This procedure sets the TIMESTAMPWITHTIMEZONE datatype to all dateTime typed elements in the XML schema.

## Syntax

```sql
DBMS_XMLSCHEMA_ANNOTATE.SETTIMESTAMPWITHTIMEZONE (
   xmlschema      IN OUT   XMLTYPE, 
   overwrite      IN       BOOLEAN DEFAULT TRUE);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| xmlschema | XMLTYPE | IN OUT | XML schema to be annotated |
| overwrite | BOOLEAN | IN | Boolean that indicates whether or not the procedure overwrites element attributes. The default is TRUE . |

## Usage Notes

This is equivalent to adding xdb:SQLType="TIMESTAMP WITH TIME ZONE" to all dateTime objects. Syntax DBMS_XMLSCHEMA_ANNOTATE. SETTIMESTAMPWITHTIMEZONE ( xmlschema IN OUT XMLTYPE, overwrite IN BOOLEAN DEFAULT TRUE); Parameters Table 211-29 SETTIMESTAMPWITHTIMEZONE Procedure Parameters Parameter Description xmlschema XML schema to be annotated overwrite Boolean that indicates whether or not the procedure overwrites element attributes. The default is TRUE .