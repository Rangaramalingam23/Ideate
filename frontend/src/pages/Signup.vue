<template>
  <div class="auth-page">
    <div class="logo">
      <span class="logo-icon">💡</span> Ideate
    </div>
    <div class="auth-container">
      <h1>Join Ideate</h1>
      <p class="subtitle">Create your account and start collaborating today.</p>
      <p class="info">"Unleash your creativity, connect with visionaries, and build the future together!"</p>
      <p class="info-sub">Ideate brings together ideators with brilliant concepts, developers with the skills to create, and backers ready to fund innovation. Collaborate directly, spark ideas, and turn dreams into reality.</p>
      
      <form v-if="!showQR" @submit.prevent="handleSignup">
        <label>Sign up as</label>
        <div 
          class="role-option" 
          :class="{ selected: selectedRole === 'Ideator' }" 
          @click="selectRole('Ideator')"
        >
          <span class="role-icon ideator">💡</span> Ideator
          <p>Share your innovative ideas and find the right team to bring them to life.</p>
        </div>
        <div 
          class="role-option" 
          :class="{ selected: selectedRole === 'Developer' }" 
          @click="selectRole('Developer')"
        >
          <span class="role-icon developer">&lt;/&gt;</span> Developer
          <p>Discover exciting projects and collaborate with visionary ideators.</p>
        </div>
        <div 
          class="role-option" 
          :class="{ selected: selectedRole === 'Backer' }" 
          @click="selectRole('Backer')"
        >
          <span class="role-icon backer">$</span> Backer
          <p>Invest in promising ideas and support the next generation of innovations.</p>
        </div>
        
        <p class="role-message">You are signing up as: <strong>{{ selectedRole }}</strong></p>
        
        <label for="full-name">Full Name</label>
        <input id="full-name" type="text" placeholder="Enter your full name" required>
        
        <label for="email">Email Address</label>
        <input id="email" type="email" placeholder="Enter your email" required>
        
        <label for="password">Password</label>
        <input id="password" type="password" placeholder="Enter your password" required>
        
        <button type="submit" class="auth-btn">Create Account</button>
      </form>
      
      <div v-if="showQR" class="qr-section">
        <h2>Set up Two-Factor Authentication</h2>
        <p>Scan this QR code with your authenticator app (e.g., Google Authenticator) to set up TOTP.</p>
        <img :src="qrCode" alt="TOTP QR Code" class="qr-code">
        <p>After scanning, enter the code from your app to verify.</p>
        <input type="text" placeholder="Enter TOTP code" maxlength="6" required>
        <button @click="handleVerifyTOTP" class="auth-btn">Verify and Complete Signup</button>
      </div>
      <p class="switch">Already have an account? <router-link to="/login">Sign in</router-link></p>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue';

// Placeholder for QR code (in real app, generate dynamically)
const qrCode = ref('https://via.placeholder.com/200?text=QR+Code');
const showQR = ref(false);
const selectedRole = ref('Ideator');

const selectRole = (role) => {
  selectedRole.value = role;
};

const handleSignup = () => {
  // Simulate signup success, show QR
  showQR.value = true;
};

const handleVerifyTOTP = () => {
  // Simulate verification, navigate or something
  alert('Signup complete!');
};
</script>

<style scoped>
.auth-page {
  display: flex;
  flex-direction: column;
  align-items: center;
  min-height: 100vh;
  background-color: #f0f9ff;
  padding: 2rem;
}

.logo {
  font-size: 1.5rem;
  font-weight: 700;
  color: #6366f1;
  margin-bottom: 2rem;
}

.logo-icon {
  color: #3b82f6;
}

.auth-container {
  background-color: white;
  padding: 2rem;
  border-radius: 1rem;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  max-width: 400px;
  width: 100%;
  text-align: left;
}

h1 {
  font-size: 2rem;
  font-weight: 700;
  color: #1e3a8a;
  margin-bottom: 0.5rem;
}

.subtitle {
  color: #6b7280;
  margin-bottom: 1rem;
}

.info {
  color: #1e3a8a;
  font-size: 1rem;
  font-style: italic;
  margin-bottom: 0.5rem;
  font-weight: 600;
}

.info-sub {
  color: #6b7280;
  font-size: 0.875rem;
  margin-bottom: 1.5rem;
}

label {
  display: block;
  font-size: 0.875rem;
  font-weight: 600;
  color: #1e3a8a;
  margin-bottom: 0.5rem;
}

input {
  width: 100%;
  padding: 0.75rem;
  border: 1px solid #d1d5db;
  border-radius: 0.375rem;
  margin-bottom: 1rem;
}

.role-option {
  background-color: #f9fafb;
  padding: 1rem;
  border-radius: 0.5rem;
  margin-bottom: 1rem;
  cursor: pointer;
}

.role-option.selected {
  background-color: #dbeafe;
  border: 1px solid #3b82f6;
}

.role-icon {
  font-size: 1rem;
  margin-right: 0.5rem;
}

.role-option p {
  font-size: 0.875rem;
  color: #6b7280;
  margin: 0;
}

.role-message {
  font-size: 0.875rem;
  color: #1e3a8a;
  margin-bottom: 1rem;
  font-weight: 500;
}

.auth-btn {
  width: 100%;
  background: linear-gradient(to right, #6366f1, #a855f7);
  color: white;
  padding: 0.75rem;
  border: none;
  border-radius: 0.375rem;
  font-weight: 600;
  cursor: pointer;
  margin-top: 1rem;
}

.qr-section {
  text-align: center;
}

.qr-code {
  width: 200px;
  height: 200px;
  margin: 1rem auto;
  display: block;
}

.switch {
  text-align: center;
  color: #6b7280;
  font-size: 0.875rem;
  margin-top: 1rem;
}

.switch a {
  color: #6366f1;
  text-decoration: none;
}
</style>