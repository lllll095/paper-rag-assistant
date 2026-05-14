# Hybrid Retrieval Evaluation

This report compares three retrieval settings:

1. **Dense only**: paper routing + embedding-based chunk retrieval.
2. **BM25 only**: paper routing + keyword-based chunk retrieval.
3. **Hybrid + reranker**: paper routing + dense retrieval + BM25 retrieval + cross-encoder reranking.

The goal is to understand whether hybrid retrieval improves recall and chunk relevance.

---

## Broad overview of AI-generated text detection

### Question

What AI-generated text detection methods are discussed in these papers?

### Retrieval Modes

- Dense-only mode: `global`
- BM25-only mode: `global`
- Hybrid mode: `global`

### Candidate Papers

These should usually be similar because all three settings use the same paper-level routing.

#### Hybrid Candidate Papers

1. `SeqXGPT Sentence-Level AI-Generated Text Detection.pdf`
   - Title: SeqXGPT Sentence Level AI Generated Text Detection
   - Paper score: `0.32273662090301514`

2. `Unsupervised and Distributional Detection of Machine-Generated Text.pdf`
   - Title: Unsupervised and Distributional Detection of Machine Generated Text
   - Paper score: `0.3335437774658203`

3. `ASurvey of AI-generated Text Forensic Systems Detection Attribution and Characterization.pdf`
   - Title: ASurvey of AI generated Text Forensic Systems Detection Attribution and Characterization
   - Paper score: `0.3376709520816803`

4. `Ghostbuster Detecting Text Ghostwritten by Large Language Models.pdf`
   - Title: Ghostbuster Detecting Text Ghostwritten by Large Language Models
   - Paper score: `0.3487025201320648`


### Selected Papers

#### Dense-only Selected Papers

1. `SeqXGPT Sentence-Level AI-Generated Text Detection.pdf`
   - Title: SeqXGPT Sentence Level AI Generated Text Detection
   - Paper score: `0.32273662090301514`

2. `Unsupervised and Distributional Detection of Machine-Generated Text.pdf`
   - Title: Unsupervised and Distributional Detection of Machine Generated Text
   - Paper score: `0.3335437774658203`

3. `ASurvey of AI-generated Text Forensic Systems Detection Attribution and Characterization.pdf`
   - Title: ASurvey of AI generated Text Forensic Systems Detection Attribution and Characterization
   - Paper score: `0.3376709520816803`

4. `Ghostbuster Detecting Text Ghostwritten by Large Language Models.pdf`
   - Title: Ghostbuster Detecting Text Ghostwritten by Large Language Models
   - Paper score: `0.3487025201320648`


#### BM25-only Selected Papers

1. `SeqXGPT Sentence-Level AI-Generated Text Detection.pdf`
   - Title: SeqXGPT Sentence Level AI Generated Text Detection
   - Paper score: `0.32273662090301514`

2. `Unsupervised and Distributional Detection of Machine-Generated Text.pdf`
   - Title: Unsupervised and Distributional Detection of Machine Generated Text
   - Paper score: `0.3335437774658203`

3. `ASurvey of AI-generated Text Forensic Systems Detection Attribution and Characterization.pdf`
   - Title: ASurvey of AI generated Text Forensic Systems Detection Attribution and Characterization
   - Paper score: `0.3376709520816803`

4. `Ghostbuster Detecting Text Ghostwritten by Large Language Models.pdf`
   - Title: Ghostbuster Detecting Text Ghostwritten by Large Language Models
   - Paper score: `0.3487025201320648`


#### Hybrid Selected Papers

1. `SeqXGPT Sentence-Level AI-Generated Text Detection.pdf`
   - Title: SeqXGPT Sentence Level AI Generated Text Detection
   - Paper score: `0.32273662090301514`

2. `Unsupervised and Distributional Detection of Machine-Generated Text.pdf`
   - Title: Unsupervised and Distributional Detection of Machine Generated Text
   - Paper score: `0.3335437774658203`

3. `ASurvey of AI-generated Text Forensic Systems Detection Attribution and Characterization.pdf`
   - Title: ASurvey of AI generated Text Forensic Systems Detection Attribution and Characterization
   - Paper score: `0.3376709520816803`

4. `Ghostbuster Detecting Text Ghostwritten by Large Language Models.pdf`
   - Title: Ghostbuster Detecting Text Ghostwritten by Large Language Models
   - Paper score: `0.3487025201320648`


### Summary Statistics

| Metric | Dense only | BM25 only | Hybrid + reranker |
|---|---:|---:|---:|
| Retrieved chunks | 8 | 8 | 8 |
| Unique sources | 3 | 3 | 3 |
| Noisy chunks | 0 | 0 | 0 |
| Overlap with hybrid | 4 | 2 | 8 |

### Source Distribution

#### Dense only

- `ASurvey of AI-generated Text Forensic Systems Detection Attribution and Characterization.pdf`: 3 chunks
- `Ghostbuster Detecting Text Ghostwritten by Large Language Models.pdf`: 3 chunks
- `SeqXGPT Sentence-Level AI-Generated Text Detection.pdf`: 2 chunks

#### BM25 only

- `ASurvey of AI-generated Text Forensic Systems Detection Attribution and Characterization.pdf`: 3 chunks
- `Ghostbuster Detecting Text Ghostwritten by Large Language Models.pdf`: 3 chunks
- `Unsupervised and Distributional Detection of Machine-Generated Text.pdf`: 2 chunks

#### Hybrid + reranker

- `ASurvey of AI-generated Text Forensic Systems Detection Attribution and Characterization.pdf`: 3 chunks
- `SeqXGPT Sentence-Level AI-Generated Text Detection.pdf`: 3 chunks
- `Ghostbuster Detecting Text Ghostwritten by Large Language Models.pdf`: 2 chunks

### Dense-only Retrieved Chunks

### Retrieved Chunk 1

- Source: `ASurvey of AI-generated Text Forensic Systems Detection Attribution and Characterization.pdf`
- Page: `13`
- Chunk ID: `491`
- Chunk Type: `main`
- Dense Score: `0.31118810176849365`
- Vector Score: `0.31118810176849365`
- BM25 Score: `unknown`
- Reranker Score: `unknown`

```text
Eric Mitchell, Yoonho Lee, Alexander Khaz- atsky, Christopher D. Manning, and Chelsea Finn. 2023. DetectGPT: Zero-Shot Machine- Generated Text Detection using Probability Cur- vature. ArXiv:2301.11305 [cs]. Edoardo Mosca, Mohamed Hesham Ibrahim Ab- dalla, Paolo Basso, Margherita Musumeci, and Georg Groh. 2023. Distinguishing fact from fiction: A benchmark dataset for identifying machine-generated scientific papers in the llm era. In Proceedings of the 3rd Workshop on Trustworthy Natural Language Processing (TrustNLP 2023), pages 190–207. Rithesh Murthy, Shelby Heinecke, Juan Carlos Niebles, Zhiwei Liu, Le Xue, Weiran Yao, Yi- hao Feng, Zeyuan Chen, Akash Gokul, Devansh Arpit, et al. 2023. Rex: Rapid exploration and exploitation for ai agents. arXiv preprint arXiv:2307.08962. Duke Nguyen, Khaing Myat Noe Naing, and Aditya Joshi. 2023. Stacking the odds: Transformer-based ensemble for ai-g
```

### Retrieved Chunk 2

- Source: `ASurvey of AI-generated Text Forensic Systems Detection Attribution and Characterization.pdf`
- Page: `2`
- Chunk ID: `430`
- Chunk Type: `main`
- Dense Score: `0.3126138746738434`
- Vector Score: `0.3126138746738434`
- BM25 Score: `unknown`
- Reranker Score: `unknown`

```text
LLMs. Consequently, post-hoc detection methods have gained prominence in AI-generated text foren- sics. Therefore, in the scope of our survey, we focus on post-hoc detection, further dividing it into supervised and zero-shot detection based on the training methodology employed. 2.2.2 Supervised Detectors Supervised detectors are trained using annotated datasets that consist of labeled human-written and AI-generated texts, aiming to identify distinctive features between human and AI-generated writ- ing. Initial efforts in AI-generated text detection em- ployed traditional techniques such as Bag-of-Words and TF-IDF encoding, coupled with classifiers like logistic regression, random forest, and SVC (Ip- polito et al., 2019; Jawahar et al., 2020). Subsequent research introduced advanced text sequence classi- fiers, including LSTM, GRU, and CNN, for detect- ing machine-generated text (Fagni e
```

### Retrieved Chunk 3

- Source: `ASurvey of AI-generated Text Forensic Systems Detection Attribution and Characterization.pdf`
- Page: `1`
- Chunk ID: `426`
- Chunk Type: `main`
- Dense Score: `0.3143196105957031`
- Vector Score: `0.3143196105957031`
- BM25 Score: `unknown`
- Reranker Score: `unknown`

```text
to organize the current work, identify gaps and future directions in this rapidly developing field. Our work facilitates the advancement of research in AI-generated text forensics, contributing to the development of more robust, transparent, and ac- countable digital information ecosystems. Related Surveys: Numerous surveys discuss as- pects of detection (Jawahar et al., 2020; Crothers et al., 2023; Tang et al., 2023) and attribu- tion (Uchendu et al., 2023) in isolated contexts. In contrast, the objective of our survey is to delineate the broad themes within the AI-generated foren- sics field by identifying its fundamental pillars, ex- ploring their interconnections, and discussing chal- lenges envisioning a future where AI-generated text becomes pervasive. 2 AI-generated Text Forensic Systems 2.1 AI-Generated Text In this survey, we define AI-generated text as out- put produced by a na
```

### Retrieved Chunk 4

- Source: `SeqXGPT Sentence-Level AI-Generated Text Detection.pdf`
- Page: `1`
- Chunk ID: `3398`
- Chunk Type: `main`
- Dense Score: `0.3295079171657562`
- Vector Score: `0.3295079171657562`
- BM25 Score: `unknown`
- Reranker Score: `unknown`

```text
existing methods, such as DetectGPT and Sniffer, fail to solve sentence-level AIGT detection. Our proposed SeqXGPT not only obtains promising results in both sentence and document-level AIGT detection challenges, but also exhibits excellent generalization on out-of-distribution datasets. 2 Background The proliferation of Large Language Models (LLMs) such as GPT-4 has given rise to increased concerns about the potential misuse of AI- generated texts (AIGT) (Brown et al., 2020; Zhang et al., 2022; Scao et al., 2022). This emphasizes the necessity for robust detection mechanisms to ensure security and trustworthiness of LLM applications. 2.1 Principal Approaches to AIGT Detection Broadly, AIGT detection methodologies fall into two primary categories: 1. Supervised Learning: This involves training models on labeled datasets to distinguish between human and AI-generated texts. Notable efforts
```

### Retrieved Chunk 5

- Source: `Ghostbuster Detecting Text Ghostwritten by Large Language Models.pdf`
- Page: `12`
- Chunk ID: `2442`
- Chunk Type: `main`
- Dense Score: `0.3323102295398712`
- Vector Score: `0.3323102295398712`
- BM25 Score: `unknown`
- Reranker Score: `unknown`

```text
a full document was AI-generated; and paragraph- level detection, detecting which paragraphs in a document were AI-generated. These tasks are motivated by real-world appli- cations of these detectors. For example, when questioning whether a student assignment was AI- generated, instructors often have access to previ- ous work by that student; document-level detec- tion may be useful when instructors do not have access to a history of student writing, or cannot verify that students did not include AI-generated text in previous assignments; and paragraph-level detection is useful when, as is often the case, AI assistance was only used for portions of the as- signment. Although the modeling work in the main body of our paper focuses only on document- level detection, we will release these additional benchmarks as a testbed for future work at https: //github.com/vivek3141/ghostbuster-data/ G
```

### Retrieved Chunk 6

- Source: `Ghostbuster Detecting Text Ghostwritten by Large Language Models.pdf`
- Page: `0`
- Chunk ID: `2380`
- Chunk Type: `main`
- Dense Score: `0.33417007327079773`
- Vector Score: `0.33417007327079773`
- BM25 Score: `unknown`
- Reranker Score: `unknown`

```text
datasets that they were not originally evaluated on (Section 6). In addition, the high false positive rates of these models raise potential ethical concerns be- cause they jeopardize students whose genuine work is misclassified as AI-generated. Furthermore, pre- vious work has indicated that text by non-native speakers of English is disproportionately flagged as AI-generated (Liang et al., 2023). These concerns underscore the need for AI-generated text detectors with strong generalization performance. We present Ghostbuster, a method for detection based on structured search and linear classification (Figure 1). First, Ghostbuster passes paired human- authored and AI-generated documents through a series of weaker language models, ranging from a unigram model to the non-instruction-tuned GPT-3 davinci. Given the word probabilities from these models, it then searches over a space of vector 
```

### Retrieved Chunk 7

- Source: `Ghostbuster Detecting Text Ghostwritten by Large Language Models.pdf`
- Page: `0`
- Chunk ID: `2377`
- Chunk Type: `main`
- Dense Score: `0.3349219262599945`
- Vector Score: `0.3349219262599945`
- BM25 Score: `unknown`
- Reranker Score: `unknown`

```text
Ghostbuster: Detecting Text Ghostwritten by Large Language Models Vivek Verma Eve Fleisig Nicholas Tomlin Dan Klein Computer Science Division, UC Berkeley {vivekverma, efleisig, nicholas_tomlin, klein}@berkeley.edu Abstract We introduce Ghostbuster, a state-of-the-art system for detecting AI-generated text. Our method works by passing documents through a series of weaker language models, running a structured search over possible combinations of their features, and then training a classifier on the selected features to predict whether docu- ments are AI-generated. Crucially, Ghostbuster does not require access to token probabilities from the target model, making it useful for de- tecting text generated by black-box or unknown models. In conjunction with our model, we release three new datasets of human- and AI- generated text as detection benchmarks in the domains of student essays, creat
```

### Retrieved Chunk 8

- Source: `SeqXGPT Sentence-Level AI-Generated Text Detection.pdf`
- Page: `0`
- Chunk ID: `3392`
- Chunk Type: `main`
- Dense Score: `0.33876076340675354`
- Vector Score: `0.33876076340675354`
- BM25 Score: `unknown`
- Reranker Score: `unknown`

```text
SeqXGPT: Sentence-Level AI-Generated Text Detection Pengyu Wang, Linyang Li , Ke Ren, Botian Jiang, Dong Zhang, Xipeng Qiu ∗ School of Computer Science, Fudan University Shanghai Key Laboratory of Intelligent Information Processing, Fudan University {pywang22,kren22,btjiang23,dongzhang22}@m.fudan.edu.cn {linyangli19,xpqiu}@fudan.edu.cn Abstract Widely applied large language models (LLMs) can generate human-like content, raising concerns about the abuse of LLMs. Therefore, it is important to build strong AI-generated text (AIGT) detectors. Current works only consider document-level AIGT detection, therefore, in this paper, we first introduce a sentence-level detection challenge by synthesizing a dataset that contains documents that are polished with LLMs, that is, the documents contain sentences written by humans and sentences modified by LLMs. Then we propose Sequence X (Check) GPT, a no
```


### BM25-only Retrieved Chunks

### Retrieved Chunk 1

- Source: `ASurvey of AI-generated Text Forensic Systems Detection Attribution and Characterization.pdf`
- Page: `7`
- Chunk ID: `460`
- Chunk Type: `main`
- Dense Score: `unknown`
- Vector Score: `unknown`
- BM25 Score: `15.3494901253937`
- Reranker Score: `unknown`

```text
Table 1 offers an overview of set of significant datasets used in AI-generated text forensics, as- sessed across several crucial dimensions, includ- ing the AI generators used, the domains of writ- ing, and performance metrics. These datasets fall into two main categories: general AI-generated text datasets (for detection and attribution purposes) and AI-misinformation datasets (for characterization). 3.1 Generators and Domains The datasets utilize a wide variety of generators, such as SCIgen, GPT models (GPT-2, GPT-3, GPT- 3.5), BLOOM, and more, across a broad set of do- mains from scientific papers to social-media posts and academic works. For instance, Facts from Fic- tion (Mosca et al., 2023) focuses on scientific papers, drawing on sources like arXiv, whereas AuTexTifica- tion (Sarvazyan et al., 2023a) covers domains such as tweets, reviews, and news articles. This diversity undersc
```

### Retrieved Chunk 2

- Source: `ASurvey of AI-generated Text Forensic Systems Detection Attribution and Characterization.pdf`
- Page: `0`
- Chunk ID: `421`
- Chunk Type: `main`
- Dense Score: `unknown`
- Vector Score: `unknown`
- BM25 Score: `13.49792296910123`
- Reranker Score: `unknown`

```text
content creation processes. However, these models introduce substantial challenges, particularly in the realm of information integrity. There is a growing concern over the potential misuse of LLMs for gen- erating and spreading misinformation, propaganda, and disinformation, thus undermining public trust and the foundations of democracy (Spitale et al., 2023; Goldstein et al., 2024). Addressing these concerns necessitates a fo- cused study of ‘AI-generated text forensics,’ an emerging field dedicated to developing methodolo- gies for analyzing, understanding, and mitigating the misuse of AI-generated text. This survey intro- duces the pillars of AI-generated text forensics as in Figure 1: (i) detection, (ii) attribution, and (iii) characterization—each serving a unique purpose in combating AI-generated content misuse. Detec- tion is pivotal for distinguishing between human and AI-generat
```

### Retrieved Chunk 3

- Source: `ASurvey of AI-generated Text Forensic Systems Detection Attribution and Characterization.pdf`
- Page: `2`
- Chunk ID: `430`
- Chunk Type: `main`
- Dense Score: `unknown`
- Vector Score: `unknown`
- BM25 Score: `13.406517717679826`
- Reranker Score: `unknown`

```text
LLMs. Consequently, post-hoc detection methods have gained prominence in AI-generated text foren- sics. Therefore, in the scope of our survey, we focus on post-hoc detection, further dividing it into supervised and zero-shot detection based on the training methodology employed. 2.2.2 Supervised Detectors Supervised detectors are trained using annotated datasets that consist of labeled human-written and AI-generated texts, aiming to identify distinctive features between human and AI-generated writ- ing. Initial efforts in AI-generated text detection em- ployed traditional techniques such as Bag-of-Words and TF-IDF encoding, coupled with classifiers like logistic regression, random forest, and SVC (Ip- polito et al., 2019; Jawahar et al., 2020). Subsequent research introduced advanced text sequence classi- fiers, including LSTM, GRU, and CNN, for detect- ing machine-generated text (Fagni e
```

### Retrieved Chunk 4

- Source: `Ghostbuster Detecting Text Ghostwritten by Large Language Models.pdf`
- Page: `12`
- Chunk ID: `2442`
- Chunk Type: `main`
- Dense Score: `unknown`
- Vector Score: `unknown`
- BM25 Score: `12.7279557405632`
- Reranker Score: `unknown`

```text
a full document was AI-generated; and paragraph- level detection, detecting which paragraphs in a document were AI-generated. These tasks are motivated by real-world appli- cations of these detectors. For example, when questioning whether a student assignment was AI- generated, instructors often have access to previ- ous work by that student; document-level detec- tion may be useful when instructors do not have access to a history of student writing, or cannot verify that students did not include AI-generated text in previous assignments; and paragraph-level detection is useful when, as is often the case, AI assistance was only used for portions of the as- signment. Although the modeling work in the main body of our paper focuses only on document- level detection, we will release these additional benchmarks as a testbed for future work at https: //github.com/vivek3141/ghostbuster-data/ G
```

### Retrieved Chunk 5

- Source: `Ghostbuster Detecting Text Ghostwritten by Large Language Models.pdf`
- Page: `2`
- Chunk ID: `2390`
- Chunk Type: `main`
- Dense Score: `unknown`
- Vector Score: `unknown`
- BM25 Score: `12.592422438546283`
- Reranker Score: `unknown`

```text
portionately misclassified as AI-generated by seven commercial GPT-generated text detectors. In Sec- tion 9, we discuss Ghostbuster’s performance on non-native English speaker data and other ethical considerations regarding detection models. 3 Datasets We collected three new datasets for benchmark- ing detection of AI-generated text across the do- mains of creative writing, news, and student es- says. For each of the three datasets, we col- lected ChatGPT-generated text corresponding to the human-authored text. All training datasets were generated using gpt-3.5-turbo. Our creative writing dataset is based on the sub- reddit r/WritingPrompts, a forum in which users share creative writing prompts and craft stories in response to these prompts. In order to avoid contamination from ChatGPT-written content, we collected data from the top 50 posters in October 2022 and scraped the last 100 pos
```

### Retrieved Chunk 6

- Source: `Ghostbuster Detecting Text Ghostwritten by Large Language Models.pdf`
- Page: `8`
- Chunk ID: `2423`
- Chunk Type: `main`
- Dense Score: `unknown`
- Vector Score: `unknown`
- BM25 Score: `12.256329355956666`
- Reranker Score: `unknown`

```text
Future work could examine tradeoffs between the false positive and false negative rates of AI- generated text detectors for different applications. For detection of AI-generated student essays, low- ering the risk of false positives is a key priority to avoid false accusations of student misconduct. In other settings, however, false positives are less concerning. For example, if detectors are used to prevent AI-generated text from being used in language model training data, or to flag poten- tially AI-generated content on the web, the ideal model calibration may differ. Other avenues for future work include improving robustness to per- turbations of AI-generated outputs, such as lightly editing to avoid detection, and different task formu- lations, including detection at the paragraph level for documents that combine human-authored and AI-generated text. Finally, future AI-generated text
```

### Retrieved Chunk 7

- Source: `Unsupervised and Distributional Detection of Machine-Generated Text.pdf`
- Page: `0`
- Chunk ID: `3659`
- Chunk Type: `main`
- Dense Score: `unknown`
- Vector Score: `unknown`
- BM25 Score: `11.537130104054466`
- Reranker Score: `unknown`

```text
used to generate fake documents,1 either news arti- cles (Zellers et al., 2019), comments (Yang et al., 2019) or other type of text (Buchanan et al., 2021) without revealing the non-human authorship of it. 1referring here to machine-generated text as opposed to text containing objectively false statements Figure 1: Histograms of the lengths of super-maximal repeats occurring in each dataset. textgen refers to human generated text. Recently, a number of papers have investigated the capacity of humans and learning algorithms to determine if a given text is human or machine generated (Ippolito et al., 2020; Dugan et al., 2020; Maronikolakis et al., 2020). However, so far all those methods are making two key assumptions: (i) the settings is framed in a supervised way for the machine learning methods, having access at train- ing time to machine-generated samples from the same generator; (ii) 
```

### Retrieved Chunk 8

- Source: `Unsupervised and Distributional Detection of Machine-Generated Text.pdf`
- Page: `8`
- Chunk ID: `3696`
- Chunk Type: `main`
- Dense Score: `unknown`
- Vector Score: `unknown`
- BM25 Score: `10.199998596926584`
- Reranker Score: `unknown`

```text
learners. arXiv preprint arXiv:2005.14165. Ben Buchanan, Andrew Lohn, Micah Musser, and Ka- terina Sedova. 2021. Truth, lies, and automation: How language models could change disinformation. Byung-Ju Choi, Jimin Hong, David Park, and Sang Wan Lee. 2020. Fˆ2-softmax: Diversifying neural text generation via frequency factorized soft- max. In Proceedings of the 2020 Conference on Empirical Methods in Natural Language Process- ing (EMNLP) , pages 9167–9182, Online. Associa- tion for Computational Linguistics. Elizabeth Clark, Tal August, Soﬁa Serrano, Nikita Haduong, Suchin Gururangan, and Noah A. Smith. 2021. All that’s ‘human’ is not gold: Evaluating human evaluation of generated text. In Proceed- ings of the 59th Annual Meeting of the Association for Computational Linguistics and the 11th Interna- tional Joint Conference on Natural Language Pro- cessing (V olume 1: Long Papers), pages 728
```


### Hybrid + Reranker Retrieved Chunks

### Retrieved Chunk 1

- Source: `ASurvey of AI-generated Text Forensic Systems Detection Attribution and Characterization.pdf`
- Page: `2`
- Chunk ID: `430`
- Chunk Type: `main`
- Dense Score: `unknown`
- Vector Score: `0.3126138746738434`
- BM25 Score: `13.406517717679826`
- Reranker Score: `5.634542465209961`

```text
LLMs. Consequently, post-hoc detection methods have gained prominence in AI-generated text foren- sics. Therefore, in the scope of our survey, we focus on post-hoc detection, further dividing it into supervised and zero-shot detection based on the training methodology employed. 2.2.2 Supervised Detectors Supervised detectors are trained using annotated datasets that consist of labeled human-written and AI-generated texts, aiming to identify distinctive features between human and AI-generated writ- ing. Initial efforts in AI-generated text detection em- ployed traditional techniques such as Bag-of-Words and TF-IDF encoding, coupled with classifiers like logistic regression, random forest, and SVC (Ip- polito et al., 2019; Jawahar et al., 2020). Subsequent research introduced advanced text sequence classi- fiers, including LSTM, GRU, and CNN, for detect- ing machine-generated text (Fagni e
```

### Retrieved Chunk 2

- Source: `SeqXGPT Sentence-Level AI-Generated Text Detection.pdf`
- Page: `0`
- Chunk ID: `3392`
- Chunk Type: `main`
- Dense Score: `unknown`
- Vector Score: `0.33876076340675354`
- BM25 Score: `9.174669325441254`
- Reranker Score: `5.61989688873291`

