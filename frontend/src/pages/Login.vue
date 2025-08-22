```vue
<template>
  <div class="auth-page">
    <div class="logo">
      <div class="emoji" style="font-size: 24px;">💡</div> Ideate
    </div>
    <div class="auth-container">
      <h1>Welcome back</h1>
      <p class="subtitle">Sign in to your account to continue collaborating.</p>
      <p class="info">"Unleash your creativity, connect with visionaries, and build the future together!"</p>
      <p class="info-sub">Ideate brings together ideators with brilliant concepts, developers with the skills to create, and backers ready to fund innovation. Collaborate directly, spark ideas, and turn dreams into reality.</p>
      
      <form v-if="!showTOTP" @submit.prevent="handleLogin">
        <label>Sign in as</label>
        <div 
          class="role-option" 
          :class="{ selected: selectedRole === 'Ideator' }" 
          @click="selectRole('Ideator')"
        >
          <div class="emoji" style="font-size: 20px;">💡</div> Ideator
          <p>Share your innovative ideas and find the right team to bring them to life.</p>
        </div>
        <div 
          class="role-option" 
          :class="{ selected: selectedRole === 'Developer' }" 
          @click="selectRole('Developer')"
        >
          <div class="emoji" style="font-size: 20px;">&lt;/&gt;</div> Developer
          <p>Discover exciting projects and collaborate with visionary ideators.</p>
        </div>
        <div 
          class="role-option" 
          :class="{ selected: selectedRole === 'Backer' }" 
          @click="selectRole('Backer')"
        >
          <div class="emoji" style="font-size: 20px;">$</div> Backer
          <p>Invest in promising ideas and support the next generation of innovations.</p>
        </div>
        
        <p class="role-message">You are signing in as: <strong>{{ selectedRole }}</strong></p>
        
        <label for="email">Email Address</label>
        <input id="email" type="email" placeholder="Enter your email" required>
        
        <label for="password">Password</label>
        <input id="password" type="password" placeholder="Enter your password" required>
        
        <button type="submit" class="auth-btn">Sign In</button>
      </form>
      
      <div v-if="showTOTP" class="totp-section">
        <h2>Two-Factor Authentication</h2>
        <p>Enter the 6-digit code from your authenticator app.</p>
        <input type="text" placeholder="Enter TOTP code" maxlength="6" required>
        <button @click="handleVerifyTOTP" class="auth-btn">Verify and Sign In</button>
      </div>
      
      <p class="switch">Don't have an account? <router-link to="/signup">Sign up</router-link></p>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import { useRouter } from 'vue-router';

const showTOTP = ref(false);
const selectedRole = ref('Ideator');
const router = useRouter();

const selectRole = (role) => {
  selectedRole.value = role;
};

const handleLogin = () => {
  showTOTP.value = true;
};

const handleVerifyTOTP = () => {
  router.push('/dashboard');
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
  display: flex;
  align-items: center;
}

.emoji {
  margin-right: 0.5rem;
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
  display: flex;
  align-items: center;
}

.role-option.selected {
  background-color: #dbeafe;
  border: 1px solid #3b82f6;
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

.totp-section {
  text-align: center;
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