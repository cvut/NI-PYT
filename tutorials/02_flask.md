Webové aplikace: Flask
======================

Výukové materiály:
[naucse.python.cz](http://naucse.python.cz/2017/mipyt-zima/intro/flask/),
[GitHub](https://github.com/pyvec/naucse.python.cz/tree/master/lessons/intro/flask).

Úkol
----

Vaším úkolem za 5 bodů je rozšířit command line aplikaci z minulého
cvičení o webové rozhraní. Stávající funkcionalita ale musí být zachována,
mimo konzole půjde tedy nevíc spustit web server a to pomocí `flask run` a
zároveň vlastním příkazem `run_server` (viz níže, hint: [application factory](http://flask.pocoo.org/docs/0.12/patterns/appfactories/)).

Výslednou aplikaci nasaďte na PythonAnywhere, nebo jiný veřejný hosting.
Odkaz na běžící aplikaci (včetně přihlašovacích údajů do aplikace) a
repozitář nám pošlete e-mailem. V repozitáři prosím nastavte tag `v0.2`.

Testy specifikující detailní chování a možné použít ke kontrole opět
najdete v repozitáři [MarekSuchanek/labelord_tests](https://github.com/MarekSuchanek/labelord_tests)
ve větvi `flask`.

### Intro

Současná aplikace vám sice umožňuje snadno nastavit štítky pro více
repozitářů, ale přidávání nových štítků přes konfigurační soubor a spouštěním
`update` je nepraktické. Naštěstí GitHub vás může o změně štítků sám
informovat pomocí webhooku. Úkolem je vytvořit webovou aplikaci, která
takové zprávy přijme, zpracuje a příslušně změní štítky v ostatních
nastavených repozitářích. Díky tomu můžete vytvářet štítky odkudkoliv
přímo na GitHubu a aplikace se postará o master-to-master replikaci.

### Požadavky

1. Konfigurační soubor je totožný pro konzolovou i webovou aplikaci. Navíc
   se v sekci `[github]` přidá položka `webhook_secret`. A v sekci `[web]`
   bude nastavení [HTTP Basic Auth](https://en.wikipedia.org/wiki/Basic_access_authentication)
   `username` a `password`.

2. Počáteční stav si uživatel aplikace provede pomocí již implementované
   CLI aplikace (`run update/replace`). Při startu aplikace se tedy pouze
   načte konfigurace ze souboru.

3. Mimo spouštění přes `flask run` je možné aplikaci spustit pomocí `click` příkazu `run_server`:
    * `--host`/`-h` = specifikace hostname (shodně jako `flask run`, výchozí `127.0.0.1`)
    * `--port`/`-p` = specifikace portu (shodně jako `flask run`, výchozí `5000`)
    * `--debug`/`-d` = debug mód (shodně jako nastavení `FLASK_DEBUG=true`, flag)
    * (dobrovolně) další možnosti z `flask run`

4. Aplikace má dvě části:

    * *Webhook část* - GitHub zašle požadavek s informací o změně štítků
      a aplikace jej zpracuje a změny zpropaguje do ostatních repozitářů.
      Tyto změny a pokusy o ně se logují do souboru. Je nutné si dát pozor
      na to, že změna štítků provedená aplikací opět vyvolá ze strany
      GitHubu požadavek s informací o změně.

    * *Administrační část* - umožňuje přístup k informacím o běhu aplikace
      a funkce pro znovunačtení konfiguračního souboru za běhu a přidání
      webhooku do repozitáře na GitHubu.

5. Obě části aplikace musí být ze zřejmých důvodů zabezpečené. Webhooky
   je možné zabezpečit položkou `secret` (viz níže). Administrační část
   musí být zabezpečena pomocí [HTTP Basic Auth](https://en.wikipedia.org/wiki/Basic_access_authentication)
   údaji z konfiguračního souboru (pokud nejsou oba nastavené, pak je
   zcela autentizace vypnuta).
   :exclamation: Pokud na veřejném hostingu nebudete mít také HTTPS, doporučujeme vytvořit si testovací účet na GitHub a použít ten.

6. Cesty v aplikaci

    * `GET /` (HTML)
        * úvodní statická stránka s informací o aplikaci a případně odkazy
    * `GET /repos` (HTML+JSON)
        * seznam spravovaných repozitářů (z konfiguračního souboru)
        * v JSON jako seznam řetězců
        * (dobrovolně) v HTML přidejte k repozitářům odkaz na GitHub, na
          stránku `/labels/<repo>` a také tlačítko pro odeslání AJAX
          požadavku `POST /repos/webhook` a zobrazení výsledku pomocí
          JavaScriptu. Na stránku pak můžete obdobně přidat i tlačítko
          pro AJAX `POST /reload`.
    * `GET /labels/<repo>` (HTML+JSON)
        * seznam aktuálních štítků pro zadaný repozitář
        * pro HTML použijte filtr pro zobrazení čtverečku s barvou štítku
          `colorbox` (název funkce `colorbox_filter`)
        * přijímá `repo` jako část URI (např. `/labels/MarekSuchanek/repo1`)
        * v JSON jako slovník název-barva
    * `POST /repos/webhook`
        * přidá webhook do zadaného repozitáře (pokud to lze)
        * přijímá `repo` jako data z formuláře - nikoliv jako část URI
    * `POST /hooks`
        * přijímá verifikované webhooks z GitHub
        * nejprve ověřte, že přijatý webhook má správný podpis (viz níže)
        * poté zjistěte, zda zpráva obsahuje správnou událost a repozitář
          (je v seznamu aktuálně povolených repozitářů)
        * váše aplikace musí odpovědět na události `ping` a `label`
        * pro vyzkoušení, co GitHub posílá, doporučujeme https://requestb.in
    * `POST /reload`
        * znovunačte konfigurační soubor (musíte si uchovat, z jakého souboru
          byla konfigurace načtena při startu)

JSON vracejte, pokud je preferováný typ pomocí `Accept` nastaven na
`application/json` a to i v případě chyb. V ostatních případech pošlete
HTML. Pro jednotlivé požadované chování, především vracení chyb si
prohlédněte poskytnuté testy.

#### Zabezpečení webhooku

Protože příjmání událostí z internetu může být riskantní,
nabízí Github možnost doplnit do vašeho webhooku `secret` položku.

Abyste rozpoznali, že vám událost poslal právě Github, je ke každému
requestu z Githubu přiložená hlavička `X-Hub-Signature`, např:
```
X-Hub-Signature: sha1=0b861d9a594a4f421cabcdef75d5aefc46df8967
```
která vám říká, že pokud použijete HMAC hexdigest
s odpovídající hash funkcí a s klíčem, který je právě uvedený v položce `secret`,
na celé tělo requestu a vámi spočítaný výsledek se shoduje s tím v hlavičce
`X-Hub-Signature`, tak tento request přišel z Githubu, z vámi zabezpečeného hooku
a dá se mu tedy věřit.
Více informací a příklad v Ruby je na [github securing].

[webhook]: https://developer.github.com/webhooks/
[github securing]: https://developer.github.com/webhooks/securing/

------------------------------------------------------------------------

Opět vám dodané testy poskytují příklady a detailní požadavky na implementace,
ale současně vás také značně omezují v kreativitě. Stále můžete ale přidat
některé funkce navíc se zachováním splnění testů (například kontrola a
odstranění webhooku z repozitáře, spouštění `update` a `replace` z webového
rozhraní nebo zobrazování rozdílů ve štítcích mezi vybranými repozitáři)
pro vyzkoušení si dalších možností  frameworku `flask` a dalších pythonních
knihoven.

Během vývoje je vhodné využít i logování: http://flask.pocoo.org/docs/dev/logging/