```text
SeqXGPT: Sentence-Level AI-Generated Text Detection Pengyu Wang, Linyang Li , Ke Ren, Botian Jiang, Dong Zhang, Xipeng Qiu ∗ School of Computer Science, Fudan University Shanghai Key Laboratory of Intelligent Information Processing, Fudan University {pywang22,kren22,btjiang23,dongzhang22}@m.fudan.edu.cn {linyangli19,xpqiu}@fudan.edu.cn Abstract Widely applied large language models (LLMs) can generate human-like content, raising concerns about the abuse of LLMs. Therefore, it is important to build strong AI-generated text (AIGT) detectors. Current works only consider document-level AIGT detection, therefore, in this paper, we first introduce a sentence-level detection challenge by synthesizing a dataset that contains documents that are polished with LLMs, that is, the documents contain sentences written by humans and sentences modified by LLMs. Then we propose Sequence X (Check) GPT, a no
```

### Retrieved Chunk 3

- Source: `ASurvey of AI-generated Text Forensic Systems Detection Attribution and Characterization.pdf`
- Page: `3`
- Chunk ID: `436`
- Chunk Type: `main`
- Dense Score: `unknown`
- Vector Score: `0.33706334233283997`
- BM25 Score: `unknown`
- Reranker Score: `5.505354881286621`

```text
tectors is their limited ability to generalize to novel AI generators. Various approaches have been ex- plored to mitigate this issue, focusing on develop- ing transferable techniques for AI-generated text detection. One such avenue involves integrating Energy-Based Models (EBMs) into the detection process (Bakhtin et al., 2019). This integration ex- ploits negative samples generated by multiple auto- regressive language models; specifically, the model assigns lower energy to human-generated text com- pared to text generated by AI models. Another strategy introduced by (Kushnareva et al., 2021a) utilizes Topological Data Analysis (TDA) on at- tention maps produced by transformer models to extract domain-invariant features for AI-generated text detection. This approach involves representing attention maps as weighted bipartite graphs, lever- aging TDA’s capability to capture both surface 
```

### Retrieved Chunk 4

- Source: `Ghostbuster Detecting Text Ghostwritten by Large Language Models.pdf`
- Page: `0`
- Chunk ID: `2380`
- Chunk Type: `main`
- Dense Score: `unknown`
- Vector Score: `0.33417007327079773`
- BM25 Score: `12.00118545728993`
- Reranker Score: `5.462650299072266`

```text
datasets that they were not originally evaluated on (Section 6). In addition, the high false positive rates of these models raise potential ethical concerns be- cause they jeopardize students whose genuine work is misclassified as AI-generated. Furthermore, pre- vious work has indicated that text by non-native speakers of English is disproportionately flagged as AI-generated (Liang et al., 2023). These concerns underscore the need for AI-generated text detectors with strong generalization performance. We present Ghostbuster, a method for detection based on structured search and linear classification (Figure 1). First, Ghostbuster passes paired human- authored and AI-generated documents through a series of weaker language models, ranging from a unigram model to the non-instruction-tuned GPT-3 davinci. Given the word probabilities from these models, it then searches over a space of vector 
```

### Retrieved Chunk 5

- Source: `Ghostbuster Detecting Text Ghostwritten by Large Language Models.pdf`
- Page: `2`
- Chunk ID: `2390`
- Chunk Type: `main`
- Dense Score: `unknown`
- Vector Score: `unknown`
- BM25 Score: `12.592422438546283`
- Reranker Score: `5.280979156494141`

```text
portionately misclassified as AI-generated by seven commercial GPT-generated text detectors. In Sec- tion 9, we discuss Ghostbuster’s performance on non-native English speaker data and other ethical considerations regarding detection models. 3 Datasets We collected three new datasets for benchmark- ing detection of AI-generated text across the do- mains of creative writing, news, and student es- says. For each of the three datasets, we col- lected ChatGPT-generated text corresponding to the human-authored text. All training datasets were generated using gpt-3.5-turbo. Our creative writing dataset is based on the sub- reddit r/WritingPrompts, a forum in which users share creative writing prompts and craft stories in response to these prompts. In order to avoid contamination from ChatGPT-written content, we collected data from the top 50 posters in October 2022 and scraped the last 100 pos
```

### Retrieved Chunk 6

- Source: `SeqXGPT Sentence-Level AI-Generated Text Detection.pdf`
- Page: `1`
- Chunk ID: `3398`
- Chunk Type: `main`
- Dense Score: `unknown`
- Vector Score: `0.3295079171657562`
- BM25 Score: `unknown`
- Reranker Score: `5.27540397644043`

```text
existing methods, such as DetectGPT and Sniffer, fail to solve sentence-level AIGT detection. Our proposed SeqXGPT not only obtains promising results in both sentence and document-level AIGT detection challenges, but also exhibits excellent generalization on out-of-distribution datasets. 2 Background The proliferation of Large Language Models (LLMs) such as GPT-4 has given rise to increased concerns about the potential misuse of AI- generated texts (AIGT) (Brown et al., 2020; Zhang et al., 2022; Scao et al., 2022). This emphasizes the necessity for robust detection mechanisms to ensure security and trustworthiness of LLM applications. 2.1 Principal Approaches to AIGT Detection Broadly, AIGT detection methodologies fall into two primary categories: 1. Supervised Learning: This involves training models on labeled datasets to distinguish between human and AI-generated texts. Notable efforts
```

### Retrieved Chunk 7

- Source: `ASurvey of AI-generated Text Forensic Systems Detection Attribution and Characterization.pdf`
- Page: `0`
- Chunk ID: `419`
- Chunk Type: `main`
- Dense Score: `unknown`
- Vector Score: `0.3390544056892395`
- BM25 Score: `12.58639807148704`
- Reranker Score: `5.121118068695068`

```text
ing the challenges of LLM misuses. We present an overview of the existing efforts in AI-generated text forensics by introducing a detailed taxonomy, focusing on three pri- mary pillars: detection, attribution, and char- acterization. These pillars enable a practi- cal understanding of AI-generated text, from identifying AI-generated content (detection), determining the specific AI model involved (attribution), and grouping the underlying intents of the text (characterization). Further- more, we explore available resources for AI- generated text forensics research and discuss the evolving challenges and future directions of forensic systems in an AI era. 1 Introduction The advent of Large Language Models (LLMs) like GPT-4 (OpenAI, 2023), Gemini (Team et al., 2023), and open-source variants such as Falcon (Al- mazrouei et al., 2023) and Llama 1&2 (Touvron et al., 2023), has significantly e
```

### Retrieved Chunk 8

- Source: `SeqXGPT Sentence-Level AI-Generated Text Detection.pdf`
- Page: `0`
- Chunk ID: `3395`
- Chunk Type: `main`
- Dense Score: `unknown`
- Vector Score: `0.3651220202445984`
- BM25 Score: `unknown`
- Reranker Score: `5.0298662185668945`

```text
can efficiently conduct sentence-level AIGT detection. given text is written or modified by an AI system (Mitchell et al., 2023; Li et al., 2023). Current AIGT detection strategies, such as supervised-learned discriminator 2, perplexity- based methods (Mitchell et al., 2023; Li et al., 2023), etc., focus on discriminating whether a whole document is generated by an AI. However, users often modify partial texts with LLMs rather than put full trust in LLMs to generate a whole document. Therefore, it is important to explore fine-grained (e.g. sentence-level) AIGT detection. Building methods that solve the sentence-level AIGT detection challenge is not an incremental modification over document-level AIGT detection. On the one hand, model-wise methods like DetectGPT and Sniffer require a rather long document as input (over 100 tokens), making 2https://github.com/openai/ gpt-2-output-dataset a
```


### Manual Judgment

Please inspect the retrieved chunks and fill in:

- Which setting retrieves the most useful chunks?
- Does BM25 help with method names, abbreviations, or technical terms?
- Does dense retrieval help with semantic but non-exact matches?
- Does hybrid + reranker combine the advantages of both?
- Does hybrid retrieval reduce or increase noise?
- Overall winner: Dense only / BM25 only / Hybrid + reranker / Tie

---

## Specific AdaDetectGPT query

### Question

How does AdaDetectGPT work?

### Retrieval Modes

- Dense-only mode: `global`
- BM25-only mode: `global`
- Hybrid mode: `global`

### Candidate Papers

These should usually be similar because all three settings use the same paper-level routing.

#### Hybrid Candidate Papers

1. `AdaDetectGPT Adaptive Detection of LLM-Generated Text with Statistical Guarantees.pdf`
   - Title: AdaDetectGPT: Adaptive Detection of LLM-Generated Text with Statistical Guarantees
   - Paper score: `0.6034888029098511`

2. `DetectGPT-SC Improving Detection of Text Generated by Large Language Models through Self-Consistency with Masked Predictions.pdf`
   - Title: DetectGPT SC Improving Detection of Text Generated by Large Language Models through Self Consistency with Masked Predictions
   - Paper score: `0.7163678407669067`

3. `DetectGPT Zero-Shot Machine-Generated Text Detection using Probability Curvature.pdf`
   - Title: DetectGPT: Zero-Shot Machine-Generated Text Detection using Probability Curvature
   - Paper score: `0.7181804180145264`

4. `Fast-DetectGPT Efficient Zero-Shot Detection of Machine-Generated Text via Conditional Probability Curvature.pdf`
   - Title: Fast DetectGPT Efficient Zero Shot Detection of Machine Generated Text via Conditional Probability Curvature
   - Paper score: `0.731763482093811`


### Selected Papers

#### Dense-only Selected Papers

1. `AdaDetectGPT Adaptive Detection of LLM-Generated Text with Statistical Guarantees.pdf`
   - Title: AdaDetectGPT: Adaptive Detection of LLM-Generated Text with Statistical Guarantees
   - Paper score: `0.6034888029098511`

2. `DetectGPT-SC Improving Detection of Text Generated by Large Language Models through Self-Consistency with Masked Predictions.pdf`
   - Title: DetectGPT SC Improving Detection of Text Generated by Large Language Models through Self Consistency with Masked Predictions
   - Paper score: `0.7163678407669067`

3. `DetectGPT Zero-Shot Machine-Generated Text Detection using Probability Curvature.pdf`
   - Title: DetectGPT: Zero-Shot Machine-Generated Text Detection using Probability Curvature
   - Paper score: `0.7181804180145264`

4. `Fast-DetectGPT Efficient Zero-Shot Detection of Machine-Generated Text via Conditional Probability Curvature.pdf`
   - Title: Fast DetectGPT Efficient Zero Shot Detection of Machine Generated Text via Conditional Probability Curvature
   - Paper score: `0.731763482093811`


#### BM25-only Selected Papers

1. `AdaDetectGPT Adaptive Detection of LLM-Generated Text with Statistical Guarantees.pdf`
   - Title: AdaDetectGPT: Adaptive Detection of LLM-Generated Text with Statistical Guarantees
   - Paper score: `0.6034888029098511`

2. `DetectGPT-SC Improving Detection of Text Generated by Large Language Models through Self-Consistency with Masked Predictions.pdf`
   - Title: DetectGPT SC Improving Detection of Text Generated by Large Language Models through Self Consistency with Masked Predictions
   - Paper score: `0.7163678407669067`

3. `DetectGPT Zero-Shot Machine-Generated Text Detection using Probability Curvature.pdf`
   - Title: DetectGPT: Zero-Shot Machine-Generated Text Detection using Probability Curvature
   - Paper score: `0.7181804180145264`

4. `Fast-DetectGPT Efficient Zero-Shot Detection of Machine-Generated Text via Conditional Probability Curvature.pdf`
   - Title: Fast DetectGPT Efficient Zero Shot Detection of Machine Generated Text via Conditional Probability Curvature
   - Paper score: `0.731763482093811`


#### Hybrid Selected Papers

1. `AdaDetectGPT Adaptive Detection of LLM-Generated Text with Statistical Guarantees.pdf`
   - Title: AdaDetectGPT: Adaptive Detection of LLM-Generated Text with Statistical Guarantees
   - Paper score: `0.6034888029098511`

2. `DetectGPT-SC Improving Detection of Text Generated by Large Language Models through Self-Consistency with Masked Predictions.pdf`
   - Title: DetectGPT SC Improving Detection of Text Generated by Large Language Models through Self Consistency with Masked Predictions
   - Paper score: `0.7163678407669067`

3. `DetectGPT Zero-Shot Machine-Generated Text Detection using Probability Curvature.pdf`
   - Title: DetectGPT: Zero-Shot Machine-Generated Text Detection using Probability Curvature
   - Paper score: `0.7181804180145264`

4. `Fast-DetectGPT Efficient Zero-Shot Detection of Machine-Generated Text via Conditional Probability Curvature.pdf`
   - Title: Fast DetectGPT Efficient Zero Shot Detection of Machine Generated Text via Conditional Probability Curvature
   - Paper score: `0.731763482093811`


### Summary Statistics

| Metric | Dense only | BM25 only | Hybrid + reranker |
|---|---:|---:|---:|
| Retrieved chunks | 8 | 8 | 8 |
| Unique sources | 3 | 3 | 3 |
| Noisy chunks | 0 | 0 | 0 |
| Overlap with hybrid | 1 | 2 | 8 |

### Source Distribution

#### Dense only

- `AdaDetectGPT Adaptive Detection of LLM-Generated Text with Statistical Guarantees.pdf`: 3 chunks
- `Fast-DetectGPT Efficient Zero-Shot Detection of Machine-Generated Text via Conditional Probability Curvature.pdf`: 3 chunks
- `DetectGPT Zero-Shot Machine-Generated Text Detection using Probability Curvature.pdf`: 2 chunks

#### BM25 only

- `AdaDetectGPT Adaptive Detection of LLM-Generated Text with Statistical Guarantees.pdf`: 3 chunks
- `DetectGPT Zero-Shot Machine-Generated Text Detection using Probability Curvature.pdf`: 3 chunks
- `DetectGPT-SC Improving Detection of Text Generated by Large Language Models through Self-Consistency with Masked Predictions.pdf`: 2 chunks

#### Hybrid + reranker

- `AdaDetectGPT Adaptive Detection of LLM-Generated Text with Statistical Guarantees.pdf`: 6 chunks
- `Fast-DetectGPT Efficient Zero-Shot Detection of Machine-Generated Text via Conditional Probability Curvature.pdf`: 1 chunks
- `DetectGPT Zero-Shot Machine-Generated Text Detection using Probability Curvature.pdf`: 1 chunks

### Dense-only Retrieved Chunks

### Retrieved Chunk 1

- Source: `AdaDetectGPT Adaptive Detection of LLM-Generated Text with Statistical Guarantees.pdf`
- Page: `9`
- Chunk ID: `255`
- Chunk Type: `main`
- Dense Score: `0.4194706678390503`
- Vector Score: `0.4194706678390503`
- BM25 Score: `unknown`
- Reranker Score: `unknown`

```text
Fast-DetectGPT 0.9048 0.95880.98470.9800 0.9571 0.9019 0.93610.97680.9608 0.9439 AdaDetectGPT 0.90720.96110.98320.9841 0.95890.91760.94000.97280.9610 0.9478 Relative ( ) 2.4288 5.6095 — 20.4444 4.2454 16.0326 6.0543 — 0.3405 6.9929 Table 3: Detection of LLM-generated text under two adversarial attacks in black-box settings. Paraphrasing Decoherence DetectGPT Xsum Writing PubMed Avg. Xsum Writing PubMed Avg. Fast (GPT-J/GPT-2) 0.91780.91370.7944 0.8753 0.7884 0.9595 0.7870 0.8449 Ada (GPT-J/GPT-2)0.92250.91210.8029 0.8792 0.8765 0.9597 0.8284 0.8882 Fast (GPT-J/Neo-2.7) 0.96020.91850.7310 0.8699 0.8579 0.9701 0.7609 0.8630 Ada (GPT-J/Neo-2.7)0.96230.91810.7587 0.8797 0.9230 0.9704 0.8124 0.9019 Fast (GPT-J/GPT-J) 0.95370.94580.7041 0.8679 0.88360.98690.7550 0.8752 Ada (GPT-J/GPT-J)0.95870.94490.7308 0.8781 0.93360.98640.8008 0.9070 underperforms Binoculars or RADAR. Nonetheless, AdaDetect
```

### Retrieved Chunk 2

- Source: `AdaDetectGPT Adaptive Detection of LLM-Generated Text with Statistical Guarantees.pdf`
- Page: `9`
- Chunk ID: `256`
- Chunk Type: `main`
- Dense Score: `0.44804322719573975`
- Vector Score: `0.44804322719573975`
- BM25 Score: `unknown`
- Reranker Score: `unknown`

```text
underperforms Binoculars or RADAR. Nonetheless, AdaDetectGPT consistently improves upon Fast-DetectGPT across various datasets, with gains on Essay reaching up to 37.8%. Additionally, we evaluate AdaDetectGPT’s robustness to two adversarial attacks, paraphrasing and decoherence, in the black-box setting. As shown in Table 3, AdaDetectGPT demonstrates greater resilience than Fast-DetectGPT to adversarially perturbed texts. The improvement reaches up to 10% for paraphrasing and up to 85% for decoherence. Finally, we employ the same five LLMs from Table 1 to compare Fast-DetectGPT and AdaDetectGPT in black-box settings. Following Bao et al. (2024), we use GPT-J as the source LLM for detecting each of the remaining four target LLMs. Due to space constraints, the results are presented in Table S11 of Appendix F.5, where AdaDetectGPT uniformly outperforms Fast-DetectGPT in all cases, with impr
```

### Retrieved Chunk 3

- Source: `AdaDetectGPT Adaptive Detection of LLM-Generated Text with Statistical Guarantees.pdf`
- Page: `8`
- Chunk ID: `251`
- Chunk Type: `main`
- Dense Score: `0.452589750289917`
- Vector Score: `0.452589750289917`
- BM25 Score: `unknown`
- Reranker Score: `unknown`

```text
AdaDetectGPT0.8534 0.8420 0.8532 0.8347 0.8061 0.8379 Relative ( ) 14.1250 18.2659 21.1936 20.3301 18.4492 18.5779 reports the AUC scores of various detectors across all combinations of datasets and five source models. It can be seen that AdaDetectGPT achieves the highest AUC across all combinations of datasets and source models, outperforming Fast-DetectGPT – the best baseline method – by 12.5%-37%. We also evaluate AdaDetectGPT on three more advanced open-source LLMs: Qwen2.5 (Bai et al., 2025), Mistral (Jiang et al., 2023), and LLaMA3 (Grattafiori et al., 2024). As shown in Table S7, AdaDetectGPT delivers consistent improvements over Fast-DetectGPT and maintains competitive performance across five datasets, achieving the best results in most cases. These findings highlight the advantage of using an adaptively learned witness function for classification. In Appendix F.3, we analyze the
```

### Retrieved Chunk 4

- Source: `Fast-DetectGPT Efficient Zero-Shot Detection of Machine-Generated Text via Conditional Probability Curvature.pdf`
- Page: `20`
- Chunk ID: `2293`
- Chunk Type: `main`
- Dense Score: `0.5600500106811523`
- Vector Score: `0.5600500106811523`
- BM25 Score: `unknown`
- Reranker Score: `unknown`

```text
DetectGPT .9875 .9793 .9961 .9762 .95 .9869 .9707 .9919 .9619 .9424 .9928 .9856 .9953 .979 .9622 Fast-DetectGPT .9994 .9965 .9988 .997 .9958 .9954 .9867 .9938 .9826 .9773 .9999 .9999 .9997 .9999 .9997 (Diff) .0119 .0172 .0028 .0208 .0458 .0085 .0160 .0018 .0207 .0349 .0071 .0143 .0044 .0209 .0376 DetectGPT(fixed) .9399 .9438 .9961 .9367 .9214 .9143 .9026 .9919 .8846 .8854 .9722 .9635 .9953 .9627 .9646 Fast-Detect(fixed) .9953 .9861 .9997 .9856 .9779 .9805 .9613 .9979 .9499 .9311 .9978 .999 .9999 .9991 .998 (Diff) .0554 .0423 .0036 .0489 .0565 .0662 .0587 .0060 .0654 .0457 .0256 .0355 .0046 .0364 .0333 SQuAD Likelihood .961 .944 .9214 .8838 .8122 .9393 .9072 .8926 .8351 .7317 .9906 .987 .9792 .9572 .9094 Entropy .5369 .4736 .539 .5277 .5593 .552 .5203 .5457 .5441 .5992 .5132 .4508 .4924 .4882 .5263 LogRank .9792 .9657 .9535 .9156 .8482 .9692 .9423 .9385 .8842 .7895 .9972 .9959 .994 .9798 
```

### Retrieved Chunk 5

- Source: `Fast-DetectGPT Efficient Zero-Shot Detection of Machine-Generated Text via Conditional Probability Curvature.pdf`
- Page: `21`
- Chunk ID: `2297`
- Chunk Type: `main`
- Dense Score: `0.5744954347610474`
- Vector Score: `0.5744954347610474`
- BM25 Score: `unknown`
- Reranker Score: `unknown`

```text
Published as a conference paper at ICLR 2024 used in Table 2, sampling with the three strategies with k = 40 , p = 0 .96, and T = 0 .8. Fast- DetectGPT in the white-box setting obtains the best accuracy on the three sampling strategies, out- performing DetectGPT by relative 95% on Top- p sampling, relative 81% on Top- k sampling, and relative 99% on sampling with a temperature, as shown in Table 9. In the black-box setting, Fast- DetectGPT outperforms DetectGPT by relatively 92%, 80%, and 98% on the three decoding strate- gies, respectively. These results demonstrate that Fast-DetectGPT works consistently in detecting texts produced by different decoding strategies. To elucidate the trajectory of detection accuracy concerning variations in sampling hyper- parameters, we conducted additional experiments with values set top = 0.90, k = 30, and T = 0.6. As indicated in the lower segment of 
```

### Retrieved Chunk 6

- Source: `Fast-DetectGPT Efficient Zero-Shot Detection of Machine-Generated Text via Conditional Probability Curvature.pdf`
- Page: `5`
- Chunk ID: `2227`
- Chunk Type: `main`
- Dense Score: `0.576409101486206`
- Vector Score: `0.576409101486206`
- BM25 Score: `unknown`
- Reranker Score: `unknown`

```text
experiments, measuring the detection accuracy in AUROC (see Appendix A). Inference Speedup. We compare the inference time (excluding the time for initializing the model) of Fast-DetectGPT and DetectGPT on a Tesla A100 GPU using XSum generations from the five models in Table 2. Despite DetectGPT’s use of GPU batch processing, splitting 100 perturbations into 10 batches, it still requires substantial computational resources. It totals 79,113 seconds (ap- proximately 22 hours) over five runs. In contrast, Fast-DetectGPT completes the task in only 233 seconds (about 4 minutes), achieving a remarkable speedup factor of approximately 340x, highlight- ing its significant performance improvement. White-Box Zero-Shot Machine-Generated Text Detection. We evaluate zero-shot methods us- ing each source model for scoring and typically Fast-DetectGPT using the source model also for sampling. The avera
```

### Retrieved Chunk 7

- Source: `DetectGPT Zero-Shot Machine-Generated Text Detection using Probability Curvature.pdf`
- Page: `6`
- Chunk ID: `1474`
- Chunk Type: `main`
- Dense Score: `0.61167973279953`
- Vector Score: `0.61167973279953`
- BM25 Score: `unknown`
- Reranker Score: `unknown`

```text
tectGPT maintains detection AUROC above 0.8 even when nearly a quarter of the text in model samples has been re- placed. Unsurprisingly, almost all methods show a gradual degradation in performance as the sample is more heavily revised. The entropy baseline shows surprisingly robust performance in this setting (althought it is least accurate on average), even slightly improving detection performance up to 24% replacement. DetectGPT shows the strongest detection performance for all revision levels. Impact of alternative decoding strategies on detection. While Table 1 suggests that DetectGPT is effective for 5We reduce the number of evaluation samples from 500 in our main experiments to reduce the API costs of these experiments. XSum SQuAD WritingPrompts Method top- p top-k top-p top-k top-p top-k log p(x) 0.92 0.87 0.89 0.85 0.98 0.96 Rank 0.76 0.76 0.81 0.80 0.84 0.83 LogRank 0.93* 0.90*
```

### Retrieved Chunk 8

- Source: `DetectGPT Zero-Shot Machine-Generated Text Detection using Probability Curvature.pdf`
- Page: `7`
- Chunk ID: `1482`
- Chunk Type: `main`
- Dense Score: `0.6181098818778992`
- Vector Score: `0.6181098818778992`
- BM25 Score: `unknown`
- Reranker Score: `unknown`

```text
ples. A threshold of slightly below 0.1 separates human and model texts across data distributions, which is important for practical scenarios in which a passage may be analyzed with- out knowing its domain a priori. Finally, Figure 10 shows an analysis of DetectGPT’s performance as a function of pas- sage length. We bin the paired human- and model-generated sequences by their average length into three bins of equal size (bottom/middle/top third), and plot the AUROC within each bin. The relationship between detection performance and passage length generally depends on the dataset and model (or tokenizer). For very long sequences, DetectGPT may see reduced performance because our implementation of DetectGPT applies all T5 mask-filling perturbations at once, and T5 may fail to track many mask tokens at once. By applying perturbations in multiple sequential rounds of smaller numbers of masks
```


### BM25-only Retrieved Chunks

### Retrieved Chunk 1

