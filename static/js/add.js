		var taglines = [
			'Free themes for <a target="_blank" href="http://twitter.github.com/bootstrap/">Twitter Bootstrap</a>',
			'Add color to your <a target="_blank" href="http://twitter.github.com/bootstrap/">Bootstrap</a> site without touching a color picker',
			'Saving the web from default <a target="_blank" href="http://twitter.github.com/bootstrap/">Bootstrap</a>'
		];

		var line = Math.floor((taglines.length) * Math.random());
		$('#tagline').html(taglines[line]);

		parseRSS('http://feeds.feedburner.com/bootswatch', function(d){
			var h ='<strong>Recent news:</strong> ';
			for (var i = 0; i < 3; i++){
				h = h + '<a href="' + d.entries[i].link + '" onclick="pageTracker._link(this.href); return false;">' + d.entries[i].title + '...</a>&nbsp;&nbsp;';
			}
			document.getElementById('ticker').innerHTML = h;
		})

		function parseRSS(url, callback) {
		  $.ajax({
		    url: 'http://ajax.googleapis.com/ajax/services/feed/load?v=1.0&num=10&callback=?&q=' + encodeURIComponent(url),
		    dataType: 'json',
		    success: function(data) {
		      callback(data.responseData.feed);
		    }
		  });
		}
		
			<script type="text/javascript">

		var _gaq = _gaq || [];
		_gaq.push(['_setAccount', 'UA-23019901-1']);
		_gaq.push(['_setDomainName', "bootswatch.com"]);
		_gaq.push(['_setAllowLinker', true]);
		_gaq.push(['_trackPageview']);

		(function() {
			var ga = document.createElement('script'); ga.type = 'text/javascript'; ga.async = true;
			ga.src = ('https:' == document.location.protocol ? 'https://ssl' : 'http://www') + '.google-analytics.com/ga.js';
			var s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(ga, s);
		})();

!function(d,s,id){var js,fjs=d.getElementsByTagName(s)[0];if(!d.getElementById(id)){js=d.createElement(s);js.id=id;js.src="//platform.twitter.com/widgets.js";fjs.parentNode.insertBefore(js,fjs);}}(document,"script","twitter-wjs");
