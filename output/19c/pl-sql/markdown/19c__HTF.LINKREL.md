---
id: 19c__HTF.LINKREL
name: HTF.LINKREL
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: HTF
tags: [htf]
source_file: HTF.html
---

# HTF.LINKREL

This function generates the <LINK> tag with the REL attribute which delineates the relationship described by the hypertext link from the anchor to the target. This is only used when the HREF attribute is present.

## Syntax

```sql
HTF.LINKREL(
   crel           IN       VARCHAR2,
   curl           IN       VARCHAR2,
   ctitle         IN       VARCHAR2   DEFAULT NULL)
  RETURN VARCHAR2;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| crel | VARCHAR2 | IN | The value for the REL attribute. |
| curl | VARCHAR2 | IN | The value for the URL attribute. |
| ctitle | VARCHAR2 | IN | The value for the TITLE attribute. |

**Returns:** `VARCHAR2`

## Usage Notes

This is the opposite of LINKREV Function . This tag indicates a relationship between documents but does not create a link. To create a link, use the ANCHOR Function . Syntax HTF.LINKREL( crel IN VARCHAR2, curl IN VARCHAR2, ctitle IN VARCHAR2 DEFAULT NULL) RETURN VARCHAR2; Parameters Table 220-57 LINKREL Function Parameters Parameter Description crel The value for the REL attribute. curl The value for the URL attribute. ctitle The value for the TITLE attribute. Examples This function generates <LINK REL="crel" HREF="curl" TITLE="ctitle">