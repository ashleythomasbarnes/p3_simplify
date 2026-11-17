# IMAGE.FLUXMAP header keyword report

**Archive example:** [ESO header page](https://archive.eso.org/hdr?DpId=ADP.2024-07-12T08:07:39.447)

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
- [ ] **BUNIT**
- [ ] **CRVALi (for example: CRVAL1, CRVAL2, CRVAL3, etc.)**
- [ ] **CRPIXi (for example: CRPIX1, CRPIX2, CRPIX3, etc.)**
- [ ] **CTYPEi (for example: CTYPE1, CTYPE2, CTYPE3, etc.)**
- [ ] **CUNITi (for example: CUNIT1, CUNIT2, CUNIT3, etc.)**
- [ ] **CDi_j**
- [ ] **FLUXERR**
- [ ] **WAVELMIN**
- [ ] **WAVELMAX**
- [ ] **BNOISE**
- [ ] **MAPMODE**
- [ ] **FEBEi (for example: FEBE1, FEBE2, FEBE3, etc.)**
- [ ] **SKY_RES**
- [ ] **SKY_RERR**
- [ ] **CHECKSUM**
- [ ] **DATASUM**
- [ ] **NOESODAT**

### Extension HDU

- [ ] **CHECKSUM**
- [ ] **DATASUM**
- [ ] **EXTNAME**

## All keyword requirements

### Primary HDU

| Keyword | Requirement | Meaning |
| --- | --- | --- |
| **PRODCATG** | `MM` | Keyword mandatory |
| **ASSOCi (for example: ASSOC1, ASSOC2, ASSOC3, etc.)** | `MA31` | Keyword mandatory where applicable [footnote 31] |
| **ASSONi (for example: ASSON1, ASSON2, ASSON3, etc.)** | `M33` | Keyword mandatory [footnote 33] |
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
| **BUNIT** | `MM` | Keyword mandatory |
| **CRVALi (for example: CRVAL1, CRVAL2, CRVAL3, etc.)** | `MM` | Keyword mandatory |
| **CRPIXi (for example: CRPIX1, CRPIX2, CRPIX3, etc.)** | `MM` | Keyword mandatory |
| **CTYPEi (for example: CTYPE1, CTYPE2, CTYPE3, etc.)** | `MM` | Keyword mandatory |
| **CUNITi (for example: CUNIT1, CUNIT2, CUNIT3, etc.)** | `MM` | Keyword mandatory |
| **CDi_j** | `MM` | Keyword mandatory |
| CSYERi (for example: CSYER1, CSYER2, CSYER3, etc.) | `RC` | Keyword recommended |
| CRDERi (for example: CRDER1, CRDER2, CRDER3, etc.) | `RC` | Keyword recommended |
| **FLUXERR** | `MM` | Keyword mandatory |
| **WAVELMIN** | `MM` | Keyword mandatory |
| **WAVELMAX** | `MM` | Keyword mandatory |
| RA_ERR | `NO` | Keyword not allowed: the Phase 3 system will reject the file |
| DEC_ERR | `NO` | Keyword not allowed: the Phase 3 system will reject the file |
| **BNOISE** | `MM` | Keyword mandatory |
| **MAPMODE** | `MM` | Keyword mandatory |
| **FEBEi (for example: FEBE1, FEBE2, FEBE3, etc.)** | `MM` | Keyword mandatory |
| STOKES | `SU` | Contact Phase 3 support to determine whether the keyword is required |
| ABMAGLIM | `NO` | Keyword not allowed: the Phase 3 system will reject the file |
| **SKY_RES** | `MM` | Keyword mandatory |
| **SKY_RERR** | `MA50` | Keyword mandatory where applicable [footnote 50] |
| ARCFILE | `RS` | Reserved keyword. If present, modified by the Phase 3 system during the archiving process |
| **CHECKSUM** | `MM` | Keyword mandatory |
| **DATASUM** | `MM` | Keyword mandatory |
| ORIGFILE | `RS` | Reserved keyword. If present, modified by the Phase 3 system during the archiving process |
| P3ORIG | `RS` | Reserved keyword. If present, modified by the Phase 3 system during the archiving process |
| **NOESODAT** | `MA59` | Keyword mandatory where applicable [footnote 59] |

### Extension HDU

| Keyword | Requirement | Meaning |
| --- | --- | --- |
| **CHECKSUM** | `MM` | Keyword mandatory |
| **DATASUM** | `MM` | Keyword mandatory |
| **EXTNAME** | `MA65` | Keyword mandatory where applicable [footnote 65] |

## Referenced footnotes

31. Mandatory for the cases where ancillary files are provided in a non-FITS format.
33. The flux map must always be associated with the RMS noise map, or the SNR map, or both.
37. If RADESYS='FK5', EQUINOX=2000.0 is mandatory. If RADESYS = 'ICRS', EQUINOX is tolerated and its value needs to be 2000.0.
38. Must be present if the system used is other than UTC.
40. If a refereed publication is not available at the time of the data release going public, the value can be left to an empty string.
50. Applicable to the case when SKY_RES is expected to vary within the data collection due to the way it is estimated (see footnote 18).
59. Applicable to products originating or containing data from a non-ESO facility.
65. A specific value is requested in particular cases: 'PHASE3PROVENANCE', 'PHASE3CATALOG', 'PHASE3FILELIST'.

## Example archive FITS headers

Lines prefixed with `*` are mandatory, mandatory for ESO files, or mandatory when applicable.

### HDU 0 — PRIMARY

```text
  SIMPLE               = True
  BITPIX               = -32
  NAXIS                = 2
  NAXIS1               = 1418
  NAXIS2               = 1517
* PRODCATG             = 'SCIENCE.IMAGE.FLUXMAP'
* ASSON1               = 'SDC345.0_CAFFEINE_coldens_ESO.fits'
* ASSON2               = 'SDC345.0_CAFFEINE_450um_weights_ESO.fits'
* ORIGIN               = 'APEX'
* TELESCOP             = 'APEX-12m'
* INSTRUME             = 'APEXBOL'
* MAPMODE              = 'OTF'
* OBSTECH              = 'CONTINUUM'
* OBJECT               = 'SDC345.0'
* RA                   = 256.363596788052
* DEC                  = -41.44307324086139
* CRVAL1               = 256.34917
* CRPIX1               = 760.561357164
* CTYPE1               = 'RA---TAN'
* CUNIT1               = 'deg'
* CRVAL2               = -41.446944
* CRPIX2               = 741.407166861
* CTYPE2               = 'DEC--TAN'
* CUNIT2               = 'deg'
  CD1_1                = -0.000213889
  CD1_2                = -0.0
  CD2_1                = -0.0
  CD2_2                = 0.000213889
* EQUINOX              = 2000.0
* RADESYS              = 'FK5'
* FEBE1                = 'ARTEMIS450-BEAR1'
* FILTER               = '450um'
  RESTFREQ             = 666.199982
  BMAJ                 = 0.0027777778
  BMIN                 = 0.0027777778
  BPA                  = 0.0
* WAVELMIN             = 435000.0
* WAVELMAX             = 485000.0
  WAVE                 = 450.0
* SKY_RES              = 10
  BTYPE                = 'spectral flux density'
* BUNIT                = 'MJy/sr'
  BCONV                = 375.47916728
* FLUXCAL              = 'ABSOLUTE'
* FLUXERR              = 25
* BNOISE               = 106.1
* TIMESYS              = 'TAI'
* TEXPTIME             = 11883
* MJD-OBS              = 59460.1161458333
* MJD-END              = 59811.9391550926
  DATE                 = '2024-06-06'
* PROG_ID              = '1102.C-0745(A)'
* NCOMBINE             = 10
* PROV1                = 'APEXBOL.2021-09-03T02:47:15.000.fits'
* PROV2                = 'APEXBOL.2021-09-03T03:05:39.000.fits'
* PROV3                = 'APEXBOL.2022-05-15T10:04:40.000.fits'
* PROV4                = 'APEXBOL.2022-05-15T10:23:12.000.fits'
* PROV5                = 'APEXBOL.2022-06-29T06:03:43.000.fits'
* PROV6                = 'APEXBOL.2022-06-29T06:22:26.000.fits'
* PROV7                = 'APEXBOL.2022-07-01T04:35:41.000.fits'
* PROV8                = 'APEXBOL.2022-07-01T04:57:04.000.fits'
* PROV9                = 'APEXBOL.2022-08-20T22:11:09.000.fits'
* PROV10               = 'APEXBOL.2022-08-20T22:32:23.000.fits'
* PROCSOFT             = 'APIS'
* REFERENC             = '2024arXiv240515713M'
  HORIGIN              = 'Herschel Science Centre'
  HCALVERS             = 'spire_cal_14_3'
  HLEVEL               = '30'
  DETECTOR             = 'PLW'
  HOBSID01             = 1342204091
  HOBSID02             = 1342204090
* NOESODAT             = True
* CHECKSUM             = 'DAAQF29PD9APD97P'
* DATASUM              = '129194275'
  ARCFILE              = 'ADP.2024-07-12T08:07:39.447.fits'
  ORIGFILE             = 'SDC345.0_CAFFEINE_450um_ESO.fits'
  P3ORIG               = 'EDP'
```
