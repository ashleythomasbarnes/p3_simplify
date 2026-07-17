# CUBE.IFS header keyword report

**Archive example:** [ESO header page](https://archive.eso.org/hdr?DpId=ADP.2026-01-19T14:23:01.707)

Mandatory checklists include keywords that are always mandatory, mandatory for ESO files, or mandatory when applicable. The placeholder `i` denotes a numbered series.

## Mandatory keyword checklists

### Primary HDU

- [ ] **PRODCATG**
- [ ] **ASSOCi (for example: ASSOC1, ASSOC2, ASSOC3, etc.)**
- [ ] **ASSONi (for example: ASSON1, ASSON2, ASSON3, etc.)**
- [ ] **ASSOMi (for example: ASSOM1, ASSOM2, ASSOM3, etc.)**
- [ ] **ORIGIN**
- [ ] **TELESCOP or TELESCi (for example: TELESC1, TELESC2, TELESC3, etc.)**
- [ ] **INSTRUME or INSTRi (for example: INSTR1, INSTR2, INSTR3, etc.)**
- [ ] **OBJECT**
- [ ] **RA and DEC**
- [ ] **EQUINOX**
- [ ] **RADESYS**
- [ ] **TIMESYS**
- [ ] **EXPTIME**
- [ ] **TEXPTIME**
- [ ] **MJD-OBS**
- [ ] **MJD-END**
- [ ] **PROG_ID or PROGIDi (for example: PROGID1, PROGID2, PROGID3, etc.)**
- [ ] **OBIDi (for example: OBID1, OBID2, OBID3, etc.)**
- [ ] **NCOMBINE**
- [ ] **OBSTECH**
- [ ] **FLUXCAL**
- [ ] **PROCSOFT**
- [ ] **REFERENC**
- [ ] **PROVi (for example: PROV1, PROV2, PROV3, etc.) or PROVXTN**
- [ ] **SPECSYS**
- [ ] **WAVELMIN**
- [ ] **WAVELMAX**
- [ ] **ABMAGLIM**
- [ ] **PIXNOISE**
- [ ] **SPEC_RES**
- [ ] **SKY_RES**
- [ ] **SKY_RERR**
- [ ] **STREHL**
- [ ] **CHECKSUM**
- [ ] **DATASUM**
- [ ] **NOESODAT**

### Extension HDU

- [ ] **BUNIT**
- [ ] **CRVALi (for example: CRVAL1, CRVAL2, CRVAL3, etc.)**
- [ ] **CRPIXi (for example: CRPIX1, CRPIX2, CRPIX3, etc.)**
- [ ] **CTYPEi (for example: CTYPE1, CTYPE2, CTYPE3, etc.)**
- [ ] **CUNITi (for example: CUNIT1, CUNIT2, CUNIT3, etc.)**
- [ ] **CDi_j**
- [ ] **HDUCLASS**
- [ ] **HDUCLASi (for example: HDUCLAS1, HDUCLAS2, HDUCLAS3, etc.)**
- [ ] **HDUDOC**
- [ ] **HDUVERS**
- [ ] **SCIDATA**
- [ ] **ERRDATA**
- [ ] **QUALDATA**
- [ ] **CHECKSUM**
- [ ] **DATASUM**
- [ ] **EXTNAME**

## All keyword requirements

### Primary HDU

| Keyword | Requirement | Meaning |
| --- | --- | --- |
| **PRODCATG** | `MM` | Keyword mandatory |
| **ASSOCi (for example: ASSOC1, ASSOC2, ASSOC3, etc.)** | `MA31` | Keyword mandatory where applicable [footnote 31] |
| **ASSONi (for example: ASSON1, ASSON2, ASSON3, etc.)** | `M34` | Keyword mandatory [footnote 34] |
| **ASSOMi (for example: ASSOM1, ASSOM2, ASSOM3, etc.)** | `MA31` | Keyword mandatory where applicable [footnote 31] |
| **ORIGIN** | `MM` | Keyword mandatory |
| **TELESCOP or TELESCi (for example: TELESC1, TELESC2, TELESC3, etc.)** | `MM` | Keyword mandatory |
| **INSTRUME or INSTRi (for example: INSTR1, INSTR2, INSTR3, etc.)** | `MM` | Keyword mandatory |
| **OBJECT** | `MM` | Keyword mandatory |
| **RA and DEC** | `MM` | Keyword mandatory |
| **EQUINOX** | `MA37` | Keyword mandatory where applicable [footnote 37] |
| **RADESYS** | `MM` | Keyword mandatory |
| **TIMESYS** | `MA38` | Keyword mandatory where applicable [footnote 38] |
| **EXPTIME** | `MM` | Keyword mandatory |
| **TEXPTIME** | `MM` | Keyword mandatory |
| **MJD-OBS** | `MM` | Keyword mandatory |
| **MJD-END** | `MM` | Keyword mandatory |
| **PROG_ID or PROGIDi (for example: PROGID1, PROGID2, PROGID3, etc.)** | `ME` | Keyword mandatory for ESO files |
| **OBIDi (for example: OBID1, OBID2, OBID3, etc.)** | `ME` | Keyword mandatory for ESO files |
| **NCOMBINE** | `ME` | Keyword mandatory for ESO files |
| **OBSTECH** | `MM` | Keyword mandatory |
| **FLUXCAL** | `MM` | Keyword mandatory |
| **PROCSOFT** | `MM` | Keyword mandatory |
| **REFERENC** | `M40` | Keyword mandatory [footnote 40] |
| **PROVi (for example: PROV1, PROV2, PROV3, etc.) or PROVXTN** | `ME` | Keyword mandatory for ESO files |
| **SPECSYS** | `MM` | Keyword mandatory |
| **WAVELMIN** | `MM` | Keyword mandatory |
| **WAVELMAX** | `MM` | Keyword mandatory |
| SPEC_BIN | `NO` | Keyword not allowed: the Phase 3 system will reject the file |
| RA_ERR | `NO` | Keyword not allowed: the Phase 3 system will reject the file |
| DEC_ERR | `NO` | Keyword not allowed: the Phase 3 system will reject the file |
| STOKES | `SU` | Contact Phase 3 support to determine whether the keyword is required |
| **ABMAGLIM** | `MM` | Keyword mandatory |
| **PIXNOISE** | `MM` | Keyword mandatory |
| ELLIPTIC | `OP` | It makes sense to provide the value, but it is optional |
| **SPEC_RES** | `MM` | Keyword mandatory |
| **SKY_RES** | `MM` | Keyword mandatory |
| **SKY_RERR** | `MA50` | Keyword mandatory where applicable [footnote 50] |
| **STREHL** | `MA51` | Keyword mandatory where applicable [footnote 51] |
| ARCFILE | `RE` | Keyword recommended; it means applicable unless you have a good reason to not use it |
| **CHECKSUM** | `MM` | Keyword mandatory |
| **DATASUM** | `MM` | Keyword mandatory |
| ORIGFILE | `RE` | Keyword recommended; it means applicable unless you have a good reason to not use it |
| P3ORIG | `RE` | Keyword recommended; it means applicable unless you have a good reason to not use it |
| **NOESODAT** | `MA59` | Keyword mandatory where applicable [footnote 59] |

### Extension HDU

| Keyword | Requirement | Meaning |
| --- | --- | --- |
| **BUNIT** | `MM` | Keyword mandatory |
| **CRVALi (for example: CRVAL1, CRVAL2, CRVAL3, etc.)** | `MM` | Keyword mandatory |
| **CRPIXi (for example: CRPIX1, CRPIX2, CRPIX3, etc.)** | `MM` | Keyword mandatory |
| **CTYPEi (for example: CTYPE1, CTYPE2, CTYPE3, etc.)** | `MM` | Keyword mandatory |
| **CUNITi (for example: CUNIT1, CUNIT2, CUNIT3, etc.)** | `MM` | Keyword mandatory |
| **CDi_j** | `MM` | Keyword mandatory |
| CSYERi (for example: CSYER1, CSYER2, CSYER3, etc.) | `RC` | Keyword recommended |
| CRDERi (for example: CRDER1, CRDER2, CRDER3, etc.) | `RC` | Keyword recommended |
| **HDUCLASS** | `MM` | Keyword mandatory |
| **HDUCLASi (for example: HDUCLAS1, HDUCLAS2, HDUCLAS3, etc.)** | `MM` | Keyword mandatory |
| **HDUDOC** | `MM` | Keyword mandatory |
| **HDUVERS** | `MM` | Keyword mandatory |
| **SCIDATA** | `MA46` | Keyword mandatory where applicable [footnote 46] |
| **ERRDATA** | `MA46` | Keyword mandatory where applicable [footnote 46] |
| **QUALDATA** | `MA46` | Keyword mandatory where applicable [footnote 46] |
| ARCFILE | `RE` | Keyword recommended; it means applicable unless you have a good reason to not use it |
| **CHECKSUM** | `MM` | Keyword mandatory |
| **DATASUM** | `MM` | Keyword mandatory |
| ORIGFILE | `RE` | Keyword recommended; it means applicable unless you have a good reason to not use it |
| P3ORIG | `RE` | Keyword recommended; it means applicable unless you have a good reason to not use it |
| **EXTNAME** | `MA65` | Keyword mandatory where applicable [footnote 65] |

## Referenced footnotes

31. Mandatory for the cases where ancillary files are provided in a non-FITS format.
34. The IFS 3D cube must always be associated with the white-light image. The white-light image must be delivered using the ASSONi/ASSOCi mechanism.
37. If RADESYS='FK5', EQUINOX=2000.0 is mandatory. If RADESYS = 'ICRS', EQUINOX is tolerated and its value needs to be 2000.0.
38. Must be present if the system used is other than UTC.
40. If a refereed publication is not available at the time of the data release going public, the value can be left to an empty string.
46. SCIDATA is mandatory for the cases where ancillary extensions are provided in association with the scientific data. ERRDATA / QUALDATA / CONFDATA / BKGDATA / BKGERR / BKGCONF shall be used if the corresponding extension is provided.
50. Applicable to the case when SKY_RES is expected to vary within the data collection due to the way it is estimated (see footnote 18).
51. For AO observations only.
59. Applicable to products originating or containing data from a non-ESO facility.
65. A specific value is requested in particular cases: 'PHASE3PROVENANCE', 'PHASE3CATALOG', 'PHASE3FILELIST'.

## Example archive FITS headers

Lines prefixed with `*` are mandatory, mandatory for ESO files, or mandatory when applicable.

### HDU 0 — PRIMARY

```text
  SIMPLE               = True
  BITPIX               = 8
  NAXIS                = 0
  EXTEND               = True
  DATE                 = '2026-01-19T14:08:09'
* ORIGIN               = 'ESO-PARANAL'
* TELESCOP             = 'ESO-VLT-U4'
* INSTRUME             = 'MUSE'
* RA                   = 150.087392789367
* DEC                  = 2.36380542319734
* EQUINOX              = 2000.0
* EXPTIME              = 2280.44820661048
* MJD-OBS              = 61053.25379774
* MJD-END              = 61053.2880801367
  DATE-OBS             = '2026-01-13T06:05:28.125'
  UTC                  = 21916.0
  LST                  = 32076.766
  PI-COI               = 'UNKNOWN'
  OBSERVER             = 'UNKNOWN'
* RADESYS              = 'FK5'
* OBJECT               = 'MUSE-JELS - Pointing 49'
* TEXPTIME             = 2700.0
* NCOMBINE             = 3
  PIPEFILE             = 'r.MUSE.2026-01-13T06:05:28.125_tpl_0000.fits'
  BARYCORR             = 18.3806829907906
* SPECSYS              = 'BARYCENT'
  ARCFILE              = 'ADP.2026-01-19T14:23:01.707.fits'
  DATAMD5              = 'Not computed'
* OBID1                = 3693695
* PROG_ID              = '112.25WM.001'
* PROV1                = 'MUSE.2026-01-13T06:05:28.125.fits'
* PROV2                = 'MUSE.2026-01-13T06:22:39.122.fits'
* PROV3                = 'MUSE.2026-01-13T06:39:50.124.fits'
* ASSON1               = 'MU_SIMC_3693695_2026-01-13T06:05:28.125_WFM-AO-N_OBJ.fits'
* PRODCATG             = 'SCIENCE.CUBE.IFS'
* PROCSOFT             = 'muse/2.8.8'
* OBSTECH              = 'IFU'
* FLUXCAL              = 'ABSOLUTE'
* WAVELMIN             = 470.02880859375
* WAVELMAX             = 935.02880859375
* SPEC_RES             = 3014.2738697403
* SKY_RES              = 0.626493246167335
* SKY_RERR             = 0.337675880098061
* PIXNOISE             = 2.85306852353742e-20
* ABMAGLIM             = 24.3549673179574
* REFERENC             = ''
* ASSON2               = 'r.MUSE.2026-01-13T06:05:28.125_tpl.log'
* ASSOC2               = 'ANCILLARY.README'
* ASSOM2               = '456bad77afcf252d32a4efb08e65d0d0'
* ASSON3               = 'r.MUSE.2026-01-13T06:05:28.125_tpl.png'
* ASSOC3               = 'ANCILLARY.PREVIEW'
* ASSOM3               = '429f987a954f81f57598f2ef1f9c46cb'
* ASSON4               = 'r.MUSE.2026-01-13T06:05:28.125_pst.png'
* ASSOC4               = 'ANCILLARY.PREVIEW'
* ASSOM4               = 'f2a1afb5e2b1acda41c8a3b388a46e5a'
* ASSON5               = 'r.MUSE.2026-01-13T06:22:39.122_pst.png'
* ASSOC5               = 'ANCILLARY.PREVIEW'
* ASSOM5               = '03cbf2f0a5a3f2636d3d762aef050f8a'
* ASSON6               = 'r.MUSE.2026-01-13T06:39:50.124_pst.png'
* ASSOC6               = 'ANCILLARY.PREVIEW'
* ASSOM6               = '6df5df2d94899cf9365877937a80bbbb'
  ORIGFILE             = 'MU_SCBC_3693695_2026-01-13T06:05:28.125_WFM-AO-N_OBJ.fits'
  VM_SM                = 'SM'
  OB_GRADE             = 'A'
  QCFLAG               = 100000010
  QC_COMM1             = 'ROTATE3_custom'
  DCARC1               = 'S.MUSE.2026-01-19T13:57:53.210'
  DCORG1               = 'r.MUSE.2026-01-13T06:05:28.125_pst_0000.fits'
  DCARC2               = 'S.MUSE.2026-01-19T13:58:30.450'
  DCORG2               = 'r.MUSE.2026-01-13T06:22:39.122_pst_0000.fits'
  DCARC3               = 'S.MUSE.2026-01-19T13:59:07.843'
  DCORG3               = 'r.MUSE.2026-01-13T06:39:50.124_pst_0000.fits'
* CHECKSUM             = 'NdRqPcPoNcPoNcPo'
* DATASUM              = '         0'
  P3ORIG               = 'IDP'
```

### HDU 1 — DATA

```text
  XTENSION             = 'IMAGE'
  BITPIX               = -32
  NAXIS                = 3
  NAXIS1               = 403
  NAXIS2               = 402
  NAXIS3               = 3721
  PCOUNT               = 0
  GCOUNT               = 1
  OBJECT               = 'MUSE-JELS - Pointing 49 (DATA)'
* CRPIX1               = 214.643015481175
* CRPIX2               = 191.72237899083
  CD1_1                = -5.55555555555556e-05
  CD1_2                = 0.0
  CD2_1                = 0.0
  CD2_2                = 5.55555555555556e-05
* CUNIT1               = 'deg'
* CUNIT2               = 'deg'
* CTYPE1               = 'RA---TAN'
* CTYPE2               = 'DEC--TAN'
  CSYER1               = 1.69760864415e-05
  CSYER2               = 6.54379526381e-06
* CRVAL1               = 150.086662
* CRVAL2               = 2.36329
* CTYPE3               = 'AWAV'
* CUNIT3               = 'angstrom'
  CD3_3                = 1.25
* CRPIX3               = 1.0
* CRVAL3               = 4700.2880859375
  CRDER3               = 0.026
  CD1_3                = 0.0
  CD2_3                = 0.0
  CD3_1                = 0.0
  CD3_2                = 0.0
* EXTNAME              = 'DATA'
* HDUCLASS             = 'ESO'
* HDUDOC               = 'SDP'
* HDUVERS              = 'SDP version 8'
* HDUCLAS1             = 'IMAGE'
* HDUCLAS2             = 'DATA'
* ERRDATA              = 'STAT'
* BUNIT                = '10**(-20)erg.s**(-1).cm**(-2).angstrom**(-1)'
  TITLE                = 'MUSE-JELS_3693695_2026-01-13T06:05:28.125_WFM-AO-N_OBJ'
* CHECKSUM             = '1hFE4fE91fEE1fE9'
* DATASUM              = '3415931082'
```

### HDU 2 — STAT

```text
  XTENSION             = 'IMAGE'
  BITPIX               = -32
  NAXIS                = 3
  NAXIS1               = 403
  NAXIS2               = 402
  NAXIS3               = 3721
  PCOUNT               = 0
  GCOUNT               = 1
  OBJECT               = 'MUSE-JELS - Pointing 49 (STAT)'
* CRPIX1               = 214.643015481175
* CRPIX2               = 191.72237899083
  CD1_1                = -5.55555555555556e-05
  CD1_2                = 0.0
  CD2_1                = 0.0
  CD2_2                = 5.55555555555556e-05
* CUNIT1               = 'deg'
* CUNIT2               = 'deg'
* CTYPE1               = 'RA---TAN'
* CTYPE2               = 'DEC--TAN'
  CSYER1               = 1.69760864415e-05
  CSYER2               = 6.54379526381e-06
* CRVAL1               = 150.086662
* CRVAL2               = 2.36329
* CTYPE3               = 'AWAV'
* CUNIT3               = 'angstrom'
  CD3_3                = 1.25
* CRPIX3               = 1.0
* CRVAL3               = 4700.2880859375
  CRDER3               = 0.026
  CD1_3                = 0.0
  CD2_3                = 0.0
  CD3_1                = 0.0
  CD3_2                = 0.0
* EXTNAME              = 'STAT'
* HDUCLASS             = 'ESO'
* HDUDOC               = 'SDP'
* HDUVERS              = 'SDP version 8'
* HDUCLAS1             = 'IMAGE'
* HDUCLAS2             = 'ERROR'
* HDUCLAS3             = 'MSE'
* SCIDATA              = 'DATA'
* BUNIT                = '10**(-40)erg**2.s**(-2).cm**(-4).angstrom**(-2)'
* CHECKSUM             = 'd8Xdg5Xcd5Xcd5Xc'
* DATASUM              = '3933271495'
```
