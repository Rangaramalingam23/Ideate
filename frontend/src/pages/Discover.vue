<template>
  <div class="discover">
    <!-- Header Section -->
    <div class="discover-header">
      <h1 class="page-title">Discover Projects</h1>
      <p class="page-subtitle">Explore innovative ideas and find your next collaboration opportunity</p>
      
      <!-- Post Project Button -->
      <div class="header-actions">
        <button class="post-project-btn">
          <svg class="btn-icon" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 6v6m0 0v6m0-6h6m-6 0H6"></path>
          </svg>
          Post Project
        </button>
      </div>
    </div>

    <!-- Error Alert -->
    <div v-if="showError" class="error-alert">
      <div class="error-content">
        <svg class="error-icon" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4m0 4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"></path>
        </svg>
        <span>Request failed with status code 404</span>
      </div>
    </div>

    <!-- Search and Filters -->
    <div class="search-filters">
      <!-- Search Bar -->
      <div class="search-container">
        <div class="search-box">
          <svg class="search-icon" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"></path>
          </svg>
          <input 
            type="text" 
            v-model="searchQuery"
            placeholder="Search projects by title, description, or tags..."
            class="search-input"
          >
        </div>
      </div>

      <!-- Filter Row -->
      <div class="filter-row">
        <!-- Category Filter -->
        <div class="filter-group">
          <label class="filter-label">Category</label>
          <select v-model="selectedCategory" class="filter-select">
            <option value="">All Categories</option>
            <option v-for="category in categories" :key="category" :value="category">
              {{ category }}
            </option>
          </select>
        </div>

        <!-- Status Filter -->
        <div class="filter-group">
          <label class="filter-label">Status</label>
          <select v-model="selectedStatus" class="filter-select">
            <option value="">All Status</option>
            <option v-for="status in statuses" :key="status" :value="status">
              {{ status }}
            </option>
          </select>
        </div>
      </div>

      <!-- Tag Filters -->
      <div class="tags-section">
        <span class="tags-label">Tags</span>
        <div class="tags-container">
          <button 
            v-for="tag in availableTags" 
            :key="tag"
            @click="toggleTag(tag)"
            class="tag-btn"
            :class="{ active: selectedTags.includes(tag) }"
          >
            {{ tag }}
          </button>
        </div>
      </div>
    </div>

    <!-- Projects Count -->
    <div class="projects-count">
      <span>Showing {{ filteredProjects.length }} projects</span>
    </div>

    <!-- Projects Grid -->
    <div v-if="filteredProjects.length > 0" class="projects-grid">
      <div 
        v-for="project in filteredProjects" 
        :key="project.id"
        class="project-card"
      >
        <div class="project-header">
          <h3 class="project-title">{{ project.title }}</h3>
          <span class="project-status" :class="project.status.toLowerCase()">
            {{ project.status }}
          </span>
        </div>
        <p class="project-description">{{ project.description }}</p>
        <div class="project-tags">
          <span 
            v-for="tag in project.tags" 
            :key="tag"
            class="project-tag"
          >
            {{ tag }}
          </span>
        </div>
        <div class="project-footer">
          <div class="project-author">
            <div class="author-avatar">
              {{ getInitials(project.author) }}
            </div>
            <span class="author-name">{{ project.author }}</span>
          </div>
          <div class="project-stats">
            <span class="stat-item">
              <svg class="stat-icon" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z"></path>
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M2.458 12C3.732 7.943 7.523 5 12 5c4.478 0 8.268 2.943 9.542 7-1.274 4.057-5.064 7-9.542 7-4.477 0-8.268-2.943-9.542-7z"></path>
              </svg>
              {{ project.views }}
            </span>
            <span class="stat-item">
              <svg class="stat-icon" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4.318 6.318a4.5 4.5 0 000 6.364L12 20.364l7.682-7.682a4.5 4.5 0 00-6.364-6.364L12 7.636l-1.318-1.318a4.5 4.5 0 00-6.364 0z"></path>
              </svg>
              {{ project.likes }}
            </span>
          </div>
        </div>
      </div>
    </div>

    <!-- Empty State -->
    <div v-else class="empty-state">
      <div class="empty-icon">💡</div>
      <h3 class="empty-title">No projects found</h3>
      <p class="empty-description">Try adjusting your filters or check back later for new projects.</p>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Discover',
  data() {
    return {
      searchQuery: '',
      selectedCategory: '',
      selectedStatus: '',
      selectedTags: [],
      showError: true,
      categories: [
        'Technology',
        'Design',
        'Business',
        'Education',
        'Health',
        'Entertainment'
      ],
      statuses: [
        'Open',
        'In Progress',
        'Completed',
        'On Hold'
      ],
      availableTags: [
        'AI', 'Mobile App', 'Web Platform', 'IoT', 'Blockchain', 'VR',
        'Machine Learning', 'Healthcare', 'Finance', 'Gaming', 'Social',
        'Productivity', 'Hardware', 'API', 'Cloud', 'Security'
      ],
      projects: [
        {
          id: 1,
          title: 'AI-Powered Health Monitoring App',
          description: 'A mobile application that uses machine learning to monitor and predict health issues based on user data and symptoms.',
          author: 'Dr. Sarah Johnson',
          status: 'Open',
          category: 'Healthcare',
          tags: ['AI', 'Mobile App', 'Healthcare'],
          views: 245,
          likes: 32
        },
        {
          id: 2,
          title: 'Blockchain-Based Voting System',
          description: 'Secure and transparent digital voting platform using blockchain technology to ensure election integrity.',
          author: 'Michael Chen',
          status: 'In Progress',
          category: 'Technology',
          tags: ['Blockchain', 'Security', 'Web Platform'],
          views: 189,
          likes: 28
        },
        {
          id: 3,
          title: 'Virtual Reality Learning Platform',
          description: 'An immersive VR environment for educational content delivery, making learning more engaging and interactive.',
          author: 'Emily Rodriguez',
          status: 'Open',
          category: 'Education',
          tags: ['VR', 'Education', 'Gaming'],
          views: 156,
          likes: 24
        }
      ]
    }
  },
  computed: {
    filteredProjects() {
      return this.projects.filter(project => {
        const matchesSearch = this.searchQuery === '' || 
          project.title.toLowerCase().includes(this.searchQuery.toLowerCase()) ||
          project.description.toLowerCase().includes(this.searchQuery.toLowerCase()) ||
          project.tags.some(tag => tag.toLowerCase().includes(this.searchQuery.toLowerCase()))

        const matchesCategory = this.selectedCategory === '' || 
          project.category === this.selectedCategory

        const matchesStatus = this.selectedStatus === '' || 
          project.status === this.selectedStatus

        const matchesTags = this.selectedTags.length === 0 ||
          this.selectedTags.some(tag => project.tags.includes(tag))

        return matchesSearch && matchesCategory && matchesStatus && matchesTags
      })
    }
  },
  mounted() {
    setTimeout(() => {
      this.showError = false
    }, 3000)
  },
  methods: {
    toggleTag(tag) {
      const index = this.selectedTags.indexOf(tag)
      if (index > -1) {
        this.selectedTags.splice(index, 1)
      } else {
        this.selectedTags.push(tag)
      }
    },
    getInitials(name) {
      return name.split(' ').map(n => n[0]).join('').slice(0, 2)
    }
  }
}
</script>

