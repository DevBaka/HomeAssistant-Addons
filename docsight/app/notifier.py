"""Notification dispatcher — routes events to external channels (webhook, etc.)."""

import json
import logging
import time
from abc import ABC, abstractmethod

import requests

from .tz import utc_now

log = logging.getLogger("docsis.notifier")

SEVERITY_ORDER = {"info": 0, "warning": 1, "critical": 2}


class NotificationChannel(ABC):
    """Base class for notification channels."""

    @abstractmethod
    def send(self, payload: dict) -> bool:
        """Send a notification payload. Returns True on success."""


class WebhookChannel(NotificationChannel):
    """HTTP POST webhook — works with ntfy, Discord, Gotify, custom endpoints."""

    def __init__(self, url, headers=None):
        self._url = url
        self._headers = {"Content-Type": "application/json"}
        if headers:
            self._headers.update(headers)
        # Detect Discord webhook
        self._is_discord = "discord.com" in url

    def send(self, payload: dict) -> bool:
        try:
            # Format payload for Discord if needed
            if self._is_discord:
                discord_payload = self._format_discord_payload(payload)
                r = requests.post(
                    self._url,
                    json=discord_payload,
                    headers=self._headers,
                    timeout=10,
                )
            else:
                r = requests.post(
                    self._url,
                    json=payload,
                    headers=self._headers,
                    timeout=10,
                )
            r.raise_for_status()
            return True
        except Exception as e:
            log.warning("Webhook POST failed (%s): %s", self._url, e)
            return False

    def _format_discord_payload(self, payload: dict) -> dict:
        """Format payload for Discord webhook format."""
        severity = payload.get("severity", "info")
        message = payload.get("message", "")
        details = payload.get("details", {})
        event_type = payload.get("event_type", "unknown")
        
        # Discord color codes for severity
        colors = {
            "info": 0x3498db,      # Blue
            "warning": 0xf39c12,   # Orange
            "critical": 0xe74c3c   # Red
        }
        color = colors.get(severity, 0x3498db)
        
        # Create embed
        embed = {
            "title": f"DOCSight Alert: {event_type.replace('_', ' ').title()}",
            "description": message,
            "color": color,
            "timestamp": payload.get("timestamp"),
            "footer": {"text": "DOCSight Cable Monitor"},
            "fields": []
        }
        
        # Add details as fields
        if details:
            for key, value in details.items():
                if key != "raw_data":  # Skip raw data to avoid huge messages
                    embed["fields"].append({
                        "name": key.replace("_", " ").title(),
                        "value": str(value),
                        "inline": True
                    })
        
        # Add severity field
        embed["fields"].append({
            "name": "Severity",
            "value": severity.upper(),
            "inline": True
        })
        
        return {
            "content": "",
            "embeds": [embed],
            "username": "DOCSight",
            "avatar_url": "https://github.com/itsDNNS/docsight/raw/main/app/static/img/icon.png"
        }


class NotificationDispatcher:
    """Routes events through severity filter and cooldown to notification channels."""

    def __init__(self, config_mgr):
        self._config_mgr = config_mgr
        self._channels = []
        self._cooldown_tracker = {}  # event_type -> last_sent_timestamp
        try:
            self._default_cooldown = int(config_mgr.get("notify_cooldown", 3600))
        except (ValueError, TypeError):
            self._default_cooldown = 3600
        try:
            self._cooldown_overrides = json.loads(
                config_mgr.get("notify_cooldowns", "{}")
            )
        except (json.JSONDecodeError, TypeError):
            self._cooldown_overrides = {}
        self._min_severity = config_mgr.get("notify_min_severity", "warning")
        self._setup_channels()

    def _setup_channels(self):
        url = self._config_mgr.get("notify_webhook_url")
        if url:
            headers = {}
            token = self._config_mgr.get("notify_webhook_token")
            if token:
                headers["Authorization"] = f"Bearer {token}"
            self._channels.append(WebhookChannel(url, headers))
            log.info("Notification channel: webhook -> %s", url)

    def dispatch(self, events: list):
        """Send qualifying events to all configured channels."""
        if not self._channels:
            return
        for event in events:
            if not self._should_send(event):
                continue
            payload = self._build_payload(event)
            for channel in self._channels:
                try:
                    channel.send(payload)
                except Exception as e:
                    log.warning(
                        "Notification failed (%s): %s",
                        type(channel).__name__, e,
                    )

    def _should_send(self, event) -> bool:
        # Severity filter
        min_level = SEVERITY_ORDER.get(self._min_severity, 1)
        event_level = SEVERITY_ORDER.get(event.get("severity", "info"), 0)
        if event_level < min_level:
            return False

        # Cooldown per event_type
        now = time.time()
        key = event.get("event_type", "unknown")
        cooldown = self._cooldown_overrides.get(key, self._default_cooldown)
        if isinstance(cooldown, str):
            try:
                cooldown = int(cooldown)
            except ValueError:
                cooldown = self._default_cooldown
        if cooldown == 0:  # 0 = disabled, never send this type
            return False
        if key in self._cooldown_tracker:
            if (now - self._cooldown_tracker[key]) < cooldown:
                return False
        self._cooldown_tracker[key] = now
        return True

    @staticmethod
    def _build_payload(event):
        return {
            "source": "docsight",
            "timestamp": event.get("timestamp", utc_now()),
            "severity": event.get("severity", "info"),
            "event_type": event.get("event_type", "unknown"),
            "message": event.get("message", ""),
            "details": event.get("details", {}),
        }

    def test(self) -> dict:
        """Send a test notification to all channels. Returns {success, error}."""
        if not self._channels:
            return {"success": False, "error": "No notification channels configured"}
        payload = {
            "source": "docsight",
            "timestamp": utc_now(),
            "severity": "info",
            "event_type": "test",
            "message": "🧪 DOCSight test notification - webhook is working!",
            "details": {
                "test": True,
                "status": "Webhook configuration successful",
                "timestamp": utc_now()
            },
        }
        errors = []
        for channel in self._channels:
            try:
                if not channel.send(payload):
                    errors.append(f"{type(channel).__name__}: send returned false")
            except Exception as e:
                errors.append(f"{type(channel).__name__}: {e}")
        if errors:
            return {"success": False, "error": "; ".join(errors)}
        return {"success": True}
