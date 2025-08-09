<!-- landingpage.vue -->
<template>
  <div class="landing-page">
    <header class="header">
      <div class="logo">
        <span class="logo-icon">💡</span> Ideate
      </div>
      <nav class="nav">
        <a href="#" class="sign-in">Sign In</a>
        <button class="get-started">Get Started</button>
      </nav>
    </header>

    <section class="hero section-animate">
      <h1 class="hero-title">Collaborate to<br>Create Innovation</h1>
      <p class="hero-subtitle">Bridge the gap between ideators, developers, and backers. Transform innovative ideas into reality through seamless collaboration and funding.</p>
      <div class="hero-buttons">
        <button class="primary-btn">Get Started Today →</button>
        <button class="secondary-btn">Explore Projects</button>
      </div>
    </section>

    <section class="features section-animate">
      <div class="feature-card animate-child" style="--child-index: 1;">
        <div class="feature-icon funding">$</div>
        <h3>Funding Opportunities</h3>
        <p>Backers can discover high-potential projects and provide the funding needed to bring ideas to life.</p>
      </div>
      <div class="feature-card animate-child" style="--child-index: 2;">
        <div class="feature-icon communication">💬</div>
        <h3>Direct Communication</h3>
        <p>Built-in messaging system enables seamless communication without third-party intermediaries.</p>
      </div>
      <div class="feature-card animate-child" style="--child-index: 3;">
        <div class="feature-icon secure">🛡️</div>
        <h3>Secure Platform</h3>
        <p>Enterprise-grade security ensures your ideas, conversations, and transactions are protected.</p>
      </div>
    </section>

    <section class="how-it-works section-animate">
      <h2>How It Works</h2>
      <p class="subtitle">From idea to reality in four simple steps. Our platform streamlines the collaboration process.</p>
      <div class="steps-container">
        <div class="steps-line"></div>
        <div class="steps">
          <div class="step animate-child" style="--child-index: 1;">
            <div class="step-number">1</div>
            <div class="step-icon blue">+</div>
            <div class="step-label ideators">Ideators</div>
            <h3>Post Your Idea</h3>
            <p>Ideators share their innovative concepts with detailed descriptions, requirements, and vision.</p>
          </div>
          <div class="step animate-child" style="--child-index: 2;">
            <div class="step-number">2</div>
            <div class="step-icon purple">Q</div>
            <div class="step-label everyone">Everyone</div>
            <h3>Discover & Connect</h3>
            <p>Developers and backers explore projects, express interest, and connect with ideators.</p>
          </div>
          <div class="step animate-child" style="--child-index: 3;">
            <div class="step-number">3</div>
            <div class="step-icon green">🤝</div>
            <div class="step-label teams">Teams</div>
            <h3>Collaborate</h3>
            <p>Teams form through direct communication, skill matching, and shared project goals.</p>
          </div>
          <div class="step animate-child" style="--child-index: 4;">
            <div class="step-number">4</div>
            <div class="step-icon orange">🚀</div>
            <div class="step-label success">Success</div>
            <h3>Build & Launch</h3>
            <p>Projects come to life through collaborative development and strategic funding.</p>
          </div>
        </div>
      </div>
    </section>

    <section class="everything section-animate">
      <h2>Everything You Need to Collaborate</h2>
      <p class="subtitle">Our platform provides all the tools and features needed to transform ideas into successful projects.</p>
      <div class="grid">
        <div class="feature-card animate-child" style="--child-index: 1;">
          <div class="feature-icon role">👥</div>
          <h3>Role-Based Collaboration</h3>
          <p>Connect ideators, developers, and backers in a seamless ecosystem designed for innovation.</p>
        </div>
        <div class="feature-card animate-child" style="--child-index: 2;">
          <div class="feature-icon smart">Q</div>
          <h3>Smart Project Discovery</h3>
          <p>Advanced filtering and AI-powered recommendations help you find the perfect projects and collaborators.</p>
        </div>
        <div class="feature-card animate-child" style="--child-index: 3;">
          <div class="feature-icon matching">➤</div>
          <h3>Developer Matching</h3>
          <p>Intelligent matching system connects projects with developers who have the right skills and experience.</p>
        </div>
        <div class="feature-card animate-child" style="--child-index: 4;">
          <div class="feature-icon funding">$</div>
          <h3>Funding Opportunities</h3>
          <p>Backers can discover high-potential projects and provide the funding needed to bring ideas to life.</p>
        </div>
        <div class="feature-card animate-child" style="--child-index: 5;">
          <div class="feature-icon communication">💬</div>
          <h3>Direct Communication</h3>
          <p>Built-in messaging system enables seamless communication without third-party intermediaries.</p>
        </div>
        <div class="feature-card animate-child" style="--child-index: 6;">
          <div class="feature-icon secure">🛡️</div>
          <h3>Secure Platform</h3>
          <p>Enterprise-grade security ensures your ideas, conversations, and transactions are protected.</p>
        </div>
      </div>
    </section>

    <footer class="footer section-animate">
      <div class="footer-logo">
        <span class="logo-icon">💡</span> Ideate
      </div>
      <p class="footer-desc">Bridge the gap between ideators, developers, and backers to bring innovative ideas to life. Collaborate, create, and transform the future together.</p>
      <div class="footer-links">
        <div class="link-group">
          <h4>Platform</h4>
          <a href="#">Discover Projects</a>
          <a href="#">Dashboard</a>
          <a href="#">Messages</a>
        </div>
        <div class="link-group">
          <h4>Support</h4>
          <a href="#">Help Center</a>
          <a href="#">Community</a>
          <a href="#">Contact Us</a>
        </div>
      </div>
    </footer>
  </div>
