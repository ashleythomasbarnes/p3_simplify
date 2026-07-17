# IMAGE header keyword report

**Product format:** IMAGE (single) MEF format

**Archive example:** [ESO header page](https://archive.eso.org/hdr?DpId=ADP.2026-07-16T08:33:58.442)

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
- [ ] **FILTER or FILTERi (for example: FILTER1, FILTER2, FILTER3, etc.)**
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
- [ ] **STREHL**
- [ ] **CHECKSUM**
- [ ] **DATASUM**
- [ ] **NDIT**
- [ ] **NJITTER**
- [ ] **NOFFSETS**
- [ ] **NUSTEP**
- [ ] **NOESODAT**

### Extension HDU

- [ ] **BUNIT**
- [ ] **CRVALi (for example: CRVAL1, CRVAL2, CRVAL3, etc.)**
- [ ] **CRPIXi (for example: CRPIX1, CRPIX2, CRPIX3, etc.)**
- [ ] **CTYPEi (for example: CTYPE1, CTYPE2, CTYPE3, etc.)**
- [ ] **CUNITi (for example: CUNIT1, CUNIT2, CUNIT3, etc.)**
- [ ] **CDi_j**
- [ ] **PHOTZP**
- [ ] **PHOTSYS**
- [ ] **HDUCLASS**
- [ ] **HDUCLASi (for example: HDUCLAS1, HDUCLAS2, HDUCLAS3, etc.)**
- [ ] **HDUDOC**
- [ ] **HDUVERS**
- [ ] **SCIDATA**
- [ ] **ERRDATA**
- [ ] **QUALDATA**
- [ ] **CONFDATA**
- [ ] **BKGDATA**
- [ ] **BKGERR**
- [ ] **BKGCONF**
- [ ] **ABMAGLIM**
- [ ] **ABMAGSAT**
- [ ] **PSF_FWHM**
- [ ] **ELLIPTIC**
- [ ] **CHECKSUM**
- [ ] **DATASUM**
- [ ] **EXTNAME**

## All keyword requirements

### Primary HDU

| Keyword | Requirement | Meaning |
| --- | --- | --- |
| **PRODCATG** | `MM` | Keyword mandatory |
| **ASSOCi (for example: ASSOC1, ASSOC2, ASSOC3, etc.)** | `MA31` | Keyword mandatory where applicable [footnote 31] |
| **ASSONi (for example: ASSON1, ASSON2, ASSON3, etc.)** | `MA32` | Keyword mandatory where applicable [footnote 32] |
| **ASSOMi (for example: ASSOM1, ASSOM2, ASSOM3, etc.)** | `MA31` | Keyword mandatory where applicable [footnote 31] |
| **ORIGIN** | `MM` | Keyword mandatory |
| **TELESCOP or TELESCi (for example: TELESC1, TELESC2, TELESC3, etc.)** | `MM` | Keyword mandatory |
| **INSTRUME or INSTRi (for example: INSTR1, INSTR2, INSTR3, etc.)** | `MM` | Keyword mandatory |
| **FILTER or FILTERi (for example: FILTER1, FILTER2, FILTER3, etc.)** | `MM` | Keyword mandatory |
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
| GAIN | `OP` | It makes sense to provide the value, but it is optional |
| DETRON | `OP` | It makes sense to provide the value, but it is optional |
| EFFRON | `OP` | It makes sense to provide the value, but it is optional |
| WEIGHT | `OP` | It makes sense to provide the value, but it is optional |
| RA_ERR | `NO` | Keyword not allowed: the Phase 3 system will reject the file |
| DEC_ERR | `NO` | Keyword not allowed: the Phase 3 system will reject the file |
| STOKES | `SU` | Contact Phase 3 support to determine whether the keyword is required |
| **STREHL** | `MA51` | Keyword mandatory where applicable [footnote 51] |
| ARCFILE | `RE` | Keyword recommended; it means applicable unless you have a good reason to not use it |
| **CHECKSUM** | `MM` | Keyword mandatory |
| **DATASUM** | `MM` | Keyword mandatory |
| ORIGFILE | `RE` | Keyword recommended; it means applicable unless you have a good reason to not use it |
| P3ORIG | `RE` | Keyword recommended; it means applicable unless you have a good reason to not use it |
| **NDIT** | `MA52` | Keyword mandatory where applicable [footnote 52] |
| **NJITTER** | `MA52` | Keyword mandatory where applicable [footnote 52] |
| **NOFFSETS** | `MA52` | Keyword mandatory where applicable [footnote 52] |
| **NUSTEP** | `MA52` | Keyword mandatory where applicable [footnote 52] |
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
| **PHOTZP** | `MM` | Keyword mandatory |
| PHOTZPER | `RC` | Keyword recommended |
| **PHOTSYS** | `MM` | Keyword mandatory |
| **HDUCLASS** | `MM` | Keyword mandatory |
| **HDUCLASi (for example: HDUCLAS1, HDUCLAS2, HDUCLAS3, etc.)** | `MM` | Keyword mandatory |
| **HDUDOC** | `MM` | Keyword mandatory |
| **HDUVERS** | `MM` | Keyword mandatory |
| **SCIDATA** | `MA46` | Keyword mandatory where applicable [footnote 46] |
| **ERRDATA** | `MA46` | Keyword mandatory where applicable [footnote 46] |
| **QUALDATA** | `MA46` | Keyword mandatory where applicable [footnote 46] |
| **CONFDATA** | `MA46` | Keyword mandatory where applicable [footnote 46] |
| **BKGDATA** | `MA46` | Keyword mandatory where applicable [footnote 46] |
| **BKGERR** | `MA46` | Keyword mandatory where applicable [footnote 46] |
| **BKGCONF** | `MA46` | Keyword mandatory where applicable [footnote 46] |
| **ABMAGLIM** | `MM` | Keyword mandatory |
| **ABMAGSAT** | `MM` | Keyword mandatory |
| **PSF_FWHM** | `MM` | Keyword mandatory |
| **ELLIPTIC** | `M49` | Keyword mandatory [footnote 49] |
| ARCFILE | `RE` | Keyword recommended; it means applicable unless you have a good reason to not use it |
| **CHECKSUM** | `MM` | Keyword mandatory |
| **DATASUM** | `MM` | Keyword mandatory |
| ORIGFILE | `RE` | Keyword recommended; it means applicable unless you have a good reason to not use it |
| P3ORIG | `RE` | Keyword recommended; it means applicable unless you have a good reason to not use it |
| **EXTNAME** | `MA65` | Keyword mandatory where applicable [footnote 65] |

## Referenced footnotes

31. Mandatory for the cases where ancillary files are provided in a non-FITS format.
32. Mandatory for the cases where ancillary files are provided in association with the scientific data.
37. If RADESYS='FK5', EQUINOX=2000.0 is mandatory. If RADESYS = 'ICRS', EQUINOX is tolerated and its value needs to be 2000.0.
38. Must be present if the system used is other than UTC.
40. If a refereed publication is not available at the time of the data release going public, the value can be left to an empty string.
46. SCIDATA is mandatory for the cases where ancillary extensions are provided in association with the scientific data. ERRDATA / QUALDATA / CONFDATA / BKGDATA / BKGERR / BKGCONF shall be used if the corresponding extension is provided.
49. For VIRCAM and OmegaCAM only.
51. For AO observations only.
52. NIR image data products qualify for the keyword if, and only if, all exposures and observations contributing to the given product share the same value for the respective parameter. If, for example, the product has been created from exposures taken with different detector integration time, the keyword DIT should not be defined in the FITS header.
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
  DATE                 = '2026-07-16T04:54:22'
* EXPTIME              = 150.0
* MJD-END              = 60779.3563837119
* RA                   = 236.193920575548
* DEC                  = -38.1939151869329
* RADESYS              = 'FK5'
* ORIGIN               = 'ESO-PARANAL'
* TELESCOP             = 'ESO-VLT-U4'
* INSTRUME             = 'ERIS'
* OBJECT               = '2MASS J15444712-3811406'
* EQUINOX              = 2000.0
  DATE-OBS             = '2025-04-14T08:28:22.9769'
  UTC                  = 30502.0
  LST                  = 62269.694
  PI-COI               = 'UNKNOWN'
  OBSERVER             = 'UNKNOWN'
* TIMESYS              = 'UTC'
* MJD-OBS              = 60779.35304371
* PRODCATG             = 'SCIENCE.IMAGE'
* NCOMBINE             = 6
* TEXPTIME             = 150.0
* OBID1                = 4145961
* FLUXCAL              = 'ABSOLUTE'
  ZPMETHOD             = 'DEFAULT'
  ARCFILE              = 'ADP.2026-07-16T08:33:58.442.fits'
  DATAMD5              = '8d39e44f4552ffd5c3f847985e4aca07'
  PIPEFILE             = 'stack.ERIS.2026-07-16T04:43:49.495.fits'
* PROV1                = 'ERIS.2025-04-14T08:28:22.977.fits'
* PROV2                = 'ERIS.2025-04-14T08:29:14.932.fits'
* PROV3                = 'ERIS.2025-04-14T08:30:09.652.fits'
* PROV4                = 'ERIS.2025-04-14T08:30:59.838.fits'
* PROV5                = 'ERIS.2025-04-14T08:31:50.967.fits'
* PROV6                = 'ERIS.2025-04-14T08:32:46.553.fits'
* FILTER               = 'Ks'
* PROG_ID              = '115.28A3.001'
* PROCSOFT             = 'eris/2.0.6'
* REFERENC             = ''
* OBSTECH              = 'IMAGE'
* CHECKSUM             = 'HLRNKLQNHLQNHLQN'
* DATASUM              = '0'
  OB_GRADE             = 'A'
  OB_COMM1             = 'none'
  QC_COMM1             = 'none'
  VM_SM                = 'SM'
* ASSON1               = 'ERIS_CAL_PHOT_OBJECT_JITTER_2025-04-14T08:28:22.9769_3.fits'
* ASSON2               = 'ERIS_CAL_PHOT_OBJECT_JITTER_2025-04-14T08:28:22.9769_20.fits'
* ASSON3               = 'ERIS_CAL_PHOT_OBJECT_JITTER_2025-04-14T08:28:22.9769_13.fits'
* ASSON4               = 'ERIS_CAL_PHOT_OBJECT_JITTER_2025-04-14T08:28:22.9769_10.fits'
* ASSON5               = 'ERIS_CAL_PHOT_OBJECT_JITTER_2025-04-14T08:28:22.9769_16.fits'
* ASSON6               = 'ERIS_CAL_PHOT_OBJECT_JITTER_2025-04-14T08:28:22.9769_6.fits'
* ASSON7               = 'ERIS_IMG_OBS_COMBINED_2025-04-14T08:28:22.9769.png'
* ASSOC7               = 'ANCILLARY.PREVIEW'
* ASSOM7               = '320d9c3575f1bd549db71da0d20f1765'
  ORIGFILE             = 'ERIS_IMG_OBS_COMBINED_2025-04-14T08:28:22.9769.fits'
  P3ORIG               = 'IDP'
```

### HDU 1 — DATA

```text
  XTENSION             = 'IMAGE'
  BITPIX               = -64
  NAXIS                = 2
  NAXIS1               = 2157
  NAXIS2               = 1084
  PCOUNT               = 0
  GCOUNT               = 1
* CRVAL1               = 236.193918256614
* CRVAL2               = -38.1939133644305
* CRPIX1               = 1079.0
* CRPIX2               = 542.5
* CTYPE1               = 'RA---TAN'
* CTYPE2               = 'DEC--TAN'
* CUNIT1               = 'deg'
* CUNIT2               = 'deg'
  CD1_1                = -3.64500494346319e-06
  CD1_2                = 0.0
  CD2_1                = 0.0
  CD2_2                = 3.64500494346319e-06
* HDUCLASS             = 'ESO'
* HDUDOC               = 'SDP'
* HDUVERS              = 'SDP version 8'
* ERRDATA              = 'ERR'
* QUALDATA             = 'DQ'
* CONFDATA             = 'CONFIDENCE'
* EXTNAME              = 'DATA'
* HDUCLAS1             = 'IMAGE'
* HDUCLAS2             = 'DATA'
* BUNIT                = 'adu/s'
  FLUXCAL              = 'ABSOLUTE'
* PHOTSYS              = 'VEGA'
* ABMAGLIM             = 6.09739012816341
* ABMAGSAT             = 4.17956561342553
* PSF_FWHM             = 0.696753335368015
* PHOTZP               = 24.621405602898
  PHOTZPER             = 0.12
  ZPMETHOD             = 'DEFAULT'
* CHECKSUM             = 'DR4nGQ3mDQ3mDQ3m'
* DATASUM              = '1143308628'
```

### HDU 2 — ERR

```text
  XTENSION             = 'IMAGE'
  BITPIX               = -64
  NAXIS                = 2
  NAXIS1               = 2157
  NAXIS2               = 1084
  PCOUNT               = 0
  GCOUNT               = 1
* CRVAL1               = 236.193918256614
* CRVAL2               = -38.1939133644305
* CRPIX1               = 1079.0
* CRPIX2               = 542.5
* CTYPE1               = 'RA---TAN'
* CTYPE2               = 'DEC--TAN'
* CUNIT1               = 'deg'
* CUNIT2               = 'deg'
  CD1_1                = -3.64500494346319e-06
  CD1_2                = 0.0
  CD2_1                = 0.0
  CD2_2                = 3.64500494346319e-06
* HDUCLASS             = 'ESO'
* HDUDOC               = 'SDP'
* HDUVERS              = 'SDP version 8'
* SCIDATA              = 'DATA'
* QUALDATA             = 'DQ'
* CONFDATA             = 'CONFIDENCE'
* EXTNAME              = 'ERR'
* HDUCLAS1             = 'IMAGE'
* HDUCLAS2             = 'ERROR'
* HDUCLAS3             = 'RMSE'
* BUNIT                = 'adu/s'
* CHECKSUM             = 'OZcTPWcROWcROWcR'
* DATASUM              = '1245796131'
```

### HDU 3 — DQ

```text
  XTENSION             = 'IMAGE'
  BITPIX               = 8
  NAXIS                = 2
  NAXIS1               = 2157
  NAXIS2               = 1084
  PCOUNT               = 0
  GCOUNT               = 1
* CRVAL1               = 236.193918256614
* CRVAL2               = -38.1939133644305
* CRPIX1               = 1079.0
* CRPIX2               = 542.5
* CTYPE1               = 'RA---TAN'
* CTYPE2               = 'DEC--TAN'
* CUNIT1               = 'deg'
* CUNIT2               = 'deg'
  CD1_1                = -3.64500494346319e-06
  CD1_2                = 0.0
  CD2_1                = 0.0
  CD2_2                = 3.64500494346319e-06
* HDUCLASS             = 'ESO'
* HDUDOC               = 'SDP'
* HDUVERS              = 'SDP version 8'
* SCIDATA              = 'DATA'
* ERRDATA              = 'ERR'
* CONFDATA             = 'CONFIDENCE'
* EXTNAME              = 'DQ'
* HDUCLAS1             = 'IMAGE'
* HDUCLAS2             = 'QUALITY'
* HDUCLAS3             = 'MASKZERO'
* CHECKSUM             = '9EhZACgY9CgYACgY'
* DATASUM              = '606081566'
```

### HDU 4 — CONFIDENCE

```text
  XTENSION             = 'IMAGE'
  BITPIX               = -64
  NAXIS                = 2
  NAXIS1               = 2157
  NAXIS2               = 1084
  PCOUNT               = 0
  GCOUNT               = 1
* CRVAL1               = 236.193918256614
* CRVAL2               = -38.1939133644305
* CRPIX1               = 1079.0
* CRPIX2               = 542.5
* CTYPE1               = 'RA---TAN'
* CTYPE2               = 'DEC--TAN'
* CUNIT1               = 'deg'
* CUNIT2               = 'deg'
  CD1_1                = -3.64500494346319e-06
  CD1_2                = 0.0
  CD2_1                = 0.0
  CD2_2                = 3.64500494346319e-06
* HDUCLASS             = 'ESO'
* HDUDOC               = 'SDP'
* HDUVERS              = 'SDP version 8'
* SCIDATA              = 'DATA'
* ERRDATA              = 'ERR'
* QUALDATA             = 'DQ'
* EXTNAME              = 'CONFIDENCE'
* HDUCLAS1             = 'IMAGE'
* HDUCLAS2             = 'CONF'
* CHECKSUM             = 'WMWaaMUVWMUZaMUZ'
* DATASUM              = '18403978'
```
