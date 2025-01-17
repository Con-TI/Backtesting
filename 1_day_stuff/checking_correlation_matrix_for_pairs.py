import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import statsmodels.api as sm

# stock_codes = ['AALI.JK', 'ABBA.JK', 'ABDA.JK', 'ABMM.JK', 'ACES.JK', 'ACST.JK', 'ADCP.JK', 'ADES.JK', 'ADHI.JK',
#                'ADMF.JK', 'ADMG.JK', 'ADMR.JK', 'ADRO.JK', 'AEGS.JK', 'AGAR.JK', 'AGII.JK', 'AGRO.JK', 'AGRS.JK',
#                'AHAP.JK', 'AIMS.JK', 'AISA.JK', 'AKKU.JK', 'AKPI.JK', 'AKRA.JK', 'AKSI.JK', 'ALDO.JK', 'ALKA.JK',
#                'ALMI.JK', 'ALTO.JK', 'AMAG.JK', 'AMAN.JK', 'AMAR.JK', 'AMFG.JK', 'AMIN.JK', 'AMMN.JK', 'AMMS.JK',
#                'AMOR.JK', 'AMRT.JK', 'ANDI.JK', 'ANJT.JK', 'ANTM.JK', 'APEX.JK', 'APIC.JK', 'APII.JK', 'APLI.JK',
#                'APLN.JK', 'ARCI.JK', 'ARGO.JK', 'ARII.JK', 'ARKA.JK', 'ARKO.JK', 'ARNA.JK', 'ARTA.JK', 'ARTI.JK',
#                'ARTO.JK', 'ASBI.JK', 'ASDM.JK', 'ASGR.JK', 'ASHA.JK', 'ASII.JK', 'ASJT.JK', 'ASLC.JK', 'ASMI.JK',
#                'ASPI.JK', 'ASRI.JK', 'ASRM.JK', 'ASSA.JK', 'ATAP.JK', 'ATIC.JK', 'AUTO.JK', 'AVIA.JK', 'AWAN.JK',
#                'AXIO.JK', 'AYAM.JK', 'AYLS.JK', 'BABP.JK', 'BABY.JK', 'BACA.JK', 'BAJA.JK', 'BALI.JK', 'BANK.JK',
#                'BAPA.JK', 'BATA.JK', 'BAUT.JK', 'BAYU.JK', 'BBCA.JK', 'BBHI.JK', 'BBKP.JK', 'BBLD.JK', 'BBMD.JK',
#                'BBNI.JK', 'BBRI.JK', 'BBRM.JK', 'BBSI.JK', 'BBSS.JK', 'BBTN.JK', 'BBYB.JK', 'BCAP.JK', 'BCIC.JK',
#                'BCIP.JK', 'BDKR.JK', 'BDMN.JK', 'BEBS.JK', 'BEEF.JK', 'BEER.JK', 'BEKS.JK', 'BELI.JK', 'BELL.JK',
#                'BESS.JK', 'BEST.JK', 'BFIN.JK', 'BGTG.JK', 'BHAT.JK', 'BHIT.JK', 'BIKA.JK', 'BIKE.JK', 'BIMA.JK',
#                'BINA.JK', 'BINO.JK', 'BIPI.JK', 'BIPP.JK', 'BIRD.JK', 'BISI.JK', 'BJBR.JK', 'BJTM.JK', 'BKDP.JK',
#                'BKSL.JK', 'BKSW.JK', 'BLTA.JK', 'BLTZ.JK', 'BLUE.JK', 'BMAS.JK', 'BMBL.JK', 'BMHS.JK', 'BMRI.JK',
#                'BMSR.JK', 'BMTR.JK', 'BNBA.JK', 'BNBR.JK', 'BNGA.JK', 'BNII.JK', 'BNLI.JK', 'BOBA.JK', 'BOGA.JK',
#                'BOLA.JK', 'BOLT.JK', 'BPFI.JK', 'BPII.JK', 'BPTR.JK', 'BRAM.JK', 'BREN.JK', 'BRIS.JK', 'BRMS.JK',
#                'BRNA.JK', 'BRPT.JK', 'BSBK.JK', 'BSDE.JK', 'BSIM.JK', 'BSML.JK', 'BSSR.JK', 'BSWD.JK', 'BTEK.JK',
#                'BTON.JK', 'BTPN.JK', 'BTPS.JK', 'BUAH.JK', 'BUDI.JK', 'BUKA.JK', 'BUKK.JK', 'BULL.JK', 'BUMI.JK',
#                'BUVA.JK', 'BVIC.JK', 'BWPT.JK', 'BYAN.JK', 'CAKK.JK', 'CAMP.JK', 'CANI.JK', 'CARE.JK', 'CARS.JK',
#                'CASA.JK', 'CASH.JK', 'CASS.JK', 'CBPE.JK', 'CBRE.JK', 'CBUT.JK', 'CCSI.JK', 'CEKA.JK', 'CENT.JK',
#                'CFIN.JK', 'CHEM.JK', 'CHIP.JK', 'CINT.JK', 'CITA.JK', 'CITY.JK', 'CLEO.JK', 'CLPI.JK', 'CMNP.JK',
#                'CMNT.JK', 'CMPP.JK', 'CMRY.JK', 'CNKO.JK', 'CNMA.JK', 'CNTX.JK', 'COAL.JK', 'COCO.JK', 'CPIN.JK',
#                'CPRO.JK', 'CRAB.JK', 'CRSN.JK', 'CSAP.JK', 'CSIS.JK', 'CSMI.JK', 'CSRA.JK', 'CTBN.JK', 'CTRA.JK',
#                'CTTH.JK', 'CUAN.JK', 'CYBR.JK', 'DADA.JK', 'DART.JK', 'DAYA.JK', 'DCII.JK', 'DEPO.JK', 'DEWA.JK',
#                'DEWI.JK', 'DFAM.JK', 'DGIK.JK', 'DGNS.JK', 'DIGI.JK', 'DILD.JK', 'DIVA.JK', 'DKFT.JK', 'DLTA.JK',
#                'DMAS.JK', 'DMMX.JK', 'DMND.JK', 'DNAR.JK', 'DNET.JK', 'DOID.JK', 'DOOH.JK', 'DPNS.JK', 'DPUM.JK',
#                'DRMA.JK', 'DSFI.JK', 'DSNG.JK', 'DSSA.JK', 'DUTI.JK', 'DVLA.JK', 'DWGL.JK', 'DYAN.JK', 'EAST.JK',
#                'ECII.JK', 'EDGE.JK', 'EKAD.JK', 'ELIT.JK', 'ELPI.JK', 'ELSA.JK', 'ELTY.JK', 'EMDE.JK', 'EMTK.JK',
#                'ENAK.JK', 'ENRG.JK', 'ENZO.JK', 'EPAC.JK', 'EPMT.JK', 'ERAA.JK', 'ERAL.JK', 'ERTX.JK', 'ESIP.JK',
#                'ESSA.JK', 'ESTA.JK', 'ESTI.JK', 'EURO.JK', 'EXCL.JK', 'FAPA.JK', 'FAST.JK', 'FASW.JK', 'FILM.JK',
#                'FIMP.JK', 'FIRE.JK', 'FISH.JK', 'FITT.JK', 'FLMC.JK', 'FMII.JK', 'FOLK.JK', 'FOOD.JK', 'FPNI.JK',
#                'FREN.JK', 'FUJI.JK', 'FUTR.JK', 'FWCT.JK', 'GDST.JK', 'GDYR.JK', 'GEMA.JK', 'GEMS.JK', 'GGRM.JK',
#                'GGRP.JK', 'GHON.JK', 'GIAA.JK', 'GJTL.JK', 'GLOB.JK', 'GLVA.JK', 'GMFI.JK', 'GMTD.JK', 'GOLD.JK',
#                'GOOD.JK', 'GOTO.JK', 'GPRA.JK', 'GPSO.JK', 'GRIA.JK', 'GRPM.JK', 'GSMF.JK', 'GTBO.JK', 'GTRA.JK',
#                'GTSI.JK', 'GULA.JK', 'GWSA.JK', 'GZCO.JK', 'HADE.JK', 'HAIS.JK', 'HAJJ.JK', 'HALO.JK', 'HATM.JK',
#                'HBAT.JK', 'HDFA.JK', 'HDIT.JK', 'HEAL.JK', 'HELI.JK', 'HERO.JK', 'HEXA.JK', 'HILL.JK', 'HITS.JK',
#                'HMSP.JK', 'HOKI.JK', 'HOMI.JK', 'HOPE.JK', 'HRME.JK', 'HRTA.JK', 'HRUM.JK', 'HUMI.JK', 'IATA.JK',
#                'IBFN.JK', 'IBOS.JK', 'IBST.JK', 'ICBP.JK', 'ICON.JK', 'IDEA.JK', 'IDPR.JK', 'IFII.JK', 'IFSH.JK',
#                'IGAR.JK', 'IKAI.JK', 'IKAN.JK', 'IKBI.JK', 'IKPM.JK', 'IMAS.JK', 'IMJS.JK', 'IMPC.JK', 'INAF.JK',
#                'INAI.JK', 'INCF.JK', 'INCI.JK', 'INCO.JK', 'INDF.JK', 'INDO.JK', 'INDR.JK', 'INDS.JK', 'INDX.JK',
#                'INDY.JK', 'INET.JK', 'INKP.JK', 'INOV.JK', 'INPC.JK', 'INPP.JK', 'INPS.JK', 'INRU.JK', 'INTA.JK',
#                'INTD.JK', 'INTP.JK', 'IOTF.JK', 'IPAC.JK', 'IPCC.JK', 'IPCM.JK', 'IPOL.JK', 'IPPE.JK', 'IPTV.JK',
#                'IRRA.JK', 'IRSX.JK', 'ISAP.JK', 'ISAT.JK', 'ISSP.JK', 'ITIC.JK', 'ITMA.JK', 'ITMG.JK', 'JARR.JK',
#                'JAST.JK', 'JATI.JK', 'JAWA.JK', 'JAYA.JK', 'JECC.JK', 'JGLE.JK', 'JIHD.JK', 'JKON.JK', 'JMAS.JK',
#                'JPFA.JK', 'JRPT.JK', 'JSMR.JK', 'JSPT.JK', 'JTPE.JK', 'KAEF.JK', 'KARW.JK', 'KAYU.JK', 'KBAG.JK',
#                'KBLI.JK', 'KBLM.JK', 'KBLV.JK', 'KDSI.JK', 'KDTN.JK', 'KEEN.JK', 'KEJU.JK', 'KETR.JK', 'KIAS.JK',
#                'KICI.JK', 'KIJA.JK', 'KING.JK', 'KINO.JK', 'KIOS.JK', 'KJEN.JK', 'KKES.JK', 'KKGI.JK', 'KLAS.JK',
#                'KLBF.JK', 'KLIN.JK', 'KMDS.JK', 'KMTR.JK', 'KOBX.JK', 'KOCI.JK', 'KOIN.JK', 'KOKA.JK', 'KONI.JK',
#                'KOPI.JK', 'KOTA.JK', 'KPIG.JK', 'KRAS.JK', 'KREN.JK', 'KRYA.JK', 'KUAS.JK', 'LABA.JK', 'LAJU.JK',
#                'LAND.JK', 'LAPD.JK', 'LCKM.JK', 'LEAD.JK', 'LFLO.JK', 'LIFE.JK', 'LINK.JK', 'LION.JK', 'LMAX.JK',
#                'LMPI.JK', 'LMSH.JK', 'LOPI.JK', 'LPCK.JK', 'LPGI.JK', 'LPIN.JK', 'LPKR.JK', 'LPLI.JK', 'LPPF.JK',
#                'LPPS.JK', 'LRNA.JK', 'LSIP.JK', 'LTLS.JK', 'LUCK.JK', 'LUCY.JK', 'MAHA.JK', 'MAIN.JK', 'MAPA.JK',
#                'MAPB.JK', 'MAPI.JK', 'MARI.JK', 'MARK.JK', 'MASA.JK', 'MASB.JK', 'MAXI.JK', 'MAYA.JK', 'MBAP.JK',
#                'MBMA.JK', 'MBSS.JK', 'MBTO.JK', 'MCAS.JK', 'MCOL.JK', 'MCOR.JK', 'MDIA.JK', 'MDKA.JK', 'MDKI.JK',
#                'MDLN.JK', 'MDRN.JK', 'MEDC.JK', 'MEDS.JK', 'MEGA.JK', 'MENN.JK', 'MERK.JK', 'MFIN.JK', 'MFMI.JK',
#                'MGLV.JK', 'MGNA.JK', 'MGRO.JK', 'MICE.JK', 'MIDI.JK', 'MIKA.JK', 'MINA.JK', 'MIRA.JK', 'MITI.JK',
#                'MKNT.JK', 'MKPI.JK', 'MKTR.JK', 'MLBI.JK', 'MLIA.JK', 'MLPL.JK', 'MLPT.JK', 'MMIX.JK', 'MMLP.JK',
#                'MNCN.JK', 'MOLI.JK', 'MORA.JK', 'MPMX.JK', 'MPOW.JK', 'MPPA.JK', 'MPRO.JK', 'MPXL.JK', 'MRAT.JK',
#                'MREI.JK', 'MSIE.JK', 'MSIN.JK', 'MSKY.JK', 'MSTI.JK', 'MTDL.JK', 'MTEL.JK', 'MTLA.JK', 'MTMH.JK',
#                'MTPS.JK', 'MTSM.JK', 'MTWI.JK', 'MUTU.JK', 'MYOH.JK', 'MYOR.JK', 'MYTX.JK', 'NANO.JK', 'NASA.JK',
#                'NASI.JK', 'NATO.JK', 'NAYZ.JK', 'NCKL.JK', 'NELY.JK', 'NETV.JK', 'NFCX.JK', 'NICK.JK', 'NICL.JK',
#                'NIKL.JK', 'NINE.JK', 'NIRO.JK', 'NISP.JK', 'NOBU.JK', 'NPGF.JK', 'NRCA.JK', 'NSSS.JK', 'NTBK.JK',
#                'NZIA.JK', 'OASA.JK', 'OBMD.JK', 'OILS.JK', 'OKAS.JK', 'OLIV.JK', 'OMED.JK', 'OMRE.JK', 'OPMS.JK',
#                'PACK.JK', 'PADA.JK', 'PADI.JK', 'PALM.JK', 'PAMG.JK', 'PANI.JK', 'PANR.JK', 'PANS.JK', 'PBID.JK',
#                'PBRX.JK', 'PBSA.JK', 'PCAR.JK', 'PDES.JK', 'PDPP.JK', 'PEGE.JK', 'PEHA.JK', 'PEVE.JK', 'PGAS.JK',
#                'PGEO.JK', 'PGJO.JK', 'PGLI.JK', 'PGUN.JK', 'PICO.JK', 'PIPA.JK', 'PJAA.JK', 'PKPK.JK', 'PLAN.JK',
#                'PLIN.JK', 'PMJS.JK', 'PMMP.JK', 'PNBN.JK', 'PNBS.JK', 'PNGO.JK', 'PNIN.JK', 'PNLF.JK', 'POLA.JK',
#                'POLI.JK', 'POLL.JK', 'POLU.JK', 'POLY.JK', 'PORT.JK', 'POWR.JK', 'PPGL.JK', 'PPRE.JK', 'PPRI.JK',
#                'PPRO.JK', 'PRAY.JK', 'PRDA.JK', 'PRIM.JK', 'PSAB.JK', 'PSDN.JK', 'PSGO.JK', 'PSKT.JK', 'PSSI.JK',
#                'PTBA.JK', 'PTDU.JK', 'PTIS.JK', 'PTMP.JK', 'PTPP.JK', 'PTPS.JK', 'PTPW.JK', 'PTRO.JK', 'PTSN.JK',
#                'PTSP.JK', 'PUDP.JK', 'PURA.JK', 'PURI.JK', 'PWON.JK', 'PYFA.JK', 'PZZA.JK', 'RAAM.JK', 'RAFI.JK',
#                'RAJA.JK', 'RALS.JK', 'RANC.JK', 'RBMS.JK', 'RCCC.JK', 'RDTX.JK', 'REAL.JK', 'RELF.JK', 'RELI.JK',
#                'RGAS.JK', 'RICY.JK', 'RIGS.JK', 'RISE.JK', 'RMKE.JK', 'RMKO.JK', 'ROCK.JK', 'RODA.JK', 'RONY.JK',
#                'ROTI.JK', 'RSCH.JK', 'RSGK.JK', 'RUIS.JK', 'RUNS.JK', 'SAFE.JK', 'SAGE.JK', 'SAME.JK', 'SAMF.JK',
#                'SAPX.JK', 'SATU.JK', 'SBAT.JK', 'SBMA.JK', 'SCCO.JK', 'SCMA.JK', 'SCNP.JK', 'SCPI.JK', 'SDMU.JK',
#                'SDPC.JK', 'SDRA.JK', 'SEMA.JK', 'SFAN.JK', 'SGER.JK', 'SGRO.JK', 'SHID.JK', 'SHIP.JK', 'SICO.JK',
#                'SIDO.JK', 'SILO.JK', 'SIMP.JK', 'SINI.JK', 'SIPD.JK', 'SKBM.JK', 'SKLT.JK', 'SKRN.JK', 'SLIS.JK',
#                'SMAR.JK', 'SMBR.JK', 'SMCB.JK', 'SMDM.JK', 'SMDR.JK', 'SMGR.JK', 'SMIL.JK', 'SMKL.JK', 'SMKM.JK',
#                'SMMA.JK', 'SMMT.JK', 'SMRA.JK', 'SMSM.JK', 'SNLK.JK', 'SOCI.JK', 'SOFA.JK', 'SOHO.JK', 'SONA.JK',
#                'SOSS.JK', 'SOTS.JK', 'SOUL.JK', 'SPMA.JK', 'SPTO.JK', 'SQMI.JK', 'SRAJ.JK', 'SRSN.JK', 'SRTG.JK',
#                'SSIA.JK', 'SSMS.JK', 'SSTM.JK', 'STAA.JK', 'STAR.JK', 'STRK.JK', 'STTP.JK', 'SULI.JK', 'SUNI.JK',
#                'SURE.JK', 'SURI.JK', 'SWAT.JK', 'SWID.JK', 'TALF.JK', 'TAMA.JK', 'TAPG.JK', 'TARA.JK', 'TAXI.JK',
#                'TAYS.JK', 'TBIG.JK', 'TBLA.JK', 'TBMS.JK', 'TCID.JK', 'TCPI.JK', 'TEBE.JK', 'TELE.JK', 'TFAS.JK',
#                'TFCO.JK', 'TGKA.JK', 'TGRA.JK', 'TGUK.JK', 'TIFA.JK', 'TINS.JK', 'TIRA.JK', 'TIRT.JK', 'TKIM.JK',
#                'TLDN.JK', 'TLKM.JK', 'TMAS.JK', 'TMPO.JK', 'TNCA.JK', 'TOBA.JK', 'TOOL.JK', 'TOPS.JK', 'TOTL.JK',
#                'TOTO.JK', 'TOWR.JK', 'TOYS.JK', 'TPIA.JK', 'TPMA.JK', 'TRGU.JK', 'TRIM.JK', 'TRIN.JK', 'TRIS.JK',
#                'TRJA.JK', 'TRON.JK', 'TRST.JK', 'TRUE.JK', 'TRUK.JK', 'TRUS.JK', 'TSPC.JK', 'TUGU.JK', 'TYRE.JK',
#                'UANG.JK', 'UCID.JK', 'UDNG.JK', 'UFOE.JK', 'ULTJ.JK', 'UNIC.JK', 'UNIQ.JK', 'UNSP.JK', 'UNTR.JK',
#                'UNVR.JK', 'URBN.JK', 'UVCR.JK', 'VAST.JK', 'VICI.JK', 'VICO.JK', 'VINS.JK', 'VIVA.JK', 'VKTR.JK',
#                'VOKS.JK', 'VRNA.JK', 'VTNY.JK', 'WAPO.JK', 'WEGE.JK', 'WEHA.JK', 'WGSH.JK', 'WICO.JK', 'WIDI.JK',
#                'WIFI.JK', 'WIIM.JK', 'WINE.JK', 'WINR.JK', 'WINS.JK', 'WIRG.JK', 'WMPP.JK', 'WMUU.JK', 'WOMF.JK',
#                'WOOD.JK', 'WOWS.JK', 'WSBP.JK', 'WTON.JK', 'YELO.JK', 'YPAS.JK', 'YULE.JK', 'ZATA.JK', 'ZBRA.JK',
#                'ZINC.JK', 'ZONE.JK', 'ZYRX.JK']

