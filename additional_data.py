# События из файла ga_hits.csv, которые считаются целевыми в данной задаче.
target_events = [
    'sub_car_request_submit_click', 'sub_car_claim_submit_click', 
    'sub_callback_submit_click', 'sub_call_number_click', 'sub_car_claim_click', 
    'sub_submit_success', 'sub_open_dialog_click']

# Значения, являющиеся пропусками.
missing_values = [float('nan'), '(none)', '(not set)', '0x0']

# Источники органического трафика в sessions['utm_medium'].
organic_mediums = ['organic', 'referral', '(none)']

# Идентификаторы социальных сетей в качестве источника.
social_media_sources = ['QxAxdyPLuQMEcrdZWdWb', 'MvfHsxITijuriZxsqZqt', 
                        'ISrKoXQCxqqYvAZICvjs', 'IZEXUFLARCUMynmHNBGo', 
                        'PlbkrSYoHuZBWfYjYnfw', 'gVRrcxiDQubJiljoTbGm']

# Города московской области.
moscow_region_cities = [
    'Aprelevka', 'Balashikha', 'Chekhov', 'Chernogolovka', 'Dedovsk', 
    'Dmitrov', 'Dolgoprudny', 'Domodedovo', 'Dubna', 'Dzerzhinsky', 
    'Elektrogorsk', 'Elektrostal', 'Elektrougli', 'Fryazino', 'Golitsyno', 
    'Istra', 'Ivanteyevka', 'Kalininets', 'Kashira', 'Khimki', 'Khotkovo', 
    'Klimovsk', 'Klin', 'Kolomna', 'Korolyov', 'Kotelniki', 'Krasnoarmeysk', 
    'Krasnogorsk', 'Krasnoznamensk', 'Kubinka', 'Kurovskoye', 
    'Likino-Dulyovo', 'Lobnya', 'Losino-Petrovsky', 'Lukhovitsy', 
    'Lytkarino', 'Lyubertsy', 'Mozhaysk', 'Mytishchi', 'Naro-Fominsk', 
    'Noginsk', 'Odintsovo', 'Orekhovo-Zuyevo', 'Pavlovsky Posad', 'Podolsk', 
    'Protvino', 'Pushchino', 'Pushkino', 'Ramenskoye', 'Reutov', 'Ruza', 
    'Sergiyev Posad', 'Serpukhov', 'Shatura', 'Shchyolkovo', 
    'Solnechnogorsk', 'Staraya Kupavna', 'Stupino', 'Vidnoye', 
    'Volokolamsk', 'Voskresensk', 'Yakhroma', 'Yegoryevsk', 'Zvenigorod']

# Крупные города России.
big_cities = ['Moscow', 'Saint Petersburg', 'Novosibirsk', 'Yekaterinburg', 
              'Kazan', 'Nizhny Novgorod', 'Chelyabinsk', 'Samara', 'Omsk', 
              'Rostov-on-Don', 'Ufa', 'Krasnoyarsk', 'Voronezh', 'Perm', 
              'Volgograd', 'Krasnodar', 'Saratov', 'Tyumen']

# Данные получены с помощью библиотеки `workalendar`. Сохранены в виде списка 
# для удобства. В реальном проекте лучше было бы получать данные напрямую из 
# библиотеки. 
russian_holidays = [
    '2021-01-01', '2021-01-02', '2021-01-03', '2021-01-04', '2021-01-05', 
    '2021-01-06', '2021-01-07', '2021-01-08', '2021-02-22', '2021-02-23', 
    '2021-03-08', '2021-05-01', '2021-05-03', '2021-05-09', '2021-05-10', 
    '2021-06-12', '2021-06-14', '2021-11-04', '2021-11-05', '2021-12-31', 
    '2022-01-01', '2022-01-02', '2022-01-03', '2022-01-04', '2022-01-05', 
    '2022-01-06', '2022-01-07', '2022-01-08', '2022-02-23', '2022-03-08', 
    '2022-05-01', '2022-05-02', '2022-05-09', '2022-06-12', '2022-06-13', 
    '2022-11-04', '2022-12-31']

