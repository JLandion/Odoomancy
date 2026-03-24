// src/axiosConfig.js
import axios from "axios";

const isLocalhost = globalThis.location.hostname === "localhost";

let dns = '';

if (isLocalhost) {
  dns = 'http://localhost:8069';
} else if (!isLocalhost && (globalThis.location.port === '8069' || globalThis.location.port === '3000')) //pda
  dns = 'http://' + globalThis.location.hostname + ':8069';
else
  dns = 'https://' + globalThis.location.hostname; //in production (without fixed port)

const apiClient = axios.create({
  baseURL: `${dns}/web/character-sheet/api`,
  headers: {
    "Content-Type": "application/json",
  },
});

export default apiClient;