# Retrieval Evaluation

This file is used for manually evaluating retrieval quality. For each question, inspect whether the retrieved chunks contain information that can answer the question.

## Grading Rubric

- **Good**: Top 1--3 chunks are clearly relevant and sufficient.
- **Medium**: Some relevant chunks are retrieved, but important context is missing or mixed with noise.
- **Bad**: Retrieved chunks are mostly irrelevant.

---

# Question 1

**Question:** What is the main contribution of this paper?

**Manual Grade:** Good / Medium / Bad

**Notes:** 

## Retrieved Chunks

### Top 1

- Source: `Release strategies and the social impacts of Language Models.pdf`
- Page: `2`
- Chunk ID: `747`

```text
time to adapt to a world in which it is prudent to mistrust everything they read a little more. In addi- tion to finding minimal evidence of misuse so far, several other factors contributed to our confidence in publishing our 774 million and 1.5 billion parameter models. These include what we learned about the positive social impact of beneficial uses, and what we learned through our partnerships among the AI community and through discussions across fields about establishing norms for responsible publica- tion. This report discusses OpenAI’s work related to staged release of large models, partnership-based research, and broader issues in responsible publication that the AI community will need to address. 1
```

### Top 2

- Source: `Detection of ChatGPT Fake Science with the xFakeSci Learning Algorithm.pdf`
- Page: `4`
- Chunk ID: `577`

```text
Alzheimer’s disease and co-morbidities 1196 Cancer and co-morbidities 1243 Depression 1513 Total number of generated articles 3952 The prompt-engineering process is computationally described in Algorithm 1. Although this process was done programmat- ically, due to the timeout limit, we executed it to produce 20 simulated articles at a time. This prompt-engineering approach enabled us to generate a large corpus of simulated articles that closely resembled real scientific publications in terms of structure, content, and overall style. This dataset played a crucial role in training the xFakeSci algorithm, enabling it to accurately distinguish between real scientific articles and machine-generated ones. Algorithm 1 The Computational Process of ChatGPT Prompt Engineering for Article Generation Require: diseases = [“Alzheimer’s”, “Cancer”, “Depression”] Require: article_number = 20. Require: a...
```

### Top 3

- Source: `Release strategies and the social impacts of Language Models.pdf`
- Page: `10`
- Chunk ID: `774`

```text
model is in use. In addition to this initial work, CTEC has plans to broaden their quantitative approach, to conduct an “in-depth qualitative linguistic analysis” on model outputs, and to run “a survey to observe the abilities for both extremism experts and non-experts to distinguish between real and fake extremist texts”. [See Appendix D for further results] 9
```

### Top 4

- Source: `ASurvey of AI-generated Text Forensic Systems Detection Attribution and Characterization.pdf`
- Page: `19`
- Chunk ID: `98`

```text
Research Paper Abstracts 600K (HW + MG) Acc 98%X Review, Polish, Re-vise, Rewrite andEdit the Title, Ab-stractAcademic Text(Liyanage andBuscaldi, 2023) GPT Academia DAGPap22, GPT Wiki Intro500-R and 500-MGF1-Score97.5% X first 7 words ofWiki Intro, first 50Words of Academicpaper or first sen-tence of AbstractMULTITuDE(Macko et al.,2023) Multilingual LLMs - GPT-3, GPT-4, LLaMA65B,ChatGPT, Alpaca-LoRa-30B, Vicuna-13B, OPT-66B, IML-Max-1.3B News MassiveSumm 11 languages- 74K (8K-HW,66K-MG) Acc 94.50% (En) ✓ Titles of selected ar-ticles To ChatGPT (Pego-raro et al., 2023)ChatGPT Medical, Open QA,Finance User-generated responses frompopular Social Networking Plat-forms 131K (58k HW, 72K MG)TPR% (De-tection Capa-bility) Detects 90% as HWX Inquiry prompts H3Plus (Su et al.,2023e) ChatGPT News CNN,DailyMail, Xsum, LCSTS,News2016, WMT210K (42K-Chinese, 95K-EnTrain samples) Acc 99.5% En, 98.65%Chi...
```

### Top 5

- Source: `GLTR Statistical Detection and Visualization of Generated Text.pdf`
- Page: `4`
- Chunk ID: `731`

```text
above random chance. While only 40% of texts were real, they trusted 56.0% of texts, Heliograf at a higher rate than GPT-2 (68.6% vs. 51.4%, p < 0.01). The difﬁculty of the task without over- lay was rated at 3.89 on a 5-point Likert scale, further supporting the need for assistive systems. With the interface, the performance improved to 72.3%. The average treatment effect shows an im- provement of 18.1% with p < 0.001, even af- ter controlling for whether a participant is a na- tive speaker and how difﬁcult they rated the task. 42.1% of the participants stated that the interface helped them be more accurate, and 37.1% found that it helped them to identify fakes faster. Qualitative Findings The tool caused students to think about the properties of the fake text. While humans would vary expressions in real texts, models rarely generate synonyms or refer- ring expressions for entities, whi...
```

---

# Question 2

**Question:** What problem does this paper study?

**Manual Grade:** Good / Medium / Bad

**Notes:** 

## Retrieved Chunks

### Top 1

- Source: `ASurvey onLLM-Generated Text Detection Necessity, Methods, and Future Directions.pdf`
- Page: `36`
- Chunk ID: `258`