# Расстояния получены с помощью библиотеки `geopy`. Сохранил их в словаре для 
# удобства и независимости от интернет соединения. В реальном проекте стоило бы 
# в реальном времени получать данные о расстоянии до Москвы или сохранить 
# данные в более удобном виде - в csv файл или базу данных. 
distances_from_moscow = {
    'zlatoust': 1391.263586320666,
    'moscow': 0.0,
    'krasnoyarsk': 3336.039749777034,
    'saint petersburg': 636.1695135872066,
    'sochi': 1361.357154793485,
    'yaroslavl': 251.13992274208584,
    'mytishchi': 19.15256793901058,
    'novorossiysk': 1226.5566120134847,
    'balashikha': 22.57464380465976,
    'pushkino': 32.29150343512499,
    'vladivostok': 6434.301687239597,
    'alexandrov': 99.03461742181614,
    'astrakhan': 1272.5934764474214,
    'reutov': 15.066736856880723,
    'kazan': 721.4395898259049,
    'ulyanovsk': 704.8643503547661,
    'tula': 173.37597779851754,
    'yekaterinburg': 1421.8971980595,
    'rostov-on-don': 959.8830610946284,
    'samara': 856.8315253096929,
    'domodedovo': 36.1846810301295,
    'yoshkar-ola': 645.0905459206801,
    'chelyabinsk': 1498.8592485500628,
    'krasnogorsk': 19.128893627152596,
    'krasnodar': 1114.8111085097096,
    'lipetsk': 353.93468708196895,
    'nakhabino': 29.34753329618301,
    'kyzyl': 3669.160067257817,
    'ryazan': 184.0749867936237,
    'tyumen': 1716.8034849522674,
    'omsk': 2243.230614478407,
    'nizhny novgorod': 403.1271008941555,
    'irkutsk': 3997.3240242086913,
    'mezhdurechensk': 3186.977397404048,
    'stupino': 100.50298403934347,
    'serpukhov': 93.79639415363022,
    'saratov': 727.5243756615845,
    'grozny': 1498.6390016944135,
    'orenburg': 1230.997301228693,
    'surgut': 2143.5097426260527,
    'volgograd': 913.40653000604,
    'engels': 734.1820123219143,
    'fryazino': 35.68825436908673,
    'naberezhnye chelny': 926.5455187130812,
    'khabarovsk': 5955.703005291212,
    'ufa': 1168.153047105715,
    'novosibirsk': 2820.763592183317,
    'kirov': 793.5857281587636,
    'kotelniki': 18.556201509278427,
    'kaluga': 162.98501946171325,
    'vyborg': 758.2625638645857,
    'barnaul': 2943.257935404941,
    'tambov': 419.072146029825,
    'tver': 162.03184502252185,
    'korolyov': 23.240966914958825,
    'kostroma': 302.3271334606748,
    'zheleznodorozhny': 1051.3212963591216,
    'dolgoprudny': 21.451753870279653,
    'kursk': 456.3676328552856,
    'pyatigorsk': 1359.1346795165907,
    'khimki': 19.27787504978214,
    'dubna': 113.336078534706,
    'izhevsk': 970.8632565557036,
    'chita': 4752.38859817778,
    'cherkessk': 1319.672066231367,
    'blagoveshchensk': 5630.258195023883,
    'bryansk': 349.6394555186336,
    'voronezh': 467.015180857099,
    'kolomna': 103.33805649619023,
    'nalchik': 1430.5028996363571,
    'obninsk': 96.82910844583522,
    'belgorod': 577.7869858749181,
    'perm': 1170.262093684163,
    'severodvinsk': 989.3463180226084,
    'gatchina': 616.369780994091,
    'syktyvkar': 1007.3633668496318,
    'naro-fominsk': 68.51450800685191,
    'protvino': 101.15152863427636,
    'kamensk-uralsky': 1506.829417564834,
    'zhukovskiy': 600.4219593564324,
    'tomsk': 2655.7361007309364,
    'stavropol': 1278.9876969538484,
    'ivanteyevka': 31.051927448382365,
    'yegoryevsk': 98.37617987397816,
    'magnitogorsk': 1399.4447582737268,
    'vidnoye': 22.273670822552017,
    'abakan': 3386.4037130516103,
    'kraskovo': 24.96235703886392,
    'safonovo': 286.2924673657379,
    'shlisselburg': 608.2272247268463,
    'cherepovets': 376.65445395984784,
    'arkhangelsk': 992.6837722348444,
    'lyubertsy': 19.131687885364908,
    'vologda': 578.1169534315311,
    'petrozavodsk': 697.9721736505935,
    'oryol': 325.58358692835327,
    'odintsovo': 23.396555594006895,
    'voskresensk': 82.36561436203819,
    'almetyevsk': 934.756507490178,
    'veliky novgorod': 492.2434986334845,
    'kovrov': 240.34824684527445,
    'ramenskoye': 43.322630130479546,
    'berezniki': 1212.7987454012757,
    'shchyolkovo': 30.14037479489325,
    'novocheboksarsk': 617.6614496689281,
    'maykop': 1252.0417154745587,
    'nefteyugansk': 2101.016020281276,
    'tomilino': 587.5370629562508,
    'kaliningrad': 1091.7810203900708,
    'vladimir': 179.35415952478112,
    'velikiye luki': 446.4897914407206,
    'nakhodka': 6512.826751067336,
    'nizhnevartovsk': 2316.101568624056,
    'nevinnomyssk': 1274.9648982402225,
    'klin': 85.25341211585662,
    'uchaly': 1395.0694573085807,
    'novy urengoy': 2357.070596933191,
    'smolensk': 370.11957641629294,
    'dedovsk': 33.44282124708212,
    'sergiyev posad': 70.71201081392101,
    'vsevolozhsk': 629.8608377734972,
    'dmitrov': 66.48470950822428,
    'cheboksary': 602.6003537044186,
    'podolsk': 35.868186236649,
    'pervouralsk': 1380.892115200903,
    'anapa': 1207.7697317191653,
    'lytkarino': 26.171266900562145,
    'kopeysk': 1513.6217762611632,
    'tosno': 582.7586696635991,
    'norilsk': 2890.251515258955,
    'tolyatti': 799.8381096242144,
    'temryuk': 1165.3624515813908,
    'ussuriysk': 6381.347211888504,
    'istra': 50.88951924026617,
    'murmansk': 1491.035365952789,
    'ivanovo': 249.58733461631263,
    'verkhnyaya pyshma': 1418.646108882692,
    'maloyaroslavets': 110.21255938028736,
    'tikhvin': 496.9134080491585,
    'neryungri': 5028.977481470272,
    'kurgan': 1630.4830408964883,
    'novomoskovsk': 198.39912622251103,
    'kemerovo': 2996.19975700017,
    'volokolamsk': 108.56175176242488,
    'elektrostal': 51.84872232603937,
    'essentuki': 1354.1058476615915,
    'kislovodsk': 1365.9041690419383,
    'malakhovka': 26.99082254199157,
    'orekhovo-zuyevo': 85.6729405699771,
    'angarsk': 4178.283677448494,
    'chekhov': 68.44709881944979,
    'severomorsk': 1499.3047699096576,
    'leninsk-kuznetskiy': 3024.4663354351296,
    'satka': 1353.5254445419057,
    'dzerzhinsk': 368.59794417334047,
    'хомутово': 6668.791623791499,
    'penza': 556.0305682853448,
    'biysk': 3068.7132170237933,
    'novokuznetsk': 3127.6022996940287,
    'lobnya': 30.440525152635374,
    'sterlitamak': 1201.8214869231806,
    'naryan-mar': 1546.3123404691437,
    'kamyshin': 819.0343184384951,
    'artyom': 6430.381425066174,
    'yurga': 2914.0593434459674,
    'asbest': 1471.9556267379069,
    'sertolovo': 656.4737697387209,
    'staraya kupavna': 35.69475828769861,
    'volzhskiy': 915.5424228748903,
    'yuzhno-sakhalinsk': 6662.822265097304,
    'dzerzhinsky': 19.755817456584587,
    'krasnoznamensk': 40.16986859789947,
    'ulan-ude': 4432.539381037524,
    'zarechnyy': 606.0887567751221,
    'kostomuksha': 1057.376319264544,
    'povarovo': 50.52734489960697,
    'meleuz': 1226.2104294516412,
    'nazran': 1483.2725769944918,
    'klimovsk': 42.08840658931683,
    'stary oskol': 495.74079214243545,
    'vorkuta': 1891.6302759858595,
    'poltavskaya': 1155.8248883948718,
    'lukhovitsy': 125.0361461564636,
    'beloozyorskiy': 61.073850334859074,
    'elektrougli': 38.19286528690888,
    'chebarkul': 1438.8690266914327,
    'pskov': 611.6967383817062,
    'ukhta': 1249.5980588134028,
    'ruza': 89.5764906198789,
    'nizhny tagil': 1377.8498180844908,
    'yakutsk': 4901.163764820078,
    'khotkovo': 60.72433440755533,
    'elista': 1148.3051053640338,
    'bratsk': 3852.601801304402,
    'noginsk': 52.95761210648052,
    'makhachkala': 1587.5655360528883,
    'vladikavkaz': 1503.498930286972,
    'belovo': 3048.147193273616,
    'frolovo': 780.2333467253039,
    'petropavlovsk-kamchatskiy': 6798.018682170094,
    'borovichi': 370.0201002038788,
    'kratovo': 38.27502643887081,
    'prokopyevsk': 3097.586118228412,
    'seversk': 2878.478697347678,
    'rybinsk': 266.62620678639803,
    'pereslavl-zalessky': 133.65119287257676,
    'taganrog': 953.8988301108136,
    'novouralsk': 1387.9078797741597,
    'gelendzhik': 1245.0497234965765,
    'aramil': 1438.094504062841,
    'neftekamsk': 1037.9314586718494,
    'novotroitsk': 1457.0530345108157,
    'tuapse': 1300.1385167816816,
    'mozhaysk': 103.83921583291148,
    'sarov': 373.8154496798572,
    'kimry': 126.08756924425133,
    'kubinka': 61.218046614594186,
    'zheleznogorsk': 3391.850347906158,
    'saransk': 514.5759444962858,
    'dimitrovgrad': 784.9888159828704,
    'slavyansk-na-kubani': 1167.5855361519575,
    'tikhoretsk': 1114.786471927972,
    'salekhard': 1940.798233727196,
    'ostrov': 596.0147871697434,
    'kommunar': 609.0316563952802,
    'tsivilsk': 617.608810996026,
    'shakhty': 911.990910602426,
    'pechora': 1487.3071484483453,
    'svetogorsk': 784.6154471409538,
    'megion': 2289.965764352699,
    'bataysk': 969.330021045852,
    'kirishi': 530.8309526915012,
    'komsomolsk-on-amur': 6086.29642220532,
    'novocherkassk': 943.5609192173324,
    'chernogolovka': 55.75814822209252,
    'gorki-2': 727.7907922818495,
    'gus-khrustalny': 192.64146200083803,
    'berdsk': 2842.4371674583103,
    'lysva': 1251.2694243399262,
    'korsakov': 6693.46814234493,
    'sovetsk': 996.7695220314324,
    'aprelevka': 41.18219415362496,
    'semibratovo': 209.0654774418882,
    'pavlovsky posad': 64.94947986028654,
    'bor': 406.57781172305175,
    'magadan': 5696.766522816334,
    'kstovo': 413.3420040082879,
    'shatura': 122.7240473979108,
    'losino-petrovsky': 39.0856643165014,
    'yalutorovsk': 1770.7930860972722,
    'ust-ilimsk': 3824.762306477272,
    'pushchino': 101.94688109279312,
    'polysayevo': 3038.5975501321755,
    'prokhladny': 1409.5731328427237,
    'tobolsk': 1866.1259900513485,
    'birobidzhan': 6025.667074308183,
    'lipitsy': 488.33181946214216,
    'volgodonsk': 968.7193376964842,
    'yeysk': 1006.6702432800072,
    'golitsyno': 42.32796602639879,
    'miass': 1420.4111070245615,
    'yelets': 352.953027033769,
    'zvenigorod': 47.72843063332915,
    'selyatino': 47.81307831562977,
    'volkhov': 561.0120810417935,
    'krasnoarmeysk': 52.84859748189735,
    'apatity': 1335.0174311357218,
    'solnechnogorsk': 62.75797256121989,
    'buynaksk': 1591.6091181217846,
    'bolshoy kamen': 6459.6647658063575,
    'noyabrsk': 2258.5967649018207,
    'tynda': 5133.7148203026745,
    'nizhnekamsk': 891.351444472025,
    'usolye-sibirskoye': 4152.668391343766,
    'kingisepp': 673.0970220244146,
    'zelenodolsk': 682.4973369990087,
    'glazov': 950.3194914895024,
    'achinsk': 3216.780147934828,
    'rodniki': 295.0464136688749,
    'shelekhov': 4209.77264099612,
    'kaspiysk': 1601.679936799069,
    'birsk': 1127.659719672664,
    'nadym': 2157.8430358400265,
    'gorno-altaysk': 3143.3301534511943,
    'kolchugino': 3029.386251308493,
    'kushchyovskaya': 1034.055831067238,
    'yuzhnyy': 3482.931087966988,
    'armavir': 1221.3111343868295,
    'mozhga': 909.9695253925483,
    'vyksa': 292.00651478106886,
    'uzlovaya': 200.30676600029304,
    'rostov': 959.8830610946284,
    'kirovsk': 605.2671113612804,
    "ul'yanovka": 192.0411085381513,
    'novoaltaysk': 2950.9705068425405,
    'kamensk-shakhtinsky': 846.2139538784264,
    'ozersk': 1442.8560961441965,
    'elektrogorsk': 74.63716516619932,
    'arzamas': 394.35402804220274,
    'snezhinsk': 1438.9690430594771,
    'borisoglebsk': 569.9580301479704,
    'mirny': 4170.726504147512,
    'vyazniki': 287.308764186897,
    'enem': 1207.821030982559,
    'nyagan': 1734.888769945378,
    'khanty-mansiysk': 1906.792032820939,
    'monino': 37.715349372745926,
    'mineralnye vody': 1342.0944633137724,
    'verkhnyaya salda': 1413.7297090555912,
    'russkiy': 1213.062834379814,
    'revda': 1379.6717524046908,
    'lesnoy gorodok': 28.475504020539947,
    'argun': 1506.098028834171,
    'kyshtym': 1434.2595681626117,
    'salavat': 1210.078586205624,
    'tuchkovo': 74.30089302855156,
    'kumertau': 1226.5856038134475,
    'polevskoy': 1399.151300955637,
    'mikhaylovka': 734.9935677109922,
    'murom': 279.2759175366648,
    'kineshma': 335.5996758437128,
    'kandalaksha': 1299.3304879892798,
    'krasnouralsk': 1384.2334857967037,
    'torzhok': 217.4706587749375,
    'yuzhnouralsk': 1509.4408603749698,
    'shuya': 263.59454702063505,
    'serov': 1426.9672333775843,
    'sosnovy bor': 685.2323134899109,
    'shadrinsk': 1617.147870036188,
    'kotlas': 806.4754172091222,
    'novotitarovskaya': 1173.4741472213989,
    'balakovo': 787.8822091993675,
    '83709': 3202.813333769226,
    'azov': 968.9726699294038,
    'kirovo-chepetsk': 811.8571178014768,
    'rubtsovsk': 2872.4015656846614,
    'kirzhach': 90.62652039638547,
    'anadyr': 6213.777177759523,
    'khasavyurt': 1531.9145979750529,
    'beryozovsky': 1433.634294395171,
    'derbent': 1707.4033646935634,
    'dubovoe': 414.1453826358143,
    'vyazma': 217.54174988855237,
    'pyt-yakh': 2113.4245970564507,
    'semender': 1583.4934150903011,
    'nikolskoye': 598.9997361692872,
    'kashira': 107.13368440394626,
    'kizlyar': 1473.3798545362304,
    'zarinsk': 2997.181989822133,
    'konakovo': 119.1786549464336,
    'kurumoch': 839.7114992062343,
    'udomlya': 285.6169847200254,
    'minusinsk': 3402.637804653251,
    'kropotkin': 1166.2245607801617,
    'aleksandrovsk-sakhalinskiy': 6299.8823011927725,
    'pavlovo': 342.2607377444623,
    'otradny': 924.9037500182482,
    'aksay': 956.2965486068668,
    'balakhna': 381.1579987404556,
    'monchegorsk': 1379.666459717234,
    'kurchatov': 473.2883426264815,
    'orsk': 1466.0377255809008,
    'beloretsk': 1344.6724341902625,
    'vyshny volochyok': 276.9809306440123,
    'plastunovskaya': 1168.6851720045977,
    'nizhnyaya tura': 1375.9166273461458,
    'poronaysk': 6485.758764373887,
    'oktyabrsky': 1018.8184366705572,
    'shakhovskaya': 135.50534368151105,
    'kizilyurt': 1545.4401863233754,
    'chistopol': 821.3604105474976,
    'kansk': 3517.5408678268373,
    'inta': 1658.5575397677376,
    'novoshakhtinsk': 903.6507811060995,
    'kartaly': 1517.4593040784584,
    'kurovskoye': 84.3681700784244,
    'kuznetsk': 652.0791300259867,
    'rossosh': 631.8948563881265,
    'samarskoye': 990.9463636012208,
    'usinsk': 1560.1926768575506,
    'kanevskaya': 1079.414438120802,
    'lyuban': 552.7103608674508,
    'dalnegorsk': 6509.488452820776,
    'urus-martan': 1513.9438781256622,
    'votkinsk': 1018.7575282525304,
    'katav-ivanovsk': 1309.0842038516064,
    'olginka': 1287.7238993616631,
    'yakhroma': 60.64340421625101,
    'novokuybyshevsk': 851.6052629828683,
    'ishimbay': 1214.0401210017262,
    'sosnovoborsk': 3386.3759431879366,
    'gudermes': 1506.983332793841,
    'labytnangi': 1937.057017992013,
    'likino-dulyovo': 84.31241624220513,
    'lodeynoye pole': 604.1151265677914,
    'syzran': 760.0979681269697,
    'belaya kalitva': 870.3865327785855,
    'spassk-dalny': 6362.30839868133,
    'belorechensk': 1232.6961732990508,
    'sarapul': 1008.78232479936,
    'raduzhny': 2358.496974772968,
    'trudovoye': 1090.3401905593514,
    'kinel': 887.7664648811271,
    'korkino': 1505.8826336695265,
    'kiselyovsk': 3086.31280001039,
    'berezovka': 1087.264673590551,
    'goryachevodsky': 1360.7786042757737,
    'michurinsk': 369.2508261957532,
    'bobrovskiy': 322.39759418097685,
    'chegem': 1420.378254627167,
    'yelizovo': 6772.820421777107,
    '53425': 3202.813333769226,
    'тимофеевка': 1006.6834116656815,
    'ust-labinsk': 1180.6818380079214,
    'starokorsunskaya': 1196.1976393224706,
    'tarko-sale': 2388.9780271861964,
    'kachkanar': 1354.197212226372,
    'iskitim': 2858.9099151934147,
    'sibay': 1407.2647547506033,
    'vlasikha': 2933.2726322389262,
    '8756': 10.730176534095364,
    'agoi': 1294.7427424182354,
    'priozersk': 733.1545071632743,
    'bologoye': 321.9803937484453,
    'тарасовка': 1491.2541362483853,
    'beloyarsky': 1836.5384486488076,
    'ust-katav': 1302.724181677159,
    'kanash': 622.9255607421362,
    'dagestanskie ogni': 1698.208239037858,
    'belogorsk': 5631.125637486317,
    'labinsk': 1255.8319936717032,
    'lyskovo': 465.1306258788371,
    'afipsky': 1208.3956944522176,
    'starnikovo': 65.1332863630618,
    'juravskaia': 1139.1135698400817,
    'korenovsk': 1151.523891415271,
    'znamenskiy': 1194.8142115320263,
    'slavgorod': 2644.610086488067,
    'kungur': 1200.4961224183248,
    'gadzhiyevo': 1519.9109169685858,
    'shchyokino': 194.4698174383533,
    'nogliki': 6268.259965863986,
    '39404': 3202.813333769226,
    'lenina': 1199.0498830456509,
    'gaiduk': 1219.513851211696,
    '9992': 982.845979460969,
    'marks': 751.1509601828144,
    'kugesi': 606.0520067073529,
    'solikamsk': 1216.98913220201,
    'bryukhovetskaya': 1111.082927529371,
    'slavyanka': 6428.684709591151,
    '24130': 3202.813333769226,
    'menzelinsk': 970.9489283044122,
    'vysokaya gora': 724.5834162625722,
    'vanino': 6362.894335239535,
    'malysheva': 1467.3592923926346,
    'korzhevskiy': 1171.954752073123,
    'troitsk': 1538.140668806304,
    'nizhnebakanskaya': 1210.9986252672918,
    'plast': 1482.6858068116453,
    'gorodishche': 591.2765666147258,
    'osinovo': 736.6860205116334,
    'zavidovo': 353.2224718264869,
    'zarechny': 1465.4555186281548,
    'novaya adygeya': 1196.6866369650947,
    'kholmsk': 6621.858284986929,
    'asha': 1245.1907526999598,
    '14076': 3202.813333769226,
    'petrovskoye': 385.1673685384485,
    'chernyakhovsk': 1012.0952920550218,
    'salsk': 1067.2210501046166,
    'argayash': 1458.8443906207276,
    '13403': 1152.7191232199125,
    'bavly': 1006.55370599998,
    'beslan': 1482.7229051085862}


def get_distance_from_moscow(city: str) -> float:
    """Возвращает расстояние от города `city` до Москвы в километрах. 
    Для неизвестных и зарубежных городов возвращает -1.
    """

    return distances_from_moscow.get(str(city).lower(), -1.0)