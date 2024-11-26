# README

## Datenmodell

### Resource (Ressource): Configuration Item
Resource is any asset, tangible or intangible, that an organization owns, leases, or utilizes to perform specific functions within an IT environment. This includes hardware like servers, software applications, network devices, and even human resources. 

Ressource bezieht sich auf jedes Asset, ob materiell oder immateriell, das eine Organisation besitzt, mietet oder nutzt, um spezifische Funktionen innerhalb einer IT-Umgebung auszuführen. Dazu gehören Hardware wie Server, Softwareanwendungen, Netzwerkgeräte und sogar personelle Ressourcen. 


### Resource Capability (Ressourcenfähigkeit oder Fähigkeit)
Resource Capability refers to the specific actions, functions, or operations that a resource—such as an application, system, IT component, or database element—can perform within an IT environment. This term includes the internal definition of roles within the resource itself, allowing for the mapping of these capabilities to functional roles like “Specialist” in complex applications. While defining capabilities internally can reduce complexity in external IAM tools, it should generally be the exception rather than the rule. Ideally, role-based access management should be centralized in IAM systems to maintain consistency and ease of management across the organization. Internal role definitions should only be used when necessary to address specific application requirements or complexities.

Ressourcenfähigkeit bezeichnet die spezifischen Aktionen, Funktionen oder Operationen, die eine Ressource—wie eine Anwendung, ein System, eine IT-Komponente oder ein Datenbankelement—innerhalb einer IT-Umgebung ausführen kann. Dieser Begriff umfasst auch die interne Definition von Rollen innerhalb der Ressource selbst, wodurch diese Fähigkeiten auf funktionale Rollen wie “Spezialist” in komplexen Anwendungen abgebildet werden können. Während die interne Definition von Fähigkeiten die Komplexität in externen IAM-Tools reduzieren kann, sollte dies im Allgemeinen die Ausnahme und nicht die Regel sein. Idealerweise sollte das rollenbasierte Zugriffsmanagement in zentralen IAM-Systemen erfolgen, um Konsistenz und einfache Verwaltung in der gesamten Organisation zu gewährleisten. Interne Rollendefinitionen sollten nur dann verwendet werden, wenn dies zur Bewältigung spezifischer Anwendungsanforderungen oder -komplexitäten erforderlich ist.

### Group
A group, within an authorization repository like Active Directory, is a collection of user accounts that are managed as a single entity for the purpose of assigning permissions and access rights. Groups are used to simplify the management of permissions by allowing administrators to assign resource capabilities to multiple users simultaneously. Instead of assigning permissions to each user individually, administrators can map resource capabilities to a group, and all members of that group inherit the associated permissions. This approach enhances efficiency and consistency in managing access control within an organization.

In einem Autorisierungs-Repository wie Active Directory ist eine Gruppe eine Sammlung von Benutzerkonten, die als eine Einheit verwaltet werden, um Berechtigungen und Zugriffsrechte zuzuweisen. Gruppen werden verwendet, um die Verwaltung von Berechtigungen zu vereinfachen, indem Administratoren Ressourcenfähigkeiten mehreren Benutzern gleichzeitig zuweisen können. Anstatt Berechtigungen jedem Benutzer einzeln zuzuweisen, können Administratoren Ressourcenfähigkeiten einer Gruppe zuordnen, wodurch alle Mitglieder dieser Gruppe die zugehörigen Berechtigungen erben. Dieser Ansatz erhöht die Effizienz und Konsistenz bei der Verwaltung der Zugriffskontrolle innerhalb einer Organisation.


### Entitlement

### Resource Bundle


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
- **Fähigkeit** 1..1 zu 0..n **Einzelrecht**
- **Fähigkeit** 1..1 zu 0..n **Anwendungsrolle**

## Use Cases
1. **Anlegen, Anzeigen, Löschen, Ändern** von Attributen des jeweiligen Datenobjekts
2. **Pflege der Verbindungen** zwischen den Datenobjekten: Verlinken, Verlinkungen löschen
3. **Baumdarstellung** der Datenobjekte und deren Verbindung

## Datenmodell-Diagramm



```mermaid
classDiagram
    Einzelrecht "0..n" --> "0..n" Anwendungsrolle
    Einzelrecht "0..n" --> "0..n" ITBundle
    Anwendungsrolle "0..n" --> "0..n" ITBundle
    Fähigkeit "0..1" --> "1" Einzelrecht
    Fähigkeit "0..n" --> "0..n" Anwendungsrolle
```