```text
discern features indicative of text generation by LLMs. Uchendu et al. (2023) noted that a lack of coherence and consistency in LLM-generated text serves as a strong indicator of falsiﬁed content. Texts produced by LLMs often exhibit semantic inconsistencies and logical errors. Additionally, Dugan et al. (2023) identiﬁed that the human discernment of LLM-generated text varies across different domains. For instance, LLMs tend to gen- erate more “generic” text in the news domain, whereas, in story domains, the text might be more “irrelevant.” Ma et al. (2023) noted that evaluators of academic writing typically emphasize style. Summaries generated by LLMs frequently lack detail, particularly in describing the research motivation and methodology, which hampers the provision of fresh insights. In contrast, LLM-generated papers exhibit fewer grammatical and other types of errors and demonstrat...
```

### Top 2

- Source: `Detection of ChatGPT Fake Science with the xFakeSci Learning Algorithm.pdf`
- Page: `4`
- Chunk ID: `577`

```text
Alzheimer’s disease and co-morbidities 1196 Cancer and co-morbidities 1243 Depression 1513 Total number of generated articles 3952 The prompt-engineering process is computationally described in Algorithm 1. Although this process was done programmat- ically, due to the timeout limit, we executed it to produce 20 simulated articles at a time. This prompt-engineering approach enabled us to generate a large corpus of simulated articles that closely resembled real scientific publications in terms of structure, content, and overall style. This dataset played a crucial role in training the xFakeSci algorithm, enabling it to accurately distinguish between real scientific articles and machine-generated ones. Algorithm 1 The Computational Process of ChatGPT Prompt Engineering for Article Generation Require: diseases = [“Alzheimer’s”, “Cancer”, “Depression”] Require: article_number = 20. Require: a...
```

### Top 3

- Source: `ASurvey onLLM-Generated Text Detection Necessity, Methods, and Future Directions.pdf`
- Page: `36`
- Chunk ID: `259`

```text
other types of errors and demonstrate a broader variety of expression (Yan et al. 2023; Liao et al. 2023). However, these papers often use general terms instead of effectively tailored information relevant to the speciﬁc problem context. In human-written texts, such as scientiﬁc papers, authors are prone to composing lengthy paragraphs and using ambiguous language (Desaire et al. 2023), often incorporating terms like “but,” “however,” and “although.” Dugan et al. (2023) also noted that relying solely on gram- matical errors as a detection strategy is unreliable. In addition, LLMs frequently commit factual and common-sense reasoning errors, which, while often overlooked by neural network-based detectors, are easily noticed by humans (Jawahar, Abdul-Mageed, and Lakshmanan 2020). 6.2 Imperceptible Features Ippolito et al. (2020) suggested that text perceived as high quality by humans tends ...
```

### Top 4

- Source: `ASurvey onLLM-Generated Text Detection Necessity, Methods, and Future Directions.pdf`
- Page: `10`
- Chunk ID: `142`

```text
by LLMs, and the lack of effective evaluation frameworks. In summary, we ﬁrmly believe that this review is more systematic and comprehen- sive than existing works. More importantly, our critical discussion not only provides guidance to new researchers but also imparts valuable insights into established works within the ﬁeld. 3.2 Systematic Investigation and Implementation Our survey utilized the System for Literature Review (SLR) as delineated by Kitchenham and Charters (2007), a methodological framework designed for evaluating the extent and quality of extant evidence pertaining to a speciﬁed research question or topic. Offering a more expansive and accurate insight compared with conventional literature reviews, this approach has been prominently utilized in numerous scholarly surveys, as evidenced by Murtaza et al. (2020) and Saeed and Omlin (2023). The research questions guiding our S...
```

### Top 5

- Source: `ASurvey of AI-generated Text Forensic Systems Detection Attribution and Characterization.pdf`
- Page: `19`
- Chunk ID: `98`

```text
Research Paper Abstracts 600K (HW + MG) Acc 98%X Review, Polish, Re-vise, Rewrite andEdit the Title, Ab-stractAcademic Text(Liyanage andBuscaldi, 2023) GPT Academia DAGPap22, GPT Wiki Intro500-R and 500-MGF1-Score97.5% X first 7 words ofWiki Intro, first 50Words of Academicpaper or first sen-tence of AbstractMULTITuDE(Macko et al.,2023) Multilingual LLMs - GPT-3, GPT-4, LLaMA65B,ChatGPT, Alpaca-LoRa-30B, Vicuna-13B, OPT-66B, IML-Max-1.3B News MassiveSumm 11 languages- 74K (8K-HW,66K-MG) Acc 94.50% (En) ✓ Titles of selected ar-ticles To ChatGPT (Pego-raro et al., 2023)ChatGPT Medical, Open QA,Finance User-generated responses frompopular Social Networking Plat-forms 131K (58k HW, 72K MG)TPR% (De-tection Capa-bility) Detects 90% as HWX Inquiry prompts H3Plus (Su et al.,2023e) ChatGPT News CNN,DailyMail, Xsum, LCSTS,News2016, WMT210K (42K-Chinese, 95K-EnTrain samples) Acc 99.5% En, 98.65%Chi...
```

---

# Question 3

**Question:** What are the key assumptions?

**Manual Grade:** Good / Medium / Bad

**Notes:** 

## Retrieved Chunks

### Top 1

- Source: `Release strategies and the social impacts of Language Models.pdf`
- Page: `12`
- Chunk ID: `779`

```text
more of GPT-2’s outputs, giving richer insight into the distribution of output qualities as opposed to just the models’ peak generation ability.11Third, they investigated the underlying factors driving people’s credibility perceptions. The authors developed a credibility score composed of independent clarity, ac- curacy, and believability scores. By breaking credibility down into parts and also soliciting free-form responses from survey participants, the authors identified many instances of participants explaining away inaccuracies in GPT-2 outputs. Participants who noted inaccuracies or lack of in-text sources still cited the story’s plausibility as their basis for their assigned credibility score. These results help explain why there is not an even larger gap in credibility scores between model sizes: believability and clarity vary less across model sizes than accuracy does, and believ...
```

