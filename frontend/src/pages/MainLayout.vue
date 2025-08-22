<template>
  <div class="main-layout">
    <!-- Navigation Header -->
    <header class="navbar">
      <div class="nav-container">
        <!-- Logo -->
        <div class="nav-brand">
          <div class="logo">
            <div class="logo-icon">💡</div>
            <span class="logo-text">Ideate</span>
          </div>
        </div>

        <!-- Navigation Links -->
        <nav class="nav-links">
          <router-link 
            to="/discover" 
            class="nav-link"
            :class="{ active: $route.path === '/discover' }"
          >
            Discover
          </router-link>
          <router-link 
            to="/dashboard" 
            class="nav-link"
            :class="{ active: $route.path === '/dashboard' }"
          >
            Dashboard
          </router-link>
          <router-link 
            to="/messages" 
            class="nav-link"
            :class="{ active: $route.path === '/messages' }"
          >
            Messages
          </router-link>
        </nav>

        <!-- User Profile -->
        <div class="nav-profile">
          <div class="profile-avatar">
            <span>{{ userInitials }}</span>
          </div>
          <span class="profile-name">{{ userName }}</span>
        </div>
      </div>
    </header>

    <!-- Main Content -->
    <main class="main-content">
      <router-view />
    </main>
  </div>
</template>

<script>
export default {
  name: 'MainLayout',
  data() {
    return {
      userName: 'Ranganathan R R'
    }
  },
  computed: {
    userInitials() {
      return this.userName
        .split(' ')
        .map(name => name.charAt(0))
        .slice(0, 2)
        .join('')
    }
  }
}
</script>

<style scoped>
.main-layout {
  min-height: 100vh;
  background-color: #f8f9fa;
}

.navbar {
  background: white;
  border-bottom: 1px solid #e9ecef;
  position: sticky;
  top: 0;
  z-index: 100;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.nav-container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 2rem;
  display: flex;
  align-items: center;
  justify-content: space-between;
  height: 70px;
}

.nav-brand {
  display: flex;
  align-items: center;
}

.logo {
  display: flex;
  align-items: center;
  gap: 0.5rem;
}

.logo-icon {
  width: 40px;
  height: 40px;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  border-radius: 12px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 20px;
}

.logo-text {
  font-size: 24px;
  font-weight: 700;
  color: #2d3748;
}

.nav-links {
  display: flex;
  gap: 2rem;
}

.nav-link {
  text-decoration: none;
  color: #6b7280;
  font-weight: 500;
  padding: 0.5rem 1rem;
  border-radius: 8px;
  transition: all 0.2s ease;
  position: relative;
}

.nav-link:hover {
  color: #4f46e5;
  background-color: #f3f4f6;
}

.nav-link.active {
  color: #4f46e5;
  background-color: #eef2ff;
}

.nav-profile {
  display: flex;
  align-items: center;
  gap: 0.75rem;
}

.profile-avatar {
  width: 40px;
  height: 40px;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  color: white;
  font-weight: 600;
  font-size: 14px;
}

.profile-name {
  font-weight: 500;
  color: #374151;
}

.main-content {
  padding: 2rem;
  max-width: 1200px;
  margin: 0 auto;
}

@media (max-width: 768px) {
  .nav-container {
    padding: 0 1rem;
  }
  
  .nav-links {
    gap: 1rem;
  }
  
  .nav-link {
    padding: 0.5rem;
    font-size: 14px;
  }
  
  .profile-name {
    display: none;
  }
  
  .main-content {
    padding: 1rem;
  }
}
</style>