</template>

<script setup>
import { onMounted } from 'vue';

onMounted(() => {
  const sections = document.querySelectorAll('.section-animate');
  const options = {
    root: null,
    threshold: 0.1,
    rootMargin: '0px'
  };

  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('visible');
        observer.unobserve(entry.target);
      }
    });
  }, options);

  sections.forEach(section => {
    observer.observe(section);
  });
});
</script>

<style scoped>
.landing-page {
  min-height: 100vh;
  background-color: #f0f9ff;
}

.header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 1rem 4rem;
  background-color: white;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.05);
}

.logo {
  font-size: 1.5rem;
  font-weight: 700;
  color: #1e40af;
}

.logo-icon {
  color: #3b82f6;
  margin-right: 0.25rem;
}

.nav {
  display: flex;
  align-items: center;
  gap: 1.5rem;
}

.sign-in {
  color: #6b7280;
  text-decoration: none;
}

.get-started {
  background-color: #a855f7;
  color: white;
  padding: 0.5rem 1rem;
  border: none;
  border-radius: 9999px;
  cursor: pointer;
}

.hero {
  text-align: center;
  padding: 4rem 0;
  position: relative;
}

.hero-title {
  font-size: 3.5rem;
  font-weight: 800;
  color: #1e3a8a;
  line-height: 1.1;
}

.hero-subtitle {
  font-size: 1.125rem;
  color: #6b7280;
  max-width: 40rem;
  margin: 1rem auto;
}

.hero-buttons {
  display: flex;
  justify-content: center;
  gap: 1rem;
  margin-top: 2rem;
}

.primary-btn {
  background-color: #6366f1;
  color: white;
  padding: 0.75rem 1.5rem;
  border: none;
  border-radius: 0.375rem;
  cursor: pointer;
}

.secondary-btn {
  background-color: white;
  color: #6366f1;
  padding: 0.75rem 1.5rem;
  border: 1px solid #6366f1;
  border-radius: 0.375rem;
  cursor: pointer;
}

