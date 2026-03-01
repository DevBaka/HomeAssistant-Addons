# 🚨 EMERGENCY FIX - Home Assistant Not Starting

## IMMEDIATE ACTIONS REQUIRED

### 1. Disable DOCSight Addon
If Home Assistant is not starting, the DOCSight addon is likely causing the issue:

**Option A: Via Supervisor (if accessible)**
1. Open Home Assistant Supervisor
2. Go to "Add-on Store"
3. Find DOCSight addon
4. Click "Disable" or "Uninstall"

**Option B: Via Configuration Files**
1. Access Home Assistant configuration directory
2. Remove DOCSight addon files:
   ```bash
   rm -rf /config/addons/docsight
   ```

**Option C: Via SSH/Terminal**
```bash
# Stop all addons
ha addons stop

# Remove problematic addon
ha addons uninstall docsight

# Restart Home Assistant
ha core restart
```

### 2. Safe Configuration Changes
The addon has been updated with safe settings:

- ✅ **Boot**: `manual` (not auto-start)
- ✅ **Startup**: `application` (not service)
- ✅ **Host Network**: `false` (isolated)
- ✅ **Architecture**: `amd64` only (reduced complexity)

### 3. Recovery Steps

1. **Remove the addon completely** first
2. **Restart Home Assistant** to confirm it works
3. **Reinstall addon** with safe config
4. **Test manually** before enabling auto-start

### 4. Alternative: Use Docker Direct

If addon continues to cause issues, run DOCSight directly:

```bash
docker run -d \
  --name docsight \
  -p 8765:8765 \
  -v docsight_data:/data \
  ghcr.io/itsdnns/docsight:latest
```

## ⚠️ What Caused This

- **Host Network**: Can conflict with Home Assistant networking
- **Auto Boot**: Starts before HA is fully ready
- **Service Startup**: Can block HA startup process
- **Multi-arch**: Complex build process

## 📞 If Problems Persist

1. **Check HA Logs**: `/config/home-assistant.log`
2. **Check Supervisor Logs**: `/config/supervisor/logs`
3. **Report Issue**: GitHub with full error logs

## 🔄 Next Steps After Recovery

Once HA is working again:
1. Test addon manually
2. Gradually enable features
3. Monitor system stability
4. Keep backup configurations

**Priority: Get Home Assistant running first!**