- Source: `AdaDetectGPT Adaptive Detection of LLM-Generated Text with Statistical Guarantees.pdf`
- Page: `16`
- Chunk ID: `288`
- Chunk Type: `main`
- Dense Score: `unknown`
- Vector Score: `unknown`
- BM25 Score: `9.961621198223394`
- Reranker Score: `unknown`

```text
• It is fine to include aspirational goals as motivation as long as it is clear that these goals are not attained by the paper. 2.Limitations Question: Does the paper discuss the limitations of the work performed by the authors? Answer: [Yes] Justification: We discuss the limitation of the work in Appendix G. Guidelines: • The answer NA means that the paper has no limitation while the answer No means that the paper has limitations, but those are not discussed in the paper. • The authors are encouraged to create a separate "Limitations" section in their paper. • The paper should point out any strong assumptions and how robust the results are to violations of these assumptions (e.g., independence assumptions, noiseless settings, model well-specification, asymptotic approximations only holding locally). The authors should reflect on how these assumptions might be violated in practice and wh
```

### Retrieved Chunk 2

- Source: `AdaDetectGPT Adaptive Detection of LLM-Generated Text with Statistical Guarantees.pdf`
- Page: `1`
- Chunk ID: `215`
- Chunk Type: `main`
- Dense Score: `unknown`
- Vector Score: `unknown`
- BM25 Score: `8.959452228291966`
- Reranker Score: `unknown`

```text
compute the logits – AdaDetectGPT achieves improvements over the best alternative in area under the curve (AUC) ranging from 12.5% to 37%. In black-box settings, where the source and target LLMs differ, it similarly offer gains of up to 20%. Theoretically, we provide statistical performance guarantees for AdaDetectGPT, deriving finite- sample error bounds for its TNR, FNR, true positive rate (TPR) and false positive rate (FPR). Existing literature on logits-based detectors generally lacks systematic statistical analysis. Our work aims to fill in this gap and contribute toward a deeper understanding of these methods in this emerging field, by offering a comprehensive analysis based on the aforementioned standard classification metrics. 1.1 Related works Existing methods for detecting machine-generated text generally fall into three categories: machine learning (ML)-based, statistics-based
```

### Retrieved Chunk 3

- Source: `AdaDetectGPT Adaptive Detection of LLM-Generated Text with Statistical Guarantees.pdf`
- Page: `4`
- Chunk ID: `229`
- Chunk Type: `main`
- Dense Score: `unknown`
- Vector Score: `unknown`
- BM25 Score: `8.897424839812748`
- Reranker Score: `unknown`

```text
0 1 2 3 Differences in statistical measures 0 1 FastDetectGPT AdaDetectGPT Dataset: SQuAD 1  0 1 2 3 4 Differences in statistical measures 0 1 FastDetectGPT AdaDetectGPT Dataset: Writing Figure 2: Boxplots visualizing the differences in the statistical measures between human- and LLM- authored passages, comparing AdaDetectGPT (with a learned witness function) and Fast-DetectGPT (without it). A larger positive difference from zero indicates better detection power. As observed, the difference computed by AdaDetectGPT is consistently larger than that of Fast-DetectGPT across the first quartile, median, and third quartile. The left panel shows statistics evaluated on the SQuAD dataset, while the right panel displays results for the WritingPrompts dataset. function. Next, in Part (d), we extend our proposal to the black-box setting. Finally, in Part (e), we establish the statistical propertie
```

### Retrieved Chunk 4

- Source: `DetectGPT Zero-Shot Machine-Generated Text Detection using Probability Curvature.pdf`
- Page: `8`
- Chunk ID: `1488`
- Chunk Type: `main`
- Dense Score: `unknown`
- Vector Score: `unknown`
- BM25 Score: `6.7851942060925765`
- Reranker Score: `unknown`

```text
each candidate passage, rather than just the candidate pas- sage; a better tuned perturbation function or more efficient curvature approximation may help mitigate these costs. Future Work. While the methods in this work make no assumptions about the models generating the samples, fu- ture work may explore how watermarking algorithms can be used in conjunction with detection algorithms like Detect- GPT to further improve detection robustness as language models continually improve their reproductions of human text. Separately, the results in Section 5.2 suggest that ex- tending DetectGPT to use ensembles of models for scoring, rather than a single model, may improve detection in the black box setting. Another topic that remains unexplored is the relationship between prompting and detection; that is, can a clever prompt successfully prevent a model’s gen- erations from being detected by exi
```

### Retrieved Chunk 5

- Source: `DetectGPT Zero-Shot Machine-Generated Text Detection using Probability Curvature.pdf`
- Page: `2`
- Chunk ID: `1445`
- Chunk Type: `main`
- Dense Score: `unknown`
- Vector Score: `unknown`
- BM25 Score: `6.7454281321213605`
- Reranker Score: `unknown`

```text
Zero-Shot Machine-Generated Text Detection using Probability Curvature generated text detection. Other work explores watermarks for generated text (Kirchenbauer et al., 2023), which modify a model’s generations to make them easier to detect. Our work does not assume text is generated with the goal of easy detection; DetectGPT detects text generated from publicly available LLMs using standard LLM sampling strategies. The widespread use of LLMs has led to much other con- temporaneous work on detecting LLM output. Sadasivan et al. (2023) show that the detection AUROC of the an de- tector is upper bounded by a function of the TV distance between the model and human text. However, we find that AUROC of DetectGPT is high even for the largest publicly- available models (Table 2), suggesting that TV distance may not correlate strongly with model scale and capability. This disconnect may be exace
```

### Retrieved Chunk 6

- Source: `DetectGPT-SC Improving Detection of Text Generated by Large Language Models through Self-Consistency with Masked Predictions.pdf`
- Page: `2`
- Chunk ID: `1518`
- Chunk Type: `main`
- Dense Score: `unknown`
- Vector Score: `unknown`
- BM25 Score: `6.239507027831058`
- Reranker Score: `unknown`

```text
incurs the cost of training these classifier models. Statistical-based detectors. Statistical-based detectors utilize statistical metrics such as entropy, perplexity, andn-gram frequency to differentiate between human-generated and AI-generated texts [1]. Some other work is based on watermark-based detectors. In previous research, watermarks have been applied in the field of image processing and computer vision to protect copyrighted content and prevent intellectual property theft [6]. Recently, with the emergence of ChatGPT, the work by Kirchenbauer et al. [ 7] demonstrated how to incorporate a watermark using only the logarithmic credentials of each step to mark AI-generated texts. While watermark-based detectors are an intriguing area of research, adding watermarks may affect the readability of the texts, and the removal of watermarks is also a challenge we need to address.
```

### Retrieved Chunk 7

- Source: `DetectGPT-SC Improving Detection of Text Generated by Large Language Models through Self-Consistency with Masked Predictions.pdf`
- Page: `6`
- Chunk ID: `1535`
- Chunk Type: `main`
- Dense Score: `unknown`
- Vector Score: `unknown`
- BM25 Score: `5.169509146528552`
- Reranker Score: `unknown`

```text
Running Title for Header masked prediction of text generated by large language models. Experimental results demonstrate that DetectGPT-SC achieves higher accuracy and efficiency compared to current state-of-the-art text detector. It does not rely on complex classifiers or extensive training data. We hope that our work will provide a valuable starting point for future research and inspire further exploration of the potential of self-consistency in language models for text detection. References [1] S. Gehrmann, H. Strobelt, and A. M. Rush, “Gltr: Statistical detection and visualization of generated text,” arXiv preprint arXiv:1906.04043, 2019. [2] I. Solaiman, M. Brundage, J. Clark, A. Askell, A. Herbert-V oss, J. Wu, A. Radford, G. Krueger, J. W. Kim, S. Kreps et al., “Release strategies and the social impacts of language models,”arXiv preprint arXiv:1908.09203, 2019. [3] S. Chakraborty, 
```

### Retrieved Chunk 8

- Source: `DetectGPT Zero-Shot Machine-Generated Text Detection using Probability Curvature.pdf`
- Page: `8`
- Chunk ID: `1489`
- Chunk Type: `main`
- Dense Score: `unknown`
- Vector Score: `unknown`
- BM25 Score: `4.595443475676008`
- Reranker Score: `unknown`

```text
erations from being detected by existing methods? Finally, future work may explore whether the local log probabil- ity curvature property we identify is present for generative models in other domains, such as audio, video, or images. We hope that the present work serves as inspiration to fu- ture work developing effective, general-purpose methods for mitigating potential harms of machine-generated media. Acknowledgements EM gratefully acknowledges funding from a Knight- Hennessy Graduate Fellowship. CF and CM are CIFAR Fellows. The Stanford Center for Research on Foundation Models (CRFM) provided part of the compute resources used for the experiments in this work. 9
```


### Hybrid + Reranker Retrieved Chunks

### Retrieved Chunk 1

- Source: `AdaDetectGPT Adaptive Detection of LLM-Generated Text with Statistical Guarantees.pdf`
- Page: `1`
- Chunk ID: `213`
- Chunk Type: `main`
- Dense Score: `unknown`
- Vector Score: `0.4809427261352539`
- BM25 Score: `unknown`
- Reranker Score: `6.063632011413574`

```text
Figure 1: Workflow of AdaDetectGPT. Built upon Fast-DetectGPT (Bao et al., 2024), our method adaptively learn a witness functionbwfrom training data by maximizing a lower bound on the TNR, while using normal approximation for FNR control. probability outputs (i.e., logits) from a source LLM to construct the statistics for classification (see e.g., Gehrmann et al., 2019; Mitchell et al., 2023). These works are motivated by the empirical observation that LLM-generated text tends to exhibit higher log-probabilities or larger differences between the logits of original and perturbed tokens. However, as we demonstrated in Section 3, relying solely on the logits can be sub-optimal for detecting LLM-generated text. Our contribution. In this paper, we propose AdaDetectGPT (see Figure 1 for a visualization), an adaptive LLM detector that leverages external training data to enhance the effectivenes
```

### Retrieved Chunk 2

- Source: `AdaDetectGPT Adaptive Detection of LLM-Generated Text with Statistical Guarantees.pdf`
- Page: `41`
- Chunk ID: `368`
- Chunk Type: `main`
- Dense Score: `unknown`
- Vector Score: `0.4973980784416199`
- BM25 Score: `unknown`
- Reranker Score: `5.962424278259277`

```text
G Broader impact and limitation AdaDetectGPT is a computationally and statistically efficient detector for machine-generated text, thus safeguarding AI systems against fake news, disinformation, and academic plagiarism. Despite AdaDetectGPT’s strong empirical performance in the black-box setting, its theoretical guarantees are mainly established in the white-box setting. Even when restricting to the white-box setting, LLM text generation often involves sampling parameters (e.g., temperature and top_k). Using different parameter values can cause the sampling distribution to deviate from that of the target model we aim to detect. This mismatch invalidates MCLT in practice. Fortunately, we observe that the shape of our statistic remains similar, but shifts toward a positive mean (see Figure S8), implying that FNR control under MCLT remains valid, although being more conservative. 4  2  0 2 
```

### Retrieved Chunk 3

- Source: `AdaDetectGPT Adaptive Detection of LLM-Generated Text with Statistical Guarantees.pdf`
- Page: `0`
- Chunk ID: `210`
- Chunk Type: `main`
- Dense Score: `unknown`
- Vector Score: `unknown`
- BM25 Score: `7.728740112323405`
- Reranker Score: `5.667010307312012`

```text
text evaluated using the distribution function of a given source LLM. However, relying solely on log probabilities can be sub-optimal. In response, we introduce AdaDetectGPT – a novel classifier that adaptively learns a witness function from training data to enhance the performance of logits-based detectors. We provide statistical guarantees on its true positive rate, false positive rate, true negative rate and false negative rate. Extensive numerical studies show AdaDetectGPT nearly uniformly improves the state-of-the-art method in various combination of datasets and LLMs, and the improvement can reach up to 37%. A python implementation of our method is available athttps://github.com/Mamba413/AdaDetectGPT. 1 Introduction Large language models (LLMs) such as ChatGPT (OpenAI, 2022), PaLM (Chowdhery et al., 2023), Llama (Grattafiori et al., 2024) and DeepSeek (Bi et al., 2024) have revolut
```

### Retrieved Chunk 4

- Source: `AdaDetectGPT Adaptive Detection of LLM-Generated Text with Statistical Guarantees.pdf`
- Page: `9`
- Chunk ID: `256`
- Chunk Type: `main`
- Dense Score: `unknown`
- Vector Score: `0.44804322719573975`
- BM25 Score: `8.84241347657191`
- Reranker Score: `5.0491943359375`

```text
underperforms Binoculars or RADAR. Nonetheless, AdaDetectGPT consistently improves upon Fast-DetectGPT across various datasets, with gains on Essay reaching up to 37.8%. Additionally, we evaluate AdaDetectGPT’s robustness to two adversarial attacks, paraphrasing and decoherence, in the black-box setting. As shown in Table 3, AdaDetectGPT demonstrates greater resilience than Fast-DetectGPT to adversarially perturbed texts. The improvement reaches up to 10% for paraphrasing and up to 85% for decoherence. Finally, we employ the same five LLMs from Table 1 to compare Fast-DetectGPT and AdaDetectGPT in black-box settings. Following Bao et al. (2024), we use GPT-J as the source LLM for detecting each of the remaining four target LLMs. Due to space constraints, the results are presented in Table S11 of Appendix F.5, where AdaDetectGPT uniformly outperforms Fast-DetectGPT in all cases, with impr
```

### Retrieved Chunk 5

- Source: `AdaDetectGPT Adaptive Detection of LLM-Generated Text with Statistical Guarantees.pdf`
- Page: `1`
- Chunk ID: `215`
- Chunk Type: `main`
- Dense Score: `unknown`
- Vector Score: `unknown`
- BM25 Score: `8.959452228291966`
- Reranker Score: `4.9158782958984375`

```text
compute the logits – AdaDetectGPT achieves improvements over the best alternative in area under the curve (AUC) ranging from 12.5% to 37%. In black-box settings, where the source and target LLMs differ, it similarly offer gains of up to 20%. Theoretically, we provide statistical performance guarantees for AdaDetectGPT, deriving finite- sample error bounds for its TNR, FNR, true positive rate (TPR) and false positive rate (FPR). Existing literature on logits-based detectors generally lacks systematic statistical analysis. Our work aims to fill in this gap and contribute toward a deeper understanding of these methods in this emerging field, by offering a comprehensive analysis based on the aforementioned standard classification metrics. 1.1 Related works Existing methods for detecting machine-generated text generally fall into three categories: machine learning (ML)-based, statistics-based
```

### Retrieved Chunk 6

- Source: `AdaDetectGPT Adaptive Detection of LLM-Generated Text with Statistical Guarantees.pdf`
- Page: `8`
- Chunk ID: `252`
- Chunk Type: `main`
- Dense Score: `unknown`
- Vector Score: `0.48041218519210815`
- BM25 Score: `unknown`
- Reranker Score: `4.0706939697265625`

```text
In Appendix F.3, we analyze the computational costof AdaDetectGPT. Training the witness function typically requires less than one minute across different sample sizes and dimensions, with memory usage below 0.5 GB. In Appendix F.4, we further conduct a sensitivity analysisto investigate the sensitivity of AdaDetectGPT’s AUC score to various factors that may affect the estimation of the witness function. Our results show that AdaDetectGPT is generally robust to the size of training data, the number of B-spline features, and the distributional shift between training and test data, consistently maintaining superior performance over baselines. Black-box results. We next consider the black-box setting, where the task is to detect text generated by three widely used advanced LLMs: GPT-4o (Hurst et al., 2024), Claude-3.5-Haiku (Anthropic, 2024), and Gemini-2.5-Flash (Comanici et al., 2025). In 
```

### Retrieved Chunk 7

- Source: `Fast-DetectGPT Efficient Zero-Shot Detection of Machine-Generated Text via Conditional Probability Curvature.pdf`
- Page: `8`
- Chunk ID: `2240`
- Chunk Type: `main`
- Dense Score: `unknown`
- Vector Score: `unknown`
- BM25 Score: `3.4566614621638627`
- Reranker Score: `-1.4680233001708984`

```text
thorship and watermarking. Limitations and Future Work. Our initial research impetus centered on accelerating the detection process of DetectGPT. However, Fast-DetectGPT not only accelerates this process but also brings about notable enhancements in detection accuracy. In this paper, our focus is predominantly on these empirical advancements, with theoretical explorations earmarked for future endeavors. Furthermore, Fast-DetectGPT’s design leans on pre-trained models to span a multitude of domains and languages. This presents a challenge in a black-box setting, as no single model can seamlessly span all linguistic territories and domains. This is due to the intrinsic nature of pre-trained models being tailored to specific domains and languages. 5 R ELATED WORK Current research primarily concentrates onsupervised methods, involving the training of classifiers to distinguish between machin
```

### Retrieved Chunk 8

- Source: `DetectGPT Zero-Shot Machine-Generated Text Detection using Probability Curvature.pdf`
- Page: `2`
- Chunk ID: `1445`
- Chunk Type: `main`
- Dense Score: `unknown`
- Vector Score: `unknown`
- BM25 Score: `6.7454281321213605`
- Reranker Score: `-1.7166247367858887`

```text
Zero-Shot Machine-Generated Text Detection using Probability Curvature generated text detection. Other work explores watermarks for generated text (Kirchenbauer et al., 2023), which modify a model’s generations to make them easier to detect. Our work does not assume text is generated with the goal of easy detection; DetectGPT detects text generated from publicly available LLMs using standard LLM sampling strategies. The widespread use of LLMs has led to much other con- temporaneous work on detecting LLM output. Sadasivan et al. (2023) show that the detection AUROC of the an de- tector is upper bounded by a function of the TV distance between the model and human text. However, we find that AUROC of DetectGPT is high even for the largest publicly- available models (Table 2), suggesting that TV distance may not correlate strongly with model scale and capability. This disconnect may be exace
```


### Manual Judgment

Please inspect the retrieved chunks and fill in:

- Which setting retrieves the most useful chunks?
- Does BM25 help with method names, abbreviations, or technical terms?
- Does dense retrieval help with semantic but non-exact matches?
- Does hybrid + reranker combine the advantages of both?
- Does hybrid retrieval reduce or increase noise?
- Overall winner: Dense only / BM25 only / Hybrid + reranker / Tie

---

## Specific DetectGPT query

### Question

How does DetectGPT detect machine-generated text?

### Retrieval Modes

- Dense-only mode: `global`
- BM25-only mode: `global`
- Hybrid mode: `global`

### Candidate Papers

These should usually be similar because all three settings use the same paper-level routing.

#### Hybrid Candidate Papers

1. `DetectGPT-SC Improving Detection of Text Generated by Large Language Models through Self-Consistency with Masked Predictions.pdf`
   - Title: DetectGPT SC Improving Detection of Text Generated by Large Language Models through Self Consistency with Masked Predictions
   - Paper score: `0.44574111700057983`

2. `DetectGPT Zero-Shot Machine-Generated Text Detection using Probability Curvature.pdf`
   - Title: DetectGPT: Zero-Shot Machine-Generated Text Detection using Probability Curvature
   - Paper score: `0.45166757702827454`

3. `Fast-DetectGPT Efficient Zero-Shot Detection of Machine-Generated Text via Conditional Probability Curvature.pdf`
   - Title: Fast DetectGPT Efficient Zero Shot Detection of Machine Generated Text via Conditional Probability Curvature
   - Paper score: `0.47658205032348633`

4. `DetectLLM Leveraging Log-Rank Information for Zero-Shot Detection of Machine-Generated Text.pdf`
   - Title: DetectLLM Leveraging Log Rank Information for Zero Shot Detection of Machine Generated Text
   - Paper score: `0.49779653549194336`


### Selected Papers

#### Dense-only Selected Papers

1. `DetectGPT-SC Improving Detection of Text Generated by Large Language Models through Self-Consistency with Masked Predictions.pdf`
   - Title: DetectGPT SC Improving Detection of Text Generated by Large Language Models through Self Consistency with Masked Predictions
   - Paper score: `0.44574111700057983`

2. `DetectGPT Zero-Shot Machine-Generated Text Detection using Probability Curvature.pdf`
   - Title: DetectGPT: Zero-Shot Machine-Generated Text Detection using Probability Curvature
   - Paper score: `0.45166757702827454`

3. `Fast-DetectGPT Efficient Zero-Shot Detection of Machine-Generated Text via Conditional Probability Curvature.pdf`
   - Title: Fast DetectGPT Efficient Zero Shot Detection of Machine Generated Text via Conditional Probability Curvature
   - Paper score: `0.47658205032348633`

4. `DetectLLM Leveraging Log-Rank Information for Zero-Shot Detection of Machine-Generated Text.pdf`
   - Title: DetectLLM Leveraging Log Rank Information for Zero Shot Detection of Machine Generated Text
   - Paper score: `0.49779653549194336`


#### BM25-only Selected Papers

1. `DetectGPT-SC Improving Detection of Text Generated by Large Language Models through Self-Consistency with Masked Predictions.pdf`
   - Title: DetectGPT SC Improving Detection of Text Generated by Large Language Models through Self Consistency with Masked Predictions
   - Paper score: `0.44574111700057983`

2. `DetectGPT Zero-Shot Machine-Generated Text Detection using Probability Curvature.pdf`
   - Title: DetectGPT: Zero-Shot Machine-Generated Text Detection using Probability Curvature
   - Paper score: `0.45166757702827454`

3. `Fast-DetectGPT Efficient Zero-Shot Detection of Machine-Generated Text via Conditional Probability Curvature.pdf`
   - Title: Fast DetectGPT Efficient Zero Shot Detection of Machine Generated Text via Conditional Probability Curvature
   - Paper score: `0.47658205032348633`

4. `DetectLLM Leveraging Log-Rank Information for Zero-Shot Detection of Machine-Generated Text.pdf`
   - Title: DetectLLM Leveraging Log Rank Information for Zero Shot Detection of Machine Generated Text
   - Paper score: `0.49779653549194336`


#### Hybrid Selected Papers

1. `DetectGPT-SC Improving Detection of Text Generated by Large Language Models through Self-Consistency with Masked Predictions.pdf`
   - Title: DetectGPT SC Improving Detection of Text Generated by Large Language Models through Self Consistency with Masked Predictions
   - Paper score: `0.44574111700057983`

2. `DetectGPT Zero-Shot Machine-Generated Text Detection using Probability Curvature.pdf`
   - Title: DetectGPT: Zero-Shot Machine-Generated Text Detection using Probability Curvature
   - Paper score: `0.45166757702827454`

3. `Fast-DetectGPT Efficient Zero-Shot Detection of Machine-Generated Text via Conditional Probability Curvature.pdf`
   - Title: Fast DetectGPT Efficient Zero Shot Detection of Machine Generated Text via Conditional Probability Curvature
   - Paper score: `0.47658205032348633`

4. `DetectLLM Leveraging Log-Rank Information for Zero-Shot Detection of Machine-Generated Text.pdf`
   - Title: DetectLLM Leveraging Log Rank Information for Zero Shot Detection of Machine Generated Text
   - Paper score: `0.49779653549194336`


### Summary Statistics

| Metric | Dense only | BM25 only | Hybrid + reranker |
|---|---:|---:|---:|
| Retrieved chunks | 8 | 8 | 8 |
| Unique sources | 4 | 3 | 3 |
| Noisy chunks | 0 | 0 | 0 |
| Overlap with hybrid | 4 | 2 | 8 |

### Source Distribution

#### Dense only

- `DetectGPT Zero-Shot Machine-Generated Text Detection using Probability Curvature.pdf`: 3 chunks
- `DetectGPT-SC Improving Detection of Text Generated by Large Language Models through Self-Consistency with Masked Predictions.pdf`: 2 chunks
- `Fast-DetectGPT Efficient Zero-Shot Detection of Machine-Generated Text via Conditional Probability Curvature.pdf`: 2 chunks
- `DetectLLM Leveraging Log-Rank Information for Zero-Shot Detection of Machine-Generated Text.pdf`: 1 chunks

#### BM25 only

- `DetectGPT Zero-Shot Machine-Generated Text Detection using Probability Curvature.pdf`: 3 chunks
- `DetectLLM Leveraging Log-Rank Information for Zero-Shot Detection of Machine-Generated Text.pdf`: 3 chunks
- `DetectGPT-SC Improving Detection of Text Generated by Large Language Models through Self-Consistency with Masked Predictions.pdf`: 2 chunks

#### Hybrid + reranker

- `DetectGPT Zero-Shot Machine-Generated Text Detection using Probability Curvature.pdf`: 6 chunks
- `DetectLLM Leveraging Log-Rank Information for Zero-Shot Detection of Machine-Generated Text.pdf`: 1 chunks
- `Fast-DetectGPT Efficient Zero-Shot Detection of Machine-Generated Text via Conditional Probability Curvature.pdf`: 1 chunks

### Dense-only Retrieved Chunks

### Retrieved Chunk 1

- Source: `DetectGPT Zero-Shot Machine-Generated Text Detection using Probability Curvature.pdf`
- Page: `6`
- Chunk ID: `1472`
- Chunk Type: `main`
- Dense Score: `0.4136630892753601`
- Vector Score: `0.4136630892753601`
- BM25 Score: `unknown`
- Reranker Score: `unknown`

