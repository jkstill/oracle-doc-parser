---
id: 19c__HTF.LINKREV
name: HTF.LINKREV
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: HTF
tags: [htf]
source_file: HTF.html
---

# HTF.LINKREV

This function generates the <LINK> tag with the REV attribute which delineates the relationship described by the hypertext link from the target to the anchor.

## Syntax

```sql
HTF.LINKREV(
   crev           IN       VARCHAR2,
   curl           IN       VARCHAR2,
   ctitle         IN       VARCHAR2   DEFAULT NULL)
  RETURN VARCHAR2;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| crev | VARCHAR2 | IN | The value for the REV attribute. |
| curl | VARCHAR2 | IN | The value for the URL attribute. |
| ctitle | VARCHAR2 | IN | The value for the TITLE attribute. |

**Returns:** `VARCHAR2`

## Usage Notes

This is the opposite of the LINKREL Function . This tag indicates a relationship between documents, but does not create a link. To create a link, use the ANCHOR Function . Syntax HTF.LINKREV( crev IN VARCHAR2, curl IN VARCHAR2, ctitle IN VARCHAR2 DEFAULT NULL) RETURN VARCHAR2; Parameters Table 220-58 LINKREV Function Parameters Parameter Description crev The value for the REV attribute. curl The value for the URL attribute. ctitle The value for the TITLE attribute. Examples This function generates <LINK REV="crev" HREF="curl" TITLE="ctitle">