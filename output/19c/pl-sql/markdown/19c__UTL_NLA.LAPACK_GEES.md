---
id: 19c__UTL_NLA.LAPACK_GEES
name: UTL_NLA.LAPACK_GEES
object_type: plsql_subprogram
oracle_version: 19c
doc_type: plsql_packages
parent: UTL_NLA
tags: [utl_nla]
source_file: UTL_NLA.html
---

# UTL_NLA.LAPACK_GEES

This procedure computes for an n by n real nonsymmetric matrix A , the eigenvalues, the real Schur form T , and, optionally, the matrix of Schur vectors Z .

## Syntax

```sql
UTL_NLA.LAPACK_GEES (
   jobvs   IN       flag,
   n       IN       POSITIVEN,
   a       IN  OUT  UTL_NLA_ARRAY_DBL,
   lda     IN       POSITIVEN,
   wr      IN OUT   UTL_NLA_ARRAY_DBL,
   wi      IN OUT   UTL_NLA_ARRAY_DBL,
   vs      IN OUT   UTL_NLA_ARRAY_DBL,
   ldvs    IN       POSITIVEN,
   info    OUT      INTEGER,
   pack    IN       flag DEFAULT 'C');
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| jobz |  |  | 'N' : Schur vectors are not computed. 'V' : Schur vectors are computed. |
| n | POSITIVEN | IN | The order of the matrix a. N >= 0 . |
| a | UTL_NLA_ARRAY_DBL | IN  OUT | UTL_NLA_ARRAY_FLT/DBL , DIMENSION (lda, n) . On entry, the n by n matrix A . On exit, A has been overwritten by its real Schur form T . |
| lda | POSITIVEN | IN | The leading dimension of the array a. lda >= max(1,n) . |
| wr | UTL_NLA_ARRAY_DBL | IN OUT | UTL_NLA_ARRAY_FLT/DBL , DIMENSION (n) . wr and wi contain the real and imaginary parts respectively of the computed eigenvalues in the same order that they appear on the diagonal of the output Schur form T . Complex conjugate pairs of eigenvalues will appear consecutively with the eigenvalue having the positive imaginary part first. |
| wi | UTL_NLA_ARRAY_DBL | IN OUT | UTL_NLA_ARRAY_FLT/DBL , DIMENSION (ldz, n) . wr and wi contain the real and imaginary parts respectively of the computed eigenvalues in the same order that they appear on the diagonal of the output Schur form T . Complex conjugate pairs of eigenvalues will appear consecutively with the eigenvalue having the positive imaginary part first. |
| vs | UTL_NLA_ARRAY_DBL | IN OUT | UTL_NLA_ARRAY_FLT/DBL , DIMENSION (n) . If jobvs = 'V' , vs contains the orthogonal matrix Z of Schur vectors. If jobvs = 'N' , vs is not referenced. |
| ldvs | POSITIVEN | IN | The leading dimension of the array vs . VS. ldvs >= 1 . If jobvs = 'V' , ldvs >= N |
| info | INTEGER | OUT | = 0 : successful exit < 0 : if info = -i , the i -th argument had an illegal value > 0 : if info = i , and i is <= N : the QR algorithm failed to compute all the eigenvalues. Elements 1:ILO-1 and i+1:N of wr and wi contain those eigenvalues which have converged. If jobvs = 'V' , vs contains the matrix which reduces A to its partially converged Schur form. |
| pack | flag | IN | (Optional) Flags the packing of the matrices: 'C' : column-major (default) 'R' : row-major |

## Usage Notes

This gives the Schur factorization A = Z*T*(Z**T) . A matrix is in real Schur form if it is upper quasi-triangular with 1 by 1 and 2 by 2 blocks. 2 by 2 blocks will be standardized in the form [ a b ] [ c a ] where b*c < 0 . The eigenvalues of such a block are a +- sqrt(bc) . See Also: LAPACK Driver Routines (LLS and Eigenvalue Problems) Subprograms for other subprograms in this group See Also: LAPACK Driver Routines (LLS and Eigenvalue Problems) Subprograms for other subprograms in this group Syntax UTL_NLA.LAPACK_GEES ( jobvs IN flag, n IN POSITIVEN, a IN OUT UTL_NLA_ARRAY_DBL, lda IN POSITIVEN, wr IN OUT UTL_NLA_ARRAY_DBL, wi IN OUT UTL_NLA_ARRAY_DBL, vs IN OUT UTL_NLA_ARRAY_DBL, ldvs IN POSITIVEN, info OUT INTEGER, pack IN flag DEFAULT 'C'); UTL_NLA.LAPACK_GEES ( jobvs IN flag, n IN POSITIVEN, a IN OUT UTL_NLA_ARRAY_FLT, lda IN POSITIVEN, wr IN OUT UTL_NLA_ARRAY_FLT, wi IN OUT UTL_NLA_ARRAY_FLT, vs IN OUT UTL_NLA_ARRAY_FLT, ldvs IN POSITIVEN, info OUT integer, pack IN flag DEFAULT 'C'); Parameters Table 271-40 LAPACK_GEES Procedure Parameters Parameter Description jobz 'N' : Schur vectors are not computed. 'V' : Schur vectors are computed. n The order of the matrix a. N >= 0 . a UTL_NLA_ARRAY_FLT/DBL , DIMENSION (lda, n) . On entry, the n by n matrix A . On exit, A has been overwritten by its real Schur form T . lda The leading dimension of the array a. lda >= max(1,n) . wr UTL_NLA_ARRAY_FLT/DBL , DIMENSION (n) . wr and wi contain the real and imaginary parts respectively of the computed eigenvalues in the same order that they appear on the diagonal of the output Schur form T . Complex conjugate pairs of eigenvalues will appear consecutively with the eigenvalue having the positive imaginary part first. wi UTL_NLA_ARRAY_FLT/DBL , DIMENSION (ldz, n) . wr and wi contain the real and imaginary parts respectively of the computed eigenvalues in the same order that they appear on the diagonal of the output Schur form T . Complex conjugate pairs of eigenvalues will appear consecutively with the eigenvalue having the positive imaginary part first. vs UTL_NLA_ARRAY_FLT/DBL , DIMENSION (n) . If jobvs = 'V' , vs contains the orthogonal matrix Z of Schur vectors. If jobvs = 'N' , vs is not referenced. ldvs The leading dimension of the array vs . VS. ldvs >= 1 . If jobvs = 'V' , ldvs >= N info = 0 : successful exit < 0 : if info = -i , the i -th argument had an illegal value > 0 : if info = i , and i is <= N : the QR algorithm failed to compute all the eigenvalues. Elements 1:ILO-1 and i+1:N of wr and wi contain those eigenvalues which have converged. If jobvs = 'V' , vs contains the matrix which reduces A to its partially converged Schur form. pack (Optional) Flags the packing of the matrices: 'C' : column-major (default) 'R' : row-major