```text
Zero-Shot Machine-Generated Text Detection using Probability Curvature 0.00 0.08 0.160.04 0.12 0.240.20 Fraction of GPT-J-generated news article re-written 0.6 0.7 0.8 0.9 1.0Detection AUROC Rank DetectGPT LogRank Likelihood Entropy Figure 5. We simulate human edits to machine-generated text by replacing varying fractions of model samples with T5-3B gener- ated text (masking out random five word spans until r% of text is masked to simulate human edits to machine-generated text). The four top-performing methods all generally degrade in performance with heavier revision, but DetectGPT is consistently most accurate. Experiment is conducted on the XSum dataset. for each token, we cannot compare to the rank, log rank, and entropy-based prior methods. We sample 150 examples 5 from the PubMedQA, XSum, and WritingPrompts datasets and compare the two pre-trained RoBERTa-based detector models with
```

### Retrieved Chunk 2

- Source: `DetectGPT Zero-Shot Machine-Generated Text Detection using Probability Curvature.pdf`
- Page: `6`
- Chunk ID: `1473`
- Chunk Type: `main`
- Dense Score: `0.41695094108581543`
- Vector Score: `0.41695094108581543`
- BM25 Score: `unknown`
- Reranker Score: `unknown`

```text
models with DetectGPT and the probability thresholding baseline. We show in Table 2 that DetectGPT can provide detection competitive with or better than the stronger of the two supervised models, and it again greatly outperforms probability thresholding on average. 5.2. Variants of Machine-Generated Text Detection Detecting paraphrased machine-generated text. In prac- tice, humans may manually edit or refine machine-generated text rather than blindly use a model’s generations for their task of interest. We therefore conduct an experiment to simulate the detection problem for model samples that have been increasingly heavily revised. We simulate human re- vision by replacing 5 word spans of the text with samples from T5-3B until r% of the text has been replaced, and report performance as r varies. Figure 5 shows that De- tectGPT maintains detection AUROC above 0.8 even when nearly a quart
```

### Retrieved Chunk 3

- Source: `DetectGPT-SC Improving Detection of Text Generated by Large Language Models through Self-Consistency with Masked Predictions.pdf`
- Page: `2`
- Chunk ID: `1519`
- Chunk Type: `main`
- Dense Score: `0.432113915681839`
- Vector Score: `0.432113915681839`
- BM25 Score: `unknown`
- Reranker Score: `unknown`

```text
of watermarks is also a challenge we need to address. However, with the emergence of ChatGPT, an innovative statistical detection method called DetectGPT [5] has been developed. Its principle is that text generated by the model typically resides in the negative curvature region of the model’s log probability. DetectGPT [ 5] generates and compares multiple variants of model-generated texts to determine whether the texts are machine-generated based on the log probabilities of the original texts and these variants. DetectGPT [5] outperforms the vast majority of existing zero-shot methods in terms of model sample detection, achieving very high AUC. It is based on this concept that DetectGPT-SC was proposed. 3 Methodology Predefined definition X is the original input text. ˆX is the sentence masked within X, which can also be referred to as "<mask>". P ( ˆX) is the mask content predicted by C
```

### Retrieved Chunk 4

- Source: `DetectLLM Leveraging Log-Rank Information for Zero-Shot Detection of Machine-Generated Text.pdf`
- Page: `2`
- Chunk ID: `1853`
- Chunk Type: `main`
- Dense Score: `0.43436291813850403`
- Vector Score: `0.43436291813850403`
- BM25 Score: `unknown`
- Reranker Score: `unknown`

```text
1020 50 100 #(Perturbations) 88 90 92performance(%) XSum 1020 50 100 #(Perturbations) 82 84 86 SQuAD 1020 50 100 #(Perturbations) 92 94 96 WritingP DetectGPT NPR(ours) Figure 2: Comparison of DetectGPT to NPR averaged across six models (in terms of AUROC). (The full results are given in Figure 6 in the Appendix). methods for detecting machine-generated text by evaluating the per-token log probability of texts and using thresholding. Mitchell et al. (2023) observed that machine-generated texts tend to lie in the local curvature of the log probability and proposed De- tectGPT, whose prominent performance can only be guaranteed by the large size of the perturbation function and by a large number of perturbations, and thus costs more computational resources. Other work explored watermarking, which im- prints specific patterns of the LLM-output text that can be detected by an algorithm while 
```

### Retrieved Chunk 5

- Source: `Fast-DetectGPT Efficient Zero-Shot Detection of Machine-Generated Text via Conditional Probability Curvature.pdf`
- Page: `4`
- Chunk ID: `2219`
- Chunk Type: `main`
- Dense Score: `0.4363716244697571`
- Vector Score: `0.4363716244697571`
- BM25 Score: `unknown`
- Reranker Score: `unknown`

```text
Published as a conference paper at ICLR 2024 Algorithm 1 Fast-DetectGPT machine-generated text detection. Input: passage x, sampling model qφ, scoring model pθ, and decision threshold ϵ Output: True – probably machine-generated, False – probably human-written. 1: function FAST DETECT GPT( x, qφ, pθ) 2: ˜xi ∼ qφ(˜x|x), i ∈ [1..N ] ▷ Conditional sampling 3: ˜µ ← 1 N P i log pθ(˜xi|x) ▷ Estimate the mean 4: ˜σ2 ← 1 N −1 P i(log pθ(˜xi|x) − ˜µ)2 ▷ Estimate the variance 5: ˆdx ← (log pθ(x) − ˜µ)/˜σ ▷ Estimate conditional probability curvature 6: return ˆdx > ϵ torch.distributions.categorical.Categorical(logits=lprobs).sample([10000]), where the lprobs is the log probability distribution of qφ(˜xj|x<j) for j from 0 to the length of x. The sampling process plays a pivotal role in guiding us toward the solution. To discern whether a token within a given context is machine-generated or human-auth
```

### Retrieved Chunk 6

- Source: `DetectGPT Zero-Shot Machine-Generated Text Detection using Probability Curvature.pdf`
- Page: `4`
- Chunk ID: `1461`
- Chunk Type: `main`
- Dense Score: `0.4410603940486908`
- Vector Score: `0.4410603940486908`
- BM25 Score: `unknown`
- Reranker Score: `unknown`

```text
tion task. Finally, we analyze more closely DetectGPT’s behavior as the choice of perturbation function, the number of samples used to estimate d (x, pθ, q), the length of the passage, and the data distribution is varied. Comparisons. We compare DetectGPT with various exist- ing zero-shot methods for machine-generated text detection that also leverage the predicted token-wise conditional dis- tributions of the source model for detection. These methods correspond to statistical tests based on token log probabil- ities, token ranks, or predictive entropy (Gehrmann et al., 2019; Solaiman et al., 2019; Ippolito et al., 2020). The first method uses the source model’s average token-wise log probability to determine if a candidate passage is machine- generated or not; passages with high average log probability are likely to be generated by the model. The second and third methods use the average
```

### Retrieved Chunk 7

- Source: `DetectGPT-SC Improving Detection of Text Generated by Large Language Models through Self-Consistency with Masked Predictions.pdf`
- Page: `5`
- Chunk ID: `1534`
- Chunk Type: `main`
- Dense Score: `0.4456269443035126`
- Vector Score: `0.4456269443035126`
- BM25 Score: `unknown`
- Reranker Score: `unknown`

```text
while a lower temperature (such as 0.1) makes the generated texts more deterministic or focused. In scoring systems, the primary evaluation is focused on the quality and coherence of the generated texts. These metrics emphasize the overall quality of the generated output rather than the specific level of randomness or diversity. 5 Conclusion In this paper, we have successfully introduced and validated DetectGPT-SC, which distinguishes itself significantly from existing literature. Our work proposes an innovative text detection method based on the self-consistency and 6
```

### Retrieved Chunk 8

- Source: `Fast-DetectGPT Efficient Zero-Shot Detection of Machine-Generated Text via Conditional Probability Curvature.pdf`
- Page: `5`
- Chunk ID: `2227`
- Chunk Type: `main`
- Dense Score: `0.45820948481559753`
- Vector Score: `0.45820948481559753`
- BM25 Score: `unknown`
- Reranker Score: `unknown`

```text
experiments, measuring the detection accuracy in AUROC (see Appendix A). Inference Speedup. We compare the inference time (excluding the time for initializing the model) of Fast-DetectGPT and DetectGPT on a Tesla A100 GPU using XSum generations from the five models in Table 2. Despite DetectGPT’s use of GPU batch processing, splitting 100 perturbations into 10 batches, it still requires substantial computational resources. It totals 79,113 seconds (ap- proximately 22 hours) over five runs. In contrast, Fast-DetectGPT completes the task in only 233 seconds (about 4 minutes), achieving a remarkable speedup factor of approximately 340x, highlight- ing its significant performance improvement. White-Box Zero-Shot Machine-Generated Text Detection. We evaluate zero-shot methods us- ing each source model for scoring and typically Fast-DetectGPT using the source model also for sampling. The avera
```


### BM25-only Retrieved Chunks

### Retrieved Chunk 1

- Source: `DetectGPT Zero-Shot Machine-Generated Text Detection using Probability Curvature.pdf`
- Page: `2`
- Chunk ID: `1445`
- Chunk Type: `main`
- Dense Score: `unknown`
- Vector Score: `unknown`
- BM25 Score: `13.58071750216719`
- Reranker Score: `unknown`

```text
Zero-Shot Machine-Generated Text Detection using Probability Curvature generated text detection. Other work explores watermarks for generated text (Kirchenbauer et al., 2023), which modify a model’s generations to make them easier to detect. Our work does not assume text is generated with the goal of easy detection; DetectGPT detects text generated from publicly available LLMs using standard LLM sampling strategies. The widespread use of LLMs has led to much other con- temporaneous work on detecting LLM output. Sadasivan et al. (2023) show that the detection AUROC of the an de- tector is upper bounded by a function of the TV distance between the model and human text. However, we find that AUROC of DetectGPT is high even for the largest publicly- available models (Table 2), suggesting that TV distance may not correlate strongly with model scale and capability. This disconnect may be exace
```

### Retrieved Chunk 2

- Source: `DetectGPT Zero-Shot Machine-Generated Text Detection using Probability Curvature.pdf`
- Page: `1`
- Chunk ID: `1438`
- Chunk Type: `main`
- Dense Score: `unknown`
- Vector Score: `unknown`
- BM25 Score: `10.758111712615761`
- Reranker Score: `unknown`

```text
Zero-Shot Machine-Generated Text Detection using Probability Curvature machine-generated text detection problem as a binary clas- sification problem. Specifically, we aim to classify whether a candidate passage was generated by a particular source model. While several works have investigated methods for training a second deep network to detect machine-generated text, such an approach has several shortcomings, including a tendency to overfit to the topics it was trained on as well as the need to train a new model for each new source model that is released. We therefore consider the zero-shot version of machine-generated text detection, where we use the source model itself, without fine-tuning or adaptation of any kind, to detect its own samples. The most common method for zero-shot machine-generated text detection is evaluating the average per-token log probability of the generated text a
```

### Retrieved Chunk 3

- Source: `DetectGPT Zero-Shot Machine-Generated Text Detection using Probability Curvature.pdf`
- Page: `0`
- Chunk ID: `1433`
- Chunk Type: `main`
- Dense Score: `unknown`
- Vector Score: `unknown`
- BM25 Score: `10.753234279133384`
- Reranker Score: `unknown`

```text
DetectGPT: Zero-Shot Machine-Generated Text Detection using Probability Curvature Eric Mitchell 1 Yoonho Lee1 Alexander Khazatsky 1 Christopher D. Manning 1 Chelsea Finn 1 Abstract The increasing fluency and widespread usage of large language models (LLMs) highlight the de- sirability of corresponding tools aiding detection of LLM-generated text. In this paper, we identify a property of the structure of an LLM’s proba- bility function that is useful for such detection. Specifically, we demonstrate that text sampled from an LLM tends to occupy negative curva- ture regions of the model’s log probability func- tion. Leveraging this observation, we then define a new curvature-based criterion for judging if a passage is generated from a given LLM. This approach, which we call DetectGPT, does not re- quire training a separate classifier, collecting a dataset of real or generated passages, or e
```

### Retrieved Chunk 4

- Source: `DetectLLM Leveraging Log-Rank Information for Zero-Shot Detection of Machine-Generated Text.pdf`
- Page: `14`
- Chunk ID: `1915`
- Chunk Type: `main`
- Dense Score: `unknown`
- Vector Score: `unknown`
- BM25 Score: `10.283032572923467`
- Reranker Score: `unknown`

```text
smaller than 50 points, which suggests that for low temperature, we should use the assumption “machine- generated text has lower entropy" for detection machine-generated text. In general, the Entropy method performs worse than random and is not an implementable detection method. For perturbation-based methods (Figure 10), while DetectGPT does not exhibit a clear trend with respect to temperature, the performance of NPR improves with the decreasing temperature most of the time. However, this trend is not as clear as the Log-Rank and Log-Likelihood methods, especially when the temperature becomes too low. This behaviour suggests that the perturbation-based method is more suitable for high temperatures, while the perturbation-free method is more suitable for low temperature. 12409
```

### Retrieved Chunk 5

- Source: `DetectLLM Leveraging Log-Rank Information for Zero-Shot Detection of Machine-Generated Text.pdf`
- Page: `13`
- Chunk ID: `1912`
- Chunk Type: `main`
- Dense Score: `unknown`
- Vector Score: `unknown`
- BM25 Score: `9.231031520236666`
- Reranker Score: `unknown`

```text
methods with four LLMs using top-p and top-k sampling. For perturbation-based methods, even with different sampling strategies, NPR provides a clearer signal for machine-generated text detection than DetectGPT. Moreover, we find that although LRR is more stable than Log-Rank and Log-Likelihood methods: when replacing temperature sampling to top- p and top-k sampling, all the above-mentioned three zero-shot methods’ performance improves, however, LRR improves approximately the same for both top-k and top-p sampling while the other two is more in favour of top-p sampling. Different Temperature. Here, we investigate how the temperature used for machine-generated texts affects the detection accuracy of different zero-shot methods. From Figure 9, we find that all the perturbation-free zero-shot methods improved their performance with the decreasing temperature. In particular, for the Log-Rank
```

### Retrieved Chunk 6

- Source: `DetectLLM Leveraging Log-Rank Information for Zero-Shot Detection of Machine-Generated Text.pdf`
- Page: `11`
- Chunk ID: `1901`
- Chunk Type: `main`
- Dense Score: `unknown`
- Vector Score: `unknown`
- BM25 Score: `8.88869366001364`
- Reranker Score: `unknown`

```text
to be machine-generated. • Entropy (Gehrmann et al., 2019): This approach is inspired by the hypothesis that machine-generated texts are more likely to have over-confident (thus low entropy) predictive distributions. In practice, (Mitchell et al., 2023) discovered that entropy is positively correlated with passage fakeness, therefore, following their convention, we use high average entropy as a signal of machine-generated text. • DetectGPT (Mitchell et al., 2023): DetectGPT is based on the hypothesis that when applying small perturbations to a passage x and produce the perturbed text ˜x, the quantity log pθ(x)− log pθ(˜x) is relatively larger for machine-generated samples than human written one. In practice, the performance of this approach depends heavily on the external perturbation function and the number of perturbations. Details on LLMs used. We used 7 LLMs ranging from 1.5B paramet
```

### Retrieved Chunk 7

- Source: `DetectGPT-SC Improving Detection of Text Generated by Large Language Models through Self-Consistency with Masked Predictions.pdf`
- Page: `6`
- Chunk ID: `1536`
- Chunk Type: `main`
- Dense Score: `unknown`
- Vector Score: `unknown`
- BM25 Score: `8.849923666424276`
- Reranker Score: `unknown`

```text
2019. [3] S. Chakraborty, A. S. Bedi, S. Zhu, B. An, D. Manocha, and F. Huang, “On the possibilities of ai-generated text detection,” arXiv preprint arXiv:2304.04736, 2023. [4] B. Guo, X. Zhang, Z. Wang, M. Jiang, J. Nie, Y . Ding, J. Yue, and Y . Wu, “How close is chatgpt to human experts? comparison corpus, evaluation, and detection,”arXiv preprint arXiv:2301.07597, 2023. [5] E. Mitchell, Y . Lee, A. Khazatsky, C. D. Manning, and C. Finn, “Detectgpt: Zero-shot machine-generated text detection using probability curvature,”arXiv preprint arXiv:2301.11305, 2023. [6] G. C. Langelaar, I. Setyawan, and R. L. Lagendijk, “Watermarking digital image and video data. a state-of-the-art overview,”IEEE Signal processing magazine, vol. 17, no. 5, pp. 20–46, 2000. [7] J. Kirchenbauer, J. Geiping, Y . Wen, J. Katz, I. Miers, and T. Goldstein, “A watermark for large language models,” arXiv preprint arX
```

### Retrieved Chunk 8

- Source: `DetectGPT-SC Improving Detection of Text Generated by Large Language Models through Self-Consistency with Masked Predictions.pdf`
- Page: `0`
- Chunk ID: `1509`
- Chunk Type: `main`
- Dense Score: `unknown`
- Vector Score: `unknown`
- BM25 Score: `8.756404705897285`
- Reranker Score: `unknown`

```text
DETECT GPT-SC: I MPROVING DETECTION OF TEXT GENERATED BY LARGE LANGUAGE MODELS THROUGH SELF -C ONSISTENCY WITH MASKED PREDICTIONS Rongsheng Wang Macao Polytechnic University p2213046@mpu.edu.mo Qi Li Iowa State University qli@iastate.edu Sihong Xie∗ HKUST (GZ) sihongxie@hkust-gz.edu.cn ABSTRACT General large language models (LLMs) such as ChatGPT have shown remarkable success, but it has also raised concerns among people about the misuse of AI-generated texts. Therefore, an important question is how to detect whether the texts are generated by ChatGPT or by humans. Existing detectors are built on the assumption that there is a distribution gap between human-generated and AI-generated texts. These gaps are typically identified using statistical information or classifiers. In contrast to prior research methods, we find that large language models such as ChatGPT exhibit strong self-consiste
```


### Hybrid + Reranker Retrieved Chunks

### Retrieved Chunk 1

- Source: `DetectGPT Zero-Shot Machine-Generated Text Detection using Probability Curvature.pdf`
- Page: `0`
- Chunk ID: `1433`
- Chunk Type: `main`
- Dense Score: `unknown`
- Vector Score: `0.4524148106575012`
- BM25 Score: `10.753234279133384`
- Reranker Score: `8.607498168945312`

```text
DetectGPT: Zero-Shot Machine-Generated Text Detection using Probability Curvature Eric Mitchell 1 Yoonho Lee1 Alexander Khazatsky 1 Christopher D. Manning 1 Chelsea Finn 1 Abstract The increasing fluency and widespread usage of large language models (LLMs) highlight the de- sirability of corresponding tools aiding detection of LLM-generated text. In this paper, we identify a property of the structure of an LLM’s proba- bility function that is useful for such detection. Specifically, we demonstrate that text sampled from an LLM tends to occupy negative curva- ture regions of the model’s log probability func- tion. Leveraging this observation, we then define a new curvature-based criterion for judging if a passage is generated from a given LLM. This approach, which we call DetectGPT, does not re- quire training a separate classifier, collecting a dataset of real or generated passages, or e
```

### Retrieved Chunk 2

- Source: `DetectGPT Zero-Shot Machine-Generated Text Detection using Probability Curvature.pdf`
- Page: `2`
- Chunk ID: `1445`
- Chunk Type: `main`
- Dense Score: `unknown`
- Vector Score: `unknown`
- BM25 Score: `13.58071750216719`
- Reranker Score: `8.331501960754395`

```text
Zero-Shot Machine-Generated Text Detection using Probability Curvature generated text detection. Other work explores watermarks for generated text (Kirchenbauer et al., 2023), which modify a model’s generations to make them easier to detect. Our work does not assume text is generated with the goal of easy detection; DetectGPT detects text generated from publicly available LLMs using standard LLM sampling strategies. The widespread use of LLMs has led to much other con- temporaneous work on detecting LLM output. Sadasivan et al. (2023) show that the detection AUROC of the an de- tector is upper bounded by a function of the TV distance between the model and human text. However, we find that AUROC of DetectGPT is high even for the largest publicly- available models (Table 2), suggesting that TV distance may not correlate strongly with model scale and capability. This disconnect may be exace
```

### Retrieved Chunk 3

- Source: `DetectGPT Zero-Shot Machine-Generated Text Detection using Probability Curvature.pdf`
- Page: `2`
- Chunk ID: `1450`
- Chunk Type: `main`
- Dense Score: `unknown`
- Vector Score: `0.4474771320819855`
- BM25 Score: `unknown`
- Reranker Score: `8.189292907714844`

```text
without any fine-tuning or adaptation to the target domain. 4. DetectGPT: Zero-shot Machine-Generated Text Detection with Random Perturbations DetectGPT is based on the hypothesis that samples from a source model pθ typically lie in areas of negative curvature of the log probability function of pθ, unlike human text. In other words, if we apply small perturbations to a passage x ∼ pθ, producing ˜x, the quantity log pθ(x) − log pθ(˜x) should be relatively large on average for machine-generated samples compared to human-written text. To leverage this hypothesis, first consider a perturbation function q(· | x) that gives a distribution over ˜x, slightly modified versions of x with similar meaning (we will generally consider roughly paragraph-length texts x). As an example, q(· | x) might be the result of simply asking a human to rewrite one of the sentences of x, while preserving the meanin
```

### Retrieved Chunk 4

- Source: `DetectGPT Zero-Shot Machine-Generated Text Detection using Probability Curvature.pdf`
- Page: `6`
- Chunk ID: `1472`
- Chunk Type: `main`
- Dense Score: `unknown`
- Vector Score: `0.4136630892753601`
- BM25 Score: `10.09347475615644`
- Reranker Score: `7.9210920333862305`

```text
Zero-Shot Machine-Generated Text Detection using Probability Curvature 0.00 0.08 0.160.04 0.12 0.240.20 Fraction of GPT-J-generated news article re-written 0.6 0.7 0.8 0.9 1.0Detection AUROC Rank DetectGPT LogRank Likelihood Entropy Figure 5. We simulate human edits to machine-generated text by replacing varying fractions of model samples with T5-3B gener- ated text (masking out random five word spans until r% of text is masked to simulate human edits to machine-generated text). The four top-performing methods all generally degrade in performance with heavier revision, but DetectGPT is consistently most accurate. Experiment is conducted on the XSum dataset. for each token, we cannot compare to the rank, log rank, and entropy-based prior methods. We sample 150 examples 5 from the PubMedQA, XSum, and WritingPrompts datasets and compare the two pre-trained RoBERTa-based detector models with
```

### Retrieved Chunk 5

- Source: `DetectGPT Zero-Shot Machine-Generated Text Detection using Probability Curvature.pdf`
- Page: `6`
- Chunk ID: `1473`
- Chunk Type: `main`
- Dense Score: `unknown`
- Vector Score: `0.41695094108581543`
- BM25 Score: `9.487253786066512`
- Reranker Score: `7.728855133056641`

```text
models with DetectGPT and the probability thresholding baseline. We show in Table 2 that DetectGPT can provide detection competitive with or better than the stronger of the two supervised models, and it again greatly outperforms probability thresholding on average. 5.2. Variants of Machine-Generated Text Detection Detecting paraphrased machine-generated text. In prac- tice, humans may manually edit or refine machine-generated text rather than blindly use a model’s generations for their task of interest. We therefore conduct an experiment to simulate the detection problem for model samples that have been increasingly heavily revised. We simulate human re- vision by replacing 5 word spans of the text with samples from T5-3B until r% of the text has been replaced, and report performance as r varies. Figure 5 shows that De- tectGPT maintains detection AUROC above 0.8 even when nearly a quart
```

### Retrieved Chunk 6

- Source: `DetectLLM Leveraging Log-Rank Information for Zero-Shot Detection of Machine-Generated Text.pdf`
- Page: `2`
- Chunk ID: `1853`
- Chunk Type: `main`
- Dense Score: `unknown`
- Vector Score: `0.43436291813850403`
- BM25 Score: `7.899461110026238`
- Reranker Score: `7.708574295043945`

```text
1020 50 100 #(Perturbations) 88 90 92performance(%) XSum 1020 50 100 #(Perturbations) 82 84 86 SQuAD 1020 50 100 #(Perturbations) 92 94 96 WritingP DetectGPT NPR(ours) Figure 2: Comparison of DetectGPT to NPR averaged across six models (in terms of AUROC). (The full results are given in Figure 6 in the Appendix). methods for detecting machine-generated text by evaluating the per-token log probability of texts and using thresholding. Mitchell et al. (2023) observed that machine-generated texts tend to lie in the local curvature of the log probability and proposed De- tectGPT, whose prominent performance can only be guaranteed by the large size of the perturbation function and by a large number of perturbations, and thus costs more computational resources. Other work explored watermarking, which im- prints specific patterns of the LLM-output text that can be detected by an algorithm while 
```

### Retrieved Chunk 7

- Source: `DetectGPT Zero-Shot Machine-Generated Text Detection using Probability Curvature.pdf`
- Page: `1`
- Chunk ID: `1440`
- Chunk Type: `main`
- Dense Score: `unknown`
- Vector Score: `0.4930853247642517`
- BM25 Score: `unknown`
- Reranker Score: `7.427803993225098`

