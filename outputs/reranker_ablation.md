# Reranker Ablation Study

This report compares two retrieval settings:

1. **Vector-only retrieval**: paper-level routing + chunk vector search.
2. **Reranker retrieval**: paper-level routing + chunk vector search + cross-encoder reranking.

The goal is to check whether the reranker improves chunk relevance.

---

## Broad overview of AI-generated text detection

### Question

What AI-generated text detection methods are discussed in these papers?

### Retrieval Mode

- Vector-only mode: `global`
- Reranker mode: `global`

### Candidate Papers

The candidate papers should be the same or very similar, because both settings use the same paper-level retrieval.

#### Vector-only Candidate Papers

1. `SeqXGPT Sentence-Level AI-Generated Text Detection.pdf`
   - Title: SeqXGPT Sentence Level AI Generated Text Detection
   - Paper score: `0.3216600716114044`

2. `Ghostbuster Detecting Text Ghostwritten by Large Language Models.pdf`
   - Title: Ghostbuster Detecting Text Ghostwritten by Large Language Models
   - Paper score: `0.34038466215133667`

3. `ASurvey of AI-generated Text Forensic Systems Detection Attribution and Characterization.pdf`
   - Title: ASurvey of AI generated Text Forensic Systems Detection Attribution and Characterization
   - Paper score: `0.34393998980522156`

4. `Unsupervised and Distributional Detection of Machine-Generated Text.pdf`
   - Title: Unsupervised and Distributional Detection of Machine Generated Text
   - Paper score: `0.3484887182712555`


#### Reranker Candidate Papers

1. `SeqXGPT Sentence-Level AI-Generated Text Detection.pdf`
   - Title: SeqXGPT Sentence Level AI Generated Text Detection
   - Paper score: `0.3216600716114044`

2. `Ghostbuster Detecting Text Ghostwritten by Large Language Models.pdf`
   - Title: Ghostbuster Detecting Text Ghostwritten by Large Language Models
   - Paper score: `0.34038466215133667`

3. `ASurvey of AI-generated Text Forensic Systems Detection Attribution and Characterization.pdf`
   - Title: ASurvey of AI generated Text Forensic Systems Detection Attribution and Characterization
   - Paper score: `0.34393998980522156`

4. `Unsupervised and Distributional Detection of Machine-Generated Text.pdf`
   - Title: Unsupervised and Distributional Detection of Machine Generated Text
   - Paper score: `0.3484887182712555`


### Selected Papers

#### Vector-only Selected Papers

1. `SeqXGPT Sentence-Level AI-Generated Text Detection.pdf`
   - Title: SeqXGPT Sentence Level AI Generated Text Detection
   - Paper score: `0.3216600716114044`

2. `Ghostbuster Detecting Text Ghostwritten by Large Language Models.pdf`
   - Title: Ghostbuster Detecting Text Ghostwritten by Large Language Models
   - Paper score: `0.34038466215133667`

3. `ASurvey of AI-generated Text Forensic Systems Detection Attribution and Characterization.pdf`
   - Title: ASurvey of AI generated Text Forensic Systems Detection Attribution and Characterization
   - Paper score: `0.34393998980522156`

4. `Unsupervised and Distributional Detection of Machine-Generated Text.pdf`
   - Title: Unsupervised and Distributional Detection of Machine Generated Text
   - Paper score: `0.3484887182712555`


#### Reranker Selected Papers

1. `SeqXGPT Sentence-Level AI-Generated Text Detection.pdf`
   - Title: SeqXGPT Sentence Level AI Generated Text Detection
   - Paper score: `0.3216600716114044`

2. `Ghostbuster Detecting Text Ghostwritten by Large Language Models.pdf`
   - Title: Ghostbuster Detecting Text Ghostwritten by Large Language Models
   - Paper score: `0.34038466215133667`

3. `ASurvey of AI-generated Text Forensic Systems Detection Attribution and Characterization.pdf`
   - Title: ASurvey of AI generated Text Forensic Systems Detection Attribution and Characterization
   - Paper score: `0.34393998980522156`

4. `Unsupervised and Distributional Detection of Machine-Generated Text.pdf`
   - Title: Unsupervised and Distributional Detection of Machine Generated Text
   - Paper score: `0.3484887182712555`


### Summary Statistics

| Metric | Vector-only | With reranker |
|---|---:|---:|
| Retrieved chunks | 8 | 8 |
| Unique sources | 3 | 3 |
| Noisy chunks | 0 | 0 |
| Overlap chunks | 5 | 5 |

### Source Distribution

#### Vector-only

- `ASurvey of AI-generated Text Forensic Systems Detection Attribution and Characterization.pdf`: 3 chunks
- `Ghostbuster Detecting Text Ghostwritten by Large Language Models.pdf`: 3 chunks
- `SeqXGPT Sentence-Level AI-Generated Text Detection.pdf`: 2 chunks

#### With reranker

- `ASurvey of AI-generated Text Forensic Systems Detection Attribution and Characterization.pdf`: 3 chunks
- `SeqXGPT Sentence-Level AI-Generated Text Detection.pdf`: 3 chunks
- `Ghostbuster Detecting Text Ghostwritten by Large Language Models.pdf`: 2 chunks

### Vector-only Retrieved Chunks

### Retrieved Chunk 1

- Source: `ASurvey of AI-generated Text Forensic Systems Detection Attribution and Characterization.pdf`
- Page: `13`
- Chunk ID: `491`
- Chunk Type: `main`
- Vector Score: `0.31118810176849365`
- Reranker Score: `unknown`

```text
Eric Mitchell, Yoonho Lee, Alexander Khaz- atsky, Christopher D. Manning, and Chelsea Finn. 2023. DetectGPT: Zero-Shot Machine- Generated Text Detection using Probability Cur- vature. ArXiv:2301.11305 [cs]. Edoardo Mosca, Mohamed Hesham Ibrahim Ab- dalla, Paolo Basso, Margherita Musumeci, and Georg Groh. 2023. Distinguishing fact from fiction: A benchmark dataset for identifying machine-generated scientific papers in the llm era. In Proceedings of the 3rd Workshop on Trustworthy Natural Language Processing (TrustNLP 2023), pages 190–207. Rithesh Murthy, Shelby Heinecke, Juan Carlos Niebles, Zhiwei Liu, Le Xue, Weiran Yao, Yi- hao Feng, Zeyuan Chen, Akash Gokul, Devansh Arpit, et al. 2023. Rex: Rapid exploration and exploitation for ai agents. arXiv preprint arXiv:2307.08962. Duke Nguyen, Khaing Myat Noe Naing, and Aditya Joshi. 2023. Stacking the odds: Transformer-based ensemble for ai-g
```

### Retrieved Chunk 2

- Source: `ASurvey of AI-generated Text Forensic Systems Detection Attribution and Characterization.pdf`
- Page: `2`
- Chunk ID: `430`
- Chunk Type: `main`
- Vector Score: `0.3126138746738434`
- Reranker Score: `unknown`

```text
LLMs. Consequently, post-hoc detection methods have gained prominence in AI-generated text foren- sics. Therefore, in the scope of our survey, we focus on post-hoc detection, further dividing it into supervised and zero-shot detection based on the training methodology employed. 2.2.2 Supervised Detectors Supervised detectors are trained using annotated datasets that consist of labeled human-written and AI-generated texts, aiming to identify distinctive features between human and AI-generated writ- ing. Initial efforts in AI-generated text detection em- ployed traditional techniques such as Bag-of-Words and TF-IDF encoding, coupled with classifiers like logistic regression, random forest, and SVC (Ip- polito et al., 2019; Jawahar et al., 2020). Subsequent research introduced advanced text sequence classi- fiers, including LSTM, GRU, and CNN, for detect- ing machine-generated text (Fagni e
```

### Retrieved Chunk 3

- Source: `ASurvey of AI-generated Text Forensic Systems Detection Attribution and Characterization.pdf`
- Page: `1`
- Chunk ID: `426`
- Chunk Type: `main`
- Vector Score: `0.3143196105957031`
- Reranker Score: `unknown`

```text
to organize the current work, identify gaps and future directions in this rapidly developing field. Our work facilitates the advancement of research in AI-generated text forensics, contributing to the development of more robust, transparent, and ac- countable digital information ecosystems. Related Surveys: Numerous surveys discuss as- pects of detection (Jawahar et al., 2020; Crothers et al., 2023; Tang et al., 2023) and attribu- tion (Uchendu et al., 2023) in isolated contexts. In contrast, the objective of our survey is to delineate the broad themes within the AI-generated foren- sics field by identifying its fundamental pillars, ex- ploring their interconnections, and discussing chal- lenges envisioning a future where AI-generated text becomes pervasive. 2 AI-generated Text Forensic Systems 2.1 AI-Generated Text In this survey, we define AI-generated text as out- put produced by a na
```

### Retrieved Chunk 4

- Source: `SeqXGPT Sentence-Level AI-Generated Text Detection.pdf`
- Page: `1`
- Chunk ID: `3398`
- Chunk Type: `main`
- Vector Score: `0.3295079171657562`
- Reranker Score: `unknown`

```text
existing methods, such as DetectGPT and Sniffer, fail to solve sentence-level AIGT detection. Our proposed SeqXGPT not only obtains promising results in both sentence and document-level AIGT detection challenges, but also exhibits excellent generalization on out-of-distribution datasets. 2 Background The proliferation of Large Language Models (LLMs) such as GPT-4 has given rise to increased concerns about the potential misuse of AI- generated texts (AIGT) (Brown et al., 2020; Zhang et al., 2022; Scao et al., 2022). This emphasizes the necessity for robust detection mechanisms to ensure security and trustworthiness of LLM applications. 2.1 Principal Approaches to AIGT Detection Broadly, AIGT detection methodologies fall into two primary categories: 1. Supervised Learning: This involves training models on labeled datasets to distinguish between human and AI-generated texts. Notable efforts
```

### Retrieved Chunk 5

- Source: `Ghostbuster Detecting Text Ghostwritten by Large Language Models.pdf`
- Page: `12`
- Chunk ID: `2442`
- Chunk Type: `main`
- Vector Score: `0.3323102295398712`
- Reranker Score: `unknown`

```text
a full document was AI-generated; and paragraph- level detection, detecting which paragraphs in a document were AI-generated. These tasks are motivated by real-world appli- cations of these detectors. For example, when questioning whether a student assignment was AI- generated, instructors often have access to previ- ous work by that student; document-level detec- tion may be useful when instructors do not have access to a history of student writing, or cannot verify that students did not include AI-generated text in previous assignments; and paragraph-level detection is useful when, as is often the case, AI assistance was only used for portions of the as- signment. Although the modeling work in the main body of our paper focuses only on document- level detection, we will release these additional benchmarks as a testbed for future work at https: //github.com/vivek3141/ghostbuster-data/ G
```

### Retrieved Chunk 6

- Source: `Ghostbuster Detecting Text Ghostwritten by Large Language Models.pdf`
- Page: `0`
- Chunk ID: `2380`
- Chunk Type: `main`
- Vector Score: `0.33417007327079773`
- Reranker Score: `unknown`

```text
datasets that they were not originally evaluated on (Section 6). In addition, the high false positive rates of these models raise potential ethical concerns be- cause they jeopardize students whose genuine work is misclassified as AI-generated. Furthermore, pre- vious work has indicated that text by non-native speakers of English is disproportionately flagged as AI-generated (Liang et al., 2023). These concerns underscore the need for AI-generated text detectors with strong generalization performance. We present Ghostbuster, a method for detection based on structured search and linear classification (Figure 1). First, Ghostbuster passes paired human- authored and AI-generated documents through a series of weaker language models, ranging from a unigram model to the non-instruction-tuned GPT-3 davinci. Given the word probabilities from these models, it then searches over a space of vector 
```

### Retrieved Chunk 7

- Source: `Ghostbuster Detecting Text Ghostwritten by Large Language Models.pdf`
- Page: `0`
- Chunk ID: `2377`
- Chunk Type: `main`
- Vector Score: `0.3349219262599945`
- Reranker Score: `unknown`

```text
Ghostbuster: Detecting Text Ghostwritten by Large Language Models Vivek Verma Eve Fleisig Nicholas Tomlin Dan Klein Computer Science Division, UC Berkeley {vivekverma, efleisig, nicholas_tomlin, klein}@berkeley.edu Abstract We introduce Ghostbuster, a state-of-the-art system for detecting AI-generated text. Our method works by passing documents through a series of weaker language models, running a structured search over possible combinations of their features, and then training a classifier on the selected features to predict whether docu- ments are AI-generated. Crucially, Ghostbuster does not require access to token probabilities from the target model, making it useful for de- tecting text generated by black-box or unknown models. In conjunction with our model, we release three new datasets of human- and AI- generated text as detection benchmarks in the domains of student essays, creat
```

### Retrieved Chunk 8

- Source: `SeqXGPT Sentence-Level AI-Generated Text Detection.pdf`
- Page: `0`
- Chunk ID: `3392`
- Chunk Type: `main`
- Vector Score: `0.33876076340675354`
- Reranker Score: `unknown`

```text
SeqXGPT: Sentence-Level AI-Generated Text Detection Pengyu Wang, Linyang Li , Ke Ren, Botian Jiang, Dong Zhang, Xipeng Qiu ∗ School of Computer Science, Fudan University Shanghai Key Laboratory of Intelligent Information Processing, Fudan University {pywang22,kren22,btjiang23,dongzhang22}@m.fudan.edu.cn {linyangli19,xpqiu}@fudan.edu.cn Abstract Widely applied large language models (LLMs) can generate human-like content, raising concerns about the abuse of LLMs. Therefore, it is important to build strong AI-generated text (AIGT) detectors. Current works only consider document-level AIGT detection, therefore, in this paper, we first introduce a sentence-level detection challenge by synthesizing a dataset that contains documents that are polished with LLMs, that is, the documents contain sentences written by humans and sentences modified by LLMs. Then we propose Sequence X (Check) GPT, a no
```


### Reranker Retrieved Chunks

### Retrieved Chunk 1

- Source: `ASurvey of AI-generated Text Forensic Systems Detection Attribution and Characterization.pdf`
- Page: `2`
- Chunk ID: `430`
- Chunk Type: `main`
- Vector Score: `unknown`
- Reranker Score: `5.634542465209961`

```text
LLMs. Consequently, post-hoc detection methods have gained prominence in AI-generated text foren- sics. Therefore, in the scope of our survey, we focus on post-hoc detection, further dividing it into supervised and zero-shot detection based on the training methodology employed. 2.2.2 Supervised Detectors Supervised detectors are trained using annotated datasets that consist of labeled human-written and AI-generated texts, aiming to identify distinctive features between human and AI-generated writ- ing. Initial efforts in AI-generated text detection em- ployed traditional techniques such as Bag-of-Words and TF-IDF encoding, coupled with classifiers like logistic regression, random forest, and SVC (Ip- polito et al., 2019; Jawahar et al., 2020). Subsequent research introduced advanced text sequence classi- fiers, including LSTM, GRU, and CNN, for detect- ing machine-generated text (Fagni e
```

### Retrieved Chunk 2

- Source: `SeqXGPT Sentence-Level AI-Generated Text Detection.pdf`
- Page: `0`
- Chunk ID: `3392`
- Chunk Type: `main`
- Vector Score: `unknown`
- Reranker Score: `5.61989688873291`

