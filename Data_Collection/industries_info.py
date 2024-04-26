from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from io import StringIO
import pandas as pd

url = 'https://www.idx.co.id/id/data-pasar/data-saham/daftar-saham/'
options = webdriver.ChromeOptions()
options.add_experimental_option('detach',True)
driver = webdriver.Chrome(options=options)
driver.get(url)
wait = WebDriverWait(driver, 100)
sectors = ['Healthcare','Basic Materials','Financials','Transportation & Logistics','Technology','Consumer Non-Cyclicals','Industrials','Energy','Consumer Cyclicals','Properties & Real Estate','Infrastructures']
stock_codes = ['AALI.JK', 'ABBA.JK', 'ABDA.JK', 'ABMM.JK', 'ACES.JK', 'ACST.JK', 'ADCP.JK', 'ADES.JK', 'ADHI.JK', 'ADMF.JK', 'ADMG.JK', 'ADMR.JK', 'ADRO.JK', 'AEGS.JK', 'AGAR.JK', 'AGII.JK', 'AGRO.JK', 'AGRS.JK', 'AHAP.JK', 'AIMS.JK', 'AISA.JK', 'AKKU.JK', 'AKPI.JK', 'AKRA.JK', 'AKSI.JK', 'ALDO.JK', 'ALKA.JK', 'ALMI.JK', 'ALTO.JK', 'AMAG.JK', 'AMAN.JK', 'AMAR.JK', 'AMFG.JK', 'AMIN.JK', 'AMMN.JK', 'AMMS.JK', 'AMOR.JK', 'AMRT.JK', 'ANDI.JK', 'ANJT.JK', 'ANTM.JK', 'APEX.JK', 'APIC.JK', 'APII.JK', 'APLI.JK', 'APLN.JK', 'ARCI.JK', 'ARGO.JK', 'ARII.JK', 'ARKA.JK', 'ARKO.JK', 'ARMY.JK', 'ARNA.JK', 'ARTA.JK', 'ARTI.JK', 'ARTO.JK', 'ASBI.JK', 'ASDM.JK', 'ASGR.JK', 'ASHA.JK', 'ASII.JK', 'ASJT.JK', 'ASLC.JK', 'ASMI.JK', 'ASPI.JK', 'ASRI.JK', 'ASRM.JK', 'ASSA.JK', 'ATAP.JK', 'ATIC.JK', 'AUTO.JK', 'AVIA.JK', 'AWAN.JK', 'AXIO.JK', 'AYAM.JK', 'AYLS.JK', 'BABP.JK', 'BABY.JK', 'BACA.JK', 'BAJA.JK', 'BALI.JK', 'BANK.JK', 'BAPA.JK', 'BAPI.JK', 'BATA.JK', 'BAUT.JK', 'BAYU.JK', 'BBCA.JK', 'BBHI.JK', 'BBKP.JK', 'BBLD.JK', 'BBMD.JK', 'BBNI.JK', 'BBRI.JK', 'BBRM.JK', 'BBSI.JK', 'BBSS.JK', 'BBTN.JK', 'BBYB.JK', 'BCAP.JK', 'BCIC.JK', 'BCIP.JK', 'BDKR.JK', 'BDMN.JK', 'BEBS.JK', 'BEEF.JK', 'BEER.JK', 'BEKS.JK', 'BELI.JK', 'BELL.JK', 'BESS.JK', 'BEST.JK', 'BFIN.JK', 'BGTG.JK', 'BHAT.JK', 'BHIT.JK', 'BIKA.JK', 'BIKE.JK', 'BIMA.JK', 'BINA.JK', 'BINO.JK', 'BIPI.JK', 'BIPP.JK', 'BIRD.JK', 'BISI.JK', 'BJBR.JK', 'BJTM.JK', 'BKDP.JK', 'BKSL.JK', 'BKSW.JK', 'BLTA.JK', 'BLTZ.JK', 'BLUE.JK', 'BMAS.JK', 'BMBL.JK', 'BMHS.JK', 'BMRI.JK', 'BMSR.JK', 'BMTR.JK', 'BNBA.JK', 'BNBR.JK', 'BNGA.JK', 'BNII.JK', 'BNLI.JK', 'BOBA.JK', 'BOGA.JK', 'BOLA.JK', 'BOLT.JK', 'BOSS.JK', 'BPFI.JK', 'BPII.JK', 'BPTR.JK', 'BRAM.JK', 'BREN.JK', 'BRIS.JK', 'BRMS.JK', 'BRNA.JK', 'BRPT.JK', 'BSBK.JK', 'BSDE.JK', 'BSIM.JK', 'BSML.JK', 'BSSR.JK', 'BSWD.JK', 'BTEK.JK', 'BTEL.JK', 'BTON.JK', 'BTPN.JK', 'BTPS.JK', 'BUAH.JK', 'BUDI.JK', 'BUKA.JK', 'BUKK.JK', 'BULL.JK', 'BUMI.JK', 'BUVA.JK', 'BVIC.JK', 'BWPT.JK', 'BYAN.JK', 'CAKK.JK', 'CAMP.JK', 'CANI.JK', 'CARE.JK', 'CARS.JK', 'CASA.JK', 'CASH.JK', 'CASS.JK', 'CBMF.JK', 'CBPE.JK', 'CBRE.JK', 'CBUT.JK', 'CCSI.JK', 'CEKA.JK', 'CENT.JK', 'CFIN.JK', 'CHEM.JK', 'CHIP.JK', 'CINT.JK', 'CITA.JK', 'CITY.JK', 'CLAY.JK', 'CLEO.JK', 'CLPI.JK', 'CMNP.JK', 'CMNT.JK', 'CMPP.JK', 'CMRY.JK', 'CNKO.JK', 'CNMA.JK', 'CNTX.JK', 'COAL.JK', 'COCO.JK', 'COWL.JK', 'CPIN.JK', 'CPRI.JK', 'CPRO.JK', 'CRAB.JK', 'CRSN.JK', 'CSAP.JK', 'CSIS.JK', 'CSMI.JK', 'CSRA.JK', 'CTBN.JK', 'CTRA.JK', 'CTTH.JK', 'CUAN.JK', 'CYBR.JK', 'DADA.JK', 'DART.JK', 'DAYA.JK', 'DCII.JK', 'DEAL.JK', 'DEFI.JK', 'DEPO.JK', 'DEWA.JK', 'DEWI.JK', 'DFAM.JK', 'DGIK.JK', 'DGNS.JK', 'DIGI.JK', 'DILD.JK', 'DIVA.JK', 'DKFT.JK', 'DLTA.JK', 'DMAS.JK', 'DMMX.JK', 'DMND.JK', 'DNAR.JK', 'DNET.JK', 'DOID.JK', 'DOOH.JK', 'DPNS.JK', 'DPUM.JK', 'DRMA.JK', 'DSFI.JK', 'DSNG.JK', 'DSSA.JK', 'DUCK.JK', 'DUTI.JK', 'DVLA.JK', 'DWGL.JK', 'DYAN.JK', 'EAST.JK', 'ECII.JK', 'EDGE.JK', 'EKAD.JK', 'ELIT.JK', 'ELPI.JK', 'ELSA.JK', 'ELTY.JK', 'EMDE.JK', 'EMTK.JK', 'ENAK.JK', 'ENRG.JK', 'ENVY.JK', 'ENZO.JK', 'EPAC.JK', 'EPMT.JK', 'ERAA.JK', 'ERAL.JK', 'ERTX.JK', 'ESIP.JK', 'ESSA.JK', 'ESTA.JK', 'ESTI.JK', 'ETWA.JK', 'EURO.JK', 'EXCL.JK', 'FAPA.JK', 'FAST.JK', 'FASW.JK', 'FILM.JK', 'FIMP.JK', 'FIRE.JK', 'FISH.JK', 'FITT.JK', 'FLMC.JK', 'FMII.JK', 'FOLK.JK', 'FOOD.JK', 'FORU.JK', 'FORZ.JK', 'FPNI.JK', 'FREN.JK', 'FUJI.JK', 'FUTR.JK', 'FWCT.JK', 'GAMA.JK', 'GDST.JK', 'GDYR.JK', 'GEMA.JK', 'GEMS.JK', 'GGRM.JK', 'GGRP.JK', 'GHON.JK', 'GIAA.JK', 'GJTL.JK', 'GLOB.JK', 'GLVA.JK', 'GMFI.JK', 'GMTD.JK', 'GOLD.JK', 'GOLL.JK', 'GOOD.JK', 'GOTO.JK', 'GPRA.JK', 'GPSO.JK', 'GRIA.JK', 'GRPM.JK', 'GSMF.JK', 'GTBO.JK', 'GTRA.JK', 'GTSI.JK', 'GULA.JK', 'GWSA.JK', 'GZCO.JK', 'HADE.JK', 'HAIS.JK', 'HAJJ.JK', 'HALO.JK', 'HATM.JK', 'HBAT.JK', 'HDFA.JK', 'HDIT.JK', 'HDTX.JK', 'HEAL.JK', 'HELI.JK', 'HERO.JK', 'HEXA.JK', 'HILL.JK', 'HITS.JK', 'HKMU.JK', 'HMSP.JK', 'HOKI.JK', 'HOME.JK', 'HOMI.JK', 'HOPE.JK', 'HOTL.JK', 'HRME.JK', 'HRTA.JK', 'HRUM.JK', 'HUMI.JK', 'IATA.JK', 'IBFN.JK', 'IBOS.JK', 'IBST.JK', 'ICBP.JK', 'ICON.JK', 'IDEA.JK', 'IDPR.JK', 'IFII.JK', 'IFSH.JK', 'IGAR.JK', 'IIKP.JK', 'IKAI.JK', 'IKAN.JK', 'IKBI.JK', 'IKPM.JK', 'IMAS.JK', 'IMJS.JK', 'IMPC.JK', 'INAF.JK', 'INAI.JK', 'INCF.JK', 'INCI.JK', 'INCO.JK', 'INDF.JK', 'INDO.JK', 'INDR.JK', 'INDS.JK', 'INDX.JK', 'INDY.JK', 'INET.JK', 'INKP.JK', 'INOV.JK', 'INPC.JK', 'INPP.JK', 'INPS.JK', 'INRU.JK', 'INTA.JK', 'INTD.JK', 'INTP.JK', 'IOTF.JK', 'IPAC.JK', 'IPCC.JK', 'IPCM.JK', 'IPOL.JK', 'IPPE.JK', 'IPTV.JK', 'IRRA.JK', 'IRSX.JK', 'ISAP.JK', 'ISAT.JK', 'ISSP.JK', 'ITIC.JK', 'ITMA.JK', 'ITMG.JK', 'JARR.JK', 'JAST.JK', 'JATI.JK', 'JAWA.JK', 'JAYA.JK', 'JECC.JK', 'JGLE.JK', 'JIHD.JK', 'JKON.JK', 'JKSW.JK', 'JMAS.JK', 'JPFA.JK', 'JRPT.JK', 'JSKY.JK', 'JSMR.JK', 'JSPT.JK', 'JTPE.JK', 'KAEF.JK', 'KARW.JK', 'KAYU.JK', 'KBAG.JK', 'KBLI.JK', 'KBLM.JK', 'KBLV.JK', 'KBRI.JK', 'KDSI.JK', 'KDTN.JK', 'KEEN.JK', 'KEJU.JK', 'KETR.JK', 'KIAS.JK', 'KICI.JK', 'KIJA.JK', 'KING.JK', 'KINO.JK', 'KIOS.JK', 'KJEN.JK', 'KKES.JK', 'KKGI.JK', 'KLAS.JK', 'KLBF.JK', 'KLIN.JK', 'KMDS.JK', 'KMTR.JK', 'KOBX.JK', 'KOCI.JK', 'KOIN.JK', 'KOKA.JK', 'KONI.JK', 'KOPI.JK', 'KOTA.JK', 'KPAL.JK', 'KPAS.JK', 'KPIG.JK', 'KRAH.JK', 'KRAS.JK', 'KREN.JK', 'KRYA.JK', 'KUAS.JK', 'LABA.JK', 'LAJU.JK', 'LAND.JK', 'LAPD.JK', 'LCGP.JK', 'LCKM.JK', 'LEAD.JK', 'LFLO.JK', 'LIFE.JK', 'LINK.JK', 'LION.JK', 'LMAS.JK', 'LMAX.JK', 'LMPI.JK', 'LMSH.JK', 'LOPI.JK', 'LPCK.JK', 'LPGI.JK', 'LPIN.JK', 'LPKR.JK', 'LPLI.JK', 'LPPF.JK', 'LPPS.JK', 'LRNA.JK', 'LSIP.JK', 'LTLS.JK', 'LUCK.JK', 'LUCY.JK', 'MABA.JK', 'MAGP.JK', 'MAHA.JK', 'MAIN.JK', 'MAMI.JK', 'MAPA.JK', 'MAPB.JK', 'MAPI.JK', 'MARI.JK', 'MARK.JK', 'MASA.JK', 'MASB.JK', 'MAXI.JK', 'MAYA.JK', 'MBAP.JK', 'MBMA.JK', 'MBSS.JK', 'MBTO.JK', 'MCAS.JK', 'MCOL.JK', 'MCOR.JK', 'MDIA.JK', 'MDKA.JK', 'MDKI.JK', 'MDLN.JK', 'MDRN.JK', 'MEDC.JK', 'MEDS.JK', 'MEGA.JK', 'MENN.JK', 'MERK.JK', 'META.JK', 'MFIN.JK', 'MFMI.JK', 'MGLV.JK', 'MGNA.JK', 'MGRO.JK', 'MICE.JK', 'MIDI.JK', 'MIKA.JK', 'MINA.JK', 'MIRA.JK', 'MITI.JK', 'MKNT.JK', 'MKPI.JK', 'MKTR.JK', 'MLBI.JK', 'MLIA.JK', 'MLPL.JK', 'MLPT.JK', 'MMIX.JK', 'MMLP.JK', 'MNCN.JK', 'MOLI.JK', 'MORA.JK', 'MPMX.JK', 'MPOW.JK', 'MPPA.JK', 'MPRO.JK', 'MPXL.JK', 'MRAT.JK', 'MREI.JK', 'MSIE.JK', 'MSIN.JK', 'MSKY.JK', 'MSTI.JK', 'MTDL.JK', 'MTEL.JK', 'MTFN.JK', 'MTLA.JK', 'MTMH.JK', 'MTPS.JK', 'MTRA.JK', 'MTSM.JK', 'MTWI.JK', 'MUTU.JK', 'MYOH.JK', 'MYOR.JK', 'MYRX.JK', 'MYTX.JK', 'NANO.JK', 'NASA.JK', 'NASI.JK', 'NATO.JK', 'NAYZ.JK', 'NCKL.JK', 'NELY.JK', 'NETV.JK', 'NFCX.JK', 'NICK.JK', 'NICL.JK', 'NIKL.JK', 'NINE.JK', 'NIPS.JK', 'NIRO.JK', 'NISP.JK', 'NOBU.JK', 'NPGF.JK', 'NRCA.JK', 'NSSS.JK', 'NTBK.JK', 'NUSA.JK', 'NZIA.JK', 'OASA.JK', 'OBMD.JK', 'OCAP.JK', 'OILS.JK', 'OKAS.JK', 'OLIV.JK', 'OMED.JK', 'OMRE.JK', 'OPMS.JK', 'PACK.JK', 'PADA.JK', 'PADI.JK', 'PALM.JK', 'PAMG.JK', 'PANI.JK', 'PANR.JK', 'PANS.JK', 'PBID.JK', 'PBRX.JK', 'PBSA.JK', 'PCAR.JK', 'PDES.JK', 'PDPP.JK', 'PEGE.JK', 'PEHA.JK', 'PEVE.JK', 'PGAS.JK', 'PGEO.JK', 'PGJO.JK', 'PGLI.JK', 'PGUN.JK', 'PICO.JK', 'PIPA.JK', 'PJAA.JK', 'PKPK.JK', 'PLAN.JK', 'PLAS.JK', 'PLIN.JK', 'PMJS.JK', 'PMMP.JK', 'PNBN.JK', 'PNBS.JK', 'PNGO.JK', 'PNIN.JK', 'PNLF.JK', 'PNSE.JK', 'POLA.JK', 'POLI.JK', 'POLL.JK', 'POLU.JK', 'POLY.JK', 'POOL.JK', 'PORT.JK', 'POSA.JK', 'POWR.JK', 'PPGL.JK', 'PPRE.JK', 'PPRI.JK', 'PPRO.JK', 'PRAS.JK', 'PRAY.JK', 'PRDA.JK', 'PRIM.JK', 'PSAB.JK', 'PSDN.JK', 'PSGO.JK', 'PSKT.JK', 'PSSI.JK', 'PTBA.JK', 'PTDU.JK', 'PTIS.JK', 'PTMP.JK', 'PTPP.JK', 'PTPS.JK', 'PTPW.JK', 'PTRO.JK', 'PTSN.JK', 'PTSP.JK', 'PUDP.JK', 'PURA.JK', 'PURE.JK', 'PURI.JK', 'PWON.JK', 'PYFA.JK', 'PZZA.JK', 'RAAM.JK', 'RAFI.JK', 'RAJA.JK', 'RALS.JK', 'RANC.JK', 'RBMS.JK', 'RCCC.JK', 'RDTX.JK', 'REAL.JK', 'RELF.JK', 'RELI.JK', 'RGAS.JK', 'RICY.JK', 'RIGS.JK', 'RIMO.JK', 'RISE.JK', 'RMKE.JK', 'RMKO.JK', 'ROCK.JK', 'RODA.JK', 'RONY.JK', 'ROTI.JK', 'RSCH.JK', 'RSGK.JK', 'RUIS.JK', 'RUNS.JK', 'SAFE.JK', 'SAGE.JK', 'SAME.JK', 'SAMF.JK', 'SAPX.JK', 'SATU.JK', 'SBAT.JK', 'SBMA.JK', 'SCCO.JK', 'SCMA.JK', 'SCNP.JK', 'SCPI.JK', 'SDMU.JK', 'SDPC.JK', 'SDRA.JK', 'SEMA.JK', 'SFAN.JK', 'SGER.JK', 'SGRO.JK', 'SHID.JK', 'SHIP.JK', 'SICO.JK', 'SIDO.JK', 'SILO.JK', 'SIMA.JK', 'SIMP.JK', 'SINI.JK', 'SIPD.JK', 'SKBM.JK', 'SKLT.JK', 'SKRN.JK', 'SKYB.JK', 'SLIS.JK', 'SMAR.JK', 'SMBR.JK', 'SMCB.JK', 'SMDM.JK', 'SMDR.JK', 'SMGR.JK', 'SMIL.JK', 'SMKL.JK', 'SMKM.JK', 'SMMA.JK', 'SMMT.JK', 'SMRA.JK', 'SMRU.JK', 'SMSM.JK', 'SNLK.JK', 'SOCI.JK', 'SOFA.JK', 'SOHO.JK', 'SONA.JK', 'SOSS.JK', 'SOTS.JK', 'SOUL.JK', 'SPMA.JK', 'SPTO.JK', 'SQMI.JK', 'SRAJ.JK', 'SRIL.JK', 'SRSN.JK', 'SRTG.JK', 'SSIA.JK', 'SSMS.JK', 'SSTM.JK', 'STAA.JK', 'STAR.JK', 'STRK.JK', 'STTP.JK', 'SUGI.JK', 'SULI.JK', 'SUNI.JK', 'SUPR.JK', 'SURE.JK', 'SURI.JK', 'SWAT.JK', 'SWID.JK', 'TALF.JK', 'TAMA.JK', 'TAMU.JK', 'TAPG.JK', 'TARA.JK', 'TAXI.JK', 'TAYS.JK', 'TBIG.JK', 'TBLA.JK', 'TBMS.JK', 'TCID.JK', 'TCPI.JK', 'TDPM.JK', 'TEBE.JK', 'TECH.JK', 'TELE.JK', 'TFAS.JK', 'TFCO.JK', 'TGKA.JK', 'TGRA.JK', 'TGUK.JK', 'TIFA.JK', 'TINS.JK', 'TIRA.JK', 'TIRT.JK', 'TKIM.JK', 'TLDN.JK', 'TLKM.JK', 'TMAS.JK', 'TMPO.JK', 'TNCA.JK', 'TOBA.JK', 'TOOL.JK', 'TOPS.JK', 'TOTL.JK', 'TOTO.JK', 'TOWR.JK', 'TOYS.JK', 'TPIA.JK', 'TPMA.JK', 'TRAM.JK', 'TRGU.JK', 'TRIL.JK', 'TRIM.JK', 'TRIN.JK', 'TRIO.JK', 'TRIS.JK', 'TRJA.JK', 'TRON.JK', 'TRST.JK', 'TRUE.JK', 'TRUK.JK', 'TRUS.JK', 'TSPC.JK', 'TUGU.JK', 'TYRE.JK', 'UANG.JK', 'UCID.JK', 'UDNG.JK', 'UFOE.JK', 'ULTJ.JK', 'UNIC.JK', 'UNIQ.JK', 'UNIT.JK', 'UNSP.JK', 'UNTR.JK', 'UNVR.JK', 'URBN.JK', 'UVCR.JK', 'VAST.JK', 'VICI.JK', 'VICO.JK', 'VINS.JK', 'VIVA.JK', 'VKTR.JK', 'VOKS.JK', 'VRNA.JK', 'VTNY.JK', 'WAPO.JK', 'WEGE.JK', 'WEHA.JK', 'WGSH.JK', 'WICO.JK', 'WIDI.JK', 'WIFI.JK', 'WIIM.JK', 'WIKA.JK', 'WINE.JK', 'WINR.JK', 'WINS.JK', 'WIRG.JK', 'WMPP.JK', 'WMUU.JK', 'WOMF.JK', 'WOOD.JK', 'WOWS.JK', 'WSBP.JK', 'WSKT.JK', 'WTON.JK', 'YELO.JK', 'YPAS.JK', 'YULE.JK', 'ZATA.JK', 'ZBRA.JK', 'ZINC.JK', 'ZONE.JK', 'ZYRX.JK']
# for 1 day
stock_codes = ['AALI.JK', 'ABBA.JK', 'ABDA.JK', 'ABMM.JK', 'ACES.JK', 'ACST.JK', 'ADES.JK', 'ADHI.JK', 'ADMF.JK', 'ADMG.JK', 'ADRO.JK', 'AGII.JK', 'AGRO.JK', 'AGRS.JK', 'AHAP.JK', 'AIMS.JK', 'AISA.JK', 'AKKU.JK', 'AKPI.JK', 'AKRA.JK', 'AKSI.JK', 'ALDO.JK', 'ALKA.JK', 'ALMI.JK', 'ALTO.JK', 'AMAG.JK', 'AMFG.JK', 'AMIN.JK', 'AMRT.JK', 'ANDI.JK', 'ANJT.JK', 'ANTM.JK', 'APEX.JK', 'APIC.JK', 'APII.JK', 'APLI.JK', 'APLN.JK', 'ARGO.JK', 'ARII.JK', 'ARMY.JK', 'ARNA.JK', 'ARTA.JK', 'ARTI.JK', 'ARTO.JK', 'ASBI.JK', 'ASDM.JK', 'ASGR.JK', 'ASII.JK', 'ASJT.JK', 'ASMI.JK', 'ASRI.JK', 'ASRM.JK', 'ASSA.JK', 'ATIC.JK', 'AUTO.JK', 'BABP.JK', 'BACA.JK', 'BAJA.JK', 'BALI.JK', 'BAPA.JK', 'BATA.JK', 'BAYU.JK', 'BBCA.JK', 'BBHI.JK', 'BBKP.JK', 'BBLD.JK', 'BBMD.JK', 'BBNI.JK', 'BBRI.JK', 'BBRM.JK', 'BBTN.JK', 'BBYB.JK', 'BCAP.JK', 'BCIC.JK', 'BCIP.JK', 'BDMN.JK', 'BEKS.JK', 'BELL.JK', 'BEST.JK', 'BFIN.JK', 'BGTG.JK', 'BHIT.JK', 'BIKA.JK', 'BIMA.JK', 'BINA.JK', 'BIPI.JK', 'BIPP.JK', 'BIRD.JK', 'BISI.JK', 'BJBR.JK', 'BJTM.JK', 'BKDP.JK', 'BKSL.JK', 'BKSW.JK', 'BLTA.JK', 'BLTZ.JK', 'BMAS.JK', 'BMRI.JK', 'BMSR.JK', 'BMTR.JK', 'BNBA.JK', 'BNBR.JK', 'BNGA.JK', 'BNII.JK', 'BNLI.JK', 'BOGA.JK', 'BOLT.JK', 'BOSS.JK', 'BPFI.JK', 'BPII.JK', 'BPTR.JK', 'BRAM.JK', 'BRIS.JK', 'BRMS.JK', 'BRNA.JK', 'BRPT.JK', 'BSDE.JK', 'BSIM.JK', 'BSSR.JK', 'BSWD.JK', 'BTEK.JK', 'BTEL.JK', 'BTON.JK', 'BTPN.JK', 'BTPS.JK', 'BUDI.JK', 'BUKK.JK', 'BULL.JK', 'BUMI.JK', 'BUVA.JK', 'BVIC.JK', 'BWPT.JK', 'BYAN.JK', 'CAKK.JK', 'CAMP.JK', 'CANI.JK', 'CARS.JK', 'CASA.JK', 'CASS.JK', 'CEKA.JK', 'CENT.JK', 'CFIN.JK', 'CINT.JK', 'CITA.JK', 'CITY.JK', 'CLEO.JK', 'CLPI.JK', 'CMNP.JK', 'CMPP.JK', 'CNKO.JK', 'CNTX.JK', 'COWL.JK', 'CPIN.JK', 'CPRO.JK', 'CSAP.JK', 'CSIS.JK', 'CTBN.JK', 'CTRA.JK', 'CTTH.JK', 'DART.JK', 'DAYA.JK', 'DEAL.JK', 'DEFI.JK', 'DEWA.JK', 'DFAM.JK', 'DGIK.JK', 'DIGI.JK', 'DILD.JK', 'DIVA.JK', 'DKFT.JK', 'DLTA.JK', 'DMAS.JK', 'DNAR.JK', 'DNET.JK', 'DOID.JK', 'DPNS.JK', 'DPUM.JK', 'DSFI.JK', 'DSNG.JK', 'DSSA.JK', 'DUCK.JK', 'DUTI.JK', 'DVLA.JK', 'DWGL.JK', 'DYAN.JK', 'ECII.JK', 'EKAD.JK', 'ELSA.JK', 'ELTY.JK', 'EMDE.JK', 'EMTK.JK', 'ENRG.JK', 'EPMT.JK', 'ERAA.JK', 'ERTX.JK', 'ESSA.JK', 'ESTI.JK', 'ETWA.JK', 'EXCL.JK', 'FAST.JK', 'FASW.JK', 'FILM.JK', 'FIRE.JK', 'FISH.JK', 'FMII.JK', 'FORU.JK', 'FORZ.JK', 'FPNI.JK', 'FREN.JK', 'GAMA.JK', 'GDST.JK', 'GDYR.JK', 'GEMA.JK', 'GEMS.JK', 'GGRM.JK', 'GHON.JK', 'GIAA.JK', 'GJTL.JK', 'GLOB.JK', 'GMFI.JK', 'GMTD.JK', 'GOLD.JK', 'GOLL.JK', 'GOOD.JK', 'GPRA.JK', 'GSMF.JK', 'GTBO.JK', 'GWSA.JK', 'GZCO.JK', 'HADE.JK', 'HDFA.JK', 'HDTX.JK', 'HEAL.JK', 'HELI.JK', 'HERO.JK', 'HEXA.JK', 'HITS.JK', 'HKMU.JK', 'HMSP.JK', 'HOKI.JK', 'HOME.JK', 'HOTL.JK', 'HRTA.JK', 'HRUM.JK', 'IATA.JK', 'IBFN.JK', 'IBST.JK', 'ICBP.JK', 'ICON.JK', 'IDPR.JK', 'IGAR.JK', 'IIKP.JK', 'IKAI.JK', 'IKBI.JK', 'IMAS.JK', 'IMJS.JK', 'IMPC.JK', 'INAF.JK', 'INAI.JK', 'INCF.JK', 'INCI.JK', 'INCO.JK', 'INDF.JK', 'INDR.JK', 'INDS.JK', 'INDX.JK', 'INDY.JK', 'INKP.JK', 'INPC.JK', 'INPP.JK', 'INPS.JK', 'INRU.JK', 'INTA.JK', 'INTD.JK', 'INTP.JK', 'IPCC.JK', 'IPCM.JK', 'IPOL.JK', 'ISAT.JK', 'ISSP.JK', 'ITMA.JK', 'ITMG.JK', 'JAWA.JK', 'JECC.JK', 'JGLE.JK', 'JIHD.JK', 'JKON.JK', 'JKSW.JK', 'JMAS.JK', 'JPFA.JK', 'JRPT.JK', 'JSKY.JK', 'JSMR.JK', 'JSPT.JK', 'JTPE.JK', 'KAEF.JK', 'KARW.JK', 'KBLI.JK', 'KBLM.JK', 'KBLV.JK', 'KBRI.JK', 'KDSI.JK', 'KIAS.JK', 'KICI.JK', 'KIJA.JK', 'KINO.JK', 'KIOS.JK', 'KKGI.JK', 'KLBF.JK', 'KMTR.JK', 'KOBX.JK', 'KOIN.JK', 'KONI.JK', 'KOPI.JK', 'KPAL.JK', 'KPAS.JK', 'KPIG.JK', 'KRAH.JK', 'KRAS.JK', 'KREN.JK', 'LAND.JK', 'LAPD.JK', 'LCGP.JK', 'LCKM.JK', 'LEAD.JK', 'LINK.JK', 'LION.JK', 'LMAS.JK', 'LMPI.JK', 'LMSH.JK', 'LPCK.JK', 'LPGI.JK', 'LPIN.JK', 'LPKR.JK', 'LPLI.JK', 'LPPF.JK', 'LPPS.JK', 'LRNA.JK', 'LSIP.JK', 'LTLS.JK', 'LUCK.JK', 'MABA.JK', 'MAGP.JK', 'MAIN.JK', 'MAMI.JK', 'MAPA.JK', 'MAPB.JK', 'MAPI.JK', 'MARI.JK', 'MARK.JK', 'MASA.JK', 'MAYA.JK', 'MBAP.JK', 'MBSS.JK', 'MBTO.JK', 'MCAS.JK', 'MCOR.JK', 'MDIA.JK', 'MDKA.JK', 'MDKI.JK', 'MDLN.JK', 'MDRN.JK', 'MEDC.JK', 'MEGA.JK', 'MERK.JK', 'META.JK', 'MFIN.JK', 'MFMI.JK', 'MGNA.JK', 'MGRO.JK', 'MICE.JK', 'MIDI.JK', 'MIKA.JK', 'MINA.JK', 'MIRA.JK', 'MITI.JK', 'MKNT.JK', 'MKPI.JK', 'MLBI.JK', 'MLIA.JK', 'MLPL.JK', 'MLPT.JK', 'MMLP.JK', 'MNCN.JK', 'MOLI.JK', 'MPMX.JK', 'MPOW.JK', 'MPPA.JK', 'MPRO.JK', 'MRAT.JK', 'MREI.JK', 'MSIN.JK', 'MSKY.JK', 'MTDL.JK', 'MTFN.JK', 'MTLA.JK', 'MTRA.JK', 'MTSM.JK', 'MTWI.JK', 'MYOH.JK', 'MYOR.JK', 'MYRX.JK', 'MYTX.JK', 'NASA.JK', 'NELY.JK', 'NFCX.JK', 'NICK.JK', 'NIKL.JK', 'NIPS.JK', 'NIRO.JK', 'NISP.JK', 'NOBU.JK', 'NRCA.JK', 'NUSA.JK', 'OASA.JK', 'OCAP.JK', 'OKAS.JK', 'OMRE.JK', 'PADI.JK', 'PALM.JK', 'PANI.JK', 'PANR.JK', 'PANS.JK', 'PBID.JK', 'PBRX.JK', 'PBSA.JK', 'PCAR.JK', 'PDES.JK', 'PEGE.JK', 'PEHA.JK', 'PGAS.JK', 'PGLI.JK', 'PICO.JK', 'PJAA.JK', 'PKPK.JK', 'PLAS.JK', 'PLIN.JK', 'PNBN.JK', 'PNBS.JK', 'PNIN.JK', 'PNLF.JK', 'PNSE.JK', 'POLA.JK', 'POLL.JK', 'POLY.JK', 'POOL.JK', 'PORT.JK', 'POWR.JK', 'PPRE.JK', 'PPRO.JK', 'PRAS.JK', 'PRDA.JK', 'PRIM.JK', 'PSAB.JK', 'PSDN.JK', 'PSKT.JK', 'PSSI.JK', 'PTBA.JK', 'PTIS.JK', 'PTPP.JK', 'PTRO.JK', 'PTSN.JK', 'PTSP.JK', 'PUDP.JK', 'PWON.JK', 'PYFA.JK', 'PZZA.JK', 'RAJA.JK', 'RALS.JK', 'RANC.JK', 'RBMS.JK', 'RDTX.JK', 'RELI.JK', 'RICY.JK', 'RIGS.JK', 'RIMO.JK', 'RISE.JK', 'RODA.JK', 'ROTI.JK', 'RUIS.JK', 'SAFE.JK', 'SAME.JK', 'SAPX.JK', 'SATU.JK', 'SCCO.JK', 'SCMA.JK', 'SCPI.JK', 'SDMU.JK', 'SDPC.JK', 'SDRA.JK', 'SGRO.JK', 'SHID.JK', 'SHIP.JK', 'SIDO.JK', 'SILO.JK', 'SIMA.JK', 'SIMP.JK', 'SIPD.JK', 'SKBM.JK', 'SKLT.JK', 'SKRN.JK', 'SKYB.JK', 'SMAR.JK', 'SMBR.JK', 'SMCB.JK', 'SMDM.JK', 'SMDR.JK', 'SMGR.JK', 'SMMA.JK', 'SMMT.JK', 'SMRA.JK', 'SMRU.JK', 'SMSM.JK', 'SOCI.JK', 'SONA.JK', 'SOSS.JK', 'SOTS.JK', 'SPMA.JK', 'SPTO.JK', 'SQMI.JK', 'SRAJ.JK', 'SRIL.JK', 'SRSN.JK', 'SRTG.JK', 'SSIA.JK', 'SSMS.JK', 'SSTM.JK', 'STAR.JK', 'STTP.JK', 'SUGI.JK', 'SULI.JK', 'SUPR.JK', 'SURE.JK', 'SWAT.JK', 'TALF.JK', 'TAMU.JK', 'TARA.JK', 'TAXI.JK', 'TBIG.JK', 'TBLA.JK', 'TBMS.JK', 'TCID.JK', 'TCPI.JK', 'TDPM.JK', 'TELE.JK', 'TFCO.JK', 'TGKA.JK', 'TGRA.JK', 'TIFA.JK', 'TINS.JK', 'TIRA.JK', 'TIRT.JK', 'TKIM.JK', 'TLKM.JK', 'TMAS.JK', 'TMPO.JK', 'TNCA.JK', 'TOBA.JK', 'TOPS.JK', 'TOTL.JK', 'TOTO.JK', 'TOWR.JK', 'TPIA.JK', 'TPMA.JK', 'TRAM.JK', 'TRIL.JK', 'TRIM.JK', 'TRIO.JK', 'TRIS.JK', 'TRST.JK', 'TRUK.JK', 'TRUS.JK', 'TSPC.JK', 'TUGU.JK', 'ULTJ.JK', 'UNIC.JK', 'UNIT.JK', 'UNSP.JK', 'UNTR.JK', 'UNVR.JK', 'URBN.JK', 'VICO.JK', 'VINS.JK', 'VIVA.JK', 'VOKS.JK', 'VRNA.JK', 'WAPO.JK', 'WEGE.JK', 'WEHA.JK', 'WICO.JK', 'WIIM.JK', 'WIKA.JK', 'WINS.JK', 'WOMF.JK', 'WOOD.JK', 'WSBP.JK', 'WSKT.JK', 'WTON.JK', 'YELO.JK', 'YPAS.JK', 'YULE.JK', 'ZBRA.JK', 'ZINC.JK', 'ZONE.JK']


dict_industries = {}
dict_shares = {}
for sector in sectors:
    input_elements = driver.find_elements(By.TAG_NAME,'input')
    sector_element = input_elements[2]
    sector_element.clear()
    sector_element.send_keys(sector)
    sector_element.send_keys(Keys.ENTER)
    select_element = wait.until(EC.presence_of_element_located((By.TAG_NAME, 'select')))
    select = Select(select_element)
    select.select_by_visible_text('All')
    table_element = wait.until(EC.presence_of_element_located((By.TAG_NAME,'table')))
    table_html = table_element.get_attribute('outerHTML')
    df = pd.read_html(StringIO(table_html))[0]
    # print(df.columns)
    shares_in_market = df['Saham Sort table by Saham in descending order'].to_list()
    shares_clean = [f'{str(share).replace('.','')}' for share in shares_in_market]
    codes = df['Kode Sort table by Kode in descending order'].to_list()
    jk_codes = [f'{code}.JK' for code in codes if f'{code}.JK' in stock_codes]
    dict_industries[sector]=jk_codes
    dict_shares[sector]=shares_clean
# print(dict_industries)
print(dict_shares)
