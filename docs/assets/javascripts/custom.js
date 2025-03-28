window.onload = function() {
    // Hide the loading message when tweets are loaded
    var hideLoadingMessage = function() {
        var loadingMessage = document.getElementById('loadingMessage');
        if (loadingMessage) {
            loadingMessage.style.display = 'none';
        }
    };

    // Check if the Twitter widgets script is loaded
    if (typeof twttr !== 'undefined') {
        twttr.widgets.load(
            document.getElementById("twitter-feed")
        );
        twttr.events.bind('loaded', function (event) {
            // Hide loading message
            hideLoadingMessage();

            // Find all twitter tweets and show them
            var tweets = document.querySelectorAll('.twitter-tweet');
            tweets.forEach(function(tweet) {
                tweet.classList.add('twitter-tweet-loaded');
            });

            // Unhide the twitter feed
            var loadingMessage = document.getElementById('twitter-feed');
            if (loadingMessage) {
                loadingMessage.style.display = 'block';
            }
        });
    } else {
        var loadingMessage = document.getElementById('twitter-feed');
        if (loadingMessage) {
            loadingMessage.style.display = 'none';
        }
    }

    // New Twitter navigation code
    const initTwitterNavigation = () => {
        const twitterPosts = document.querySelector('.twitter-posts');
        const prevButton = document.querySelector('.twitter-nav-prev');
        const nextButton = document.querySelector('.twitter-nav-next');
        
        if (twitterPosts && prevButton && nextButton) {
            const tweetWidth = 300; // Width of each tweet
            const scrollAmount = tweetWidth + 16; // Width + gap
            
            prevButton.addEventListener('click', () => {
                twitterPosts.scrollBy({
                    left: -scrollAmount,
                    behavior: 'smooth'
                });
            });
            
            nextButton.addEventListener('click', () => {
                twitterPosts.scrollBy({
                    left: scrollAmount,
                    behavior: 'smooth'
                });
            });
        }
    };

    // Initialize after a short delay to ensure tweets are loaded
    setTimeout(initTwitterNavigation, 200);
};
