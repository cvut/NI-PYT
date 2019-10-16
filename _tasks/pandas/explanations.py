# Zdroj: https://www.policie.cz/clanek/statistika-nehodovosti-900835.aspx?q=Y2hudW09Mg%3d%3d

# Význam souborů 00.csv, 01.csv, ...  (chybějící jsou prázdné)
file_names = {'00.csv': 'nehody na území hl. m. Prahy',
 '01.csv': 'nehody na území Středočeského kraje',
 '02.csv': 'nehody na území Jihočeského kraje',
 '03.csv': 'nehody na území Plzeňského kraje',
 '04.csv': 'nehody na území Ústeckého kraje',
 '05.csv': 'nehody na území Královéhradeckého kraje',
 '06.csv': 'nehody na území Jihomoravského kraje',
 '07.csv': 'nehody na území Moravskoslezského kraje',
 '14.csv': 'nehody na území Olomouckého kraje',
 '15.csv': 'nehody na území Zlínského kraje',
 '16.csv': 'nehody na území kraje Vysočina',
 '17.csv': 'nehody na území Pardubického kraje',
 '18.csv': 'nehody na území Libereckého kraje',
 '19.csv': 'nehody na území Karlovarského kraje'}

# Jména sloupců v souborech 00.csv, 01.csv, ...
main_columns = ['identifikacni_cislo',
 'druh_pozemni_komunikace',
 'cislo_pozemni_komunikace',
 'den_mesic_rok',
 'weekday(p2a)',
 'cas',
 'druh_nehody',
 'druh_srazky_jedoucich_vozidel',
 'druh_pevne_prekazky',
 'charakter_nehody',
 'zavineni_nehody',
 'alkohol_u_vinika_nehody_pritomen',
 'hlavni_priciny_nehody',
 'usmrceno_osob',
 'tezce_zraneno_osob',
 'lehce_zraneno_osob',
 'celkova_hmotna_skoda',
 'druh_povrchu_vozovky',
 'stav_povrchu_vozovky_v_dobe_nehody',
 'stav_komunikace',
 'povetrnostni_podminky_v_dobe_nehody',
 'viditelnost',
 'rozhledove_pomery',
 'deleni_komunikace',
 'situovani_nehody_na_komunikaci',
 'rizeni_provozu_v_dobe_nehody',
 'mistni_uprava_prednosti_v_jizde',
 'specificka_mista_a_objekty_v_miste_nehody',
 'smerove_pomery',
 'pocet_zucastnenych_vozidel',
 'misto_dopravni_nehody',
 'druh_krizujici_komunikace',
 'druh_vozidla',
 'vyrobni_znacka_motoroveho_vozidla',
 'rok_vyroby_vozidla',
 'charakteristika_vozidla',
 'smyk',
 'vozidlo_po_nehode',
 'unik_provoznich_prepravovanych_hmot',
 'zpusob_vyprosteni_osob_z_vozidla',
 'smer_jizdy_nebo_postaveni_vozidla',
 'skoda_na_vozidle',
 'kategorie_ridice',
 'stav_ridice',
 'vnejsi_ovlivneni_ridice',
 'a',
 'b',
 'souradnice_x',
 'souradnice_y',
 'f',
 'g',
 'h',
 'i',
 'j',
 'k',
 'l',
 'n',
 'o',
 'p',
 'q',
 'r',
 's',
 't',
 'lokalita_nehody']

# Jména sloupců v souboru CHODCI.csv
ped_columns = ['identifikacni_cislo',
 'kategorie_chodce',
 'stav_chodce',
 'chovani_chodce',
 'situace_v_miste_nehody']

