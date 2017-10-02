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

Testy specifikující detailní chování a možné použít ke kontrole opět včetně
skeletonu najdete v repozitáři [MarekSuchanek/labelord_tests](https://github.com/MarekSuchanek/labelord_tests)
ve větvi `flask`.

### Intro

Současná aplikace vám sice umožňuje snadno nastavit štítky pro více
repozitářů, ale přidávání nových štítků přes konfigurační soubor a spouštěním
`update` je nepraktické. Naštěstí GitHub vás může o změně štítků sám
informovat pomocí webhooku. Úkolem je vytvořit webovou aplikaci, která
takové zprávy přijme, zpracuje a příslušně změní štítky v ostatních
nastavených repozitářích. Díky tomu můžete vytvářet štítky odkudkoliv
přímo na GitHubu a aplikace se postará o master-to-master replikaci.

### Specifikace

1. Konfigurační soubor je totožný pro konzolovou i webovou aplikaci. Navíc
   se v sekci `[github]` přidá pouze položka `webhook_secret`. Jelikož je
   nutné umožnit spouštět aplikaci pomocí `flask run`, musí být umožněno
   specifikovat konfigurační soubor přes proměnnou prostředí `LABELORD_CONFIG`,
   výchozí hodnota zůstává totožná (`./config.cfg`).

2. Počáteční stav si uživatel aplikace provede pomocí již implementované
   CLI aplikace (`run update/replace`). Při startu webové aplikace se tedy
   pouze načte konfigurace ze souboru (neprobíhá žádná komunikace).

3. Mimo spouštění přes `flask run` je možné aplikaci spustit pomocí `click` příkazu `run_server`:
    * `--host`/`-h` = specifikace hostname (shodně jako `flask run`, výchozí `127.0.0.1`)
    * `--port`/`-p` = specifikace portu (shodně jako `flask run`, výchozí `5000`)
    * `--debug`/`-d` = debug mód (shodně jako nastavení `FLASK_DEBUG=true`, flag)
    * (dobrovolně) další možnosti z `flask run`

4. Informativní část aplikace = `GET /`:
    * Popisuje k čemu aplikace slouží.
    * Obsahuje seznam repozitářů, které jsou pomocí konfiguračního souboru
      povolené k replikaci (je jedno jestli použijete pro výpis tabulku,
      seznam nebo jinou formu).
    * Seznamu obsahuje odkazy na jednotlivé repozitáře na GitHubu (zkuste
      použít filtr).

5. Webhook část aplikace = `POST /`:
    * GitHub na tuto cestu zašle `POST` požadavek s informací o změně
      štítků a aplikace jej zpracuje - změny zpropaguje do ostatních repozitářů.
      Je nutné si dát pozor na to, že změna štítků provedená aplikací může opět
      vyvolat ze strany GitHubu požadavek s informací o změně.
    * Nejprve ověřte, že přijatý webhook má správný podpis (viz níže).
    * Poté zjistěte, zda zpráva obsahuje správnou událost a repozitář
      (je v seznamu povolených repozitářů k replikaci).
    * Vaše aplikace musí odpovědět na události `ping` a `label`.
    * Pro vyzkoušení, co GitHub posílá, doporučujeme https://requestb.in.
    * Použijte webhooky s obsahem typu `application/json`.

6. Přesné požadované chování včetně návratových kódů pro dané situace
   naleznete v dodaných testech.

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
některé funkce navíc se zachováním splnění testů (například přidávání,
kontrola a odstranění webhooku z repozitáře, spouštění `update` a `replace`
z webového rozhraní, znovunačtení konfigurace, vypisování aktuálních štítků
pro zadaný repozitář nebo  zobrazování rozdílů ve štítcích mezi vybranými
repozitáři) pro vyzkoušení si dalších možností  frameworku `flask` a dalších
pythonních knihoven. Pokud ale umožníte změny ve vašich repozitářích z
webové aplikace, pak byste ji měli adekvátně zabezpečit (například pomocí
[HTTP Basic Auth](https://en.wikipedia.org/wiki/Basic_access_authentication)
v kombinaci s HTTPS).

Během vývoje je vhodné využít i logování: http://flask.pocoo.org/docs/dev/logging/
