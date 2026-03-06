---
id: 19c__UTL_INADDR.GET_HOST_ADDRESS
name: UTL_INADDR.GET_HOST_ADDRESS
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: UTL_INADDR
tags: [utl_inaddr]
source_file: UTL_INADDR.html
---

# UTL_INADDR.GET_HOST_ADDRESS

This function retrieves the IP address of the specified host.

## Syntax

```sql
UTL_INADDR.GET_HOST_ADDRESS (
   host  IN VARCHAR2 DEFAULT NULL) 
RETURN host_address VARCHAR2;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| host | VARCHAR2 | IN | The name of the host to retrieve the IP address. |

**Returns:** `host_address`

## Usage Notes

Syntax UTL_INADDR.GET_HOST_ADDRESS ( host IN VARCHAR2 DEFAULT NULL) RETURN host_address VARCHAR2; Parameters Table 267-3 GET_HOST_ADDRESS Function Parameters Parameter Description host The name of the host to retrieve the IP address. Return Values Table 267-4 GET_HOST_ADDRESS Function Return Values Parameter Description host_address The IP address of the specified host, or that of the local host if host is NULL . Exceptions UNKNOWN_HOST: The specified IP address is unknown Usage Notes The permission to obtain the host name or IP address of the current host is controlled by the resolve privilege on LOCALHOST .