```text
We empirically verify this hypothesis, and find that it holds true across a diverse body of LLMs, even when the minor rewrites, or perturbations, come from alternative language models. We leverage this observation to build DetectGPT, a zero-shot method for automated machine-generated text detection. To test if a passage came from a source model pθ, DetectGPT compares the log probability of the candidate passage under pθ with the average log probability of several perturbations of the passage under pθ (generated with, e.g., T5; Raffel et al. (2020)). If the perturbed passages tend to have lower average log probability than the original by some margin, the candidate passage is likely to have come from pθ. See Figure 1 for an overview of the problem and DetectGPT. See Figure 2 for an illustration of the under- lying hypothesis and Figure 3 for empirical evaluation of the hypothesis. Our exp
```

### Retrieved Chunk 8

- Source: `Fast-DetectGPT Efficient Zero-Shot Detection of Machine-Generated Text via Conditional Probability Curvature.pdf`
- Page: `4`
- Chunk ID: `2219`
- Chunk Type: `main`
- Dense Score: `unknown`
- Vector Score: `0.4363716244697571`
- BM25 Score: `7.259480098497036`
- Reranker Score: `7.364211559295654`

```text
Published as a conference paper at ICLR 2024 Algorithm 1 Fast-DetectGPT machine-generated text detection. Input: passage x, sampling model qφ, scoring model pθ, and decision threshold ϵ Output: True – probably machine-generated, False – probably human-written. 1: function FAST DETECT GPT( x, qφ, pθ) 2: ˜xi ∼ qφ(˜x|x), i ∈ [1..N ] ▷ Conditional sampling 3: ˜µ ← 1 N P i log pθ(˜xi|x) ▷ Estimate the mean 4: ˜σ2 ← 1 N −1 P i(log pθ(˜xi|x) − ˜µ)2 ▷ Estimate the variance 5: ˆdx ← (log pθ(x) − ˜µ)/˜σ ▷ Estimate conditional probability curvature 6: return ˆdx > ϵ torch.distributions.categorical.Categorical(logits=lprobs).sample([10000]), where the lprobs is the log probability distribution of qφ(˜xj|x<j) for j from 0 to the length of x. The sampling process plays a pivotal role in guiding us toward the solution. To discern whether a token within a given context is machine-generated or human-auth
```


### Manual Judgment

Please inspect the retrieved chunks and fill in:

- Which setting retrieves the most useful chunks?
- Does BM25 help with method names, abbreviations, or technical terms?
- Does dense retrieval help with semantic but non-exact matches?
- Does hybrid + reranker combine the advantages of both?
- Does hybrid retrieval reduce or increase noise?
- Overall winner: Dense only / BM25 only / Hybrid + reranker / Tie

---

## Logits-related methods

### Question

Which methods use logits for AI-generated text detection?

### Retrieval Modes

- Dense-only mode: `global`
- BM25-only mode: `global`
- Hybrid mode: `global`

### Candidate Papers

These should usually be similar because all three settings use the same paper-level routing.

#### Hybrid Candidate Papers

1. `DALD Improving Logits-based Detector without Logits from Black-box LLMs.pdf`
   - Title: DALD Improving Logits based Detector without Logits from Black box LLMs
   - Paper score: `0.3437868654727936`

2. `Ghostbuster Detecting Text Ghostwritten by Large Language Models.pdf`
   - Title: Ghostbuster Detecting Text Ghostwritten by Large Language Models
   - Paper score: `0.3704579472541809`

3. `SeqXGPT Sentence-Level AI-Generated Text Detection.pdf`
   - Title: SeqXGPT Sentence Level AI Generated Text Detection
   - Paper score: `0.39839988946914673`

4. `DetectLLM Leveraging Log-Rank Information for Zero-Shot Detection of Machine-Generated Text.pdf`
   - Title: DetectLLM Leveraging Log Rank Information for Zero Shot Detection of Machine Generated Text
   - Paper score: `0.4021763801574707`


### Selected Papers

#### Dense-only Selected Papers

1. `DALD Improving Logits-based Detector without Logits from Black-box LLMs.pdf`
   - Title: DALD Improving Logits based Detector without Logits from Black box LLMs
   - Paper score: `0.3437868654727936`

2. `Ghostbuster Detecting Text Ghostwritten by Large Language Models.pdf`
   - Title: Ghostbuster Detecting Text Ghostwritten by Large Language Models
   - Paper score: `0.3704579472541809`

3. `SeqXGPT Sentence-Level AI-Generated Text Detection.pdf`
   - Title: SeqXGPT Sentence Level AI Generated Text Detection
   - Paper score: `0.39839988946914673`

4. `DetectLLM Leveraging Log-Rank Information for Zero-Shot Detection of Machine-Generated Text.pdf`
   - Title: DetectLLM Leveraging Log Rank Information for Zero Shot Detection of Machine Generated Text
   - Paper score: `0.4021763801574707`


#### BM25-only Selected Papers

1. `DALD Improving Logits-based Detector without Logits from Black-box LLMs.pdf`
   - Title: DALD Improving Logits based Detector without Logits from Black box LLMs
   - Paper score: `0.3437868654727936`

2. `Ghostbuster Detecting Text Ghostwritten by Large Language Models.pdf`
   - Title: Ghostbuster Detecting Text Ghostwritten by Large Language Models
   - Paper score: `0.3704579472541809`

3. `SeqXGPT Sentence-Level AI-Generated Text Detection.pdf`
   - Title: SeqXGPT Sentence Level AI Generated Text Detection
   - Paper score: `0.39839988946914673`

4. `DetectLLM Leveraging Log-Rank Information for Zero-Shot Detection of Machine-Generated Text.pdf`
   - Title: DetectLLM Leveraging Log Rank Information for Zero Shot Detection of Machine Generated Text
   - Paper score: `0.4021763801574707`


#### Hybrid Selected Papers

1. `DALD Improving Logits-based Detector without Logits from Black-box LLMs.pdf`
   - Title: DALD Improving Logits based Detector without Logits from Black box LLMs
   - Paper score: `0.3437868654727936`

2. `Ghostbuster Detecting Text Ghostwritten by Large Language Models.pdf`
   - Title: Ghostbuster Detecting Text Ghostwritten by Large Language Models
   - Paper score: `0.3704579472541809`

3. `SeqXGPT Sentence-Level AI-Generated Text Detection.pdf`
   - Title: SeqXGPT Sentence Level AI Generated Text Detection
   - Paper score: `0.39839988946914673`

4. `DetectLLM Leveraging Log-Rank Information for Zero-Shot Detection of Machine-Generated Text.pdf`
   - Title: DetectLLM Leveraging Log Rank Information for Zero Shot Detection of Machine Generated Text
   - Paper score: `0.4021763801574707`


### Summary Statistics

| Metric | Dense only | BM25 only | Hybrid + reranker |
|---|---:|---:|---:|
| Retrieved chunks | 8 | 8 | 8 |
| Unique sources | 3 | 3 | 4 |
| Noisy chunks | 0 | 0 | 0 |
| Overlap with hybrid | 3 | 3 | 8 |

### Source Distribution

#### Dense only

- `DALD Improving Logits-based Detector without Logits from Black-box LLMs.pdf`: 3 chunks
- `Ghostbuster Detecting Text Ghostwritten by Large Language Models.pdf`: 3 chunks
- `SeqXGPT Sentence-Level AI-Generated Text Detection.pdf`: 2 chunks

#### BM25 only

- `Ghostbuster Detecting Text Ghostwritten by Large Language Models.pdf`: 3 chunks
- `DALD Improving Logits-based Detector without Logits from Black-box LLMs.pdf`: 3 chunks
- `DetectLLM Leveraging Log-Rank Information for Zero-Shot Detection of Machine-Generated Text.pdf`: 2 chunks

#### Hybrid + reranker

- `SeqXGPT Sentence-Level AI-Generated Text Detection.pdf`: 3 chunks
- `DALD Improving Logits-based Detector without Logits from Black-box LLMs.pdf`: 3 chunks
- `Ghostbuster Detecting Text Ghostwritten by Large Language Models.pdf`: 1 chunks
- `DetectLLM Leveraging Log-Rank Information for Zero-Shot Detection of Machine-Generated Text.pdf`: 1 chunks

### Dense-only Retrieved Chunks

### Retrieved Chunk 1

- Source: `DALD Improving Logits-based Detector without Logits from Black-box LLMs.pdf`
- Page: `0`
- Chunk ID: `1320`
- Chunk Type: `main`
- Dense Score: `0.2732464373111725`
- Vector Score: `0.2732464373111725`
- BM25 Score: `unknown`
- Reranker Score: `unknown`

```text
DALD: Improving Logits-based Detector without Logits from Black-box LLMs Cong Zeng1∗ Shengkun Tang1∗ Xianjun Yang2 Yuanzhou Chen3 Yiyou Sun4 Zhiqiang Xu1 Yao Li5 Haifeng Chen4 Wei ChengB4 Dongkuan Xu6 MBZUAI1 University of California, Santa Barbara2 University of California, Los Angeles3 NEC Labs America4 University of North Carolina, Chapel Hill5 NC State University6 {cong.zeng, shengkun.tang, zhiqiang.xu}@mbzuai.ac.ae xianjunyang@ucsb.edu {sunyiyou, haifengchen, weicheng}@nec-labs.com dxu27@ncsu.edu yuanzhouchen@cs.ucla.edu yaoli@ad.unc.edu Abstract The advent of Large Language Models (LLMs) has revolutionized text generation, producing outputs that closely mimic human writing. This blurring of lines between machine- and human-written text presents new challenges in distinguishing one from the other – a task further complicated by the frequent updates and closed nature of leading propr
```

### Retrieved Chunk 2

- Source: `DALD Improving Logits-based Detector without Logits from Black-box LLMs.pdf`
- Page: `2`
- Chunk ID: `1330`
- Chunk Type: `main`
- Dense Score: `0.3458750247955322`
- Vector Score: `0.3458750247955322`
- BM25 Score: `unknown`
- Reranker Score: `unknown`

```text
In logits-based detection methods, a surrogate model that closely mirrors the probability distribution curves of the target black-box LLM is instrumental in enhancing detection accuracy. We posit that this observed effect stems from the foundational assumptions inherent in logits-based detectors and proceed to examine the ramifications of this postulate in tackling the third question. To sum up, our contributions are as follows: • The introduction of DALD, a framework that significantly improves the performance of surrogate models in detecting LLM-generated text generated by both closed-source and open-source models. • DALD’s unique ability to enhance detection without reliance on knowledge of the source model – a game-changer in a domain where the source is often unknown. • The capability of a single detector, enabled by DALD, to accurately identify text from varying sources, democratiz
```

### Retrieved Chunk 3

- Source: `SeqXGPT Sentence-Level AI-Generated Text Detection.pdf`
- Page: `1`
- Chunk ID: `3398`
- Chunk Type: `main`
- Dense Score: `0.3624163866043091`
- Vector Score: `0.3624163866043091`
- BM25 Score: `unknown`
- Reranker Score: `unknown`

```text
existing methods, such as DetectGPT and Sniffer, fail to solve sentence-level AIGT detection. Our proposed SeqXGPT not only obtains promising results in both sentence and document-level AIGT detection challenges, but also exhibits excellent generalization on out-of-distribution datasets. 2 Background The proliferation of Large Language Models (LLMs) such as GPT-4 has given rise to increased concerns about the potential misuse of AI- generated texts (AIGT) (Brown et al., 2020; Zhang et al., 2022; Scao et al., 2022). This emphasizes the necessity for robust detection mechanisms to ensure security and trustworthiness of LLM applications. 2.1 Principal Approaches to AIGT Detection Broadly, AIGT detection methodologies fall into two primary categories: 1. Supervised Learning: This involves training models on labeled datasets to distinguish between human and AI-generated texts. Notable efforts
```

### Retrieved Chunk 4

- Source: `Ghostbuster Detecting Text Ghostwritten by Large Language Models.pdf`
- Page: `0`
- Chunk ID: `2377`
- Chunk Type: `main`
- Dense Score: `0.36471661925315857`
- Vector Score: `0.36471661925315857`
- BM25 Score: `unknown`
- Reranker Score: `unknown`

```text
Ghostbuster: Detecting Text Ghostwritten by Large Language Models Vivek Verma Eve Fleisig Nicholas Tomlin Dan Klein Computer Science Division, UC Berkeley {vivekverma, efleisig, nicholas_tomlin, klein}@berkeley.edu Abstract We introduce Ghostbuster, a state-of-the-art system for detecting AI-generated text. Our method works by passing documents through a series of weaker language models, running a structured search over possible combinations of their features, and then training a classifier on the selected features to predict whether docu- ments are AI-generated. Crucially, Ghostbuster does not require access to token probabilities from the target model, making it useful for de- tecting text generated by black-box or unknown models. In conjunction with our model, we release three new datasets of human- and AI- generated text as detection benchmarks in the domains of student essays, creat
```

### Retrieved Chunk 5

- Source: `Ghostbuster Detecting Text Ghostwritten by Large Language Models.pdf`
- Page: `8`
- Chunk ID: `2422`
- Chunk Type: `main`
- Dense Score: `0.37137413024902344`
- Vector Score: `0.37137413024902344`
- BM25 Score: `unknown`
- Reranker Score: `unknown`

```text
age future work on this issue, we propose an ad- ditional paragraph-level detection benchmark in Appendix F. 8 Conclusion We introduced Ghostbuster, a model for detect- ing AI-generated language that uses structured search on token probabilities from weaker mod- els to identify whether a given document was AI- generated. We validated Ghostbuster by evalu- ating its performance on datasets from three do- mains (news, student essays, and creative writing), as well as through generalization experiments on text generated by different models and using dif- ferent prompts. We also release our three datasets as benchmarks for evaluating performance on de- tecting AI-generated text. Ghostbuster achieved over 98.4 F1 across all datasets on in-domain detec- tion of AI-generated text, representing substantial progress over currently available models. Future work could examine tradeoffs between the 
```

### Retrieved Chunk 6

- Source: `SeqXGPT Sentence-Level AI-Generated Text Detection.pdf`
- Page: `1`
- Chunk ID: `3400`
- Chunk Type: `main`
- Dense Score: `0.37843796610832214`
- Vector Score: `0.37843796610832214`
- BM25 Score: `unknown`
- Reranker Score: `unknown`

```text
a perturbation-based method leveraging average per-token log probabilities. The recent work of Li et al. (2023) extends this further by studying multi-model detection through text perplexities, aiming to trace the precise LLM origin of texts. 2.2 Detection Task Formulations The AIGT detection tasks can be formulated in different setups: 1. Particular-Model Binary AIGT Detection: In this setup, the objective is to discriminate whether a text was produced by a specific known AI model or by a human. Both GPTZero and DetectGPT fall into this category. 2. Mixed-Model Binary AIGT Detection: Here, the detectors are designed to identify AI-generated content without the need to pinpoint the exact model of origin. 3https://gptzero.me/
```

### Retrieved Chunk 7

- Source: `DALD Improving Logits-based Detector without Logits from Black-box LLMs.pdf`
- Page: `1`
- Chunk ID: `1325`
- Chunk Type: `main`
- Dense Score: `0.3789195716381073`
- Vector Score: `0.3789195716381073`
- BM25 Score: `unknown`
- Reranker Score: `unknown`

```text
Accurate and reliable machine-generated text detection methods are necessary in order to address these issues[13–17]. Methods for detecting text generated by Large Language Models are broadly categorized into watermarking[18–21], training-based classifiers[ 22–26], and zero-shot detectors. Watermarking methods discreetly embed identifiable markers within the text output, striving to retain the model’s linguistic integrity. However, this tactic is implementable solely by the model provider. Training- based classifiers, while effective, are costly and often lack the agility to adapt to new domains or model updates. Our emphasis is on zero-shot detectors that exploit the intrinsic differences between text written by machines and humans, offering the advantage of being generally training-free. Most zero-shot detectors primarily depend on analyzing model output logits for detection. Notably, 
```

### Retrieved Chunk 8

- Source: `Ghostbuster Detecting Text Ghostwritten by Large Language Models.pdf`
- Page: `0`
- Chunk ID: `2380`
- Chunk Type: `main`
- Dense Score: `0.38298046588897705`
- Vector Score: `0.38298046588897705`
- BM25 Score: `unknown`
- Reranker Score: `unknown`

```text
datasets that they were not originally evaluated on (Section 6). In addition, the high false positive rates of these models raise potential ethical concerns be- cause they jeopardize students whose genuine work is misclassified as AI-generated. Furthermore, pre- vious work has indicated that text by non-native speakers of English is disproportionately flagged as AI-generated (Liang et al., 2023). These concerns underscore the need for AI-generated text detectors with strong generalization performance. We present Ghostbuster, a method for detection based on structured search and linear classification (Figure 1). First, Ghostbuster passes paired human- authored and AI-generated documents through a series of weaker language models, ranging from a unigram model to the non-instruction-tuned GPT-3 davinci. Given the word probabilities from these models, it then searches over a space of vector 
```


### BM25-only Retrieved Chunks

### Retrieved Chunk 1

- Source: `Ghostbuster Detecting Text Ghostwritten by Large Language Models.pdf`
- Page: `9`
- Chunk ID: `2426`
- Chunk Type: `main`
- Dense Score: `unknown`
- Vector Score: `unknown`
- BM25 Score: `13.372225722042872`
- Reranker Score: `unknown`

```text
likely for shorter text, domains further from those on which Ghostbuster was trained (e.g., text mes- sages), text in varieties of English besides Standard American or British English, or in non-English languages, text written by non-native speakers of English, AI-generated text that has been edited or paraphrased by a human, and text that was gen- erated by prompting an AI model to paraphrase or adjust a human-authored input. To avoid per- petuation of algorithmic harms due to these lim- itations, we strongly discourage incorporation of Ghostbuster into any systems that automatically penalize students or other writers for alleged usage of text generation without human supervision. In- stead, we recommend cautious use of Ghostbuster, in conjunction with human supervision and ad- ditional factors, if classifying a person’s writing as AI-generated could harm that person. Ghost- buster can 
```

### Retrieved Chunk 2

- Source: `DALD Improving Logits-based Detector without Logits from Black-box LLMs.pdf`
- Page: `3`
- Chunk ID: `1337`
- Chunk Type: `main`
- Dense Score: `unknown`
- Vector Score: `unknown`
- BM25 Score: `13.264630182583613`
- Reranker Score: `unknown`

```text
black-box detection without any access to the source model logits in our setting. 3.2 Logits-based Detection Methods Logits-based LLM detection methods compute a metric by discrepancy gap hypothesis of humans and machines for classification. For example, based on the observation that the LLM-generated text occupies negative curvature regions of the model’s log probability function, DetectGPT[27] proposes to utilize the source model for scoring, which refers to the white-box settings. Following DetectGPT, Fast-DetectGPT[29] replaces the perturbations-based sampling method with conditional probability sampling to accelerate the inference speed and improve the detection performance. Formally, given an input passage x and the target source model pθ, Fast-DetectGPT chooses another accessible but open-sourced model sθ for scoring, which is called the surrogate model. Together with a sampling m
```

### Retrieved Chunk 3

- Source: `Ghostbuster Detecting Text Ghostwritten by Large Language Models.pdf`
- Page: `8`
- Chunk ID: `2424`
- Chunk Type: `main`
- Dense Score: `unknown`
- Vector Score: `unknown`
- BM25 Score: `13.264298690097489`
- Reranker Score: `unknown`

```text
AI-generated text. Finally, future AI-generated text detectors could provide additional explanations for classification decisions, so that human users can use their own judgment when evaluating the deci- sions of these systems.
```

### Retrieved Chunk 4

- Source: `DALD Improving Logits-based Detector without Logits from Black-box LLMs.pdf`
- Page: `1`
- Chunk ID: `1325`
- Chunk Type: `main`
- Dense Score: `unknown`
- Vector Score: `unknown`
- BM25 Score: `12.50946093229392`
- Reranker Score: `unknown`

```text
Accurate and reliable machine-generated text detection methods are necessary in order to address these issues[13–17]. Methods for detecting text generated by Large Language Models are broadly categorized into watermarking[18–21], training-based classifiers[ 22–26], and zero-shot detectors. Watermarking methods discreetly embed identifiable markers within the text output, striving to retain the model’s linguistic integrity. However, this tactic is implementable solely by the model provider. Training- based classifiers, while effective, are costly and often lack the agility to adapt to new domains or model updates. Our emphasis is on zero-shot detectors that exploit the intrinsic differences between text written by machines and humans, offering the advantage of being generally training-free. Most zero-shot detectors primarily depend on analyzing model output logits for detection. Notably, 
```

### Retrieved Chunk 5

- Source: `DALD Improving Logits-based Detector without Logits from Black-box LLMs.pdf`
- Page: `3`
- Chunk ID: `1336`
- Chunk Type: `main`
- Dense Score: `unknown`
- Vector Score: `unknown`
- BM25 Score: `12.442566169287424`
- Reranker Score: `unknown`

```text
produced by an AI model ftar or a human, which can be considered as a binary classification task. Typically, there are two different task settings for LLM detection, namely white-box and black-box detection. In the black-box setting, we only have access to the generated text, treating the language model as a “black box” where we input text and receive output without knowing the internal workings or probabilities. In the white-box setting, we have additional information about the model, specifically the output probabilities p(xl|x[1:l−1]) for each token at each position l in the text. However, in the practical scenario, it is usually difficult to get access to the source model, especially widespread but closed-source models such as ChatGPT, GPT-4 and Claude-3. Therefore, we focus on improving the black-box detection without any access to the source model logits in our setting. 3.2 Logits-
```

### Retrieved Chunk 6

- Source: `Ghostbuster Detecting Text Ghostwritten by Large Language Models.pdf`
- Page: `8`
- Chunk ID: `2423`
- Chunk Type: `main`
- Dense Score: `unknown`
- Vector Score: `unknown`
- BM25 Score: `12.341018901685606`
- Reranker Score: `unknown`

```text
Future work could examine tradeoffs between the false positive and false negative rates of AI- generated text detectors for different applications. For detection of AI-generated student essays, low- ering the risk of false positives is a key priority to avoid false accusations of student misconduct. In other settings, however, false positives are less concerning. For example, if detectors are used to prevent AI-generated text from being used in language model training data, or to flag poten- tially AI-generated content on the web, the ideal model calibration may differ. Other avenues for future work include improving robustness to per- turbations of AI-generated outputs, such as lightly editing to avoid detection, and different task formu- lations, including detection at the paragraph level for documents that combine human-authored and AI-generated text. Finally, future AI-generated text
```

### Retrieved Chunk 7

- Source: `DetectLLM Leveraging Log-Rank Information for Zero-Shot Detection of Machine-Generated Text.pdf`
- Page: `0`
- Chunk ID: `1843`
- Chunk Type: `main`
- Dense Score: `unknown`
- Vector Score: `unknown`
- BM25 Score: `12.191089759801827`
- Reranker Score: `unknown`

```text
to detect machine-generated text, preventing malicious use such as plagiarism, misinforma- tion, and propaganda. In this paper, we intro- duce two novel zero-shot methods for detecting machine-generated text by leveraging the Log- Rank information. One is called DetectLLM- LRR, which is fast and efficient, and the other is called DetectLLM-NPR, which is more ac- curate, but slower due to the need for perturba- tions. Our experiments on three datasets and seven language models show that our proposed methods improve over the state of the art by 3.9 and 1.75 AUROC points absolute. More- over, DetectLLM-NPR needs fewer perturba- tions than previous work to achieve the same level of performance, which makes it more practical for real-world use. We also investi- gate the efficiency-performance trade-off based on users’ preference for these two measures and provide intuition for using them in p
```

### Retrieved Chunk 8

- Source: `DetectLLM Leveraging Log-Rank Information for Zero-Shot Detection of Machine-Generated Text.pdf`
- Page: `14`
- Chunk ID: `1915`
- Chunk Type: `main`
- Dense Score: `unknown`
- Vector Score: `unknown`
- BM25 Score: `11.957004291515881`
- Reranker Score: `unknown`

```text
smaller than 50 points, which suggests that for low temperature, we should use the assumption “machine- generated text has lower entropy" for detection machine-generated text. In general, the Entropy method performs worse than random and is not an implementable detection method. For perturbation-based methods (Figure 10), while DetectGPT does not exhibit a clear trend with respect to temperature, the performance of NPR improves with the decreasing temperature most of the time. However, this trend is not as clear as the Log-Rank and Log-Likelihood methods, especially when the temperature becomes too low. This behaviour suggests that the perturbation-based method is more suitable for high temperatures, while the perturbation-free method is more suitable for low temperature. 12409
```


### Hybrid + Reranker Retrieved Chunks

### Retrieved Chunk 1

- Source: `SeqXGPT Sentence-Level AI-Generated Text Detection.pdf`
- Page: `1`
- Chunk ID: `3400`
- Chunk Type: `main`
- Dense Score: `unknown`
- Vector Score: `0.37843796610832214`
- BM25 Score: `unknown`
- Reranker Score: `6.267269134521484`

```text
a perturbation-based method leveraging average per-token log probabilities. The recent work of Li et al. (2023) extends this further by studying multi-model detection through text perplexities, aiming to trace the precise LLM origin of texts. 2.2 Detection Task Formulations The AIGT detection tasks can be formulated in different setups: 1. Particular-Model Binary AIGT Detection: In this setup, the objective is to discriminate whether a text was produced by a specific known AI model or by a human. Both GPTZero and DetectGPT fall into this category. 2. Mixed-Model Binary AIGT Detection: Here, the detectors are designed to identify AI-generated content without the need to pinpoint the exact model of origin. 3https://gptzero.me/
```

### Retrieved Chunk 2