```text
SeqXGPT: Sentence-Level AI-Generated Text Detection Pengyu Wang, Linyang Li , Ke Ren, Botian Jiang, Dong Zhang, Xipeng Qiu ∗ School of Computer Science, Fudan University Shanghai Key Laboratory of Intelligent Information Processing, Fudan University {pywang22,kren22,btjiang23,dongzhang22}@m.fudan.edu.cn {linyangli19,xpqiu}@fudan.edu.cn Abstract Widely applied large language models (LLMs) can generate human-like content, raising concerns about the abuse of LLMs. Therefore, it is important to build strong AI-generated text (AIGT) detectors. Current works only consider document-level AIGT detection, therefore, in this paper, we first introduce a sentence-level detection challenge by synthesizing a dataset that contains documents that are polished with LLMs, that is, the documents contain sentences written by humans and sentences modified by LLMs. Then we propose Sequence X (Check) GPT, a no
```

### Retrieved Chunk 3

- Source: `ASurvey of AI-generated Text Forensic Systems Detection Attribution and Characterization.pdf`
- Page: `3`
- Chunk ID: `436`
- Chunk Type: `main`
- Vector Score: `unknown`
- Reranker Score: `5.505354881286621`

```text
tectors is their limited ability to generalize to novel AI generators. Various approaches have been ex- plored to mitigate this issue, focusing on develop- ing transferable techniques for AI-generated text detection. One such avenue involves integrating Energy-Based Models (EBMs) into the detection process (Bakhtin et al., 2019). This integration ex- ploits negative samples generated by multiple auto- regressive language models; specifically, the model assigns lower energy to human-generated text com- pared to text generated by AI models. Another strategy introduced by (Kushnareva et al., 2021a) utilizes Topological Data Analysis (TDA) on at- tention maps produced by transformer models to extract domain-invariant features for AI-generated text detection. This approach involves representing attention maps as weighted bipartite graphs, lever- aging TDA’s capability to capture both surface 
```

### Retrieved Chunk 4

- Source: `Ghostbuster Detecting Text Ghostwritten by Large Language Models.pdf`
- Page: `0`
- Chunk ID: `2380`
- Chunk Type: `main`
- Vector Score: `unknown`
- Reranker Score: `5.462650299072266`

```text
datasets that they were not originally evaluated on (Section 6). In addition, the high false positive rates of these models raise potential ethical concerns be- cause they jeopardize students whose genuine work is misclassified as AI-generated. Furthermore, pre- vious work has indicated that text by non-native speakers of English is disproportionately flagged as AI-generated (Liang et al., 2023). These concerns underscore the need for AI-generated text detectors with strong generalization performance. We present Ghostbuster, a method for detection based on structured search and linear classification (Figure 1). First, Ghostbuster passes paired human- authored and AI-generated documents through a series of weaker language models, ranging from a unigram model to the non-instruction-tuned GPT-3 davinci. Given the word probabilities from these models, it then searches over a space of vector 
```

### Retrieved Chunk 5

- Source: `SeqXGPT Sentence-Level AI-Generated Text Detection.pdf`
- Page: `1`
- Chunk ID: `3398`
- Chunk Type: `main`
- Vector Score: `unknown`
- Reranker Score: `5.27540397644043`

```text
existing methods, such as DetectGPT and Sniffer, fail to solve sentence-level AIGT detection. Our proposed SeqXGPT not only obtains promising results in both sentence and document-level AIGT detection challenges, but also exhibits excellent generalization on out-of-distribution datasets. 2 Background The proliferation of Large Language Models (LLMs) such as GPT-4 has given rise to increased concerns about the potential misuse of AI- generated texts (AIGT) (Brown et al., 2020; Zhang et al., 2022; Scao et al., 2022). This emphasizes the necessity for robust detection mechanisms to ensure security and trustworthiness of LLM applications. 2.1 Principal Approaches to AIGT Detection Broadly, AIGT detection methodologies fall into two primary categories: 1. Supervised Learning: This involves training models on labeled datasets to distinguish between human and AI-generated texts. Notable efforts
```

### Retrieved Chunk 6

- Source: `ASurvey of AI-generated Text Forensic Systems Detection Attribution and Characterization.pdf`
- Page: `0`
- Chunk ID: `419`
- Chunk Type: `main`
- Vector Score: `unknown`
- Reranker Score: `5.121118545532227`

```text
ing the challenges of LLM misuses. We present an overview of the existing efforts in AI-generated text forensics by introducing a detailed taxonomy, focusing on three pri- mary pillars: detection, attribution, and char- acterization. These pillars enable a practi- cal understanding of AI-generated text, from identifying AI-generated content (detection), determining the specific AI model involved (attribution), and grouping the underlying intents of the text (characterization). Further- more, we explore available resources for AI- generated text forensics research and discuss the evolving challenges and future directions of forensic systems in an AI era. 1 Introduction The advent of Large Language Models (LLMs) like GPT-4 (OpenAI, 2023), Gemini (Team et al., 2023), and open-source variants such as Falcon (Al- mazrouei et al., 2023) and Llama 1&2 (Touvron et al., 2023), has significantly e
```

### Retrieved Chunk 7

- Source: `SeqXGPT Sentence-Level AI-Generated Text Detection.pdf`
- Page: `0`
- Chunk ID: `3395`
- Chunk Type: `main`
- Vector Score: `unknown`
- Reranker Score: `5.0298662185668945`

```text
can efficiently conduct sentence-level AIGT detection. given text is written or modified by an AI system (Mitchell et al., 2023; Li et al., 2023). Current AIGT detection strategies, such as supervised-learned discriminator 2, perplexity- based methods (Mitchell et al., 2023; Li et al., 2023), etc., focus on discriminating whether a whole document is generated by an AI. However, users often modify partial texts with LLMs rather than put full trust in LLMs to generate a whole document. Therefore, it is important to explore fine-grained (e.g. sentence-level) AIGT detection. Building methods that solve the sentence-level AIGT detection challenge is not an incremental modification over document-level AIGT detection. On the one hand, model-wise methods like DetectGPT and Sniffer require a rather long document as input (over 100 tokens), making 2https://github.com/openai/ gpt-2-output-dataset a
```

### Retrieved Chunk 8

- Source: `Ghostbuster Detecting Text Ghostwritten by Large Language Models.pdf`
- Page: `0`
- Chunk ID: `2377`
- Chunk Type: `main`
- Vector Score: `unknown`
- Reranker Score: `4.997632026672363`

```text
Ghostbuster: Detecting Text Ghostwritten by Large Language Models Vivek Verma Eve Fleisig Nicholas Tomlin Dan Klein Computer Science Division, UC Berkeley {vivekverma, efleisig, nicholas_tomlin, klein}@berkeley.edu Abstract We introduce Ghostbuster, a state-of-the-art system for detecting AI-generated text. Our method works by passing documents through a series of weaker language models, running a structured search over possible combinations of their features, and then training a classifier on the selected features to predict whether docu- ments are AI-generated. Crucially, Ghostbuster does not require access to token probabilities from the target model, making it useful for de- tecting text generated by black-box or unknown models. In conjunction with our model, we release three new datasets of human- and AI- generated text as detection benchmarks in the domains of student essays, creat
```


### Manual Judgment

Please inspect the retrieved chunks and fill in:

- Which setting retrieves more useful chunks?
- Does the reranker move more relevant chunks to the top?
- Does the reranker reduce checklist / references / appendix noise?
- Does the reranker hurt source diversity for broad questions?
- Overall winner: Vector-only / Reranker / Tie

---

## Specific AdaDetectGPT query

### Question

How does AdaDetectGPT work?

### Retrieval Mode

- Vector-only mode: `global`
- Reranker mode: `global`

### Candidate Papers

The candidate papers should be the same or very similar, because both settings use the same paper-level retrieval.

#### Vector-only Candidate Papers

1. `AdaDetectGPT Adaptive Detection of LLM-Generated Text with Statistical Guarantees.pdf`
   - Title: AdaDetectGPT Adaptive Detection of LLM Generated Text with Statistical Guarantees
   - Paper score: `0.6125631332397461`

2. `DetectGPT-SC Improving Detection of Text Generated by Large Language Models through Self-Consistency with Masked Predictions.pdf`
   - Title: DetectGPT SC Improving Detection of Text Generated by Large Language Models through Self Consistency with Masked Predictions
   - Paper score: `0.7034844160079956`

3. `Fast-DetectGPT Efficient Zero-Shot Detection of Machine-Generated Text via Conditional Probability Curvature.pdf`
   - Title: Fast DetectGPT Efficient Zero Shot Detection of Machine Generated Text via Conditional Probability Curvature
   - Paper score: `0.710049569606781`

4. `GPT-who AnInformation Density-based Machine-Generated Text Detector.pdf`
   - Title: GPT who AnInformation Density based Machine Generated Text Detector
   - Paper score: `0.7131985425949097`


#### Reranker Candidate Papers

1. `AdaDetectGPT Adaptive Detection of LLM-Generated Text with Statistical Guarantees.pdf`
   - Title: AdaDetectGPT Adaptive Detection of LLM Generated Text with Statistical Guarantees
   - Paper score: `0.6125631332397461`

2. `DetectGPT-SC Improving Detection of Text Generated by Large Language Models through Self-Consistency with Masked Predictions.pdf`
   - Title: DetectGPT SC Improving Detection of Text Generated by Large Language Models through Self Consistency with Masked Predictions
   - Paper score: `0.7034844160079956`

3. `Fast-DetectGPT Efficient Zero-Shot Detection of Machine-Generated Text via Conditional Probability Curvature.pdf`
   - Title: Fast DetectGPT Efficient Zero Shot Detection of Machine Generated Text via Conditional Probability Curvature
   - Paper score: `0.710049569606781`

4. `GPT-who AnInformation Density-based Machine-Generated Text Detector.pdf`
   - Title: GPT who AnInformation Density based Machine Generated Text Detector
   - Paper score: `0.7131985425949097`


### Selected Papers

#### Vector-only Selected Papers

1. `AdaDetectGPT Adaptive Detection of LLM-Generated Text with Statistical Guarantees.pdf`
   - Title: AdaDetectGPT Adaptive Detection of LLM Generated Text with Statistical Guarantees
   - Paper score: `0.6125631332397461`

2. `DetectGPT-SC Improving Detection of Text Generated by Large Language Models through Self-Consistency with Masked Predictions.pdf`
   - Title: DetectGPT SC Improving Detection of Text Generated by Large Language Models through Self Consistency with Masked Predictions
   - Paper score: `0.7034844160079956`

3. `Fast-DetectGPT Efficient Zero-Shot Detection of Machine-Generated Text via Conditional Probability Curvature.pdf`
   - Title: Fast DetectGPT Efficient Zero Shot Detection of Machine Generated Text via Conditional Probability Curvature
   - Paper score: `0.710049569606781`

4. `GPT-who AnInformation Density-based Machine-Generated Text Detector.pdf`
   - Title: GPT who AnInformation Density based Machine Generated Text Detector
   - Paper score: `0.7131985425949097`


#### Reranker Selected Papers

1. `AdaDetectGPT Adaptive Detection of LLM-Generated Text with Statistical Guarantees.pdf`
   - Title: AdaDetectGPT Adaptive Detection of LLM Generated Text with Statistical Guarantees
   - Paper score: `0.6125631332397461`

2. `DetectGPT-SC Improving Detection of Text Generated by Large Language Models through Self-Consistency with Masked Predictions.pdf`
   - Title: DetectGPT SC Improving Detection of Text Generated by Large Language Models through Self Consistency with Masked Predictions
   - Paper score: `0.7034844160079956`

3. `Fast-DetectGPT Efficient Zero-Shot Detection of Machine-Generated Text via Conditional Probability Curvature.pdf`
   - Title: Fast DetectGPT Efficient Zero Shot Detection of Machine Generated Text via Conditional Probability Curvature
   - Paper score: `0.710049569606781`

4. `GPT-who AnInformation Density-based Machine-Generated Text Detector.pdf`
   - Title: GPT who AnInformation Density based Machine Generated Text Detector
   - Paper score: `0.7131985425949097`


### Summary Statistics

| Metric | Vector-only | With reranker |
|---|---:|---:|
| Retrieved chunks | 8 | 8 |
| Unique sources | 4 | 3 |
| Noisy chunks | 0 | 0 |
| Overlap chunks | 4 | 4 |

### Source Distribution

#### Vector-only

- `AdaDetectGPT Adaptive Detection of LLM-Generated Text with Statistical Guarantees.pdf`: 3 chunks
- `Fast-DetectGPT Efficient Zero-Shot Detection of Machine-Generated Text via Conditional Probability Curvature.pdf`: 3 chunks
- `GPT-who AnInformation Density-based Machine-Generated Text Detector.pdf`: 1 chunks
- `DetectGPT-SC Improving Detection of Text Generated by Large Language Models through Self-Consistency with Masked Predictions.pdf`: 1 chunks

#### With reranker

- `AdaDetectGPT Adaptive Detection of LLM-Generated Text with Statistical Guarantees.pdf`: 3 chunks
- `DetectGPT-SC Improving Detection of Text Generated by Large Language Models through Self-Consistency with Masked Predictions.pdf`: 3 chunks
- `Fast-DetectGPT Efficient Zero-Shot Detection of Machine-Generated Text via Conditional Probability Curvature.pdf`: 2 chunks

### Vector-only Retrieved Chunks

### Retrieved Chunk 1

- Source: `AdaDetectGPT Adaptive Detection of LLM-Generated Text with Statistical Guarantees.pdf`
- Page: `9`
- Chunk ID: `255`
- Chunk Type: `main`
- Vector Score: `0.4194706678390503`
- Reranker Score: `unknown`

```text
Fast-DetectGPT 0.9048 0.95880.98470.9800 0.9571 0.9019 0.93610.97680.9608 0.9439 AdaDetectGPT 0.90720.96110.98320.9841 0.95890.91760.94000.97280.9610 0.9478 Relative ( ) 2.4288 5.6095 — 20.4444 4.2454 16.0326 6.0543 — 0.3405 6.9929 Table 3: Detection of LLM-generated text under two adversarial attacks in black-box settings. Paraphrasing Decoherence DetectGPT Xsum Writing PubMed Avg. Xsum Writing PubMed Avg. Fast (GPT-J/GPT-2) 0.91780.91370.7944 0.8753 0.7884 0.9595 0.7870 0.8449 Ada (GPT-J/GPT-2)0.92250.91210.8029 0.8792 0.8765 0.9597 0.8284 0.8882 Fast (GPT-J/Neo-2.7) 0.96020.91850.7310 0.8699 0.8579 0.9701 0.7609 0.8630 Ada (GPT-J/Neo-2.7)0.96230.91810.7587 0.8797 0.9230 0.9704 0.8124 0.9019 Fast (GPT-J/GPT-J) 0.95370.94580.7041 0.8679 0.88360.98690.7550 0.8752 Ada (GPT-J/GPT-J)0.95870.94490.7308 0.8781 0.93360.98640.8008 0.9070 underperforms Binoculars or RADAR. Nonetheless, AdaDetect
```

### Retrieved Chunk 2

- Source: `AdaDetectGPT Adaptive Detection of LLM-Generated Text with Statistical Guarantees.pdf`
- Page: `9`
- Chunk ID: `256`
- Chunk Type: `main`
- Vector Score: `0.44804322719573975`
- Reranker Score: `unknown`

