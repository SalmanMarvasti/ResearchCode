#isDebug
IS_DEBUG = False

#Writer method
START_YEAR = 2007
START_MONTH = 4
START_DAY = 1
FINISH_YEAR = 2017
FINISH_MONTH = 4
FINISH_DAY = 1
CLOSE_HOURS = 16
DATA_ACCESS_CLASS = 'Yahoo'
DATA_ACCESS_PATH = '/home/sepehr/QSTK-0.2.8/QSTK/QSData'

#Main method
BACK_UP = []

EXACT_CHOSEN_STOCK = ['ADSK', 'WFC', 'NSC', 'WY', 'MHS', 'BLL', 'AFL', 'HES', 'SNDK', 'COL', 'UST', 'ED', 'TER', 'DGX', 'QLGC', 'FTI', 'WWY', 'FAST', 'MYL', 'SCHW', 'SBUX', 'SPLS', 'BEAM', 'JCP', 'AKAM', 'WFT', 'VAR', 'HPQ', 'PFE', 'XRAY', 'CSC', 'FLIR', 'TEX', 'FMCC', 'FITB', 'SHW',
          'LUK', 'WHR', 'HUM', 'RSH', 'HNZ', 'HON', 'CSCO', 'MBI', 'KEY', 'TIE', 'BC', 'PNC', 'HOG', 'BCR', 'NCC', 'AMGN', 'JDSU', 'STI', 'NOVL', 'RRC', 'LYB', 'EXPE', 'TWX', 'CTXS', 'FNMA', 'BBBY', 'WMT', 'AMT', 'HRB', 'LH', 'LLY', 'EFX', 'AMP', 'GOOG', 'MAS', 'GD', 'CLX', 'ADBE', 'TYC', 'NOV', 'BWA', 'TIF', 'SII', 'GLW', 'SJM',
          'UIS', 'S', 'ROK', 'RTN', 'JWN', 'HBAN', 'KR', 'WYE', 'PCP', 'ORLY', 'MTG', 'VLO', 'MUR', 'WAMUQ', 'CF', 'MU', 'ITT', 'POM', 'ITW', 'ARG', 'TGT', 'IRM', 'FII', 'L', 'ANF', 'MET', 'APH', 'XRX', 'CAT', 'C', 'FTR', 'LMT', 'EXC', 'EBAY', 'LIFE', 'ABI', 'RDC', 'AMD', 'ROST', 'EQT', 'COP', 'GCI', 'PX',
          'CAH', 'EQR', 'KBH', 'DVN', 'XTO', 'CTAS', 'DHR', 'RSG', 'EXPD', 'CTSH', 'CMS', 'FDO', 'WFR', 'CI', 'NRG',
          'VFC', 'PXD', 'NYX', 'APOL', 'ZMH', 'PBG', 'SLE', 'FLS', 'VZ', 'LM', 'EQ', 'PTV', 'HAL', 'CVX', 'WAG', 'LUV',
          'LRCX', 'GILD', 'USB', 'DISCA', 'AET', 'CBE', 'DE', 'RIG', 'OMC', 'MCO', 'FFIV', 'MCHP', 'MI', 'CB', 'EK',
          'AGN', 'XLNX', 'KO', 'JNJ', 'MCD', 'RRD', 'CVH', 'GPC', 'CMI', 'BDK', 'ASH', 'PCL', 'ODP', 'PKI', 'HST', 'KMI', 'TMO', 'CBG', 'DIS', 'ZION', 'HP', 'DRI', 'LEN', 'DLTR', 'WU', 'ACAS', 'ISRG', 'SDS', 'K', 'PRU', 'MDP', 'NBR', 'JOY', 'GIS', 'ALL', 'GGP', 'RAI', 'JAVA', 'SYMC', 'WPO', 'KMB', 'CHK', 'HIG', 'AAPL', 'SYK', 'CBS', 'HSP', 'HPCCP', 'BSX', 'NDAQ', 'KLAC', 'CINF', 'COV', 'STZ', 'OMX', 'RHI', 'TXN', 'SLM', 'WYN', 'CVS', 'MMC', 'PDCO', 'PLL', 'WB', 'DNB', 'HSY', 'COH', 'JNS',
          'SAI', 'UNH', 'LLTC', 'TLAB', 'PAYX', 'OKE', 'CLF', 'CMG', 'A', 'DD', 'FISV', 'XOM', 'GENZ', 'MKC', 'SWN',
          'JEC', 'EMN', 'VRSN', 'EIX', 'LEG', 'PWR', 'COG', 'NTAP', 'JBL', 'IACI', 'WPI', 'SE', 'SH', 'BEN', 'LXK',
          'NBL', 'LOW', 'ESV', 'Q', 'SO', 'TROW', 'CFC+A', 'SHLD', 'BRCM', 'BDX', 'NWSA', 'HAR',
          'PCAR', 'NWL', 'CNP', 'KSS', 'FMC', 'WEC', 'AMAT', 'KG', 'XL', 'RL',
          '$VIX', 'BIG', 'ROH', 'NYT', 'ETN', 'WMB', 'DDS', 'CERN', 'ALTR', 'SNV', 'PEP', 'V', 'MOLX', 'AA', 'NUE',
          'AVP', 'BBY', 'BLK', 'IFF', 'ROP', 'CVG', 'AON', 'EMR', 'HCN', 'TWC', 'PNW', 'IVZ', 'HCP', 'TEL', 'SCG',
          'CMCSA', 'BAX', 'F', 'MAR', 'BMC', 'CCI', 'ACN', 'STT', 'XEL', 'WFM', 'CAG', 'LNC', 'WLP', 'NKE', 'CMA',
          'KFT', 'PCS', 'TEG', 'ICE', 'BHI', 'NU', 'DYN', 'IGT', 'R', 'CIEN', 'CCE', 'PPL', 'AVY', 'DDR', 'PEG', 'GPS', 'FOSL', 'PH', 'NTRS', 'LLL', 'CA', 'MSI', 'STX', 'VMC', 'SLB', 'CSX', 'THC', 'WAT', 'WPX', 'DUK', 'IP', 'HCBK', 'EL', 'DF', 'XYL', 'CCL', 'MMM', 'AMZN', 'JCI', 'MDT', 'VIA.B', 'TE', 'KIM', 'DPS', 'TRIP', 'HRL', 'NSM', 'NFLX', 'MTW', 'ADI', 'DV', 'MHP', 'CEG', 'UPS', 'MON', 'SVU', 'TAP', 'COF', 'TJX', 'BTU', 'ABT', 'ACE', 'PBI', 'AIG', 'AEE', 'DOW', 'OI', 'APA', 'OXY', 'FCX', 'AXP', 'PSA', 'IBM', '$DJI', 'PSX', 'BSC', 'DO', 'ECL', 'HOT', 'M', 'IYR', 'ESRX', 'VTR', 'LIZ', 'MO', 'SNA', 'EP', 'URBN', 'PRGO', 'CNX', 'DVA', 'GME', 'YUM', 'APC', 'APD', 'GM', 'MSFT',
          'PCG', 'DTE', 'ATI', 'COST', 'CIT', 'GLD', 'NFX', 'ADP', 'RF', 'CPWR', 'BA', 'PM', 'T', 'INTC', 'EOG', 'CME',
          'MTB', 'MNST', 'SUN', 'AN', 'VIAB', 'AYE', 'MJN', 'MWV', 'NVLS', 'NVDA', 'ETFC', 'QCOM', 'ETR', 'LSI', 'BMS',
          'AIZ', 'X', 'SPY', 'D', 'CFN', 'SGP', 'BJS', 'NI', 'DNR', 'LEHMQ', 'ALXN', 'IPG', 'TRV', 'NE', 'AVB', 'HRS',
          'FRX', 'EW', 'BMY', 'IR', 'CTX', 'LTD', 'TSO', 'SRCL', 'MCK', 'SWY', 'PCLN', 'MOS', 'PBCT', 'MRO', 'GAS',
          'ANR', 'NOC', 'BIIB', 'NEM', 'FLR', 'SRE', 'CTL', 'FE', 'SIAL', 'GS', 'ERTS', 'SAF', 'PFG', 'WM', 'TXT',
          'SYY', 'DHI', 'CBSH', 'FSLR', 'CRM', 'EA', 'KMX', 'NEE', 'STJ', 'GNW', 'FDX', 'RHT', '$SPX', 'DFS', 'GR', 'TMK', 'MPC', 'PLD', 'HAS', 'BAC', 'CCMO', 'UTX', 'TSN', 'TSS', 'VNO', 'CHRW', 'PG', 'SWK', 'WIN', 'WDC', 'SEE', 'UNM', 'CAM', 'PPG', 'UNP', 'MS', 'JNPR', 'WEN', 'ACS', 'ABKFQ', 'WYNN', 'AEP', 'PGN', 'PHM', 'YHOO', 'BUD', 'CPB', 'GWW', 'FIS', 'CVC', 'BRK.B',
          'TDC', 'INTU', 'BK', 'MWW', 'GE', 'ADM', 'CL', 'AIV', 'CELG', 'ABC', 'BXP', 'QEP', 'SSP', 'AZO', 'MA', 'PGR',
          'DOV', 'MAT', 'MRK', 'GT', 'ORCL', 'JPM', 'HD', 'FHN', 'AES', 'JNY', 'BBT']
