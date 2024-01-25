window.onload = function() {
    // Check if the Twitter widgets script is loaded
    if (typeof twttr !== 'undefined') {
      twttr.widgets.load(
        document.getElementById("twitter-feed")
      );
      twttr.events.bind('loaded', function (event) {
        // Find all twitter tweets and show them
        var tweets = document.querySelectorAll('.twitter-tweet');
        tweets.forEach(function(tweet) {
          tweet.classList.add('twitter-tweet-loaded');
        });
      });
    }
};