```text
underperforms Binoculars or RADAR. Nonetheless, AdaDetectGPT consistently improves upon Fast-DetectGPT across various datasets, with gains on Essay reaching up to 37.8%. Additionally, we evaluate AdaDetectGPT’s robustness to two adversarial attacks, paraphrasing and decoherence, in the black-box setting. As shown in Table 3, AdaDetectGPT demonstrates greater resilience than Fast-DetectGPT to adversarially perturbed texts. The improvement reaches up to 10% for paraphrasing and up to 85% for decoherence. Finally, we employ the same five LLMs from Table 1 to compare Fast-DetectGPT and AdaDetectGPT in black-box settings. Following Bao et al. (2024), we use GPT-J as the source LLM for detecting each of the remaining four target LLMs. Due to space constraints, the results are presented in Table S11 of Appendix F.5, where AdaDetectGPT uniformly outperforms Fast-DetectGPT in all cases, with impr
```

### Retrieved Chunk 3

- Source: `AdaDetectGPT Adaptive Detection of LLM-Generated Text with Statistical Guarantees.pdf`
- Page: `8`
- Chunk ID: `251`
- Chunk Type: `main`
- Vector Score: `0.452589750289917`
- Reranker Score: `unknown`

```text
AdaDetectGPT0.8534 0.8420 0.8532 0.8347 0.8061 0.8379 Relative ( ) 14.1250 18.2659 21.1936 20.3301 18.4492 18.5779 reports the AUC scores of various detectors across all combinations of datasets and five source models. It can be seen that AdaDetectGPT achieves the highest AUC across all combinations of datasets and source models, outperforming Fast-DetectGPT – the best baseline method – by 12.5%-37%. We also evaluate AdaDetectGPT on three more advanced open-source LLMs: Qwen2.5 (Bai et al., 2025), Mistral (Jiang et al., 2023), and LLaMA3 (Grattafiori et al., 2024). As shown in Table S7, AdaDetectGPT delivers consistent improvements over Fast-DetectGPT and maintains competitive performance across five datasets, achieving the best results in most cases. These findings highlight the advantage of using an adaptively learned witness function for classification. In Appendix F.3, we analyze the
```

### Retrieved Chunk 4

- Source: `Fast-DetectGPT Efficient Zero-Shot Detection of Machine-Generated Text via Conditional Probability Curvature.pdf`
- Page: `20`
- Chunk ID: `2293`
- Chunk Type: `main`
- Vector Score: `0.5600500106811523`
- Reranker Score: `unknown`

```text
DetectGPT .9875 .9793 .9961 .9762 .95 .9869 .9707 .9919 .9619 .9424 .9928 .9856 .9953 .979 .9622 Fast-DetectGPT .9994 .9965 .9988 .997 .9958 .9954 .9867 .9938 .9826 .9773 .9999 .9999 .9997 .9999 .9997 (Diff) .0119 .0172 .0028 .0208 .0458 .0085 .0160 .0018 .0207 .0349 .0071 .0143 .0044 .0209 .0376 DetectGPT(fixed) .9399 .9438 .9961 .9367 .9214 .9143 .9026 .9919 .8846 .8854 .9722 .9635 .9953 .9627 .9646 Fast-Detect(fixed) .9953 .9861 .9997 .9856 .9779 .9805 .9613 .9979 .9499 .9311 .9978 .999 .9999 .9991 .998 (Diff) .0554 .0423 .0036 .0489 .0565 .0662 .0587 .0060 .0654 .0457 .0256 .0355 .0046 .0364 .0333 SQuAD Likelihood .961 .944 .9214 .8838 .8122 .9393 .9072 .8926 .8351 .7317 .9906 .987 .9792 .9572 .9094 Entropy .5369 .4736 .539 .5277 .5593 .552 .5203 .5457 .5441 .5992 .5132 .4508 .4924 .4882 .5263 LogRank .9792 .9657 .9535 .9156 .8482 .9692 .9423 .9385 .8842 .7895 .9972 .9959 .994 .9798 
```

### Retrieved Chunk 5

- Source: `Fast-DetectGPT Efficient Zero-Shot Detection of Machine-Generated Text via Conditional Probability Curvature.pdf`
- Page: `21`
- Chunk ID: `2297`
- Chunk Type: `main`
- Vector Score: `0.5744954347610474`
- Reranker Score: `unknown`

```text
Published as a conference paper at ICLR 2024 used in Table 2, sampling with the three strategies with k = 40 , p = 0 .96, and T = 0 .8. Fast- DetectGPT in the white-box setting obtains the best accuracy on the three sampling strategies, out- performing DetectGPT by relative 95% on Top- p sampling, relative 81% on Top- k sampling, and relative 99% on sampling with a temperature, as shown in Table 9. In the black-box setting, Fast- DetectGPT outperforms DetectGPT by relatively 92%, 80%, and 98% on the three decoding strate- gies, respectively. These results demonstrate that Fast-DetectGPT works consistently in detecting texts produced by different decoding strategies. To elucidate the trajectory of detection accuracy concerning variations in sampling hyper- parameters, we conducted additional experiments with values set top = 0.90, k = 30, and T = 0.6. As indicated in the lower segment of 
```

### Retrieved Chunk 6

- Source: `Fast-DetectGPT Efficient Zero-Shot Detection of Machine-Generated Text via Conditional Probability Curvature.pdf`
- Page: `5`
- Chunk ID: `2227`
- Chunk Type: `main`
- Vector Score: `0.576409101486206`
- Reranker Score: `unknown`

```text
experiments, measuring the detection accuracy in AUROC (see Appendix A). Inference Speedup. We compare the inference time (excluding the time for initializing the model) of Fast-DetectGPT and DetectGPT on a Tesla A100 GPU using XSum generations from the five models in Table 2. Despite DetectGPT’s use of GPU batch processing, splitting 100 perturbations into 10 batches, it still requires substantial computational resources. It totals 79,113 seconds (ap- proximately 22 hours) over five runs. In contrast, Fast-DetectGPT completes the task in only 233 seconds (about 4 minutes), achieving a remarkable speedup factor of approximately 340x, highlight- ing its significant performance improvement. White-Box Zero-Shot Machine-Generated Text Detection. We evaluate zero-shot methods us- ing each source model for scoring and typically Fast-DetectGPT using the source model also for sampling. The avera
```

### Retrieved Chunk 7

- Source: `GPT-who AnInformation Density-based Machine-Generated Text Detector.pdf`
- Page: `5`
- Chunk ID: `2508`
- Chunk Type: `main`
- Vector Score: `0.6207282543182373`
- Reranker Score: `unknown`

```text
ZeroGPT (ZeroGPT, 2023), OpenAI’s detector (So- laiman et al., 2019), Li et al. (2023)’s LongFormer- based detector 7 tuned for the InTheWild bench- mark (we refer to this method as “ITW”), a sty- lometric detector8 (Abbasi and Chen, 2008) and fine-tuned BERT9 (Kenton and Toutanova, 2019). We are unable to report results for exhaustively all methods across all datasets due to inherent inap- plicability in certain task settings. For example, most SOTA text detectors cannot be applied to the ArguGPT dataset as it only contains text written by multiple machines, while most text detectors are designed to differentiate between human-written and machine-generated texts. Beyond such limita- 4https://github.com/eric-mitchell/detect-gpt 5https://github.com/HendrikStrobelt/ detecting-fake-text 6https://github.com/BurhanUlTayyab/GPTZero 7https://github.com/yafuly/DeepfakeTextDetect 8https://github.
```

### Retrieved Chunk 8

- Source: `DetectGPT-SC Improving Detection of Text Generated by Large Language Models through Self-Consistency with Masked Predictions.pdf`
- Page: `2`
- Chunk ID: `1519`
- Chunk Type: `main`
- Vector Score: `0.6309280395507812`
- Reranker Score: `unknown`

```text
of watermarks is also a challenge we need to address. However, with the emergence of ChatGPT, an innovative statistical detection method called DetectGPT [5] has been developed. Its principle is that text generated by the model typically resides in the negative curvature region of the model’s log probability. DetectGPT [ 5] generates and compares multiple variants of model-generated texts to determine whether the texts are machine-generated based on the log probabilities of the original texts and these variants. DetectGPT [5] outperforms the vast majority of existing zero-shot methods in terms of model sample detection, achieving very high AUC. It is based on this concept that DetectGPT-SC was proposed. 3 Methodology Predefined definition X is the original input text. ˆX is the sentence masked within X, which can also be referred to as "<mask>". P ( ˆX) is the mask content predicted by C
```


### Reranker Retrieved Chunks

### Retrieved Chunk 1

- Source: `AdaDetectGPT Adaptive Detection of LLM-Generated Text with Statistical Guarantees.pdf`
- Page: `1`
- Chunk ID: `213`
- Chunk Type: `main`
- Vector Score: `unknown`
- Reranker Score: `6.063632011413574`

```text
Figure 1: Workflow of AdaDetectGPT. Built upon Fast-DetectGPT (Bao et al., 2024), our method adaptively learn a witness functionbwfrom training data by maximizing a lower bound on the TNR, while using normal approximation for FNR control. probability outputs (i.e., logits) from a source LLM to construct the statistics for classification (see e.g., Gehrmann et al., 2019; Mitchell et al., 2023). These works are motivated by the empirical observation that LLM-generated text tends to exhibit higher log-probabilities or larger differences between the logits of original and perturbed tokens. However, as we demonstrated in Section 3, relying solely on the logits can be sub-optimal for detecting LLM-generated text. Our contribution. In this paper, we propose AdaDetectGPT (see Figure 1 for a visualization), an adaptive LLM detector that leverages external training data to enhance the effectivenes
```

### Retrieved Chunk 2

- Source: `AdaDetectGPT Adaptive Detection of LLM-Generated Text with Statistical Guarantees.pdf`
- Page: `41`
- Chunk ID: `368`
- Chunk Type: `main`
- Vector Score: `unknown`
- Reranker Score: `5.962424278259277`

```text
G Broader impact and limitation AdaDetectGPT is a computationally and statistically efficient detector for machine-generated text, thus safeguarding AI systems against fake news, disinformation, and academic plagiarism. Despite AdaDetectGPT’s strong empirical performance in the black-box setting, its theoretical guarantees are mainly established in the white-box setting. Even when restricting to the white-box setting, LLM text generation often involves sampling parameters (e.g., temperature and top_k). Using different parameter values can cause the sampling distribution to deviate from that of the target model we aim to detect. This mismatch invalidates MCLT in practice. Fortunately, we observe that the shape of our statistic remains similar, but shifts toward a positive mean (see Figure S8), implying that FNR control under MCLT remains valid, although being more conservative. 4  2  0 2 
```

### Retrieved Chunk 3

- Source: `AdaDetectGPT Adaptive Detection of LLM-Generated Text with Statistical Guarantees.pdf`
- Page: `9`
- Chunk ID: `256`
- Chunk Type: `main`
- Vector Score: `unknown`
- Reranker Score: `5.0491943359375`

```text
underperforms Binoculars or RADAR. Nonetheless, AdaDetectGPT consistently improves upon Fast-DetectGPT across various datasets, with gains on Essay reaching up to 37.8%. Additionally, we evaluate AdaDetectGPT’s robustness to two adversarial attacks, paraphrasing and decoherence, in the black-box setting. As shown in Table 3, AdaDetectGPT demonstrates greater resilience than Fast-DetectGPT to adversarially perturbed texts. The improvement reaches up to 10% for paraphrasing and up to 85% for decoherence. Finally, we employ the same five LLMs from Table 1 to compare Fast-DetectGPT and AdaDetectGPT in black-box settings. Following Bao et al. (2024), we use GPT-J as the source LLM for detecting each of the remaining four target LLMs. Due to space constraints, the results are presented in Table S11 of Appendix F.5, where AdaDetectGPT uniformly outperforms Fast-DetectGPT in all cases, with impr
```

### Retrieved Chunk 4

- Source: `Fast-DetectGPT Efficient Zero-Shot Detection of Machine-Generated Text via Conditional Probability Curvature.pdf`
- Page: `21`
- Chunk ID: `2297`
- Chunk Type: `main`
- Vector Score: `unknown`
- Reranker Score: `-1.8355700969696045`

```text
Published as a conference paper at ICLR 2024 used in Table 2, sampling with the three strategies with k = 40 , p = 0 .96, and T = 0 .8. Fast- DetectGPT in the white-box setting obtains the best accuracy on the three sampling strategies, out- performing DetectGPT by relative 95% on Top- p sampling, relative 81% on Top- k sampling, and relative 99% on sampling with a temperature, as shown in Table 9. In the black-box setting, Fast- DetectGPT outperforms DetectGPT by relatively 92%, 80%, and 98% on the three decoding strate- gies, respectively. These results demonstrate that Fast-DetectGPT works consistently in detecting texts produced by different decoding strategies. To elucidate the trajectory of detection accuracy concerning variations in sampling hyper- parameters, we conducted additional experiments with values set top = 0.90, k = 30, and T = 0.6. As indicated in the lower segment of 
```

### Retrieved Chunk 5

- Source: `DetectGPT-SC Improving Detection of Text Generated by Large Language Models through Self-Consistency with Masked Predictions.pdf`
- Page: `2`
- Chunk ID: `1519`
- Chunk Type: `main`
- Vector Score: `unknown`
- Reranker Score: `-1.9079310894012451`

```text
of watermarks is also a challenge we need to address. However, with the emergence of ChatGPT, an innovative statistical detection method called DetectGPT [5] has been developed. Its principle is that text generated by the model typically resides in the negative curvature region of the model’s log probability. DetectGPT [ 5] generates and compares multiple variants of model-generated texts to determine whether the texts are machine-generated based on the log probabilities of the original texts and these variants. DetectGPT [5] outperforms the vast majority of existing zero-shot methods in terms of model sample detection, achieving very high AUC. It is based on this concept that DetectGPT-SC was proposed. 3 Methodology Predefined definition X is the original input text. ˆX is the sentence masked within X, which can also be referred to as "<mask>". P ( ˆX) is the mask content predicted by C
```

### Retrieved Chunk 6

- Source: `DetectGPT-SC Improving Detection of Text Generated by Large Language Models through Self-Consistency with Masked Predictions.pdf`
- Page: `0`
- Chunk ID: `1510`
- Chunk Type: `main`
- Vector Score: `unknown`
- Reranker Score: `-2.5270957946777344`

```text
self-consistency in text generation and continuation. Self-consistency capitalizes on the intuition that AI-generated texts can still be reasoned with by large language models using the same logical reasoning when portions of the texts are masked, which differs from human-generated texts. Using this observation, we subsequently proposed a new method for AI-generated texts detection based on self-consistency with masked predictions to determine whether a text is generated by LLMs. This method, which we call DetectGPT-SC. We conducted a series of experiments to evaluate the performance of DetectGPT-SC. In these experiments, we employed various mask scheme, zero-shot, and simple prompt for completing masked texts and self-consistency predictions. The results indicate that DetectGPT-SC outperforms the current state-of-the-art across different tasks. 1 Introduction Large language models (LLMs
```

### Retrieved Chunk 7

- Source: `DetectGPT-SC Improving Detection of Text Generated by Large Language Models through Self-Consistency with Masked Predictions.pdf`
- Page: `2`
- Chunk ID: `1520`
- Chunk Type: `main`
- Vector Score: `unknown`
- Reranker Score: `-2.72000789642334`

