---
id: 19c__OWA_SEC.SET_AUTHORIZATION
name: OWA_SEC.SET_AUTHORIZATION
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: OWA_SEC
tags: [owa_sec]
source_file: OWA_SEC.html
---

# OWA_SEC.SET_AUTHORIZATION

This procedure, called in the initialization portion of the OWA_CUSTOM package, sets the authorization scheme for the PL/SQL Gateway.

## Syntax

```sql
OWA_SEC.SET_AUTHORIZATION(
    scheme         IN       INTEGER);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| scheme | INTEGER) | IN | The authorization scheme. It is one of the following schemes for SET_AUTHORIZATION : OWA_SEC.NO_CHECK - Specifies that the PL/SQL application is not to do any custom authentication. This is the default. OWA_SEC.GLOBAL - Defines an authorize function that is called for all users and all procedures. This is the OWA_CUSTOM . AUTHORIZE Function in the " sys " schema. OWA_SEC.PER_PACKAGE - Define an authorize function that is called when procedures in a package or anonymous procedures are called. If the procedures are in a package, the package. AUTHORIZE function in the user's schema is called to authorize the user. If the procedures are not in a package, then the anonymous authorize function in the user's schema is called. OWA_SEC.CUSTOM - Implements different authorize functions for each user. The function OWA_CUSTOM . AUTHORIZE Function in the user's schema is called to authorize the user. If the user's schema does not contain an OWA_CUSTOM .AUTHORIZE Function, the PL/SQL Gateway looks for it in the "sys" schema. The custom authorize function has the following signature: FUNCTION AUTHORIZE RETURN BOOLEAN; If the function returns TRUE , authentication succeeded. If it returns FALSE , authentication failed. If the authorize function is not defined, the Gateway returns an error and fails. |

## Usage Notes

This implements your authorize function, which authorizes the user before his requested procedure is run. The placement of the authorize function depends on the scheme you select. Syntax OWA_SEC.SET_AUTHORIZATION( scheme IN INTEGER); Parameters Table 228-2 SET_AUTHORIZATION Procedure Parameters Parameter Description scheme The authorization scheme. It is one of the following schemes for SET_AUTHORIZATION : OWA_SEC.NO_CHECK - Specifies that the PL/SQL application is not to do any custom authentication. This is the default. OWA_SEC.GLOBAL - Defines an authorize function that is called for all users and all procedures. This is the OWA_CUSTOM . AUTHORIZE Function in the " sys " schema. OWA_SEC.PER_PACKAGE - Define an authorize function that is called when procedures in a package or anonymous procedures are called. If the procedures are in a package, the package. AUTHORIZE function in the user's schema is called to authorize the user. If the procedures are not in a package, then the anonymous authorize function in the user's schema is called. OWA_SEC.CUSTOM - Implements different authorize functions for each user. The function OWA_CUSTOM . AUTHORIZE Function in the user's schema is called to authorize the user. If the user's schema does not contain an OWA_CUSTOM .AUTHORIZE Function, the PL/SQL Gateway looks for it in the "sys" schema. The custom authorize function has the following signature: FUNCTION AUTHORIZE RETURN BOOLEAN; If the function returns TRUE , authentication succeeded. If it returns FALSE , authentication failed. If the authorize function is not defined, the Gateway returns an error and fails.