EXACT_STOCK = EXACT_CHOSEN_STOCK
RETURNIZED_MEAN_MULTIPLIER = 0
START_OF_PICKER = 0
NUMBER_OF_STOCKS_PICKED = 30
AAPL_DEVIATION = 0.57
MEAN_THRESHHOLD = 4
WINDOW_OVERLAP = 5

#Line
STRAIGHT_LINE_TOLERANCE = None
STRAIGHT_LINE_TOLERANCE_RETURNIZED = 0.000001
STRAIGHT_LINE_TOLERANCE_ORIGINAL = 0.09
NUMBER_OF_POINTS_CHOSEN_FOR_EACH_LINE = 3
NORMALIZE_SCALE = 1

#ClusterMethods
CIRCLE_RADIUS_AROUND_CENTROIDS = 0.05

#Addresses
ADDRESS_TO_FILES = '/home/sepehr/QSTK-0.2.8/QSTK/QSData/Yahoo/'
ADDRESS_TO_UPDATED_FILES = '/home/sepehr/Documents/Marvasti Project/refactored code/updated files'
ADDRESS_TO_SHELL_SCRIPT = '/home/sepehr/Documents/Marvasti\ Project/refactored\ code/updater\ script/get-yahoo-quotes.sh'

#invalid data
ARRAY_OF_INVALID_STOCKS = ['ARG', 'COP', 'FDO', 'WAG', 'CVH', 'PCL', 'ACAS', 'AAPL', 'KG', 'ALTR', 'BAX', 'KFT', 'HCBK', 'VIA.B', 'BSC', 'URBN', 'PRGO', 'CNX', 'SUN', 'NVLS', 'CTX', 'WEN', 'BRK.B', 'ARG', 'COP', 'FDO', 'WAG', 'CVH', 'PCL', 'ACAS', 'AAPL', 'KG', 'ALTR', 'BAX', 'KFT', 'HCBK', 'VIA.B', 'BSC', 'URBN', 'PRGO', 'CNX', 'SUN', 'NVLS', 'CTX', 'WEN', 'BRK.B', 'MHS', 'QLGC', 'WWY', 'SPLS', 'CSC', 'RSH', 'HNZ', 'TIE', 'BCR', 'NCC', 'JDSU', 'NOVL', 'TYC', 'SII', 'WYE', 'PCP', 'WAMUQ', 'POM', 'XTO', 'WFR', 'NYX', 'APOL', 'ZMH', 'PBG', 'SLE', 'EQ', 'PTV', 'CBE', 'MI', 'EK', 'BDK', 'JOY', 'RAI', 'JAVA', 'WPO', 'HSP', 'HPCCP', 'COV', 'OMX', 'PLL', 'COH', 'JNS', 'SAI', 'LLTC', 'TLAB', 'DD', 'GENZ', 'IACI', 'WPI', 'LXK', 'CFC+A', 'BRCM', 'HAR', '$VIX', 'ROH', 'MOLX', 'TWC', 'BMC', 'WFM', 'WLP', 'PCS', 'TEG', 'BHI', 'NU', 'TE', 'DV', 'MHP', 'CEG', 'ACE', 'DOW', '$DJI', 'HOT', 'LIZ', 'EP', 'AYE', 'MJN', 'MWV', 'CFN', 'SGP', 'BJS', 'LEHMQ', 'FRX', 'LTD', 'TSO', 'SWY', 'GAS', 'ANR', 'SIAL', 'ERTS', 'SAF', 'STJ', '$SPX', 'GR', 'CCMO', 'CAM', 'ACS', 'ABKFQ', 'PGN', 'YHOO', 'CVC', 'MWW', 'JNY']

