import { config } from './config.js';

export class AuthAPI {
  constructor() {
    this.baseURL = config.API_URL;
  }

  async request(endpoint, body) {
    console.log(`Attempting to connect to: ${this.baseURL}${endpoint}`);
    
    const response = await fetch(`${this.baseURL}${endpoint}`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(body),
    });

    const data = await response.json();
    return { response, data };
  }

  async login(email, password) {
    return this.request("/login", { email, password });
  }

  async signup(name, email, password) {
    return this.request("/signup", { name, email, password });
  }
}