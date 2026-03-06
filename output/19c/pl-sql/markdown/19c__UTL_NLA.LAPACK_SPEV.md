---
id: 19c__UTL_NLA.LAPACK_SPEV
name: UTL_NLA.LAPACK_SPEV
object_type: plsql_subprogram
oracle_version: 19c
doc_type: plsql_packages
parent: UTL_NLA
tags: [utl_nla]
source_file: UTL_NLA.html
---

# UTL_NLA.LAPACK_SPEV

This procedure computes all the eigenvalues and, optionally, eigenvectors of a real symmetric matrix A in packed storage.

## Syntax

```sql
UTL_NLA.LAPACK_SPEV (
   jobz     IN      flag,
   uplo     IN      flag,
   n        IN      POSITIVEN,
   ap       IN OUT  UTL_NLA_ARRAY_DBL,
   w        IN OUT  UTL_NLA_ARRAY_DBL,
   z        IN OUT  UTL_NLA_ARRAY_DBL,
   ldz      IN      POSITIVEN,
   info     OUT     INTEGER,
   pack     IN      flag DEFAULT 'C');
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| jobz | flag | IN | 'N' : Compute eigenvalues only. 'V' : Compute eigenvalues and eigenvectors. |
| uplo | flag | IN | 'U' : Upper triangle of A is stored. 'L' : Lower triangle of A is stored. |
| n | POSITIVEN | IN | The order of the matrix a. N >= 0 . |
| ap | UTL_NLA_ARRAY_DBL | IN OUT | UTL_NLA_ARRAY_FLT / DBL, DIMENSION (n*(n+1)/2) . On entry, the upper or lower triangle of the symmetric matrix a packed columnwise in a linear array. The j -th column of a is stored in the array ap : If uplo = 'U' , ap(i + (j-1)*j/2) = a(i,j) for 1<=i<=j . If uplo = 'L' , ap(i + (j-1)*(2*n-j)/2) = a(i,j) for j<=i<=n . On exit, ap is overwritten by values generated during the reduction to tridiagonal form: If uplo = 'U' , the diagonal and first superdiagonal of the tridiagonal matrix T overwrite the corresponding elements of A . If uplo = 'L' , the diagonal and first subdiagonal of T overwrite the corresponding elements of A . |
| w | UTL_NLA_ARRAY_DBL | IN OUT | UTL_NLA_ARRAY_FLT/DBL , DIMENSION (n) . If info = 0 , the eigenvalues in ascending order. |
| z | UTL_NLA_ARRAY_DBL | IN OUT | UTL_NLA_ARRAY_FLT/DBL , DIMENSION (ldz,n) . If jobz = 'V' , then if info = 0 , z contains the orthonormal eigenvectors of the matrix A , with the i -th column of z holding the eigenvector associated with w(i) . If jobz = 'N' , then z is not referenced. |
| ldz | POSITIVEN | IN | The leading dimension of the array z . ldz >= 1 , and if jobz = 'v' , ldz >= max(1,n) . |
| info | INTEGER | OUT | = 0 : successful exit < 0 : if info = -i , the i -th argument had an illegal value > 0 : if info = i , the algorithm failed to converge; i off-diagonal elements of an intermediate tridiagonal form did not converge to zero |
| pack | flag | IN | (Optional) Flags the packing of the matrices: 'C' : column-major (default) 'R' : row-major |

## Usage Notes

See Also: LAPACK Driver Routines (LLS and Eigenvalue Problems) Subprograms for other subprograms in this group See Also: LAPACK Driver Routines (LLS and Eigenvalue Problems) Subprograms for other subprograms in this group Syntax UTL_NLA.LAPACK_SPEV ( jobz IN flag, uplo IN flag, n IN POSITIVEN, ap IN OUT UTL_NLA_ARRAY_DBL, w IN OUT UTL_NLA_ARRAY_DBL, z IN OUT UTL_NLA_ARRAY_DBL, ldz IN POSITIVEN, info OUT INTEGER, pack IN flag DEFAULT 'C'); UTL_NLA.LAPACK_SPEV ( jobz IN flag, uplo IN flag, n IN POSITIVEN, ap IN OUT UTL_NLA_ARRAY_FLT, w IN OUT UTL_NLA_ARRAY_FLT, z IN OUT UTL_NLA_ARRAY_FLT, ldz IN POSITIVEN, info OUT INTEGER, pack IN flag DEFAULT 'C'); Parameters Table 271-53 LAPACK_SPEV Procedure Parameters Parameter Description jobz 'N' : Compute eigenvalues only. 'V' : Compute eigenvalues and eigenvectors. uplo 'U' : Upper triangle of A is stored. 'L' : Lower triangle of A is stored. n The order of the matrix a. N >= 0 . ap UTL_NLA_ARRAY_FLT / DBL, DIMENSION (n*(n+1)/2) . On entry, the upper or lower triangle of the symmetric matrix a packed columnwise in a linear array. The j -th column of a is stored in the array ap : If uplo = 'U' , ap(i + (j-1)*j/2) = a(i,j) for 1<=i<=j . If uplo = 'L' , ap(i + (j-1)*(2*n-j)/2) = a(i,j) for j<=i<=n . On exit, ap is overwritten by values generated during the reduction to tridiagonal form: If uplo = 'U' , the diagonal and first superdiagonal of the tridiagonal matrix T overwrite the corresponding elements of A . If uplo = 'L' , the diagonal and first subdiagonal of T overwrite the corresponding elements of A . w UTL_NLA_ARRAY_FLT/DBL , DIMENSION (n) . If info = 0 , the eigenvalues in ascending order. z UTL_NLA_ARRAY_FLT/DBL , DIMENSION (ldz,n) . If jobz = 'V' , then if info = 0 , z contains the orthonormal eigenvectors of the matrix A , with the i -th column of z holding the eigenvector associated with w(i) . If jobz = 'N' , then z is not referenced. ldz The leading dimension of the array z . ldz >= 1 , and if jobz = 'v' , ldz >= max(1,n) . info = 0 : successful exit < 0 : if info = -i , the i -th argument had an illegal value > 0 : if info = i , the algorithm failed to converge; i off-diagonal elements of an intermediate tridiagonal form did not converge to zero pack (Optional) Flags the packing of the matrices: 'C' : column-major (default) 'R' : row-major