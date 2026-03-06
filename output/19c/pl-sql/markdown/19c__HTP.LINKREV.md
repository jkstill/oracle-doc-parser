---
id: 19c__HTP.LINKREV
name: HTP.LINKREV
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: HTP
tags: [htp]
source_file: HTP.html
---

# HTP.LINKREV

This procedure generates the <LINK> tag with the REV attribute which delineates the relationship described by the hypertext link from the target to the anchor.

## Syntax

```sql
HTP.LINKREV(
   crev           IN       VARCHAR2,
   curl           IN       VARCHAR2,
   ctitle         IN       VARCHAR2   DEFAULT NULL);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| crel |  |  | The value for the REV attribute. |
| curl | VARCHAR2 | IN | The value for the URL attribute. |
| ctitle | VARCHAR2 | IN | The value for the TITLE attribute. |

## Usage Notes

This is the opposite of the LINKREL Procedure . This tag indicates a relationship between documents, but does not create a link. To create a link, use the ANCHOR Procedure . Syntax HTP.LINKREV( crev IN VARCHAR2, curl IN VARCHAR2, ctitle IN VARCHAR2 DEFAULT NULL); Parameters Table 221-56 LINKREV Procedure Parameters Parameter Description crel The value for the REV attribute. curl The value for the URL attribute. ctitle The value for the TITLE attribute. Examples This procedure generates <LINK REV=" crev " HREF=" curl " TITLE=" ctitle ">