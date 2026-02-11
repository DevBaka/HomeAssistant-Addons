class DOCSightCard extends HTMLElement {
  constructor() {
    super();
    this.attachShadow({ mode: 'open' });
  }

  setConfig(config) {
    if (!config.entity) {
      throw new Error('You need to define an entity');
    }
    this.config = config;
  }

  getCardSize() {
    return 3;
  }

  render() {
    const { entity, title } = this.config;
    
    return `
      <style>
        ha-card {
          padding: 16px;
          background: var(--card-background-color, #fff);
          border-radius: var(--ha-card-border-radius, 12px);
          box-shadow: var(--ha-card-box-shadow, 0 2px 4px rgba(0,0,0,0.1));
        }
        
        .header {
          display: flex;
          align-items: center;
          margin-bottom: 16px;
          font-size: 1.2em;
          font-weight: 500;
          color: var(--primary-text-color);
        }
        
        .status {
          display: flex;
          align-items: center;
          margin-bottom: 12px;
        }
        
        .status-indicator {
          width: 12px;
          height: 12px;
          border-radius: 50%;
          margin-right: 8px;
        }
        
        .status-online {
          background-color: var(--success-color);
        }
        
        .status-error {
          background-color: var(--error-color);
        }
        
        .actions {
          display: flex;
          gap: 8px;
          margin-top: 16px;
        }
        
        ha-button {
          flex: 1;
        }
        
        .metrics {
          display: grid;
          grid-template-columns: 1fr 1fr;
          gap: 12px;
          margin-top: 16px;
        }
        
        .metric {
          text-align: center;
          padding: 8px;
          background: var(--secondary-background-color);
          border-radius: 8px;
        }
        
        .metric-value {
          font-size: 1.1em;
          font-weight: 500;
          color: var(--primary-text-color);
        }
        
        .metric-label {
          font-size: 0.8em;
          color: var(--secondary-text-color);
        }
      </style>
      
      <ha-card>
        <div class="header">
          <ha-icon icon="mdi:network-outline"></ha-icon>
          <span style="margin-left: 8px;">${title || 'DOCSight'}</span>
        </div>
        
        <div class="status">
          <div class="status-indicator" id="status-indicator"></div>
          <span id="status-text">Loading...</span>
        </div>
        
        <div class="metrics">
          <div class="metric">
            <div class="metric-value" id="uptime">-</div>
            <div class="metric-label">Uptime</div>
          </div>
          <div class="metric">
            <div class="metric-value" id="last-check">-</div>
            <div class="metric-label">Last Check</div>
          </div>
        </div>
        
        <div class="actions">
          <ha-button @click="${() => this.openDOCSight()}">
            <ha-icon icon="mdi:open-in-new"></ha-icon>
            Open DOCSight
          </ha-button>
          <ha-button @click="${() => this.refreshData()}">
            <ha-icon icon="mdi:refresh"></ha-icon>
            Refresh
          </ha-button>
        </div>
      </ha-card>
    `;
  }

  connectedCallback() {
    this.render();
    this.shadowRoot.innerHTML = this.render();
    this.updateData();
    
    // Update every 30 seconds
    this.interval = setInterval(() => this.updateData(), 30000);
  }

  disconnectedCallback() {
    if (this.interval) {
      clearInterval(this.interval);
    }
  }

  updateData() {
    const hass = this.hass;
    if (!hass) return;

    const statusEntity = this.config.entity;
    const uptimeEntity = this.config.entity.replace('status', 'uptime');
    const lastCheckEntity = this.config.entity.replace('status', 'last_check');

    // Update status
    const statusState = hass.states[statusEntity];
    if (statusState) {
      const statusElement = this.shadowRoot.getElementById('status-text');
      const indicatorElement = this.shadowRoot.getElementById('status-indicator');
      
      statusElement.textContent = statusState.state;
      indicatorElement.className = `status-indicator ${
        statusState.state === 'Online' ? 'status-online' : 'status-error'
      }`;
    }

    // Update uptime
    const uptimeState = hass.states[uptimeEntity];
    if (uptimeState) {
      this.shadowRoot.getElementById('uptime').textContent = uptimeState.state;
    }

    // Update last check
    const lastCheckState = hass.states[lastCheckEntity];
    if (lastCheckState) {
      const date = new Date(lastCheckState.state);
      this.shadowRoot.getElementById('last-check').textContent = 
        date.toLocaleTimeString();
    }
  }

  openDOCSight() {
    const hass = this.hass;
    if (!hass) return;

    // Open DOCSight panel
    hass.navigate('/panel/docsight');
  }

  refreshData() {
    const hass = this.hass;
    if (!hass) return;

    // Call refresh service
    hass.callService('docsight', 'refresh_data');
  }
}

customElements.define('docsight-card', DOCSightCard);

// Card configuration
window.customCards = window.customCards || [];
window.customCards.push({
  type: 'docsight-card',
  name: 'DOCSight Card',
  description: 'A card for displaying DOCSight internet monitoring status',
  preview: true,
});
