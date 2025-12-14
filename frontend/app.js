let state = {
  isLogin: true,
  formData: {
    email: "",
    password: "",
    name: "",
  },
  message: { text: "", type: "" },
  loading: false,
  token: null,
};

const API_URL = process.env.REACT_APP_API_URL;

fetch(`${API_URL}/signup`, {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify(userData)
})

const authForm = document.getElementById("authForm");
const welcomeScreen = document.getElementById("welcomeScreen");
const formTitle = document.getElementById("formTitle");
const formSubtitle = document.getElementById("formSubtitle");
const nameGroup = document.getElementById("nameGroup");
const emailInput = document.getElementById("email");
const passwordInput = document.getElementById("password");
const nameInput = document.getElementById("name");
const submitBtn = document.getElementById("submitBtn");
const messageContainer = document.getElementById("messageContainer");
const toggleText = document.getElementById("toggleText");
const tokenDisplay = document.getElementById("tokenDisplay");
const headerIcon = document.getElementById("headerIcon");

emailInput.addEventListener("change", (e) => {
  state.formData.email = e.target.value;
});

passwordInput.addEventListener("change", (e) => {
  state.formData.password = e.target.value;
});

nameInput.addEventListener("change", (e) => {
  state.formData.name = e.target.value;
});

document.addEventListener("keypress", (e) => {
  if (
    e.key === "Enter" &&
    !state.token &&
    document.activeElement.tagName === "INPUT"
  ) {
    handleSubmit(e);
  }
});

// Toggle between login and signup
function toggleMode() {
  state.isLogin = !state.isLogin;
  state.message = { text: "", type: "" };
  state.formData = { email: "", password: "", name: "" };

  // Update form
  emailInput.value = "";
  passwordInput.value = "";
  nameInput.value = "";
  messageContainer.classList.add("hidden");

  // Update UI
  if (state.isLogin) {
    formTitle.textContent = "Welcome Back";
    formSubtitle.textContent = "Sign in to your account";
    submitBtn.textContent = "Sign In";
    toggleText.textContent = "Don't have an account? Sign up";
    nameGroup.classList.add("hidden");
    headerIcon.style.background = "#e0e7ff";
    headerIcon.style.color = "#4f46e5";
  } else {
    formTitle.textContent = "Create Account";
    formSubtitle.textContent = "Sign up to get started";
    submitBtn.textContent = "Sign Up";
    toggleText.textContent = "Already have an account? Sign in";
    nameGroup.classList.remove("hidden");
    headerIcon.style.background = "#e0e7ff";
    headerIcon.style.color = "#4f46e5";
  }
}

// Display message
function showMessage(text, type) {
  state.message = { text, type };
  messageContainer.innerHTML = `
    <div class="message ${type}">
      <span>${type === "success" ? "✓" : "⚠️"}</span>
      <span>${text}</span>
    </div>
  `;
  messageContainer.classList.remove("hidden");
}

async function handleSubmit(e) {
  e.preventDefault();

  state.loading = true;
  submitBtn.disabled = true;
  submitBtn.textContent = "Processing...";
  messageContainer.classList.add("hidden");

  try {
    const endpoint = state.isLogin ? "/login" : "/signup";
    const body = state.isLogin
      ? { email: state.formData.email, password: state.formData.password }
      : state.formData;

    const response = await fetch(`${API_URL}${endpoint}`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(body),
    });

    const data = await response.json();

    if (response.ok) {
      showMessage(
        state.isLogin ? "Login successful!" : "Account created successfully!",
        "success"
      );

      if (data.token) {
        state.token = data.token;
        showWelcomeScreen();
      }

      state.formData = { email: "", password: "", name: "" };
      emailInput.value = "";
      passwordInput.value = "";
      nameInput.value = "";
    } else {
      showMessage(data.detail || "An error occurred", "error");
    }
  } catch (error) {
    showMessage(
      "Failed to connect to server. Make sure backend is running.",
      "error"
    );
  } finally {
    state.loading = false;
    submitBtn.disabled = false;
    submitBtn.textContent = state.isLogin ? "Sign In" : "Sign Up";
  }
}

// Show welcome screen after login
function showWelcomeScreen() {
  authForm.classList.add("hidden");
  welcomeScreen.classList.remove("hidden");
  tokenDisplay.textContent = state.token;
}

function handleLogout() {
  state.token = null;
  state.isLogin = true;
  state.message = { text: "", type: "" };
  state.formData = { email: "", password: "", name: "" };

  // Reset form
  emailInput.value = "";
  passwordInput.value = "";
  nameInput.value = "";

  // Show form
  authForm.classList.remove("hidden");
  welcomeScreen.classList.add("hidden");
  messageContainer.classList.add("hidden");
  nameGroup.classList.add("hidden");

  // Update UI
  formTitle.textContent = "Welcome Back";
  formSubtitle.textContent = "Sign in to your account";
  submitBtn.textContent = "Sign In";
  toggleText.textContent = "Don't have an account? Sign up";

  showMessage("Logged out successfully", "success");
}