### Top 2

- Source: `ASurvey onLLM-Generated Text Detection Necessity, Methods, and Future Directions.pdf`
- Page: `46`
- Chunk ID: `306`

```text
detectors that are more practical and aligned with real-world scenarios. 9.7 Constructing Detectors with Misinformation Discrimination Capabilities Contemporary detection methodologies have largely overlooked the capacity to iden- tify misinformation. Existing detectors primarily emphasize the distribution of features within the text generated by LLMs but often overlooked their potential for factual veriﬁcation. A proﬁcient detector should possess the capability to discern the veracity or falsity of factual claims presented in text. In the initial stages of generative modeling’s emergence, when it had yet to pose signiﬁcant societal challenges, the emphasis was on assessing the truth or falsity of the content in LLM-generated text, with less regard for its 321
```

### Top 3

- Source: `Release strategies and the social impacts of Language Models.pdf`
- Page: `64`
- Chunk ID: `917`

```text
allow us to leverage the automated nature of our article synthesis system by showing each respondent a different generated text.3 We included this platform in our survey as an exter- nal link. Respondents each read a story generated by GPT-2, and then answered a number of questions about their perceptions of the story’s credibility. To disaggregate the concept of credibility and understand the aspects of the text that individuals understood to correspond with being credible, we separately asked whether the story was believable, accurate, and clear (each on a 1-4 scale, with 4 as the best rating). To calculate an overall credibility index (also referred to as the credibility score), we summed each respondent’s answers to the three questions and scaled the result to be between 1 and 10. Consistent with our previous experiments, all our articles were generated using the first sentence of a ...
```

### Top 4

- Source: `Release strategies and the social impacts of Language Models.pdf`
- Page: `59`
- Chunk ID: `907`

```text
4 Roadmap While these efforts represent our first experiments with GPT-2, CTEC has several other plans to more fully develop our threat model and assessment. We will continue to broaden our quantitative approach, but we will also add two additional initiatives. First, a team of linguists at the Middlebury Institute will be conducting in-depth qualitative linguistic analysis on the outputs from these models. In particular, this team is interested in investigating how GPT-2 produces language, how it represents the ideologies latent in the source texts, and how its word choice varies across samples. This initiative will search for signs of contradictions, unusual stylistic markers, and other “tells” of fake content that may be noticeable to experienced linguists. Second, much like the work done by Adelani et al
```

### Top 5

- Source: `ASurvey onLLM-Generated Text Detection Necessity, Methods, and Future Directions.pdf`
- Page: `45`
- Chunk ID: `302`

```text
understanding of the model’s internal workings, thereby offering broader applicability across various models and environments. 9.3 Optimizing Detectors for Low-Resource Environments Many contemporary detection techniques tend to overlook the challenges faced by resource-constrained settings, often neglecting the need for resources in developing the detector. The relative efﬁcacy of various detectors across different data volume set- tings remains inadequately explored. Concurrently, determining the minimal resource prerequisites for different detection methods to yield satisfactory results is imperative. Beyond examining the model’s adaptability across distinct domains (Rodriguez et al. 320
```

---

# Question 4

**Question:** What are the limitations of the method?

**Manual Grade:** Good / Medium / Bad

**Notes:** 

## Retrieved Chunks

### Top 1

- Source: `ASurvey onLLM-Generated Text Detection Necessity, Methods, and Future Directions.pdf`
- Page: `27`
- Chunk ID: `215`

```text
perturbations, achieving improved performance with an approximate 2% increase in AUROC. While innovative and sometimes more effective than supervised methods, Detect- GPT has limitations, including potential performance drops if rewrites don’t adequately represent the space of meaningful alternatives, and high computational demands, as it requires perturbing and scoring numerous texts. To address these challenges, Deng et al. (2023) proposed a method using a Bayesian surrogate model to score a small set of representative samples. By extrapolating the scores from these samples to others, the method enhances query efﬁciency and reduces computational overhead while preserv- ing performance. Extensive empirical studies on datasets such as GPT-2, LLaMA2, and Vicuna have demonstrated its efﬁciency over DetectGPT (Mitchell et al. 2023), especially in detecting texts generated by the LLaMA. This...
```

### Top 2

- Source: `Detection of ChatGPT Fake Science with the xFakeSci Learning Algorithm.pdf`
- Page: `6`
- Chunk ID: `591`

```text
to further guide the classification process without having to train the algorithm with too many samples. The algorithmic steps for the calibration process are explained in Algorithm 4. Though the ranges provide an extra net for predicting the label, it is also possible that some document instances may fall outside the specified ranges of the datasets, which could result in not 7/18
```

### Top 3

- Source: `ASurvey onLLM-Generated Text Detection Necessity, Methods, and Future Directions.pdf`
- Page: `44`
- Chunk ID: `296`

```text
inconsistencies. This dimension presents a rich avenue for exploration and discourse. Request for Objective and Fair Benchmark. A prevalent issue in LLM-generated text de- tection research is the discrepancy between claimed detector performance and practical results. While many studies report impressive and robust detector capabilities, these methods often underperform on test sets created by other researchers. This variance arises from using different strategies to construct their test sets including the parameters used to generate the test set, the computational environment, text distribution, and text processing strategies, including truncation, which can all inﬂuence the effectiveness of detectors. Due to these factors’ complex nature, the reproducibility of evaluation results is often compromised, even when researchers adhere to identical dataset production protocols. As discussed i...
```

