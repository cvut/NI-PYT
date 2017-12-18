# Generátory a AsyncIO

Výukové materiály:
[naucse.python.cz](http://naucse.python.cz/2017/mipyt-zima/intro/async/),
[GitHub](https://github.com/pyvec/naucse.python.cz/tree/master/lessons/intro/async).

## Úkol

Vaším úkolem za 5 bodů je implementovat funkci `gather_acquaintances`, která pomocí asynchronní komunikace s [GitHub API] (včetně [GitHub Search API]) ze všech* issues podle zadané specifikace zjistí všechny uživatele, kteří tyto issue komentovali, a to včetně počtu komentářů. Tato funkce nebude mít asynchronní API (tedy nebude `async def`, ale jen `def`).

*) [GitHub Search API] má limit na 1000 výsledků

Funkce `asya.logic.gather_acquaintances` (v projektu [MarekSuchanek/asya]):

* parametr `search_specs` = slovník obsahující specifikaci vyhledávání issues pro [GitHub Search API] (možné rovnou používat pro požadavky)
* parametr `supervisor` = objekt, na kterém vaše implementace volá příslušné metody v daných částech kódu (třídu `AsyaSupervisor` není možné měnit, ale lze "registrovat" vlastní funkce, které se budou volat, není to však vyžadováno - viz [dokumentace třídy](http://asya.readthedocs.io/en/latest/api.html#module-asya.supervisor); zda voláte metody správně, zjistíte například chováním CLI s progressbarem):
  * `supervisor.report_issues_search_page(page, number)` - volat před zpracováním dané stránky výsledků hledání issues, `page` = `dict` s tělem odpovědi, `number` = číslo stránky
  * `supervisor.report_issue(issue)` - volat po zpracování daného issue, `issue` = `dict` s daty issue
  * `supervisor.report_comment(comment)` - volat po zpracování daného komentáře, `comment` = `dict` s daty komentáře
  * `supervisor.report_skip(headers)` - volat v případě přeskočení chyby 404 (dle nastavení `skip_404` viz níže), `headers` = hlavičky odpovědi způsobující chybu
  * `supervisor.report_wait(active, headers)` - volat v případě zahájení/ukončení čekání (dle nastavení `wait_rate_limit` viz níže), `active` = flag zahájení (`True`) a ukočení (`False`), `headers` = hlavičky odpovědi způsobující čekání
* vrací slovník, kde klíčem je uživatelské jméno a hodnotou příslušný počet komentářů

```python
>>> gather_acquaintances({'q': 'author:MarekSuchanek'}, supervisor)
{'MarekSuchanek': 7, 'hroncok': 15, 'encukou': 10}
```

Další požadavky:

* Použijte `asyncio` a `aiohttp` pro asynchronní požadavky na [GitHub API].
* Pro stránkování použijte velikost stránky (parametr `per_page`) nastavenou na objektu `supervisor` (pomocí `supervisor.per_page`) a to jak pro výsledky issues, tak i komentáře.
* Použijte [personal access token] pro autorizaci požadavků ze `supervisor.token`, je-li nastavený. Token ovlivňuje výsledky a [API Rate Limit].
* [GitHub API] endpoint nepište "natvrdo", ale využijte `supervisor.api_endpoint`.
* Chybu způsobenou vyčerpáním [API Rate Limit] řešte podle nastavení příslušného flagu `wait_rate_limit` (pokud `True`, pak se čeká do vypršení limitu, jinak se vyhodí příslušná vyjímka `AsyaException`).
* Chyby způsobené nepřístupností issue/komentářů (404) přeskočte podle nastavení příslušného flagu `skip_404` (pokud `True`, pak se přeskakuje, jinak se vyhodí příslušná vyjímka `AsyaException`).
* V ostatních případech chyby v rámci komunikace se rovněž vyhodí vyjímka `AsyaException`.

Vytvořte nový privátní repozitář s obsahem z [MarekSuchanek/asya] (release `v0.0`), dejte nám cvičícím přístup a pro odevzdání vytvořte tag `v0.1`. Úpravy mimo modul `asya.logic` (soubor `asya/logic.py`) budou ignorovány, ale je vhodné se podívat na [dokumentaci] a zdrojový kód ostatních modulů.

Za bonusový bod implementujte také klasické synchronní řešení s knihovnou `requests` a porovnejte rychlost obou řešení s různými dotazy (a počty výsledků). Použijte stejný formát funkce `gather_acquaintances`, pracujte třeba v jiné větvi a řešení otagujte `v0.1-alt`.

[GitHub API]: https://developer.github.com/v3/
[GitHub Search API]: https://developer.github.com/v3/search/
[personal access token]: https://github.com/blog/1509-personal-api-tokens
[API Rate Limit]: https://developer.github.com/v3/rate_limit/
[MarekSuchanek/asya]: https://github.com/MarekSuchanek/asya
[dokumentaci]: http://asya.readthedocs.io/
