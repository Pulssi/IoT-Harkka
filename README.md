# Ääniohjauksella toimiva valojen ohjaus

Harjoitustyön tavoitteena on ohjata led-valoja puheen avulla. Harjoitustyön kontrollerina toimii Raspberry Pi ja led-valojen kytkentä tehdään koulussa oleville kytkentäalustoille. Tämän lisäksi tavoitteena on visualisoida valojen tilaa IBM Watson IoT Platform -palvelun avulla.

## Toteutus

Projektin puheentunnistus on toteutettu pythonin speechRecognition -kirjastolla, joka käyttää googlen SpeechToText API:a puheen muuttamisessa tekstiksi. Tätä käytetään äänikomentojen tunnistukseen, joilla Raspberry Pi:n I/O pinnejä ohjataan.

Pinnien tila lähetetään MQTT-protokollalla Node-RED palveluun, jossa data muutetaan JSON muotoiseksi ja lähetetään IBM Watson IoT Platform -palveluuun visualisointia  varten.

Node-Red -palvelulla on myös pinnien ohjaamiseen toteutettu sähköpostilla toimiva ohajus. Palvelussa oleva node tarkistaa tietyn aikavälein onko määrättyyn sähköposti tiliin tullut uutta viestiä ja mikäli on niin lukee viestin sisällön ja muuttaa pinnin tilaa vastaavasti.

Projektista löytyy kuvakaappauksia images -kansiosta sekä toiminnallisuutta havainnollistava video videos -kansiosta.
