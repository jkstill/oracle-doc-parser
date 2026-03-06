---
id: 19c__HTP.META
name: HTP.META
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: HTP
tags: [htp]
source_file: HTP.html
---

# HTP.META

This procedure generates the <META> tag, which embeds meta-information about the document and also specifies values for HTTP headers. For example, you can specify the expiration date, keywords, and author name.

## Syntax

```sql
HTP.META(
   chttp_equiv    IN       VARCHAR2,
   cname          IN       VARCHAR2,
   ccontent       IN       VARCHAR2);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| chttp_equiv | VARCHAR2 | IN | The value for the CHTTP_EQUIV attribute. |
| cname | VARCHAR2 | IN | The value for the NAME attribute. |
| ccontent | VARCHAR2) | IN | The value for the CONTENT attribute. |

## Usage Notes

Syntax HTP.META( chttp_equiv IN VARCHAR2, cname IN VARCHAR2, ccontent IN VARCHAR2); Parameters Table 221-61 META Procedure Parameters Parameter Description chttp_equiv The value for the CHTTP_EQUIV attribute. cname The value for the NAME attribute. ccontent The value for the CONTENT attribute. Examples This procedure generates <META HTTP-EQUIV=" chttp_equiv " NAME =" cname" CONTENT=" ccontent "> so that HTP.meta ('Refresh', NULL, 120); generates <META HTTP-EQUIV="Refresh" CONTENT=120> On some Web browsers, this causes the current URL to be reloaded automatically every 120 seconds.