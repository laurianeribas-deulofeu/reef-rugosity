
<h1>Data from: Portraying gradients of structural complexity in coral reefs using fine-scale depth profiles</h1>
<em>Lauriane Ribas-Deulofeu<sup>1,2,3†</sup>, Pierre-Alexandre Château<sup>4</sup>, Vianney Denis<sup>5</sup> and Chaolun Allen Chen<sup>1,2,3,6</sup>*</em>

<sup>1</sup>Biodiversity Research Center, Academia Sinica, Taipei, Taiwan,<br>
<sup>2</sup>Taiwan International Graduate Program-Biodiversity, Academia Sinica, Taipei, Taiwan,<br>
<sup>3</sup>Department of Life Science, National Taiwan Normal University, Taipei, Taiwan,<br>
<sup>4</sup>Department of Marine Environment and Engineering, National Sun Yat-sen University, Kaohsiung, Taiwan,<br>
<sup>5</sup>Institute of Oceanography, National Taiwan University, Taipei, Taiwan,<br>
<sup>6</sup>Department of Life Science, Tunghai University, Taichung, Taiwan<br>
<hr>

<h2><strong><em>Overview</strong></em></h2>
<p>This repository contains the dataset and Python program used in the study published in Frontiers in Marine Science titled "Portraying Gradients of Structural Complexity in Coral Reefs Using Fine-Scale Depth Profiles." The research focuses on estimating reef structural complexity through the analysis of fine and coarse scales of rugosity using high-resolution depth profiles.</p><br>

<h2><strong><em>Files in the repository</strong></em></h2>
<strong> 1. Supplementary Files 1 A & B | Python program—rugosity calculations</strong>
   <blockquote> - Python script for rugosity calculations based on the proposed method </blockquote>
		<blockquote><blockquote>A. Python Program - Rugosity calculations (theoretical transects)</blockquote></blockquote>
		<blockquote><blockquote>B. Python Program - Rugosity calculations (in situ transects)</blockquote></blockquote>

<strong>2. Supplementary File - Data Sheet 2 | Depth profiles of the nine theoretical transects</strong>
    <blockquote> - Data file containing depth profiles of nine theoretical transects. </blockquote>

<strong>3. Supplementary File - Data Sheet 3 | Depth profiles of the 50 in situ transects</strong>
    <blockquote> - Data file containing depth profiles of the 50 in situ transects collected in South Taiwan. </blockquote>

<h2><strong><em>Field Survey</strong></em></h2>
Fifty field transects were surveyed at 10 locations in Kenting National Park (KNP), South Taiwan. Transects were positioned around 5 m in depth, with a minimum depth of 1.8 m and a maximum of 10.1 m. Fine resolution depth profiles were recorded following the method proposed by Dustan et al. (2013). Pressure data were collected using a titanium HOBO water level logger, and depth profiles were obtained by converting pressure data using the formula recommended by Fofonoff and Millard (1983).<br>

<h2><strong><em> Rugosity estimations methodology</strong></em></h2>
<strong><em>Rugosity Estimations</strong></em><br>
Our calculations (Files S1 A & B) used the roughness index Rq, representing the Root Mean Squared deviation from the assessed surface profile. To discriminate between the contributions of fine and coarse scales of rugosity on the total rugosity profile, we adapted the Rq index (Equation 1) with polynomial functions, as follows:<br>
<p>
    R<sub>q</sub> = &radic;<span style="text-decoration: overline">(1/l &sum;<sub>i=1</sub><sup>n</sup> (m&times;(depth<sub>i</sub> - poly<sub>i</sub>)<sup>2</sup>)</span>       
	<em> (Equation 1)</em>, <br> with l = transect length; and m = l/n; in this study, l = 20 m
</p>

<strong><em>Virtual Chain Index</strong></em><br>
To compare our method with commonly used rugosity methods, we computed the expected rugosity of our transects with the chain method. Our “virtual chain index” (Equation 2) was calculated as follows:<br>
<p>
    Virtual chain index = 1/l &sum;<sub>i=1</sub><sup>n</sup> &radic;((depth<sub>i</sub> - depth<sub>(i-1)</sub>)<sup>2</sup> + m<sup>2</sup>)
         <em>(Equation 2)</em>, <br> with virtual chain link size corresponding to the depth profile resolution of the transects, since m = l/n
</p>

<h2><strong><em>Citation</strong></em></h2>
If you find this dataset or methodology useful, please cite the associated paper:<br>
Ribas-Deulofeu L, Château P-A, Denis V and Chen CA (2021) Portraying Gradients of Structural Complexity in Coral Reefs Using Fine-Scale Depth Profiles. Front. Mar. Sci. 8:675853.  <a href="https://www.frontiersin.org/articles/10.3389/fmars.2021.675853/full" target="_blank">doi: 10.3389/fmars.2021.675853</a>.<br>

<h2><strong><em>License</strong></em></h2>
This dataset and Python program are available under the Creative Commons Attribution License (CCBY). The use, distribution, or reproduction in other forums is permitted, provided the original authors and that the original publication is cited, per accepted academic practice.<br>

<h2><strong><em>References</strong></em></h2>
Dustan, P., Doherty, O., and Pardede, S. (2013). Digital Reef Rugosity Estimates Coral Reef Habitat Complexity. PLoS One 8, e57386.  <a href="https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0057386)" target="_blank">doi:10.1371/journal.pone.0057386</a>.<br>
Fofonoff, N. P., and Millard, R. C. (1983). Algorithms for computation of fundamental properties of seawater. UNESCO Available at: https://development.oceanbestpractices.net/handle/11329/109 [Accessed October 14, 2019].<br>
Ribas-Deulofeu L, Château P-A, Denis V and Chen CA (2021) Portraying Gradients of Structural Complexity in Coral Reefs Using Fine-Scale Depth Profiles. Front. Mar. Sci. 8:675853.  <a href="https://www.frontiersin.org/articles/10.3389/fmars.2021.675853/full" target="_blank">doi: 10.3389/fmars.2021.675853</a>.<br>
</p>