### Top 4

- Source: `Release strategies and the social impacts of Language Models.pdf`
- Page: `24`
- Chunk ID: `816`

```text
and others about improving processes for distributed risk analysis. Our legal negotiation process and subsequent learnings about GPT-2 demonstrate that there is no standardizable model sharing approach. We provide a template agreement in Appendix A to help organizations develop appropriate processes in this area. 23
```

### Top 5

- Source: `DetectLLM Leveraging Log-Rank Information for Zero-Shot Detection of Machine-Generated Text.pdf`
- Page: `8`
- Chunk ID: `672`

```text
and the disadvantages of different zero-shot meth- ods. Then, we analyzed the computational costs of these methods, and we provided guidance on balancing efficiency and performance. Limitations One of the limitations of zero-shot methods is the white box assumption that we can have some statis- tics about the source model. This induces two problems: for closed-source models (such as GPT- 3), these statistics might not have been provided. Moreover, in practice, the detector might have to run the model locally to get the statistics for the purpose of detection, which requires that the de- tector have enough resources to use the LLM for inference. Based on the limitations of zero-shot methods, we consider weakly supervised learning (Ratner et al., 2017) as an important direction for future work. Though many papers in detecting machine-generated text assume knowing the source LLM where the t...
```

---

# Question 5

**Question:** What experiments are conducted in this paper?

**Manual Grade:** Good / Medium / Bad

**Notes:** 

## Retrieved Chunks

### Top 1

- Source: `Detection of ChatGPT Fake Science with the xFakeSci Learning Algorithm.pdf`
- Page: `4`
- Chunk ID: `576`

```text
comparable to real abstracts. They included three key elements: (a) the role of the prompt: “a biomedical researcher,” (b) the request example: “Generate a list of 20 simulated PubMed-style abstracts,” (c) topic example: “the Alzheimer’s disease,” and (d) specifications: each article must contain ID, Title, and Abstract fields. We also instructed prompts to generate a valid JSON response with these specifications. The number of words helped offset any bias and made the fake articles comparable to the precise level of detail required (the 200-250 words range is a common requirement by many prominent biomedical informatics journals). Table 1 captures the search queries and the number of fake articles generated in the JSON format. Table 1. Result Counts of Prompt Engineering Search Query Count (JSON Records) Alzheimer’s disease and co-morbidities 1196 Cancer and co-morbidities 1243 Depressi...
```

### Top 2

- Source: `Detection of ChatGPT Fake Science with the xFakeSci Learning Algorithm.pdf`
- Page: `2`
- Chunk ID: `565`

```text
experiments in the subject area of three different diseases. Additionally, we performed experiments to evaluate whether the year of publication plays a role in class prediction. This section presents the outcomes of experiments utilizing ChatGPT-generated text obtained algorithmically using ChatGPT prompt-engineering, as outlined in Algorithm 1, and scientific publications retrieved from the PubMed web portal37 related to the Alzheimer’s, cancer, and depression diseases. Here, we present the results of multi-mode experiments, where xFakeSci was trained using a combination of ChatGPT and PubMed abstracts and evaluated on a dataset of unseen documents from all three diseases. Specifically, we trained xFakeSci using an equal-sized dataset of ChatGPT-generated and PubMed abstracts. Then, we calibrated the algorithm using the exact number of k-Folds for each disease. For the PubMed dataset, w...
```

### Top 3

- Source: `Detection of ChatGPT Fake Science with the xFakeSci Learning Algorithm.pdf`
- Page: `4`
- Chunk ID: `577`

```text
Alzheimer’s disease and co-morbidities 1196 Cancer and co-morbidities 1243 Depression 1513 Total number of generated articles 3952 The prompt-engineering process is computationally described in Algorithm 1. Although this process was done programmat- ically, due to the timeout limit, we executed it to produce 20 simulated articles at a time. This prompt-engineering approach enabled us to generate a large corpus of simulated articles that closely resembled real scientific publications in terms of structure, content, and overall style. This dataset played a crucial role in training the xFakeSci algorithm, enabling it to accurately distinguish between real scientific articles and machine-generated ones. Algorithm 1 The Computational Process of ChatGPT Prompt Engineering for Article Generation Require: diseases = [“Alzheimer’s”, “Cancer”, “Depression”] Require: article_number = 20. Require: a...
```

### Top 4

- Source: `Unsupervised and distributional detection.pdf`
- Page: `8`
- Chunk ID: `964`

```text
Figure 8: Histogram of diversity for different sampling strategies. enhanced sufﬁx arrays. Journal of discrete algo- rithms, 2(1):53–86. Anton Bakhtin, Yuntian Deng, Sam Gross, Myle Ott, Marc’Aurelio Ranzato, and Arthur Szlam. 2021. Residual energy-based models for text. Journal of Machine Learning Research, 22(40):1–41. Emily M Bender, Timnit Gebru, Angelina McMillan- Major, and Shmargaret Shmitchell. 2021. On the dangers of stochastic parrots: Can language models be too big. In Proceedings of the 2020 Conference on Fairness, Accountability, and Transparency; As- sociation for Computing Machinery: New York, NY, USA. Tom B Brown, Benjamin Mann, Nick Ryder, Melanie Subbiah, Jared Kaplan, Prafulla Dhariwal, Arvind Neelakantan, Pranav Shyam, Girish Sastry, Amanda Askell, et al. 2020. Language models are few-shot learners. arXiv preprint arXiv:2005.14165. Ben Buchanan, Andrew Lohn, Micah Mus...
```

