import { AuthController } from './auth.js';

const authController = new AuthController();

// Expose to window for HTML onclick handlers
window.toggleMode = () => authController.toggleMode();
window.handleSubmit = (e) => authController.handleSubmit(e);
window.handleLogout = () => authController.handleLogout();