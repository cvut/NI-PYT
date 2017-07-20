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

Vaším úkolem za 5 bodů je vytvořit command line aplikaci nad vybraným webovým
API, pomocí knihoven [requests] a [click].
Hotovou aplikaci odevzdáte jako gitový repozitář na GitHubu, případně fakultním
GitLabu. V obou případech nám nezapomeňte [dát přístup](00_uvod.md).

Nebráníme se veřejným repozitářům, ale neradi bychom viděli, že jednu úlohu
odevzdá úplně stejně několik různých lidí, pokud chcete, udělejte repozitář
privátní.

Odkaz na repozitář nám pošlete e-mailem.
V repozitáři prosím nastavte tag `v0.1`.
Termín odevzdání je začátek příštího cvičení (dřívější paralelky).

Co by aplikace měla dělat? Můžete si vybrat:

### Twitter Wall

Twitter Wall pro terminál. Aplikace, která bude zobrazovat tweety odpovídající
určitému hledání do terminálu v nekonečné smyčce.

Aplikace načte určitý počet tweetů odpovídající hledanému výrazu, zobrazí je
a v nějakém intervalu se bude dotazovat na nové tweety (použijte API argument
`since_id`).

Pomocí argumentů půjde nastavit:

 * cesta ke konfiguračnímu souboru s přístupovými údaji
 * hledaný výraz
 * počet na začátku načtených tweetů
 * časový interval dalších dotazů
 * nějaké vlastnosti ovlivňující chování (např. zda zobrazovat retweety)

### GitHub Issues Bot

Robot (založte mu vlastní účet na GitHubu), který v intervalech projde issues
v repozitáři na GitHubu a ty neolabelované olabeluje podle zadaných pravidel.
Nezapomeňte robotovi dát přístup do vašeho testovacího repozitáře.

Pravidla by měla být nějakým způsobem konfigurovatelná
(např. páry regulární výraz → label).

Pomocí argumentů půjde nastavit:

 * cesta ke konfiguračnímu souboru s přístupovými údaji
 * který repozitář se má procházet
 * kde je soubor s definovanými pravidly
 * jak často issues kontrolovat
 * jaký label nastavit, pokud žádné pravidlo nezabralo
 * nějaké vlastnosti ovlivňující chování (např. zda má robot vyhodnocovat i komentáře, či procházet i Pull Requesty)

### Vlastní nápad

Můžete využít i jiné API (např. místní [Sirius] či [KOSapi]) a vymyslet vlastní aplikaci.
Zadání vám ale musí schválit cvičící **už na cvičení**, protože v dalších cvičeních na tuto
aplikaci budeme nabalovat další a další funkce.

[Sirius]: https://github.com/cvut/sirius/wiki
[KOSapi]: https://kosapi.fit.cvut.cz/projects/kosapi/wiki
