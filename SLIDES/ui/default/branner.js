// David Prager Branner
// 20140215

// Different settings for JS and CSS if running locally or on web.
var currentURL = window.location.href;
if (currentURL.search(/http/) === 0) {
  // Don't use htmlpreview.github.io here; displays markdown, not HTML.
  var urlPrefix = "https://github.com/brannerchinese/Gauge_Voice_Transcription/blob/master/SLIDES/";
  var whereWeAre = "via HTTP.";
}
else {
  var urlPrefix = "";
  var whereWeAre = "from the filesystem.";
}