filtered_data = pd.read_pickle('../Data_Collection/clean_data_1day.pkl')
# Clean data contains 5minute price data for the stocks in stock_codes
close_prices = filtered_data['Close']
percentage_changes_1step = close_prices.pct_change(periods=1)


# 3.TODO organising data (remove stocks that don't move much and stocks with long flat portions)
def has_consecutive_repeats(column, num_of_repeat):
    prev_value = None
    consecutive_count = 1
    for value in column:
        if value == prev_value:
            consecutive_count += 1
            if consecutive_count > num_of_repeat:
                return True
        else:
            consecutive_count = 1
        prev_value = value
    return False


list_of_flat_stocks = []
for column in close_prices.columns:
    current_series = close_prices[column]
    if has_consecutive_repeats(current_series, 70):
        list_of_flat_stocks.append(column)
# print(len(list_of_flat_stocks))
percentage_changes_1step = percentage_changes_1step.drop(columns=list_of_flat_stocks)


# 3.TODO lagged correlation matrix
# lagged_df = pd.concat([percentage_changes_1step.shift(i) for i in range(20)], axis=1)
# lagged_df.columns = [f'{col}_lag{i}' for col in percentage_changes_1step.columns for i in range(20)]
# corr = lagged_df.corr(method='pearson')
# corr = corr.dropna(how='all', axis=0)
# corr = corr.dropna(how='all', axis=1)