```text
"<mask>". P ( ˆX) is the mask content predicted by ChatGPT. DetectGPT-SC is based on the hypothesis that AI-generated texts can still undergo reasoning by large language models using the same logical reasoning process even when certain portions of the texts are masked, which distinguishes it from texts generated by humans. DetectGPT-SC is shown in Figure 1, by masking the input text X multiple times, we obtain ˆX1, ˆX2, and ˆX3, which represent the masked content in X. Simultaneously, we replace the corresponding positions in the input text X with the "<mask>" token. Then, we utilize ChatGPT to generate completions for the masked ˆX1, ˆX2, and ˆX3, resulting in new inferred results: P ( ˆX1), P ( ˆX2), and P ( ˆX3). Next, we employ cosine similarity and Word2Vec to compute the similarity betweenP ( ˆXi), i = 1, 2, 3 and ˆXi, i = 1, 2, 3. Word2Vec is a word embedding model that represents
```

### Retrieved Chunk 8

- Source: `Fast-DetectGPT Efficient Zero-Shot Detection of Machine-Generated Text via Conditional Probability Curvature.pdf`
- Page: `5`
- Chunk ID: `2227`
- Chunk Type: `main`
- Vector Score: `unknown`
- Reranker Score: `-3.4360907077789307`

```text
experiments, measuring the detection accuracy in AUROC (see Appendix A). Inference Speedup. We compare the inference time (excluding the time for initializing the model) of Fast-DetectGPT and DetectGPT on a Tesla A100 GPU using XSum generations from the five models in Table 2. Despite DetectGPT’s use of GPU batch processing, splitting 100 perturbations into 10 batches, it still requires substantial computational resources. It totals 79,113 seconds (ap- proximately 22 hours) over five runs. In contrast, Fast-DetectGPT completes the task in only 233 seconds (about 4 minutes), achieving a remarkable speedup factor of approximately 340x, highlight- ing its significant performance improvement. White-Box Zero-Shot Machine-Generated Text Detection. We evaluate zero-shot methods us- ing each source model for scoring and typically Fast-DetectGPT using the source model also for sampling. The avera
```


### Manual Judgment

Please inspect the retrieved chunks and fill in:

- Which setting retrieves more useful chunks?
- Does the reranker move more relevant chunks to the top?
- Does the reranker reduce checklist / references / appendix noise?
- Does the reranker hurt source diversity for broad questions?
- Overall winner: Vector-only / Reranker / Tie

---

## Specific DetectGPT query

### Question

How does DetectGPT detect machine-generated text?

### Retrieval Mode

- Vector-only mode: `global`
- Reranker mode: `global`

### Candidate Papers

The candidate papers should be the same or very similar, because both settings use the same paper-level retrieval.

#### Vector-only Candidate Papers

1. `DetectGPT-SC Improving Detection of Text Generated by Large Language Models through Self-Consistency with Masked Predictions.pdf`
   - Title: DetectGPT SC Improving Detection of Text Generated by Large Language Models through Self Consistency with Masked Predictions
   - Paper score: `0.4306338429450989`

2. `Fast-DetectGPT Efficient Zero-Shot Detection of Machine-Generated Text via Conditional Probability Curvature.pdf`
   - Title: Fast DetectGPT Efficient Zero Shot Detection of Machine Generated Text via Conditional Probability Curvature
   - Paper score: `0.467221736907959`

3. `DetectLLM Leveraging Log Rank Information for Zero-Shot Detection of Machine-Generated Text.pdf`
   - Title: DetectLLM Leveraging Log Rank Information for Zero Shot Detection of Machine Generated Text
   - Paper score: `0.49767881631851196`

4. `DetectLLM Leveraging Log-Rank Information for Zero-Shot Detection of Machine-Generated Text.pdf`
   - Title: DetectLLM Leveraging Log Rank Information for Zero Shot Detection of Machine Generated Text
   - Paper score: `0.4983159601688385`


#### Reranker Candidate Papers

1. `DetectGPT-SC Improving Detection of Text Generated by Large Language Models through Self-Consistency with Masked Predictions.pdf`
   - Title: DetectGPT SC Improving Detection of Text Generated by Large Language Models through Self Consistency with Masked Predictions
   - Paper score: `0.4306338429450989`

2. `Fast-DetectGPT Efficient Zero-Shot Detection of Machine-Generated Text via Conditional Probability Curvature.pdf`
   - Title: Fast DetectGPT Efficient Zero Shot Detection of Machine Generated Text via Conditional Probability Curvature
   - Paper score: `0.467221736907959`

3. `DetectLLM Leveraging Log Rank Information for Zero-Shot Detection of Machine-Generated Text.pdf`
   - Title: DetectLLM Leveraging Log Rank Information for Zero Shot Detection of Machine Generated Text
   - Paper score: `0.49767881631851196`

4. `DetectLLM Leveraging Log-Rank Information for Zero-Shot Detection of Machine-Generated Text.pdf`
   - Title: DetectLLM Leveraging Log Rank Information for Zero Shot Detection of Machine Generated Text
   - Paper score: `0.4983159601688385`


### Selected Papers

#### Vector-only Selected Papers

1. `DetectGPT-SC Improving Detection of Text Generated by Large Language Models through Self-Consistency with Masked Predictions.pdf`
   - Title: DetectGPT SC Improving Detection of Text Generated by Large Language Models through Self Consistency with Masked Predictions
   - Paper score: `0.4306338429450989`

2. `Fast-DetectGPT Efficient Zero-Shot Detection of Machine-Generated Text via Conditional Probability Curvature.pdf`
   - Title: Fast DetectGPT Efficient Zero Shot Detection of Machine Generated Text via Conditional Probability Curvature
   - Paper score: `0.467221736907959`

3. `DetectLLM Leveraging Log Rank Information for Zero-Shot Detection of Machine-Generated Text.pdf`
   - Title: DetectLLM Leveraging Log Rank Information for Zero Shot Detection of Machine Generated Text
   - Paper score: `0.49767881631851196`

4. `DetectLLM Leveraging Log-Rank Information for Zero-Shot Detection of Machine-Generated Text.pdf`
   - Title: DetectLLM Leveraging Log Rank Information for Zero Shot Detection of Machine Generated Text
   - Paper score: `0.4983159601688385`


#### Reranker Selected Papers

1. `DetectGPT-SC Improving Detection of Text Generated by Large Language Models through Self-Consistency with Masked Predictions.pdf`
   - Title: DetectGPT SC Improving Detection of Text Generated by Large Language Models through Self Consistency with Masked Predictions
   - Paper score: `0.4306338429450989`

2. `Fast-DetectGPT Efficient Zero-Shot Detection of Machine-Generated Text via Conditional Probability Curvature.pdf`
   - Title: Fast DetectGPT Efficient Zero Shot Detection of Machine Generated Text via Conditional Probability Curvature
   - Paper score: `0.467221736907959`

3. `DetectLLM Leveraging Log Rank Information for Zero-Shot Detection of Machine-Generated Text.pdf`
   - Title: DetectLLM Leveraging Log Rank Information for Zero Shot Detection of Machine Generated Text
   - Paper score: `0.49767881631851196`

4. `DetectLLM Leveraging Log-Rank Information for Zero-Shot Detection of Machine-Generated Text.pdf`
   - Title: DetectLLM Leveraging Log Rank Information for Zero Shot Detection of Machine Generated Text
   - Paper score: `0.4983159601688385`


### Summary Statistics

| Metric | Vector-only | With reranker |
|---|---:|---:|
| Retrieved chunks | 8 | 8 |
| Unique sources | 4 | 4 |
| Noisy chunks | 0 | 0 |
| Overlap chunks | 4 | 4 |

### Source Distribution

#### Vector-only

- `DetectGPT-SC Improving Detection of Text Generated by Large Language Models through Self-Consistency with Masked Predictions.pdf`: 3 chunks
- `Fast-DetectGPT Efficient Zero-Shot Detection of Machine-Generated Text via Conditional Probability Curvature.pdf`: 3 chunks
- `DetectLLM Leveraging Log Rank Information for Zero-Shot Detection of Machine-Generated Text.pdf`: 1 chunks
- `DetectLLM Leveraging Log-Rank Information for Zero-Shot Detection of Machine-Generated Text.pdf`: 1 chunks

#### With reranker

- `DetectLLM Leveraging Log Rank Information for Zero-Shot Detection of Machine-Generated Text.pdf`: 2 chunks
- `DetectLLM Leveraging Log-Rank Information for Zero-Shot Detection of Machine-Generated Text.pdf`: 2 chunks
- `Fast-DetectGPT Efficient Zero-Shot Detection of Machine-Generated Text via Conditional Probability Curvature.pdf`: 2 chunks
- `DetectGPT-SC Improving Detection of Text Generated by Large Language Models through Self-Consistency with Masked Predictions.pdf`: 2 chunks

### Vector-only Retrieved Chunks

### Retrieved Chunk 1

- Source: `DetectGPT-SC Improving Detection of Text Generated by Large Language Models through Self-Consistency with Masked Predictions.pdf`
- Page: `2`
- Chunk ID: `1519`
- Chunk Type: `main`
- Vector Score: `0.432113915681839`
- Reranker Score: `unknown`

```text
of watermarks is also a challenge we need to address. However, with the emergence of ChatGPT, an innovative statistical detection method called DetectGPT [5] has been developed. Its principle is that text generated by the model typically resides in the negative curvature region of the model’s log probability. DetectGPT [ 5] generates and compares multiple variants of model-generated texts to determine whether the texts are machine-generated based on the log probabilities of the original texts and these variants. DetectGPT [5] outperforms the vast majority of existing zero-shot methods in terms of model sample detection, achieving very high AUC. It is based on this concept that DetectGPT-SC was proposed. 3 Methodology Predefined definition X is the original input text. ˆX is the sentence masked within X, which can also be referred to as "<mask>". P ( ˆX) is the mask content predicted by C
```

### Retrieved Chunk 2

- Source: `DetectLLM Leveraging Log Rank Information for Zero-Shot Detection of Machine-Generated Text.pdf`
- Page: `2`
- Chunk ID: `1771`
- Chunk Type: `main`
- Vector Score: `0.43436291813850403`
- Reranker Score: `unknown`

```text
1020 50 100 #(Perturbations) 88 90 92performance(%) XSum 1020 50 100 #(Perturbations) 82 84 86 SQuAD 1020 50 100 #(Perturbations) 92 94 96 WritingP DetectGPT NPR(ours) Figure 2: Comparison of DetectGPT to NPR averaged across six models (in terms of AUROC). (The full results are given in Figure 6 in the Appendix). methods for detecting machine-generated text by evaluating the per-token log probability of texts and using thresholding. Mitchell et al. (2023) observed that machine-generated texts tend to lie in the local curvature of the log probability and proposed De- tectGPT, whose prominent performance can only be guaranteed by the large size of the perturbation function and by a large number of perturbations, and thus costs more computational resources. Other work explored watermarking, which im- prints specific patterns of the LLM-output text that can be detected by an algorithm while 
```

### Retrieved Chunk 3

- Source: `DetectLLM Leveraging Log-Rank Information for Zero-Shot Detection of Machine-Generated Text.pdf`
- Page: `2`
- Chunk ID: `1853`
- Chunk Type: `main`
- Vector Score: `0.43436291813850403`
- Reranker Score: `unknown`

```text
1020 50 100 #(Perturbations) 88 90 92performance(%) XSum 1020 50 100 #(Perturbations) 82 84 86 SQuAD 1020 50 100 #(Perturbations) 92 94 96 WritingP DetectGPT NPR(ours) Figure 2: Comparison of DetectGPT to NPR averaged across six models (in terms of AUROC). (The full results are given in Figure 6 in the Appendix). methods for detecting machine-generated text by evaluating the per-token log probability of texts and using thresholding. Mitchell et al. (2023) observed that machine-generated texts tend to lie in the local curvature of the log probability and proposed De- tectGPT, whose prominent performance can only be guaranteed by the large size of the perturbation function and by a large number of perturbations, and thus costs more computational resources. Other work explored watermarking, which im- prints specific patterns of the LLM-output text that can be detected by an algorithm while 
```

### Retrieved Chunk 4

- Source: `Fast-DetectGPT Efficient Zero-Shot Detection of Machine-Generated Text via Conditional Probability Curvature.pdf`
- Page: `4`
- Chunk ID: `2219`
- Chunk Type: `main`
- Vector Score: `0.4363716244697571`
- Reranker Score: `unknown`

```text
Published as a conference paper at ICLR 2024 Algorithm 1 Fast-DetectGPT machine-generated text detection. Input: passage x, sampling model qφ, scoring model pθ, and decision threshold ϵ Output: True – probably machine-generated, False – probably human-written. 1: function FAST DETECT GPT( x, qφ, pθ) 2: ˜xi ∼ qφ(˜x|x), i ∈ [1..N ] ▷ Conditional sampling 3: ˜µ ← 1 N P i log pθ(˜xi|x) ▷ Estimate the mean 4: ˜σ2 ← 1 N −1 P i(log pθ(˜xi|x) − ˜µ)2 ▷ Estimate the variance 5: ˆdx ← (log pθ(x) − ˜µ)/˜σ ▷ Estimate conditional probability curvature 6: return ˆdx > ϵ torch.distributions.categorical.Categorical(logits=lprobs).sample([10000]), where the lprobs is the log probability distribution of qφ(˜xj|x<j) for j from 0 to the length of x. The sampling process plays a pivotal role in guiding us toward the solution. To discern whether a token within a given context is machine-generated or human-auth
```

### Retrieved Chunk 5

- Source: `DetectGPT-SC Improving Detection of Text Generated by Large Language Models through Self-Consistency with Masked Predictions.pdf`
- Page: `5`
- Chunk ID: `1534`
- Chunk Type: `main`
- Vector Score: `0.4456269443035126`
- Reranker Score: `unknown`

```text
while a lower temperature (such as 0.1) makes the generated texts more deterministic or focused. In scoring systems, the primary evaluation is focused on the quality and coherence of the generated texts. These metrics emphasize the overall quality of the generated output rather than the specific level of randomness or diversity. 5 Conclusion In this paper, we have successfully introduced and validated DetectGPT-SC, which distinguishes itself significantly from existing literature. Our work proposes an innovative text detection method based on the self-consistency and 6
```

### Retrieved Chunk 6

- Source: `Fast-DetectGPT Efficient Zero-Shot Detection of Machine-Generated Text via Conditional Probability Curvature.pdf`
- Page: `5`
- Chunk ID: `2227`
- Chunk Type: `main`
- Vector Score: `0.45820948481559753`
- Reranker Score: `unknown`

```text
experiments, measuring the detection accuracy in AUROC (see Appendix A). Inference Speedup. We compare the inference time (excluding the time for initializing the model) of Fast-DetectGPT and DetectGPT on a Tesla A100 GPU using XSum generations from the five models in Table 2. Despite DetectGPT’s use of GPU batch processing, splitting 100 perturbations into 10 batches, it still requires substantial computational resources. It totals 79,113 seconds (ap- proximately 22 hours) over five runs. In contrast, Fast-DetectGPT completes the task in only 233 seconds (about 4 minutes), achieving a remarkable speedup factor of approximately 340x, highlight- ing its significant performance improvement. White-Box Zero-Shot Machine-Generated Text Detection. We evaluate zero-shot methods us- ing each source model for scoring and typically Fast-DetectGPT using the source model also for sampling. The avera
```

### Retrieved Chunk 7

- Source: `Fast-DetectGPT Efficient Zero-Shot Detection of Machine-Generated Text via Conditional Probability Curvature.pdf`
- Page: `20`
- Chunk ID: `2293`
- Chunk Type: `main`
- Vector Score: `0.46127474308013916`
- Reranker Score: `unknown`

