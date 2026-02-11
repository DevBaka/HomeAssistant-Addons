# DevBaka Home Assistant Addons

[![Build Status](https://github.com/DevBaka/HomeAssistant-Addons/workflows/Build%20Home%20Assistant%20Addons/badge.svg)](https://github.com/DevBaka/HomeAssistant-Addons/actions)
[![License](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

## 📦 Available Addons

### 🌐 DOCSight
Monitor your cable internet connection 24/7 and collect evidence for ISP complaints.

**Features:**
- 24/7 cable internet monitoring
- Automatic evidence collection for ISP complaints
- Web-based dashboard
- Router integration (FritzBox, etc.)
- Local-only operation (no cloud)

**Installation:**
1. Add this repository to Home Assistant Supervisor: `https://github.com/DevBaka/HomeAssistant-Addons`
2. Install the DOCSight addon
3. Configure and start
4. Access at `http://your-ha-ip:8765`

### 🎵 Icecast Server
Icecast2 streaming server for Home Assistant.

## 🔄 Automatic Updates

This repository automatically tracks upstream updates:

- **DOCSight**: Daily checks for new releases from [itsDNNS/docsight](https://github.com/itsDNNS/docsight)
- **Automatic builds**: New versions are built and published automatically
- **Version tracking**: Maintains compatibility with Home Assistant

## 🚀 Development

### Manual Update
To manually update DOCSight to the latest version:

```bash
./update-docsight.sh
```

### Local Development
```bash
# Build specific addon
docker build -t docsight-dev ./docsight

# Run locally
docker run -p 8765:8765 -v $(pwd)/data:/data docsight-dev
```

## 📋 Architecture Support

All addons support:
- `amd64` (x86_64)
- `aarch64` (ARM64)
- `armv7` (ARM 32-bit)

## 🤝 Contributing

1. Fork this repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📄 License

This repository is licensed under the MIT License. See [LICENSE](LICENSE) for details.

## 🔗 Links

- [Home Assistant](https://www.home-assistant.io/)
- [Home Assistant Addons Documentation](https://developers.home-assistant.io/docs/add-ons/)
- [DOCSight Upstream](https://github.com/itsDNNS/docsight)
