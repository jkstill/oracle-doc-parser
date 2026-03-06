---
id: 19c__DBMS_SESSION.FREE_UNUSED_USER_MEMORY
name: DBMS_SESSION.FREE_UNUSED_USER_MEMORY
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_SESSION
tags: [dbms_session]
source_file: DBMS_SESSION.html
---

# DBMS_SESSION.FREE_UNUSED_USER_MEMORY

This procedure reclaims unused memory after performing operations requiring large amounts of memory (more than 100K).

## Syntax

```sql
DBMS_SESSION.FREE_UNUSED_USER_MEMORY;
```

## Usage Notes

Examples of operations that use large amounts of memory include: Large sorting where entire sort_area_size is used and sort_area_size is hundreds of KB. Compiling large PL/SQL packages, procedures, or functions. Storing hundreds of KB of data within PL/SQL indexed tables. You can monitor user memory by tracking the statistics "session UGA memory" and "session PGA memory" in the v$sesstat or v$statname fixed views. Monitoring these statistics also shows how much memory this procedure has freed. Note: This procedure should only be used in cases where memory is at a premium. It should be used infrequently and judiciously. Note: This procedure should only be used in cases where memory is at a premium. It should be used infrequently and judiciously. Syntax DBMS_SESSION.FREE_UNUSED_USER_MEMORY; Return Values The behavior of this procedure depends upon the configuration of the server operating on behalf of the client: Dedicated server : This returns unused PGA memory and session memory to the operating system. Session memory is allocated from the PGA in this configuration. Shared server : This returns unused session memory to the shared_pool . Session memory is allocated from the shared_pool in this configuration. Usage Notes In order to free memory using this procedure, the memory must not be in use. After an operation allocates memory, only the same type of operation can reuse the allocated memory. For example, after memory is allocated for sort, even if the sort is complete and the memory is no longer in use, only another sort can reuse the sort-allocated memory. For both sort and compilation, after the operation is complete, the memory is no longer in use, and the user can call this procedure to free the unused memory. An indexed table implicitly allocates memory to store values assigned to the indexed table's elements. Thus, the more elements in an indexed table, the more memory the RDBMS allocates to the indexed table. As long as there are elements within the indexed table, the memory associated with an indexed table is in use. The scope of indexed tables determines how long their memory is in use. Indexed tables declared globally are indexed tables declared in packages or package bodies. They allocate memory from session memory. For an indexed table declared globally, the memory remains in use for the lifetime of a user's login (lifetime of a user's session), and is freed after the user disconnects from ORACLE. Indexed tables declared locally are indexed tables declared within functions, procedures, or anonymous blocks. These indexed tables allocate memory from PGA memory. For an indexed table declared locally, the memory remains in use for as long as the user is still running the procedure, function, or anonymous block in which the indexed table is declared.After the procedure, function, or anonymous block is finished running, the memory is then available for other locally declared indexed tables to use (in other words, the memory is no longer in use). Assigning an uninitialized, "empty" indexed table to an existing index table is a method to explicitly re-initialize the indexed table and the memory associated with the indexed table. After this operation, the memory associated with the indexed table is no longer in use, making it available to be freed by calling this procedure. This method is particularly useful on indexed tables declared globally which can grow during the lifetime of a user's session, as long as the user no longer needs the contents of the indexed table. The memory rules associated with an indexed table's scope still apply; this method and this procedure, however, allow users to intervene and to explicitly free the memory associated with an indexed table.