# 1.TODO Finding heatmap of correlation matrix of 1step percent changes (trying to find correlated stocks)
# rows = percentage_changes_1step.shape[0]
# storage = []
# for m in range(5,101,5):
#     for n in range(0,rows+1, round(rows/m)):
#         selected = percentage_changes_1step[n:(n+round(rows/m))]
#         storage.append(selected.std())
# std_dev = pd.concat(storage, axis=1).mean(axis=1)
# # no_volatility = list(std_dev[std_dev==0].index)
# have_volatility = std_dev[std_dev != 0].sort_values(ascending=True)
# for stock in list(have_volatility.index):
#     std = have_volatility[stock]
#     plt.plot(close_prices.index,close_prices[stock].values)
#     plt.title(f'{stock}, {std}')
#     plt.show()
# percentage_changes_1step = percentage_changes_1step.drop(columns=have_volatility.index)
corr = percentage_changes_1step.corr(method='pearson')
corr = corr.dropna(how='all', axis=0)
corr = corr.dropna(how='all', axis=1)
up_threshold = 0.4
low_threshold = -0.4
pos_corr_pairs = []
neg_corr_pairs = []
for i, col1 in enumerate(corr.columns):
    for j, col2 in enumerate(corr.columns):
        if i < j:
            corr_value = corr.loc[col1, col2]
            if corr_value > up_threshold:
                pos_corr_pairs.append((col1, col2, corr_value))
            elif corr_value < low_threshold:
                neg_corr_pairs.append((col1, col2, corr_value))
