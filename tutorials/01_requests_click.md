requests a click
================

Výukové materiály o virtuálním prostředí:
[naucse.python.cz](http://naucse.python.cz/2017/mipyt-zima/fast-track/install/),
[GitHub](https://github.com/pyvec/naucse.python.cz/tree/master/lessons/fast-track/install/).

Výukové materiály o requests:
[naucse.python.cz](http://naucse.python.cz/2017/mipyt-zima/intro/requests/),
[GitHub](https://github.com/pyvec/naucse.python.cz/tree/master/lessons/intro/requests).

Výukové materiály o clicku:
[naucse.python.cz](http://naucse.python.cz/2017/mipyt-zima/intro/click/),
[GitHub](https://github.com/pyvec/naucse.python.cz/tree/master/lessons/intro/click).

Úkol
----

Vaším úkolem za 5 bodů je vytvořit command line aplikaci pracující s [GitHub API](https://developer.github.com/v3/),
pomocí knihoven [requests](http://docs.python-requests.org) a [click](http://click.pocoo.org).
Hotovou aplikaci odevzdáte jako gitový repozitář na [GitHubu](https://github.com),
případně [fakultním GitLabu](https://gitlab.fit.cvut.cz). V obou případech
nám nezapomeňte [dát přístup](https://help.github.com/articles/inviting-collaborators-to-a-personal-repository/).

Vzhledem k tomu, že všichni máte stejné zadání, doporučujeme použít privátní
repozitář. Svůj kód můžete zveřejnit pod nějakou open-source licencí po našem
zkontrolování všech navazujících úloh.

Odkaz na repozitář nám pošlete e-mailem. Pro odevzdání v repozitáři prosím
nastavte tag `v0.1`.

Přesné rozhraní a chování třídy je dané přiloženými testy.
Testy najdete v repozitáři [MarekSuchanek/labelord_tests](https://github.com/MarekSuchanek/labelord_tests).

Termín odevzdání je u této úlohy mimořádně v pondělí (včetně) za 19 dní, termín je tedy shodný s příští úlohou.
Důrazně však doporučujeme odevzdat ji dříve.

### Intro

Aplikace bude sloužit pro globální správu štítků (labels), kterými se
na GitHubu označují issues, napříč více projekty. Cílem je usnadnit práci
s více repozitáři tak, aby nebylo nutné vytvářet štítky ručně u jednotlivých
repozitářů a aby byly všude stejné (barvy + názvy) dle zadané specifikace.

Terminálová aplikace musí splňovat požadavky na jednotlivé příkazy,
přepínače, výstupy a návratové kódy uvedené v tomto textu. To můžete
ověřovat pomocí poskytnutých testů (a měli byste).

### Konfigurace

Základním vstupem je konfigurační soubor ve formátu [INI](https://en.wikipedia.org/wiki/INI_file)
(použijte [ConfigParser](https://docs.python.org/3/library/configparser.html)),
některá nastavení lze ale provádět i jiným způsobem dle následujícího popisu.

Bez ohledu na zvolený příkaz se cesta ke konfiguračnímu souboru zadává
nepovinným přepínačem (option) `-c`/`--config`. Pokud není specifikován,
bere se výchozí cesta `./config.cfg` (avšak ani tento soubor nemusí existovat).

:bulb: Je vhodné do repozitáře vložit vzorový konfigurační soubor, aby uživatelé věděli, jak má vypadat, aniž by pročítali dokumentaci, a mohli jej použít jako šablonu.

#### GitHub token

GitHub token lze zadat třemi způsoby (seřazeno podle priority od nejmenší):

1. V konfiguračním souboru může být direktiva s tokenem (viz níže)

2. Token může být v proměnné prostředí `GITHUB_TOKEN` (hint: použijte [click](http://click.pocoo.org/6/arguments/#environment-variables))

3. Nejvyšší prioritu má hodnota přepínače `-t`/`--token`

```ini
[github]
token = MY_SECRET_TOKEN
```

Obdobně priorita funguje v celé aplikaci – argument/přepínač „vítězí“ nad
konfiguračním souborem.

Pokud aplikace nedostane token ani jednou cestou, tak musí vypsat na standardní
chybový výstup `No GitHub token has been provided` a skončit s kódem 3. V případě,
že je zadán neplatný token, program vypíše příslušné chybové hlášení (identické
z GitHubu *401*, viz testy) a skončí s kódem 4.

:exclamation: Dávejte pozor, aby se váš soukromý token neobjevil na GitHubu!

### Příkazy

Aplikace je rozdělena na jednotlivé příkazy realizující danou
požadovanou funkcionalitu.

#### list_repos

Aplikace na příkaz `list_repos` vypíše všechny repozitáře, se kterými může
na základě zadaného tokenu pracovat (na každý řádek jeden `owner/name`):

```console
$ python labelord.py --config my-config.cfg list_repos
MarekSuchanek/repo1
MarekSuchanek/repo2
CVUT/MI-PYT
```

Všechny ostatní GitHub chyby než *Bad credentials* končí kódem 10. GitHub
chybou se rozumí odpověď s jiným HTTP stavovým kódem, než je očekávaný.

#### list_labels

Aplikace na příkaz `list_labels <reposlug>` vypíše všechny štítky, které jsou
aktuálně pro zadaný repozitář nastavené (na každý řádek `#XXXXXX name`):

```console
$ python labelord.py --config my-config.cfg list_labels MarekSuchanek/repo1
#AaAaAa help wanted
#FF0000 bug
#00FF00 fixed
#0000FF feature request
```

Pokud není zadaný repozitář nalezen (*404*), program skončí s příslušným
chybovým hlášením a kódem 5. Všechny ostatní GitHub chyby končí kódem 10.

(Štítky musí zachovávat velikost písmen z konfiguračního souboru či z
GitHub API. Pořadí ve výpisu nehraje roli.)

#### run

Aplikace na příkaz `run` provede aktualizaci štítků. Úspěch či selhání se
signalizuje návratovým kódem a dle zvoleného režimu případně i výstupem.


##### Specifikace štítků

Specifikace štítků se může nacházet v konfiguračním souboru:

```ini
[labels]
Bug = FF0000
Last year = 23FB89
```

(Prázdný seznam je validní vstup. Pozor na zachování velikostí písma názvů štítků.)

Případně je možné specifikovat vzorový repozitář (vlastní nebo veřejný cizí)
pomocí `-r`/`--template-repo` nebo přes konfigurační soubor (vzorovy repozitář 
má přednost před specifikací štíků v konfigurační souboru):

```ini
[others]
template-repo = MarekSuchanek/myLabels
```

Pokud nejsou štítky specifikované ani jedním způsobem,
pak program na standardní chybový výstup vypíše
`No labels specification has been found`, skončí s kódem 6.

##### Specifikace repozitářů

Repozitáře, ve kterých program bude provádět změny, se definují opět
v konfiguračním souboru:

```ini
[repos]
MarekSuchanek/repo1 = on
MarekSuchanek/repo2 = on
CVUT/MI-PYT = off
```

(„Vypnutý“ repozitář se chová stejně, jako by tam nebyl.)

(Prázdný seznam je validní vstup. Použijte `getboolean` z `ConfigParser`.)

:exclamation: Klíče v konfiguračním souboru (v tomto případě názvy repozitářů) si `ConfigParser` převede na lowercase. Pro zachování velikosti písmen použijte před načtením souboru `cfg.optionxform = str`.

Nebo pomocí přepínače `-a`/`--all-repos` pro výběr všech dostupných
repozitářů (které vypíše `list_repos`).

Pokud nejsou repozitáře specifikované ani jedním způsobem,
pak program na standardní chybový výstup vypíše
`No repositories specification has been found`, skončí s kódem 7.

##### Módy

Módy (argument `run <mode>`):
* `update` = Pokud specifikovaný štítek s daným jménem v repozitáři
  neexistuje, je vytvořen s příslušnou barvou. V opačném případě je jeho
  barva upravena, je-li jiná než ve specifikaci. Štítky, které jsou v
  repozitáři *navíc* (jejich jméno není ve specifikaci), jsou ponechány.
* `replace` = Pracuje jako `update`, ale štítky *navíc* jsou odstraněny.

:bulb: Například pokud je specifikovaný prázdný seznam štítků, v módu `update` se nestane vůbec nic, ale v módu `replace` jsou odstraněny všechny štítky.

V případě, že uživatel zadá jiný mód nebo nezadá žádný, musí být informován
příslušnou chybovou hláškou a návratovým kódem. Ušetřete si práci a použijte
argument s typem `click.Choice` (viz [dokumentace pro option](http://click.pocoo.org/6/options/#choice-options)).

##### Běh na nečisto

Při běhu s přepínačem `-d`/`--dry-run` se program chová stejně (výpisy), ale
neprovádí žádné změny na GitHubu. Slouží ke zjištění potřebných změn, které
chce program provést.

Příklad výstup běhu na nečisto v režimu `verbose` (viz níže):

```
[ADD][DRY] MarekSuchanek/repo1; help wanted; AAAAAA
[DEL][DRY] MarekSuchanek/repo1; wont fix; ABBaBa
[LBL][ERR] MarekSuchanek/repo2; 404 - Not Found
[UPD][DRY] MarekSuchanek/repo3; help wanted; AAAAAA
[SUMMARY] 1 error(s) in total, please check log above
```

##### Výstup a chyby

Výstup aplikace je dán tím, zda je zvolen přepínač `-v`/`--verbose`,
`-q`/`--quiet` nebo ani jeden z nich (případně oba).

Pokud je zvoleno `-v`/`--verbose`, tak se následující vypisuje na standardní
výstup:

```
[ADD][SUC] MarekSuchanek/repo1; help wanted; AAAAAA
[DEL][ERR] MarekSuchanek/repo1; wont fix; ABBaBa; 500 - Internal Server Error
[LBL][ERR] MarekSuchanek/repo2; 404 - Not Found
[UPD][SUC] MarekSuchanek/repo3; help wanted; AAAAAA
[SUMMARY] 2 error(s) in total, please check log above
```

Pokud je zvoleno `-q`/`--quiet`, tak se logicky nevypisuje nic na
standardní výstup (ani chybový) a informací o běhu je pouze návratový kód.

V případě, že není zvolena ani jedna z předchozích, nebo jsou zvoleny obě,
pak se na chybový výstup vypisují chyby a na standardní výstup se vypíše shrnutí:
 - `SUMMARY: X repo(s) updated successfully`, (kód 0)
 - `SUMMARY: X error(s) in total, please check log above`, (kód 10)


```
ERROR: UPD; MarekSuchanek/repo1; ABC; CCaXXF; 422 - Validation Failed
ERROR: LBL; MarekSuchanek/repo2; 404 - Not Found
ERROR: ADD; pyvec/naucse.python.cz; ABC; CCaXXF; 404 - Not Found
SUMMARY: 3 error(s) in total, please check log above
```

Pro jednoduchost se vypisují chyby identické s těmi, které vrací GitHub
včetně chybového HTTP kódu. Hypotetický uživatel aplikace si pak chybu
zjistí v dokumentaci GitHub API (na kterou se můžete odkázat). Ostatní
chyby a nesprávná ukočení aplikace ošetřete volitelně nad rámec úlohy
(například případ selhání připojení k API - timeout).

Další detaily o výstupech a chování programu můžete zjistit v přiložených
testech, kterými musí vaše implementace projít.

#### Velikost znaků ve štítcích

* Při výpisu se vždy vypisují písmena podle vstupu z API nebo konfiguračního
souboru.
* Při změně hraje velikost znaků v barvě roli (například ve specifikaci je
#AAAAAA a na GitHubu u příslušného štítku #AAAaaa, update tento štítek
změní, ačkoliv se jedná o stejnou barvu a jen jiný zápis).
* Podobně je tomu i u názvů štítků. Štítek by měl být upraven pokud je ve
specifikaci napsáno "stejné" jméno jinak - například "Bug" a "bug".

#### Tagy ve výpisu

* `ADD` = Operace přidání štítku
* `UPD` = Operace aktualizace štítku
* `DEL` = Operace odstranění štítku
* `LBL` = Operace čtení štítků z repozitáře (pouze pokud dojde k chybě v 
této fázi)
* `DRY` = Operace proběhla v pořádku nanečisto (žádná reálná změna na GitHub)
* `SUC` = Operace proběhla v pořádku naostro
* `ERR` = Operace neproběhla v pořádku (indikace chyby)

------------------------------------------------------------------------

Ačkoliv je dodán předpřipravný skeleton společně s testy, které je nutné
splnit, fantazii se meze nekladou. Dobrovolně můžete udělat navíc další
možnosti, například možnost obarvení výstupu přepínačem `-y`/`--colorful`,
další styl výpisu nebo vstupu nebo i něco složitějšího (celý nový příkaz),
pokud si chcete vyzkoušet další pythonní knihovny a další funkce nad rámec
této úlohy. Dobré by také bylo, aby váš skript obsahoval informaci o verzi 
(--version).

### Referenční řešení

Naše refereční řešení si můžete prohlédnout zde: [v0.1@MarekSuchanek/labelord](https://github.com/MarekSuchanek/labelord/releases/tag/v0.1)
