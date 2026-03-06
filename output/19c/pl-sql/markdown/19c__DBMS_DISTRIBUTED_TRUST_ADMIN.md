---
id: 19c__DBMS_DISTRIBUTED_TRUST_ADMIN
name: DBMS_DISTRIBUTED_TRUST_ADMIN
object_type: plsql_subprogram
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_DISTRIBUTED_TRUST_ADMIN
tags: [dbms_distributed_trust_admin]
source_file: DBMS_DISTRIBUTED_TRUST_ADMIN.html
---

# DBMS_DISTRIBUTED_TRUST_ADMIN

If you have not yet used the package DBMS_DISTRIBUTED_TRUST_ADMIN to change the trust listing, by default you trust all databases in the same enterprise domain if that domain it listed as trusted in the directory service:

## Syntax

```sql
SELECT * FROM TRUSTED_SERVERS;
TRUST      NAME                                                                            
--------- ---------------------
Trusted   All
```

## Usage Notes

SELECT * FROM TRUSTED_SERVERS; TRUST NAME --------- --------------------- Trusted All Because all servers are currently trusted, you can execute the DENY_SERVER Procedure and specify that a particular server is not trusted: EXECUTE DBMS_DISTRIBUTED_TRUST_ADMIN.DENY_SERVER ('SALES.US.AMERICAS.ACME_AUTO.COM'); PL/SQL procedure successfully completed. SELECT * FROM TRUSTED_SERVERS; TRUST NAME --------- ----------------------------------------------- Untrusted SALES.US.AMERICAS.ACME_AUTO.COM By executing the DENY_ALL Procedure , you can choose to not trust any database server: EXECUTE DBMS_DISTRIBUTED_TRUST_ADMIN.DENY_ALL; PL/SQL procedure successfully completed. SELECT * FROM TRUSTED_SERVERS; TRUST NAME --------- ----------------------------------------------- Untrusted All The ALLOW_SERVER Procedure can be used to specify that one particular database is to be trusted: EXECUTE DBMS_DISTRIBUTED_TRUST_ADMIN.ALLOW_SERVER ('SALES.US.AMERICAS.ACME_AUTO.COM'); PL/SQL procedure successfully completed. SELECT * FROM TRUSTED_SERVERS; TRUST NAME --------- ------------------------------------------------ Trusted SALES.US.AMERICAS.ACME_AUTO.COM