# SPECTRUM header keyword report

**Archive example:** [ESO header page](https://archive.eso.org/hdr?DpId=ADP.2026-07-13T03:27:49.375)

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
- [ ] **EXT_OBJ**
- [ ] **CONTNORM**
- [ ] **TOT_FLUX**
- [ ] **FLUXERR**
- [ ] **WAVELMIN**
- [ ] **WAVELMAX**
- [ ] **SPEC_BIN**
- [ ] **SNR**
- [ ] **SPEC_RES**
- [ ] **STREHL**
- [ ] **CHECKSUM**
- [ ] **DATASUM**
- [ ] **NOESODAT**

### Extension HDU

- [ ] **OBJECT**
- [ ] **RA and DEC**
- [ ] **NELEM**
- [ ] **VOCLASS**
- [ ] **VOPUB**
- [ ] **TITLE**
- [ ] **APERTURE**
- [ ] **TELAPSE**
- [ ] **TMID**
- [ ] **SPEC_VAL**
- [ ] **SPEC_BW**
- [ ] **CHECKSUM**
- [ ] **DATASUM**
- [ ] **TFIELDS**
- [ ] **TTYPEi (for example: TTYPE1, TTYPE2, TTYPE3, etc.)**
- [ ] **TFORMi (for example: TFORM1, TFORM2, TFORM3, etc.)**
- [ ] **TUNITi (for example: TUNIT1, TUNIT2, TUNIT3, etc.)**
- [ ] **TUTYPi (for example: TUTYP1, TUTYP2, TUTYP3, etc.)**
- [ ] **TUCDi (for example: TUCD1, TUCD2, TUCD3, etc.)**
- [ ] **TDMINi (for example: TDMIN1, TDMIN2, TDMIN3, etc.)**
- [ ] **TDMAXi (for example: TDMAX1, TDMAX2, TDMAX3, etc.)**
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
| BUNIT | `NO` | Keyword not allowed: the Phase 3 system will reject the file |
| CDi_j | `NO` | Keyword not allowed: the Phase 3 system will reject the file |
| **SPECSYS** | `MM` | Keyword mandatory |
| **EXT_OBJ** | `MA42` | Keyword mandatory where applicable [footnote 42] |
| **CONTNORM** | `MM` | Keyword mandatory |
| **TOT_FLUX** | `MM` | Keyword mandatory |
| **FLUXERR** | `M43` | Keyword mandatory [footnote 43] |
| **WAVELMIN** | `MM` | Keyword mandatory |
| **WAVELMAX** | `MM` | Keyword mandatory |
| LAMRMS | `OP` | It makes sense to provide the value, but it is optional |
| LAMNLIN | `OP` | It makes sense to provide the value, but it is optional |
| **SPEC_BIN** | `MM` | Keyword mandatory |
| SPEC_ERR | `RC` | Keyword recommended |
| SPEC_SYE | `RC` | Keyword recommended |
| RA_ERR | `RC` | Keyword recommended |
| DEC_ERR | `RC` | Keyword recommended |
| STOKES | `SU` | Contact Phase 3 support to determine whether the keyword is required |
| **SNR** | `MM` | Keyword mandatory |
| **SPEC_RES** | `MM` | Keyword mandatory |
| **STREHL** | `MA51` | Keyword mandatory where applicable [footnote 51] |
| ARCFILE | `RS` | Reserved keyword. If present, modified by the Phase 3 system during the archiving process |
| **CHECKSUM** | `MM` | Keyword mandatory |
| **DATASUM** | `MM` | Keyword mandatory |
| ORIGFILE | `RS` | Reserved keyword. If present, modified by the Phase 3 system during the archiving process |
| P3ORIG | `RS` | Reserved keyword. If present, modified by the Phase 3 system during the archiving process |
| **NOESODAT** | `MA59` | Keyword mandatory where applicable [footnote 59] |

### Extension HDU

| Keyword | Requirement | Meaning |
| --- | --- | --- |
| **OBJECT** | `MM` | Keyword mandatory |
| **RA and DEC** | `MM` | Keyword mandatory |
| **NELEM** | `MM` | Keyword mandatory |
| **VOCLASS** | `MM` | Keyword mandatory |
| **VOPUB** | `MM` | Keyword mandatory |
| **TITLE** | `MM` | Keyword mandatory |
| **APERTURE** | `MM` | Keyword mandatory |
| **TELAPSE** | `MM` | Keyword mandatory |
| **TMID** | `MM` | Keyword mandatory |
| **SPEC_VAL** | `MM` | Keyword mandatory |
| **SPEC_BW** | `MM` | Keyword mandatory |
| **CHECKSUM** | `MM` | Keyword mandatory |
| **DATASUM** | `MM` | Keyword mandatory |
| **TFIELDS** | `MM` | Keyword mandatory |
| **TTYPEi (for example: TTYPE1, TTYPE2, TTYPE3, etc.)** | `MM` | Keyword mandatory |
| **TFORMi (for example: TFORM1, TFORM2, TFORM3, etc.)** | `MM` | Keyword mandatory |
| TCOMMi (for example: TCOMM1, TCOMM2, TCOMM3, etc.) | `OP` | It makes sense to provide the value, but it is optional |
| **TUNITi (for example: TUNIT1, TUNIT2, TUNIT3, etc.)** | `M61` | Keyword mandatory [footnote 61] |
| **TUTYPi (for example: TUTYP1, TUTYP2, TUTYP3, etc.)** | `M62` | Keyword mandatory [footnote 62] |
| **TUCDi (for example: TUCD1, TUCD2, TUCD3, etc.)** | `MM` | Keyword mandatory |
| **TDMINi (for example: TDMIN1, TDMIN2, TDMIN3, etc.)** | `MA63` | Keyword mandatory where applicable [footnote 63] |
| **TDMAXi (for example: TDMAX1, TDMAX2, TDMAX3, etc.)** | `MA63` | Keyword mandatory where applicable [footnote 63] |
| **EXTNAME** | `MA65` | Keyword mandatory where applicable [footnote 65] |

## Referenced footnotes

31. Mandatory for the cases where ancillary files are provided in a non-FITS format.
32. Mandatory for the cases where ancillary files are provided in association with the scientific data.
37. If RADESYS='FK5', EQUINOX=2000.0 is mandatory. If RADESYS = 'ICRS', EQUINOX is tolerated and its value needs to be 2000.0.
38. Must be present if the system used is other than UTC.
40. If a refereed publication is not available at the time of the data release going public, the value can be left to an empty string.
42. EXT_OBJ is mandatory for externally submitted data products (e.g. spectroscopic public surveys). EXT_OBJ is not applicable to data processed in an unsupervised way, for which the keyword value cannot be assessed and thus the property is not known.
43. FLUXERR applies to SCIENCE.SPECTRUM with FLUXCAL='ABSOLUTE'. In case of SCIENCE.SPECTRUM with FLUXCAL = 'UNCALIBRATED', the FLUXERR keyword shall be set to -1. The special value -2 is reserved for the case when the flux error cannot be determined.
51. For AO observations only.
59. Applicable to products originating or containing data from a non-ESO facility.
61. For quantities having no units of measurement, the value shall be set to an empty string.
62. In case the UType is not defined in the IVOA document [9] like e.g. for CONTINUUM, the corresponding TUTYPi keyword shall be set to an empty string.
63. Mandatory for the TTYPE1 array only (start/stop spectral coordinates).
65. A specific value is requested in particular cases: 'PHASE3PROVENANCE', 'PHASE3CATALOG', 'PHASE3FILELIST'.

## Example archive FITS headers

Lines prefixed with `*` are mandatory, mandatory for ESO files, or mandatory when applicable.

### HDU 0 — PRIMARY

```text
  SIMPLE               = True
  BITPIX               = 16
  NAXIS                = 0
  EXTEND               = True
  DATE                 = '2026-07-12T10:53:04'
* ORIGIN               = 'ESO-LASILLA'
* OBJECT               = 'HR7590'
* RA                   = 300.141352
* DEC                  = -72.91597
* EXPTIME              = 61.3063
* MJD-OBS              = 61233.447006216
* MJD-END              = 61233.4477157797
* TELESCOP             = 'ESO-3.6'
* INSTRUME             = 'NIRPS'
* EQUINOX              = 2000.0
  DATE-OBS             = '2026-07-12T10:43:41'
  UTC                  = 38622.0
  LST                  = 4929.233
  PI-COI               = 'UNKNOWN'
  OBSERVER             = 'UNKNOWN'
* RADESYS              = 'FK5'
* PRODCATG             = 'SCIENCE.SPECTRUM'
* CONTNORM             = False
* FLUXERR              = -2.0
* REFERENC             = ''
  PRODLVL              = 2
* SPECSYS              = 'BARYCENT'
* PROCSOFT             = 'nirps/3.2.7'
  DISPELEM             = 'VIS'
* PROG_ID              = '60.A-9109(A)'
* OBID1                = 1000290075
* OBSTECH              = 'ECHELLE'
* FLUXCAL              = 'ABSOLUTE'
* WAVELMIN             = 966.050878989813
* WAVELMAX             = 1923.08435528157
* SPEC_BIN             = 0.00431819750343709
* TEXPTIME             = 61.3063
  LAMNLIN              = 380
  LAMRMS               = 0.003
* SPEC_RES             = 70000.0
  SPEC_ERR             = 0.000153896752812773
* TOT_FLUX             = False
* SNR                  = 175.154819591757
* PROV1                = 'NIRPS.2026-07-12T10:43:41.337.fits'
* NCOMBINE             = 1
  DATAMD5              = '4d2e258486006332dea039b910a7ec39'
* CHECKSUM             = 'YNa5aKX2ZKa2aKU2'
* DATASUM              = '0'
* ASSOC1               = 'ANCILLARY.2DECHELLE.TAR'
* ASSOM1               = 'b6895f02a22d4d8531ec225823fdb92e'
* ASSON1               = 'r.NIRPS.2026-07-12T10:43:41.337.tar'
* ASSON2               = 'r.NIRPS.2026-07-12T10:43:41.337_CCF_TELL_CORR_A.fits'
* ASSON3               = 'r.NIRPS.2026-07-12T10:43:41.337_S1D_FINAL_B.fits'
  ARCFILE              = 'ADP.2026-07-13T03:27:49.375.fits'
  ORIGFILE             = 'r.NIRPS.2026-07-12T10:43:41.337_S1D_FINAL_A.fits'
  P3ORIG               = 'IDP'
```

### HDU 1 — SPECTRUM

```text
  XTENSION             = 'BINTABLE'
  BITPIX               = 8
  NAXIS                = 2
  NAXIS1               = 46985348
  NAXIS2               = 1
  PCOUNT               = 0
  GCOUNT               = 1
* TFIELDS              = 31
* TTYPE1               = 'WAVE'
* TFORM1               = '221629D'
* TUNIT1               = 'angstrom'
* TTYPE2               = 'FLUX'
* TFORM2               = '221629D'
* TUNIT2               = 'erg.cm**(-2).s**(-1).angstrom**(-1)'
* TTYPE3               = 'ERR'
* TFORM3               = '221629D'
* TUNIT3               = 'erg.cm**(-2).s**(-1).angstrom**(-1)'
* TTYPE4               = 'QUAL'
* TFORM4               = '221629J'
* TUNIT4               = ''
* TTYPE5               = 'SNR'
* TFORM5               = '221629D'
* TUNIT5               = ''
* TTYPE6               = 'WAVE_AIR'
* TFORM6               = '221629D'
* TUNIT6               = 'angstrom'
* TTYPE7               = 'FLUX_EL'
* TFORM7               = '221629D'
* TUNIT7               = ''
* TTYPE8               = 'ERR_EL'
* TFORM8               = '221629D'
* TUNIT8               = ''
* TTYPE9               = 'QUAL_EL'
* TFORM9               = '221629J'
* TUNIT9               = ''
* TTYPE10              = 'FLUX_CAL'
* TFORM10              = '221629D'
* TUNIT10              = 'erg.s**(-1).cm**(-2).angstrom**(-1)'
* TTYPE11              = 'ERR_CAL'
* TFORM11              = '221629D'
* TUNIT11              = 'erg.s**(-1).cm**(-2).angstrom**(-1)'
* TTYPE12              = 'QUAL_CAL'
* TFORM12              = '221629J'
* TUNIT12              = ''
* TTYPE13              = 'FLUX_CAL_SKYSUB'
* TFORM13              = '221629D'
* TUNIT13              = 'erg.s**(-1).cm**(-2).angstrom**(-1)'
* TTYPE14              = 'ERR_CAL_SKYSUB'
* TFORM14              = '221629D'
* TUNIT14              = 'erg.s**(-1).cm**(-2).angstrom**(-1)'
* TTYPE15              = 'QUAL_CAL_SKYSUB'
* TFORM15              = '221629J'
* TUNIT15              = ''
* TTYPE16              = 'FLUX_EL_SKYSUB'
* TFORM16              = '221629D'
* TUNIT16              = ''
* TTYPE17              = 'ERR_EL_SKYSUB'
* TFORM17              = '221629D'
* TUNIT17              = ''
* TTYPE18              = 'QUAL_EL_SKYSUB'
* TFORM18              = '221629J'
* TUNIT18              = ''
* TTYPE19              = 'FLUX_TELL_EL'
* TFORM19              = '221629D'
* TUNIT19              = ''
* TTYPE20              = 'ERR_TELL_EL'
* TFORM20              = '221629D'
* TUNIT20              = ''
* TTYPE21              = 'QUAL_TELL_EL'
* TFORM21              = '221629J'
* TUNIT21              = ''
* TTYPE22              = 'ATM_TRANSM'
* TFORM22              = '221629D'
* TUNIT22              = ''
* TTYPE23              = 'FLUX_TELL_CAL'
* TFORM23              = '221629D'
* TUNIT23              = 'erg.s**(-1).cm**(-2).angstrom**(-1)'
* TTYPE24              = 'ERR_TELL_CAL'
* TFORM24              = '221629D'
* TUNIT24              = 'erg.s**(-1).cm**(-2).angstrom**(-1)'
* TTYPE25              = 'QUAL_TELL_CAL'
* TFORM25              = '221629J'
* TUNIT25              = ''
* TTYPE26              = 'FLUX_TELL_EL_SKYSUB'
* TFORM26              = '221629D'
* TUNIT26              = ''
* TTYPE27              = 'ERR_TELL_EL_SKYSUB'
* TFORM27              = '221629D'
* TUNIT27              = ''
* TTYPE28              = 'QUAL_TELL_EL_SKYSUB'
* TFORM28              = '221629J'
* TUNIT28              = ''
* TTYPE29              = 'FLUX_TELL_CAL_SKYSUB'
* TFORM29              = '221629D'
* TUNIT29              = 'erg.s**(-1).cm**(-2).angstrom**(-1)'
* TTYPE30              = 'ERR_TELL_CAL_SKYSUB'
* TFORM30              = '221629D'
* TUNIT30              = 'erg.s**(-1).cm**(-2).angstrom**(-1)'
* TTYPE31              = 'QUAL_TELL_CAL_SKYSUB'
* TFORM31              = '221629J'
* TUNIT31              = ''
* OBJECT               = 'HR7590'
* RA                   = 300.141352
* DEC                  = -72.91597
* VOCLASS              = 'SPECTRUM V2.0'
* VOPUB                = 'ESO/SAF'
* APERTURE             = 0.00025
* TELAPSE              = 61.3063
* TMID                 = 61233.4473609978
* TDMIN1               = 9660.50878989813
* TDMAX1               = 19230.8435528157
* SPEC_VAL             = 1444.56761713569
* SPEC_BW              = 957.033476291755
* EXTNAME              = 'SPECTRUM'
  INHERIT              = True
* TUTYP1               = 'spec:Data.SpectralAxis.Value'
* TUCD1                = 'em.wl;meta.main'
* TUTYP2               = 'spec:Data.FluxAxis.Value'
* TUCD2                = 'phot.flux.density;em.wl;src.net;meta.main'
* TUTYP3               = 'spec:Data.FluxAxis.Accuracy.StatError'
* TUCD3                = 'stat.error;phot.flux.density;meta.main;src.net'
* TUTYP4               = 'spec:Data.FluxAxis.Accuracy.QualityStatus'
* TUCD4                = 'meta.code.qual;meta.main;src.net'
* TUTYP5               = 'eso:Data.FluxAxis.Accuracy.SNR'
* TUCD5                = 'stat.snr'
* TUTYP6               = 'eso:Data.SpectralAxis.Value'
* TUCD6                = 'em.wl;obs.atmos'
* TUTYP7               = 'eso:Data.FluxAxis.Value'
* TUCD7                = ''
* TUTYP8               = 'eso:Data.FluxAxis.Accuracy.StatError'
* TUCD8                = ''
* TUTYP9               = 'eso:Data.FluxAxis.Accuracy.QualityStatus'
* TUCD9                = 'meta.code.qual'
* TUTYP10              = 'eso:Data.FluxAxis.Value'
* TUCD10               = 'phot.flux.density;em.wl'
* TUTYP11              = 'eso:Data.FluxAxis.Accuracy.StatError'
* TUCD11               = 'stat.error;phot.flux.density'
* TUTYP12              = 'eso:Data.FluxAxis.Accuracy.QualityStatus'
* TUCD12               = 'meta.code.qual'
* TUTYP13              = 'eso:Data.FluxAxis.Value'
* TUCD13               = 'phot.flux.density;em.wl;src.net'
* TUTYP14              = 'eso:Data.FluxAxis.Accuracy.StatError'
* TUCD14               = 'stat.error;phot.flux.density;src.net'
* TUTYP15              = 'eso:Data.FluxAxis.Accuracy.QualityStatus'
* TUCD15               = 'meta.code.qual;src.net'
* TUTYP16              = 'eso:Data.FluxAxis.Value'
* TUCD16               = ''
* TUTYP17              = 'eso:Data.FluxAxis.Accuracy.StatError'
* TUCD17               = ''
* TUTYP18              = 'eso:Data.FluxAxis.Accuracy.QualityStatus'
* TUCD18               = 'meta.code.qual'
* TUTYP19              = 'eso:Data.FluxAxis.Value'
* TUCD19               = ''
* TUTYP20              = 'eso:Data.FluxAxis.Accuracy.StatError'
* TUCD20               = ''
* TUTYP21              = 'eso:Data.FluxAxis.Accuracy.QualityStatus'
* TUCD21               = 'meta.code.qual'
* TUTYP22              = ''
* TUCD22               = 'phys.transmission'
* TUTYP23              = 'eso:Data.FluxAxis.Value'
* TUCD23               = 'phot.flux.density;em.wl'
* TUTYP24              = 'eso:Data.FluxAxis.Accuracy.StatError'
* TUCD24               = 'stat.error;phot.flux.density'
* TUTYP25              = 'eso:Data.FluxAxis.Accuracy.QualityStatus'
* TUCD25               = 'meta.code.qual'
* TUTYP26              = 'eso:Data.FluxAxis.Value'
* TUCD26               = ''
* TUTYP27              = 'eso:Data.FluxAxis.Accuracy.StatError'
* TUCD27               = ''
* TUTYP28              = 'eso:Data.FluxAxis.Accuracy.QualityStatus'
* TUCD28               = 'meta.code.qual'
* TUTYP29              = 'eso:Data.FluxAxis.Value'
* TUCD29               = 'phot.flux.density;em.wl;src.net'
* TUTYP30              = 'eso:Data.FluxAxis.Accuracy.StatError'
* TUCD30               = 'stat.error;phot.flux.density;src.net'
* TUTYP31              = 'eso:Data.FluxAxis.Accuracy.QualityStatus'
* TUCD31               = 'meta.code.qual;src.net'
* NELEM                = 221629
* CHECKSUM             = 'UVAhXT4eUT9eUT9e'
* DATASUM              = '2523876983'
* TITLE                = '2026-07-12T10:43:41_HR7590'
```