# Význam čísel v jednotlivých sloupcích
decode_key = {'alkohol_u_vinika_nehody_pritomen': {0: 'nezjišťováno',
                                      1: 'ano; obsah alkoholu v krvi do 0,24 ?',
                                      2: 'ne',
                                      3: 'ano; obsah alkoholu v krvi od 0,24 ? '
                                         'do 0,5 ?',
                                      4: 'pod vlivem drog',
                                      5: 'pod vlivem alkoholu a drog',
                                      6: 'ano; obsah alkoholu v krvi od 0,5 ? '
                                         'do 0,8 ?',
                                      7: 'ano; obsah alkoholu v krvi od 0,8 ? '
                                         'do 1,0 ?',
                                      8: 'ano; obsah alkoholu v krvi od 1,0 ? '
                                         'do 1,5 ?',
                                      9: 'ano; obsah alkoholu v krvi 1,5 ? a '
                                         'více'},
 'charakter_nehody': {1: 'nehoda; s následky na životě',
                      2: 'nehoda; pouze s hmotnou škodou'},
 'charakteristika_vozidla': {0: 'nezjištěno',
                             1: 'soukromé; nevyužívané k výdělečné činnosti',
                             2: 'soukromé; využívané k výdělečné činnosti',
                             3: 'soukromá organizace; (podnikatel, s.r.o., '
                                'v.o.s., a.s., atd.)',
                             4: 'veřejná hromadná doprava',
                             5: 'městská hromadná doprava',
                             6: 'mezinárodní kamionová doprava',
                             7: 'TAXI',
                             8: 'státní podnik, státní organizace',
                             9: 'registrované mimo území ČR',
                             10: 'zastupitelský úřad',
                             11: 'ministerstvo vnitra',
                             12: 'policie ČR',
                             13: 'městská, obecní policie',
                             14: 'soukromé bezpečnostní agentury',
                             15: 'ministerstvo obrany',
                             16: 'jiné',
                             17: 'odcizené',
                             18: 'vozidlo AUTOŠKOLY provádějící výcvik'},
 'chovani_chodce': {1: 'správné, přiměřené',
                    2: 'špatný odhad vzdálenosti a rychlosti vozidla',
                    3: 'náhlé vstoupení do vozovky; z chodníku, krajnice',
                    4: 'náhlé vstoupení do vozovky; z nástupního nebo dělícího '
                       'ostrůvku',
                    5: 'zmatené, zbrklé , nerozhodné jednání',
                    6: 'náhlá změna směru chůze',
                    7: 'náraz do vozidla z boku',
                    8: 'hra dětí na vozovce'},
 'deleni_komunikace': {0: 'žádná z uvedených',
                       1: 'dvoupruhová',
                       2: 'třípruhová',
                       3: 'čtyřpruhová s dělícím pásem',
                       4: 'čtyřpruhová s dělící čarou',
                       5: 'vícepruhová',
                       6: 'rychlostní komunikace'},
 'druh_krizujici_komunikace': {1: 'silnice 1. třídy',
                               2: 'silnice 2. třídy',
                               3: 'silnice 3. třídy',
                               6: 'místní komunikace',
                               7: 'účelová komunikace',
                               9: 'větev mimoúrovňové křižovatky'},
 'druh_nehody': {0: 'jiný druh nehody',
                 1: 'srážka; s jedoucím nekolejovým vozidlem',
                 2: 'srážka; s vozidlem zaparkovaným, odstaveným',
                 3: 'srážka; s pevnou překážkou',
                 4: 'srážka; s chodcem',
                 5: 'srážka; s lesní zvěří',
                 6: 'srážka; s domácím zvířetem',
                 7: 'srážka; s vlakem',
                 8: 'srážka; s tramvají',
                 9: 'havárie'},
 'druh_pevne_prekazky': {0: 'nepříchází v úvahu; nejedná se o srážku s pevnou '
                            'překážkou',
                         1: 'strom',
                         2: 'sloup; telefonní, veřejného osvětlení, '
                            'elektrického vedení, signalizace apod.',
                         3: 'odrazník, patník,; sloupek směrový, sloupek '
                            'dopravní značky apod.',
                         4: 'svodidlo',
                         5: 'překážka vzniklá provozem jiného vozidla; (např. '
                            'ztráta náikladu , výstroje vozidla nebo jeho '
                            'části)',
                         6: 'zeď, pevná část mostů,; podjezdů, tunelů apod.',
                         7: 'závory železničního přejezdu',
                         8: 'překážka vzniklá stavební činností; (přenosné '
                            'dopravní značky, hromada štěrku, písku nebo '
                            'jiného stavebního materiálu apod.)',
                         9: 'jiná překážka; (zábradlí, oplocení, násep, '
                            'nástupní ostrůvek apod.)'},
 'druh_povrchu_vozovky': {1: 'dlažba',
                          2: 'živice',
                          3: 'beton',
                          4: 'panely',
                          5: 'štěrk',
                          6: 'jiný nezpevněný povrch'},
 'druh_pozemni_komunikace': {0: 'dálnice',
                             1: 'silnice 1. třídy',
                             2: 'silnice 2. třídy',
                             3: 'silnice 3. třídy',
                             4: 'uzel; tj. křižovatka sledovaná ve vybraných '
                                'městech',
                             5: 'komunikace sledovaná; (ve vybraných městech)',
                             6: 'komunikace místní',
                             7: 'komunikace účelová; polní a lesní cesty atd.',
                             8: 'komunikace účelová; ostatní (parkoviště, '
                                'odpočívky apod.)'},
 'druh_srazky_jedoucich_vozidel': {0: 'nepřichází v úvahu; nejedná se o srážku '
                                      'jedoucích vozidel',
                                   1: 'čelní',
                                   2: 'boční',
                                   3: 'z boku',
                                   4: 'zezadu'},
 'druh_vozidla': {0: 'moped',
                  1: 'malý motocykl (do 50 ccm)',
                  2: 'motocykl (včetně sidecarů, skútrů apod.)',
                  3: 'osobní automobil bez přívěsu',
                  4: 'osobní automobil s přívěsem',
                  5: 'nákladní automobil (včetně multikáry, autojeřábu, '
                     'cisterny atd.)',
                  6: 'nákladní automobil s přívěsem',
                  7: 'nákladní automobil s návěsem',
                  8: 'autobus',
                  9: 'traktor (i s přívěsem)',
                  10: 'tramvaj',
                  11: 'trolejbus',
                  12: 'jiné motorové vozidlo; (zemědělské, lesní, stavební '
                      'stroje atd.)',
                  13: 'jízdní kolo',
                  14: 'povoz, jízda na koni',
                  15: 'jiné nemotorové vozidlo',
                  16: 'vlak',
                  17: 'nezjištěno, řidič ujel',
                  18: 'jiný druh vozidla'},
 'hlavni_priciny_nehody': {100: 'nezaviněná řidičem',
                           201: 'nepřizpůsobení rychlosti; intenzitě (hustotě) '
                                'provozu',
                           202: 'nepřizpůsobení rychlosti; viditelnosti (mlha, '
                                'soumrak, jízda v noci na tlumená světla '
                                'apod.)',
                           203: 'nepřizpůsobení rychlosti; vlastnostem vozidla '
                                'a nákladu',
                           204: 'nepřizpůsobení rychlosti; stavu vozovky '
                                '(náledí, výtluky, bláto, mokrý povrch apod.)',
                           205: 'nepřizpůsobení rychlosti; dopravně '
                                'technickému stavu vozovky (zatáčka, klesání, '
                                'stoupání, šířka vozovky apod.)',
                           206: 'překročení předepsané rychlosti stanovené '
                                'pravidly',
                           207: 'překročení rychlosti stanovené dopravní '
                                'značkou',
                           208: 'nepřizpůsobení rychlosti; bočnímu, nárazovému '
                                'větru (i při míjení, předjíždění vozidel)',
                           209: 'jiný druh nepřiměřené rychlosti',
                           301: 'předjíždění; vpravo',
                           302: 'předjíždění; bez dostatečného bočního odstupu',
                           303: 'předjíždění; bez dostatečného rozhledu (v '
                                'nepřehledné zatáčce nebo její blízkosti, před '
                                'vrcholem stoupání apod.)',
                           304: 'při předjíždění; došlo k ohrožení '
                                'protijedoucího řidiče vozidla (špatný odhad '
                                'vzdálenosti potřebné k předjetí apod.)',
                           305: 'při předjíždění; došlo k ohrožení '
                                'předjížděného řidiče vozidla (vynucené '
                                'zařazení, předjížděný řidič musel prudce '
                                'brzdit, měnit směr jízdy apod.)',
                           306: 'předjíždění; vlevo vozidla odbočujícího vlevo',
                           307: 'předjíždění; v místech, kde je to zakázáno '
                                'dopravní značkou',
                           308: 'při předjíždění; byla přejeta podélná čára '
                                'souvislá',
                           309: 'bránění v předjíždění',
                           310: 'přehlédnutí již předjíždějícícho souběžně '
                                'jedoucího vozidla',
                           311: 'jiný druh nesprávného předjíždění',
                           401: 'jízda na "červenou" 3-barevného semaforu',
                           402: 'proti příkazu dopravní značky; STŮJ DEJ '
                                'PŘEDNOST',
                           403: 'proti příkazu dopravní značky; DEJ PŘEDNOST',
                           404: 'vozidlu přijíždějícímu zprava',
                           405: 'při odbočování vlevo',
                           406: 'tramvají, která odbočuje',
                           407: 'protijedoucímu vozidlu při objíždění překážky',
                           408: 'při zařazování do proudu jedoucích vozidel ze '
                                'stanice, místa zastavení nebo stání',
                           409: 'při vjíždění na silnici',
                           410: 'při otáčení nebo couvání',
                           411: 'při přejíždění z jednoho jízdního pruhu do '
                                'druhého',
                           412: 'chodci na vyznačeném přechodu',
                           413: 'při odbočování vlevo; souběžně jedoucímu '
                                'vozidlu',
                           414: 'jiné nedání přednosti',
                           501: 'jízda po nesprávné straně vozovky, vjetí do '
                                'protisměru',
                           502: 'vyhýbání bez dostatečného bočního odstupu '
                                '(vůle)',
                           503: 'nedodržení bezpečné vzdálenosti za vozidlem',
                           504: 'nesprávné otáčení nebo couvání',
                           505: 'chyby při udání směru jízdy',
                           506: 'bezohledná, agresivní, neohleduplná jízda',
                           507: 'náhlé bezdůvodné snížení rychlosti jízdy, '
                                'zabrzdění nebo zastavení',
                           508: 'řidič se plně nevěnoval řízení vozidla',
                           509: 'samovolné rozjetí nezajištěného vozidla',
                           510: 'vjetí na nezpevněnou komunikaci',
                           511: 'nezvládnutí řízení vozidla',
                           512: 'jízda (vjetí) jednosměrnou ulicí, silnicí (v '
                                'protisměru)',
                           513: 'nehoda v důsledku  použití (policií) '
                                'prostředků k násilnému zastavení vozidla '
                                '(zastavovací pásy, zábrana, vozidlo atp.)',
                           514: 'nehoda v důsledku použití služební zbraně '
                                '(policií)',
                           515: 'nehoda při provádění služebního zákroku '
                                '(pronásledování pachatele atd.)',
                           516: 'jiný druh nesprávného způsobu jízdy',
                           601: 'závada řízení',
                           602: 'závada provozní brzdy',
                           603: 'neúčinná nebo nefungující parkovací brzda',
                           604: 'opotřebení běhounu pláště pod stanovenou mez',
                           605: 'defekt pneumatiky způsobený průrazem nebo '
                                'náhlým únikem vzduchu',
                           606: 'závada osvětlovací soustavy vozidla '
                                '(neúčinná, chybějící, znečištěná apod.)',
                           607: 'nepřipojená nebo poškozená spojovací hadice '
                                'pro bzrdění přípojného vozidla',
                           608: 'nesprávné uložení nákladu',
                           609: 'upadnutí, ztráta kola vozidla (i rezervního)',
                           610: 'zablokování kol v důsledku mechanické závady '
                                'vozidla (zadřený motor, převodovka, '
                                'rozvodovka, spadlý řetěz apod.)',
                           611: 'lom závěsu kola, pružiny',
                           612: 'nezajištěná nebo poškozená bočnice (i u '
                                'přívěsu)',
                           613: 'závada závěsu pro přívěs',
                           614: 'utržená spojovací hřídel',
                           615: 'jiná technická závada (vztahuje se i na '
                                'přípojná vozidla)'},
 'kategorie_chodce': {1: 'muž',
                      2: 'žena',
                      3: 'dítě (do 15 let)',
                      4: 'skupina dětí',
                      5: 'jiná skupina'},
 'kategorie_ridice': {0: 'nezjištěno; (např. u cizinců)',
                      1: 's řidičským oprávněním skupiny; A',
                      2: 's řidičským oprávněním skupiny; B',
                      3: 's řidičským oprávněním skupiny; C',
                      4: 's řidičským oprávněním skupiny; D',
                      5: 's řidičským oprávněním skupiny; T',
                      6: 's řidičským oprávněním skupiny; A a s omezením do 50 '
                         'ccm',
                      7: 'bez příslušného řidičského oprávnění',
                      8: 'ostatní řidiči vozidel; (např. cyklisté, vozkové, '
                         'strojvedoucí atd.)',
                      9: 'nezjištěno, řidič místo nehody opustil; (u p44 je '
                         'kód 17, nebo u p50a je kód 4)'},
 'lokalita_nehody': {1: 'v obci; vyplňí se i položka p5b', 2: 'mimo obec'},
 'mistni_uprava_prednosti_v_jizde': {0: 'žádná místní úprava',
                                     1: 'světelná signalilzace přepnuta na '
                                        'přerušovanou žlutou',
                                     2: 'světelná signalizace mimo provoz',
                                     3: 'přednost vyznačena dopravními '
                                        'značkami',
                                     4: 'přednost vyznačena přenosnými '
                                        'dopravními značkami nebo zařízením',
                                     5: 'přednost nevyznačena - vyplývá z '
                                        'pravidel silníčního provozu'},
 'misto_dopravni_nehody': {0: 'mimo křižovatku',
                           10: 'na kžižovatce; jedná-li se o křížení místních '
                               'komunikací, účelových komunikací nebo jde o '
                               'mezilehlou křižovatku (na sledovaném úseku ve '
                               'sledovaných městech)',
                           11: 'uvnitř zóny 1-8 předmětné křižovatky',
                           12: 'uvnitř zóny 1-8 předmětné křižovatky',
                           13: 'uvnitř zóny 1-8 předmětné křižovatky',
                           14: 'uvnitř zóny 1-8 předmětné křižovatky',
                           15: 'uvnitř zóny 1-8 předmětné křižovatky',
                           16: 'uvnitř zóny 1-8 předmětné křižovatky',
                           17: 'uvnitř zóny 1-8 předmětné křižovatky',
                           18: 'uvnitř zóny 1-8 předmětné křižovatky',
                           19: 'na křižovatce; uvnitř hranic křižovatky '
                               'definovaných pro systém evidence nehod (zóna '
                               '9)',
                           22: 'na vjezdové nebo výjezdové části větve při '
                               'mimoúrovňovém křížení',
                           23: 'na vjezdové nebo výjezdové části větve při '
                               'mimoúrovňovém křížení',
                           24: 'na vjezdové nebo výjezdové části větve při '
                               'mimoúrovňovém křížení',
                           25: 'na vjezdové nebo výjezdové části větve při '
                               'mimoúrovňovém křížení',
                           26: 'na vjezdové nebo výjezdové části větve při '
                               'mimoúrovňovém křížení',
                           27: 'na vjezdové nebo výjezdové části větve při '
                               'mimoúrovňovém křížení',
                           28: 'na vjezdové nebo výjezdové části větve při '
                               'mimoúrovňovém křížení',
                           29: 'mimo zónu 11-19 a 22-28'},
 'nasledky': {1: 'usmrcení',
              2: 'těžké zranění',
              3: 'lehké zranění',
              4: 'bez zranění'},
 'pohlavi_osoby': {1: 'muž',
                   2: 'žena',
                   3: 'chlapec (do 15 let)',
                   4: 'dívka (do 15 let)'},
 'poskytnuti_prvni_pomoci': {1: 'nebylo třeba poskytnout',
                             2: 'poskytnuta osádkou vozidel zúčastněných na '
                                'nehodě',
                             3: 'jinou osobou',
                             4: 'leteckou záchrannou službou',
                             5: 'vozidlem RZP',
                             6: 'neybyla poskytnuta, ale bylo nutno '
                                'poskytnout'},
 'povetrnostni_podminky_v_dobe_nehody': {0: 'jiné ztížené',
                                         1: 'neztížené',
                                         2: 'mlha',
                                         3: 'na počátku deště, slabý déšť, '
                                            'mrholení apod.',
                                         4: 'déšť',
                                         5: 'sněžení',
                                         6: 'tvoří se námraza, náledí',
                                         7: 'nárazový vítr (boční, vichřice '
                                            'apod.)'},
 'rizeni_provozu_v_dobe_nehody': {0: 'žádný způsob řízení provozu',
                                  1: 'policistou nebo jiným pověřeným orgánem',
                                  2: 'světelným signalizačním zařízením',
                                  3: 'místní úprava; vyplní se následující '
                                     'položka č. 24'},
 'rozhledove_pomery': {0: 'jiné špatné',
                       1: 'dobré',
                       2: 'špatné; vlivem okolní zástavby (budovy, plné '
                          'zábradlí apod.)',
                       3: 'špatné; vlivem průběhu komunikace, nebo podéllného '
                          'profilu nebo trasování (nepřehledný vrchol '
                          'stoupání, zářez komunikace apod.)',
                       4: 'špatné; vlivem vegetace - trvale (stromy, keře '
                          'apod.)',
                       5: 'špatné; vlivem vegetace - přechodně (tráva, obilí '
                          'apod.)',
                       6: 'výhled zakryt stojícím vozidlem'},
 'situace_v_miste_nehody': {0: 'jiná situace',
                            1: 'vstup chodce; na signál VOLNO',
                            2: 'vstup chodce; na signál STŮJ',
                            3: 'vstup chodce; do vozovky v blízkosti přechodu '
                               '(cca do 20 m)',
                            4: 'přecházení; po vyznačeném přechodu',
                            5: 'přecházení; těsně před nebo za vozidlem '
                               'stojícím v zastávce',
                            6: 'přecházení; těsně před nebo za vozidlem '
                               'parkujícím',
                            7: 'chůze,; stání na chodníku',
                            8: 'chůze; po správné straně',
                            9: 'chůze; po nesprávné straně',
                            10: 'přecházení; mimo přechod (20 a více metrů od '
                                'přechodu)'},
 'situovani_nehody_na_komunikaci': {0: 'žádné z uvedených',
                                    1: 'na jízdním pruhu',
                                    2: 'na odstavném pruhu',
                                    3: 'na krajnici',
                                    4: 'na odbočovacím, připojovacím pruhu',
                                    5: 'na pruhu pro pomalá vozidla',
                                    6: 'na chodníku nebo ostrůvku',
                                    7: 'na kolejích tramvaje',
                                    8: 'mimo komunikaci',
                                    9: 'na stezce pro cyklisty'},
 'smer_jizdy_nebo_postaveni_vozidla': {1: 'vozidlo jedoucí - ve měru staničení '
                                          '(na komunikaci)',
                                       2: 'vozidlo odstavené, parkující; - ve '
                                          'směru staničení (na komunikaci)',
                                       3: 'vozidlo jedoucí - proti směru '
                                          'staničení (na komunikaci)',
                                       4: 'vozidlo odstavené, parkující; - '
                                          'proti směru staničení (na '
                                          'komunikaci)',
                                       5: 'vozidlo jedoucí - na komunikaci bez '
                                          'staničení',
                                       6: 'vozidlo odstavené, parkující; - na '
                                          'komunikaci bez staničení',
                                       10: 'zachycuje postavení vozidla při '
                                           'nehodě na křižovatce',
                                       11: 'zachycuje postavení vozidla při '
                                           'nehodě na křižovatce',
                                       12: 'zachycuje postavení vozidla při '
                                           'nehodě na křižovatce',
                                       13: 'zachycuje postavení vozidla při '
                                           'nehodě na křižovatce',
                                       14: 'zachycuje postavení vozidla při '
                                           'nehodě na křižovatce',
                                       15: 'zachycuje postavení vozidla při '
                                           'nehodě na křižovatce',
                                       16: 'zachycuje postavení vozidla při '
                                           'nehodě na křižovatce',
                                       17: 'zachycuje postavení vozidla při '
                                           'nehodě na křižovatce',
                                       18: 'zachycuje postavení vozidla při '
                                           'nehodě na křižovatce',
                                       19: 'zachycuje postavení vozidla při '
                                           'nehodě na křižovatce',
                                       20: 'zachycuje postavení vozidla při '
                                           'nehodě na křižovatce',
                                       21: 'zachycuje postavení vozidla při '
                                           'nehodě na křižovatce',
                                       22: 'zachycuje postavení vozidla při '
                                           'nehodě na křižovatce',
                                       23: 'zachycuje postavení vozidla při '
                                           'nehodě na křižovatce',
                                       24: 'zachycuje postavení vozidla při '
                                           'nehodě na křižovatce',
                                       25: 'zachycuje postavení vozidla při '
                                           'nehodě na křižovatce',
                                       26: 'zachycuje postavení vozidla při '
                                           'nehodě na křižovatce',
                                       27: 'zachycuje postavení vozidla při '
                                           'nehodě na křižovatce',
                                       28: 'zachycuje postavení vozidla při '
                                           'nehodě na křižovatce',
                                       29: 'zachycuje postavení vozidla při '
                                           'nehodě na křižovatce',
                                       30: 'zachycuje postavení vozidla při '
                                           'nehodě na křižovatce',
                                       31: 'zachycuje postavení vozidla při '
                                           'nehodě na křižovatce',
                                       32: 'zachycuje postavení vozidla při '
                                           'nehodě na křižovatce',
                                       33: 'zachycuje postavení vozidla při '
                                           'nehodě na křižovatce',
                                       34: 'zachycuje postavení vozidla při '
                                           'nehodě na křižovatce',
                                       35: 'zachycuje postavení vozidla při '
                                           'nehodě na křižovatce',
                                       36: 'zachycuje postavení vozidla při '
                                           'nehodě na křižovatce',
                                       37: 'zachycuje postavení vozidla při '
                                           'nehodě na křižovatce',
                                       38: 'zachycuje postavení vozidla při '
                                           'nehodě na křižovatce',
                                       39: 'zachycuje postavení vozidla při '
                                           'nehodě na křižovatce',
                                       40: 'zachycuje postavení vozidla při '
                                           'nehodě na křižovatce',
                                       41: 'zachycuje postavení vozidla při '
                                           'nehodě na křižovatce',
                                       42: 'zachycuje postavení vozidla při '
                                           'nehodě na křižovatce',
                                       43: 'zachycuje postavení vozidla při '
                                           'nehodě na křižovatce',
                                       44: 'zachycuje postavení vozidla při '
                                           'nehodě na křižovatce',
                                       45: 'zachycuje postavení vozidla při '
                                           'nehodě na křižovatce',
                                       46: 'zachycuje postavení vozidla při '
                                           'nehodě na křižovatce',
                                       47: 'zachycuje postavení vozidla při '
                                           'nehodě na křižovatce',
                                       48: 'zachycuje postavení vozidla při '
                                           'nehodě na křižovatce',
                                       49: 'zachycuje postavení vozidla při '
                                           'nehodě na křižovatce',
                                       50: 'zachycuje postavení vozidla při '
                                           'nehodě na křižovatce',
                                       51: 'zachycuje postavení vozidla při '
                                           'nehodě na křižovatce',
                                       52: 'zachycuje postavení vozidla při '
                                           'nehodě na křižovatce',
                                       53: 'zachycuje postavení vozidla při '
                                           'nehodě na křižovatce',
                                       54: 'zachycuje postavení vozidla při '
                                           'nehodě na křižovatce',
                                       55: 'zachycuje postavení vozidla při '
                                           'nehodě na křižovatce',
                                       56: 'zachycuje postavení vozidla při '
                                           'nehodě na křižovatce',
                                       57: 'zachycuje postavení vozidla při '
                                           'nehodě na křižovatce',
                                       58: 'zachycuje postavení vozidla při '
                                           'nehodě na křižovatce',
                                       59: 'zachycuje postavení vozidla při '
                                           'nehodě na křižovatce',
                                       60: 'zachycuje postavení vozidla při '
                                           'nehodě na křižovatce',
                                       61: 'zachycuje postavení vozidla při '
                                           'nehodě na křižovatce',
                                       62: 'zachycuje postavení vozidla při '
                                           'nehodě na křižovatce',
                                       63: 'zachycuje postavení vozidla při '
                                           'nehodě na křižovatce',
                                       64: 'zachycuje postavení vozidla při '
                                           'nehodě na křižovatce',
                                       65: 'zachycuje postavení vozidla při '
                                           'nehodě na křižovatce',
                                       66: 'zachycuje postavení vozidla při '
                                           'nehodě na křižovatce',
                                       67: 'zachycuje postavení vozidla při '
                                           'nehodě na křižovatce',
                                       68: 'zachycuje postavení vozidla při '
                                           'nehodě na křižovatce',
                                       69: 'zachycuje postavení vozidla při '
                                           'nehodě na křižovatce',
                                       70: 'zachycuje postavení vozidla při '
                                           'nehodě na křižovatce',
                                       71: 'zachycuje postavení vozidla při '
                                           'nehodě na křižovatce',
                                       72: 'zachycuje postavení vozidla při '
                                           'nehodě na křižovatce',
                                       73: 'zachycuje postavení vozidla při '
                                           'nehodě na křižovatce',
                                       74: 'zachycuje postavení vozidla při '
                                           'nehodě na křižovatce',
                                       75: 'zachycuje postavení vozidla při '
                                           'nehodě na křižovatce',
                                       76: 'zachycuje postavení vozidla při '
                                           'nehodě na křižovatce',
                                       77: 'zachycuje postavení vozidla při '
                                           'nehodě na křižovatce',
                                       78: 'zachycuje postavení vozidla při '
                                           'nehodě na křižovatce',
                                       79: 'zachycuje postavení vozidla při '
                                           'nehodě na křižovatce',
                                       80: 'zachycuje postavení vozidla při '
                                           'nehodě na křižovatce',
                                       81: 'zachycuje postavení vozidla při '
                                           'nehodě na křižovatce',
                                       82: 'zachycuje postavení vozidla při '
                                           'nehodě na křižovatce',
                                       83: 'zachycuje postavení vozidla při '
                                           'nehodě na křižovatce',
                                       84: 'zachycuje postavení vozidla při '
                                           'nehodě na křižovatce',
                                       85: 'zachycuje postavení vozidla při '
                                           'nehodě na křižovatce',
                                       86: 'zachycuje postavení vozidla při '
                                           'nehodě na křižovatce',
                                       87: 'zachycuje postavení vozidla při '
                                           'nehodě na křižovatce',
                                       88: 'zachycuje postavení vozidla při '
                                           'nehodě na křižovatce',
                                       89: 'zachycuje postavení vozidla při '
                                           'nehodě na křižovatce',
                                       90: 'zachycuje postavení vozidla při '
                                           'nehodě na křižovatce',
                                       91: 'zachycuje postavení vozidla při '
                                           'nehodě na křižovatce',
                                       92: 'zachycuje postavení vozidla při '
                                           'nehodě na křižovatce',
                                       93: 'zachycuje postavení vozidla při '
                                           'nehodě na křižovatce',
                                       94: 'zachycuje postavení vozidla při '
                                           'nehodě na křižovatce',
                                       95: 'zachycuje postavení vozidla při '
                                           'nehodě na křižovatce',
                                       96: 'zachycuje postavení vozidla při '
                                           'nehodě na křižovatce',
                                       97: 'zachycuje postavení vozidla při '
                                           'nehodě na křižovatce',
                                       98: 'zachycuje postavení vozidla při '
                                           'nehodě na křižovatce',
                                       99: 'zachycuje postavení vozidla při '
                                           'nehodě na křižovatce'},
 'smerove_pomery': {1: 'přímý úsek',
                    2: 'přímý úsek po projetí zatáčkou; (do vzdálenosti cca '
                       '100 m od optického konce zatáčky)',
                    3: 'zatáčka',
                    4: 'křižovatka průsečná - čtyřramenná',
                    5: 'křižovatka styková - tříramenná',
                    6: 'křižovatka pěti a víceramenná',
                    7: 'kruhový objezd'},
 'smyk': {0: 'ne', 1: 'ano'},
 'specificka_mista_a_objekty_v_miste_nehody': {0: 'žádné nebo žádné z '
                                                  'uvedených',
                                               1: 'přechod pro chodce',
                                               2: 'v blízkosti přechodu pro '
                                                  'chodce (do vzdálenosti 20 '
                                                  'm)',
                                               3: 'železniční přejezd '
                                                  'nezabezpečený závorami ani '
                                                  'světelným výstražným '
                                                  'zařízením',
                                               4: 'železniční přejezd '
                                                  'zabezpečený',
                                               5: 'most, nadjezd, podjezd, '
                                                  'tunel',
                                               6: 'zastávka autobusu, '
                                                  'trolejbusu, tramvaje s '
                                                  'nástup. ostrůvkem',
                                               7: 'zastávka tramvaje, '
                                                  'autobusu, trolejbusu bez '
                                                  'nástup. ostrůvku',
                                               8: 'výjezd z parkoviště, lesní '
                                                  'cesty apod.  (pol. 36 = '
                                                  '7,8)',
                                               9: 'čerpadlo pohonných hmot',
                                               10: 'parkoviště přiléhající ke '
                                                   'komunikaci'},
 'stav_chodce': {0: 'nezjištěno',
                 1: 'dobrý; žádné nepříznivé okolnosti nebyly zjištěny',
                 2: 'nepozornost, roztržitost',
                 3: 'pod vlivem léků, narkotik',
                 4: 'pod vlivem alkoholu; obsah alkoholu v krvi do 0,99 ?',
                 5: 'fyzická indispozice; (nemoc, nevolnost, snížená '
                    'pohyblivost apod.)',
                 6: 'pokus o sebevraždu, sebevražda',
                 7: 'invalida',
                 8: 'jiný neuvedený stav',
                 9: 'pod vlivem alkoholu; obsah alkoholu v krvi 1 ? a více'},
 'stav_komunikace': {1: 'dobrý, bez závad',
                     2: "podélný sklon vyšší než 8 '%",
                     3: 'nesprávně umístěná, znečištěná, chybějící dopravní '
                        'značka',
                     4: 'zvlněný povrch v podélném směru',
                     5: 'souvislé výtluky',
                     6: 'nesouvislé výtluky',
                     7: 'trvalé zúžení vozovky',
                     8: 'příčná stružka, hrbol, vystouplé, propadlé kolejnice',
                     9: 'neoznačená nebo nedostatečně označená překážka na '
                        'komunikaci',
                     10: 'přechodná uzavírka jednoho jízdního pruhu',
                     11: 'přechodná uzavírka komunikace nebo jízdního pásu',
                     12: 'jiný (neuvedený) stav nebo závada komunikace'},
 'stav_povrchu_vozovky_v_dobe_nehody': {0: 'jiný stav povrchu vozovky v době '
                                           'nehody',
                                        1: 'povrch suchý; neznečištěný',
                                        2: 'povrch suchý; znečištěný (písek, '
                                           'prach, listí, štěrk atd.)',
                                        3: 'povrch mokrý',
                                        4: 'na vozovce je bláto',
                                        5: 'na vozovce je náledí, ujetý sníh; '
                                           '- posypané',
                                        6: 'na vozovce je náledí, ujetý sníh; '
                                           '- neposypané',
                                        7: 'na vozovce je rozlitý olej, nafta '
                                           'apod.',
                                        8: 'souvislá sněhová vrstva, rozbředlý '
                                           'sníh',
                                        9: 'náhlá změna stavu vozovky; '
                                           '(námraza na mostu, místní náledí)'},
 'stav_ridice': {0: 'jiný nepříznivý stav',
                 1: 'dobrý; žádné nepříznivé okolnosti nebyly zjištěny',
                 2: 'unaven, usnul, náhlá fyzická indispozice',
                 3: 'pod vlivem; léků, narkotik',
                 4: 'pod vlivem; alkoholu, obsah alkoholu v krvi do 0,99 ?',
                 5: 'pod vlivem; alkoholu, obsah alkoholu v krvi 1 ? a více',
                 6: 'nemoc, úraz apod.',
                 7: 'invalida',
                 8: 'řidič při jízdě zemřel (infarkt apod.)',
                 9: 'pokus o sebevraždu, sebevražda'},
 'unik_provoznich_prepravovanych_hmot': {0: 'žádné z uvedených',
                                         1: 'došlo k úniku pohonných hmot, '
                                            'oleje, chladícího média apod.',
                                         2: 'došlo k úniku jiných nebezpečných '
                                            'látek; - pevných',
                                         3: 'došlo k úniku jiných nebezpečných '
                                            'látek; - kapalných',
                                         4: 'došlo k úniku jiných nebezpečných '
                                            'látek; - plynných'},
 'viditelnost': {1: 've dne; viditelnost nezhoršená vlivem povětrnostních '
                    'podmínek',
                 2: 've dne; zhoršená viditelnost (svítání, soumrak)',
                 3: 've dne; zhoršená viditelnost vlivem povětrnostních '
                    'podmínek (mlha, sněžení, déšť apod.)',
                 4: 'v noci; s veřejným osvětlením, viditelnost nezhoršená '
                    'vlivem povětrnostních podmínek',
                 5: 'v noci; s veřejným osvětlením, zhoršená viditelnost '
                    'vlivem povětrnostních podmínek (mlha, déšť, sněžení '
                    'apod.)',
                 6: 'v noci; bez veřejného osvětlení, viditelnost nezhoršená '
                    'vlivem povětrnostních podmínek',
                 7: 'v noci; bez veřejného osvětlení, viditelnost zhoršená '
                    'vlivem povětrnostních podmínek (mlha, déšť, sněžení '
                    'apod.)'},
 'vnejsi_ovlivneni_ridice': {0: 'jiné ovlivnění',
                             1: 'řidič nebyl ovlivněn',
                             2: 'oslněn sluncem',
                             3: 'oslněn světlomety jiného vozidla',
                             4: 'ovlivněn jednáním jiného účastníka silničního '
                                'provozu',
                             5: 'ovlivněn při vyhýbání lesní zvěří, domácímu '
                                'zvířectvu apod.'},
 'vozidlo_po_nehode': {0: 'žádná z uvedených',
                       1: 'nedošlo k požáru',
                       2: 'došlo k požáru',
                       3: 'řidič ujel; - zjištěn',
                       4: 'řidič ujel (utekl); - nezjištěn'},
 'vyrobni_znacka_motoroveho_vozidla': {0: 'žádná z uvedených',
                                       1: 'ALFA-ROMEO',
                                       2: 'AUDI',
                                       3: 'AVIA',
                                       4: 'BMW',
                                       5: 'CHEVROLET',
                                       6: 'CHRYSLER',
                                       7: 'CITROEN',
                                       8: 'DACIA',
                                       9: 'DAEWOO',
                                       10: 'DAF',
                                       11: 'DODGE',
                                       12: 'FIAT',
                                       13: 'FORD',
                                       14: 'GAZ, VOLHA',
                                       15: 'FERRARI',
                                       16: 'HONDA',
                                       17: 'HYUNDAI',
                                       18: 'IFA',
                                       19: 'IVECO',
                                       20: 'JAGUAR',
                                       21: 'JEEP',
                                       22: 'LANCIA',
                                       23: 'LAND ROVER',
                                       24: 'LIAZ',
                                       25: 'MAZDA',
                                       26: 'MERCEDES',
                                       27: 'MITSUBISHI',
                                       28: 'MOSKVIČ',
                                       29: 'NISSAN',
                                       30: 'OLTCIT',
                                       31: 'OPEL',
                                       32: 'PEUGEOT',
                                       33: 'PORSCHE',
                                       34: 'PRAGA',
                                       35: 'RENAULT',
                                       36: 'ROVER',
                                       37: 'SAAB',
                                       38: 'SEAT',
                                       39: 'ŠKODA',
                                       40: 'SCANIA',
                                       41: 'SUBARU',
                                       42: 'SUZUKI',
                                       43: 'TATRA',
                                       44: 'TOYOTA',
                                       45: 'TRABANT',
                                       46: 'VAZ',
                                       47: 'VOLKSWAGEN',
                                       48: 'VOLVO',
                                       49: 'WARTBURG',
                                       50: 'ZASTAVA',
                                       51: 'AGM',
                                       52: 'ARO',
                                       53: 'AUSTIN',
                                       54: 'BARKAS',
                                       55: 'DAIHATSU',
                                       56: 'DATSUN',
                                       57: 'DESTACAR',
                                       58: 'ISUZU',
                                       59: 'KAROSA',
                                       60: 'KIA',
                                       61: 'LUBLIN',
                                       62: 'MAN',
                                       63: 'MASERATI',
                                       64: 'MULTICAR',
                                       65: 'PONTIAC',
                                       66: 'ROSS',
                                       67: 'SIMCA',
                                       68: 'SSANGYONG',
                                       69: 'TALBOT',
                                       70: 'TAZ',
                                       71: 'ZAZ',
                                       72: 'BOVA',
                                       73: 'IKARUS',
                                       74: 'NEOPLAN',
                                       75: 'OASA',
                                       76: 'RAF',
                                       77: 'SETRA',
                                       78: 'SOR',
                                       79: 'APRILIA',
                                       80: 'CAGIVA',
                                       81: 'ČZ',
                                       82: 'DERBI',
                                       83: 'DUCATI',
                                       84: 'GILERA',
                                       85: 'HARLEY',
                                       86: 'HERO',
                                       87: 'HUSQVARNA',
                                       88: 'JAWA',
                                       89: 'KAWASAKI',
                                       90: 'KTM',
                                       91: 'MALAGUTI',
                                       92: 'MANET',
                                       93: 'MZ',
                                       94: 'PIAGGIO',
                                       95: 'SIMSON',
                                       96: 'VELOREX',
                                       97: 'YAMAHA',
                                       98: 'jiné vyrobené v ČR',
                                       99: 'jiné vyrobené mimo ČR'},
 'zavineni_nehody': {0: 'jiné zavinění',
                     1: 'řidičem; motorového vozidla',
                     2: 'řidičem; nemotorového vozidla',
                     3: 'chodcem',
                     4: 'lesní zvěří, domácím zvířectvem',
                     5: 'jiným účastníkem silničního provozu',
                     6: 'závadou komunikace',
                     7: 'technickou závadou vozidla'},
 'zpusob_vyprosteni_osob_z_vozidla': {1: 'nebylo třeba užít násilí',
                                      2: 'použitím páčidel apod.',
                                      3: 'použitím speciální vyprošťovací '
                                         'techniky'}}