### Top 5

- Source: `Detection of ChatGPT Fake Science with the xFakeSci Learning Algorithm.pdf`
- Page: `9`
- Chunk ID: `607`

```text
is also the responsibility of publishers and those involved in the production of science to play a proactive role in promoting good science. This includes raising awareness of the importance of implementing advanced fake science detection algorithms, including ours, and activating the use of technologies to distinguish fake research and fabricated findings35. Looking ahead, there are several avenues for future research based on our current work: (1) conducting a preprocessing step (e.g., clustering) to group more closely related publications together (e.g., breast cancer, prostate cancer, and others), or separate diseases from co-morbidities. The use of knowledge graphs may be a powerful tool to use in continuing to investigate this research direction; (2) further experimentation in training and calibrating the xFakeSci algorithm by utilizing heuristics learned from preprocessing steps a...
```

---

# Question 6

**Question:** What baselines are compared in this paper?

**Manual Grade:** Good / Medium / Bad

**Notes:** 

## Retrieved Chunks

### Top 1

- Source: `DetectLLM Leveraging Log-Rank Information for Zero-Shot Detection of Machine-Generated Text.pdf`
- Page: `11`
- Chunk ID: `687`

```text
A Experimental Details and Baselines Details on Baselines. We mainly compare the proposed methods with zero-shot methods, which utilize the source model itself to extract distinguishable statistic features, including: • Log-Likelihood (log p) (Solaiman et al., 2019): This approach evaluates the average token-wise log probability of the text and classifies text with higher Log-Likelihood to be machine-generated. • Rank (Gehrmann et al., 2019): This approach evaluates the average rank of each token of the text and classifies text with a smaller average rank to be machine-generated. • Log-Rank (Mitchell et al., 2023): Instead of using the Rank score directly, this approach evaluates the average Log-Rank of each token of the text and classifies text with a smaller average Log-Rank to be machine-generated. • Entropy (Gehrmann et al., 2019): This approach is inspired by the hypothesis that mac...
```

### Top 2

- Source: `DetectLLM Leveraging Log-Rank Information for Zero-Shot Detection of Machine-Generated Text.pdf`
- Page: `3`
- Chunk ID: `647`

```text
erated by the target LLM; • Log-Rank: passage with a higher average ob- served Log-Rank is more likely to have been generated by the target LLM; • Entropy: machine-generated text has higher entropy; • DetectGPT: machine-generated text has more negative log probability curvature. More detail and exact definitions of these meth- ods can be found in Appendix A. These zero-shot baselines, along with our newly proposed LRR and NPR, can be categorized as • Perturbation-free: log p(x), Rank, Log- Rank, Entropy, LRR. They only query the LLM for statistics about the target text x. • Perturbation Based: DetectGPT and NPR. These methods query the LLM not only for the target text x, but also for perturbed versions thereof ˜x1,···,˜xp. As perturbation-based methods perform better (but are also more time-consuming), for fair com- parison, we compare them within their own group. Supervised Methods We a...
```

### Top 3

- Source: `DetectLLM Leveraging Log-Rank Information for Zero-Shot Detection of Machine-Generated Text.pdf`
- Page: `5`
- Chunk ID: `656`

```text
Function Perturbation Dataset # (Perturbations) 10 20 50 100 NPR (ours) T5-large 86.69 88.00 88.74 88.94 T5-3b 91.39 92.35 93.04 93.20 Diff 4.70 4.35 4.30 4.26 DetectGPT T5-large 77.94 81.12 83.90 84.54 T5-3b 86.70 89.57 91.38 92.10 Diff 8.76 8.45 7.48 7.56 Table 3: Perturbation analysis. Comparing DetectGPT to NPR using different perturbations (AUROC scores). count for a total mass probability p. The results (averaged across 4 LLMs) are shown in Table 2, and complete results can be found in Table 9 of Appendix D. We find that, although almost all the zero-shot methods perform better when using top- k and top-p sampling than temperature sampling, Log-Rank and Log-Likelihood methods are more in favour of top-p sampling, while LRR is stable in both top- p and top-k sampling. For top- k de- coding, LRR improves 4.06, 9.33, and 1.38 points over the second-best zero-shot method baseline on th...
```

### Top 4

- Source: `ASurvey onLLM-Generated Text Detection Necessity, Methods, and Future Directions.pdf`
- Page: `44`
- Chunk ID: `296`

```text
inconsistencies. This dimension presents a rich avenue for exploration and discourse. Request for Objective and Fair Benchmark. A prevalent issue in LLM-generated text de- tection research is the discrepancy between claimed detector performance and practical results. While many studies report impressive and robust detector capabilities, these methods often underperform on test sets created by other researchers. This variance arises from using different strategies to construct their test sets including the parameters used to generate the test set, the computational environment, text distribution, and text processing strategies, including truncation, which can all inﬂuence the effectiveness of detectors. Due to these factors’ complex nature, the reproducibility of evaluation results is often compromised, even when researchers adhere to identical dataset production protocols. As discussed i...
```

### Top 5

- Source: `Detection of ChatGPT Fake Science with the xFakeSci Learning Algorithm.pdf`
- Page: `11`
- Chunk ID: `612`

