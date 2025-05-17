// Lazy load index posts when placeholder is near viewport

function loadIndexPosts() {
  const placeholder = document.getElementById('index-posts-placeholder');
  const template = document.getElementById('index-posts-template');
  if (!placeholder || !template) return;
  const content = template.content.cloneNode(true);
  placeholder.replaceWith(content);
}

window.addEventListener('DOMContentLoaded', () => {
  const placeholder = document.getElementById('index-posts-placeholder');
  const template = document.getElementById('index-posts-template');
  if (!placeholder || !template) return;

  if ('IntersectionObserver' in window) {
    const observer = new IntersectionObserver((entries, obs) => {
      if (entries.some(e => e.isIntersecting)) {
        loadIndexPosts();
        obs.disconnect();
      }
    }, { rootMargin: '200px 0px' });
    observer.observe(placeholder);
  } else {
    loadIndexPosts();
  }
});
