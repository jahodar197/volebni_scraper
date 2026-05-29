# Projekt 3 – Volební scraper

**Autor:** Roman Jahoda  
**Email:** jahodar197@gmail.com

## Popis projektu

Tento project je scraper výsledků voleb z roku 2017, který bere data z webu volby.cz pro daný okres.

## Použité knihovny

* requests
* beautifulsoup4
* lxml

## Instalace

Knihovny nejdřív nainstaluj pomocí příkazu:

pip install -r requirements.txt

## Spuštění programu

Program se spouští příkazem ve scriptu:

scrape\_election\_data("Odkaz", "Výstupní soubor")

## Jak funguje?

1. Odkaz -> https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ\&xkraj=2\&xnumnuts=2101
2. Název výstupního souboru -> benesov\_volby17.csv

v příkazu: scrape\_election\_data("https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ\&xkraj=2\&xnumnuts=2101", "benesov\_volby17.csv")

## Běh

Načítám seznam obcí…
Načítám stránku: https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ\&xkraj=2\&xnumnuts=2101
Nalezeno obcí: 114
Začínám stahovat data z jednotlivých obcí…
Zpracovávám obec: Benešov (529303)
Načítám stránku: https://volby.cz/pls/ps2017nss/ps311?xjazyk=CZ\&xkraj=2\&xobec=529303\&xvyber=2101
Zpracovávám obec: Bernartice (532568)
Načítám stránku: https://volby.cz/pls/ps2017nss/ps311?xjazyk=CZ\&xkraj=2\&xobec=532568\&xvyber=2101 …

Hotovo! Výsledky jsou uložené v souboru benesov\_volby17.csv






