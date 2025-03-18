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
};