```text
DetectGPT .9875 .9793 .9961 .9762 .95 .9869 .9707 .9919 .9619 .9424 .9928 .9856 .9953 .979 .9622 Fast-DetectGPT .9994 .9965 .9988 .997 .9958 .9954 .9867 .9938 .9826 .9773 .9999 .9999 .9997 .9999 .9997 (Diff) .0119 .0172 .0028 .0208 .0458 .0085 .0160 .0018 .0207 .0349 .0071 .0143 .0044 .0209 .0376 DetectGPT(fixed) .9399 .9438 .9961 .9367 .9214 .9143 .9026 .9919 .8846 .8854 .9722 .9635 .9953 .9627 .9646 Fast-Detect(fixed) .9953 .9861 .9997 .9856 .9779 .9805 .9613 .9979 .9499 .9311 .9978 .999 .9999 .9991 .998 (Diff) .0554 .0423 .0036 .0489 .0565 .0662 .0587 .0060 .0654 .0457 .0256 .0355 .0046 .0364 .0333 SQuAD Likelihood .961 .944 .9214 .8838 .8122 .9393 .9072 .8926 .8351 .7317 .9906 .987 .9792 .9572 .9094 Entropy .5369 .4736 .539 .5277 .5593 .552 .5203 .5457 .5441 .5992 .5132 .4508 .4924 .4882 .5263 LogRank .9792 .9657 .9535 .9156 .8482 .9692 .9423 .9385 .8842 .7895 .9972 .9959 .994 .9798 
```

### Retrieved Chunk 8

- Source: `DetectGPT-SC Improving Detection of Text Generated by Large Language Models through Self-Consistency with Masked Predictions.pdf`
- Page: `0`
- Chunk ID: `1509`
- Chunk Type: `main`
- Vector Score: `0.4709795117378235`
- Reranker Score: `unknown`

```text
DETECT GPT-SC: I MPROVING DETECTION OF TEXT GENERATED BY LARGE LANGUAGE MODELS THROUGH SELF -C ONSISTENCY WITH MASKED PREDICTIONS Rongsheng Wang Macao Polytechnic University p2213046@mpu.edu.mo Qi Li Iowa State University qli@iastate.edu Sihong Xie∗ HKUST (GZ) sihongxie@hkust-gz.edu.cn ABSTRACT General large language models (LLMs) such as ChatGPT have shown remarkable success, but it has also raised concerns among people about the misuse of AI-generated texts. Therefore, an important question is how to detect whether the texts are generated by ChatGPT or by humans. Existing detectors are built on the assumption that there is a distribution gap between human-generated and AI-generated texts. These gaps are typically identified using statistical information or classifiers. In contrast to prior research methods, we find that large language models such as ChatGPT exhibit strong self-consiste
```


### Reranker Retrieved Chunks

### Retrieved Chunk 1

- Source: `DetectLLM Leveraging Log Rank Information for Zero-Shot Detection of Machine-Generated Text.pdf`
- Page: `2`
- Chunk ID: `1771`
- Chunk Type: `main`
- Vector Score: `unknown`
- Reranker Score: `7.708574295043945`

```text
1020 50 100 #(Perturbations) 88 90 92performance(%) XSum 1020 50 100 #(Perturbations) 82 84 86 SQuAD 1020 50 100 #(Perturbations) 92 94 96 WritingP DetectGPT NPR(ours) Figure 2: Comparison of DetectGPT to NPR averaged across six models (in terms of AUROC). (The full results are given in Figure 6 in the Appendix). methods for detecting machine-generated text by evaluating the per-token log probability of texts and using thresholding. Mitchell et al. (2023) observed that machine-generated texts tend to lie in the local curvature of the log probability and proposed De- tectGPT, whose prominent performance can only be guaranteed by the large size of the perturbation function and by a large number of perturbations, and thus costs more computational resources. Other work explored watermarking, which im- prints specific patterns of the LLM-output text that can be detected by an algorithm while 
```

### Retrieved Chunk 2

- Source: `DetectLLM Leveraging Log-Rank Information for Zero-Shot Detection of Machine-Generated Text.pdf`
- Page: `2`
- Chunk ID: `1853`
- Chunk Type: `main`
- Vector Score: `unknown`
- Reranker Score: `7.708574295043945`

```text
1020 50 100 #(Perturbations) 88 90 92performance(%) XSum 1020 50 100 #(Perturbations) 82 84 86 SQuAD 1020 50 100 #(Perturbations) 92 94 96 WritingP DetectGPT NPR(ours) Figure 2: Comparison of DetectGPT to NPR averaged across six models (in terms of AUROC). (The full results are given in Figure 6 in the Appendix). methods for detecting machine-generated text by evaluating the per-token log probability of texts and using thresholding. Mitchell et al. (2023) observed that machine-generated texts tend to lie in the local curvature of the log probability and proposed De- tectGPT, whose prominent performance can only be guaranteed by the large size of the perturbation function and by a large number of perturbations, and thus costs more computational resources. Other work explored watermarking, which im- prints specific patterns of the LLM-output text that can be detected by an algorithm while 
```

### Retrieved Chunk 3

- Source: `Fast-DetectGPT Efficient Zero-Shot Detection of Machine-Generated Text via Conditional Probability Curvature.pdf`
- Page: `4`
- Chunk ID: `2219`
- Chunk Type: `main`
- Vector Score: `unknown`
- Reranker Score: `7.364211559295654`

```text
Published as a conference paper at ICLR 2024 Algorithm 1 Fast-DetectGPT machine-generated text detection. Input: passage x, sampling model qφ, scoring model pθ, and decision threshold ϵ Output: True – probably machine-generated, False – probably human-written. 1: function FAST DETECT GPT( x, qφ, pθ) 2: ˜xi ∼ qφ(˜x|x), i ∈ [1..N ] ▷ Conditional sampling 3: ˜µ ← 1 N P i log pθ(˜xi|x) ▷ Estimate the mean 4: ˜σ2 ← 1 N −1 P i(log pθ(˜xi|x) − ˜µ)2 ▷ Estimate the variance 5: ˆdx ← (log pθ(x) − ˜µ)/˜σ ▷ Estimate conditional probability curvature 6: return ˆdx > ϵ torch.distributions.categorical.Categorical(logits=lprobs).sample([10000]), where the lprobs is the log probability distribution of qφ(˜xj|x<j) for j from 0 to the length of x. The sampling process plays a pivotal role in guiding us toward the solution. To discern whether a token within a given context is machine-generated or human-auth
```

### Retrieved Chunk 4

- Source: `DetectLLM Leveraging Log Rank Information for Zero-Shot Detection of Machine-Generated Text.pdf`
- Page: `0`
- Chunk ID: `1761`
- Chunk Type: `main`
- Vector Score: `unknown`
- Reranker Score: `7.34819221496582`

```text
to detect machine-generated text, preventing malicious use such as plagiarism, misinforma- tion, and propaganda. In this paper, we intro- duce two novel zero-shot methods for detecting machine-generated text by leveraging the Log- Rank information. One is called DetectLLM- LRR, which is fast and efficient, and the other is called DetectLLM-NPR, which is more ac- curate, but slower due to the need for perturba- tions. Our experiments on three datasets and seven language models show that our proposed methods improve over the state of the art by 3.9 and 1.75 AUROC points absolute. More- over, DetectLLM-NPR needs fewer perturba- tions than previous work to achieve the same level of performance, which makes it more practical for real-world use. We also investi- gate the efficiency-performance trade-off based on users’ preference for these two measures and provide intuition for using them in p
```

### Retrieved Chunk 5

- Source: `DetectLLM Leveraging Log-Rank Information for Zero-Shot Detection of Machine-Generated Text.pdf`
- Page: `0`
- Chunk ID: `1843`
- Chunk Type: `main`
- Vector Score: `unknown`
- Reranker Score: `7.34819221496582`

```text
to detect machine-generated text, preventing malicious use such as plagiarism, misinforma- tion, and propaganda. In this paper, we intro- duce two novel zero-shot methods for detecting machine-generated text by leveraging the Log- Rank information. One is called DetectLLM- LRR, which is fast and efficient, and the other is called DetectLLM-NPR, which is more ac- curate, but slower due to the need for perturba- tions. Our experiments on three datasets and seven language models show that our proposed methods improve over the state of the art by 3.9 and 1.75 AUROC points absolute. More- over, DetectLLM-NPR needs fewer perturba- tions than previous work to achieve the same level of performance, which makes it more practical for real-world use. We also investi- gate the efficiency-performance trade-off based on users’ preference for these two measures and provide intuition for using them in p
```

### Retrieved Chunk 6

- Source: `DetectGPT-SC Improving Detection of Text Generated by Large Language Models through Self-Consistency with Masked Predictions.pdf`
- Page: `2`
- Chunk ID: `1519`
- Chunk Type: `main`
- Vector Score: `unknown`
- Reranker Score: `7.316025733947754`

```text
of watermarks is also a challenge we need to address. However, with the emergence of ChatGPT, an innovative statistical detection method called DetectGPT [5] has been developed. Its principle is that text generated by the model typically resides in the negative curvature region of the model’s log probability. DetectGPT [ 5] generates and compares multiple variants of model-generated texts to determine whether the texts are machine-generated based on the log probabilities of the original texts and these variants. DetectGPT [5] outperforms the vast majority of existing zero-shot methods in terms of model sample detection, achieving very high AUC. It is based on this concept that DetectGPT-SC was proposed. 3 Methodology Predefined definition X is the original input text. ˆX is the sentence masked within X, which can also be referred to as "<mask>". P ( ˆX) is the mask content predicted by C
```

### Retrieved Chunk 7

- Source: `Fast-DetectGPT Efficient Zero-Shot Detection of Machine-Generated Text via Conditional Probability Curvature.pdf`
- Page: `1`
- Chunk ID: `2207`
- Chunk Type: `main`
- Vector Score: `unknown`
- Reranker Score: `7.041775226593018`

```text
supervised classifiers on detection accuracy. This stems from their need for “universal features” that can function across multiple domains and languages (Gehrmann et al., 2019; Mitchell et al., 2023). A typical zero-shot classifier, DetectGPT (Mitchell et al., 2023), works under the assumption that machine-generated text variations typically have lower model probability than the original, while human-written ones could go either way. Despite its effectiveness, employing probability curvature demands the execution of around one hundred model calls or interactions with services such as the OpenAI API to create the perturbation texts, leading to prohibitive computational costs. In this paper, we posit a new hypothesis for detecting machine-generated text. By viewing text generation as a sequential decision-making process on tokens, our core assertion is that humans and machines exhibit dis
```

### Retrieved Chunk 8

- Source: `DetectGPT-SC Improving Detection of Text Generated by Large Language Models through Self-Consistency with Masked Predictions.pdf`
- Page: `2`
- Chunk ID: `1520`
- Chunk Type: `main`
- Vector Score: `unknown`
- Reranker Score: `6.773212432861328`

```text
"<mask>". P ( ˆX) is the mask content predicted by ChatGPT. DetectGPT-SC is based on the hypothesis that AI-generated texts can still undergo reasoning by large language models using the same logical reasoning process even when certain portions of the texts are masked, which distinguishes it from texts generated by humans. DetectGPT-SC is shown in Figure 1, by masking the input text X multiple times, we obtain ˆX1, ˆX2, and ˆX3, which represent the masked content in X. Simultaneously, we replace the corresponding positions in the input text X with the "<mask>" token. Then, we utilize ChatGPT to generate completions for the masked ˆX1, ˆX2, and ˆX3, resulting in new inferred results: P ( ˆX1), P ( ˆX2), and P ( ˆX3). Next, we employ cosine similarity and Word2Vec to compute the similarity betweenP ( ˆXi), i = 1, 2, 3 and ˆXi, i = 1, 2, 3. Word2Vec is a word embedding model that represents
```


### Manual Judgment

Please inspect the retrieved chunks and fill in:

- Which setting retrieves more useful chunks?
- Does the reranker move more relevant chunks to the top?
- Does the reranker reduce checklist / references / appendix noise?
- Does the reranker hurt source diversity for broad questions?
- Overall winner: Vector-only / Reranker / Tie

---

## Statistical guarantee query

### Question

Which methods provide statistical guarantees for AI-generated text detection?

### Retrieval Mode

- Vector-only mode: `global`
- Reranker mode: `global`

### Candidate Papers

The candidate papers should be the same or very similar, because both settings use the same paper-level retrieval.

#### Vector-only Candidate Papers

1. `SeqXGPT Sentence-Level AI-Generated Text Detection.pdf`
   - Title: SeqXGPT Sentence Level AI Generated Text Detection
   - Paper score: `0.35137027502059937`

2. `Intrinsic Dimension Estimation for Robust Detection of AI-Generated Texts.pdf`
   - Title: Intrinsic Dimension Estimation for Robust Detection of AI Generated Texts
   - Paper score: `0.35572031140327454`

3. `DetectGPT-SC Improving Detection of Text Generated by Large Language Models through Self-Consistency with Masked Predictions.pdf`
   - Title: DetectGPT SC Improving Detection of Text Generated by Large Language Models through Self Consistency with Masked Predictions
   - Paper score: `0.35857266187667847`

4. `Unsupervised and Distributional Detection of Machine-Generated Text.pdf`
   - Title: Unsupervised and Distributional Detection of Machine Generated Text
   - Paper score: `0.3624788224697113`


#### Reranker Candidate Papers

1. `SeqXGPT Sentence-Level AI-Generated Text Detection.pdf`
   - Title: SeqXGPT Sentence Level AI Generated Text Detection
   - Paper score: `0.35137027502059937`

2. `Intrinsic Dimension Estimation for Robust Detection of AI-Generated Texts.pdf`
   - Title: Intrinsic Dimension Estimation for Robust Detection of AI Generated Texts
   - Paper score: `0.35572031140327454`

3. `DetectGPT-SC Improving Detection of Text Generated by Large Language Models through Self-Consistency with Masked Predictions.pdf`
   - Title: DetectGPT SC Improving Detection of Text Generated by Large Language Models through Self Consistency with Masked Predictions
   - Paper score: `0.35857266187667847`

4. `Unsupervised and Distributional Detection of Machine-Generated Text.pdf`
   - Title: Unsupervised and Distributional Detection of Machine Generated Text
   - Paper score: `0.3624788224697113`


### Selected Papers

#### Vector-only Selected Papers

1. `SeqXGPT Sentence-Level AI-Generated Text Detection.pdf`
   - Title: SeqXGPT Sentence Level AI Generated Text Detection
   - Paper score: `0.35137027502059937`

2. `Intrinsic Dimension Estimation for Robust Detection of AI-Generated Texts.pdf`
   - Title: Intrinsic Dimension Estimation for Robust Detection of AI Generated Texts
   - Paper score: `0.35572031140327454`

3. `DetectGPT-SC Improving Detection of Text Generated by Large Language Models through Self-Consistency with Masked Predictions.pdf`
   - Title: DetectGPT SC Improving Detection of Text Generated by Large Language Models through Self Consistency with Masked Predictions
   - Paper score: `0.35857266187667847`

4. `Unsupervised and Distributional Detection of Machine-Generated Text.pdf`
   - Title: Unsupervised and Distributional Detection of Machine Generated Text
   - Paper score: `0.3624788224697113`


#### Reranker Selected Papers