```text
Table 5. Model Calibration: Summary of Lower and Upper Bound Ranges for Different Diseases and Datasets by Year Periods: 2010-2014, 2015-2019, 2020-2024 Alzheimer’s Cancer Depression GPT Pub 10-14 15-19 20-24 GPT 10-14 15-19 20-24 GPT 10-14 15-19 20-24 Lower 0.27 0.15 0.14 0.14 0.25 0.13 0.15 0.15 0.28 0.10 0.09 0.10 Upper 0.30 0.16 0.15 0.15 0.29 0.15 0.16 0.17 0.32 0.11 0.13 0.11 Table 6. Multi-Mode Experiments: xFakeSci Performance Evaluation for Recent Publications (2019 - 2024) Classifier Used Disease Dataset Tested TP FP FN TN F1 Score xFakeSci Depression 50 25 0 25 80.00% xFakeSci Cancer 50 9 0 41 91.74% xFakeSci Alzheimer’s 50 12 0 38 89.29% Table 7. Multi-Mode Experiments: F1 Classification Scores From Most Recent Publications Classifier / Publication (2020-2024) Depression Cancer Alzheimer’s xFakeSci 80% 91% 89% Naive Bayes 52% 43% 47% Linear SVM 39% 51% 50% Classical SVM 44% 4...
```

---

# Question 7

**Question:** What evaluation metrics are used?

**Manual Grade:** Good / Medium / Bad

**Notes:** 

## Retrieved Chunks

### Top 1

- Source: `ASurvey onLLM-Generated Text Detection Necessity, Methods, and Future Directions.pdf`
- Page: `37`
- Chunk ID: `263`

```text
purpose. This analytical approach not only bolsters experts’ trust in decision-making models but also fosters learning from the models’ behavior, improving the identiﬁcation of LLM-generated samples. 7. Evaluation 7.1 Evaluation Metrics Evaluation metrics are indispensable for the assessment of model performance within any NLP task, including LLM-generated text detection. This section discusses conven- tionally utilized metrics in these tasks. Common metrics include Accuracy, Precision, Recall, F1 score, and AUROC (Dalianis 2018). Accuracy provides an overall measure of success in correctly identifying both human-written and LLM-generated texts, mak- ing it a straightforward metric for assessing the general effectiveness of a detection model. Precision and Recall in LLM-generated text detection are used to assess the precision of identifying LLM-generated text and the ability to capture ...
```

### Top 2

- Source: `ASurvey onLLM-Generated Text Detection Necessity, Methods, and Future Directions.pdf`
- Page: `11`
- Chunk ID: `148`

```text
watermarking and statistics-based approaches to neural-based detectors and human- assisted methods, providing insights into their effectiveness and limitations. Section 7 focuses on evaluation metrics include accuracy, precision, recall, false positive rate, true negative rate, false negative rate, F1 score, and the area under the receiver operating 286
```

### Top 3

- Source: `Authorship Attributionin the Era of LLMs Problems Methodologies and Challenges.pdf`
- Page: `8`
- Chunk ID: `461`

```text
for quantifying the performance of authorship models, providing a standardized means to assess and compare the effectiveness of different authorship attribution approaches. As in other classifica- tion tasks, existing studies predominantly use the Area Under the Receiver Operating Characteristic (AUCROC) and F1 score to evalu- ate attribution algorithms. In human authorship attribution, where there are a large number of candidate authors, retrieval metrics like Mean Reciprocal Rank (MRR) and recall-at-k are used (Rivera- Soto et al., 2021). Additionally, Self-BLEU and perplexity are useful metrics, with a lower Self-BLEU score indicating higher textual diversity (Zhang et al., 2024). Common evaluation metrics include: • Accuracy: Measures the proportion of correctly identified authors but can be misleading in imbalanced datasets. • Precision, Recall, and F1-Score: Crucial in imbalanced d...
```

### Top 4

- Source: `ASurvey onLLM-Generated Text Detection Necessity, Methods, and Future Directions.pdf`
- Page: `25`
- Chunk ID: `206`

```text
logits. The Rank metric calculates the ranking of each word in a sample within the model’s output probability distribution. This ranking is determined by comparing the logit score of the word against the logit scores of all other possible words. If the average rank of each word in the sample is high, it suggests that the sample is likely generated by 300
```

### Top 5

- Source: `ASurvey of AI-generated Text Forensic Systems Detection Attribution and Characterization.pdf`
- Page: `7`
- Chunk ID: `43`

```text
as tweets, reviews, and news articles. This diversity underscores the datasets’ comprehensive coverage in testing detection and attribution systems. 3.2 Performance Metrics The benchmarks use metrics like accuracy and F1 scores to evaluate the effectiveness of detection and attribution. We highlight the top performance records for each dataset. Detection performance in general AI-generated text is notably high. For example, the MULTITuDE (Macko et al., 2023) dataset, which concentrates on news text, marked an accuracy of 94%. In contrast, AI-misinformation de- tection performance is significantly lower, reflecting the complex challenges inherent in characterizing AI-generated misinformation. 3.3 AI-Misinformation Benchmarks Specific benchmarks address the difficulty of detect- ing AI-generated misinformation. Notably, early benchmarks such as Synthetic Lies (Zhou et al., 2023) demonstrat...
```

---

# Question 8

**Question:** What is the proposed algorithm?

**Manual Grade:** Good / Medium / Bad

**Notes:** 

## Retrieved Chunks

### Top 1

- Source: `Detection of ChatGPT Fake Science with the xFakeSci Learning Algorithm.pdf`
- Page: `4`
- Chunk ID: `577`

