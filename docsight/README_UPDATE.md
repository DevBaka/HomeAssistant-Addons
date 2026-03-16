# 🚀 DOCSight Update & Panel Integration

## ✨ Neue Features

### 1. 🖥️ Home Assistant Panel Integration
DOCSight erscheint jetzt direkt in deiner Home Assistant Sidebar!

**Aktivierung:**
1. Im Addon-Konfigurationsmenü `ha_panel: true` setzen
2. Addon neustarten
3. Home Assistant neustarten
4. DOCSight-Icon in der Sidebar erscheint

### 2. 🔄 Automatische Updates
Das Addon kann jetzt automatisch nach Updates suchen!

**Optionen:**
- `check_updates: true` - Automatisch bei jedem Start nach Updates suchen
- `auto_update: false` - Updates nur manuell installieren (sicherer)

### 3. 🎯 Manuelles Update
Du kannst Updates jederzeit manuell auslösen!

**Update-Methoden:**
1. **Über Addon-Konfiguration:** `check_updates: true` und neustarten
2. **Manuell im Container:** `/app/manual_update.sh` ausführen
3. **Über Terminal:** `docker exec <container> /app/manual_update.sh`

## 📋 Konfiguration

```json
{
  "log_level": "info",
  "auto_update": false,
  "check_updates": true,
  "ha_panel": true
}
```

### Erklärungen:
- **log_level:** Debug-Level (debug/info/warning/error)
- **auto_update:** Updates automatisch installieren (empfohlen: false)
- **check_updates:** Bei jedem Start nach Updates suchen (empfohlen: true)
- **ha_panel:** DOCSight in HA Sidebar integrieren (empfohlen: true)

## 🔧 Wie es funktioniert

### Update-Prozess:
1. **Prüfung:** Vergleicht lokale Version mit GitHub-Release
2. **Download:** Lädt neueste Version von itsDNNS/docsight
3. **Backup:** Sichert HA-Addon-Konfiguration
4. **Update:** Ersetzt App-Dateien, behält Konfiguration
5. **Fertig:** Neustart erforderlich

### Panel-Installation:
1. **Konfiguration:** Fügt `panel_iframe` zu `configuration.yaml` hinzu
2. **Backup:** Erstellt Backup der existierenden Konfiguration
3. **Integration:** DOCSight erscheint als Sidebar-Panel

## 🚨 Wichtige Hinweise

### Sicherheit:
- **Auto-Update** ist standardmäßig deaktiviert
- **Backups** werden automatisch erstellt
- **Konfiguration** wird immer erhalten

### Kompatibilität:
- Funktioniert mit allen HA-Versionen
- Keine Abhängigkeiten von anderen Addons
- Netzwerk-isoliert (sicher)

### Fehlersuche:
- **Logs zeigen** Update-Status
- **Backups** im Config-Verzeichnis
- **Manueller Trigger** immer möglich

## 🎉 Ergebnis

Nach der Konfiguration hast du:
- ✅ **DOCSight Panel** direkt in Home Assistant
- ✅ **Automatische Update-Prüfung** bei jedem Start
- ✅ **Manuelle Updates** mit einem Klick
- ✅ **Sichere Backups** aller Konfigurationen

**Zugriff:** Sidebar → Network-Icon → DOCSight 🌐