1. `SeqXGPT Sentence-Level AI-Generated Text Detection.pdf`
   - Title: SeqXGPT Sentence Level AI Generated Text Detection
   - Paper score: `0.35137027502059937`

2. `Intrinsic Dimension Estimation for Robust Detection of AI-Generated Texts.pdf`
   - Title: Intrinsic Dimension Estimation for Robust Detection of AI Generated Texts
   - Paper score: `0.35572031140327454`

3. `DetectGPT-SC Improving Detection of Text Generated by Large Language Models through Self-Consistency with Masked Predictions.pdf`
   - Title: DetectGPT SC Improving Detection of Text Generated by Large Language Models through Self Consistency with Masked Predictions
   - Paper score: `0.35857266187667847`

4. `Unsupervised and Distributional Detection of Machine-Generated Text.pdf`
   - Title: Unsupervised and Distributional Detection of Machine Generated Text
   - Paper score: `0.3624788224697113`


### Summary Statistics

| Metric | Vector-only | With reranker |
|---|---:|---:|
| Retrieved chunks | 8 | 8 |
| Unique sources | 4 | 3 |
| Noisy chunks | 0 | 0 |
| Overlap chunks | 2 | 2 |

### Source Distribution

#### Vector-only

- `Intrinsic Dimension Estimation for Robust Detection of AI-Generated Texts.pdf`: 3 chunks
- `SeqXGPT Sentence-Level AI-Generated Text Detection.pdf`: 2 chunks
- `Unsupervised and Distributional Detection of Machine-Generated Text.pdf`: 2 chunks
- `DetectGPT-SC Improving Detection of Text Generated by Large Language Models through Self-Consistency with Masked Predictions.pdf`: 1 chunks

#### With reranker

- `SeqXGPT Sentence-Level AI-Generated Text Detection.pdf`: 3 chunks
- `DetectGPT-SC Improving Detection of Text Generated by Large Language Models through Self-Consistency with Masked Predictions.pdf`: 3 chunks
- `Intrinsic Dimension Estimation for Robust Detection of AI-Generated Texts.pdf`: 2 chunks

### Vector-only Retrieved Chunks

### Retrieved Chunk 1

- Source: `Intrinsic Dimension Estimation for Robust Detection of AI-Generated Texts.pdf`
- Page: `6`
- Chunk ID: `2576`
- Chunk Type: `main`
- Vector Score: `0.32673242688179016`
- Reranker Score: `unknown`

```text
estimation, so we use this model for all further experiments in English, and XLM-R of the same size for multilingual experiments. Artificial text detection. We show that intrinsic dimension can lead to a robust method of artificial text detection. In all experiments below, we use the one-feature thresholding classifier (see Section 4). Comparison with universal detectors. First, we show that our detector is the best among general- purpose methods designed to detect texts of any domain, generated by any AI model, without access to the generator itself. Such methods are needed, e.g., for plagiarism detection. To be applicable in real life, the algorithm should provide high artificial text detection rate while avoiding false accusations of real authors. Besides, it should be resistant to adversaries who transform the content generated by popular AI models to reduce the chance to be caught. 
```

### Retrieved Chunk 2

- Source: `SeqXGPT Sentence-Level AI-Generated Text Detection.pdf`
- Page: `1`
- Chunk ID: `3398`
- Chunk Type: `main`
- Vector Score: `0.334208607673645`
- Reranker Score: `unknown`

```text
existing methods, such as DetectGPT and Sniffer, fail to solve sentence-level AIGT detection. Our proposed SeqXGPT not only obtains promising results in both sentence and document-level AIGT detection challenges, but also exhibits excellent generalization on out-of-distribution datasets. 2 Background The proliferation of Large Language Models (LLMs) such as GPT-4 has given rise to increased concerns about the potential misuse of AI- generated texts (AIGT) (Brown et al., 2020; Zhang et al., 2022; Scao et al., 2022). This emphasizes the necessity for robust detection mechanisms to ensure security and trustworthiness of LLM applications. 2.1 Principal Approaches to AIGT Detection Broadly, AIGT detection methodologies fall into two primary categories: 1. Supervised Learning: This involves training models on labeled datasets to distinguish between human and AI-generated texts. Notable efforts
```

### Retrieved Chunk 3

- Source: `Intrinsic Dimension Estimation for Robust Detection of AI-Generated Texts.pdf`
- Page: `7`
- Chunk ID: `2580`
- Chunk Type: `main`
- Vector Score: `0.3349151015281677`
- Reranker Score: `unknown`

```text
et al., 2023]. When generated texts are transformed by DIPPER, they lose some characteristic features of the generator, which causes a dramatic drop in quality for most detectors; but for the PHD classifier the accuracy of artificial text detection even increases slightly after this perturbation. Interestingly, the MLE dimension estimator also works quite well for this task, and even achieves 6% better detection for GPT-3.5 generations; but its adversarial robustness is significantly worse. Cross-domain and cross-model performance. Table 3 shows that our ID estimation is stable across text domains; consequently, our proposed PHD text detector is robust to domain transfer. We compare the cross-domain ability of PHD with a supervised classifier obtained by fine-tuning RoBERTa- base with a linear classification head on its CLS token, a supervised classification approach used previously for 
```

### Retrieved Chunk 4

- Source: `SeqXGPT Sentence-Level AI-Generated Text Detection.pdf`
- Page: `2`
- Chunk ID: `3402`
- Chunk Type: `main`
- Vector Score: `0.3373628258705139`
- Reranker Score: `unknown`

```text
consisting of few sentences, which can potentially lead to a higher rate of false negatives or false positives. In response to this limitation, we aim to study sentence-level AIGT detection . Sentence-level AIGT detection offers a fine-grained text analysis compared to document-level AIGT detection, as it explores each sentence within the entire text. By addressing this challenge, we could significantly reduce the risk of misidentification and achieve both higher detection accuracy and finer detection granularity than document-level detection. Similarly, we study sentence-level detection challenges as follows: 1. Particular-Model Binary AIGT Detection: Discriminate whether each sentence within a candidate document is generated by a specific model or by a human. 2. Mixed-Model Binary AIGT Detection: Discriminate whether each sentence is generated by an AI model or a human, regardless of w
```

### Retrieved Chunk 5

- Source: `Intrinsic Dimension Estimation for Robust Detection of AI-Generated Texts.pdf`
- Page: `0`
- Chunk ID: `2543`
- Chunk Type: `main`
- Vector Score: `0.3454873561859131`
- Reranker Score: `unknown`

```text
Intrinsic Dimension Estimation for Robust Detection of AI-Generated Texts Eduard Tulchinskii1, Kristian Kuznetsov1, Laida Kushnareva2, Daniil Cherniavskii3, Sergey Nikolenko5, Evgeny Burnaev1,3, Serguei Barannikov1,4, Irina Piontkovskaya2 1Skolkovo Institute of Science and Technology, Russia; 2AI Foundation and Algorithm Lab, Russia; 3Artificial Intelligence Research Institute (AIRI), Russia;4CNRS, Université Paris Cité, France; 5St. Petersburg Department of the Steklov Institute of Mathematics, Russia Abstract Rapidly increasing quality of AI-generated content makes it difficult to distinguish between human and AI-generated texts, which may lead to undesirable conse- quences for society. Therefore, it becomes increasingly important to study the properties of human texts that are invariant over different text domains and varying proficiency of human writers, can be easily calculated for 
```

### Retrieved Chunk 6

- Source: `DetectGPT-SC Improving Detection of Text Generated by Large Language Models through Self-Consistency with Masked Predictions.pdf`
- Page: `1`
- Chunk ID: `1516`
- Chunk Type: `main`
- Vector Score: `0.34866413474082947`
- Reranker Score: `unknown`

```text
classifiers. • Accurate domain invariant detection : We introduce a strategy of implementing self-consistency with masked predictions in LLMs to enhance the accuracy of text detection. Our method overcomes the constraints of training separate classifiers, amassing extensive datasets of real or generated texts, or explicitly adding watermarks to the generated content. It can be realized by simply interacting with LLMs using prompts. In text detection across different domains, DetectGPT-SC achieved an accuracy of 91.1% on HC3 and 93.3% on CYN, demonstrating strong detection and generalization capabilities. • Comprehensive empirical evaluation: We conducted extensive empirical evaluations using the most advanced text detectors ChatGPT Detector [4], GLTR [1], PPL [4], Roberta-base-openai-detector [2], and DetectGPT [5] on CYN dataset and HC3 dataset. 2
```

### Retrieved Chunk 7

- Source: `Unsupervised and Distributional Detection of Machine-Generated Text.pdf`
- Page: `0`
- Chunk ID: `3657`
- Chunk Type: `main`
- Vector Score: `0.3531365990638733`
- Reranker Score: `unknown`

```text
Unsupervised and Distributional Detection of Machine-Generated Text Matthias Gallé and Jos Rozen and Germán Kruszewski and Hady Elsahar Naver Labs Europe Abstract The power of natural language generation models has provoked a ﬂurry of interest in au- tomatic methods to detect if a piece of text is human or machine-authored. The problem so far has been framed in a standard super- vised way and consists in training a classiﬁer on annotated data to predict the origin of one given new document. In this paper, we frame the problem in an unsupervised and distribu- tional way: we assume that we have access to a large collection of unannotated documents, a big fraction of which is machine-generated. We propose a method to detect those machine-generated documents leveraging re- peated higher-order n-grams, which we show over-appear in machine-generated text as com- pared to human ones. That weak 
```

### Retrieved Chunk 8

- Source: `Unsupervised and Distributional Detection of Machine-Generated Text.pdf`
- Page: `1`
- Chunk ID: `3661`
- Chunk Type: `main`
- Vector Score: `0.3547978699207306`
- Reranker Score: `unknown`

```text
this precise setting and showed that the quality of a human/machine discriminator degraded quickly when the prompts used to generate text where from a different domain. On the other side, the problem of determining the origin of one ﬁxed document is in most use cases not the real problem. As an ex- ample, an article generated by an existing template- based data-to-text method (Reiter and Dale, 2000) is arguably of less concern than an article diffusing false information written by a human author. In- deed, one danger of the current language models lies in their capacity of generating a huge amount of human-like text but biased towards a desired opinion or topic (Leroux, 2020; Buchanan et al., 2021). We therefore frame the problem of detecting machine-generated texts as follows: given a set of documents, and the suspicion that a large fraction of them is generated by machine; is it possib
```


### Reranker Retrieved Chunks

### Retrieved Chunk 1

- Source: `SeqXGPT Sentence-Level AI-Generated Text Detection.pdf`
- Page: `1`
- Chunk ID: `3398`
- Chunk Type: `main`
- Vector Score: `unknown`
- Reranker Score: `5.327618598937988`

```text
existing methods, such as DetectGPT and Sniffer, fail to solve sentence-level AIGT detection. Our proposed SeqXGPT not only obtains promising results in both sentence and document-level AIGT detection challenges, but also exhibits excellent generalization on out-of-distribution datasets. 2 Background The proliferation of Large Language Models (LLMs) such as GPT-4 has given rise to increased concerns about the potential misuse of AI- generated texts (AIGT) (Brown et al., 2020; Zhang et al., 2022; Scao et al., 2022). This emphasizes the necessity for robust detection mechanisms to ensure security and trustworthiness of LLM applications. 2.1 Principal Approaches to AIGT Detection Broadly, AIGT detection methodologies fall into two primary categories: 1. Supervised Learning: This involves training models on labeled datasets to distinguish between human and AI-generated texts. Notable efforts
```

### Retrieved Chunk 2

- Source: `DetectGPT-SC Improving Detection of Text Generated by Large Language Models through Self-Consistency with Masked Predictions.pdf`
- Page: `0`
- Chunk ID: `1509`
- Chunk Type: `main`
- Vector Score: `unknown`
- Reranker Score: `4.409615993499756`

```text
DETECT GPT-SC: I MPROVING DETECTION OF TEXT GENERATED BY LARGE LANGUAGE MODELS THROUGH SELF -C ONSISTENCY WITH MASKED PREDICTIONS Rongsheng Wang Macao Polytechnic University p2213046@mpu.edu.mo Qi Li Iowa State University qli@iastate.edu Sihong Xie∗ HKUST (GZ) sihongxie@hkust-gz.edu.cn ABSTRACT General large language models (LLMs) such as ChatGPT have shown remarkable success, but it has also raised concerns among people about the misuse of AI-generated texts. Therefore, an important question is how to detect whether the texts are generated by ChatGPT or by humans. Existing detectors are built on the assumption that there is a distribution gap between human-generated and AI-generated texts. These gaps are typically identified using statistical information or classifiers. In contrast to prior research methods, we find that large language models such as ChatGPT exhibit strong self-consiste
```

### Retrieved Chunk 3

- Source: `Intrinsic Dimension Estimation for Robust Detection of AI-Generated Texts.pdf`
- Page: `6`
- Chunk ID: `2576`
- Chunk Type: `main`
- Vector Score: `unknown`
- Reranker Score: `4.126020431518555`

```text
estimation, so we use this model for all further experiments in English, and XLM-R of the same size for multilingual experiments. Artificial text detection. We show that intrinsic dimension can lead to a robust method of artificial text detection. In all experiments below, we use the one-feature thresholding classifier (see Section 4). Comparison with universal detectors. First, we show that our detector is the best among general- purpose methods designed to detect texts of any domain, generated by any AI model, without access to the generator itself. Such methods are needed, e.g., for plagiarism detection. To be applicable in real life, the algorithm should provide high artificial text detection rate while avoiding false accusations of real authors. Besides, it should be resistant to adversaries who transform the content generated by popular AI models to reduce the chance to be caught. 
```

### Retrieved Chunk 4

- Source: `SeqXGPT Sentence-Level AI-Generated Text Detection.pdf`
- Page: `1`
- Chunk ID: `3400`
- Chunk Type: `main`
- Vector Score: `unknown`
- Reranker Score: `4.082741737365723`

```text
a perturbation-based method leveraging average per-token log probabilities. The recent work of Li et al. (2023) extends this further by studying multi-model detection through text perplexities, aiming to trace the precise LLM origin of texts. 2.2 Detection Task Formulations The AIGT detection tasks can be formulated in different setups: 1. Particular-Model Binary AIGT Detection: In this setup, the objective is to discriminate whether a text was produced by a specific known AI model or by a human. Both GPTZero and DetectGPT fall into this category. 2. Mixed-Model Binary AIGT Detection: Here, the detectors are designed to identify AI-generated content without the need to pinpoint the exact model of origin. 3https://gptzero.me/
```

### Retrieved Chunk 5

- Source: `DetectGPT-SC Improving Detection of Text Generated by Large Language Models through Self-Consistency with Masked Predictions.pdf`
- Page: `0`
- Chunk ID: `1510`
- Chunk Type: `main`
- Vector Score: `unknown`
- Reranker Score: `4.067139625549316`

```text
self-consistency in text generation and continuation. Self-consistency capitalizes on the intuition that AI-generated texts can still be reasoned with by large language models using the same logical reasoning when portions of the texts are masked, which differs from human-generated texts. Using this observation, we subsequently proposed a new method for AI-generated texts detection based on self-consistency with masked predictions to determine whether a text is generated by LLMs. This method, which we call DetectGPT-SC. We conducted a series of experiments to evaluate the performance of DetectGPT-SC. In these experiments, we employed various mask scheme, zero-shot, and simple prompt for completing masked texts and self-consistency predictions. The results indicate that DetectGPT-SC outperforms the current state-of-the-art across different tasks. 1 Introduction Large language models (LLMs
```

