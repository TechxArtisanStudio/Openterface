/**
 * Social Media Posts Lazy Loading
 * Handles lazy loading for Twitter and Bluesky embeds
 */

document.addEventListener('DOMContentLoaded', function() {
    const socialPosts = document.querySelectorAll('.social-post-item[data-lazy="true"]');
    
    // Check if Intersection Observer is supported
    if (!('IntersectionObserver' in window)) {
        // Fallback: Load all posts immediately
        loadAllSocialPosts();
        return;
    }
    
    // Intersection Observer for lazy loading
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const postItem = entry.target;
                loadSocialPost(postItem);
                observer.unobserve(postItem);
            }
        });
    }, {
        rootMargin: '50px 0px',
        threshold: 0.1
    });
    
    // Observe all lazy posts
    socialPosts.forEach(post => {
        observer.observe(post);
    });
    
    // Fallback: Load all posts after 3 seconds if they haven't loaded yet
    setTimeout(() => {
        socialPosts.forEach(post => {
            if (post.classList.contains('loading')) {
                loadSocialPost(post);
            }
        });
    }, 3000);
    
    function loadSocialPost(postItem) {
        // Remove loading class and add loaded class
        postItem.classList.remove('loading');
        postItem.classList.add('loaded');
        
        // Trigger social media widget loading
        setTimeout(() => {
            // Twitter widgets
            if (typeof twttr !== 'undefined' && twttr.widgets) {
                twttr.widgets.load(postItem);
            }
            
            // Bluesky embeds
            if (typeof window.BlueskyEmbed !== 'undefined') {
                window.BlueskyEmbed.loadEmbeds();
            }
        }, 100);
    }
    
    function loadAllSocialPosts() {
        socialPosts.forEach(post => {
            loadSocialPost(post);
        });
    }
});
