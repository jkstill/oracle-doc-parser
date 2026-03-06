---
id: 19c__SESSION_CACHED_CURSORS
name: SESSION_CACHED_CURSORS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: performance
source_file: SESSION_CACHED_CURSORS.html
---

# SESSION_CACHED_CURSORS

SESSION_CACHED_CURSORS specifies the number of session cursors to cache.

## Usage Notes

Repeated parse calls of the same SQL (including recursive SQL) or PL/SQL statement cause the session cursor for that statement to be moved into the session cursor cache. Oracle uses a least recently used algorithm to remove entries in the session cursor cache to make room for new entries when needed. See Also: Oracle Database Performance Tuning Guide for information about enabling the session cursor cache See Also: Oracle Database Performance Tuning Guide for information about enabling the session cursor cache