#categories
BasicIndustries = ['SHLM', 'ADES', 'AEGN', 'AMTX', 'AMRK', 'AMWD', 'AMRS', 'AQMS', 'RKDA', 'APWC', 'BCPC', 'CLXT', 'CVCO', 'CENX', 'CADC', 'CHNR', 'CDXS', 'CRWS', 'CSWI', 'CTIB', 'DELT', 'EVGN', 'GEVO', 'GLDD', 'GPP', 'GPRE', 'GURE', 'HCCI', 'HYGS', 'IOSP', 'FSTR', 'LAYN', 'LMB', 'MBII', 'MTRX', 'MERC', 'MRDN', 'MRDNW', 'MEOH', 'MPVD', 'MYRG', 'NEWA', 'NWPX', 'ZEUS', 'OPNT', 'OCC', 'OSN', 'PEIX', 'PAAS', 'PATK', 'PESI', 'PGLC', 'PLPC', 'PRIM', 'GOLD', 'RGSE', 'REGI', 'RGLD', 'SNES', 'SMED', 'SND', 'SSRM', 'STLD', 'SRCL', 'SRCLP', 'STRL', 'SYNL', 'SES', 'TANH', 'TORM          ', 'USLM', 'UFPI', 'USAP', 'WWR', 'VERU', 'WDFC', 'YTEN']
CapitalGoods = ['AVHI', 'AAON', 'ABAX', 'AXDX', 'ADOM', 'AEIS', 'AEHR', 'AVAV', 'AEMD', 'AMOT', 'AIMC', 'AOBC', 'ARII', 'ALOG', 'APOG', 'ARCW', 'ARTW', 'ASTE', 'ATRO', 'ASTC', 'ASV', 'AAXN', 'BELFA', 'BELFB', 'BLBD', 'BNSO', 'BWEN', 'BRKR', 'CSTE', 'CAMT', 'CECE', 'CETX', 'CETXP', 'CETXW', 'KOOL', 'GTLS', 'CAAS', 'CCCL', 'CXDC', 'CDTI', 'CLIR', 'CLIRW', 'CODA', 'CGNX', 'COHR', 'COHU', 'CMCO', 'CVGI', 'CHCI', 'CTRL', 'CPSH', 'CYBE', 'DAIO', 'BOOM', 'DORM', 'DXPE', 'DYSL', 'EACQ', 'EACQU', 'EACQW', 'EML', 'EKSO', 'ESLT', 'ELSE', 'WIRE', 'EXFO', 'FARO', 'GSM', 'FLIR', 'FLDM', 'FRTA', 'RAIL', 'FEIM', 'FTEK', 'FFHL', 'GRMN', 'GENC', 'GNTX', 'THRM', 'GEOS', 'ROCK', 'GRBK', 'GIFI', 'HDNG', 'HBIO', 'HAYN', 'HEBT', 'HIHO', 'HOVNP', 'HTGM', 'HURC', 'IEP', 'IESC', 'IIVI', 'ILMN', 'ISNS', 'PI', 'IIIN', 'IART', 'IIN', 'ITRI', 'KALU', 'KNDI', 'KEQU', 'KLAC', 'KLXI', 'KRNT', 'KTOS', 'LGIH', 'LCUT', 'MBUU', 'MATW', 'MCFT', 'MRCY', 'MLAB', 'MICT', 'MICTW', 'MVIS', 'MSON', 'MKSI', 'MINI', 'MPAA', 'MTSC', 'NANO', 'NEON', 'NFEC', 'NNBR', 'NDSN', 'NSYS', 'NTIC', 'NVMI', 'KZIA', 'OFLX', 'ORBK', 'PCAR', 'PACB', 'PKOH', 'PRCP', 'PPIH', 'PGTI', 'PRPO', 'PSDV', 'RAVN', 'ROLL', 'RETO', 'RFIL', 'SMIT', 'SHLO', 'SORL', 'SPAR', 'STRT', 'SNHY', 'RUN', 'SYPR', 'TATT', 'TAYD', 'TGEN', 'TNAV', 'TSLA', 'XONE', 'TRNS', 'TRS', 'TRMB', 'USCR', 'UFPT', 'OLED', 'VREX', 'VICR', 'WKHS', 'XCRA', 'YECO', 'ZKIN']
ConsumerDurables = ['AMSC', 'CRMT', 'BSET', 'CASY', 'CENT', 'CENTA', 'CVO', 'CTHR', 'CJJD', 'CDXC', 'CPRT', 'CYAN', 'DAKT', 'EDUC', 'EFOI', 'CLWT', 'FLXS', 'FOMX', 'FELE', 'GPAC', 'GPACU', 'GPACW', 'HWKN', 'HELE', 'MLHR', 'HOFT', 'HDSN', 'IDSY', 'IDSA', 'IPHS', 'INSG', 'TILE', 'IRDM', 'IRDMB', 'IRBT', 'ITI', 'JASN', 'JASNW', 'KBAL', 'LAWS', 'LFUS', 'LYTS', 'LITE', 'MAGS', 'MTEX', 'MDWD', 'NSSC', 'NAII', 'NHTC', 'NXEO', 'NXEOU', 'NXEOW', 'NVFY', 'OBCI', 'OESX', 'PPSI', 'POOL', 'POWL', 'RVLT', 'RUSHA', 'RUSHB', 'SCHN', 'SNBR', 'SGLB', 'SGLBW', 'SLGN', 'SODA', 'STLY', 'SUMR', 'TGLS', 'DXYN', 'GT', 'TA', 'TANNI', 'TANNL', 'TANNZ', 'HEAR', 'UTSI', 'VIRC', 'WLFC', 'XGTI', 'XGTIW']
ConsumerNonDurables = ['ALCO', 'ABAC', 'FUV', 'BUFF', 'BRID', 'BUR', 'CVGW', 'CALM', 'CSWC', 'CELH', 'CHKE', 'CTAS', 'CLAR', 'COKE', 'JVA', 'COLM', 'CORE', 'BREW', 'CROX', 'CUI', 'DTEA', 'DSWL', 'DFBG', 'ENTG', 'ESCA', 'EVK', 'FARM', 'FORD', 'FOSL', 'FOXF', 'FRPT', 'FORK', 'FNKO', 'FTFT', 'WILC', 'GPIC', 'GIII', 'GLAD', 'GLADN', 'HAS', 'TWNK', 'TWNKW', 'HWCC', 'ICON', 'IFON', 'IMTE', 'IPAR', 'ITRN', 'JJSF', 'JAKK', 'JBSS', 'JOUT', 'KBSF', 'KOSS', 'LANC', 'LNDC', 'LBIX', 'LWAY', 'LMNR', 'LRAD', 'LULU', 'MAT', 'MGPI', 'MDLZ', 'MNST', 'NAKD', 'FIZZ', 'NBEV', 'SEED', 'PERY', 'PPC', 'POPE', 'PRMW', 'RADA', 'RAND', 'RAVE', 'RIBT', 'RIBTW', 'RELL', 'RCKY', 'RMCF', 'SANW', 'SAFM', 'SENEA', 'SENEB', 'SQBG', 'TYHT', 'LNCE', 'SPTN', 'SHOO', 'SGC', 'TAIT', 'TLF', 'PETZ', 'TESS', 'CHEF', 'HAIN', 'KHC', 'SMPL', 'SMPLW', 'THST', 'UNFI', 'UG', 'UEIC', 'VRA', 'VOXX', 'WEYS', 'WVVI', 'WVVIP']
ConsumerServices = ['FLWS', 'AEY', 'AGNC', 'AGNCB', 'AGNCN', 'AMMA', 'ASPS', 'AMZN', 'AMCX', 'UHAL', 'APEI', 'ANGI', 'ARCI', 'APDN', 'APDNW', 'ARKR', 'ASNA', 'ASCMA', 'ASPU', 'ATAI', 'CAR', 'BCOM', 'BZUN', 'BECN', 'BBGI', 'BBBY', 'BGFV', 'BJRI', 'BLMN', 'BMCH', 'BOBE', 'WIFI', 'BOJA', 'BBRG', 'BWLD', 'BLDR', 'CZR', 'PRSS', 'ABCD', 'CPHC', 'CPLA', 'CECO', 'CTRE', 'TAST', 'CDW', 'CETV', 'CNTY', 'BURG', 'CHTR', 'CSSE', 'PLCE', 'CALI', 'CIFS', 'HTHT', 'CHSCL', 'CHSCM', 'CHSCN', 'CHSCO', 'CHSCP', 'CHDN', 'CHUY', 'CMCT', 'CMCTP', 'CIDM', 'CTRN', 'CCOI', 'COGT', 'CMCSA', 'CDOR', 'CONN', 'COST', 'CBRL', 'CONE', 'DJCO', 'DSKE', 'DSKEW', 'PLAY', 'DFRG', 'TACO', 'TACOW', 'DENN', 'DEST', 'DXLG', 'DISCA', 'DISCB', 'DISCK', 'DISH', 'SAUC', 'DLTR', 'DLTH', 'DNKN', 'EEI', 'LOCO', 'EMITF', 'ERI', 'EMMS', 'NYNY', 'ENG', 'EQIX', 'ESND', 'EVLV', 'EXPE', 'EXPO', 'EZPW', 'DAVE', 'FAST', 'FAT', 'FRGI', 'FCFS', 'FIVE', 'FOGO', 'FORR', 'FRAN', 'FRED', 'FTD', 'FLL', 'GAIA', 'GLPI', 'GNUS', 'GOOD', 'GOODM', 'GOODO', 'GOODP', 'LAND', 'LANDP', 'ENT', 'SELF', 'GOGO', 'GLNG', 'GMLP', 'GMLPP', 'GDEN', 'GOGL', 'GTIM', 'LOPE', 'GYRO', 'HLG', 'HCOM', 'HDS', 'HMNY', 'HMTV', 'HIBB', 'HPT', 'HMHC', 'HURN', 'HBP', 'IAC', 'ICFI', 'IFMK', 'III', 'IMKTA', 'NSIT', 'ISIG', 'ISCA', 'IRCP', 'IZEA', 'MAYS', 'JACK', 'JMBA', 'JD', 'JCTCF', 'KIRK', 'KONA', 'LAMR', 'LMRK', 'LMRKO', 'LMRKP', 'LE', 'LAUR', 'LBRDA', 'LBRDK', 'LEXEA', 'LEXEB', 'LBTYA', 'LBTYB', 'LBTYK', 'LILA', 'LILAK', 'LVNTA', 'LVNTB', 'QVCA', 'QVCB', 'BATRA', 'BATRK', 'FWONA', 'FWONK', 'LSXMA', 'LSXMB', 'LSXMK', 'LTBR', 'LINC', 'LIND', 'LINDW', 'LINU', 'LKQ', 'MMYT', 'LOAN', 'MANT', 'MAR', 'MLCO', 'MCRI', 'MNRO', 'MTGE', 'MTGEP', 'NATH', 'NAUH', 'NCMI', 'NFLX', 'NYMT', 'NYMTN', 'NYMTO', 'NWS', 'NWSA', 'NXST', 'NDLS', 'NCLH', 'NTRI', 'NVEE', 'NXTD', 'NXTDW', 'OMEX', 'ODP', 'OLLI', 'ORBC', 'ORLY', 'OACQ', 'OACQR', 'OACQU', 'OACQW', 'OSTK', 'PZZA', 'FRSH', 'PAYX', 'CNXN', 'PCMI', 'SKIS', 'PENN', 'PFMT', 'PNK', 'PLYA', 'PBPB', 'PCH', 'PINC', 'PRGX', 'PSMT', 'RCM', 'RICK', 'RDI', 'RDIB', 'RRGB', 'RRR', 'MARK', 'ROIC', 'RVEN', 'RNET', 'REDU', 'RLJE', 'ROKU', 'ROST', 'RUTH', 'SBRA', 'SBRAP', 'SALM', 'SBAC', 'SCHL', 'SNI', 'SHLD', 'SHLDW', 'SHOS', 'SECO', 'SIR', 'SNH', 'SNHNI', 'SNHNL', 'SSC', 'SGBX', 'SCVL', 'SBGI', 'SIRI', 'SONC', 'SOHO', 'SOHOB', 'SOHOO', 'SP', 'SPWH', 'FUND', 'SFM', 'SBUX', 'SMRT', 'SFIX', 'STRS', 'STRA', 'STKL', 'TEDU', 'TTEK', 'TXRH', 'ANDE', 'CAKE', 'FINL', 'HABT', 'HCKT', 'INTG', 'MSG', 'MEET', 'MIK', 'STKS', 'PRSC', 'RMR', 'TST', 'TTS', 'TITN', 'CLUB', 'TSCO', 'TWMC', 'TRNC', 'TUES', 'TOUR', 'FOX', 'FOXA', 'PRTS', 'ULTA', 'UNIT', 'UONE', 'UONEK', 'URBN', 'VIA', 'VIAB', 'VDTH', 'VLGEA', 'VSEC', 'WEN', 'WHLR', 'WHLRD', 'WHLRP', 'WHLRW', 'WHLM', 'WLDN', 'WING', 'WINA', 'WPCS', 'WYNN', 'YTRA', 'YOGA', 'YGYI', 'ZAGG', 'ZUMZ']
Energy = ['AXAS', 'AHGP', 'ARLP', 'AETI', 'AREX', 'BLDP', 'BKEP', 'BKEPP', 'CLMT', 'CPST', 'CRZO', 'CDEV', 'CCLP', 'DWSN', 'FANG', 'DMLP', 'ESES', 'EXXI', 'EVEP', 'XOG', 'GPOR', 'HNRG', 'HOLI', 'IPWR', 'ISRL', 'LGCY', 'LGCYO', 'LGCYP', 'LLEX', 'LONE', 'TUSK', 'MARPS', 'MMLP', 'MGEE', 'MCEP', 'NCSM', 'ORIG', 'PTEN', 'PDCE', 'PVAC', 'PLUG', 'PNRG', 'PFIE', 'METC', 'RCON', 'REXX', 'ROSE', 'ROSEU', 'ROSEW', 'SAEX', 'SNDE', 'TELL', 'TRCH', 'TPIC', 'TGA', 'USEG', 'UPL', 'VTNR', 'VNOM', 'WLB', 'WPRT', 'WWD', 'ZN', 'ZNWAA']
Finance = ['PIH', 'TURN', 'FCCY', 'SRCE', 'ABIL', 'ANCX', 'ACNB', 'AGFS', 'AGFSW', 'ABTX', 'AMBC', 'AMBCW', 'ATAX', 'AMNB', 'ANAT', 'AMRB', 'ABCB', 'AMSF', 'ASRV', 'ASRVP', 'ATLO', 'AFSI', 'ANCB', 'ANDA', 'ANDAR', 'ANDAU', 'ANDAW', 'ACGL', 'ACGLO', 'ACGLP', 'AGII', 'AGIIL', 'AROW', 'ASFI', 'ATAC', 'ATACR', 'ATACU', 'AAME', 'ACBI', 'ACFC', 'ATLC', 'AFH', 'AFHBL', 'AUBN', 'BWINA', 'BWINB', 'BANF', 'BANFP', 'BCTF', 'BKMU', 'BOCH', 'BMRC', 'BMLP', 'BKSC', 'BOTJ', 'OZRK', 'BFIN', 'BWFG', 'BANR', 'DFVL', 'DFVS', 'DLBL', 'DLBS', 'DTUL', 'DTUS', 'DTYL', 'DTYS', 'FLAT', 'STPP', 'TAPR', 'BHAC', 'BHACR', 'BHACU', 'BHACW', 'BYBK', 'BCBP', 'BSF', 'BNCL', 'BGCP', 'BRPA', 'BRPAR', 'BRPAU', 'BRPAW', 'BCAC', 'BCACR', 'BCACU', 'BCACW', 'BRAC', 'BRACR', 'BRACU', 'BRACW', 'HAWK', 'BCOR', 'BHBK', 'BOFI', 'BOFIL', 'BOKF', 'BOKFL', 'BRQS', 'BOMN', 'BPFH', 'BPFHP', 'BPFHW', 'BDGE', 'BHF', 'BYFC', 'BPY', 'BRKL', 'BMTC', 'BLMT', 'CFFI', 'CATC', 'CAC', 'CCBG', 'CFFN', 'CSTR', 'CARO', 'CART', 'CARV', 'CATY', 'CATYW', 'CBFV', 'CBOE', 'CBTX', 'CSFL', 'CFBK', 'CVCY', 'CNBKA', 'CHFN', 'CHFC', 'CHMG', 'CCCR', 'JRJC', 'HGSH', 'CLDC', 'CINF', 'CZNC', 'CZWI', 'CZFC', 'CIZN', 'CHCO', 'CIVB', 'CIVBP', 'CSBK', 'CMSS', 'CMSSR', 'CMSSU', 'CMSSW', 'CME', 'CCNE', 'CWAY', 'COBZ', 'CVLY', 'CIGI', 'CBAN', 'COLB', 'CBSH', 'CBSHP', 'ESXB', 'CFBI', 'CTBI', 'CWBC', 'CNFR', 'CNOB', 'CNAC', 'CNACR', 'CNACU', 'CNACW', 'CPSS', 'CRVL', 'ICBK', 'COWN', 'PMTS', 'CACC', 'DGLD', 'DSLV', 'GLDI', 'SLVO', 'TVIX', 'TVIZ', 'UGLD', 'USLV', 'USOI', 'VIIX', 'VIIZ', 'XIV', 'ZIV', 'CRESY', 'CVBF', 'DHIL', 'DCOM', 'DNBF', 'DGICA', 'DGICB', 'LYL', 'DOTA', 'DOTAR', 'DOTAU', 'DOTAW', 'ETFC', 'EBMT', 'EGBN', 'EFBI', 'EWBC', 'EHTH', 'ELEC', 'ELECU', 'ELECW', 'ESBK', 'EMCI', 'EMCF', 'ECPG', 'ESGR', 'ENFC', 'EBTC', 'EFSC', 'EQFN', 'EQBK', 'ERIE', 'ESQ', 'ESSA', 'EEFT', 'FANH', 'FMAO', 'FFKT', 'FMNB', 'FBSS', 'FSAC', 'FSACU', 'FSACW', 'FNHC', 'FFBW', 'FDBC', 'LION', 'FITB', 'FITBI', 'FNGN', 'FISI', 'FNTE', 'FNTEU', 'FNTEW', 'FBNC', 'FNLC', 'BUSE', 'FBIZ', 'FCAP', 'FCNCA', 'FCBC', 'FCCO', 'FBNK', 'FDEF', 'FFBC', 'FFBCW', 'FFIN', 'THFF', 'FFNW', 'FFWM', 'FGBI', 'FHB', 'INBK', 'INBKL', 'FIBK', 'FRME', 'FMBH', 'FMBI', 'FNWB', 'FSFG', 'FUNC', 'FUSB', 'FSV', 'FFIC', 'FNBG', 'FRPH', 'FSBW', 'FSBC', 'FULT', 'GABC', 'GBCI', 'GLBZ', 'GBLI', 'GBLIL', 'GBLIZ', 'GSHT', 'GSHTU', 'GSHTW', 'GOV', 'GOVNI', 'GSBC', 'IAM', 'IAMXR', 'IAMXW', 'GNBC', 'GCBC', 'GLRE', 'GRIF', 'GGAL', 'GTYH', 'GTYHU', 'GTYHW', 'GBNK', 'GNTY', 'GFED', 'GWGH', 'HALL', 'HBK', 'HLNE', 'HBHC', 'HBHCL', 'HAFC', 'HONE', 'HWBK', 'HYAC', 'HYACU', 'HYACW', 'HIIQ', 'HTLF', 'HNNA', 'HTBK', 'HFWA', 'HX', 'HMNF', 'HBCP', 'HOMB', 'HFBL', 'HMST', 'HMTA', 'HTBI', 'HOPE', 'HFBC', 'HBNC', 'HBMD', 'HBAN', 'HBANN', 'HBANO', 'HBANP', 'HVBC', 'IBKC', 'IBKCO', 'IBKCP', 'ICCH', 'IROQ', 'ILG', 'INDB', 'IBCP', 'IBTX', 'INDU', 'INDUU', 'INDUW', 'IPCC', 'IBKR', 'IBOC', 'INTL', 'ISTR', 'ISBC', 'ITIC', 'JXSB', 'JRVR', 'JTPY', 'WYIG', 'WYIGU', 'WYIGW', 'KAAC', 'KAACU', 'KAACW', 'KBLM', 'KBLMR', 'KBLMU', 'KBLMW', 'KRNY', 'KFFB', 'KINS', 'KNSL', 'LSBK', 'LBAI', 'LKFN', 'LCA', 'LCAHU', 'LCAHW', 'LARK', 'LCNB', 'LTXB', 'LACQU', 'TREE', 'LOB', 'LIVE', 'LMFA', 'LMFAW', 'LPLA', 'MBTF', 'MACQ', 'MACQW', 'MIII', 'MIIIU', 'MIIIW', 'MCBC', 'MFNC', 'MGYR', 'MHLD', 'MSFG', 'MLVF', 'MKTX', 'MRLN', 'MPAC', 'MPACU', 'MPACW', 'MBFI', 'MBFIO', 'MBFIP', 'MFIN', 'MFINL', 'MELR', 'MBWM', 'MBIN', 'EBSB', 'CASH', 'MPB', 'MBCN', 'MSBI', 'MOFG', 'MMAC', 'MMDM', 'MMDMR', 'MMDMU', 'MMDMW', 'MORN', 'MSBF', 'MFSF', 'NDAQ', 'NKSH', 'NCOM', 'NESR', 'NESRW', 'NGHC', 'NGHCN', 'NGHCO', 'NGHCP', 'NGHCZ', 'NHLD', 'NHLDW', 'NSEC', 'NWLI', 'ISM', 'JSM', 'NAVI', 'NBTB', 'UEPS', 'NYMTP', 'NODK', 'NICK', 'NCBS', 'NMIH', 'NBN', 'NTRS', 'NTRSP', 'NFBK', 'NRIM', 'NWBI', 'NWFL', 'OVLY', 'OCFC', 'OFED', 'OVBC', 'OLBK', 'ONB', 'OPOF', 'OSBC', 'OSBCP', 'OBAS', 'OPHC', 'ORIT', 'ORRF', 'OSPR', 'OSPRU', 'OSPRW', 'OTTW', 'OXBR', 'OXBRW', 'PMBC', 'PPBI', 'PACW', 'PBNC', 'PKBK', 'PBHC', 'PNBK', 'PYDS', 'PBBI', 'PCSB', 'PDLB', 'PGC', 'PWOD', 'WRLS', 'WRLSR', 'WRLSU', 'WRLSW', 'PEBO', 'PEBK', 'PFIS', 'PBCT', 'PBCTP', 'PUB', 'PICO', 'PNFP', 'PLBC', 'PBSK', 'BPOP', 'BPOPM', 'BPOPN', 'PBIB', 'PRAA', 'PFBI', 'PVBC', 'PROV', 'PBIP', 'QCRH', 'RNDB', 'RBB', 'RDFN', 'RNST', 'RBCAA', 'FRBK', 'RVSB', 'STBA', 'SCAC', 'SCACU', 'SCACW', 'SAFT', 'SAL', 'SASR', 'SBFG', 'SBFGP', 'SBCF', 'SNFCA', 'SEIC', 'SLCT', 'SIGI', 'STNLU', 'SFBS', 'SVBI', 'SHBI', 'SIFI', 'SIEB', 'BSRR', 'SBNY', 'SBNYW', 'SRUN', 'SRUNU', 'SRUNW', 'SAMG', 'SFNC', 'SLM', 'SLMBP', 'SMBK', 'SFBC', 'SSB', 'SFST', 'SMBC', 'SONA', 'SBSI', 'STFC', 'STBZ', 'STLR', 'STLRU', 'STLRW', 'SBT', 'SSFN', 'SYBT', 'SMMF', 'SNBC', 'SBBX', 'SIVB', 'TROW', 'AMTD', 'TBNK', 'TCBI', 'TCBIL', 'TCBIP', 'TCBIW', 'TFSL', 'TBBK', 'CG', 'TCGP', 'TCFC', 'FBMS', 'FLIC', 'NAVG', 'TIL', 'TSBK', 'TIPT', 'TCBK', 'TSC', 'TBK', 'TRST', 'TRMK', 'TRCB', 'GROW', 'UMBF', 'UMPQ', 'UNAM', 'UBSH', 'UNB', 'UBCP', 'UBOH', 'UBSI', 'UCBA', 'UCBI', 'UCFC', 'UBNK', 'UFCS', 'UIHC', 'UBFO', 'UNTY', 'UVSP', 'VALU', 'VEAC', 'VEACU', 'VEACW', 'VBTX', 'VBFC', 'VIRT', 'VRTS', 'VRTSP', 'WAFD', 'WAFDW', 'WASH', 'WSBF', 'WCFB', 'WEBK', 'WSBC', 'WTBA', 'WABC', 'WNEB', 'WLTW', 'WINS', 'WTFC', 'WTFCM', 'WTFCW', 'WETF', 'WMIH', 'WRLD', 'WSFS', 'WVFC', 'YERR', 'YIN', 'ZAIS', 'ZION', 'ZIONW', 'ZIONZ']
HealthCare = ['ABEO', 'ABEOW', 'ABMD', 'ABLX', 'ACIU', 'ACHC', 'ACAD', 'ACST', 'XLRN', 'ARAY', 'ACRX', 'ACER', 'ACERW', 'ACET', 'AKAO', 'ACHV', 'ACHN', 'ACRS', 'ACOR', 'ADMS', 'ADMP', 'ADAP', 'ADUS', 'ADMA', 'ADRO', 'AAAP', 'ADXS', 'ADXSW', 'ADVM', 'AGLE', 'AERI', 'AEZS', 'GNMX', 'AFMD', 'AGEN', 'AGRX', 'AGIO', 'ALRN', 'AIMT', 'AKTX', 'AKCA', 'AKBA', 'AKER', 'AKRX', 'ALBO', 'ALDR', 'ALDX', 'ALXN', 'ALGN', 'ALIM', 'ALKS', 'ALNA', 'AHPI', 'ALQA', 'AFAM', 'ALNY', 'ATEC', 'ALPN', 'ALT', 'AMAG', 'AMRN', 'AMDA', 'AMED', 'AMGN', 'FOLD', 'AMPH', 'ANAB', 'AVXL', 'ANGO', 'ANIP', 'ANIK', 'ATRS', 'ANTH', 'APLS', 'APEN', 'AGTC', 'APRI', 'APVO', 'APTO', 'AQXP', 'ARDM', 'ARLZ', 'PETX', 'ABUS', 'ABIO', 'ARDX', 'ARNA', 'ARGX', 'ARGS', 'ARQL', 'ARRY', 'ARWR', 'ASNS', 'ASND', 'ASMB', 'ATRA', 'ATNX', 'ATHX', 'ATOS', 'ATRC', 'ATRI', 'LIFE', 'BOLD', 'AUPH', 'EARS', 'AVDL', 'ATXI', 'AVEO', 'AVXS', 'AVGR', 'AVIR', 'AHPA', 'AHPAU', 'AHPAW', 'AXGN', 'AXON          ', 'AXSM', 'AYTU', 'AZRX', 'BGNE', 'BLPH', 'BLCM', 'BNTC', 'BNTCW', 'BYSI', 'BASI', 'ORPN', 'BIOC', 'BCRX', 'BDSI', 'BIIB', 'BIOL', 'BLFS', 'BLRX', 'BMRN', 'BMRA', 'BVXV', 'BVXVW', 'BPTH', 'BIOS', 'BSTC', 'BSPM', 'TECH', 'BEAT', 'BIVV', 'BLUE', 'BPMC', 'BCLI', 'CLBS', 'CALA', 'CGIX', 'CAPR', 'CARA', 'CRME', 'CSII', 'CDNA', 'CASM', 'CASC', 'CASI', 'CATB', 'CBIO', 'CPRX', 'CATS', 'CELC', 'CELG', 'CELGZ', 'CLDX', 'CLRB', 'CLRBW', 'CLRBZ', 'CLLS', 'CBMG', 'CLSN', 'CYAD', 'MLNT', 'CERC', 'CERCW', 'CERS', 'CSBR', 'CHEK', 'CHEKW', 'CKPT', 'CEMI', 'CCXI', 'CHFS', 'CHMA', 'CMRX', 'CBPO', 'CDTX', 'CTXR', 'CTXRW', 'CLSD', 'CMTA', 'CBLI', 'CLVS', 'CODX', 'CGNT', 'CHRS', 'COLL', 'CYHHZ', 'CGEN', 'CNAT', 'CNCE', 'CXRX', 'CFMS', 'CNMD', 'CFRX', 'CTRV', 'CRBP', 'CORT', 'CORI', 'CRVS', 'CRSP', 'CTIC', 'CPIX', 'CRIS', 'CUTR', 'CYCC', 'CYCCP', 'CBAY', 'CYTK', 'CTMX', 'CYTX', 'CYTXW', 'CTSO', 'CYTR', 'DARE', 'DRIO', 'DRIOW', 'DBVT', 'DCPH', 'DMPI', 'XRAY', 'DEPO', 'DERM', 'DXCM', 'DRNA', 'DFFN', 'DRAD', 'DVCR', 'DOVA', 'DRRX', 'DYNT', 'DVAX', 'EGRX', 'EDAP', 'EDGE', 'EDIT', 'EGLT', 'EIGR', 'EBIO', 'ENTA', 'ENDP', 'ECYT', 'ELGX', 'NDRA', 'NDRAW', 'ENTL', 'EPZM', 'ERYP', 'ESPR', 'EPIX', 'EVOK', 'EXAS', 'EXAC', 'EXEL', 'ESRX', 'EYEG', 'EYEGW', 'FATE', 'FENC', 'FCSC', 'FGEN', 'FPRX', 'FVE', 'FLKS', 'FLXN', 'FONR', 'FBIO', 'FBIOP', 'FWP', 'FMI', 'FLGT', 'GTHX', 'GLPG', 'GALT', 'GLMD', 'GEMP', 'GENE', 'GNMK', 'GNCA', 'GHDX', 'GERN', 'GILD', 'GBT', 'GLYC', 'GRFS', 'GTXI', 'GWPH', 'HALO', 'HCSG', 'HTBX', 'HSIC', 'HRTX', 'HSKA', 'HSGX', 'HOLX', 'HZNP', 'HCM', 'ICAD', 'ICLR', 'ICUI', 'IDRA', 'IDXX', 'RXDX', 'KANG', 'ICCC', 'IMDZ', 'IMNP          ', 'IMGN', 'IMMU', 'IMRN', 'IMRNW', 'IPXL', 'IMMY', 'INCY', 'INFI', 'INVA', 'INGN', 'INO', 'INSM', 'PODD', 'INSY', 'NTEC', 'NTLA', 'IPCI', 'ICPT', 'IDXG', 'XENT', 'ITCI', 'ISRG', 'NVIV', 'IVTY', 'IONS', 'IRMD', 'IRTC', 'IRIX', 'IRWD', 'JAGX', 'JAZZ', 'JNCE', 'JNP', 'JUNO', 'KTWO', 'KALA', 'KALV', 'KMDA', 'KPTI', 'KMPH', 'KERX', 'KIN', 'KTOV', 'KTOVW', 'KRYS', 'KURA', 'LJPC', 'LAKE', 'LNTH', 'LPTX', 'LMAT', 'LXRX', 'LHCG', 'LLIT', 'LPNT', 'LFVN', 'LGND', 'IOVA', 'LPCN', 'LIVN', 'LOXO', 'LMNX', 'LUNA', 'MBVX', 'MGNX', 'MDGL', 'MGLN', 'MNKD', 'MRNS', 'MASI', 'MZOR', 'MNOV', 'MDGS', 'MEDP', 'MEIP', 'VIVO', 'MMSI', 'MACK', 'MRSN', 'MRUS', 'MESO', 'MBOT', 'MTP', 'MDXG', 'NERV', 'MGEN', 'MRTX', 'MTEM', 'MBRX', 'MNTA', 'MTFB', 'MTFBW', 'MBIO', 'MYL', 'MYND', 'MYNDW', 'MYOK', 'MYOS', 'MYGN', 'NBRV', 'NSTG', 'NAOV', 'NK', 'NTRA', 'NRCIA', 'NRCIB', 'EYE', 'NATR', 'BABY', 'NKTR', 'NEOG', 'NEOS', 'NEOT', 'NVCN', 'NEO', 'NEPT', 'CUR', 'NBIX', 'NURO', 'NUROW', 'NTRP', 'NLNK', 'NITE', 'NOVN', 'NVAX', 'NVLN', 'NVCR', 'NVUS', 'NCNA', 'NUVA', 'NVTR', 'NXTM', 'NYMX', 'OASM', 'OBLN', 'OBSV', 'OCUL', 'OHRP', 'OMER', 'ONS', 'ONSIW', 'ONSIZ', 'OMED', 'ONTX', 'ONTXW', 'ONCS', 'OPGN', 'OPGNW', 'OPHT', 'OPK', 'OPTN', 'ORMP', 'OSUR', 'OREX', 'ONVO', 'OFIX', 'KIDS', 'OTIC', 'OVAS', 'OVID', 'OXFD', 'PCRX', 'PTIE', 'PRTK', 'PDCO', 'PAVM', 'PAVMW', 'PDLI', 'PTX', 'PETQ', 'PETS', 'PZRX', 'PAHC', 'FCRE', 'PIRS', 'PSTI', 'PLXP', 'PTLA', 'PRAH', 'PRAN', 'LENS', 'IMMP', 'PDEX', 'PGNX', 'PRPH', 'PRQR', 'PTGX', 'PRTO', 'PTI', 'PRTA', 'PMD', 'PTCT', 'PULM', 'PLSE', 'PBYI', 'QGEN', 'QDEL', 'QTNT', 'RARX', 'RDUS', 'RDNT', 'RETA', 'REPH', 'RDHL', 'REGN', 'RGNX', 'RGLS', 'RELV', 'RGEN', 'RPRX', 'RSLS', 'HAIR', 'RTRX', 'RVNC', 'RWLK', 'RYTM', 'RIGL', 'RIOT', 'RTTR', 'RMTI', 'ROSG', 'RTIX', 'RXII', 'RXIIW', 'SAGE', 'SGMO', 'GCVRZ', 'SRPT', 'SVRA', 'SCPH', 'SCYX', 'SPNE', 'SGEN', 'EYES', 'EYESW', 'SELB', 'SNMX', 'SRTS', 'SRTSW', 'MCRB', 'SHPG', 'SNNA', 'SIEN', 'SRRA', 'SVA', 'SKLN', 'SLNO', 'SLNOW', 'SNGX', 'SNGXW', 'SNOA', 'SNOAW', 'SRNE', 'ONCE', 'SPPI', 'SPRO', 'SBPH', 'STAA', 'STDY', 'SBOT', 'STML', 'SSKN', 'SBBP', 'SCMP', 'SMMT', 'SNSS', 'SUPN', 'SGRY', 'SRDX', 'SNDX', 'SGYP', 'SYRS', 'TTOO', 'TCMD', 'TNDM', 'TPIV', 'TLGT', 'TENX', 'TSRO', 'TTPH', 'TGTX', 'ENSG', 'MDCO', 'TXMD', 'TRPX', 'TBPH', 'TIG', 'TTNP', 'TVTY', 'TOCA', 'TNXP', 'TCON', 'TRVN', 'TRIL', 'TRIB', 'TROV', 'TRUP', 'TYME', 'RARE', 'QURE', 'UTHR', 'URGN', 'UTMD', 'VLRX', 'VNDA', 'VBLT', 'VBIV', 'VCYT', 'VSTM', 'VCEL', 'VRML', 'VRNA', 'VSAR', 'VRTX', 'VICL', 'VRAY', 'VKTX', 'VKTXW', 'VTGN', 'VTL', 'VIVE', 'VVUS', 'VYGR', 'VTVT', 'WBA', 'WVE', 'WMGI', 'WMGIZ', 'XBIT', 'XNCR', 'XBIO', 'XENE', 'XOMA', 'XTLB', 'ZFGN', 'ZLAB', 'ZEAL', 'ZIOP', 'ZGNX', 'ZSAN', 'ZYNE']
Miscellaneous = ['ACTG', 'AKAM', 'ALJJ', 'ARTX', 'ATHN', 'RILY', 'RILYL', 'RILYZ', 'BOXL', 'BSQR', 'CATM', 'CASS', 'CBAK', 'CDK', 'CCRC', 'CREG', 'CMPR', 'CLCT', 'CSGP', 'CRAI', 'CTRP', 'APPS', 'EBAY', 'EBAYL', 'ESIO', 'ETSY', 'XELA', 'EXLS', 'FNJN', 'FCEL', 'GPRO', 'GRVY', 'HQY', 'HPJ', 'HMSY', 'IKNX', 'INWK', 'IDCC', 'ITUS', 'KGJI', 'TAX', 'LLNW', 'LQDT', 'MARA', 'MCHX', 'MXWL', 'MELI', 'MLNK', 'MGI', 'LABL', 'NTES', 'EGOV', 'NOVT', 'OMNT', 'PYPL', 'PFSW', 'PCOM', 'POLA', 'QIWI', 'QTRH', 'QNST', 'RRD', 'RDWR', 'REIS', 'REFR', 'RECN', 'RMNI', 'RMGN', 'RPXC', 'SREV', 'SFLY', 'SSNT', 'SITO', 'SGRP', 'SPEX', 'STMP', 'TRHC', 'TTGT', 'JYNT', 'PCLN', 'NCTY', 'TIVO', 'ULBI', 'USAT', 'USATP', 'XELB', 'Z', 'ZG']
PublicUtilities = ['CAFD', 'EGHT', 'ADTN', 'AKTS', 'ALSK', 'AMOV', 'APLP', 'ARTNA', 'AY', 'ATNI', 'AUDC', 'CDZI', 'CWST', 'CLNE', 'CLFD', 'CLRO', 'JCS', 'CTWS', 'CNSL', 'CWCO', 'DZSI', 'FTR', 'FTRPR', 'GNCMA', 'GWRS', 'INFN', 'IGLD', 'JSYN', 'JSYNR', 'JSYNU', 'JSYNW', 'LOOP', 'CALL', 'MTSL', 'MSEX', 'NTGR', 'NEXT', 'NEXTW', 'NIHD', 'OPTT', 'OHGI', 'OTEL', 'OTTR', 'PTNR', 'PEGI', 'PDVW', 'PCYO', 'RGCO', 'SHEN', 'SKYS', 'SPKE', 'SPKEP', 'SPOK', 'SUNW', 'TERP', 'YORW', 'TMUS', 'ECOL', 'VEON', 'VVPR', 'VOD', 'WSTL', 'WIN']
Technology = ['VNET', 'TWOU', 'JOBS', 'ACIA', 'ACIW', 'ACMR', 'ATVI', 'ACTA', 'ACXM', 'IOTS', 'ADBE', 'AMD', 'AGYS', 'AIRG', 'AMCN', 'ALRM', 'ALLT', 'MDRX', 'AOSL', 'GOOG', 'GOOGL', 'AABA', 'ALTR', 'TSG', 'AMBA', 'DOX', 'AMRH', 'AMRHW', 'AMSWA', 'AMKR', 'ASYS', 'ADI', 'ANSS', 'APPF', 'APPN', 'AAPL', 'AMAT', 'AAOI', 'APTI', 'ARRS', 'ASML', 'AZPN', 'ALOT', 'ASUR', 'TEAM', 'ATOM', 'ATTU', 'ADSK', 'ADP', 'AUTO', 'AVNW', 'AVID', 'AWRE', 'ACLS', 'AXTI', 'BOSC', 'BIDU', 'BAND', 'BBSI', 'BV', 'BNFT', 'BKYI', 'BBOX', 'BLKB', 'BL', 'EPAY', 'BLIN          ', 'BCOV', 'AVGO', 'BSFT', 'BVSN', 'BRKS', 'CA', 'CCMP', 'CDNS', 'CAMP', 'CALD', 'CSIQ', 'CARB', 'CARG', 'CAVM', 'CRNT', 'CERN', 'CEVA', 'CYOU', 'CHKP', 'CNIT', 'CCIH', 'CNET', 'IMOS', 'CRUS', 'CSCO', 'CTXS', 'CTSH', 'CHUBA', 'CHUBK', 'COMM', 'CVLT', 'CPSI', 'CTG', 'CMTL', 'CCUR', 'CSOD', 'CPAH', 'COUP', 'CRAY', 'CREE', 'CRTO', 'CCRN', 'CSGS', 'CSPI', 'CVV', 'CYBR', 'CY', 'CYRN', 'DWCH', 'DTRM', 'DGII', 'DMRC', 'DGLY', 'DIOD', 'DLHC', 'DSPG', 'EBIX', 'ELON', 'SATS', 'EDGW', 'EGAN', 'EA', 'EFII', 'ELTK', 'EMKR', 'EIGI', 'WATT', 'ERII', 'ENPH', 'PLUS', 'ERIC', 'EVBG', 'MRAM', 'EVOL', 'EXTR', 'FFIV', 'FB', 'FNSR', 'FEYE', 'FSLR', 'FISV', 'FIVN', 'FLEX', 'FPAY', 'FSCT', 'FRSX', 'FORM', 'FORTY', 'FTNT', 'FMCI', 'FMCIR', 'FMCIU', 'FMCIW', 'FSNN', 'GDS', 'GFN', 'GFNCP', 'GFNSL', 'GIGM', 'GILT', 'GLUU', 'GEC', 'GSUM', 'GRPN', 'GSIT', 'HQCL', 'HLIT', 'HSTM', 'HSII', 'HIMX', 'HDP', 'HSON', 'ICHR', 'INVE', 'INFO', 'IMMR', 'IMPV', 'INOD', 'ISSC', 'INOV', 'INPX', 'INSE', 'IDTI', 'INTC', 'LINK', 'IMI', 'INAP', 'IIJI', 'INTX', 'IVAC', 'INTU', 'IPAS', 'IPGP', 'IXYS', 'JCOM', 'JASO', 'JKHY', 'JMU', 'KELYA', 'KELYB', 'KTEC', 'KTCC', 'KFRC', 'KE', 'KONE', 'KOPN', 'KLIC', 'KVHI', 'LRCX', 'LTRX', 'LSCC', 'LTRPA', 'LTRPB', 'LPTH', 'LECO', 'LPSN', 'LOGI', 'LOGM', 'LORL', 'MTSI', 'MGIC', 'MNGA', 'MAMS', 'MANH', 'MNTX', 'MRVL', 'MTCH', 'MTLS', 'MATR', 'MXIM', 'MGRC', 'MDCA', 'MTBC', 'MTBCP', 'MDSO', 'MLNX', 'MCHP', 'MU', 'MSCC', 'MSFT', 'MSTR', 'MIME', 'MNDO', 'MB', 'MIND', 'MINDP', 'MITK', 'MITL', 'MOBL', 'MOMO', 'MDB', 'MPWR', 'TYPE', 'MSDI', 'MSDIW', 'MOSY', 'MOXC', 'MYSZ', 'NNDM', 'NH', 'NATI', 'NETE', 'NTAP', 'NLST', 'NTCT', 'NTWK', 'NICE', 'NUAN', 'NTNX', 'NVEC', 'NVDA', 'NXPI', 'OIIM', 'OCLR', 'OKTA', 'OMCL', 'ON', 'OTIV', 'OTEX', 'OSIS', 'PFIN', 'PCYG', 'PRKR', 'PCTY', 'PCTI', 'PDFS', 'PEGA', 'PRFT', 'PERI', 'PLAB', 'PXLW', 'PLXS', 'PNTR', 'COOL', 'POWI', 'PSDO', 'IPDN', 'PRGS', 'PFPT', 'PTC', 'QADA', 'QADB', 'QRVO', 'QCOM', 'QSII', 'QBAK', 'QLYS', 'QTNA', 'QRHC', 'QUIK', 'QUMU', 'RDCM', 'RSYS', 'RMBS', 'RPD', 'RCMT', 'RNWK', 'RP', 'RCII', 'RESN', 'RBCN', 'RMBL', 'SABR', 'SANM', 'SPNS', 'SCSC', 'SGMS', 'SEAC', 'STX', 'SCWX', 'LEDS', 'SMTC', 'SGOC', 'SHSP', 'PIXY', 'SSTI', 'SWIR', 'SIFY', 'SIGM', 'SGMA', 'SILC', 'SLAB', 'SIMO', 'SPIL', 'SLP', 'SINA', 'SWKS', 'SGH', 'SMSI', 'SMTX', 'SRAX', 'SCKT', 'SOHU', 'SEDG', 'SOFO', 'RBBN', 'ANY', 'SPI', 'SPLK', 'SPSC', 'SSNC', 'STAF', 'SSYS', 'STRM', 'SPWR', 'SMCI', 'SPCB', 'SCON', 'SPRT', 'SYKE', 'SYMC', 'SYNC', 'SYNA', 'SNCR', 'SNPS', 'SYNT', 'TTWO', 'TLND', 'TECD', 'TCCO', 'TTEC', 'TXN', 'DSGX', 'KEYW', 'MIDD', 'TTD', 'ULTI', 'TNTR', 'TISA', 'TSEM', 'TACT', 'TZOO', 'TRIP', 'TRVG', 'TRUE', 'TSRI', 'TTMI', 'TCX', 'TWIN', 'UBNT', 'UCTT', 'UPLD', 'VRNS', 'VDSI', 'VECO', 'VRNT', 'VRSN', 'VRSK', 'VERI', 'VSAT', 'VIAV', 'VRTU', 'VUZI', 'WSTG', 'WEB', 'WB', 'WDC', 'WIX', 'WDAY', 'WSCI', 'XLNX', 'XPER', 'XPLR', 'XNET', 'YNDX', 'YY', 'ZBRA', 'ZIXI', 'ZNGA']
Transportation = ['AIRT', 'ATSG', 'ALGT', 'AAL', 'ARCB', 'AAWW', 'CHRW', 'CPLP', 'CVTI', 'CYRX', 'CYRXW', 'CSX', 'DCIX', 'DRYS', 'EGLE', 'ECHO', 'ESEA', 'EXPD', 'FWRD', 'GLBS', 'OMAB', 'HA', 'HTLD', 'HUBG', 'HUNT', 'HUNTU', 'HUNTW', 'JBHT', 'JBLU', 'LSTR', 'MRTN', 'ODFL', 'PTSI', 'PANL', 'PATI', 'PHII', 'PHIIK', 'PXS', 'RYAAY', 'SAIA', 'SHIP', 'SHIPW', 'SINO', 'SKYW', 'SAVE', 'SBLK', 'SBLKL', 'SBLKZ', 'GASS', 'STB', 'TOPS', 'ULH', 'USAK', 'WERN', 'YRCW']

AllCategories = BasicIndustries + CapitalGoods + ConsumerDurables + ConsumerNonDurables +\
    ConsumerServices + Energy + Finance + HealthCare + Miscellaneous + PublicUtilities +\
    Technology + Transportation

#writer
windowLength = 14