<style scoped>
.discover {
  max-width: 1200px;
  margin: 0 auto;
}

.discover-header {
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
  margin-bottom: 2rem;
  flex-wrap: wrap;
  gap: 1rem;
}

.page-title {
  font-size: 2.5rem;
  font-weight: 700;
  color: #1a202c;
  margin-bottom: 0.5rem;
}

.page-subtitle {
  color: #718096;
  font-size: 1.1rem;
}

.header-actions {
  display: flex;
  gap: 1rem;
}

.post-project-btn {
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  color: white;
  border: none;
  padding: 0.75rem 1.5rem;
  border-radius: 8px;
  font-weight: 600;
  display: flex;
  align-items: center;
  gap: 0.5rem;
  cursor: pointer;
  transition: transform 0.2s ease;
}

.post-project-btn:hover {
  transform: translateY(-1px);
}

.btn-icon {
  width: 20px;
  height: 20px;
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

.search-filters {
  background: white;
  padding: 1.5rem;
  border-radius: 12px;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
  margin-bottom: 2rem;
}

.search-container {
  margin-bottom: 1.5rem;
}

.search-box {
  position: relative;
  max-width: 600px;
}

.search-icon {
  position: absolute;
  left: 1rem;
  top: 50%;
  transform: translateY(-50%);
  width: 20px;
  height: 20px;
  color: #9ca3af;
}

.search-input {
  width: 100%;
  padding: 0.75rem 1rem 0.75rem 3rem;
  border: 2px solid #e5e7eb;
  border-radius: 8px;
  font-size: 1rem;
  transition: border-color 0.2s ease;
}

.search-input:focus {
  outline: none;
  border-color: #667eea;
}

.filter-row {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: 1rem;
  margin-bottom: 1.5rem;
}

.filter-group {
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
}

.filter-label {
  font-weight: 600;
  color: #374151;
  font-size: 0.875rem;
}

.filter-select {
  padding: 0.5rem;
  border: 2px solid #e5e7eb;
  border-radius: 6px;
  background: white;
  font-size: 0.875rem;
  transition: border-color 0.2s ease;
}

.filter-select:focus {
  outline: none;
  border-color: #667eea;
}

.tags-section {
  border-top: 1px solid #e5e7eb;
  padding-top: 1.5rem;
}

.tags-label {
  font-weight: 600;
  color: #374151;
  font-size: 0.875rem;
  margin-bottom: 0.75rem;
  display: block;
}

.tags-container {
  display: flex;
  flex-wrap: wrap;
  gap: 0.5rem;
}

.tag-btn {
  padding: 0.5rem 1rem;
  border: 2px solid #e5e7eb;
  border-radius: 20px;
  background: white;
  color: #6b7280;
  font-size: 0.875rem;
  cursor: pointer;
  transition: all 0.2s ease;
}

.tag-btn:hover {
  border-color: #667eea;
  color: #667eea;
}

.tag-btn.active {
  background: #667eea;
  border-color: #667eea;
  color: white;
}

.projects-count {
  margin-bottom: 1.5rem;
  color: #6b7280;
  font-weight: 500;
}

.projects-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(350px, 1fr));
  gap: 1.5rem;
}

