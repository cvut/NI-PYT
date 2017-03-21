Webové aplikace: Flask
======================

Výukové materiály:
[naucse.python.cz](http://naucse.python.cz/lessons/intro/flask/),
[GitHub](https://github.com/pyvec/naucse.python.cz/tree/master/lessons/intro/flask).

Úkol
----

Vaším úkolem za 5 bodů je rozšířit command line aplikaci z minulého
cvičení o webové rozhraní. Stávající funkcionalita ale musí být zachována,
k tomu můžete použít například podpříkazy pro click:

```python
@click.group()
def cli():
    pass

@cli.command()
def web():
    """Run the web app"""
    click.echo('Running the web app')

@cli.command()
def console():
    """Run the console app"""
    click.echo('Running the console app')
```

Výslednou aplikaci nasaďte na PythonAnywhere, nebo jiný veřejný hosting.
Odkaz na běžící aplikaci a repozitář nám pošlete e-mailem.
V repozitáři prosím nastavte tag `v0.2`.
Termín odevzdání je začátek příštího cvičení (dřívější paralelky).

### Twitter Wall

Konzole není pro Twitter Wall dostatečně vhodné médium,
doplňte do aplikace webový frontend, který bude zobrazovat
výsledky hledání. Hledaný pojem by měl jít zadat pomocí URL.

Pro plný počet bodů  musí rozhraní zobrazovat avatary uživatelů
a zpracovávat [entity] jako obrázky, odkazy, zmínky a hash tagy.
Ideální je k tomu využít filtr.

[entity]: https://dev.twitter.com/overview/api/entities-in-twitter-objects

### GitHub Issues Bot

Bylo by dobré, kdyby labelovací robot neprocházel issues v určitém intervalu,
ale dozvěděl se o nově založených issues.
Vyrobte webovou aplikaci, která bude na nějakém URL naslouchat událostem na
GitHubu a nově založenou issue olabeluje hned po založení.
K tomu použijte [webhook].

Pro načtení dat od GitHubu použijte globální objekt `request`:

```python
from flask import request

@app.route('/hook', methods=['POST'])
def hook():
    data = request.get_json()
    ...
    return ''
```

Ve výchozí routě `/` by měla být jednoduchá
HTML stránka, která bude informovat uživatele, jak lze aplikaci použít.

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

### Vlastní zadání

Pokud jste minule pracovali na jiném API, konzultujte s cvičícím, co máte dělat.
