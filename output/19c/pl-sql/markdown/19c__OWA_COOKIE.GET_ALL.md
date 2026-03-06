---
id: 19c__OWA_COOKIE.GET_ALL
name: OWA_COOKIE.GET_ALL
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: OWA_COOKIE
tags: [owa_cookie]
source_file: OWA_COOKIE.html
---

# OWA_COOKIE.GET_ALL

This procedure returns all cookie names and their values from the client's browser. The values appear in the order in which they were sent from the browser.

## Syntax

```sql
OWA_COOKIE.GET_ALL(
   names          OUT      vc_arr,
   vals           OUT      vc_arr,
   num_vals       OUT      INTEGER);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| names | vc_arr | OUT | The names of the cookies. |
| vals | vc_arr | OUT | The values of the cookies. |
| num_vals | INTEGER) | OUT | The number of cookie-value pairs. |

## Usage Notes

Syntax OWA_COOKIE.GET_ALL( names OUT vc_arr, vals OUT vc_arr, num_vals OUT INTEGER); Parameters Table 223-3 GET_ALL Procedure Parameters Parameter Description names The names of the cookies. vals The values of the cookies. num_vals The number of cookie-value pairs.