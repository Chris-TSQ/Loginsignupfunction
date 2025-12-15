export const config = {
  API_URL: import.meta.env?.VITE_API_URL || 
           window.ENV?.REACT_APP_API_URL || 
           "http://localhost:8000",
  
  log() {
    console.log("API URL configured as:", this.API_URL);
  }
};