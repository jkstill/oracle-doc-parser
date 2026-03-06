---
id: 19c__V$ENCRYPTION_WALLET
name: V$ENCRYPTION_WALLET
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dynamic_performance]
source_file: V-ENCRYPTION_WALLET.html
---

# V$ENCRYPTION_WALLET

V$ENCRYPTION_WALLET displays information on the status of the wallet and the wallet location for Transparent Data Encryption. In a multitenant container database (CDB), this view displays information on the wallets for all pluggable database (PDBs) when queried from CDB$ROOT . When queried from a PDB, this view only displays wallet details of that PDB.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| WRL_TYPE | VARCHAR2(20) |  |
| WRL_PARAMETER | VARCHAR2(4000) |  |
| STATUS | VARCHAR2(30) |  |
| WALLET_TYPE | VARCHAR2(20) |  |
| WALLET_ORDER | VARCHAR2(9) |  |
| KEYSTORE_MODE | VARCHAR2(8) |  |
| FULLY_BACKED_UP | VARCHAR2(9) |  |
| CON_ID | NUMBER |  |

## Usage Notes

See Also: " TDE_CONFIGURATION " " WALLET_ROOT " Oracle Database Advanced Security Guide for information about creating user-defined master encryption keys Oracle Database Advanced Security Guide for information about opening hardware keystores See Also: " TDE_CONFIGURATION " " WALLET_ROOT " Oracle Database Advanced Security Guide for information about creating user-defined master encryption keys Oracle Database Advanced Security Guide for information about opening hardware keystores