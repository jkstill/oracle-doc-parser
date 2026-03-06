---
id: 19c__UTL_INADDR.GET_HOST_NAME
name: UTL_INADDR.GET_HOST_NAME
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: UTL_INADDR
tags: [utl_inaddr]
source_file: UTL_INADDR.html
---

# UTL_INADDR.GET_HOST_NAME

This function retrieves the name of the local or remote host given its IP address.

## Syntax

```sql
UTL_INADDR.GET_HOST_NAME (
   ip  IN VARCHAR2 DEFAULT NULL)
RETURN host_name VARCHAR2;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| ip | VARCHAR2 | IN | The IP address of the host used to determine its host name. If ip is not NULL, the official name of the host with its domain name is returned. If this is NULL, the name of the local host is returned and the name does not contain the domain to which the local host belongs. |

**Returns:** `host_name`

## Usage Notes

Syntax UTL_INADDR.GET_HOST_NAME ( ip IN VARCHAR2 DEFAULT NULL) RETURN host_name VARCHAR2; Parameters Table 267-5 GET_HOST_NAME Function Parameters Parameter Description ip The IP address of the host used to determine its host name. If ip is not NULL, the official name of the host with its domain name is returned. If this is NULL, the name of the local host is returned and the name does not contain the domain to which the local host belongs. Return Values Table 267-6 GET_HOST_NAME Function Return Values Parameter Description host_name The name of the local or remote host of the specified IP address. Exceptions UNKNOWN_HOST: The specified IP address is unknown Usage Notes The permission to obtain the host name or IP address of the current host is controlled by the resolve privilege granted through DBMS_NETWORK_ACL_ADMIN on LOCALHOST .