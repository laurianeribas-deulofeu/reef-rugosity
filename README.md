
<h1>Data from: Portraying Gradients of Structural Complexity in Coral Reefs Using Fine-Scale Depth Profiles</h1>
<em>Lauriane Ribas-Deulofeu^1,2,3†^, Pierre-Alexandre Château4, Vianney Denis5 and Chaolun Allen Chen1,2,3,6 *</em>

1Biodiversity Research Center, Academia Sinica, Taipei, Taiwan,<br>
2Taiwan International Graduate Program-Biodiversity, Academia Sinica, Taipei, Taiwan,<br>
3Department of Life Science, National Taiwan Normal University, Taipei, Taiwan,<br>
4Department of Marine Environment and Engineering, National Sun Yat-sen University, Kaohsiung, Taiwan,<br>
5Institute of Oceanography, National Taiwan University, Taipei, Taiwan,<br>
6Department of Life Science, Tunghai University, Taichung, Taiwan<br>
<hr>

<h2><strong><em>Overview</strong></em></h2>
<p>This repository contains the dataset and Python program used in the study published in Frontiers in Marine Science titled "Portraying Gradients of Structural Complexity in Coral Reefs Using Fine-Scale Depth Profiles." The research focuses on estimating reef structural complexity through the analysis of fine and coarse scales of rugosity using high-resolution depth profiles.</p><br>

<p><strong>Files in the repository</strong><br>
<strong> 1. Supplementary Files 1 A & B | Python program—rugosity calculations</strong><br>
    - Python script for rugosity calculations based on the proposed method <br>
		A. Python Program - Rugosity calculations (theoretical transects)<br>
		B. Python Program - Rugosity calculations (in situ transects)<br>

<strong>2. Supplementary File - Data Sheet 2 | Depth profiles of the nine theoretical transects</strong><br>
    - Data file containing depth profiles of nine theoretical transects.<br>

<strong>3. Supplementary File - Data Sheet 3 | Depth profiles of the 50 in situ transects</strong>
    - Data file containing depth profiles of the 50 in situ transects collected in South Taiwan.<br>

<h2><strong><em>Field Survey</strong></em></h2>
Fifty field transects were surveyed at 10 locations in Kenting National Park (KNP), South Taiwan. Transects were positioned around 5 m in depth, with a minimum depth of 1.8 m and a maximum of 10.1 m. Fine resolution depth profiles were recorded following the method proposed by Dustan et al. (2013). Pressure data were collected using a titanium HOBO water level logger, and depth profiles were obtained by converting pressure data using the formula recommended by Fofonoff and Millard (1983).<br>

<h2><strong><em> Rugosity estimations methodology</strong></em></h2>
<strong><em>Rugosity Estimations</strong></em><br>
Our calculations (Files S1 A & B) used the roughness index Rq, representing the Root Mean Squared deviation from the assessed surface profile. To discriminate between the contributions of fine and coarse scales of rugosity on the total rugosity profile, we adapted the Rq index (Equation 1) with polynomial functions, as follows:<br>
R_q=√(1/l ∑_(i=1)^n▒〖m×(〖depth〗_i-〖poly〗_i)〗^2 )  (Equation 1) <br>
with l=transect length; and m=l/n; in this study, l=20 m<br>

<strong><em>Virtual Chain Index</strong></em><br>
To compare our method with commonly used rugosity methods, we computed the expected rugosity of our transects with the chain method. Our “virtual chain index” (Equation 2) was calculated as follows:<br>
Virtual chain index=1/l ∑_(i=1)^n▒〖 √((〖depth〗_i-〖depth〗_(i-1) )^2+〖m 〗^2 )  (Equation 2) 〗 <br>
with virtual chain link size corresponding to the depth profile resolution of the transects, since m=l/n<br>

<h2><strong><em>Citation</strong></em></h2>
If you find this dataset or methodology useful, please cite the associated paper:<br>
Ribas-Deulofeu L, Château P-A, Denis V and Chen CA (2021) Portraying Gradients of Structural Complexity in Coral Reefs Using Fine-Scale Depth Profiles. Front. Mar. Sci. 8:675853.  <a href="doi: 10.3389/fmars.2021.675853" target="_blank">https://www.frontiersin.org/articles/10.3389/fmars.2021.675853/full</a>.<br>

<h2><strong><em>License</strong></em></h2>
This dataset and Python program are available under the Creative Commons Attribution License (CCBY). The use, distribution, or reproduction in other forums is permitted, provided the original authors and that the original publication is cited, per accepted academic practice.<br>

<h2><strong><em>References</strong></em></h2>
Dustan, P., Doherty, O., and Pardede, S. (2013). Digital Reef Rugosity Estimates Coral Reef Habitat Complexity. PLoS One 8, e57386.  <a href="doi:10.1371/journal.pone.0057386" target="_blank">[https://doi.org/your-doi-number](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0057386)</a>.<br>
Fofonoff, N. P., and Millard, R. C. (1983). Algorithms for computation of fundamental properties of seawater. UNESCO Available at: https://development.oceanbestpractices.net/handle/11329/109 [Accessed October 14, 2019].<br>
Ribas-Deulofeu L, Château P-A, Denis V and Chen CA (2021) Portraying Gradients of Structural Complexity in Coral Reefs Using Fine-Scale Depth Profiles. Front. Mar. Sci. 8:675853.  <a href="https://www.frontiersin.org/articles/10.3389/fmars.2021.675853/full" target="_blank">doi: 10.3389/fmars.2021.675853</a>.<br>
</p>