```text
Alzheimer’s disease and co-morbidities 1196 Cancer and co-morbidities 1243 Depression 1513 Total number of generated articles 3952 The prompt-engineering process is computationally described in Algorithm 1. Although this process was done programmat- ically, due to the timeout limit, we executed it to produce 20 simulated articles at a time. This prompt-engineering approach enabled us to generate a large corpus of simulated articles that closely resembled real scientific publications in terms of structure, content, and overall style. This dataset played a crucial role in training the xFakeSci algorithm, enabling it to accurately distinguish between real scientific articles and machine-generated ones. Algorithm 1 The Computational Process of ChatGPT Prompt Engineering for Article Generation Require: diseases = [“Alzheimer’s”, “Cancer”, “Depression”] Require: article_number = 20. Require: a...
```

### Top 2

- Source: `Detection of ChatGPT Fake Science with the xFakeSci Learning Algorithm.pdf`
- Page: `1`
- Chunk ID: `560`

```text
algorithm, which we designed to predict the class of a given document and determine whether it is real or fake. We outline the computational steps, including constructing the network training models, calibrating using data-driven heuristics, testing the algorithm in multiple contexts (diseases) and data from various publication periods, and finally, (4) benchmarking it against the most common classical data mining algorithms as a verification step. 3 Results 3.1 Outcome of Evaluating the Premise As mentioned earlier, we investigated the premise that of whether AI-generated content may exhibit unique characteristics that differ from those observed in scientific articles. We tested this intuition two stages: 2/18
```

### Top 3

- Source: `Detection of ChatGPT Fake Science with the xFakeSci Learning Algorithm.pdf`
- Page: `9`
- Chunk ID: `608`

```text
learned from preprocessing steps and the discoveries of clusters; and (3) testing the algorithm on more than two data sources (clinical reports, publications, and ChatGPT-generated documents). 10/18
```

### Top 4

- Source: `Detection of ChatGPT Fake Science with the xFakeSci Learning Algorithm.pdf`
- Page: `7`
- Chunk ID: `594`

```text
the distance is calculated. distance = min (|point − rangeend| , |point − rangestart |) (5) proximity = min(distanced,distanced′) (6) Algorithm 5 illustrates the computational steps for multi-mode execution, demonstrating the complexity involved, including the proximity distance. To use the algorithm in detecting fake science, it must be trained using two different types of data: (1) a real publication dataset and (2) ChatGPT-generated articles. The algorithm also expects the ratio means of each data source, which are computed using the calibration algorithm. 5 Discussion In a world where generative AI has become widespread, various studies aimed to investigate the potential issues of using ChatGPT to generate fake science. The literature review showed a desperate need to advance the algorithmic approaches to discern real publications from fake ones, especially, when they are mixed. Our ...
```

### Top 5

- Source: `DetectLLM Leveraging Log-Rank Information for Zero-Shot Detection of Machine-Generated Text.pdf`
- Page: `6`
- Chunk ID: `665`

```text
The computational time for Log-Likelihood, rank, Log-Rank, and entropy is approximately tm, the estimated time for LRR is 2·tm, while the es- timated computational time for the perturbation- based method is n·tp + (n + 1)·tm. The estimated values of tp and tm are illustrated in Table 6, which can help us estimate the total running time (in sec- onds) of different zero-shot methods. 6.2 Balancing Efficiency and Performance In this subsection, we provide additional experi- ments on LRR (the best perturbation-free method) and NPR (the best perturbation-based method, more time-consuming than LRR but also rather sat- isfactory performance) to provide users with some intuition on setting parameters of NPR and choos- ing among between these two methods according to user’s preference of efficiency and performance. First, we study the perturbation function used for NPR. Different from Section 5.2...
```

---

# Question 9

**Question:** What are the main theoretical results?

**Manual Grade:** Good / Medium / Bad

**Notes:** 

## Retrieved Chunks

### Top 1

- Source: `DetectLLM Leveraging Log-Rank Information for Zero-Shot Detection of Machine-Generated Text.pdf`
- Page: `5`
- Chunk ID: `658`

```text
For example, students might set a high tempera- ture to encourage more original and diverse output when writing a creative essay, whereas fake news producers might set lower temperatures to generate seemingly convincing news articles for their decep- tive purposes. Based on our experiments in Table 4, we found that Log-Likelihood (log p), Log-Rank and LRR is highly sensitive to the temperature and can get even better results than perturbation-based methods when the temperature is relatively low. In addition, the performance improvement of the Rank method with the increased temperature is neg- ligible compared to Log-Likelihood, Log-Rank and LRR, while the performance of the entropy method seems to be positively correlated to the tempera- ture. We conjure that the abnormal behaviour of the Entropy method might be because of the as- sumption that “machine-generated text has higher entropy"...
```

### Top 2

- Source: `Release strategies and the social impacts of Language Models.pdf`
- Page: `11`
- Chunk ID: `777`

```text
Human Detection Over the past six months, we have seen substantial research into the ability of humans to discriminate between human- and machine-generated text samples. Research on human perception of generated text suggests that the quality of outputs increases with model size at least up until the 774 million parameter model. With a human-in-the-loop, GPT-2 can generate out- puts that humans find credible. Kreps and McCain at Cornell University found that cherry-picked fake news samples from the 355 million parameter version of GPT-2 were considered “credible” about 66% of the time.9Similarly cherry-picked outputs from the 774 million and 1.5 billion parameter versions of 9GPT-2 was used to generate continuations of a real New Y ork Times article using the first one or two paragraphs as a prompt. Each of the three model sizes (355M, 774M, and 1.5B) was used to generate 20 outputs, and...
```

### Top 3

- Source: `Release strategies and the social impacts of Language Models.pdf`
- Page: `12`
- Chunk ID: `779`

