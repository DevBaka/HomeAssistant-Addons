# DOCSight Home Assistant Integration

## 🚀 Installation

### 1. Install the Addon
1. Add this repository to Home Assistant Supervisor: `https://github.com/DevBaka/HomeAssistant-Addons`
2. Install the DOCSight addon
3. Enable "Home Assistant Integration" in the addon configuration
4. Start the addon

### 2. Configure the Integration
1. Restart Home Assistant after addon installation
2. Go to **Settings** > **Devices & Services**
3. Click **+ Add Integration**
4. Search for "DOCSight" and select it
5. Enter your DOCSight host (usually `homeassistant.local`) and port (8765)
6. Click **Submit**

## 📱 Using the Integration

### Panel Access
After installation, you'll find a new "DOCSight" panel in your Home Assistant sidebar:
- Click the network icon in the sidebar
- The DOCSight web interface opens directly inside Home Assistant
- No need to open a separate browser tab!

### Dashboard Card
Add the DOCSight card to your Lovelace dashboard:

```yaml
type: custom:docsight-card
entity: sensor.docsight_status
title: Internet Monitor
```

### Available Sensors
- **sensor.docsight_status**: Current monitoring status (Online/Error)
- **sensor.docsight_uptime**: System uptime
- **sensor.docsight_last_check**: Last successful check time

### Services
Use these services in automations:

```yaml
# Refresh monitoring data
service: docsight.refresh_data

# Generate ISP report
service: docsight.generate_report
data:
  timeframe: "7d"
```

## 🔧 Automation Examples

### Alert on Internet Issues
```yaml
alias: Internet Issues Alert
trigger:
  - platform: state
    entity_id: sensor.docsight_status
    to: "Error"
action:
  - service: notify.mobile_app
    data:
      message: "DOCSight detected internet connection issues!"
```

### Weekly Report Generation
```yaml
alias: Weekly Internet Report
trigger:
  - platform: time
    at: "09:00:00"
condition:
  - condition: time
    weekday:
      - mon
action:
  - service: docsight.generate_report
    data:
      timeframe: "7d"
```

## 🎨 Customization

### Card Configuration
```yaml
type: custom:docsight-card
entity: sensor.docsight_status
title: "Internet Monitor"
show_metrics: true
show_actions: true
```

### Panel Customization
The DOCSight panel can be customized in your `configuration.yaml`:

```yaml
frontend:
  themes: !include_dir_merge_named themes
  extra_module_url:
    - /local/docsight/lovelace_card.js
```

## 🐛 Troubleshooting

### Integration Not Showing
1. Make sure the addon is running
2. Check that "Home Assistant Integration" is enabled in addon settings
3. Restart Home Assistant completely

### Panel Not Working
1. Verify the integration is configured correctly
2. Check that DOCSight is accessible at the configured host/port
3. Look at the addon logs for connection errors

### Sensors Unavailable
1. Check the integration status in Settings > Devices & Services
2. Verify network connectivity between Home Assistant and DOCSight
3. Check the addon logs for API errors

## 📚 Advanced Usage

### Multiple DOCSight Instances
You can run multiple DOCSight instances by:
1. Installing multiple addon instances with different ports
2. Adding each instance as a separate integration
3. Using different entity names for each

### Custom API Endpoints
The integration exposes additional API endpoints:
- `/api/status`: Current monitoring status
- `/api/refresh`: Force data refresh
- `/api/report`: Generate reports

## 🔗 Links

- [DOCSight Documentation](https://github.com/itsDNNS/docsight)
- [Home Assistant Integrations](https://www.home-assistant.io/integrations/)
- [Support Issues](https://github.com/DevBaka/HomeAssistant-Addons/issues)
