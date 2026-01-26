---
layout: page
permalink: /projects/
title: projects
description: Browse projects by research area
nav: true
nav_order: 3
---

<!-- _pages/projects.md -->

<style>
.category-tabs {
  margin: 2rem 0;
  border-bottom: 2px solid #dee2e6;
}

.category-tabs .nav-item {
  margin-bottom: -2px;
}

.category-tabs .nav-link {
  border: none;
  border-bottom: 3px solid transparent;
  color: #6c757d;
  padding: 0.75rem 1.5rem;
  cursor: pointer;
  transition: all 0.3s ease;
}

.category-tabs .nav-link:hover {
  color: #495057;
  border-bottom-color: #dee2e6;
}

.category-tabs .nav-link.active {
  color: var(--global-theme-color);
  border-bottom-color: var(--global-theme-color);
  font-weight: 600;
}

.category-description {
  border-left: 3px solid #17a2b8;
  padding-left: 1rem;
  margin: 1.5rem 0 2rem 0;
  display: none;
}

.category-description.active {
  display: block;
}

.category-description p {
  margin: 0;
  font-style: italic;
  font-size: 0.95rem;
  opacity: 0.85;
  line-height: 1.5;
}

.projects-placeholder {
  text-align: center;
  padding: 3rem 2rem;
  color: var(--global-text-color-light);
}

.projects-placeholder h3 {
  margin-bottom: 1rem;
  color: var(--global-text-color);
}
</style>

<!-- Category Tabs -->
<ul class="nav category-tabs" role="tablist">
  <li class="nav-item" role="presentation">
    <a class="nav-link active" id="all-tab" data-category="all" role="tab" aria-controls="all" aria-selected="true">All</a>
  </li>
  <li class="nav-item" role="presentation">
    <a class="nav-link" id="morality-tab" data-category="morality" role="tab" aria-controls="morality" aria-selected="false">Communication of Morality</a>
  </li>
  <li class="nav-item" role="presentation">
    <a class="nav-link" id="artificial-tab" data-category="artificial" role="tab" aria-controls="artificial" aria-selected="false">Artificial Influence</a>
  </li>
  <li class="nav-item" role="presentation">
    <a class="nav-link" id="translational-tab" data-category="translational" role="tab" aria-controls="translational" aria-selected="false">Translational Communication Interventions</a>
  </li>
</ul>

<!-- Category Descriptions -->
<div class="category-description active" id="desc-all">
  <p>Browse all projects across all research areas.</p>
</div>

<div class="category-description" id="desc-morality">
  <p>Projects examining how moral appeals circulate through media, shape persuasion, and moralize attitudes and public discourse.</p>
</div>

<div class="category-description" id="desc-artificial">
  <p>Projects exploring how algorithms and generative AI produce intentional and emergent influence in communication systems.</p>
</div>

<div class="category-description" id="desc-translational">
  <p>Projects designing and evaluating communication interventions that translate theory into real-world public-interest impact.</p>
</div>

<div class="projects-content">
  <div class="projects-placeholder">
    <h3>Projects Coming Soon</h3>
    <p>This page will feature detailed project descriptions organized by research area.</p>
  </div>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  const tabs = document.querySelectorAll('.category-tabs .nav-link');

  // Function to activate a specific tab
  function activateTab(tabId) {
    const targetTab = document.getElementById(tabId);
    if (targetTab) {
      targetTab.click();
    }
  }

  // Tab click handlers
  tabs.forEach(tab => {
    tab.addEventListener('click', function(e) {
      e.preventDefault();

      const category = this.getAttribute('data-category');

      // Update active tab
      tabs.forEach(t => {
        t.classList.remove('active');
        t.setAttribute('aria-selected', 'false');
      });
      this.classList.add('active');
      this.setAttribute('aria-selected', 'true');

      // Update active description
      document.querySelectorAll('.category-description').forEach(desc => {
        desc.classList.remove('active');
      });
      document.getElementById('desc-' + category).classList.add('active');
    });
  });

  // Check for hash in URL on page load
  if (window.location.hash) {
    const hash = window.location.hash.substring(1); // Remove the # symbol
    activateTab(hash);
  }

  // Listen for hash changes
  window.addEventListener('hashchange', function() {
    if (window.location.hash) {
      const hash = window.location.hash.substring(1);
      activateTab(hash);
    }
  });
});
</script>
