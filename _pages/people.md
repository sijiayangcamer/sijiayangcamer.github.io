---
layout: page
permalink: /people/
title: people
description:
nav: true
nav_order: 2
---

<style>
.member-tabs {
  margin: 2rem 0;
  border-bottom: 2px solid #dee2e6;
}

.member-tabs .nav-item {
  margin-bottom: -2px;
}

.member-tabs .nav-link {
  border: none;
  border-bottom: 3px solid transparent;
  color: #6c757d;
  padding: 0.75rem 1.5rem;
  cursor: pointer;
  transition: all 0.3s ease;
}

.member-tabs .nav-link:hover {
  color: #495057;
  border-bottom-color: #dee2e6;
}

.member-tabs .nav-link.active {
  color: var(--global-theme-color);
  border-bottom-color: var(--global-theme-color);
  font-weight: 600;
}

.member-card-wrapper {
  display: none;
}

.member-card-wrapper.visible {
  display: block;
}

.member-card-wrapper.visible .member-card {
  display: flex;
}
</style>

<!-- Member Tabs -->
<ul class="nav member-tabs" role="tablist">
  <li class="nav-item" role="presentation">
    <a class="nav-link active" id="all-tab" data-category="all" role="tab" aria-controls="all" aria-selected="true">all</a>
  </li>
  <li class="nav-item" role="presentation">
    <a class="nav-link" id="graduate-tab" data-category="graduate" role="tab" aria-controls="graduate" aria-selected="false">graduate students</a>
  </li>
  <li class="nav-item" role="presentation">
    <a class="nav-link" id="undergraduate-tab" data-category="undergraduate" role="tab" aria-controls="undergraduate" aria-selected="false">undergraduate students</a>
  </li>
  <li class="nav-item" role="presentation">
    <a class="nav-link" id="alumni-tab" data-category="alumni" role="tab" aria-controls="alumni" aria-selected="false">alumni</a>
  </li>
</ul>

<div class="people-page">
  <div class="members-grid" id="members-container">
    {% if site.data.members.graduate_students %}
      {% for member in site.data.members.graduate_students %}
        <div class="member-card-wrapper" data-member-type="graduate" data-member-name="{{ member.name }}">
          {% if member.publications %}
            {% include member_card.liquid member=member type="graduate" publications=member.publications %}
          {% else %}
            {% include member_card.liquid member=member type="graduate" %}
          {% endif %}
        </div>
      {% endfor %}
    {% endif %}

    {% if site.data.members.undergraduate_students %}
      {% for member in site.data.members.undergraduate_students %}
        <div class="member-card-wrapper" data-member-type="undergraduate" data-member-name="{{ member.name }}">
          {% if member.publications %}
            {% include member_card.liquid member=member type="undergraduate" publications=member.publications %}
          {% else %}
            {% include member_card.liquid member=member type="undergraduate" %}
          {% endif %}
        </div>
      {% endfor %}
    {% endif %}

    {% if site.data.members.alumni %}
      {% for member in site.data.members.alumni %}
        <div class="member-card-wrapper" data-member-type="alumni" data-member-name="{{ member.name }}">
          {% if member.publications %}
            {% include member_card.liquid member=member type="alumni" publications=member.publications %}
          {% else %}
            {% include member_card.liquid member=member type="alumni" %}
          {% endif %}
        </div>
      {% endfor %}
    {% endif %}
  </div>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  const tabs = document.querySelectorAll('.member-tabs .nav-link');
  const memberWrappers = document.querySelectorAll('.member-card-wrapper');

  // Fisher-Yates shuffle algorithm for randomization
  function shuffleArray(array) {
    const shuffled = [...array];
    for (let i = shuffled.length - 1; i > 0; i--) {
      const j = Math.floor(Math.random() * (i + 1));
      [shuffled[i], shuffled[j]] = [shuffled[j], shuffled[i]];
    }
    return shuffled;
  }

  // Function to randomize and display members
  function randomizeAndDisplayMembers(category) {
    // Get all wrappers for this category
    const wrappersArray = Array.from(memberWrappers);
    const container = document.getElementById('members-container');

    // Filter wrappers by category
    const filteredWrappers = wrappersArray.filter(wrapper => {
      const memberType = wrapper.getAttribute('data-member-type');
      return category === 'all' || memberType === category;
    });

    // Randomize order using Fisher-Yates shuffle
    const randomizedWrappers = shuffleArray(filteredWrappers);

    // Hide all wrappers first
    memberWrappers.forEach(wrapper => wrapper.classList.remove('visible'));

    // Show and reorder randomized wrappers
    randomizedWrappers.forEach(wrapper => {
      wrapper.classList.add('visible');
      container.appendChild(wrapper);
    });
  }

  // Handle expand/collapse publications
  function setupPublicationExpanders() {
    const expandButtons = document.querySelectorAll('.expand-pubs-btn');

    expandButtons.forEach(button => {
      button.addEventListener('click', function(e) {
        e.preventDefault();

        const memberId = this.getAttribute('data-member-id');
        const pubSection = this.closest('.member-publications');
        const hiddenPubs = pubSection.querySelectorAll('.pub-item-hidden');
        const expandText = this.querySelector('.expand-text');
        const collapseText = this.querySelector('.collapse-text');
        const isExpanded = this.classList.contains('expanded');

        if (isExpanded) {
          // Collapse
          hiddenPubs.forEach(pub => {
            pub.style.display = 'none';
          });
          expandText.style.display = 'inline';
          collapseText.style.display = 'none';
          this.classList.remove('expanded');
        } else {
          // Expand
          hiddenPubs.forEach(pub => {
            pub.style.display = 'flex';
          });
          expandText.style.display = 'none';
          collapseText.style.display = 'inline';
          this.classList.add('expanded');
        }
      });
    });
  }

  // Initially show all members in random order
  randomizeAndDisplayMembers('all');

  // Setup publication expanders
  setupPublicationExpanders();

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

      // Randomize and display members
      randomizeAndDisplayMembers(category);

      // Re-setup publication expanders after DOM changes
      setTimeout(() => {
        setupPublicationExpanders();
      }, 100);
    });
  });
});
</script>