### Retrieved Chunk 6

- Source: `SeqXGPT Sentence-Level AI-Generated Text Detection.pdf`
- Page: `0`
- Chunk ID: `3395`
- Chunk Type: `main`
- Vector Score: `unknown`
- Reranker Score: `4.037962913513184`

```text
can efficiently conduct sentence-level AIGT detection. given text is written or modified by an AI system (Mitchell et al., 2023; Li et al., 2023). Current AIGT detection strategies, such as supervised-learned discriminator 2, perplexity- based methods (Mitchell et al., 2023; Li et al., 2023), etc., focus on discriminating whether a whole document is generated by an AI. However, users often modify partial texts with LLMs rather than put full trust in LLMs to generate a whole document. Therefore, it is important to explore fine-grained (e.g. sentence-level) AIGT detection. Building methods that solve the sentence-level AIGT detection challenge is not an incremental modification over document-level AIGT detection. On the one hand, model-wise methods like DetectGPT and Sniffer require a rather long document as input (over 100 tokens), making 2https://github.com/openai/ gpt-2-output-dataset a
```

### Retrieved Chunk 7

- Source: `DetectGPT-SC Improving Detection of Text Generated by Large Language Models through Self-Consistency with Masked Predictions.pdf`
- Page: `2`
- Chunk ID: `1517`
- Chunk Type: `main`
- Vector Score: `unknown`
- Reranker Score: `4.031418323516846`

```text
Running Title for Header 2 Related Work Recent research has shown promising results in the development of detection methods. The existing detectors are built on the assumption that there is a distributional difference between human-generated texts and AI-generated texts. These differences are typically identified by training classifiers or using statistical information. Classifier-based detectors. Classifier-based detectors are commonly used in natural language processing detection paradigms, especially in fake news and misinformation detection [3]. Guo et al. [4] proposed the ChatGPT Detector, where they initially constructed a dataset consisting of ChatGPT conversations with human questions and answers, and trained a text detection classifier based on this dataset. The use of these methods requires substantial data collection and incurs the cost of training these classifier models.
```

### Retrieved Chunk 8

- Source: `Intrinsic Dimension Estimation for Robust Detection of AI-Generated Texts.pdf`
- Page: `0`
- Chunk ID: `2544`
- Chunk Type: `main`
- Vector Score: `unknown`
- Reranker Score: `3.231004238128662`

```text
proficiency of human writers, can be easily calculated for any language, and can robustly separate natural and AI-generated texts regardless of the generation model and sampling method. In this work, we propose such an invariant for human- written texts, namely the intrinsic dimensionality of the manifold underlying the set of embeddings for a given text sample. We show that the average intrinsic dimensionality of fluent texts in a natural language is hovering around the value 9 for several alphabet-based languages and around 7 for Chinese, while the average intrinsic dimensionality of AI-generated texts for each language is ≈ 1.5 lower, with a clear statistical separation between human-generated and AI-generated distri- butions. This property allows us to build a score-based artificial text detector. The proposed detector’s accuracy is stable over text domains, generator models, and hum
```


### Manual Judgment

Please inspect the retrieved chunks and fill in:

- Which setting retrieves more useful chunks?
- Does the reranker move more relevant chunks to the top?
- Does the reranker reduce checklist / references / appendix noise?
- Does the reranker hurt source diversity for broad questions?
- Overall winner: Vector-only / Reranker / Tie

---

## Comparison between DetectGPT and AdaDetectGPT

### Question

What is the difference between DetectGPT and AdaDetectGPT?

### Retrieval Mode

- Vector-only mode: `global`
- Reranker mode: `global`

### Candidate Papers

The candidate papers should be the same or very similar, because both settings use the same paper-level retrieval.

#### Vector-only Candidate Papers

1. `AdaDetectGPT Adaptive Detection of LLM-Generated Text with Statistical Guarantees.pdf`
   - Title: AdaDetectGPT Adaptive Detection of LLM Generated Text with Statistical Guarantees
   - Paper score: `0.6420181393623352`

2. `Fast-DetectGPT Efficient Zero-Shot Detection of Machine-Generated Text via Conditional Probability Curvature.pdf`
   - Title: Fast DetectGPT Efficient Zero Shot Detection of Machine Generated Text via Conditional Probability Curvature
   - Paper score: `0.6681676506996155`

3. `DetectGPT-SC Improving Detection of Text Generated by Large Language Models through Self-Consistency with Masked Predictions.pdf`
   - Title: DetectGPT SC Improving Detection of Text Generated by Large Language Models through Self Consistency with Masked Predictions
   - Paper score: `0.6825336217880249`

4. `GPT-who AnInformation Density-based Machine-Generated Text Detector.pdf`
   - Title: GPT who AnInformation Density based Machine Generated Text Detector
   - Paper score: `0.6846862435340881`


#### Reranker Candidate Papers

1. `AdaDetectGPT Adaptive Detection of LLM-Generated Text with Statistical Guarantees.pdf`
   - Title: AdaDetectGPT Adaptive Detection of LLM Generated Text with Statistical Guarantees
   - Paper score: `0.6420181393623352`

2. `Fast-DetectGPT Efficient Zero-Shot Detection of Machine-Generated Text via Conditional Probability Curvature.pdf`
   - Title: Fast DetectGPT Efficient Zero Shot Detection of Machine Generated Text via Conditional Probability Curvature
   - Paper score: `0.6681676506996155`

3. `DetectGPT-SC Improving Detection of Text Generated by Large Language Models through Self-Consistency with Masked Predictions.pdf`
   - Title: DetectGPT SC Improving Detection of Text Generated by Large Language Models through Self Consistency with Masked Predictions
   - Paper score: `0.6825336217880249`

4. `GPT-who AnInformation Density-based Machine-Generated Text Detector.pdf`
   - Title: GPT who AnInformation Density based Machine Generated Text Detector
   - Paper score: `0.6846862435340881`


### Selected Papers

#### Vector-only Selected Papers

1. `AdaDetectGPT Adaptive Detection of LLM-Generated Text with Statistical Guarantees.pdf`
   - Title: AdaDetectGPT Adaptive Detection of LLM Generated Text with Statistical Guarantees
   - Paper score: `0.6420181393623352`

2. `Fast-DetectGPT Efficient Zero-Shot Detection of Machine-Generated Text via Conditional Probability Curvature.pdf`
   - Title: Fast DetectGPT Efficient Zero Shot Detection of Machine Generated Text via Conditional Probability Curvature
   - Paper score: `0.6681676506996155`

3. `DetectGPT-SC Improving Detection of Text Generated by Large Language Models through Self-Consistency with Masked Predictions.pdf`
   - Title: DetectGPT SC Improving Detection of Text Generated by Large Language Models through Self Consistency with Masked Predictions
   - Paper score: `0.6825336217880249`

4. `GPT-who AnInformation Density-based Machine-Generated Text Detector.pdf`
   - Title: GPT who AnInformation Density based Machine Generated Text Detector
   - Paper score: `0.6846862435340881`


#### Reranker Selected Papers

1. `AdaDetectGPT Adaptive Detection of LLM-Generated Text with Statistical Guarantees.pdf`
   - Title: AdaDetectGPT Adaptive Detection of LLM Generated Text with Statistical Guarantees
   - Paper score: `0.6420181393623352`

2. `Fast-DetectGPT Efficient Zero-Shot Detection of Machine-Generated Text via Conditional Probability Curvature.pdf`
   - Title: Fast DetectGPT Efficient Zero Shot Detection of Machine Generated Text via Conditional Probability Curvature
   - Paper score: `0.6681676506996155`

3. `DetectGPT-SC Improving Detection of Text Generated by Large Language Models through Self-Consistency with Masked Predictions.pdf`
   - Title: DetectGPT SC Improving Detection of Text Generated by Large Language Models through Self Consistency with Masked Predictions
   - Paper score: `0.6825336217880249`

4. `GPT-who AnInformation Density-based Machine-Generated Text Detector.pdf`
   - Title: GPT who AnInformation Density based Machine Generated Text Detector
   - Paper score: `0.6846862435340881`


### Summary Statistics

| Metric | Vector-only | With reranker |
|---|---:|---:|
| Retrieved chunks | 8 | 8 |
| Unique sources | 3 | 3 |
| Noisy chunks | 0 | 0 |
| Overlap chunks | 2 | 2 |

### Source Distribution

#### Vector-only

- `AdaDetectGPT Adaptive Detection of LLM-Generated Text with Statistical Guarantees.pdf`: 3 chunks
- `Fast-DetectGPT Efficient Zero-Shot Detection of Machine-Generated Text via Conditional Probability Curvature.pdf`: 3 chunks
- `GPT-who AnInformation Density-based Machine-Generated Text Detector.pdf`: 2 chunks

#### With reranker

- `AdaDetectGPT Adaptive Detection of LLM-Generated Text with Statistical Guarantees.pdf`: 3 chunks
- `Fast-DetectGPT Efficient Zero-Shot Detection of Machine-Generated Text via Conditional Probability Curvature.pdf`: 3 chunks
- `DetectGPT-SC Improving Detection of Text Generated by Large Language Models through Self-Consistency with Masked Predictions.pdf`: 2 chunks

### Vector-only Retrieved Chunks

### Retrieved Chunk 1

- Source: `AdaDetectGPT Adaptive Detection of LLM-Generated Text with Statistical Guarantees.pdf`
- Page: `9`
- Chunk ID: `255`
- Chunk Type: `main`
- Vector Score: `0.366325318813324`
- Reranker Score: `unknown`

```text
Fast-DetectGPT 0.9048 0.95880.98470.9800 0.9571 0.9019 0.93610.97680.9608 0.9439 AdaDetectGPT 0.90720.96110.98320.9841 0.95890.91760.94000.97280.9610 0.9478 Relative ( ) 2.4288 5.6095 — 20.4444 4.2454 16.0326 6.0543 — 0.3405 6.9929 Table 3: Detection of LLM-generated text under two adversarial attacks in black-box settings. Paraphrasing Decoherence DetectGPT Xsum Writing PubMed Avg. Xsum Writing PubMed Avg. Fast (GPT-J/GPT-2) 0.91780.91370.7944 0.8753 0.7884 0.9595 0.7870 0.8449 Ada (GPT-J/GPT-2)0.92250.91210.8029 0.8792 0.8765 0.9597 0.8284 0.8882 Fast (GPT-J/Neo-2.7) 0.96020.91850.7310 0.8699 0.8579 0.9701 0.7609 0.8630 Ada (GPT-J/Neo-2.7)0.96230.91810.7587 0.8797 0.9230 0.9704 0.8124 0.9019 Fast (GPT-J/GPT-J) 0.95370.94580.7041 0.8679 0.88360.98690.7550 0.8752 Ada (GPT-J/GPT-J)0.95870.94490.7308 0.8781 0.93360.98640.8008 0.9070 underperforms Binoculars or RADAR. Nonetheless, AdaDetect
```

### Retrieved Chunk 2

- Source: `AdaDetectGPT Adaptive Detection of LLM-Generated Text with Statistical Guarantees.pdf`
- Page: `9`
- Chunk ID: `256`
- Chunk Type: `main`
- Vector Score: `0.3740534782409668`
- Reranker Score: `unknown`

```text
underperforms Binoculars or RADAR. Nonetheless, AdaDetectGPT consistently improves upon Fast-DetectGPT across various datasets, with gains on Essay reaching up to 37.8%. Additionally, we evaluate AdaDetectGPT’s robustness to two adversarial attacks, paraphrasing and decoherence, in the black-box setting. As shown in Table 3, AdaDetectGPT demonstrates greater resilience than Fast-DetectGPT to adversarially perturbed texts. The improvement reaches up to 10% for paraphrasing and up to 85% for decoherence. Finally, we employ the same five LLMs from Table 1 to compare Fast-DetectGPT and AdaDetectGPT in black-box settings. Following Bao et al. (2024), we use GPT-J as the source LLM for detecting each of the remaining four target LLMs. Due to space constraints, the results are presented in Table S11 of Appendix F.5, where AdaDetectGPT uniformly outperforms Fast-DetectGPT in all cases, with impr
```

### Retrieved Chunk 3

- Source: `AdaDetectGPT Adaptive Detection of LLM-Generated Text with Statistical Guarantees.pdf`
- Page: `8`
- Chunk ID: `251`
- Chunk Type: `main`
- Vector Score: `0.4149060547351837`
- Reranker Score: `unknown`

```text
AdaDetectGPT0.8534 0.8420 0.8532 0.8347 0.8061 0.8379 Relative ( ) 14.1250 18.2659 21.1936 20.3301 18.4492 18.5779 reports the AUC scores of various detectors across all combinations of datasets and five source models. It can be seen that AdaDetectGPT achieves the highest AUC across all combinations of datasets and source models, outperforming Fast-DetectGPT – the best baseline method – by 12.5%-37%. We also evaluate AdaDetectGPT on three more advanced open-source LLMs: Qwen2.5 (Bai et al., 2025), Mistral (Jiang et al., 2023), and LLaMA3 (Grattafiori et al., 2024). As shown in Table S7, AdaDetectGPT delivers consistent improvements over Fast-DetectGPT and maintains competitive performance across five datasets, achieving the best results in most cases. These findings highlight the advantage of using an adaptively learned witness function for classification. In Appendix F.3, we analyze the
```

### Retrieved Chunk 4

- Source: `Fast-DetectGPT Efficient Zero-Shot Detection of Machine-Generated Text via Conditional Probability Curvature.pdf`
- Page: `20`
- Chunk ID: `2293`
- Chunk Type: `main`
- Vector Score: `0.45760059356689453`
- Reranker Score: `unknown`

```text
DetectGPT .9875 .9793 .9961 .9762 .95 .9869 .9707 .9919 .9619 .9424 .9928 .9856 .9953 .979 .9622 Fast-DetectGPT .9994 .9965 .9988 .997 .9958 .9954 .9867 .9938 .9826 .9773 .9999 .9999 .9997 .9999 .9997 (Diff) .0119 .0172 .0028 .0208 .0458 .0085 .0160 .0018 .0207 .0349 .0071 .0143 .0044 .0209 .0376 DetectGPT(fixed) .9399 .9438 .9961 .9367 .9214 .9143 .9026 .9919 .8846 .8854 .9722 .9635 .9953 .9627 .9646 Fast-Detect(fixed) .9953 .9861 .9997 .9856 .9779 .9805 .9613 .9979 .9499 .9311 .9978 .999 .9999 .9991 .998 (Diff) .0554 .0423 .0036 .0489 .0565 .0662 .0587 .0060 .0654 .0457 .0256 .0355 .0046 .0364 .0333 SQuAD Likelihood .961 .944 .9214 .8838 .8122 .9393 .9072 .8926 .8351 .7317 .9906 .987 .9792 .9572 .9094 Entropy .5369 .4736 .539 .5277 .5593 .552 .5203 .5457 .5441 .5992 .5132 .4508 .4924 .4882 .5263 LogRank .9792 .9657 .9535 .9156 .8482 .9692 .9423 .9385 .8842 .7895 .9972 .9959 .994 .9798 
```

### Retrieved Chunk 5

- Source: `Fast-DetectGPT Efficient Zero-Shot Detection of Machine-Generated Text via Conditional Probability Curvature.pdf`
- Page: `18`
- Chunk ID: `2283`
- Chunk Type: `main`
- Vector Score: `0.5024181604385376`
- Reranker Score: `unknown`

