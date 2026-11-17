# CATALOG header keyword report

**Archive example:** [ESO header page](https://archive.eso.org/hdr?DpId=ADP.2025-05-14T09:12:30.235)

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
- [ ] **MJD-OBS**
- [ ] **MJD-END**
- [ ] **PROG_ID or PROGIDi (for example: PROGID1, PROGID2, PROGID3, etc.)**
- [ ] **OBIDi (for example: OBID1, OBID2, OBID3, etc.)**
- [ ] **OBSTECH**
- [ ] **PROCSOFT**
- [ ] **REFERENC**
- [ ] **PROVi (for example: PROV1, PROV2, PROV3, etc.) or PROVXTN**
- [ ] **PHOTSYS**
- [ ] **WAVELMIN**
- [ ] **WAVELMAX**
- [ ] **BNOISE**
- [ ] **MAPMODE**
- [ ] **FEBEi (for example: FEBE1, FEBE2, FEBE3, etc.)**
- [ ] **ABMAGLIM**
- [ ] **MAGLIMi (for example: MAGLIM1, MAGLIM2, MAGLIM3, etc.)**
- [ ] **SKY_RES**
- [ ] **SKY_RERR**
- [ ] **CHECKSUM**
- [ ] **DATASUM**
- [ ] **FPRAia**
- [ ] **FPDEia**
- [ ] **SKYSQDEG**
- [ ] **M_EPOCH**
- [ ] **APMATCHD**
- [ ] **TXLNKi (for example: TXLNK1, TXLNK2, TXLNK3, etc.)**
- [ ] **TXRGF**
- [ ] **TXCTY**
- [ ] **NOESODAT**

### Extension HDU

- [ ] **CHECKSUM**
- [ ] **DATASUM**
- [ ] **TFIELDS**
- [ ] **TTYPEi (for example: TTYPE1, TTYPE2, TTYPE3, etc.)**
- [ ] **TFORMi (for example: TFORM1, TFORM2, TFORM3, etc.)**
- [ ] **TCOMMi (for example: TCOMM1, TCOMM2, TCOMM3, etc.)**
- [ ] **TUNITi (for example: TUNIT1, TUNIT2, TUNIT3, etc.)**
- [ ] **TUCDi (for example: TUCD1, TUCD2, TUCD3, etc.)**
- [ ] **TNULLi (for example: TNULL1, TNULL2, TNULL3, etc.)**
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
| **FILTER or FILTERi (for example: FILTER1, FILTER2, FILTER3, etc.)** | `MA35` | Keyword mandatory where applicable [footnote 35] |
| **OBJECT** | `MM` | Keyword mandatory |
| **RA and DEC** | `MA36` | Keyword mandatory where applicable [footnote 36] |
| **EQUINOX** | `MA37 MA36` | Keyword mandatory where applicable [footnote 37]; Keyword mandatory where applicable [footnote 36] |
| **RADESYS** | `MA36` | Keyword mandatory where applicable [footnote 36] |
| **TIMESYS** | `MA38` | Keyword mandatory where applicable [footnote 38] |
| **MJD-OBS** | `MM` | Keyword mandatory |
| **MJD-END** | `MM` | Keyword mandatory |
| **PROG_ID or PROGIDi (for example: PROGID1, PROGID2, PROGID3, etc.)** | `ME` | Keyword mandatory for ESO files |
| **OBIDi (for example: OBID1, OBID2, OBID3, etc.)** | `ME` | Keyword mandatory for ESO files |
| **OBSTECH** | `MA39` | Keyword mandatory where applicable [footnote 39] |
| **PROCSOFT** | `MM` | Keyword mandatory |
| **REFERENC** | `M40` | Keyword mandatory [footnote 40] |
| **PROVi (for example: PROV1, PROV2, PROV3, etc.) or PROVXTN** | `ME` | Keyword mandatory for ESO files |
| **PHOTSYS** | `MM` | Keyword mandatory |
| **WAVELMIN** | `MA44` | Keyword mandatory where applicable [footnote 44] |
| **WAVELMAX** | `MA44` | Keyword mandatory where applicable [footnote 44] |
| **BNOISE** | `MA45` | Keyword mandatory where applicable [footnote 45] |
| **MAPMODE** | `MA45` | Keyword mandatory where applicable [footnote 45] |
| **FEBEi (for example: FEBE1, FEBE2, FEBE3, etc.)** | `MA45` | Keyword mandatory where applicable [footnote 45] |
| STOKES | `SU` | Contact Phase 3 support to determine whether the keyword is required |
| **ABMAGLIM** | `MA47` | Keyword mandatory where applicable [footnote 47] |
| **MAGLIMi (for example: MAGLIM1, MAGLIM2, MAGLIM3, etc.)** | `MA48` | Keyword mandatory where applicable [footnote 48] |
| **SKY_RES** | `MA45` | Keyword mandatory where applicable [footnote 45] |
| **SKY_RERR** | `MA50` | Keyword mandatory where applicable [footnote 50] |
| ARCFILE | `RS` | Reserved keyword. If present, modified by the Phase 3 system during the archiving process |
| **CHECKSUM** | `MM` | Keyword mandatory |
| **DATASUM** | `MM` | Keyword mandatory |
| ORIGFILE | `RS` | Reserved keyword. If present, modified by the Phase 3 system during the archiving process |
| P3ORIG | `RS` | Reserved keyword. If present, modified by the Phase 3 system during the archiving process |
| **FPRAia** | `MA54` | Keyword mandatory where applicable [footnote 54] |
| **FPDEia** | `MA54` | Keyword mandatory where applicable [footnote 54] |
| **SKYSQDEG** | `MA54` | Keyword mandatory where applicable [footnote 54] |
| **M_EPOCH** | `MA55` | Keyword mandatory where applicable [footnote 55] |
| **APMATCHD** | `MA56` | Keyword mandatory where applicable [footnote 56] |
| **TXLNKi (for example: TXLNK1, TXLNK2, TXLNK3, etc.)** | `MA57 MA58` | Keyword mandatory where applicable [footnote 57]; Keyword mandatory where applicable [footnote 58] |
| **TXRGF** | `MA57` | Keyword mandatory where applicable [footnote 57] |
| **TXCTY** | `MA57` | Keyword mandatory where applicable [footnote 57] |
| **NOESODAT** | `MA59` | Keyword mandatory where applicable [footnote 59] |
| TZEROi (for example: TZERO1, TZERO2, TZERO3, etc.) | `NO` | Keyword not allowed: the Phase 3 system will reject the file |
| TSCALi (for example: TSCAL1, TSCAL2, TSCAL3, etc.) | `NO` | Keyword not allowed: the Phase 3 system will reject the file |
| EXTVER | `NO` | Keyword not allowed: the Phase 3 system will reject the file |
| EXTLEVEL | `NO` | Keyword not allowed: the Phase 3 system will reject the file |

### Extension HDU

| Keyword | Requirement | Meaning |
| --- | --- | --- |
| **CHECKSUM** | `MM` | Keyword mandatory |
| **DATASUM** | `MM` | Keyword mandatory |
| **TFIELDS** | `MM` | Keyword mandatory |
| **TTYPEi (for example: TTYPE1, TTYPE2, TTYPE3, etc.)** | `MM` | Keyword mandatory |
| **TFORMi (for example: TFORM1, TFORM2, TFORM3, etc.)** | `MM` | Keyword mandatory |
| **TCOMMi (for example: TCOMM1, TCOMM2, TCOMM3, etc.)** | `MM` | Keyword mandatory |
| **TUNITi (for example: TUNIT1, TUNIT2, TUNIT3, etc.)** | `M61` | Keyword mandatory [footnote 61] |
| **TUCDi (for example: TUCD1, TUCD2, TUCD3, etc.)** | `MM` | Keyword mandatory |
| TDMINi (for example: TDMIN1, TDMIN2, TDMIN3, etc.) | `OP` | It makes sense to provide the value, but it is optional |
| TDMAXi (for example: TDMAX1, TDMAX2, TDMAX3, etc.) | `OP` | It makes sense to provide the value, but it is optional |
| **TNULLi (for example: TNULL1, TNULL2, TNULL3, etc.)** | `MA64` | Keyword mandatory where applicable [footnote 64] |
| **EXTNAME** | `MA65` | Keyword mandatory where applicable [footnote 65] |
| TZEROi (for example: TZERO1, TZERO2, TZERO3, etc.) | `NO` | Keyword not allowed: the Phase 3 system will reject the file |
| TSCALi (for example: TSCAL1, TSCAL2, TSCAL3, etc.) | `NO` | Keyword not allowed: the Phase 3 system will reject the file |
| EXTVER | `NO` | Keyword not allowed: the Phase 3 system will reject the file |
| EXTLEVEL | `NO` | Keyword not allowed: the Phase 3 system will reject the file |

## Referenced footnotes

31. Mandatory for the cases where ancillary files are provided in a non-FITS format.
32. Mandatory for the cases where ancillary files are provided in association with the scientific data.
35. Applicable to photometric catalogues as well as APEX catalogues.
36. There can be cases where that keyword does not apply, for instance in the case of target catalogues of spectroscopic surveys, e.g. PESSTO where no appropriate RA/DEC value can be defined to characterise the catalogue as a whole.
37. If RADESYS='FK5', EQUINOX=2000.0 is mandatory. If RADESYS = 'ICRS', EQUINOX is tolerated and its value needs to be 2000.0.
38. Must be present if the system used is other than UTC.
39. Does not apply to catalogues for which no unique value of OBSTECH can be identified.
40. If a refereed publication is not available at the time of the data release going public, the value can be left to an empty string.
44. Applicable to spectroscopic and APEX catalogues. For photometric catalogues, the value is calculated by the Phase 3 system unless the combination (INSTRi, FILTERi) is not unique, in which case please contact Phase 3 operations support staff at https://support.eso.org/ to assess the correct values of the WAVELMIN/MAX keywords, to be added in the headers.
45. For APEX catalogues only.
47. For photometric catalogues. And if there is more than one filter, it is not applicable. Use MAGLIMi instead.
48. For photometric catalogues with more than one filter.
50. Applicable to the case when SKY_RES is expected to vary within the data collection due to the way it is estimated (see footnote 18).
54. Does not apply to spectroscopic catalogues for which no coverage pattern exists.
55. Applicable to multi-epoch catalogues formatted according to section 12.5.1 only.
56. For aperture-matched catalogues only.
57. In case data link is used (see section 12.3).
58. In case provenance per catalogue record is used (see section 5.2.3).
59. Applicable to products originating or containing data from a non-ESO facility.
61. For quantities having no units of measurement, the value shall be set to an empty string.
64. See section 5.18 and section 12.2.6 for applicability.
65. A specific value is requested in particular cases: 'PHASE3PROVENANCE', 'PHASE3CATALOG', 'PHASE3FILELIST'.

## Example archive FITS headers

Lines prefixed with `*` are mandatory, mandatory for ESO files, or mandatory when applicable.

### HDU 0 — PRIMARY

```text
  SIMPLE               = True
  BITPIX               = 8
  NAXIS                = 0
  EXTEND               = True
* PRODCATG             = 'SCIENCE.CATALOGTILE'
* ORIGIN               = 'ESO-PARANAL'
* TELESCOP             = 'ESO-VLT-U4'
* INSTRUME             = 'MUSE'
* OBJECT               = 'NGC3627'
* RA                   = 170.072929
* DEC                  = 12.98949
* EQUINOX              = 2000.0
* RADESYS              = 'FK5'
* MJD-OBS              = 58143.30544515
* MJD-END              = 58253.10481107778
* PROG_ID              = '1100.B-0651(A)'
* OBSTECH              = 'IFU'
* WAVELMIN             = 475.125
* WAVELMAX             = 934.625
* ABMAGLIM             = 0.0
* NOESODAT             = 'F'
* REFERENC             = '2023MNRAS.520.4902G'
  DATE                 = '2025-05-13T13:59:12.094104'
* M_EPOCH              = False
* PHOTSYS              = 'AB'
* PROCSOFT             = 'Groves23'
* SKYSQDEG             = 0.002293400603824618
  FPRA1                = 170.0459011778574
  FPDE1                = 12.948413847608585
  FPRA2                = 170.04589410763856
  FPDE2                = 13.014358276338157
  FPRA3                = 170.08158874491266
  FPDE3                = 13.014359477502964
  FPRA4                = 170.0815863399736
  FPDE4                = 12.948415042473824
* OBID1                = 1805686
* OBID2                = 1805690
* OBID3                = 1805694
* OBID4                = 1805698
* OBID5                = 1805702
* OBID6                = 1805706
* OBID7                = 1805710
* OBID8                = 1805714
* PROV1                = 'ADP.2021-07-16T10:20:56.465.fits'
* ASSON1               = 'NGC3627_nebulae_mask.fits'
* CHECKSUM             = 'OoAAQn52OnA8On58'
* DATASUM              = '0'
  AUTHOR               = 'PHANGS collaboration'
  ARCFILE              = 'ADP.2025-05-14T09:12:30.235.fits'
  ORIGFILE             = 'NGC3627_catalog.fits'
  P3ORIG               = 'EDP'
```

### HDU 1 — PHASE3CATALOG

```text
  XTENSION             = 'BINTABLE'
  BITPIX               = 8
  NAXIS                = 2
  NAXIS1               = 603
  NAXIS2               = 1631
  PCOUNT               = 0
  GCOUNT               = 1
* TFIELDS              = 75
* TUCD1                = 'meta.id;meta.main'
* TCOMM1               = 'Unique source identifier'
* TUNIT1               = ''
* TUCD2                = 'meta.id.part'
* TCOMM2               = 'Galaxy name'
* TUNIT2               = ''
* TUCD3                = 'meta.id.part'
* TCOMM3               = 'Region ID within galaxy'
* TUNIT3               = ''
* TUCD4                = 'pos.eq.ra;meta.main'
* TCOMM4               = 'Right Ascension (J2000)'
* TUCD5                = 'pos.eq.dec;meta.main'
* TCOMM5               = 'Declination (J2000)'
* TUCD6                = 'meta.code'
* TCOMM6               = 'Flag for edge region'
* TUNIT6               = ''
* TUCD7                = 'meta.code'
* TCOMM7               = 'Flag for stellar contamination'
* TUNIT7               = ''
* TUCD8                = 'pos.posang'
* TCOMM8               = 'Deprojected angle from galaxy center'
* TUCD9                = 'phys.area;instr.pixel'
* TCOMM9               = 'Region area in pixels'
* TUCD10               = 'phot.flux;em.line.Hbeta'
* TCOMM10              = 'Hbeta flux'
* TUCD11               = 'phot.flux;em.line.OIII'
* TCOMM11              = '[O III] 5006 flux'
* TUCD12               = 'phot.flux;em.line.Halpha'
* TCOMM12              = 'Halpha flux'
* TUCD13               = 'phot.flux;em.line'
* TCOMM13              = '[N II] 6583 flux'
* TUCD14               = 'phot.flux;em.line'
* TCOMM14              = '[S II] 6716 flux'
* TUCD15               = 'phot.flux;em.line'
* TCOMM15              = '[S II] 6730 flux'
* TUCD16               = 'phot.flux;em.line'
* TCOMM16              = '[S III] 9068 flux'
* TUCD17               = 'phot.flux;em.line'
* TCOMM17              = '[O I] 6300 flux'
* TUCD18               = 'stat.error;phot.flux;em.line.Hbeta'
* TCOMM18              = 'Hbeta flux error'
* TUCD19               = 'stat.error;phot.flux;em.line.OIII'
* TCOMM19              = '[O III] 5006 flux error'
* TUCD20               = 'stat.error;phot.flux;em.line.Halpha'
* TCOMM20              = 'Halpha flux error'
* TUCD21               = 'stat.error;phot.flux;em.line'
* TCOMM21              = '[N II] 6583 flux error'
* TUCD22               = 'stat.error;phot.flux;em.line'
* TCOMM22              = '[S II] 6716 flux error'
* TUCD23               = 'stat.error;phot.flux;em.line'
* TCOMM23              = '[S II] 6730 flux error'
* TUCD24               = 'stat.error;phot.flux;em.line'
* TCOMM24              = '[S III] 9068 flux error'
* TUCD25               = 'stat.error;phot.flux;em.line'
* TCOMM25              = '[O I] 6300 flux error'
* TUCD26               = 'spect.line.width;em.line.Halpha'
* TCOMM26              = 'Halpha velocity dispersion'
* TUCD27               = 'spect.line.width;em.line'
* TCOMM27              = '[N II] velocity dispersion'
* TUCD28               = 'spect.line.width;em.line.OIII'
* TCOMM28              = '[O III] velocity dispersion'
* TUCD29               = 'phys.veloc;em.line.Halpha'
* TCOMM29              = 'Halpha line-of-sight velocity'
* TUCD30               = 'phys.veloc;em.line'
* TCOMM30              = '[N II] velocity'
* TUCD31               = 'phys.veloc;em.line.OIII'
* TCOMM31              = '[O III] velocity'
* TUCD32               = 'stat.error;spect.line.width;em.line.Halpha'
* TCOMM32              = 'Halpha sigma error'
* TUCD33               = 'stat.error;spect.line.width;em.line'
* TCOMM33              = '[N II] sigma error'
* TUCD34               = 'stat.error;spect.line.width;em.line.OIII'
* TCOMM34              = '[O III] sigma error'
* TUCD35               = 'stat.error;phys.veloc;em.line.Halpha'
* TCOMM35              = 'Halpha velocity error'
* TUCD36               = 'stat.error;phys.veloc;em.line'
* TCOMM36              = '[N II] velocity error'
* TUCD37               = 'stat.error;phys.veloc;em.line.OIII'
* TCOMM37              = '[O III] velocity error'
* TUCD38               = 'phot.flux;em.line.Hbeta'
* TCOMM38              = 'Extinction-corrected Hbeta flux'
* TUCD39               = 'phot.flux;em.line.OIII'
* TCOMM39              = 'Extinction-corrected [O III] 5006 flux'
* TUCD40               = 'phot.flux;em.line.Halpha'
* TCOMM40              = 'Extinction-corrected Halpha flux'
* TUCD41               = 'phot.flux;em.line'
* TCOMM41              = 'Extinction-corrected [N II] 6583 flux'
* TUCD42               = 'phot.flux;em.line'
* TCOMM42              = 'Extinction-corrected [S II] 6716 flux'
* TUCD43               = 'phot.flux;em.line'
* TCOMM43              = 'Extinction-corrected [S II] 6730 flux'
* TUCD44               = 'phot.flux;em.line'
* TCOMM44              = 'Extinction-corrected [S III] 9068 flux'
* TUCD45               = 'phot.flux;em.line'
* TCOMM45              = 'Extinction-corrected [O I] 6300 flux'
* TUCD46               = 'stat.error;phot.flux;em.line.Hbeta'
* TCOMM46              = 'Uncertainty of extinction-corrected Hbeta flux'
* TUCD47               = 'stat.error;phot.flux;em.line.OIII'
* TCOMM47              = 'Uncertainty of extinction-corrected [O III] 5006 flux'
* TUCD48               = 'stat.error;phot.flux;em.line.Halpha'
* TCOMM48              = 'Uncertainty of extinction-corrected Halpha flux'
* TUCD49               = 'stat.error;phot.flux;em.line'
* TCOMM49              = 'Uncertainty of extinction-corrected [N II] 6583 flux'
* TUCD50               = 'stat.error;phot.flux;em.line'
* TCOMM50              = 'Uncertainty of extinction-corrected [S II] 6716 flux'
* TUCD51               = 'stat.error;phot.flux;em.line'
* TCOMM51              = 'Uncertainty of extinction-corrected [S II] 6730 flux'
* TUCD52               = 'stat.error;phot.flux;em.line'
* TCOMM52              = 'Uncertainty of extinction-corrected [S III] 9068 flux'
* TUCD53               = 'stat.error;phot.flux;em.line'
* TCOMM53              = 'Uncertainty of extinction-corrected [O I] 6300 flux'
* TUCD54               = 'phys.abund.z'
* TCOMM54              = 'Gas-phase metallicity'
* TUNIT54              = ''
* TUCD55               = 'stat.error;phys.abund.z'
* TCOMM55              = 'Gas-phase metallicity error'
* TUNIT55              = ''
* TUCD56               = 'meta.code.class'
* TCOMM56              = 'BPT classification using [N II]'
* TUNIT56              = ''
* TUCD57               = 'meta.code.class'
* TCOMM57              = 'BPT classification using [S II]'
* TUNIT57              = ''
* TUCD58               = 'meta.code.class'
* TCOMM58              = 'BPT classification using [O I]'
* TUNIT58              = ''
* TUCD59               = 'meta.code.class'
* TCOMM59              = 'Region environment classification'
* TUNIT59              = ''
* TUCD60               = 'arith.diff;phys.abund.z'
* TCOMM60              = 'Difference in metallicity scaling'
* TUNIT60              = ''
* TUCD61               = 'phys.size'
* TCOMM61              = 'Deprojected galactocentric radius in R25 units'
* TUCD62               = 'phys.size'
* TCOMM62              = 'Deprojected galactocentric radius in Reff units'
* TUCD63               = 'spect.line.eqwidth;em.line.Halpha'
* TCOMM63              = 'Raw equivalent width of Halpha'
* TUCD64               = 'stat.error;spect.line.eqwidth;em.line.Halpha'
* TCOMM64              = 'Uncertainty of raw Halpha EW'
* TUCD65               = 'spect.line.eqwidth;em.line.Hbeta'
* TCOMM65              = 'Raw equivalent width of Hbeta'
* TUCD66               = 'stat.error;spect.line.eqwidth;em.line.Hbeta'
* TCOMM66              = 'Uncertainty of raw Hbeta EW'
* TUCD67               = 'spect.line.eqwidth;em.line.Halpha'
* TCOMM67              = 'Fitted equivalent width of Halpha'
* TUCD68               = 'stat.error;spect.line.eqwidth;em.line.Halpha'
* TCOMM68              = 'Uncertainty of fitted Halpha EW'
* TUCD69               = 'spect.line.eqwidth;em.line.Hbeta'
* TCOMM69              = 'Fitted equivalent width of Hbeta'
* TUCD70               = 'stat.error;spect.line.eqwidth;em.line.Hbeta'
* TCOMM70              = 'Uncertainty of fitted Hbeta EW'
* TUCD71               = 'phys.ionizparam'
* TCOMM71              = 'Log of ionization parameter'
* TUNIT71              = ''
* TUCD72               = 'stat.error;phys.ionizparam'
* TCOMM72              = 'Uncertainty on ionization parameter'
* TUNIT72              = ''
* TUCD73               = 'phys.absorption'
* TCOMM73              = 'Visual extinction (Av)'
* TUCD74               = 'stat.error;phys.absorption'
* TCOMM74              = 'Uncertainty on visual extinction'
* TUCD75               = 'phys.luminosity;em.line.Halpha'
* TCOMM75              = 'Extinction-corrected Halpha luminosity'
* EXTNAME              = 'PHASE3CATALOG'
* TTYPE1               = 'SOURCE_ID'
* TFORM1               = '12A'
* TTYPE2               = 'GAL_NAME'
* TFORM2               = '7A'
* TTYPE3               = 'REGION_ID'
* TFORM3               = 'D'
* TTYPE4               = 'RAJ2000'
* TFORM4               = 'D'
* TUNIT4               = 'deg'
* TTYPE5               = 'DECJ2000'
* TFORM5               = 'D'
* TUNIT5               = 'deg'
* TTYPE6               = 'FLAG_EDGE'
* TFORM6               = 'D'
* TTYPE7               = 'FLAG_STAR'
* TFORM7               = 'D'
* TTYPE8               = 'DEPROJ_PHI'
* TFORM8               = 'D'
* TUNIT8               = 'rad'
* TTYPE9               = 'REGION_AREA'
* TFORM9               = 'D'
* TUNIT9               = 'pix**2'
* TTYPE10              = 'HB4861_FLUX'
* TFORM10              = 'D'
* TUNIT10              = '10**(-20)erg.s**(-1).cm**(-2)'
* TTYPE11              = 'OIII5006_FLUX'
* TFORM11              = 'D'
* TUNIT11              = '10**(-20)erg.s**(-1).cm**(-2)'
* TTYPE12              = 'HA6562_FLUX'
* TFORM12              = 'D'
* TUNIT12              = '10**(-20)erg.s**(-1).cm**(-2)'
* TTYPE13              = 'NII6583_FLUX'
* TFORM13              = 'D'
* TUNIT13              = '10**(-20)erg.s**(-1).cm**(-2)'
* TTYPE14              = 'SII6716_FLUX'
* TFORM14              = 'D'
* TUNIT14              = '10**(-20)erg.s**(-1).cm**(-2)'
* TTYPE15              = 'SII6730_FLUX'
* TFORM15              = 'D'
* TUNIT15              = '10**(-20)erg.s**(-1).cm**(-2)'
* TTYPE16              = 'SIII9068_FLUX'
* TFORM16              = 'D'
* TUNIT16              = '10**(-20)erg.s**(-1).cm**(-2)'
* TTYPE17              = 'OI6300_FLUX'
* TFORM17              = 'D'
* TUNIT17              = '10**(-20)erg.s**(-1).cm**(-2)'
* TTYPE18              = 'HB4861_FLUX_ERR'
* TFORM18              = 'D'
* TUNIT18              = '10**(-20)erg.s**(-1).cm**(-2)'
* TTYPE19              = 'OIII5006_FLUX_ERR'
* TFORM19              = 'D'
* TUNIT19              = '10**(-20)erg.s**(-1).cm**(-2)'
* TTYPE20              = 'HA6562_FLUX_ERR'
* TFORM20              = 'D'
* TUNIT20              = '10**(-20)erg.s**(-1).cm**(-2)'
* TTYPE21              = 'NII6583_FLUX_ERR'
* TFORM21              = 'D'
* TUNIT21              = '10**(-20)erg.s**(-1).cm**(-2)'
* TTYPE22              = 'SII6716_FLUX_ERR'
* TFORM22              = 'D'
* TUNIT22              = '10**(-20)erg.s**(-1).cm**(-2)'
* TTYPE23              = 'SII6730_FLUX_ERR'
* TFORM23              = 'D'
* TUNIT23              = '10**(-20)erg.s**(-1).cm**(-2)'
* TTYPE24              = 'SIII9068_FLUX_ERR'
* TFORM24              = 'D'
* TUNIT24              = '10**(-20)erg.s**(-1).cm**(-2)'
* TTYPE25              = 'OI6300_FLUX_ERR'
* TFORM25              = 'D'
* TUNIT25              = '10**(-20)erg.s**(-1).cm**(-2)'
* TTYPE26              = 'HA6562_SIGMA'
* TFORM26              = 'D'
* TUNIT26              = 'km/s'
* TTYPE27              = 'NII6583_SIGMA'
* TFORM27              = 'D'
* TUNIT27              = 'km/s'
* TTYPE28              = 'OIII5006_SIGMA'
* TFORM28              = 'D'
* TUNIT28              = 'km/s'
* TTYPE29              = 'HA6562_VEL'
* TFORM29              = 'D'
* TUNIT29              = 'km/s'
* TTYPE30              = 'NII6583_VEL'
* TFORM30              = 'D'
* TUNIT30              = 'km/s'
* TTYPE31              = 'OIII5006_VEL'
* TFORM31              = 'D'
* TUNIT31              = 'km/s'
* TTYPE32              = 'HA6562_SIGMA_ERR'
* TFORM32              = 'D'
* TUNIT32              = 'km/s'
* TTYPE33              = 'NII6583_SIGMA_ERR'
* TFORM33              = 'D'
* TUNIT33              = 'km/s'
* TTYPE34              = 'OIII5006_SIGMA_ERR'
* TFORM34              = 'D'
* TUNIT34              = 'km/s'
* TTYPE35              = 'HA6562_VEL_ERR'
* TFORM35              = 'D'
* TUNIT35              = 'km/s'
* TTYPE36              = 'NII6583_VEL_ERR'
* TFORM36              = 'D'
* TUNIT36              = 'km/s'
* TTYPE37              = 'OIII5006_VEL_ERR'
* TFORM37              = 'D'
* TUNIT37              = 'km/s'
* TTYPE38              = 'HB4861_FLUX_CORR'
* TFORM38              = 'D'
* TUNIT38              = '10**(-20)erg.s**(-1).cm**(-2)'
* TTYPE39              = 'OIII5006_FLUX_CORR'
* TFORM39              = 'D'
* TUNIT39              = '10**(-20)erg.s**(-1).cm**(-2)'
* TTYPE40              = 'HA6562_FLUX_CORR'
* TFORM40              = 'D'
* TUNIT40              = '10**(-20)erg.s**(-1).cm**(-2)'
* TTYPE41              = 'NII6583_FLUX_CORR'
* TFORM41              = 'D'
* TUNIT41              = '10**(-20)erg.s**(-1).cm**(-2)'
* TTYPE42              = 'SII6716_FLUX_CORR'
* TFORM42              = 'D'
* TUNIT42              = '10**(-20)erg.s**(-1).cm**(-2)'
* TTYPE43              = 'SII6730_FLUX_CORR'
* TFORM43              = 'D'
* TUNIT43              = '10**(-20)erg.s**(-1).cm**(-2)'
* TTYPE44              = 'SIII9068_FLUX_CORR'
* TFORM44              = 'D'
* TUNIT44              = '10**(-20)erg.s**(-1).cm**(-2)'
* TTYPE45              = 'OI6300_FLUX_CORR'
* TFORM45              = 'D'
* TUNIT45              = '10**(-20)erg.s**(-1).cm**(-2)'
* TTYPE46              = 'HB4861_FLUX_CORR_ERR'
* TFORM46              = 'D'
* TUNIT46              = '10**(-20)erg.s**(-1).cm**(-2)'
* TTYPE47              = 'OIII5006_FLUX_CORR_ERR'
* TFORM47              = 'D'
* TUNIT47              = '10**(-20)erg.s**(-1).cm**(-2)'
* TTYPE48              = 'HA6562_FLUX_CORR_ERR'
* TFORM48              = 'D'
* TUNIT48              = '10**(-20)erg.s**(-1).cm**(-2)'
* TTYPE49              = 'NII6583_FLUX_CORR_ERR'
* TFORM49              = 'D'
* TUNIT49              = '10**(-20)erg.s**(-1).cm**(-2)'
* TTYPE50              = 'SII6716_FLUX_CORR_ERR'
* TFORM50              = 'D'
* TUNIT50              = '10**(-20)erg.s**(-1).cm**(-2)'
* TTYPE51              = 'SII6730_FLUX_CORR_ERR'
* TFORM51              = 'D'
* TUNIT51              = '10**(-20)erg.s**(-1).cm**(-2)'
* TTYPE52              = 'SIII9068_FLUX_CORR_ERR'
* TFORM52              = 'D'
* TUNIT52              = '10**(-20)erg.s**(-1).cm**(-2)'
* TTYPE53              = 'OI6300_FLUX_CORR_ERR'
* TFORM53              = 'D'
* TUNIT53              = '10**(-20)erg.s**(-1).cm**(-2)'
* TTYPE54              = 'MET_SCAL'
* TFORM54              = 'D'
* TTYPE55              = 'MET_SCAL_ERR'
* TFORM55              = 'D'
* TTYPE56              = 'BPT_NII'
* TFORM56              = 'D'
* TTYPE57              = 'BPT_SII'
* TFORM57              = 'D'
* TTYPE58              = 'BPT_OI'
* TFORM58              = 'D'
* TTYPE59              = 'ENVIRONMENT'
* TFORM59              = 'D'
* TTYPE60              = 'DELTA_MET_SCAL'
* TFORM60              = 'D'
* TTYPE61              = 'DEPROJ_R_R25'
* TFORM61              = 'D'
* TUNIT61              = 'arcsec'
* TTYPE62              = 'DEPROJ_R_REFF'
* TFORM62              = 'D'
* TUNIT62              = 'arcsec'
* TTYPE63              = 'EW_HA6562_RAW'
* TFORM63              = 'D'
* TUNIT63              = 'angstrom'
* TTYPE64              = 'EW_HA6562_RAW_ERR'
* TFORM64              = 'D'
* TUNIT64              = 'angstrom'
* TTYPE65              = 'EW_HB4861_RAW'
* TFORM65              = 'D'
* TUNIT65              = 'angstrom'
* TTYPE66              = 'EW_HB4861_RAW_ERR'
* TFORM66              = 'D'
* TUNIT66              = 'angstrom'
* TTYPE67              = 'EW_HA6562_FIT'
* TFORM67              = 'D'
* TUNIT67              = 'angstrom'
* TTYPE68              = 'EW_HA6562_FIT_ERR'
* TFORM68              = 'D'
* TUNIT68              = 'angstrom'
* TTYPE69              = 'EW_HB4861_FIT'
* TFORM69              = 'D'
* TUNIT69              = 'angstrom'
* TTYPE70              = 'EW_HB4861_FIT_ERR'
* TFORM70              = 'D'
* TUNIT70              = 'angstrom'
* TTYPE71              = 'LOGU'
* TFORM71              = 'D'
* TTYPE72              = 'LOGU_ERR'
* TFORM72              = 'D'
* TTYPE73              = 'AV'
* TFORM73              = 'D'
* TUNIT73              = 'mag'
* TTYPE74              = 'AV_ERR'
* TFORM74              = 'D'
* TUNIT74              = 'mag'
* TTYPE75              = 'HA6562_LUM_CORR'
* TFORM75              = 'D'
* TUNIT75              = 'erg/s'
* CHECKSUM             = 'V7akX4RhV4XhV4Xh'
* DATASUM              = '1426465751'
```
