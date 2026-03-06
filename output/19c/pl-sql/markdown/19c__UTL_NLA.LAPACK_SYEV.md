---
id: 19c__UTL_NLA.LAPACK_SYEV
name: UTL_NLA.LAPACK_SYEV
object_type: plsql_subprogram
oracle_version: 19c
doc_type: plsql_packages
parent: UTL_NLA
tags: [utl_nla]
source_file: UTL_NLA.html
---

# UTL_NLA.LAPACK_SYEV

This procedure computes all eigenvalues and, optionally, eigenvectors of a real symmetric matrix A .

## Syntax

```sql
UTL_NLA.LAPACK_SYEV (
   jobz     IN      flag,
   uplo     IN      flag,
   n        IN      POSITIVEN,
   a        IN OUT  UTL_NLA_ARRAY_DBL,
   lda      IN      POSITIVEN,
   w        IN OUT  UTL_NLA_ARRAY_DBL,
   info     OUT     INTEGER,
   pack     IN      flag DEFAULT 'C');
```

## Usage Notes

See Also: LAPACK Driver Routines (LLS and Eigenvalue Problems) Subprograms for other subprograms in this group See Also: LAPACK Driver Routines (LLS and Eigenvalue Problems) Subprograms for other subprograms in this group Syntax UTL_NLA.LAPACK_SYEV ( jobz IN flag, uplo IN flag, n IN POSITIVEN, a IN OUT UTL_NLA_ARRAY_DBL, lda IN POSITIVEN, w IN OUT UTL_NLA_ARRAY_DBL, info OUT INTEGER, pack IN flag DEFAULT 'C'); UTL_NLA.LAPACK_SYEV ( jobz IN flag, uplo IN flag, n IN POSITIVEN, a IN OUT UTL_NLA_ARRAY_FLT, lda IN POSITIVEN, w IN OUT UTL_NLA_ARRAY_FLT, info OUT INTEGER, pack IN flag DEFAULT 'C'); Parameters Table 271-58 LAPACK_SYEV Procedure Parameters Paramete Description jobz 'N' : Compute eigenvalues only. 'V' : Compute eigenvalues and eigenvectors. uplo 'U' : Upper triangle of A is stored. 'L' : Upper triangle of A is stored. n The order of the matrix a. N >= 0 . a UTL_NLA_ARRAY_FLT / DBL, DIMENSION (lda, n) . On entry, the symmetric matrix a : If uplo = 'U' , the leading n by n upper triangular part of a contains the upper triangular part of the matrix a . If uplo = 'L' , the leading n by n lower triangular part of a contains the lower triangular part of the matrix a . On exit: If jobz = 'V' , then if info = 0 , a contains the orthonormal eigenvectors of the matrix a . If jobz = 'N' , then on exit the lower triangle (if uplo = 'L' ) or the upper triangle (if uplo='U' ) of a , including the diagonal, is destroyed. lda The leading dimension of the array a . lda >= max(1,n) . w UTL_NLA_ARRAY_FLT/DBL , DIMENSION (n) . If info = 0 , the eigenvalues in ascending order. info = 0 : successful exit < 0 : if info = -i , the i -th argument had an illegal value > 0 : if info = i , the algorithm failed to converge; i off-diagonal elements of an intermediate tridiagonal form did not converge to zero pack (Optional) Flags the packing of the matrices: 'C' : column-major (default) 'R' : row-major