---
layout: page
permalink: /publications/
title: publications
description: Browse publications by research area
nav: true
nav_order: 4
---

<!-- _pages/publications.md -->

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

.publication-entry {
  display: none;
}

.publication-entry.visible {
  display: block;
}

/* Hide empty year headers */
.bibliography h2.bibliography__year {
  display: none;
}

.bibliography h2.bibliography__year.has-visible-pubs {
  display: block;
}

/* Also handle year headers without specific class */
.publications h2 {
  display: none;
}

.publications h2.has-visible-pubs {
  display: block;
}

/* Hide the Abs button since abstracts are always shown */
.abstract.btn {
  display: none !important;
}
</style>

<!-- Category Tabs -->
<ul class="nav category-tabs" role="tablist">
  <li class="nav-item" role="presentation">
    <a class="nav-link active" id="all-tab" data-category="all" role="tab" aria-controls="all" aria-selected="true">all</a>
  </li>
  <li class="nav-item" role="presentation">
    <a class="nav-link" id="morality-tab" data-category="morality" role="tab" aria-controls="morality" aria-selected="false">communication of morality</a>
  </li>
  <li class="nav-item" role="presentation">
    <a class="nav-link" id="artificial-tab" data-category="artificial" role="tab" aria-controls="artificial" aria-selected="false">artificial influence</a>
  </li>
  <li class="nav-item" role="presentation">
    <a class="nav-link" id="translational-tab" data-category="translational" role="tab" aria-controls="translational" aria-selected="false">translational communication interventions</a>
  </li>
</ul>

<!-- Category Descriptions -->
<div class="category-description active" id="desc-all">
  <p>Browse all publications across all research areas.</p>
</div>

<div class="category-description" id="desc-morality">
  <p>How moral appeals circulate through media, shape persuasion, and moralize attitudes and public discourse.</p>
</div>

<div class="category-description" id="desc-artificial">
  <p>How algorithms and generative AI produce intentional and emergent influence in communication systems.</p>
</div>

<div class="category-description" id="desc-translational">
  <p>How to design and evaluate communication interventions that translate theory into real-world public-interest impact.</p>
</div>

<div class="publications">
{% bibliography %}
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  const tabs = document.querySelectorAll('.category-tabs .nav-link');
  const publications = document.querySelectorAll('.publications .bibliography li');

  // Function to activate a specific tab
  function activateTab(tabId) {
    const targetTab = document.getElementById(tabId);
    if (targetTab) {
      targetTab.click();
    }
  }

  // Function to update year header visibility
  function updateYearHeaders() {
    // Find all year headers (h2 elements in the publications area)
    const yearHeaders = document.querySelectorAll('.publications h2');

    yearHeaders.forEach(header => {
      // Find all li elements between this header and the next header
      let nextElement = header.nextElementSibling;
      let hasVisiblePubs = false;

      while (nextElement) {
        if (nextElement.tagName === 'H2') {
          // Reached next year header, stop
          break;
        }
        if (nextElement.tagName === 'OL' || nextElement.tagName === 'UL') {
          // Check if this list has visible items
          const visibleItems = nextElement.querySelectorAll('li.visible');
          if (visibleItems.length > 0) {
            hasVisiblePubs = true;
            break;
          }
        }
        if (nextElement.tagName === 'LI' && nextElement.classList.contains('visible')) {
          hasVisiblePubs = true;
          break;
        }
        nextElement = nextElement.nextElementSibling;
      }

      if (hasVisiblePubs) {
        header.classList.add('has-visible-pubs');
      } else {
        header.classList.remove('has-visible-pubs');
      }
    });
  }

  // Add category classes to publications based on data attribute
  publications.forEach(pub => {
    const bibEntry = pub.querySelector('.row[data-category]');
    if (bibEntry) {
      // Get category from the row element inside the li
      const categoryAttr = bibEntry.getAttribute('data-category');
      pub.classList.add('publication-entry');
      if (categoryAttr) {
        pub.setAttribute('data-pub-category', categoryAttr);
      }
    } else {
      // No category attribute means it's a book chapter or other entry
      // Should appear in "All" but not in specific categories
      pub.classList.add('publication-entry');
    }
  });

  // Initially show all publications
  publications.forEach(pub => pub.classList.add('visible'));

  // Update year headers after a brief delay to ensure DOM is ready
  setTimeout(updateYearHeaders, 100);

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

      // Filter publications
      publications.forEach(pub => {
        const pubCategory = pub.getAttribute('data-pub-category');
        if (category === 'all') {
          pub.classList.add('visible');
        } else if (pubCategory === category) {
          pub.classList.add('visible');
        } else {
          pub.classList.remove('visible');
        }
      });

      // Update year header visibility after filtering
      updateYearHeaders();
    });
  });

  // Check for hash in URL on page load
  if (window.location.hash) {
    const hash = window.location.hash.substring(1); // Remove the # symbol
    activateTab(hash);
  }

  // Listen for hash changes (e.g., when user clicks back/forward)
  window.addEventListener('hashchange', function() {
    if (window.location.hash) {
      const hash = window.location.hash.substring(1);
      activateTab(hash);
    }
  });
});
</script>
