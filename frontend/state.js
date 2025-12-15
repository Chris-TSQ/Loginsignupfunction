export class AppState {
  constructor() {
    this.isLogin = true;
    this.formData = { email: "", password: "", name: "" };
    this.message = { text: "", type: "" };
    this.loading = false;
    this.token = null;
  }

  reset() {
    this.formData = { email: "", password: "", name: "" };
    this.message = { text: "", type: "" };
  }

  toggleMode() {
    this.isLogin = !this.isLogin;
    this.reset();
  }

  setLoading(loading) {
    this.loading = loading;
  }

  setToken(token) {
    this.token = token;
  }

  setMessage(text, type) {
    this.message = { text, type };
  }

  updateFormData(field, value) {
    this.formData[field] = value;
  }
}