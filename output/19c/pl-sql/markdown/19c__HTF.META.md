---
id: 19c__HTF.META
name: HTF.META
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: HTF
tags: [htf]
source_file: HTF.html
---

# HTF.META

This function generates the <META> tag, which embeds meta-information about the document and also specifies values for HTTP headers. For example, you can specify the expiration date, keywords, and author name.

## Syntax

```sql
HTF.META(
   chttp_equiv    IN       VARCHAR2,
   cname          IN       VARCHAR2,
   ccontent       IN       VARCHAR2)
  RETURN VARCHAR2;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| chttp_equiv | VARCHAR2 | IN | The value for the CHTTP_EQUIV attribute. |
| cname | VARCHAR2 | IN | The value for the NAME attribute. |
| ccontent | VARCHAR2) | IN | The value for the CONTENT attribute. |

**Returns:** `VARCHAR2`

## Usage Notes

Syntax HTF.META( chttp_equiv IN VARCHAR2, cname IN VARCHAR2, ccontent IN VARCHAR2) RETURN VARCHAR2; Parameters Table 220-63 META Function Parameters Parameter Description chttp_equiv The value for the CHTTP_EQUIV attribute. cname The value for the NAME attribute. ccontent The value for the CONTENT attribute. Examples This function generates <META HTTP-EQUIV="chttp_equiv" NAME ="cname" CONTENT="ccontent"> so that HTF.meta ('Refresh', NULL, 120); generates <META HTTP-EQUIV="Refresh" CONTENT=120> On some Web browsers, this causes the current URL to be reloaded automatically every 120 seconds.