```text
more of GPT-2’s outputs, giving richer insight into the distribution of output qualities as opposed to just the models’ peak generation ability.11Third, they investigated the underlying factors driving people’s credibility perceptions. The authors developed a credibility score composed of independent clarity, ac- curacy, and believability scores. By breaking credibility down into parts and also soliciting free-form responses from survey participants, the authors identified many instances of participants explaining away inaccuracies in GPT-2 outputs. Participants who noted inaccuracies or lack of in-text sources still cited the story’s plausibility as their basis for their assigned credibility score. These results help explain why there is not an even larger gap in credibility scores between model sizes: believability and clarity vary less across model sizes than accuracy does, and believ...
```

### Top 4

- Source: `Release strategies and the social impacts of Language Models.pdf`
- Page: `17`
- Chunk ID: `793`

```text
They reported that their largest GROVER-MEGA model detected its own and other GROVER models’ outputs at 92% accuracy. They also tested our 124 million and 355 million parameter GPT-2 models and found detection accuracy increased with size. Zellers et al. argued that these findings support the release of large generative models to aid in defense against misuse. While we agree there are benefits, releasing models enables misuse itself and defenses are not impenetrable. Attention to reducing tradeoffs between reducing false positives and false negatives will be needed since each has distinct implications for online platforms. 16
```

### Top 5

- Source: `DetectLLM Leveraging Log-Rank Information for Zero-Shot Detection of Machine-Generated Text.pdf`
- Page: `11`
- Chunk ID: `687`

```text
A Experimental Details and Baselines Details on Baselines. We mainly compare the proposed methods with zero-shot methods, which utilize the source model itself to extract distinguishable statistic features, including: • Log-Likelihood (log p) (Solaiman et al., 2019): This approach evaluates the average token-wise log probability of the text and classifies text with higher Log-Likelihood to be machine-generated. • Rank (Gehrmann et al., 2019): This approach evaluates the average rank of each token of the text and classifies text with a smaller average rank to be machine-generated. • Log-Rank (Mitchell et al., 2023): Instead of using the Rank score directly, this approach evaluates the average Log-Rank of each token of the text and classifies text with a smaller average Log-Rank to be machine-generated. • Entropy (Gehrmann et al., 2019): This approach is inspired by the hypothesis that mac...
```

---

# Question 10

**Question:** What future work is mentioned?

**Manual Grade:** Good / Medium / Bad

**Notes:** 

## Retrieved Chunks

### Top 1

- Source: `Authorship Attributionin the Era of LLMs Problems Methodologies and Challenges.pdf`
- Page: `8`
- Chunk ID: `463`

```text
sures the average absolute difference between the predicted position index and the actual change point. 7 OPPORTUNITIES AND FUTURE DIRECTIONS This section explores future directions in the field of authorship attribution, focusing on leveraging the potential of LLMs while ad- dressing associated challenges. Future efforts should aim for finer granularity in authorship attribution, leveraging LLM capabilities, improving generalization, enhancing explainability, preventing mis- use, developing standardized benchmarks, and integrating interdis- ciplinary perspectives to enrich the field. 9
```

### Top 2

- Source: `ASurvey of AI-generated Text Forensic Systems Detection Attribution and Characterization.pdf`
- Page: `7`
- Chunk ID: `45`

```text
seed prompts, and detailed performance metrics, can be found in Table 4 in the Appendix. 4 Future of AI-generated Text Forensics The rapid evolution of LLMs foreshadows an AI- centric future where AI systems may partially or entirely manage many everyday writing tasks. Con- currently, this shift introduces significant challenges and more complex threat scenarios. In the subse- quent sections, we explore such potential challenges
```

### Top 3

- Source: `Release strategies and the social impacts of Language Models.pdf`
- Page: `9`
- Chunk ID: `771`

```text
plan of action. Given the scale of AI’s potential effects, we think it remains an open question as to what the appropriate heuristics are for such notification procedures, and it will require close collaboration between AI researchers, security professionals, potentially affected stakeholders, and policymakers, to determine appropriate approaches. 8
```

### Top 4

- Source: `Release strategies and the social impacts of Language Models.pdf`
- Page: `59`
- Chunk ID: `907`

```text
4 Roadmap While these efforts represent our first experiments with GPT-2, CTEC has several other plans to more fully develop our threat model and assessment. We will continue to broaden our quantitative approach, but we will also add two additional initiatives. First, a team of linguists at the Middlebury Institute will be conducting in-depth qualitative linguistic analysis on the outputs from these models. In particular, this team is interested in investigating how GPT-2 produces language, how it represents the ideologies latent in the source texts, and how its word choice varies across samples. This initiative will search for signs of contradictions, unusual stylistic markers, and other “tells” of fake content that may be noticeable to experienced linguists. Second, much like the work done by Adelani et al
```

### Top 5

- Source: `Detection of ChatGPT Fake Science with the xFakeSci Learning Algorithm.pdf`
- Page: `9`
- Chunk ID: `607`

```text
is also the responsibility of publishers and those involved in the production of science to play a proactive role in promoting good science. This includes raising awareness of the importance of implementing advanced fake science detection algorithms, including ours, and activating the use of technologies to distinguish fake research and fabricated findings35. Looking ahead, there are several avenues for future research based on our current work: (1) conducting a preprocessing step (e.g., clustering) to group more closely related publications together (e.g., breast cancer, prostate cancer, and others), or separate diseases from co-morbidities. The use of knowledge graphs may be a powerful tool to use in continuing to investigate this research direction; (2) further experimentation in training and calibrating the xFakeSci algorithm by utilizing heuristics learned from preprocessing steps a...
```

---