- Source: `DALD Improving Logits-based Detector without Logits from Black-box LLMs.pdf`
- Page: `3`
- Chunk ID: `1336`
- Chunk Type: `main`
- Dense Score: `unknown`
- Vector Score: `0.4254685044288635`
- BM25 Score: `12.442566169287424`
- Reranker Score: `6.1152777671813965`

```text
produced by an AI model ftar or a human, which can be considered as a binary classification task. Typically, there are two different task settings for LLM detection, namely white-box and black-box detection. In the black-box setting, we only have access to the generated text, treating the language model as a “black box” where we input text and receive output without knowing the internal workings or probabilities. In the white-box setting, we have additional information about the model, specifically the output probabilities p(xl|x[1:l−1]) for each token at each position l in the text. However, in the practical scenario, it is usually difficult to get access to the source model, especially widespread but closed-source models such as ChatGPT, GPT-4 and Claude-3. Therefore, we focus on improving the black-box detection without any access to the source model logits in our setting. 3.2 Logits-
```

### Retrieved Chunk 3

- Source: `DALD Improving Logits-based Detector without Logits from Black-box LLMs.pdf`
- Page: `2`
- Chunk ID: `1330`
- Chunk Type: `main`
- Dense Score: `unknown`
- Vector Score: `0.3458750247955322`
- BM25 Score: `unknown`
- Reranker Score: `5.963219165802002`

```text
In logits-based detection methods, a surrogate model that closely mirrors the probability distribution curves of the target black-box LLM is instrumental in enhancing detection accuracy. We posit that this observed effect stems from the foundational assumptions inherent in logits-based detectors and proceed to examine the ramifications of this postulate in tackling the third question. To sum up, our contributions are as follows: • The introduction of DALD, a framework that significantly improves the performance of surrogate models in detecting LLM-generated text generated by both closed-source and open-source models. • DALD’s unique ability to enhance detection without reliance on knowledge of the source model – a game-changer in a domain where the source is often unknown. • The capability of a single detector, enabled by DALD, to accurately identify text from varying sources, democratiz
```

### Retrieved Chunk 4

- Source: `DALD Improving Logits-based Detector without Logits from Black-box LLMs.pdf`
- Page: `3`
- Chunk ID: `1337`
- Chunk Type: `main`
- Dense Score: `unknown`
- Vector Score: `unknown`
- BM25 Score: `13.264630182583613`
- Reranker Score: `5.9245405197143555`

```text
black-box detection without any access to the source model logits in our setting. 3.2 Logits-based Detection Methods Logits-based LLM detection methods compute a metric by discrepancy gap hypothesis of humans and machines for classification. For example, based on the observation that the LLM-generated text occupies negative curvature regions of the model’s log probability function, DetectGPT[27] proposes to utilize the source model for scoring, which refers to the white-box settings. Following DetectGPT, Fast-DetectGPT[29] replaces the perturbations-based sampling method with conditional probability sampling to accelerate the inference speed and improve the detection performance. Formally, given an input passage x and the target source model pθ, Fast-DetectGPT chooses another accessible but open-sourced model sθ for scoring, which is called the surrogate model. Together with a sampling m
```

### Retrieved Chunk 5

- Source: `Ghostbuster Detecting Text Ghostwritten by Large Language Models.pdf`
- Page: `1`
- Chunk ID: `2386`
- Chunk Type: `main`
- Dense Score: `unknown`
- Vector Score: `unknown`
- BM25 Score: `11.90203672886834`
- Reranker Score: `5.709489822387695`

```text
tions from the model that might have generated the text. Recent supervised methods have used lo- gistic regression, RoBERTa, and T5 to distinguish between human-authored and AI-generated text (Guo et al., 2023; Chen et al., 2023; Uchendu et al., 2020). Concurrent with this work, Bhattacharjee et al. (2023) used contrastive domain adaptation for unsupervised AI-generated text detection. However, Sadasivan et al. (2023) argued that there is an upper bound on the performance of gen-
```

### Retrieved Chunk 6

- Source: `SeqXGPT Sentence-Level AI-Generated Text Detection.pdf`
- Page: `1`
- Chunk ID: `3398`
- Chunk Type: `main`
- Dense Score: `unknown`
- Vector Score: `0.3624163866043091`
- BM25 Score: `unknown`
- Reranker Score: `5.286731719970703`

```text
existing methods, such as DetectGPT and Sniffer, fail to solve sentence-level AIGT detection. Our proposed SeqXGPT not only obtains promising results in both sentence and document-level AIGT detection challenges, but also exhibits excellent generalization on out-of-distribution datasets. 2 Background The proliferation of Large Language Models (LLMs) such as GPT-4 has given rise to increased concerns about the potential misuse of AI- generated texts (AIGT) (Brown et al., 2020; Zhang et al., 2022; Scao et al., 2022). This emphasizes the necessity for robust detection mechanisms to ensure security and trustworthiness of LLM applications. 2.1 Principal Approaches to AIGT Detection Broadly, AIGT detection methodologies fall into two primary categories: 1. Supervised Learning: This involves training models on labeled datasets to distinguish between human and AI-generated texts. Notable efforts
```

### Retrieved Chunk 7

- Source: `DetectLLM Leveraging Log-Rank Information for Zero-Shot Detection of Machine-Generated Text.pdf`
- Page: `0`
- Chunk ID: `1843`
- Chunk Type: `main`
- Dense Score: `unknown`
- Vector Score: `0.41239988803863525`
- BM25 Score: `12.191089759801827`
- Reranker Score: `5.261913299560547`

```text
to detect machine-generated text, preventing malicious use such as plagiarism, misinforma- tion, and propaganda. In this paper, we intro- duce two novel zero-shot methods for detecting machine-generated text by leveraging the Log- Rank information. One is called DetectLLM- LRR, which is fast and efficient, and the other is called DetectLLM-NPR, which is more ac- curate, but slower due to the need for perturba- tions. Our experiments on three datasets and seven language models show that our proposed methods improve over the state of the art by 3.9 and 1.75 AUROC points absolute. More- over, DetectLLM-NPR needs fewer perturba- tions than previous work to achieve the same level of performance, which makes it more practical for real-world use. We also investi- gate the efficiency-performance trade-off based on users’ preference for these two measures and provide intuition for using them in p
```

### Retrieved Chunk 8

- Source: `SeqXGPT Sentence-Level AI-Generated Text Detection.pdf`
- Page: `0`
- Chunk ID: `3395`
- Chunk Type: `main`
- Dense Score: `unknown`
- Vector Score: `0.38384005427360535`
- BM25 Score: `unknown`
- Reranker Score: `5.04334831237793`

```text
can efficiently conduct sentence-level AIGT detection. given text is written or modified by an AI system (Mitchell et al., 2023; Li et al., 2023). Current AIGT detection strategies, such as supervised-learned discriminator 2, perplexity- based methods (Mitchell et al., 2023; Li et al., 2023), etc., focus on discriminating whether a whole document is generated by an AI. However, users often modify partial texts with LLMs rather than put full trust in LLMs to generate a whole document. Therefore, it is important to explore fine-grained (e.g. sentence-level) AIGT detection. Building methods that solve the sentence-level AIGT detection challenge is not an incremental modification over document-level AIGT detection. On the one hand, model-wise methods like DetectGPT and Sniffer require a rather long document as input (over 100 tokens), making 2https://github.com/openai/ gpt-2-output-dataset a
```


### Manual Judgment

Please inspect the retrieved chunks and fill in:

- Which setting retrieves the most useful chunks?
- Does BM25 help with method names, abbreviations, or technical terms?
- Does dense retrieval help with semantic but non-exact matches?
- Does hybrid + reranker combine the advantages of both?
- Does hybrid retrieval reduce or increase noise?
- Overall winner: Dense only / BM25 only / Hybrid + reranker / Tie

---

## Statistical guarantee query

### Question

Which methods provide statistical guarantees for AI-generated text detection?

### Retrieval Modes

- Dense-only mode: `global`
- BM25-only mode: `global`
- Hybrid mode: `global`

### Candidate Papers

These should usually be similar because all three settings use the same paper-level routing.

#### Hybrid Candidate Papers

1. `AdaDetectGPT Adaptive Detection of LLM-Generated Text with Statistical Guarantees.pdf`
   - Title: AdaDetectGPT: Adaptive Detection of LLM-Generated Text with Statistical Guarantees
   - Paper score: `0.3299407660961151`

2. `Intrinsic Dimension Estimation for Robust Detection of AI-Generated Texts.pdf`
   - Title: Intrinsic Dimension Estimation for Robust Detection of AI Generated Texts
   - Paper score: `0.34540003538131714`

3. `Unsupervised and Distributional Detection of Machine-Generated Text.pdf`
   - Title: Unsupervised and Distributional Detection of Machine Generated Text
   - Paper score: `0.3520149886608124`

4. `SeqXGPT Sentence-Level AI-Generated Text Detection.pdf`
   - Title: SeqXGPT Sentence Level AI Generated Text Detection
   - Paper score: `0.355413556098938`


### Selected Papers

#### Dense-only Selected Papers

1. `AdaDetectGPT Adaptive Detection of LLM-Generated Text with Statistical Guarantees.pdf`
   - Title: AdaDetectGPT: Adaptive Detection of LLM-Generated Text with Statistical Guarantees
   - Paper score: `0.3299407660961151`

2. `Intrinsic Dimension Estimation for Robust Detection of AI-Generated Texts.pdf`
   - Title: Intrinsic Dimension Estimation for Robust Detection of AI Generated Texts
   - Paper score: `0.34540003538131714`

3. `Unsupervised and Distributional Detection of Machine-Generated Text.pdf`
   - Title: Unsupervised and Distributional Detection of Machine Generated Text
   - Paper score: `0.3520149886608124`

4. `SeqXGPT Sentence-Level AI-Generated Text Detection.pdf`
   - Title: SeqXGPT Sentence Level AI Generated Text Detection
   - Paper score: `0.355413556098938`


#### BM25-only Selected Papers

1. `AdaDetectGPT Adaptive Detection of LLM-Generated Text with Statistical Guarantees.pdf`
   - Title: AdaDetectGPT: Adaptive Detection of LLM-Generated Text with Statistical Guarantees
   - Paper score: `0.3299407660961151`

2. `Intrinsic Dimension Estimation for Robust Detection of AI-Generated Texts.pdf`
   - Title: Intrinsic Dimension Estimation for Robust Detection of AI Generated Texts
   - Paper score: `0.34540003538131714`

3. `Unsupervised and Distributional Detection of Machine-Generated Text.pdf`
   - Title: Unsupervised and Distributional Detection of Machine Generated Text
   - Paper score: `0.3520149886608124`

4. `SeqXGPT Sentence-Level AI-Generated Text Detection.pdf`
   - Title: SeqXGPT Sentence Level AI Generated Text Detection
   - Paper score: `0.355413556098938`


#### Hybrid Selected Papers

1. `AdaDetectGPT Adaptive Detection of LLM-Generated Text with Statistical Guarantees.pdf`
   - Title: AdaDetectGPT: Adaptive Detection of LLM-Generated Text with Statistical Guarantees
   - Paper score: `0.3299407660961151`

2. `Intrinsic Dimension Estimation for Robust Detection of AI-Generated Texts.pdf`
   - Title: Intrinsic Dimension Estimation for Robust Detection of AI Generated Texts
   - Paper score: `0.34540003538131714`

3. `Unsupervised and Distributional Detection of Machine-Generated Text.pdf`
   - Title: Unsupervised and Distributional Detection of Machine Generated Text
   - Paper score: `0.3520149886608124`

4. `SeqXGPT Sentence-Level AI-Generated Text Detection.pdf`
   - Title: SeqXGPT Sentence Level AI Generated Text Detection
   - Paper score: `0.355413556098938`


### Summary Statistics

| Metric | Dense only | BM25 only | Hybrid + reranker |
|---|---:|---:|---:|
| Retrieved chunks | 8 | 8 | 8 |
| Unique sources | 3 | 4 | 3 |
| Noisy chunks | 0 | 0 | 0 |
| Overlap with hybrid | 3 | 4 | 8 |

### Source Distribution

#### Dense only

- `Intrinsic Dimension Estimation for Robust Detection of AI-Generated Texts.pdf`: 3 chunks
- `SeqXGPT Sentence-Level AI-Generated Text Detection.pdf`: 3 chunks
- `Unsupervised and Distributional Detection of Machine-Generated Text.pdf`: 2 chunks

#### BM25 only

- `AdaDetectGPT Adaptive Detection of LLM-Generated Text with Statistical Guarantees.pdf`: 3 chunks
- `Intrinsic Dimension Estimation for Robust Detection of AI-Generated Texts.pdf`: 3 chunks
- `Unsupervised and Distributional Detection of Machine-Generated Text.pdf`: 1 chunks
- `SeqXGPT Sentence-Level AI-Generated Text Detection.pdf`: 1 chunks

#### Hybrid + reranker

- `SeqXGPT Sentence-Level AI-Generated Text Detection.pdf`: 3 chunks
- `AdaDetectGPT Adaptive Detection of LLM-Generated Text with Statistical Guarantees.pdf`: 3 chunks
- `Intrinsic Dimension Estimation for Robust Detection of AI-Generated Texts.pdf`: 2 chunks

### Dense-only Retrieved Chunks

### Retrieved Chunk 1

- Source: `Intrinsic Dimension Estimation for Robust Detection of AI-Generated Texts.pdf`
- Page: `6`
- Chunk ID: `2576`
- Chunk Type: `main`
- Dense Score: `0.32673242688179016`
- Vector Score: `0.32673242688179016`
- BM25 Score: `unknown`
- Reranker Score: `unknown`

```text
estimation, so we use this model for all further experiments in English, and XLM-R of the same size for multilingual experiments. Artificial text detection. We show that intrinsic dimension can lead to a robust method of artificial text detection. In all experiments below, we use the one-feature thresholding classifier (see Section 4). Comparison with universal detectors. First, we show that our detector is the best among general- purpose methods designed to detect texts of any domain, generated by any AI model, without access to the generator itself. Such methods are needed, e.g., for plagiarism detection. To be applicable in real life, the algorithm should provide high artificial text detection rate while avoiding false accusations of real authors. Besides, it should be resistant to adversaries who transform the content generated by popular AI models to reduce the chance to be caught. 
```

### Retrieved Chunk 2

- Source: `SeqXGPT Sentence-Level AI-Generated Text Detection.pdf`
- Page: `1`
- Chunk ID: `3398`
- Chunk Type: `main`
- Dense Score: `0.334208607673645`
- Vector Score: `0.334208607673645`
- BM25 Score: `unknown`
- Reranker Score: `unknown`

```text
existing methods, such as DetectGPT and Sniffer, fail to solve sentence-level AIGT detection. Our proposed SeqXGPT not only obtains promising results in both sentence and document-level AIGT detection challenges, but also exhibits excellent generalization on out-of-distribution datasets. 2 Background The proliferation of Large Language Models (LLMs) such as GPT-4 has given rise to increased concerns about the potential misuse of AI- generated texts (AIGT) (Brown et al., 2020; Zhang et al., 2022; Scao et al., 2022). This emphasizes the necessity for robust detection mechanisms to ensure security and trustworthiness of LLM applications. 2.1 Principal Approaches to AIGT Detection Broadly, AIGT detection methodologies fall into two primary categories: 1. Supervised Learning: This involves training models on labeled datasets to distinguish between human and AI-generated texts. Notable efforts
```

### Retrieved Chunk 3

- Source: `Intrinsic Dimension Estimation for Robust Detection of AI-Generated Texts.pdf`
- Page: `7`
- Chunk ID: `2580`
- Chunk Type: `main`
- Dense Score: `0.3349151015281677`
- Vector Score: `0.3349151015281677`
- BM25 Score: `unknown`
- Reranker Score: `unknown`

```text
et al., 2023]. When generated texts are transformed by DIPPER, they lose some characteristic features of the generator, which causes a dramatic drop in quality for most detectors; but for the PHD classifier the accuracy of artificial text detection even increases slightly after this perturbation. Interestingly, the MLE dimension estimator also works quite well for this task, and even achieves 6% better detection for GPT-3.5 generations; but its adversarial robustness is significantly worse. Cross-domain and cross-model performance. Table 3 shows that our ID estimation is stable across text domains; consequently, our proposed PHD text detector is robust to domain transfer. We compare the cross-domain ability of PHD with a supervised classifier obtained by fine-tuning RoBERTa- base with a linear classification head on its CLS token, a supervised classification approach used previously for 
```

### Retrieved Chunk 4

- Source: `SeqXGPT Sentence-Level AI-Generated Text Detection.pdf`
- Page: `2`
- Chunk ID: `3402`
- Chunk Type: `main`
- Dense Score: `0.3373628258705139`
- Vector Score: `0.3373628258705139`
- BM25 Score: `unknown`
- Reranker Score: `unknown`

```text
consisting of few sentences, which can potentially lead to a higher rate of false negatives or false positives. In response to this limitation, we aim to study sentence-level AIGT detection . Sentence-level AIGT detection offers a fine-grained text analysis compared to document-level AIGT detection, as it explores each sentence within the entire text. By addressing this challenge, we could significantly reduce the risk of misidentification and achieve both higher detection accuracy and finer detection granularity than document-level detection. Similarly, we study sentence-level detection challenges as follows: 1. Particular-Model Binary AIGT Detection: Discriminate whether each sentence within a candidate document is generated by a specific model or by a human. 2. Mixed-Model Binary AIGT Detection: Discriminate whether each sentence is generated by an AI model or a human, regardless of w
```

### Retrieved Chunk 5

- Source: `Intrinsic Dimension Estimation for Robust Detection of AI-Generated Texts.pdf`
- Page: `0`
- Chunk ID: `2543`
- Chunk Type: `main`
- Dense Score: `0.3454873561859131`
- Vector Score: `0.3454873561859131`
- BM25 Score: `unknown`
- Reranker Score: `unknown`

```text
Intrinsic Dimension Estimation for Robust Detection of AI-Generated Texts Eduard Tulchinskii1, Kristian Kuznetsov1, Laida Kushnareva2, Daniil Cherniavskii3, Sergey Nikolenko5, Evgeny Burnaev1,3, Serguei Barannikov1,4, Irina Piontkovskaya2 1Skolkovo Institute of Science and Technology, Russia; 2AI Foundation and Algorithm Lab, Russia; 3Artificial Intelligence Research Institute (AIRI), Russia;4CNRS, Université Paris Cité, France; 5St. Petersburg Department of the Steklov Institute of Mathematics, Russia Abstract Rapidly increasing quality of AI-generated content makes it difficult to distinguish between human and AI-generated texts, which may lead to undesirable conse- quences for society. Therefore, it becomes increasingly important to study the properties of human texts that are invariant over different text domains and varying proficiency of human writers, can be easily calculated for 
```

### Retrieved Chunk 6

- Source: `Unsupervised and Distributional Detection of Machine-Generated Text.pdf`
- Page: `0`
- Chunk ID: `3657`
- Chunk Type: `main`
- Dense Score: `0.3531365990638733`
- Vector Score: `0.3531365990638733`
- BM25 Score: `unknown`
- Reranker Score: `unknown`

```text
Unsupervised and Distributional Detection of Machine-Generated Text Matthias Gallé and Jos Rozen and Germán Kruszewski and Hady Elsahar Naver Labs Europe Abstract The power of natural language generation models has provoked a ﬂurry of interest in au- tomatic methods to detect if a piece of text is human or machine-authored. The problem so far has been framed in a standard super- vised way and consists in training a classiﬁer on annotated data to predict the origin of one given new document. In this paper, we frame the problem in an unsupervised and distribu- tional way: we assume that we have access to a large collection of unannotated documents, a big fraction of which is machine-generated. We propose a method to detect those machine-generated documents leveraging re- peated higher-order n-grams, which we show over-appear in machine-generated text as com- pared to human ones. That weak 
```

### Retrieved Chunk 7

- Source: `Unsupervised and Distributional Detection of Machine-Generated Text.pdf`
- Page: `1`
- Chunk ID: `3661`
- Chunk Type: `main`
- Dense Score: `0.3547978699207306`
- Vector Score: `0.3547978699207306`
- BM25 Score: `unknown`
- Reranker Score: `unknown`

```text
this precise setting and showed that the quality of a human/machine discriminator degraded quickly when the prompts used to generate text where from a different domain. On the other side, the problem of determining the origin of one ﬁxed document is in most use cases not the real problem. As an ex- ample, an article generated by an existing template- based data-to-text method (Reiter and Dale, 2000) is arguably of less concern than an article diffusing false information written by a human author. In- deed, one danger of the current language models lies in their capacity of generating a huge amount of human-like text but biased towards a desired opinion or topic (Leroux, 2020; Buchanan et al., 2021). We therefore frame the problem of detecting machine-generated texts as follows: given a set of documents, and the suspicion that a large fraction of them is generated by machine; is it possib
```

### Retrieved Chunk 8

- Source: `SeqXGPT Sentence-Level AI-Generated Text Detection.pdf`
- Page: `0`
- Chunk ID: `3395`
- Chunk Type: `main`
- Dense Score: `0.36551475524902344`
- Vector Score: `0.36551475524902344`
- BM25 Score: `unknown`
- Reranker Score: `unknown`

```text
can efficiently conduct sentence-level AIGT detection. given text is written or modified by an AI system (Mitchell et al., 2023; Li et al., 2023). Current AIGT detection strategies, such as supervised-learned discriminator 2, perplexity- based methods (Mitchell et al., 2023; Li et al., 2023), etc., focus on discriminating whether a whole document is generated by an AI. However, users often modify partial texts with LLMs rather than put full trust in LLMs to generate a whole document. Therefore, it is important to explore fine-grained (e.g. sentence-level) AIGT detection. Building methods that solve the sentence-level AIGT detection challenge is not an incremental modification over document-level AIGT detection. On the one hand, model-wise methods like DetectGPT and Sniffer require a rather long document as input (over 100 tokens), making 2https://github.com/openai/ gpt-2-output-dataset a
```


### BM25-only Retrieved Chunks

### Retrieved Chunk 1

- Source: `AdaDetectGPT Adaptive Detection of LLM-Generated Text with Statistical Guarantees.pdf`
- Page: `1`
- Chunk ID: `215`
- Chunk Type: `main`
- Dense Score: `unknown`
- Vector Score: `unknown`
- BM25 Score: `18.72273401446101`
- Reranker Score: `unknown`

```text
compute the logits – AdaDetectGPT achieves improvements over the best alternative in area under the curve (AUC) ranging from 12.5% to 37%. In black-box settings, where the source and target LLMs differ, it similarly offer gains of up to 20%. Theoretically, we provide statistical performance guarantees for AdaDetectGPT, deriving finite- sample error bounds for its TNR, FNR, true positive rate (TPR) and false positive rate (FPR). Existing literature on logits-based detectors generally lacks systematic statistical analysis. Our work aims to fill in this gap and contribute toward a deeper understanding of these methods in this emerging field, by offering a comprehensive analysis based on the aforementioned standard classification metrics. 1.1 Related works Existing methods for detecting machine-generated text generally fall into three categories: machine learning (ML)-based, statistics-based
```

### Retrieved Chunk 2

- Source: `AdaDetectGPT Adaptive Detection of LLM-Generated Text with Statistical Guarantees.pdf`
- Page: `15`
- Chunk ID: `285`
- Chunk Type: `main`
- Dense Score: `unknown`
- Vector Score: `unknown`
- BM25 Score: `14.140384631025539`
- Reranker Score: `unknown`

```text
Zhang, S., Song, Y ., Yang, J., Li, Y ., Han, B., and Tan, M. Detecting machine-generated texts by multi-population aware optimization for maximum mean discrepancy. InThe Twelfth International Conference on Learning Representations, 2024. Zhang, X., Zhao, J., and LeCun, Y . Character-level convolutional networks for text classification. InProceedings of the 29th International Conference on Neural Information Processing Systems - Volume 1, pp. 649–657, Cambridge, MA, USA, 2015. MIT Press. Zhao, X., Ananth, P. V ., Li, L., and Wang, Y .-X. Provable robust watermarking for AI-generated text. InThe Twelfth International Conference on Learning Representations, 2024. Zhou, H., Zhu, J., Xu, E., Ye, K., Yang, Y ., and Shi, C. Learn-to-distance: Distance learning for detect- ing llm-generated text. InThe Fourteenth International Conference on Learning Representations, 2026a. Zhou, H., Zhu, J., Ya
```

### Retrieved Chunk 3

- Source: `Unsupervised and Distributional Detection of Machine-Generated Text.pdf`
- Page: `1`
- Chunk ID: `3665`
- Chunk Type: `main`
- Dense Score: `unknown`
- Vector Score: `unknown`
- BM25 Score: `13.769405694212452`
- Reranker Score: `unknown`

```text
that of humans, which have a harder time picking up those statistical signals but are unbeaten so far when recognizing incoherence or factually wrong statements. Maronikolakis et al. (2020) obtains a similar conclusion that automatic models are better than humans for detecting fake headlines. Studying the performance of automatic classiﬁers, Bakhtin et al. (2021) provide an exhaustive analysis varying generator and discriminator architecture as well as training data, concluding that performance of the discrimiantor is high if it is trained on data from the same domain. However, any domain shift affects it in a severe way. Dugan et al. (2020) focuses specif- ically on the problem of detecting the boundary, from which moment the human generated prompt stops and the machine-written text starts. The fact that pre-trained language models have statistical patterns which differ from human-gener
```

### Retrieved Chunk 4

