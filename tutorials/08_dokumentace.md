Dokumentace
===========

Výukové materiály:
[naucse.python.cz](http://naucse.python.cz/2017/mipyt-zima/intro/docs/),
[GitHub](https://github.com/pyvec/naucse.python.cz/tree/master/lessons/intro/docs).

Úkol
----

Vaším úkolem za 5 bodů je vytvořit pomocí Sphinx dokumentaci k vašemu projektu.

Měla by obsahovat textovou část, ze které bude jasné, co je, k čemu je,
jak se nainstaluje a jak se používá vaše aplikace.
Můžete předpokládat, že uživatel ví, co je to GitHub, issue, pull request,
label, repozitář apod.
Nepředpokládejte ale, že ví, kde najde API token či webhook, že ví, co to je,
jak se k nim chovat apod.

Pokud hypoteticky ukážeme dokumentaci kolegům, kteří nikdy neviděli zadání
vašeho úkolu, musí to pro ně být stejně pochopitelné.

Dále by dokumentace měla obsahovat textovou část s ukázkami kódu, které se
testují pomocí doctestu. Tato část může vysvětlovat, jak váš kód použít pro
výrobu jiné aplikace, nebo může popisovat, jak aplikace uvnitř funguje.

V dokumentaci by měla existovat kapitola s kompletní API dokumentací vašich
modulů, tříd, funkcí apod. Všechny tyto věci musí mít v kódu dokumentační
řetězce, které v dokumentaci musí být zobrazeny (t.j. změna dokumentačního
řetězce se automaticky promítne ve vygenerované dokumentaci).

Jak sestavit a testovat dokumentaci by mělo být jasné z `README.rst`
(a to musí mít reStructuredText syntaxi).

Generování dokumentace ani doctesty nesmí způsobit chybu ani varování.
Potlačení chybových a varovných hlášek (např. konfigurací, přesměrováním
*stderr*, apod.) je povoleno jen po konzultaci s cvičícím.

Na Travis CI spouštějte dokumentační testy.

Dokumentace musí být v angličtině.

Dosavadní funkcionalita aplikace musí být samozřejmě zachována.

Úkol odevzdáváte tradičně s tagem v0.5 a nahráním nové verze na
(testovací či pravou) PyPI.
(Nahrání je nutné – čtenář dokumentace k verzi 0.5 se bude dívat po balíčku
této verze.)

Za fungující publikaci smysluplné dokumentace na [Read the Docs] je bod navíc.