print(pos_corr_pairs)
print(neg_corr_pairs)
print(len(pos_corr_pairs))
print(len(neg_corr_pairs))
# plt.figure(figsize=(8, 6))  # Set the figure size
# sns.heatmap(corr, cmap='viridis')
# plt.show()


# 4.TODO Plotting pairs without lag
for pair in pos_corr_pairs:
    figure = plt.figure(figsize=(10,6))
    grid = plt.GridSpec(nrows=3,ncols=2)
    series1 = close_prices[pair[0]].reset_index(drop=True)
    series2 = close_prices[pair[1]].reset_index(drop=True)
    ax1 = figure.add_subplot(grid[0,0])
    ax1.plot(series1.index, series1.values,color='b')
    ax2 = ax1.twinx()
    ax2.plot(series2.index, series2.values, color='r')
    ax1.set_xlabel('time')
    ax1.set_ylabel(f'price {pair[0]}')
    ax2.set_ylabel(f'price {pair[1]}')
    ax1.set_title(f'Blue: {pair[0]}, Red: {pair[1]}, Corr: {pair[2]}')
    change_since_start_1 = (series1 / series1.iloc[0]) - 1
    change_since_start_2 = (series2 / series2.iloc[0]) - 1
    ax3 = figure.add_subplot(grid[1,0])
    ax3.plot(change_since_start_1.index,change_since_start_1.values,color='b')
    ax3.plot(change_since_start_2.index,change_since_start_2.values,color='r')
    ax3.set_xlabel('time')
    ax3.set_ylabel('Change Since Start')
    ax3.axhline(0, linestyle='--', color='y')
    diff_between_series = change_since_start_1-change_since_start_2
    ax4 = figure.add_subplot(grid[2,0])
    ax4.plot(diff_between_series.index,diff_between_series.values,color='k')
    ax4.set_xlabel('time')
    ax4.set_ylabel('diff_between_stocks')
    ax4.axhline(0, linestyle='--', color='y')

    ax5 = figure.add_subplot(grid[0,1])
    X1 = sm.add_constant(series1)
    model1 = sm.OLS(series2, X1).fit()
    residuals_series = pd.Series(model1.resid,index=series1.index)
    ax5.plot(residuals_series.index,residuals_series.values)
    ax5.set_ylabel('Residuals of Asset Prices')

    ax6 = figure.add_subplot(grid[1,1])
    log_series_1 = (series1.pct_change())[1:]
    print(log_series_1)
    log_series_2 = (series2.pct_change())[1:]
    X2 = sm.add_constant(log_series_1)
    model2 = sm.OLS(log_series_2,X2).fit()
    residuals_series_log = pd.Series(model2.resid,index=change_since_start_1.index)
    ax6.plot(residuals_series_log.index,residuals_series_log.values)
    ax6.set_ylabel('Residuals of log prices')

    plt.tight_layout()
    plt.show()