.project-card {
  background: white;
  border-radius: 12px;
  padding: 1.5rem;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
  transition: transform 0.2s ease, box-shadow 0.2s ease;
  cursor: pointer;
}

.project-card:hover {
  transform: translateY(-2px);
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
}

.project-header {
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
  margin-bottom: 1rem;
  gap: 1rem;
}

.project-title {
  font-size: 1.25rem;
  font-weight: 600;
  color: #1a202c;
  flex: 1;
}

.project-status {
  padding: 0.25rem 0.75rem;
  border-radius: 20px;
  font-size: 0.75rem;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.5px;
}

.project-status.open {
  background: #d1fae5;
  color: #065f46;
}

.project-status.in.progress {
  background: #fef3c7;
  color: #92400e;
}

.project-status.completed {
  background: #dbeafe;
  color: #1e40af;
}

.project-description {
  color: #4b5563;
  line-height: 1.6;
  margin-bottom: 1rem;
}

.project-tags {
  display: flex;
  flex-wrap: wrap;
  gap: 0.5rem;
  margin-bottom: 1rem;
}

.project-tag {
  background: #f3f4f6;
  color: #374151;
  padding: 0.25rem 0.75rem;
  border-radius: 12px;
  font-size: 0.75rem;
  font-weight: 500;
}

.project-footer {
  display: flex;
  justify-content: space-between;
  align-items: center;
  border-top: 1px solid #f3f4f6;
  padding-top: 1rem;
}

.project-author {
  display: flex;
  align-items: center;
  gap: 0.75rem;
}

.author-avatar {
  width: 32px;
  height: 32px;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  color: white;
  font-weight: 600;
  font-size: 0.75rem;
}

.author-name {
  color: #374151;
  font-weight: 500;
  font-size: 0.875rem;
}

.project-stats {
  display: flex;
  gap: 1rem;
}

.stat-item {
  display: flex;
  align-items: center;
  gap: 0.25rem;
  color: #6b7280;
  font-size: 0.875rem;
}

.stat-icon {
  width: 16px;
  height: 16px;
}

.empty-state {
  text-align: center;
  padding: 4rem 2rem;
  background: white;
  border-radius: 12px;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
}

.empty-icon {
  font-size: 4rem;
  margin-bottom: 1rem;
}

.empty-title {
  font-size: 1.5rem;
  font-weight: 600;
  color: #1a202c;
  margin-bottom: 0.5rem;
}

.empty-description {
  color: #6b7280;
}

@media (max-width: 768px) {
  .discover-header {
    flex-direction: column;
    align-items: stretch;
  }
  
  .page-title {
    font-size: 2rem;
  }
  
  .filter-row {
    grid-template-columns: 1fr;
  }
  
  .projects-grid {
    grid-template-columns: 1fr;
  }
  
  .project-header {
    flex-direction: column;
    align-items: flex-start;
    gap: 0.5rem;
  }
  
  .project-footer {
    flex-direction: column;
    gap: 1rem;
    align-items: flex-start;
  }
}
</style>