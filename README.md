# README

## Datenmodell

### Fähigkeit
- **Name**
- **Beschreibung**

### Anwendung
- **Name**
- **LeanixId**

### Einzelrecht
- **Name**
- **Beschreibung**
- **Privilegiert** (ja/nein)
- **SoDArea**
- **Bestellbar** (ja/nein)

### ITBundle
- **Name**
- **Beschreibung**
- **Privilegiert** (ja/nein)
- **SoDArea**
- **Bestellbar** (ja/nein)

## Datenmodell-Beziehungen
- **Anwendung** 1..1 zu 0..n **Einzelrecht**
- **Anwendung** 1..1 zu 0..n **Anwendungsrolle**
- **Anwendung** 1..1 zu 0..n **ITBundle**
- **Einzelrecht** 0..n zu 0..n **Anwendungsrolle**
- **Einzelrecht** 0..n zu 0..n **ITBundle**
- **Anwendungsrolle** 0..n zu 0..n **ITBundle**

## Use Cases
1. **Anlegen, Anzeigen, Löschen, Ändern** von Attributen des jeweiligen Datenobjekts
2. **Pflege der Verbindungen** zwischen den Datenobjekten: Verlinken, Verlinkungen löschen
3. **Baumdarstellung** der Datenobjekte und deren Verbindung

## Datenmodell-Diagramm

```mermaid
classDiagram
    Faehigkeit {
        +String Name
        +String Beschreibung
    }

    Anwendung {
        +String Name
        +String LeanixId
    }

    Einzelrecht {
        +String Name
        +String Beschreibung
        +Boolean privilegiert
        +String SoDArea
        +Boolean bestellbar
    }

    ITBundle {
        +String Name
        +String Beschreibung
        +Boolean privilegiert
        +String SoDArea
        +Boolean bestellbar
    }

    Anwendungsrolle {
        +String Name
        +String Beschreibung
    }

    Anwendung "1" --> "0..n" Einzelrecht
    Anwendung "1" --> "0..n" Anwendungsrolle
    Anwendung "1" --> "0..n" ITBundle
    Einzelrecht "0..n" --> "0..n" Anwendungsrolle
    Einzelrecht "0..n" --> "0..n" ITBundle
    Anwendungsrolle "0..n" --> "0..n" ITBundle