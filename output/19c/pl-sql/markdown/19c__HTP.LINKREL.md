---
id: 19c__HTP.LINKREL
name: HTP.LINKREL
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: HTP
tags: [htp]
source_file: HTP.html
---

# HTP.LINKREL

This procedure generates the <LINK> tag with the REL attribute which delineates the relationship described by the hypertext link from the anchor to the target. This is only used when the HREF attribute is present.

## Syntax

```sql
HTP.LINKREL(
   crel           IN       VARCHAR2,
   curl           IN       VARCHAR2,
   ctitle         IN       VARCHAR2   DEFAULT NULL);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| crel | VARCHAR2 | IN | The value for the REL attribute. |
| curl | VARCHAR2 | IN | The value for the URL attribute. |
| ctitle | VARCHAR2 | IN | The value for the TITLE attribute. |

## Usage Notes

This is the opposite of LINKREV Procedure . This tag indicates a relationship between documents but does not create a link. To create a link, use the ANCHOR Procedure . Syntax HTP.LINKREL( crel IN VARCHAR2, curl IN VARCHAR2, ctitle IN VARCHAR2 DEFAULT NULL); Parameters Table 221-55 LINKREL Procedure Parameters Parameter Description crel The value for the REL attribute. curl The value for the URL attribute. ctitle The value for the TITLE attribute. Examples This procedure generates <LINK REL=" crel " HREF=" curl " TITLE=" ctitle ">