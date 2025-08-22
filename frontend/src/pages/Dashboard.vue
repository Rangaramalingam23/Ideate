<template>
  <div class="dashboard">
    <!-- Welcome Header -->
    <div class="welcome-header">
      <h1 class="welcome-title">Welcome back, {{ userName }}</h1>
      <p class="welcome-subtitle">{{ dashboardSubtitle }}</p>
    </div>

    <!-- Error Alert (if any) -->
    <div v-if="showError" class="error-alert">
      <div class="error-content">
        <svg class="error-icon" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4m0 4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"></path>
        </svg>
        <span>Request failed with status code 404</span>
      </div>
    </div>

    <!-- Stats Grid -->
    <div class="stats-grid">
      <div class="stat-card">
        <div class="stat-icon projects-icon">
          <svg fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9.663 17h4.673M12 3v1m6.364 1.636l-.707.707M21 12h-1M4 12H3m3.343-5.657l-.707-.707m2.828 9.9a5 5 0 117.072 0l-.548.547A3.374 3.374 0 0014 18.469V19a2 2 0 11-4 0v-.531c0-.895-.356-1.754-.988-2.386l-.548-.547z"></path>
          </svg>
        </div>
        <div class="stat-content">
          <h3 class="stat-title">Projects Posted</h3>
          <p class="stat-value">{{ stats.projectsPosted }}</p>
        </div>
      </div>

      <div class="stat-card">
        <div class="stat-icon views-icon">
          <svg fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 19v-6a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2a2 2 0 002-2zm0 0V9a2 2 0 012-2h2a2 2 0 012 2v10m-6 0a2 2 0 002 2h2a2 2 0 002-2m0 0V5a2 2 0 012-2h2a2 2 0 012 2v14a2 2 0 01-2 2h-2a2 2 0 01-2-2z"></path>
          </svg>
        </div>
        <div class="stat-content">
          <h3 class="stat-title">Total Views</h3>
          <p class="stat-value">{{ stats.totalViews }}</p>
        </div>
      </div>

      <div class="stat-card">
        <div class="stat-icon developers-icon">
          <svg fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4.354a4 4 0 110 5.292M15 21H3v-1a6 6 0 0112 0v1zm0 0h6v-1a6 6 0 00-9-5.197m13.5-9a2.5 2.5 0 11-5 0 2.5 2.5 0 015 0z"></path>
          </svg>
        </div>
        <div class="stat-content">
          <h3 class="stat-title">Interested Developers</h3>
          <p class="stat-value">{{ stats.interestedDevelopers }}</p>
        </div>
      </div>

      <div class="stat-card">
        <div class="stat-icon backers-icon">
          <svg fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8c-1.657 0-3 .895-3 2s1.343 2 3 2 3 .895 3 2-1.343 2-3 2m0-8c1.11 0 2.08.402 2.599 1M12 8V7m0 1v8m0 0v1m0-1c-1.11 0-2.08-.402-2.599-1M21 12a9 9 0 11-18 0 9 9 0 0118 0z"></path>
          </svg>
        </div>
        <div class="stat-content">
          <h3 class="stat-title">Interested Backers</h3>
          <p class="stat-value">{{ stats.interestedBackers }}</p>
        </div>
      </div>
    </div>

    <!-- Recent Activity Section -->
    <div class="recent-activity">
      <h2 class="section-title">Recent Activity</h2>
      <div class="activity-card">
        <div class="activity-item">
          <div class="activity-icon">
            <svg fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z"></path>
            </svg>
          </div>
          <div class="activity-content">
            <p class="activity-text">Dashboard data loaded successfully</p>
            <span class="activity-time">Just now</span>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Dashboard',
  data() {
    return {
      userName: 'Ranganathan R R',
      dashboardSubtitle: 'Ideator Dashboard • Here\'s What\'s Happening With Your Projects',
      showError: true,
      stats: {
        projectsPosted: 0,
        totalViews: 0,
        interestedDevelopers: 0,
        interestedBackers: 0
      }
    }
  },
  mounted() {
    // Simulate API call
    this.loadDashboardData()
  },
  methods: {
    loadDashboardData() {
      // This would be replaced with actual API calls
      setTimeout(() => {
        this.showError = false
      }, 3000)
    }
  }
}
</script>

<style scoped>
.dashboard {
  max-width: 1200px;
  margin: 0 auto;
}

.welcome-header {
  margin-bottom: 2rem;
}

.welcome-title {
  font-size: 2.5rem;
  font-weight: 700;
  color: #1a202c;
  margin-bottom: 0.5rem;
}

.welcome-subtitle {
  color: #718096;
  font-size: 1.1rem;
}

.error-alert {
  background-color: #fed7d7;
  border: 1px solid #feb2b2;
  border-radius: 8px;
  padding: 1rem;
  margin-bottom: 2rem;
}

.error-content {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  color: #c53030;
}

.error-icon {
  width: 20px;
  height: 20px;
}

.stats-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  gap: 1.5rem;
  margin-bottom: 3rem;
}

.stat-card {
  background: white;
  border-radius: 12px;
  padding: 1.5rem;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
  display: flex;
  align-items: center;
  gap: 1rem;
  transition: transform 0.2s ease, box-shadow 0.2s ease;
}

.stat-card:hover {
  transform: translateY(-2px);
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
}

.stat-icon {
  width: 60px;
  height: 60px;
  border-radius: 12px;
  display: flex;
  align-items: center;
  justify-content: center;
  flex-shrink: 0;
}

.stat-icon svg {
  width: 30px;
  height: 30px;
}

.projects-icon {
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  color: white;
}

.views-icon {
  background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
  color: white;
}

.developers-icon {
  background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%);
  color: white;
}

.backers-icon {
  background: linear-gradient(135deg, #43e97b 0%, #38f9d7 100%);
  color: white;
}

.stat-content {
  flex: 1;
}

.stat-title {
  font-size: 0.875rem;
  color: #718096;
  margin-bottom: 0.25rem;
  font-weight: 500;
}

.stat-value {
  font-size: 2rem;
  font-weight: 700;
  color: #1a202c;
}

.recent-activity {
  background: white;
  border-radius: 12px;
  padding: 1.5rem;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
}

.section-title {
  font-size: 1.5rem;
  font-weight: 600;
  color: #1a202c;
  margin-bottom: 1rem;
}

.activity-card {
  background: #f7fafc;
  border-radius: 8px;
  padding: 1rem;
}

.activity-item {
  display: flex;
  align-items: center;
  gap: 1rem;
}

.activity-icon {
  width: 40px;
  height: 40px;
  background: #667eea;
  border-radius: 8px;
  display: flex;
  align-items: center;
  justify-content: center;
  color: white;
}

.activity-icon svg {
  width: 20px;
  height: 20px;
}

.activity-content {
  flex: 1;
}

.activity-text {
  color: #2d3748;
  font-weight: 500;
  margin-bottom: 0.25rem;
}

.activity-time {
  color: #718096;
  font-size: 0.875rem;
}

@media (max-width: 768px) {
  .welcome-title {
    font-size: 2rem;
  }
  
  .stats-grid {
    grid-template-columns: 1fr;
    gap: 1rem;
  }
  
  .stat-card {
    padding: 1rem;
  }
  
  .stat-value {
    font-size: 1.5rem;
  }
}
</style>