# Aplikacja do wyznaczania drogi dojazdu - HowToDrive.pl
## Cel projeku
Głównym celem projektu było stworzenie aplikacji webowej opartej o FastAPI, dzięki której użytkownik będzie mógł wyznaczyć trasę dojazdu do wybranego miejsca. 


## Jak uruchomić aplikację

1. Pobrać repozytorium:
```bash
git clone https://github.com/filiperni/future-team-name-ai-project
```
2. Wyłączyć Cors w przeglądarce żeby appka działała.
3. otworzyć folder z projektem w terminalu.
4. Stworzyć wirtualne środowisko:
```bash
python3 -m venv .venv
```
5. Aktywuj wirtualne środowisko:
```bash
source .venv/bin/activate
```
6. Zainstalować wymagane biblioteki:
```bash
pip install --upgrade pip
pip install -r requirements.txt
```
7. Uruchomić lokalny server uvicorn:
```bash
uvicorn main:app --reload --timeout-keep-alive 120
```
8. Uruchomić aplikację w przeglądarce:
```bash
otworzyć plik stronka.html w przeglądarce
```