export class UIController {
  constructor() {
    this.elements = {
      authForm: document.getElementById("authForm"),
      welcomeScreen: document.getElementById("welcomeScreen"),
      formTitle: document.getElementById("formTitle"),
      formSubtitle: document.getElementById("formSubtitle"),
      nameGroup: document.getElementById("nameGroup"),
      emailInput: document.getElementById("email"),
      passwordInput: document.getElementById("password"),
      nameInput: document.getElementById("name"),
      submitBtn: document.getElementById("submitBtn"),
      messageContainer: document.getElementById("messageContainer"),
      toggleText: document.getElementById("toggleText"),
      tokenDisplay: document.getElementById("tokenDisplay"),
      headerIcon: document.getElementById("headerIcon"),
    };
  }

  updateModeUI(isLogin) {
    const { formTitle, formSubtitle, submitBtn, toggleText, nameGroup, headerIcon } = this.elements;

    if (isLogin) {
      formTitle.textContent = "Welcome Back";
      formSubtitle.textContent = "Sign in to your account";
      submitBtn.textContent = "Sign In";
      toggleText.textContent = "Don't have an account? Sign up";
      nameGroup.classList.add("hidden");
    } else {
      formTitle.textContent = "Create Account";
      formSubtitle.textContent = "Sign up to get started";
      submitBtn.textContent = "Sign Up";
      toggleText.textContent = "Already have an account? Sign in";
      nameGroup.classList.remove("hidden");
    }
    
    headerIcon.style.background = "#e0e7ff";
    headerIcon.style.color = "#4f46e5";
  }

  showMessage(text, type) {
    this.elements.messageContainer.innerHTML = `
      <div class="message ${type}">
        <span>${type === "success" ? "✓" : "⚠️"}</span>
        <span>${text}</span>
      </div>
    `;
    this.elements.messageContainer.classList.remove("hidden");
  }

  hideMessage() {
    this.elements.messageContainer.classList.add("hidden");
  }

  clearForm() {
    const { emailInput, passwordInput, nameInput } = this.elements;
    emailInput.value = "";
    passwordInput.value = "";
    nameInput.value = "";
  }

  setLoading(loading, isLogin) {
    this.elements.submitBtn.disabled = loading;
    this.elements.submitBtn.textContent = loading ? "Processing..." : (isLogin ? "Sign In" : "Sign Up");
  }

  showWelcomeScreen(token) {
    this.elements.authForm.classList.add("hidden");
    this.elements.welcomeScreen.classList.remove("hidden");
    this.elements.tokenDisplay.textContent = token;
  }

  showAuthForm() {
    const { authForm, welcomeScreen, messageContainer, nameGroup } = this.elements;
    authForm.classList.remove("hidden");
    welcomeScreen.classList.add("hidden");
    messageContainer.classList.add("hidden");
    nameGroup.classList.add("hidden");
  }
}