- Source: `Intrinsic Dimension Estimation for Robust Detection of AI-Generated Texts.pdf`
- Page: `0`
- Chunk ID: `2544`
- Chunk Type: `main`
- Dense Score: `unknown`
- Vector Score: `unknown`
- BM25 Score: `13.322657131256387`
- Reranker Score: `unknown`

```text
proficiency of human writers, can be easily calculated for any language, and can robustly separate natural and AI-generated texts regardless of the generation model and sampling method. In this work, we propose such an invariant for human- written texts, namely the intrinsic dimensionality of the manifold underlying the set of embeddings for a given text sample. We show that the average intrinsic dimensionality of fluent texts in a natural language is hovering around the value 9 for several alphabet-based languages and around 7 for Chinese, while the average intrinsic dimensionality of AI-generated texts for each language is ≈ 1.5 lower, with a clear statistical separation between human-generated and AI-generated distri- butions. This property allows us to build a score-based artificial text detector. The proposed detector’s accuracy is stable over text domains, generator models, and hum
```

### Retrieved Chunk 5

- Source: `AdaDetectGPT Adaptive Detection of LLM-Generated Text with Statistical Guarantees.pdf`
- Page: `0`
- Chunk ID: `210`
- Chunk Type: `main`
- Dense Score: `unknown`
- Vector Score: `unknown`
- BM25 Score: `12.857606390427538`
- Reranker Score: `unknown`

```text
text evaluated using the distribution function of a given source LLM. However, relying solely on log probabilities can be sub-optimal. In response, we introduce AdaDetectGPT – a novel classifier that adaptively learns a witness function from training data to enhance the performance of logits-based detectors. We provide statistical guarantees on its true positive rate, false positive rate, true negative rate and false negative rate. Extensive numerical studies show AdaDetectGPT nearly uniformly improves the state-of-the-art method in various combination of datasets and LLMs, and the improvement can reach up to 37%. A python implementation of our method is available athttps://github.com/Mamba413/AdaDetectGPT. 1 Introduction Large language models (LLMs) such as ChatGPT (OpenAI, 2022), PaLM (Chowdhery et al., 2023), Llama (Grattafiori et al., 2024) and DeepSeek (Bi et al., 2024) have revolut
```

### Retrieved Chunk 6

- Source: `SeqXGPT Sentence-Level AI-Generated Text Detection.pdf`
- Page: `2`
- Chunk ID: `3404`
- Chunk Type: `main`
- Dense Score: `unknown`
- Vector Score: `unknown`
- BM25 Score: `11.742563843476809`
- Reranker Score: `unknown`

```text
human-authored and AI-generated sentences. To ensure diversity while preserving coherence, we randomly select the first to third sentences from the human-generated documents as the prompt for subsequent AI sentence generation. Specifically, when generating the AI component of a document using language models such as GPT- 2, we utilize the prompt obtained via the above process to get the corresponding AI-generated sentences. In the case of instruction-tuned models like GPT-3.5-turbo, we provide specific instruction to assure the generation. We show instruction details in Appendix D. Regarding open-source models, we gather the AI-generated portions of a document from GPT-2 (Radford et al., 2019), GPT-J (Wang and Komatsuzaki, 2021), GPT-Neo (Black et al., 2022), and LLaMA (Touvron et al., 2023). For models which provide only partial access, we collect data from GPT-3.5-turbo, an instruction
```

### Retrieved Chunk 7

- Source: `Intrinsic Dimension Estimation for Robust Detection of AI-Generated Texts.pdf`
- Page: `0`
- Chunk ID: `2543`
- Chunk Type: `main`
- Dense Score: `unknown`
- Vector Score: `unknown`
- BM25 Score: `10.940328487596751`
- Reranker Score: `unknown`

```text
Intrinsic Dimension Estimation for Robust Detection of AI-Generated Texts Eduard Tulchinskii1, Kristian Kuznetsov1, Laida Kushnareva2, Daniil Cherniavskii3, Sergey Nikolenko5, Evgeny Burnaev1,3, Serguei Barannikov1,4, Irina Piontkovskaya2 1Skolkovo Institute of Science and Technology, Russia; 2AI Foundation and Algorithm Lab, Russia; 3Artificial Intelligence Research Institute (AIRI), Russia;4CNRS, Université Paris Cité, France; 5St. Petersburg Department of the Steklov Institute of Mathematics, Russia Abstract Rapidly increasing quality of AI-generated content makes it difficult to distinguish between human and AI-generated texts, which may lead to undesirable conse- quences for society. Therefore, it becomes increasingly important to study the properties of human texts that are invariant over different text domains and varying proficiency of human writers, can be easily calculated for 
```

### Retrieved Chunk 8

- Source: `Intrinsic Dimension Estimation for Robust Detection of AI-Generated Texts.pdf`
- Page: `6`
- Chunk ID: `2576`
- Chunk Type: `main`
- Dense Score: `unknown`
- Vector Score: `unknown`
- BM25 Score: `10.9063954952778`
- Reranker Score: `unknown`

```text
estimation, so we use this model for all further experiments in English, and XLM-R of the same size for multilingual experiments. Artificial text detection. We show that intrinsic dimension can lead to a robust method of artificial text detection. In all experiments below, we use the one-feature thresholding classifier (see Section 4). Comparison with universal detectors. First, we show that our detector is the best among general- purpose methods designed to detect texts of any domain, generated by any AI model, without access to the generator itself. Such methods are needed, e.g., for plagiarism detection. To be applicable in real life, the algorithm should provide high artificial text detection rate while avoiding false accusations of real authors. Besides, it should be resistant to adversaries who transform the content generated by popular AI models to reduce the chance to be caught. 
```


### Hybrid + Reranker Retrieved Chunks

### Retrieved Chunk 1

- Source: `SeqXGPT Sentence-Level AI-Generated Text Detection.pdf`
- Page: `1`
- Chunk ID: `3398`
- Chunk Type: `main`
- Dense Score: `unknown`
- Vector Score: `0.334208607673645`
- BM25 Score: `unknown`
- Reranker Score: `5.327617168426514`

```text
existing methods, such as DetectGPT and Sniffer, fail to solve sentence-level AIGT detection. Our proposed SeqXGPT not only obtains promising results in both sentence and document-level AIGT detection challenges, but also exhibits excellent generalization on out-of-distribution datasets. 2 Background The proliferation of Large Language Models (LLMs) such as GPT-4 has given rise to increased concerns about the potential misuse of AI- generated texts (AIGT) (Brown et al., 2020; Zhang et al., 2022; Scao et al., 2022). This emphasizes the necessity for robust detection mechanisms to ensure security and trustworthiness of LLM applications. 2.1 Principal Approaches to AIGT Detection Broadly, AIGT detection methodologies fall into two primary categories: 1. Supervised Learning: This involves training models on labeled datasets to distinguish between human and AI-generated texts. Notable efforts
```

### Retrieved Chunk 2

- Source: `AdaDetectGPT Adaptive Detection of LLM-Generated Text with Statistical Guarantees.pdf`
- Page: `1`
- Chunk ID: `215`
- Chunk Type: `main`
- Dense Score: `unknown`
- Vector Score: `unknown`
- BM25 Score: `18.72273401446101`
- Reranker Score: `5.063398361206055`

```text
compute the logits – AdaDetectGPT achieves improvements over the best alternative in area under the curve (AUC) ranging from 12.5% to 37%. In black-box settings, where the source and target LLMs differ, it similarly offer gains of up to 20%. Theoretically, we provide statistical performance guarantees for AdaDetectGPT, deriving finite- sample error bounds for its TNR, FNR, true positive rate (TPR) and false positive rate (FPR). Existing literature on logits-based detectors generally lacks systematic statistical analysis. Our work aims to fill in this gap and contribute toward a deeper understanding of these methods in this emerging field, by offering a comprehensive analysis based on the aforementioned standard classification metrics. 1.1 Related works Existing methods for detecting machine-generated text generally fall into three categories: machine learning (ML)-based, statistics-based
```

### Retrieved Chunk 3

- Source: `AdaDetectGPT Adaptive Detection of LLM-Generated Text with Statistical Guarantees.pdf`
- Page: `0`
- Chunk ID: `209`
- Chunk Type: `main`
- Dense Score: `unknown`
- Vector Score: `0.37700194120407104`
- BM25 Score: `11.511815394821955`
- Reranker Score: `4.880607604980469`

```text
AdaDetectGPT: Adaptive Detection of LLM-Generated Text with Statistical Guarantees Hongyi Zhou∗ Department of Mathematics Tsinghua University Beijing, China Jin Zhu∗ School of Mathematics University of Birmingham Birmingham, UK Pingfan Su Department of Statistics LSE London, UK Kai Ye Department of Statistics LSE London, UK Ying Yang Department of Statistics and Data Science Tsinghua University Beijing, China Shakeel A O B Gavioli-Akilagun† Department of Decision Analytics and Operations City University Hong Kong Hongkong, China Chengchun Shi† Department of Statistics LSE London, UK Abstract We study the problem of determining whether a piece of text has been authored by a human or by a large language model (LLM). Existing state of the art logits-based detectors make use of statistics derived from the log-probability of the observed text evaluated using the distribution function of a giv
```

### Retrieved Chunk 4

- Source: `Intrinsic Dimension Estimation for Robust Detection of AI-Generated Texts.pdf`
- Page: `6`
- Chunk ID: `2576`
- Chunk Type: `main`
- Dense Score: `unknown`
- Vector Score: `0.32673242688179016`
- BM25 Score: `10.9063954952778`
- Reranker Score: `4.126020431518555`

```text
estimation, so we use this model for all further experiments in English, and XLM-R of the same size for multilingual experiments. Artificial text detection. We show that intrinsic dimension can lead to a robust method of artificial text detection. In all experiments below, we use the one-feature thresholding classifier (see Section 4). Comparison with universal detectors. First, we show that our detector is the best among general- purpose methods designed to detect texts of any domain, generated by any AI model, without access to the generator itself. Such methods are needed, e.g., for plagiarism detection. To be applicable in real life, the algorithm should provide high artificial text detection rate while avoiding false accusations of real authors. Besides, it should be resistant to adversaries who transform the content generated by popular AI models to reduce the chance to be caught. 
```

### Retrieved Chunk 5

- Source: `SeqXGPT Sentence-Level AI-Generated Text Detection.pdf`
- Page: `1`
- Chunk ID: `3400`
- Chunk Type: `main`
- Dense Score: `unknown`
- Vector Score: `0.3669587969779968`
- BM25 Score: `unknown`
- Reranker Score: `4.082742214202881`

```text
a perturbation-based method leveraging average per-token log probabilities. The recent work of Li et al. (2023) extends this further by studying multi-model detection through text perplexities, aiming to trace the precise LLM origin of texts. 2.2 Detection Task Formulations The AIGT detection tasks can be formulated in different setups: 1. Particular-Model Binary AIGT Detection: In this setup, the objective is to discriminate whether a text was produced by a specific known AI model or by a human. Both GPTZero and DetectGPT fall into this category. 2. Mixed-Model Binary AIGT Detection: Here, the detectors are designed to identify AI-generated content without the need to pinpoint the exact model of origin. 3https://gptzero.me/
```

### Retrieved Chunk 6

- Source: `SeqXGPT Sentence-Level AI-Generated Text Detection.pdf`
- Page: `0`
- Chunk ID: `3395`
- Chunk Type: `main`
- Dense Score: `unknown`
- Vector Score: `0.36551475524902344`
- BM25 Score: `unknown`
- Reranker Score: `4.037962913513184`

```text
can efficiently conduct sentence-level AIGT detection. given text is written or modified by an AI system (Mitchell et al., 2023; Li et al., 2023). Current AIGT detection strategies, such as supervised-learned discriminator 2, perplexity- based methods (Mitchell et al., 2023; Li et al., 2023), etc., focus on discriminating whether a whole document is generated by an AI. However, users often modify partial texts with LLMs rather than put full trust in LLMs to generate a whole document. Therefore, it is important to explore fine-grained (e.g. sentence-level) AIGT detection. Building methods that solve the sentence-level AIGT detection challenge is not an incremental modification over document-level AIGT detection. On the one hand, model-wise methods like DetectGPT and Sniffer require a rather long document as input (over 100 tokens), making 2https://github.com/openai/ gpt-2-output-dataset a
```

### Retrieved Chunk 7

- Source: `Intrinsic Dimension Estimation for Robust Detection of AI-Generated Texts.pdf`
- Page: `0`
- Chunk ID: `2544`
- Chunk Type: `main`
- Dense Score: `unknown`
- Vector Score: `0.3520209789276123`
- BM25 Score: `13.322657131256387`
- Reranker Score: `3.231004238128662`

```text
proficiency of human writers, can be easily calculated for any language, and can robustly separate natural and AI-generated texts regardless of the generation model and sampling method. In this work, we propose such an invariant for human- written texts, namely the intrinsic dimensionality of the manifold underlying the set of embeddings for a given text sample. We show that the average intrinsic dimensionality of fluent texts in a natural language is hovering around the value 9 for several alphabet-based languages and around 7 for Chinese, while the average intrinsic dimensionality of AI-generated texts for each language is ≈ 1.5 lower, with a clear statistical separation between human-generated and AI-generated distri- butions. This property allows us to build a score-based artificial text detector. The proposed detector’s accuracy is stable over text domains, generator models, and hum
```

### Retrieved Chunk 8

- Source: `AdaDetectGPT Adaptive Detection of LLM-Generated Text with Statistical Guarantees.pdf`
- Page: `15`
- Chunk ID: `285`
- Chunk Type: `main`
- Dense Score: `unknown`
- Vector Score: `0.37250983715057373`
- BM25 Score: `14.140384631025539`
- Reranker Score: `3.227660655975342`

```text
Zhang, S., Song, Y ., Yang, J., Li, Y ., Han, B., and Tan, M. Detecting machine-generated texts by multi-population aware optimization for maximum mean discrepancy. InThe Twelfth International Conference on Learning Representations, 2024. Zhang, X., Zhao, J., and LeCun, Y . Character-level convolutional networks for text classification. InProceedings of the 29th International Conference on Neural Information Processing Systems - Volume 1, pp. 649–657, Cambridge, MA, USA, 2015. MIT Press. Zhao, X., Ananth, P. V ., Li, L., and Wang, Y .-X. Provable robust watermarking for AI-generated text. InThe Twelfth International Conference on Learning Representations, 2024. Zhou, H., Zhu, J., Xu, E., Ye, K., Yang, Y ., and Shi, C. Learn-to-distance: Distance learning for detect- ing llm-generated text. InThe Fourteenth International Conference on Learning Representations, 2026a. Zhou, H., Zhu, J., Ya
```


### Manual Judgment

Please inspect the retrieved chunks and fill in:

- Which setting retrieves the most useful chunks?
- Does BM25 help with method names, abbreviations, or technical terms?
- Does dense retrieval help with semantic but non-exact matches?
- Does hybrid + reranker combine the advantages of both?
- Does hybrid retrieval reduce or increase noise?
- Overall winner: Dense only / BM25 only / Hybrid + reranker / Tie

---

## Comparison between DetectGPT and AdaDetectGPT

### Question

What is the difference between DetectGPT and AdaDetectGPT?

### Retrieval Modes

- Dense-only mode: `global`
- BM25-only mode: `global`
- Hybrid mode: `global`

### Candidate Papers

These should usually be similar because all three settings use the same paper-level routing.

#### Hybrid Candidate Papers

1. `AdaDetectGPT Adaptive Detection of LLM-Generated Text with Statistical Guarantees.pdf`
   - Title: AdaDetectGPT: Adaptive Detection of LLM-Generated Text with Statistical Guarantees
   - Paper score: `0.6266366839408875`

2. `DetectGPT Zero-Shot Machine-Generated Text Detection using Probability Curvature.pdf`
   - Title: DetectGPT: Zero-Shot Machine-Generated Text Detection using Probability Curvature
   - Paper score: `0.6826760172843933`

3. `Fast-DetectGPT Efficient Zero-Shot Detection of Machine-Generated Text via Conditional Probability Curvature.pdf`
   - Title: Fast DetectGPT Efficient Zero Shot Detection of Machine Generated Text via Conditional Probability Curvature
   - Paper score: `0.6828979849815369`

4. `DetectGPT-SC Improving Detection of Text Generated by Large Language Models through Self-Consistency with Masked Predictions.pdf`
   - Title: DetectGPT SC Improving Detection of Text Generated by Large Language Models through Self Consistency with Masked Predictions
   - Paper score: `0.6932278871536255`


### Selected Papers

#### Dense-only Selected Papers

1. `AdaDetectGPT Adaptive Detection of LLM-Generated Text with Statistical Guarantees.pdf`
   - Title: AdaDetectGPT: Adaptive Detection of LLM-Generated Text with Statistical Guarantees
   - Paper score: `0.6266366839408875`

2. `DetectGPT Zero-Shot Machine-Generated Text Detection using Probability Curvature.pdf`
   - Title: DetectGPT: Zero-Shot Machine-Generated Text Detection using Probability Curvature
   - Paper score: `0.6826760172843933`

3. `Fast-DetectGPT Efficient Zero-Shot Detection of Machine-Generated Text via Conditional Probability Curvature.pdf`
   - Title: Fast DetectGPT Efficient Zero Shot Detection of Machine Generated Text via Conditional Probability Curvature
   - Paper score: `0.6828979849815369`

4. `DetectGPT-SC Improving Detection of Text Generated by Large Language Models through Self-Consistency with Masked Predictions.pdf`
   - Title: DetectGPT SC Improving Detection of Text Generated by Large Language Models through Self Consistency with Masked Predictions
   - Paper score: `0.6932278871536255`


#### BM25-only Selected Papers

1. `AdaDetectGPT Adaptive Detection of LLM-Generated Text with Statistical Guarantees.pdf`
   - Title: AdaDetectGPT: Adaptive Detection of LLM-Generated Text with Statistical Guarantees
   - Paper score: `0.6266366839408875`

2. `DetectGPT Zero-Shot Machine-Generated Text Detection using Probability Curvature.pdf`
   - Title: DetectGPT: Zero-Shot Machine-Generated Text Detection using Probability Curvature
   - Paper score: `0.6826760172843933`

3. `Fast-DetectGPT Efficient Zero-Shot Detection of Machine-Generated Text via Conditional Probability Curvature.pdf`
   - Title: Fast DetectGPT Efficient Zero Shot Detection of Machine Generated Text via Conditional Probability Curvature
   - Paper score: `0.6828979849815369`

4. `DetectGPT-SC Improving Detection of Text Generated by Large Language Models through Self-Consistency with Masked Predictions.pdf`
   - Title: DetectGPT SC Improving Detection of Text Generated by Large Language Models through Self Consistency with Masked Predictions
   - Paper score: `0.6932278871536255`


#### Hybrid Selected Papers

1. `AdaDetectGPT Adaptive Detection of LLM-Generated Text with Statistical Guarantees.pdf`
   - Title: AdaDetectGPT: Adaptive Detection of LLM-Generated Text with Statistical Guarantees
   - Paper score: `0.6266366839408875`

2. `DetectGPT Zero-Shot Machine-Generated Text Detection using Probability Curvature.pdf`
   - Title: DetectGPT: Zero-Shot Machine-Generated Text Detection using Probability Curvature
   - Paper score: `0.6826760172843933`

3. `Fast-DetectGPT Efficient Zero-Shot Detection of Machine-Generated Text via Conditional Probability Curvature.pdf`
   - Title: Fast DetectGPT Efficient Zero Shot Detection of Machine Generated Text via Conditional Probability Curvature
   - Paper score: `0.6828979849815369`

4. `DetectGPT-SC Improving Detection of Text Generated by Large Language Models through Self-Consistency with Masked Predictions.pdf`
   - Title: DetectGPT SC Improving Detection of Text Generated by Large Language Models through Self Consistency with Masked Predictions
   - Paper score: `0.6932278871536255`


### Summary Statistics

| Metric | Dense only | BM25 only | Hybrid + reranker |
|---|---:|---:|---:|
| Retrieved chunks | 8 | 8 | 8 |
| Unique sources | 3 | 3 | 3 |
| Noisy chunks | 0 | 0 | 0 |
| Overlap with hybrid | 2 | 1 | 8 |

### Source Distribution

#### Dense only

- `AdaDetectGPT Adaptive Detection of LLM-Generated Text with Statistical Guarantees.pdf`: 3 chunks
- `Fast-DetectGPT Efficient Zero-Shot Detection of Machine-Generated Text via Conditional Probability Curvature.pdf`: 3 chunks
- `DetectGPT Zero-Shot Machine-Generated Text Detection using Probability Curvature.pdf`: 2 chunks

#### BM25 only

- `AdaDetectGPT Adaptive Detection of LLM-Generated Text with Statistical Guarantees.pdf`: 3 chunks
- `DetectGPT-SC Improving Detection of Text Generated by Large Language Models through Self-Consistency with Masked Predictions.pdf`: 3 chunks
- `DetectGPT Zero-Shot Machine-Generated Text Detection using Probability Curvature.pdf`: 2 chunks

#### Hybrid + reranker

- `AdaDetectGPT Adaptive Detection of LLM-Generated Text with Statistical Guarantees.pdf`: 4 chunks
- `DetectGPT Zero-Shot Machine-Generated Text Detection using Probability Curvature.pdf`: 3 chunks
- `DetectGPT-SC Improving Detection of Text Generated by Large Language Models through Self-Consistency with Masked Predictions.pdf`: 1 chunks

### Dense-only Retrieved Chunks

### Retrieved Chunk 1

- Source: `AdaDetectGPT Adaptive Detection of LLM-Generated Text with Statistical Guarantees.pdf`
- Page: `9`
- Chunk ID: `255`
- Chunk Type: `main`
- Dense Score: `0.366325318813324`
- Vector Score: `0.366325318813324`
- BM25 Score: `unknown`
- Reranker Score: `unknown`

```text
Fast-DetectGPT 0.9048 0.95880.98470.9800 0.9571 0.9019 0.93610.97680.9608 0.9439 AdaDetectGPT 0.90720.96110.98320.9841 0.95890.91760.94000.97280.9610 0.9478 Relative ( ) 2.4288 5.6095 — 20.4444 4.2454 16.0326 6.0543 — 0.3405 6.9929 Table 3: Detection of LLM-generated text under two adversarial attacks in black-box settings. Paraphrasing Decoherence DetectGPT Xsum Writing PubMed Avg. Xsum Writing PubMed Avg. Fast (GPT-J/GPT-2) 0.91780.91370.7944 0.8753 0.7884 0.9595 0.7870 0.8449 Ada (GPT-J/GPT-2)0.92250.91210.8029 0.8792 0.8765 0.9597 0.8284 0.8882 Fast (GPT-J/Neo-2.7) 0.96020.91850.7310 0.8699 0.8579 0.9701 0.7609 0.8630 Ada (GPT-J/Neo-2.7)0.96230.91810.7587 0.8797 0.9230 0.9704 0.8124 0.9019 Fast (GPT-J/GPT-J) 0.95370.94580.7041 0.8679 0.88360.98690.7550 0.8752 Ada (GPT-J/GPT-J)0.95870.94490.7308 0.8781 0.93360.98640.8008 0.9070 underperforms Binoculars or RADAR. Nonetheless, AdaDetect
```

### Retrieved Chunk 2

- Source: `AdaDetectGPT Adaptive Detection of LLM-Generated Text with Statistical Guarantees.pdf`
- Page: `9`
- Chunk ID: `256`
- Chunk Type: `main`
- Dense Score: `0.3740534782409668`
- Vector Score: `0.3740534782409668`
- BM25 Score: `unknown`
- Reranker Score: `unknown`

```text
underperforms Binoculars or RADAR. Nonetheless, AdaDetectGPT consistently improves upon Fast-DetectGPT across various datasets, with gains on Essay reaching up to 37.8%. Additionally, we evaluate AdaDetectGPT’s robustness to two adversarial attacks, paraphrasing and decoherence, in the black-box setting. As shown in Table 3, AdaDetectGPT demonstrates greater resilience than Fast-DetectGPT to adversarially perturbed texts. The improvement reaches up to 10% for paraphrasing and up to 85% for decoherence. Finally, we employ the same five LLMs from Table 1 to compare Fast-DetectGPT and AdaDetectGPT in black-box settings. Following Bao et al. (2024), we use GPT-J as the source LLM for detecting each of the remaining four target LLMs. Due to space constraints, the results are presented in Table S11 of Appendix F.5, where AdaDetectGPT uniformly outperforms Fast-DetectGPT in all cases, with impr
```

### Retrieved Chunk 3

- Source: `AdaDetectGPT Adaptive Detection of LLM-Generated Text with Statistical Guarantees.pdf`
- Page: `8`
- Chunk ID: `251`
- Chunk Type: `main`
- Dense Score: `0.4149060547351837`
- Vector Score: `0.4149060547351837`
- BM25 Score: `unknown`
- Reranker Score: `unknown`

```text
AdaDetectGPT0.8534 0.8420 0.8532 0.8347 0.8061 0.8379 Relative ( ) 14.1250 18.2659 21.1936 20.3301 18.4492 18.5779 reports the AUC scores of various detectors across all combinations of datasets and five source models. It can be seen that AdaDetectGPT achieves the highest AUC across all combinations of datasets and source models, outperforming Fast-DetectGPT – the best baseline method – by 12.5%-37%. We also evaluate AdaDetectGPT on three more advanced open-source LLMs: Qwen2.5 (Bai et al., 2025), Mistral (Jiang et al., 2023), and LLaMA3 (Grattafiori et al., 2024). As shown in Table S7, AdaDetectGPT delivers consistent improvements over Fast-DetectGPT and maintains competitive performance across five datasets, achieving the best results in most cases. These findings highlight the advantage of using an adaptively learned witness function for classification. In Appendix F.3, we analyze the
```

