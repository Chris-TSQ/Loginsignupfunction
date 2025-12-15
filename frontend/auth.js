import { AppState } from './state.js';
import { AuthAPI } from './api.js';
import { UIController } from './ui.js';
import { config } from './config.js';

export class AuthController {
  constructor() {
    this.state = new AppState();
    this.api = new AuthAPI();
    this.ui = new UIController();
    this.init();
  }

  init() {
    config.log();
    this.attachEventListeners();
  }

  attachEventListeners() {
    const { emailInput, passwordInput, nameInput } = this.ui.elements;

    emailInput.addEventListener("change", (e) => 
      this.state.updateFormData("email", e.target.value)
    );
    passwordInput.addEventListener("change", (e) => 
      this.state.updateFormData("password", e.target.value)
    );
    nameInput.addEventListener("change", (e) => 
      this.state.updateFormData("name", e.target.value)
    );

    document.addEventListener("keypress", (e) => {
      if (e.key === "Enter" && !this.state.token && document.activeElement.tagName === "INPUT") {
        this.handleSubmit(e);
      }
    });
  }

  toggleMode() {
    this.state.toggleMode();
    this.ui.clearForm();
    this.ui.hideMessage();
    this.ui.updateModeUI(this.state.isLogin);
  }

  async handleSubmit(e) {
    e.preventDefault();
    this.state.setLoading(true);
    this.ui.setLoading(true, this.state.isLogin);
    this.ui.hideMessage();

    try {
      const { response, data } = this.state.isLogin
        ? await this.api.login(this.state.formData.email, this.state.formData.password)
        : await this.api.signup(this.state.formData.name, this.state.formData.email, this.state.formData.password);

      if (response.ok) {
        this.ui.showMessage(
          this.state.isLogin ? "Login successful!" : "Account created successfully!",
          "success"
        );

        if (data.token) {
          this.state.setToken(data.token);
          this.ui.showWelcomeScreen(data.token);
        }

        this.state.reset();
        this.ui.clearForm();
      } else {
        this.ui.showMessage(data.detail || "An error occurred", "error");
      }
    } catch (error) {
      console.error("Connection error:", error);
      this.ui.showMessage(
        `Failed to connect to server at ${config.API_URL}. Make sure backend is running.`,
        "error"
      );
    } finally {
      this.state.setLoading(false);
      this.ui.setLoading(false, this.state.isLogin);
    }
  }

  handleLogout() {
    this.state.token = null;
    this.state.isLogin = true;
    this.state.reset();
    this.ui.clearForm();
    this.ui.showAuthForm();
    this.ui.updateModeUI(true);
    this.ui.showMessage("Logged out successfully", "success");
  }
}