---
id: 19c__OWA_SEC.SET_PROTECTION_REALM
name: OWA_SEC.SET_PROTECTION_REALM
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: OWA_SEC
tags: [owa_sec]
source_file: OWA_SEC.html
---

# OWA_SEC.SET_PROTECTION_REALM

This procedure sets the realm of the page that is returned to the user. The user enters a username and login that already exist in the realm.

## Syntax

```sql
OWA_SEC.SET_PROTECTION_REALM(
   realm      IN      VARCHAR2);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| realm | VARCHAR2) | IN | The realm where the page belongs. This string is displayed to the user. |

## Usage Notes

Syntax OWA_SEC.SET_PROTECTION_REALM( realm IN VARCHAR2); Parameters Table 228-3 SET_PROTECTION_REALM Procedure Parameters Parameter Description realm The realm where the page belongs. This string is displayed to the user.