### Retrieved Chunk 4

- Source: `Fast-DetectGPT Efficient Zero-Shot Detection of Machine-Generated Text via Conditional Probability Curvature.pdf`
- Page: `20`
- Chunk ID: `2293`
- Chunk Type: `main`
- Dense Score: `0.45760059356689453`
- Vector Score: `0.45760059356689453`
- BM25 Score: `unknown`
- Reranker Score: `unknown`

```text
DetectGPT .9875 .9793 .9961 .9762 .95 .9869 .9707 .9919 .9619 .9424 .9928 .9856 .9953 .979 .9622 Fast-DetectGPT .9994 .9965 .9988 .997 .9958 .9954 .9867 .9938 .9826 .9773 .9999 .9999 .9997 .9999 .9997 (Diff) .0119 .0172 .0028 .0208 .0458 .0085 .0160 .0018 .0207 .0349 .0071 .0143 .0044 .0209 .0376 DetectGPT(fixed) .9399 .9438 .9961 .9367 .9214 .9143 .9026 .9919 .8846 .8854 .9722 .9635 .9953 .9627 .9646 Fast-Detect(fixed) .9953 .9861 .9997 .9856 .9779 .9805 .9613 .9979 .9499 .9311 .9978 .999 .9999 .9991 .998 (Diff) .0554 .0423 .0036 .0489 .0565 .0662 .0587 .0060 .0654 .0457 .0256 .0355 .0046 .0364 .0333 SQuAD Likelihood .961 .944 .9214 .8838 .8122 .9393 .9072 .8926 .8351 .7317 .9906 .987 .9792 .9572 .9094 Entropy .5369 .4736 .539 .5277 .5593 .552 .5203 .5457 .5441 .5992 .5132 .4508 .4924 .4882 .5263 LogRank .9792 .9657 .9535 .9156 .8482 .9692 .9423 .9385 .8842 .7895 .9972 .9959 .994 .9798 
```

### Retrieved Chunk 5

- Source: `Fast-DetectGPT Efficient Zero-Shot Detection of Machine-Generated Text via Conditional Probability Curvature.pdf`
- Page: `18`
- Chunk ID: `2283`
- Chunk Type: `main`
- Dense Score: `0.5024181604385376`
- Vector Score: `0.5024181604385376`
- BM25 Score: `unknown`
- Reranker Score: `unknown`

```text
Fast-DetectGPT (GPT-J/Neo-2.7) 0.9396 0.9492 0.7225 0.8704* Fast-DetectGPT (GPT-J/GPT-J) 0.9329* 0.9568 0.6664 0.8520 Table 7: Detection of GPT-3 generations, evaluated in AUROC. Fast-DetectGPT in the black-box settings (using local models) significantly outperforms DetectGPT in both the black-box setting and the white-box setting (using GPT-3) on News (XSum) and story (WritingPrompts). Fast-DetectGPT uses 6B GPT-J to generate samples and models from 1.5B GPT-2 to 6B GPT-J to score samples, while DetectGPT uses 11B T5 to generate perturbations and models from 1.5B GPT-2 to 6B GPT-J, and GPT-3 service to score them.♢ – we report the official scores from Mitchell et al. (2023) instead of rerunning the experiments after confirming the consistency on RoBERTa-base/large. Table 7 presents a comparison between Fast-DetectGPT, zero-shot DetectGPT, and supervised RoBERTa-based classifiers for the
```

### Retrieved Chunk 6

- Source: `Fast-DetectGPT Efficient Zero-Shot Detection of Machine-Generated Text via Conditional Probability Curvature.pdf`
- Page: `21`
- Chunk ID: `2297`
- Chunk Type: `main`
- Dense Score: `0.5080249905586243`
- Vector Score: `0.5080249905586243`
- BM25 Score: `unknown`
- Reranker Score: `unknown`

```text
Published as a conference paper at ICLR 2024 used in Table 2, sampling with the three strategies with k = 40 , p = 0 .96, and T = 0 .8. Fast- DetectGPT in the white-box setting obtains the best accuracy on the three sampling strategies, out- performing DetectGPT by relative 95% on Top- p sampling, relative 81% on Top- k sampling, and relative 99% on sampling with a temperature, as shown in Table 9. In the black-box setting, Fast- DetectGPT outperforms DetectGPT by relatively 92%, 80%, and 98% on the three decoding strate- gies, respectively. These results demonstrate that Fast-DetectGPT works consistently in detecting texts produced by different decoding strategies. To elucidate the trajectory of detection accuracy concerning variations in sampling hyper- parameters, we conducted additional experiments with values set top = 0.90, k = 30, and T = 0.6. As indicated in the lower segment of 
```

### Retrieved Chunk 7

- Source: `DetectGPT Zero-Shot Machine-Generated Text Detection using Probability Curvature.pdf`
- Page: `6`
- Chunk ID: `1474`
- Chunk Type: `main`
- Dense Score: `0.5336488485336304`
- Vector Score: `0.5336488485336304`
- BM25 Score: `unknown`
- Reranker Score: `unknown`

```text
tectGPT maintains detection AUROC above 0.8 even when nearly a quarter of the text in model samples has been re- placed. Unsurprisingly, almost all methods show a gradual degradation in performance as the sample is more heavily revised. The entropy baseline shows surprisingly robust performance in this setting (althought it is least accurate on average), even slightly improving detection performance up to 24% replacement. DetectGPT shows the strongest detection performance for all revision levels. Impact of alternative decoding strategies on detection. While Table 1 suggests that DetectGPT is effective for 5We reduce the number of evaluation samples from 500 in our main experiments to reduce the API costs of these experiments. XSum SQuAD WritingPrompts Method top- p top-k top-p top-k top-p top-k log p(x) 0.92 0.87 0.89 0.85 0.98 0.96 Rank 0.76 0.76 0.81 0.80 0.84 0.83 LogRank 0.93* 0.90*
```

### Retrieved Chunk 8

- Source: `DetectGPT Zero-Shot Machine-Generated Text Detection using Probability Curvature.pdf`
- Page: `12`
- Chunk ID: `1508`
- Chunk Type: `main`
- Dense Score: `0.5422935485839844`
- Vector Score: `0.5422935485839844`
- BM25 Score: `unknown`
- Reranker Score: `unknown`

```text
Table 5. Top-k sampling evaluation with k = 40 . DetectGPT generally provides the most accurate performance (highest AUROC), although the gap is narrowed comparing to direct sampling, presumably because top-k generations are more generic. 13
```


### BM25-only Retrieved Chunks

### Retrieved Chunk 1

- Source: `AdaDetectGPT Adaptive Detection of LLM-Generated Text with Statistical Guarantees.pdf`
- Page: `4`
- Chunk ID: `229`
- Chunk Type: `main`
- Dense Score: `unknown`
- Vector Score: `unknown`
- BM25 Score: `24.61733296769065`
- Reranker Score: `unknown`

```text
0 1 2 3 Differences in statistical measures 0 1 FastDetectGPT AdaDetectGPT Dataset: SQuAD 1  0 1 2 3 4 Differences in statistical measures 0 1 FastDetectGPT AdaDetectGPT Dataset: Writing Figure 2: Boxplots visualizing the differences in the statistical measures between human- and LLM- authored passages, comparing AdaDetectGPT (with a learned witness function) and Fast-DetectGPT (without it). A larger positive difference from zero indicates better detection power. As observed, the difference computed by AdaDetectGPT is consistently larger than that of Fast-DetectGPT across the first quartile, median, and third quartile. The left panel shows statistics evaluated on the SQuAD dataset, while the right panel displays results for the WritingPrompts dataset. function. Next, in Part (d), we extend our proposal to the black-box setting. Finally, in Part (e), we establish the statistical propertie
```

### Retrieved Chunk 2

- Source: `AdaDetectGPT Adaptive Detection of LLM-Generated Text with Statistical Guarantees.pdf`
- Page: `8`
- Chunk ID: `252`
- Chunk Type: `main`
- Dense Score: `unknown`
- Vector Score: `unknown`
- BM25 Score: `18.902450751628603`
- Reranker Score: `unknown`

```text
In Appendix F.3, we analyze the computational costof AdaDetectGPT. Training the witness function typically requires less than one minute across different sample sizes and dimensions, with memory usage below 0.5 GB. In Appendix F.4, we further conduct a sensitivity analysisto investigate the sensitivity of AdaDetectGPT’s AUC score to various factors that may affect the estimation of the witness function. Our results show that AdaDetectGPT is generally robust to the size of training data, the number of B-spline features, and the distributional shift between training and test data, consistently maintaining superior performance over baselines. Black-box results. We next consider the black-box setting, where the task is to detect text generated by three widely used advanced LLMs: GPT-4o (Hurst et al., 2024), Claude-3.5-Haiku (Anthropic, 2024), and Gemini-2.5-Flash (Comanici et al., 2025). In 
```

### Retrieved Chunk 3

- Source: `AdaDetectGPT Adaptive Detection of LLM-Generated Text with Statistical Guarantees.pdf`
- Page: `38`
- Chunk ID: `361`
- Chunk Type: `main`
- Dense Score: `unknown`
- Vector Score: `unknown`
- BM25 Score: `17.8198003691338`
- Reranker Score: `unknown`

```text
n100 150 200 250 300 350 Runtime (Memory) 9.28(0.36) 23.45(0.37) 40.19(0.37) 44.25(0.37) 59.57(0.60) 69.56(0.37) F.4 Sensitivity analysis Since AdaDetectGPT requires training a witness function, we examine three factors influencing its performance: (1) the size of the training set; (ii) tuning parameters for generating B-spline basis and (iii) distribution shift between training and test data. Robust to training data sizes. We evaluate AdaDetectGPT across varying dataset sizes by setting n1 =n 2 ∈ {100,200,300,400,500,600} for both human- and machine-generated texts. Figure S5 demonstrates that AdaDetectGPT clearly outperforms FastDetectGPT when sample size is large. This is expected because a larger sample size leads to a more accurate estimation of w. Notably, even with limited data n1 =n 2 = 100, AdaDetectGPT maintains superior accuracy compared to baseline methods, though the perform
```

### Retrieved Chunk 4

- Source: `DetectGPT Zero-Shot Machine-Generated Text Detection using Probability Curvature.pdf`
- Page: `3`
- Chunk ID: `1455`
- Chunk Type: `main`
- Dense Score: `unknown`
- Vector Score: `unknown`
- BM25 Score: `16.229959214625115`
- Reranker Score: `unknown`

```text
used to estimate the expectation effectively allows for trading off between accuracy and speed. AUROC by around 0.020, so we use this normalized version of the perturbation discrepancy in our experiments. The resulting method, DetectGPT, is summarized in Alg. 1. Hav- ing described an application of the perturbation discrepancy to machine-generated text detection, we next provide an interpretation of this quantity. Interpretation of perturbation discrepancy as curvature While Figure 3 suggests that the perturbation discrepancy may be useful, it is not immediately obvious what it mea- sures. In this section, we show that the perturbation dis- crepancy approximates a measure of the local curvature of the log probability function near the candidate passage, more specifically, that it is proportional to the negative trace of the Hessian of the log probability function. 2 To han- dle the non-d
```

### Retrieved Chunk 5

- Source: `DetectGPT-SC Improving Detection of Text Generated by Large Language Models through Self-Consistency with Masked Predictions.pdf`
- Page: `2`
- Chunk ID: `1517`
- Chunk Type: `main`
- Dense Score: `unknown`
- Vector Score: `unknown`
- BM25 Score: `14.628150567936359`
- Reranker Score: `unknown`

```text
Running Title for Header 2 Related Work Recent research has shown promising results in the development of detection methods. The existing detectors are built on the assumption that there is a distributional difference between human-generated texts and AI-generated texts. These differences are typically identified by training classifiers or using statistical information. Classifier-based detectors. Classifier-based detectors are commonly used in natural language processing detection paradigms, especially in fake news and misinformation detection [3]. Guo et al. [4] proposed the ChatGPT Detector, where they initially constructed a dataset consisting of ChatGPT conversations with human questions and answers, and trained a text detection classifier based on this dataset. The use of these methods requires substantial data collection and incurs the cost of training these classifier models.
```

### Retrieved Chunk 6

- Source: `DetectGPT-SC Improving Detection of Text Generated by Large Language Models through Self-Consistency with Masked Predictions.pdf`
- Page: `0`
- Chunk ID: `1512`
- Chunk Type: `main`
- Dense Score: `unknown`
- Vector Score: `unknown`
- BM25 Score: `13.94770994228422`
- Reranker Score: `unknown`

```text
challenges, not only rendering equitable student assessment more complex but also impeding student learning while amplifying the presence of persuasive yet erroneous news articles. Unfortunately, when classifying AI-generated and human-generated texts, humans perform only slightly better than random guessing [1], leading researchers to consider automated detection that can identify signals that are difficult for humans to detect. The foundation of current text detection is based on an assumption that there is a distributional difference between AI-generated texts and human-generated texts. These differences are typically ascertained by employing statistical information or training classifiers [9]. Recent research has delved deeper into understanding the unique capabilities of large language models, such as self-consistency as introduced by Wang et al. [8]. Wang et al. [8] introduced a ne
```

### Retrieved Chunk 7

- Source: `DetectGPT-SC Improving Detection of Text Generated by Large Language Models through Self-Consistency with Masked Predictions.pdf`
- Page: `2`
- Chunk ID: `1521`
- Chunk Type: `main`
- Dense Score: `unknown`
- Vector Score: `unknown`
- BM25 Score: `13.585605327591832`
- Reranker Score: `unknown`

```text
model that represents words as vectors and captures the semantic relationships between them. By calculating the cosine similarity between P ( ˆXi), i = 1, 2, 3 and ˆXi, i = 1, 2, 3 in the vector space, we can evaluate their semantic similarity. The cosine similarity is shown as follows: BARTSCORE = mX t=1 ωt log p (yt | y< t, x, θ) (1) Finally, we utilize BARTScore [11] to calculate the similarity between P ( ˆX) and X, which enables us to assess the similarity between the generated texts and the original text. BARTScore compares the similarity between two text sequences and provides a comprehensive similarity score. It evaluates the overall similarity between the generated texts and the original text, including aspects such as syntactic structure and contextual coherence. The BARTScore is shown as follows: Cosine Similarity = P ( ˆX) · XP ( ˆX)  · |X| (2) 3
```

### Retrieved Chunk 8

- Source: `DetectGPT Zero-Shot Machine-Generated Text Detection using Probability Curvature.pdf`
- Page: `7`
- Chunk ID: `1482`
- Chunk Type: `main`
- Dense Score: `unknown`
- Vector Score: `unknown`
- BM25 Score: `13.554880391797843`
- Reranker Score: `unknown`

```text
ples. A threshold of slightly below 0.1 separates human and model texts across data distributions, which is important for practical scenarios in which a passage may be analyzed with- out knowing its domain a priori. Finally, Figure 10 shows an analysis of DetectGPT’s performance as a function of pas- sage length. We bin the paired human- and model-generated sequences by their average length into three bins of equal size (bottom/middle/top third), and plot the AUROC within each bin. The relationship between detection performance and passage length generally depends on the dataset and model (or tokenizer). For very long sequences, DetectGPT may see reduced performance because our implementation of DetectGPT applies all T5 mask-filling perturbations at once, and T5 may fail to track many mask tokens at once. By applying perturbations in multiple sequential rounds of smaller numbers of masks
```


### Hybrid + Reranker Retrieved Chunks

### Retrieved Chunk 1

- Source: `AdaDetectGPT Adaptive Detection of LLM-Generated Text with Statistical Guarantees.pdf`
- Page: `4`
- Chunk ID: `229`
- Chunk Type: `main`
- Dense Score: `unknown`
- Vector Score: `0.4683022201061249`
- BM25 Score: `24.61733296769065`
- Reranker Score: `6.326869010925293`

```text
0 1 2 3 Differences in statistical measures 0 1 FastDetectGPT AdaDetectGPT Dataset: SQuAD 1  0 1 2 3 4 Differences in statistical measures 0 1 FastDetectGPT AdaDetectGPT Dataset: Writing Figure 2: Boxplots visualizing the differences in the statistical measures between human- and LLM- authored passages, comparing AdaDetectGPT (with a learned witness function) and Fast-DetectGPT (without it). A larger positive difference from zero indicates better detection power. As observed, the difference computed by AdaDetectGPT is consistently larger than that of Fast-DetectGPT across the first quartile, median, and third quartile. The left panel shows statistics evaluated on the SQuAD dataset, while the right panel displays results for the WritingPrompts dataset. function. Next, in Part (d), we extend our proposal to the black-box setting. Finally, in Part (e), we establish the statistical propertie
```

### Retrieved Chunk 2

- Source: `AdaDetectGPT Adaptive Detection of LLM-Generated Text with Statistical Guarantees.pdf`
- Page: `9`
- Chunk ID: `256`
- Chunk Type: `main`
- Dense Score: `unknown`
- Vector Score: `0.3740534782409668`
- BM25 Score: `unknown`
- Reranker Score: `4.36726713180542`

```text
underperforms Binoculars or RADAR. Nonetheless, AdaDetectGPT consistently improves upon Fast-DetectGPT across various datasets, with gains on Essay reaching up to 37.8%. Additionally, we evaluate AdaDetectGPT’s robustness to two adversarial attacks, paraphrasing and decoherence, in the black-box setting. As shown in Table 3, AdaDetectGPT demonstrates greater resilience than Fast-DetectGPT to adversarially perturbed texts. The improvement reaches up to 10% for paraphrasing and up to 85% for decoherence. Finally, we employ the same five LLMs from Table 1 to compare Fast-DetectGPT and AdaDetectGPT in black-box settings. Following Bao et al. (2024), we use GPT-J as the source LLM for detecting each of the remaining four target LLMs. Due to space constraints, the results are presented in Table S11 of Appendix F.5, where AdaDetectGPT uniformly outperforms Fast-DetectGPT in all cases, with impr
```

### Retrieved Chunk 3

- Source: `AdaDetectGPT Adaptive Detection of LLM-Generated Text with Statistical Guarantees.pdf`
- Page: `0`
- Chunk ID: `210`
- Chunk Type: `main`
- Dense Score: `unknown`
- Vector Score: `unknown`
- BM25 Score: `16.138881097467298`
- Reranker Score: `2.6803369522094727`

```text
text evaluated using the distribution function of a given source LLM. However, relying solely on log probabilities can be sub-optimal. In response, we introduce AdaDetectGPT – a novel classifier that adaptively learns a witness function from training data to enhance the performance of logits-based detectors. We provide statistical guarantees on its true positive rate, false positive rate, true negative rate and false negative rate. Extensive numerical studies show AdaDetectGPT nearly uniformly improves the state-of-the-art method in various combination of datasets and LLMs, and the improvement can reach up to 37%. A python implementation of our method is available athttps://github.com/Mamba413/AdaDetectGPT. 1 Introduction Large language models (LLMs) such as ChatGPT (OpenAI, 2022), PaLM (Chowdhery et al., 2023), Llama (Grattafiori et al., 2024) and DeepSeek (Bi et al., 2024) have revolut
```

### Retrieved Chunk 4

- Source: `AdaDetectGPT Adaptive Detection of LLM-Generated Text with Statistical Guarantees.pdf`
- Page: `7`
- Chunk ID: `247`
- Chunk Type: `main`
- Dense Score: `unknown`
- Vector Score: `0.443564236164093`
- BM25 Score: `unknown`
- Reranker Score: `2.6607179641723633`

```text
evaluate AdaDetectGPT, we compute the AUC on each of the five datasets, with its witness function bwtrained on two randomly selected datasets that differ from the test dataset. Benchmark methods.In white-box settings, we compare the proposed AdaDetectGPT againsteight state-of-the-art detectors: Likelihood, Entropy, LogRank(Gehrmann et al., 2019), LogRank Ratio (LRR, Su et al., 2023), DetectGPT(Mitchell et al., 2023) and its variants Normalized Perturbed log Rank (NPR, Su et al., 2023), Fast-DetectGPT(Bao et al., 2024), DNAGPT(Yang et al., 2024b). In black-box settings, we further compare against RoBERTaBaseand RoBERTaLarge(Solaiman et al., 2019), Binoculars(Hans et al., 2024), RADAR(Hu et al., 2023), and BiScope(Guo et al., 2024a), but omitDetectGPT,NPRandDNAGPTdue to their high computational cost. This yieldstenbaseline algorithms. We measure the detection power of each detector using A
```

### Retrieved Chunk 5

- Source: `DetectGPT-SC Improving Detection of Text Generated by Large Language Models through Self-Consistency with Masked Predictions.pdf`
- Page: `2`
- Chunk ID: `1519`
- Chunk Type: `main`
- Dense Score: `unknown`
- Vector Score: `0.5957632660865784`
- BM25 Score: `13.419429149053038`
- Reranker Score: `2.0015382766723633`

```text
of watermarks is also a challenge we need to address. However, with the emergence of ChatGPT, an innovative statistical detection method called DetectGPT [5] has been developed. Its principle is that text generated by the model typically resides in the negative curvature region of the model’s log probability. DetectGPT [ 5] generates and compares multiple variants of model-generated texts to determine whether the texts are machine-generated based on the log probabilities of the original texts and these variants. DetectGPT [5] outperforms the vast majority of existing zero-shot methods in terms of model sample detection, achieving very high AUC. It is based on this concept that DetectGPT-SC was proposed. 3 Methodology Predefined definition X is the original input text. ˆX is the sentence masked within X, which can also be referred to as "<mask>". P ( ˆX) is the mask content predicted by C
```

### Retrieved Chunk 6

- Source: `DetectGPT Zero-Shot Machine-Generated Text Detection using Probability Curvature.pdf`
- Page: `12`
- Chunk ID: `1508`
- Chunk Type: `main`
- Dense Score: `unknown`
- Vector Score: `0.5422935485839844`
- BM25 Score: `unknown`
- Reranker Score: `1.9752681255340576`

```text
Table 5. Top-k sampling evaluation with k = 40 . DetectGPT generally provides the most accurate performance (highest AUROC), although the gap is narrowed comparing to direct sampling, presumably because top-k generations are more generic. 13
```

### Retrieved Chunk 7

- Source: `DetectGPT Zero-Shot Machine-Generated Text Detection using Probability Curvature.pdf`
- Page: `5`
- Chunk ID: `1470`
- Chunk Type: `main`
- Dense Score: `unknown`
- Vector Score: `unknown`
- BM25 Score: `12.393047077123628`
- Reranker Score: `1.8043674230575562`

```text
like English news, but perform significantly worse than zero- shot methods in the case of English scientific writing and fail altogether for German writing. This finding echoes past work showing that language models trained for machine- generated text detection overfit to their training data (source model, decoding strategy, topic, language, etc.; Uchendu et al. (2020); Ippolito et al. (2020); Jawahar et al. (2020)). In contrast, zero-shot methods generalize relatively easily to new languages and domains; DetectGPT’s performance in particular is mostly unaffected by the change in language from English to German. While our experiments have shown that DetectGPT is ef- fective on a variety of domains and models, it is natural to wonder if it is effective for the largest publicly-available LMs. Therefore, we also evaluate multiple zero-shot and su- pervised methods on two 175B parameter mode
```

### Retrieved Chunk 8

- Source: `DetectGPT Zero-Shot Machine-Generated Text Detection using Probability Curvature.pdf`
- Page: `8`
- Chunk ID: `1486`
- Chunk Type: `main`
- Dense Score: `unknown`
- Vector Score: `0.581191897392273`
- BM25 Score: `unknown`
- Reranker Score: `1.5131006240844727`

```text
Limitations. One limitation of probability-based methods for zero-shot machine-generated text detection (like Detect- GPT) is the white-box assumption that we can evaluate log probabilities of the model(s) in question. For models be- hind APIs that do provide probabilities (such as GPT-3), evaluating probabilities nonetheless costs money. Another assumption of DetectGPT is access to a reasonable pertur- bation function. While in this work, we use off-the-shelf mask-filling models such as T5 and mT5 (for non-English languages), some domains may see reduced performance if existing mask-filling models do not well represent the space of meaningful rephrases, reducing the quality of the curvature estimate. While DetectGPT provides the best available detection performance for PubMedQA, its drop in performance compared to other datasets may be a result Average length 0.985 0.990 0.995AUROC gpt-
```


### Manual Judgment

Please inspect the retrieved chunks and fill in:

- Which setting retrieves the most useful chunks?
- Does BM25 help with method names, abbreviations, or technical terms?
- Does dense retrieval help with semantic but non-exact matches?
- Does hybrid + reranker combine the advantages of both?
- Does hybrid retrieval reduce or increase noise?
- Overall winner: Dense only / BM25 only / Hybrid + reranker / Tie

---

# Overall Notes

Use this report to decide whether hybrid retrieval improves your RAG system.

Typical patterns:

- If BM25 performs well on exact method names, keep it for keyword recall.
- If dense retrieval performs better on conceptual questions, keep dense retrieval for semantic recall.
- If hybrid + reranker consistently ranks better chunks near the top, it should be the default retrieval pipeline.
- If hybrid retrieval loses source diversity, adjust `max_per_source`.
- If all methods retrieve poor chunks, improve paper catalog, chunking, or chunk_type labeling.