```text
Fast-DetectGPT (GPT-J/Neo-2.7) 0.9396 0.9492 0.7225 0.8704* Fast-DetectGPT (GPT-J/GPT-J) 0.9329* 0.9568 0.6664 0.8520 Table 7: Detection of GPT-3 generations, evaluated in AUROC. Fast-DetectGPT in the black-box settings (using local models) significantly outperforms DetectGPT in both the black-box setting and the white-box setting (using GPT-3) on News (XSum) and story (WritingPrompts). Fast-DetectGPT uses 6B GPT-J to generate samples and models from 1.5B GPT-2 to 6B GPT-J to score samples, while DetectGPT uses 11B T5 to generate perturbations and models from 1.5B GPT-2 to 6B GPT-J, and GPT-3 service to score them.♢ – we report the official scores from Mitchell et al. (2023) instead of rerunning the experiments after confirming the consistency on RoBERTa-base/large. Table 7 presents a comparison between Fast-DetectGPT, zero-shot DetectGPT, and supervised RoBERTa-based classifiers for the
```

### Retrieved Chunk 6

- Source: `Fast-DetectGPT Efficient Zero-Shot Detection of Machine-Generated Text via Conditional Probability Curvature.pdf`
- Page: `21`
- Chunk ID: `2297`
- Chunk Type: `main`
- Vector Score: `0.5080249905586243`
- Reranker Score: `unknown`

```text
Published as a conference paper at ICLR 2024 used in Table 2, sampling with the three strategies with k = 40 , p = 0 .96, and T = 0 .8. Fast- DetectGPT in the white-box setting obtains the best accuracy on the three sampling strategies, out- performing DetectGPT by relative 95% on Top- p sampling, relative 81% on Top- k sampling, and relative 99% on sampling with a temperature, as shown in Table 9. In the black-box setting, Fast- DetectGPT outperforms DetectGPT by relatively 92%, 80%, and 98% on the three decoding strate- gies, respectively. These results demonstrate that Fast-DetectGPT works consistently in detecting texts produced by different decoding strategies. To elucidate the trajectory of detection accuracy concerning variations in sampling hyper- parameters, we conducted additional experiments with values set top = 0.90, k = 30, and T = 0.6. As indicated in the lower segment of 
```

### Retrieved Chunk 7

- Source: `GPT-who AnInformation Density-based Machine-Generated Text Detector.pdf`
- Page: `5`
- Chunk ID: `2508`
- Chunk Type: `main`
- Vector Score: `0.5744547843933105`
- Reranker Score: `unknown`

```text
ZeroGPT (ZeroGPT, 2023), OpenAI’s detector (So- laiman et al., 2019), Li et al. (2023)’s LongFormer- based detector 7 tuned for the InTheWild bench- mark (we refer to this method as “ITW”), a sty- lometric detector8 (Abbasi and Chen, 2008) and fine-tuned BERT9 (Kenton and Toutanova, 2019). We are unable to report results for exhaustively all methods across all datasets due to inherent inap- plicability in certain task settings. For example, most SOTA text detectors cannot be applied to the ArguGPT dataset as it only contains text written by multiple machines, while most text detectors are designed to differentiate between human-written and machine-generated texts. Beyond such limita- 4https://github.com/eric-mitchell/detect-gpt 5https://github.com/HendrikStrobelt/ detecting-fake-text 6https://github.com/BurhanUlTayyab/GPTZero 7https://github.com/yafuly/DeepfakeTextDetect 8https://github.
```

### Retrieved Chunk 8

- Source: `GPT-who AnInformation Density-based Machine-Generated Text Detector.pdf`
- Page: `6`
- Chunk ID: `2511`
- Chunk Type: `main`
- Vector Score: `0.5855199098587036`
- Reranker Score: `unknown`

```text
Task Type Domain GPTZero ZeroGPT OpenAI Detector DetectGPT BERT ITW GPT -who CS 0.30 0.67 0.81 0.58 0.99 0.98 0.99 PHX 0.25 0.68 0.70 0.54 0.99 0.98 0.98Task 1 HSS 0.72 0.92 0.63 0.57 0.99 0.96 0.98 CS 0.17 0.25 0.64 0.16 0.99 0.81 0.84 PHX 0.06 0.10 0.24 0.17 0.96 0.76 0.90Task 2 HSS 0.44 0.62 0.27 0.20 0.97 0.29 0.80 CS 0.02 0.03 0.06 0.03 0.97 0.38 0.63 PHX 0.02 0.03 0.04 0.05 0.97 0.31 0.75Task 3 HSS 0.20 0.25 0.06 0.06 0.99 0.08 0.62 Average F1 0.24 0.40 0.38 0.26 0.98 0.62 0.83 Table 2: Test Set Performance (F1 Scores) of different machine text detectors on the GPA Benchmark. Best performance are in bold, and second best underlined. Human v. GROVER GTLR GPTZero DetectGPT RoBERTa BERT ITW Stylometry GPT -who GPT-1 0.58 0.47 0.47 0.51 0.98 0.95 0.92 0.99 1.00 GPT-2_small 0.57 0.51 0.51 0.51 0.71 0.75 0.47 0.75 0.88 GPT-2_medium 0.56 0.49 0.50 0.52 0.75 0.65 0.47 0.72 0.87 GPT-2_large
```


### Reranker Retrieved Chunks

### Retrieved Chunk 1

- Source: `AdaDetectGPT Adaptive Detection of LLM-Generated Text with Statistical Guarantees.pdf`
- Page: `4`
- Chunk ID: `229`
- Chunk Type: `main`
- Vector Score: `unknown`
- Reranker Score: `6.326869010925293`

```text
0 1 2 3 Differences in statistical measures 0 1 FastDetectGPT AdaDetectGPT Dataset: SQuAD 1  0 1 2 3 4 Differences in statistical measures 0 1 FastDetectGPT AdaDetectGPT Dataset: Writing Figure 2: Boxplots visualizing the differences in the statistical measures between human- and LLM- authored passages, comparing AdaDetectGPT (with a learned witness function) and Fast-DetectGPT (without it). A larger positive difference from zero indicates better detection power. As observed, the difference computed by AdaDetectGPT is consistently larger than that of Fast-DetectGPT across the first quartile, median, and third quartile. The left panel shows statistics evaluated on the SQuAD dataset, while the right panel displays results for the WritingPrompts dataset. function. Next, in Part (d), we extend our proposal to the black-box setting. Finally, in Part (e), we establish the statistical propertie
```

### Retrieved Chunk 2

- Source: `AdaDetectGPT Adaptive Detection of LLM-Generated Text with Statistical Guarantees.pdf`
- Page: `9`
- Chunk ID: `256`
- Chunk Type: `main`
- Vector Score: `unknown`
- Reranker Score: `4.36726713180542`

```text
underperforms Binoculars or RADAR. Nonetheless, AdaDetectGPT consistently improves upon Fast-DetectGPT across various datasets, with gains on Essay reaching up to 37.8%. Additionally, we evaluate AdaDetectGPT’s robustness to two adversarial attacks, paraphrasing and decoherence, in the black-box setting. As shown in Table 3, AdaDetectGPT demonstrates greater resilience than Fast-DetectGPT to adversarially perturbed texts. The improvement reaches up to 10% for paraphrasing and up to 85% for decoherence. Finally, we employ the same five LLMs from Table 1 to compare Fast-DetectGPT and AdaDetectGPT in black-box settings. Following Bao et al. (2024), we use GPT-J as the source LLM for detecting each of the remaining four target LLMs. Due to space constraints, the results are presented in Table S11 of Appendix F.5, where AdaDetectGPT uniformly outperforms Fast-DetectGPT in all cases, with impr
```

### Retrieved Chunk 3

- Source: `AdaDetectGPT Adaptive Detection of LLM-Generated Text with Statistical Guarantees.pdf`
- Page: `7`
- Chunk ID: `247`
- Chunk Type: `main`
- Vector Score: `unknown`
- Reranker Score: `2.6607179641723633`

```text
evaluate AdaDetectGPT, we compute the AUC on each of the five datasets, with its witness function bwtrained on two randomly selected datasets that differ from the test dataset. Benchmark methods.In white-box settings, we compare the proposed AdaDetectGPT againsteight state-of-the-art detectors: Likelihood, Entropy, LogRank(Gehrmann et al., 2019), LogRank Ratio (LRR, Su et al., 2023), DetectGPT(Mitchell et al., 2023) and its variants Normalized Perturbed log Rank (NPR, Su et al., 2023), Fast-DetectGPT(Bao et al., 2024), DNAGPT(Yang et al., 2024b). In black-box settings, we further compare against RoBERTaBaseand RoBERTaLarge(Solaiman et al., 2019), Binoculars(Hans et al., 2024), RADAR(Hu et al., 2023), and BiScope(Guo et al., 2024a), but omitDetectGPT,NPRandDNAGPTdue to their high computational cost. This yieldstenbaseline algorithms. We measure the detection power of each detector using A
```

### Retrieved Chunk 4

- Source: `DetectGPT-SC Improving Detection of Text Generated by Large Language Models through Self-Consistency with Masked Predictions.pdf`
- Page: `2`
- Chunk ID: `1519`
- Chunk Type: `main`
- Vector Score: `unknown`
- Reranker Score: `2.0015382766723633`

```text
of watermarks is also a challenge we need to address. However, with the emergence of ChatGPT, an innovative statistical detection method called DetectGPT [5] has been developed. Its principle is that text generated by the model typically resides in the negative curvature region of the model’s log probability. DetectGPT [ 5] generates and compares multiple variants of model-generated texts to determine whether the texts are machine-generated based on the log probabilities of the original texts and these variants. DetectGPT [5] outperforms the vast majority of existing zero-shot methods in terms of model sample detection, achieving very high AUC. It is based on this concept that DetectGPT-SC was proposed. 3 Methodology Predefined definition X is the original input text. ˆX is the sentence masked within X, which can also be referred to as "<mask>". P ( ˆX) is the mask content predicted by C
```

### Retrieved Chunk 5

- Source: `Fast-DetectGPT Efficient Zero-Shot Detection of Machine-Generated Text via Conditional Probability Curvature.pdf`
- Page: `18`
- Chunk ID: `2284`
- Chunk Type: `main`
- Vector Score: `unknown`
- Reranker Score: `1.4515247344970703`

```text
RoBERTa-based classifiers for the detection of GPT-3 generations. In contrast to DetectGPT, which employs the OpenAI API to assess perturbations, we utilize delegate models (specifically, GPT-2, Neo-2.7, and GPT-J) to identify GPT-3 generations. Fast-DetectGPT outperforms supervised RoBERTa-base, RoBERTa-large, and GPTZero classifiers, achieving higher detection accuracy across the three datasets. On average, it improves the AUROC by 0.0310 AUROC (a relative increase of 20%). Conversely, DetectGPT in the white-box setting (us- ing T5-11B/GPT-3) achieves superior detection accuracy on PubMedQA but lags behind on XSum and WritingPrompt compared to RoBERTa-large. In the black-box setting (T5-11B/Neo-2.7), De- tectGPT experiences a significant reduction in detection accuracy, averaging 0.0750 AUROC less. These findings emphasize that Fast-DetectGPT, operating in the black-box setting, offers
```

### Retrieved Chunk 6

- Source: `Fast-DetectGPT Efficient Zero-Shot Detection of Machine-Generated Text via Conditional Probability Curvature.pdf`
- Page: `18`
- Chunk ID: `2283`
- Chunk Type: `main`
- Vector Score: `unknown`
- Reranker Score: `0.5604941844940186`

```text
Fast-DetectGPT (GPT-J/Neo-2.7) 0.9396 0.9492 0.7225 0.8704* Fast-DetectGPT (GPT-J/GPT-J) 0.9329* 0.9568 0.6664 0.8520 Table 7: Detection of GPT-3 generations, evaluated in AUROC. Fast-DetectGPT in the black-box settings (using local models) significantly outperforms DetectGPT in both the black-box setting and the white-box setting (using GPT-3) on News (XSum) and story (WritingPrompts). Fast-DetectGPT uses 6B GPT-J to generate samples and models from 1.5B GPT-2 to 6B GPT-J to score samples, while DetectGPT uses 11B T5 to generate perturbations and models from 1.5B GPT-2 to 6B GPT-J, and GPT-3 service to score them.♢ – we report the official scores from Mitchell et al. (2023) instead of rerunning the experiments after confirming the consistency on RoBERTa-base/large. Table 7 presents a comparison between Fast-DetectGPT, zero-shot DetectGPT, and supervised RoBERTa-based classifiers for the
```

### Retrieved Chunk 7

- Source: `DetectGPT-SC Improving Detection of Text Generated by Large Language Models through Self-Consistency with Masked Predictions.pdf`
- Page: `2`
- Chunk ID: `1517`
- Chunk Type: `main`
- Vector Score: `unknown`
- Reranker Score: `0.44695040583610535`

```text
Running Title for Header 2 Related Work Recent research has shown promising results in the development of detection methods. The existing detectors are built on the assumption that there is a distributional difference between human-generated texts and AI-generated texts. These differences are typically identified by training classifiers or using statistical information. Classifier-based detectors. Classifier-based detectors are commonly used in natural language processing detection paradigms, especially in fake news and misinformation detection [3]. Guo et al. [4] proposed the ChatGPT Detector, where they initially constructed a dataset consisting of ChatGPT conversations with human questions and answers, and trained a text detection classifier based on this dataset. The use of these methods requires substantial data collection and incurs the cost of training these classifier models.
```

### Retrieved Chunk 8

- Source: `Fast-DetectGPT Efficient Zero-Shot Detection of Machine-Generated Text via Conditional Probability Curvature.pdf`
- Page: `7`
- Chunk ID: `2236`
- Chunk Type: `main`
- Vector Score: `unknown`
- Reranker Score: `0.2644207775592804`

```text
Detectors are expected to generalize to differ- ent domains and languages for higher usabil- ity. We compare Fast-DetectGPT against su- pervised detectors on both in-distribution and out-distribution datasets. Figure 5 reveals that Fast-DetectGPT achieves competitive detection accuracy on the in-distribution datasets XSum and WMT16-English. However, it significantly outperforms supervised detectors on the out- distribution datasets PubMedQA and WMT16- German. Moreover, it is noteworthy that Fast- DetectGPT consistently outperforms DetectGPT across all four datasets. These results underscore the robustness of Fast-DetectGPT across diverse domains and languages. Detection Method Detection Accuracy (AUROC) Figure 5: Compare with supervised detectors, evaluated in AUROC. We generate 200 test sam- ples for each dataset and source model. Robustness against Decoding Strategies. Machine systems 
```


### Manual Judgment

Please inspect the retrieved chunks and fill in:

- Which setting retrieves more useful chunks?
- Does the reranker move more relevant chunks to the top?
- Does the reranker reduce checklist / references / appendix noise?
- Does the reranker hurt source diversity for broad questions?
- Overall winner: Vector-only / Reranker / Tie

---

# Overall Notes

Use this report to decide whether the reranker is actually improving retrieval.

Common outcomes:

- If the paper-level candidate papers are wrong, improve `build_paper_catalog.py`.
- If candidate papers are right but chunks are poor, improve the reranker or chunking.
- If broad queries lose diversity, adjust `max_per_source` or retrieve more candidate papers.
- If noisy chunks remain, improve `chunk_type` labeling in `build_index.py`.