.stats {
  display: flex;
  justify-content: center;
  gap: 4rem;
  padding: 2rem 0;
  background: linear-gradient(to bottom, #f0f9ff, white);
  text-align: center;
}

.stat-item h2 {
  font-size: 2.25rem;
  font-weight: 700;
  color: #1e3a8a;
}

.stat-item p {
  color: #6b7280;
}

.stat-icon {
  width: 4rem;
  height: 4rem;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 1.5rem;
  margin: 0 auto 1rem;
}

.lightbulb {
  background-color: #dbeafe;
  color: #3b82f6;
}

.people {
  background-color: #f3e8ff;
  color: #a855f7;
}

.funded {
  background-color: #dcfce7;
  color: #22c55e;
}

.features {
  display: flex;
  justify-content: center;
  gap: 2rem;
  padding: 4rem;
  background-color: white;
}

.feature-card {
  background-color: #f9fafb;
  padding: 1.5rem;
  border-radius: 1rem;
  max-width: 20rem;
  text-align: center;
}

.feature-icon {
  width: 3rem;
  height: 3rem;
  border-radius: 0.5rem;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 1.5rem;
  color: white;
  margin: 0 auto 1rem;
  font-weight: bold;
}

.funding {
  background-color: #f97316;
}

.communication {
  background-color: #a855f7;
}

.secure {
  background-color: #3b82f6;
}

.feature-card h3 {
  font-size: 1.25rem;
  font-weight: 600;
  color: #1e3a8a;
}

.feature-card p {
  color: #6b7280;
  font-size: 0.875rem;
}

.how-it-works {
  text-align: center;
  padding: 4rem 0;
  background-color: #f0f9ff;
}

.how-it-works h2 {
  font-size: 2.25rem;
  font-weight: 700;
  color: #1e3a8a;
}

.subtitle {
  color: #6b7280;
  max-width: 40rem;
  margin: 1rem auto;
}

.steps-container {
  position: relative;
  margin-top: 4rem;
}

.steps-line {
  position: absolute;
  top: 2.5rem;
  left: 10%;
  width: 80%;
  height: 0.25rem;
  background: linear-gradient(to right, #3b82f6, #a855f7, #22c55e, #f97316);
  border-radius: 9999px;
}

.steps {
  display: flex;
  justify-content: space-between;
  max-width: 80%;
  margin: 0 auto;
  gap: 1rem;
}

.step {
  background-color: white;
  padding: 1.5rem;
  border-radius: 1rem;
  text-align: left;
  width: 24%;
  position: relative;
}

.step-number {
  position: absolute;
  top: -2.5rem;
  left: calc(50% - 1.25rem);
  width: 2.5rem;
  height: 2.5rem;
  border-radius: 50%;
  background-color: #a855f7;
  color: white;
  display: flex;
  align-items: center;
  justify-content: center;
  font-weight: bold;
}

.step-icon {
  width: 3rem;
  height: 3rem;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 1.5rem;
  color: white;
  margin-bottom: 1rem;
  font-weight: bold;
}

.blue {
  background-color: #3b82f6;
}

.purple {
  background-color: #a855f7;
}

.green {
  background-color: #22c55e;
}

.orange {
  background-color: #f97316;
}

.step-label {
  font-size: 0.75rem;
  font-weight: 600;
  padding: 0.25rem 0.75rem;
  border-radius: 9999px;
  margin-bottom: 1rem;
  display: inline-block;
}

.ideators {
  background-color: #dbeafe;
  color: #3b82f6;
}

.everyone {
  background-color: #f3e8ff;
  color: #a855f7;
}

.teams {
  background-color: #dcfce7;
  color: #22c55e;
}

.success {
  background-color: #ffedd5;
  color: #f97316;
}

.step h3 {
  font-size: 1.25rem;
  font-weight: 600;
  color: #1e3a8a;
}

.step p {
  color: #6b7280;
  font-size: 0.875rem;
}

.everything {
  text-align: center;
  padding: 4rem 0;
  background-color: white;
}

.everything h2 {
  font-size: 2.25rem;
  font-weight: 700;
  color: #1e3a8a;
}

.grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 2rem;
  max-width: 80%;
  margin: 4rem auto;
}

.role {
  background-color: #3b82f6;
}

.smart {
  background-color: #a855f7;
}

.matching {
  background-color: #22c55e;
}

.footer {
  background-color: #1e3a8a;
  color: white;
  padding: 4rem;
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
}

.footer-logo {
  font-size: 1.5rem;
  font-weight: 700;
}

.footer-desc {
  max-width: 20rem;
  font-size: 0.875rem;
  margin-top: 1rem;
}

.footer-links {
  display: flex;
  gap: 4rem;
}

.link-group h4 {
  font-size: 1rem;
  font-weight: 600;
  margin-bottom: 1rem;
}

.link-group a {
  display: block;
  color: white;
  text-decoration: none;
  font-size: 0.875rem;
  margin-bottom: 0.5rem;
}

/* Enhanced scroll animations */
.section-animate {
  opacity: 0;
  transition: opacity 0.5s ease-out;
}

.section-animate.visible {
  opacity: 1;
}

.section-animate .animate-child {
  opacity: 0;
  transform: translateY(60px) scale(0.95);
  filter: blur(4px);
  transition: opacity 1s ease-out, transform 1s ease-out, filter 1s ease-out;
  transition-delay: calc(0.2s * (var(--child-index) - 1));
}

.section-animate.visible .animate-child {
  opacity: 1;
  transform: translateY(0) scale(1);
  filter: blur(0);
}

/* Smooth scrolling */
html {
  scroll-behavior: smooth;
}
</style>