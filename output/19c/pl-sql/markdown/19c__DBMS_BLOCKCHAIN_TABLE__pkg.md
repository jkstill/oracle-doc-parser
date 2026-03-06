---
id: 19c__DBMS_BLOCKCHAIN_TABLE__pkg
name: DBMS_BLOCKCHAIN_TABLE
object_type: plsql_package
oracle_version: 19c
doc_type: plsql_packages
tags: [dbms_blockchain_table]
source_file: dbms_blockchain_table.html
---

# DBMS_BLOCKCHAIN_TABLE

A blockchain table is an append-only table designed for centralized blockchain applications. The DBMS_BLOCKCHAIN_TABLE package allows you do the following: delete rows in a blockchain table that are beyond the row retention defined for the blockchain table; get the bytes that are input to the cryptographic hash for a row so you can verify the hash in the row; sign a row you inserted into a blockchain table after the row is added to a chain in the blockchain table; and have the database verify the hashes on some or all rows in a blockchain table. Blockchain tables support only DER encoding for X.509 certificates, not PEM encoding.