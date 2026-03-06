---
id: 19c__DBMS_MGD_ID_UTL.SET_PROXY
name: DBMS_MGD_ID_UTL.SET_PROXY
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_MGD_ID_UTL
tags: [dbms_mgd_id_utl]
source_file: DBMS_MGD_ID_UTL.html
---

# DBMS_MGD_ID_UTL.SET_PROXY

This procedure sets the host and port of the proxy server for Internet access.

## Syntax

```sql
DBMS_MGD_ID_UTL.SET_PROXY (
   proxt_host   IN  VARCHAR2,
   proxy_port   IN  VARCHAR2);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| proxy_host |  |  | Name of host |
| proxy_port | VARCHAR2) | IN | Host port number |

## Usage Notes

This procedure must be called if the database server accesses the Internet using a proxy server. Internet access is necessary because some rules need to look up the Object Naming Service (ONS) table to get the company prefix index. You do not need to call this procedure does if you are only using schemes that do not contain any rules requiring Internet access. Syntax DBMS_MGD_ID_UTL.SET_PROXY ( proxt_host IN VARCHAR2, proxy_port IN VARCHAR2); Parameters Table 109-18 SET_PROXY Procedure Parameters Parameter Description proxy_host Name of host proxy_port Host port number Examples See the REFRESH_CATEGORY Function for an example.