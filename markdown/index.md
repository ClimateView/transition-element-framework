---
hide: navigation
---

<style>
body {
    background-color: #F9F9F9;
}
</style>

<h1 style="display:none;">Home</h1>


<div class="full-width-container" markdown>
<figure class="video_container">
  <video id="myVideo"  poster="/images/placeholder_film.svg">
    <source src="/images/OSI_Film_Final_V004-2.mp4" type="video/mp4">
  </video>
</figure>
</div>
<script>
  const video = document.getElementById('myVideo');
  var played = false;
  
  // Hide controls initially
  video.controls = false;

// Show controls and play video when the video is clicked 
video.addEventListener('click', function() { 
  if (!played || video.paused) {
setTimeout(() => {
   video.play(); 
}, "100");
  video.controls = true; 
  played = true;
}
});
</script>



<h2 class="cv-h1" >The Transition Element Framework™</h2>

An open-source initiative built on the foundation of IPCC climate mitigation strategies, the TEF transforms complex IPCC knowledge into a standardised, accessible framework. Already used by cities and governments worldwide, the TEF provides a shared language and transparent methodology for planning and measuring climate action, enabling cities to set KPIs and track real decarbonisation progress.   

With the TEF, cities can move beyond pledges to implement actionable, collaborative mitigation strategies.


<div class="grid cv-grid cards" markdown>

- __Get the backstory__{ .cv-inverted }
	![Introduction Card](/images/card_intro.png)  
	__Introduction__{ .cv-h4 }
	
	The Transition Element Framework builds on the IPCC's work by converting its critical knowledge into a practical platform to guide climate action from concept to implementation.
	
	[Read more](/introduction.md)



-    __Discover the knowledge__{ .cv-inverted }
	![Compendium Card](/images/card_compendium.png)  
	__Mitigation Compendium__{ .cv-h4 }

    The Mitigation Compendium is a curated collection of IPCC Mitigation Options. It makes essential IPCC knowledge accessible, laying the groundwork for informed action and analysis.

    [Explore Mitigation Compendium](/2-ipcc-mitigation-options/index.md)

-    __Reveal the building blocks__{ .cv-inverted }
	![Transition Elements Card](/images/card_te.png)  
	__Transition Elements__{ .cv-h4 }

	The Transition Elements serve as building blocks for climate action. Each element represents an IPCC Mitigation Option broken down into its essential parts.

    [Explore Transition Elements](/3-transition-elements/index.md)

</div>



## Updates  { .cv-h3 }

This platform is a work in progress. By sharing our progress early and openly, we invite the scientific and climate action community to help shape its development. We aim to create new possibilities for others to use, expand, and build upon the work we have started. [Join us](/5-resources/5-about/contact.md) in exploring how this framework can be a powerful tool for advancing climate strategies worldwide.


<div class="grid cards" markdown>

- __September 16, 2024__{ .cv-inverted }
	![News Whitepaper](/images/news_whitepaper.png)  
	[New white paper: Standardising Climate Mitigation](/4-whitepapers/whitepaper-standardising-climate-mitigation.md){ .cv-h4 }
	
	The Transition Element Framework (TEF) is a structured approach for organising and standardising IPCC Mitigation Options to support data-driven decision-making, scenario planning, and collaborative climate action. It extracts, organises, and gives a common language to all Mitigation Options.
	
	[Download white paper](/introduction.md)

-
</div>


<div class="cv-joinus">
<h3 class="cv-compact cv-h3">Join us</h3>
We aim to create new possibilities for others to use, expand, and build upon
the work we have started. Join us in exploring how this framework can be a
powerful tool for advancing climate strategies worldwide.

<p>📧 <a href="mailto:opensource@climateview.global">opensource@climateview.global</a></p>

</div>

<div class="cv-joinus">
<h3 class="cv-compact cv-h3">Open Source</h3>
The Transition Element Framework is an open-source work in progress. The website is currently being generated primarily by hand with some degree of automation from our model files on GitHub. We want to fully automate this process before opening up our GitHub repository for general access; in order to ensure that the repository is as usable as possible. Until then, our YAML model files can be found within each Activity and Transition Element description page. 

</div>


<br/>

<div class="cv-textbox" markdown>
The Transition Element Framework was developed by ClimateView and originated from a collaboration with the [Swedish Climate Policy Council](https://www.klimatpolitiskaradet.se/en/), the [Swedish Energy Agency](https://www.energimyndigheten.se/en/), and the [Swedish Environmental Protection Agency](https://www.naturvardsverket.se/en/). The TEF has been co-developed with cities worldwide, including the Ruhr region in Germany and, most recently, the Scottish Climate Intelligence Service (SCIS). Components of the TEF are being used in pursuit of a German Institute for Standardization (DIN) specification and, subsequently, a European Committee for Standardization (CEN) standard.
</div>

<br/>