for pair in neg_corr_pairs:
    figure,ax1 = plt.subplots(figsize=(10,6))
    series1 = close_prices[pair[0]].reset_index(drop=True)
    series2 = close_prices[pair[1]].reset_index(drop=True)
    ax1.plot(series1.index, series1.values,color='b')
    ax2 = ax1.twinx()
    ax2.plot(series2.index, series2.values, color='r')
    plt.xlabel('time')
    plt.ylabel('price')
    plt.title(f'Blue: {pair[0]}, Red: {pair[1]}, Corr: {pair[2]}')
    plt.show()

# 5.TODO Plotting pairs with lag
# for pair in pos_corr_pairs:
#     figure, ax1 = plt.subplots(figsize=(10, 6))
#     if pair[0][:7] != pair[1][:7]:
#         series1 = close_prices[pair[0][:7]].shift(int(pair[0][-1:])).reset_index(drop=True)
#         series2 = close_prices[pair[1][:7]].shift(int(pair[0][-1:])).reset_index(drop=True)
#         ax1.plot(series1.index, series1.values, color='b')
#         ax2 = ax1.twinx()
#         ax2.plot(series2.index, series2.values, color='r')
#         plt.xlabel('time')
#         plt.ylabel('price')
#         plt.title(f'Blue: {pair[0]}, Red: {pair[1]}, Corr: {pair[2]}')
#         plt.show()
# for pair in neg_corr_pairs:
#     figure, ax1 = plt.subplots(figsize=(10, 6))
#     if pair[0][:7] != pair[1][:7]:
#         series1 = close_prices[pair[0][:7]].shift(int(pair[0][-1:])).reset_index(drop=True)
#         series2 = close_prices[pair[1][:7]].shift(int(pair[0][-1:])).reset_index(drop=True)
#         ax1.plot(series1.index, series1.values, color='b')
#         ax2 = ax1.twinx()
#         ax2.plot(series2.index, series2.values, color='r')
#         plt.xlabel('time')
#         plt.ylabel('price')
#         plt.title(f'Blue: {pair[0]}, Red: {pair[1]}, Corr: {pair[2]}')
#         plt.show()
