#!/usr/bin/env python3
"""
Test script to debug Discord webhook issues
"""
import requests
import json
from datetime import datetime

# Your webhook URL
WEBHOOK_URL = "https://discord.com/api/webhooks/1482928937184133334/1PBReRlgBEOUxASnhbCPK8MHeOGx8lmIMiLXnUtY9rvq6SI7MVyJYMB7uHmu_oGC3B2n"

def test_minimal_payload():
    """Test with minimal Discord payload"""
    payload = {
        "content": "🧪 DOCSight Test - Minimal Payload"
    }
    
    try:
        response = requests.post(WEBHOOK_URL, json=payload, timeout=10)
        print(f"Minimal payload - Status: {response.status_code}")
        print(f"Response: {response.text}")
        return response.status_code == 204
    except Exception as e:
        print(f"Minimal payload failed: {e}")
        return False

def test_embed_payload():
    """Test with Discord embed"""
    payload = {
        "content": "",
        "embeds": [
            {
                "title": "DOCSight Test Alert",
                "description": "This is a test message from DOCSight",
                "color": 0x3498db,
                "timestamp": datetime.utcnow().isoformat(),
                "footer": {"text": "DOCSight Cable Monitor"}
            }
        ],
        "username": "DOCSight"
    }
    
    try:
        response = requests.post(WEBHOOK_URL, json=payload, timeout=10)
        print(f"Embed payload - Status: {response.status_code}")
        print(f"Response: {response.text}")
        return response.status_code == 204
    except Exception as e:
        print(f"Embed payload failed: {e}")
        return False

def test_original_payload():
    """Test with original DOCSight payload"""
    payload = {
        "source": "docsight",
        "timestamp": datetime.utcnow().isoformat(),
        "severity": "info",
        "event_type": "test",
        "message": "DOCSight test notification",
        "details": {"test": True},
    }
    
    try:
        response = requests.post(WEBHOOK_URL, json=payload, timeout=10)
        print(f"Original payload - Status: {response.status_code}")
        print(f"Response: {response.text}")
        return response.status_code == 204
    except Exception as e:
        print(f"Original payload failed: {e}")
        return False

if __name__ == "__main__":
    print("Testing Discord webhook...")
    print("=" * 50)
    
    print("\n1. Testing minimal payload...")
    test_minimal_payload()
    
    print("\n2. Testing embed payload...")
    test_embed_payload()
    
    print("\n3. Testing original payload...")
    test_original_payload()
    
    print("\n" + "=" * 50)
    print("Test complete!")
