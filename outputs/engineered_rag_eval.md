# Engineered RAG Retrieval Evaluation

This report evaluates the retrieval part of the engineered hierarchical RAG system.

The evaluation focuses on:

1. paper-level routing quality;
2. whether broad queries retrieve from multiple papers;
3. whether specific paper queries retrieve the correct paper;
4. whether noisy chunks such as checklist, references, or appendix are avoided.

---

## Broad overview of AI-generated text detection

### Question

What AI-generated text detection methods are discussed in these papers?

### Expected Behavior

- Expected retrieval behavior: `global`
- Expected source keywords: `[]`
- Expected minimum unique sources: `2`

### Actual Retrieval Summary

- Actual mode: `global`
- Number of retrieved chunks: `8`
- Number of unique sources: `3`
- Number of noisy chunks: `0`

### Checks

- Behavior check: **Pass**
- Expected source check: **Not required**
- Source diversity check: **Pass**
- Noise check: **Pass**

### Candidate Papers

1. `SeqXGPT Sentence-Level AI-Generated Text Detection.pdf`
   - Title: SeqXGPT Sentence Level AI Generated Text Detection
   - Score: `0.3216600716114044`

2. `Ghostbuster Detecting Text Ghostwritten by Large Language Models.pdf`
   - Title: Ghostbuster Detecting Text Ghostwritten by Large Language Models
   - Score: `0.34038466215133667`

3. `ASurvey of AI-generated Text Forensic Systems Detection Attribution and Characterization.pdf`
   - Title: ASurvey of AI generated Text Forensic Systems Detection Attribution and Characterization
   - Score: `0.34393998980522156`

4. `Unsupervised and Distributional Detection of Machine-Generated Text.pdf`
   - Title: Unsupervised and Distributional Detection of Machine Generated Text
   - Score: `0.3484887182712555`


### Selected Papers

1. `SeqXGPT Sentence-Level AI-Generated Text Detection.pdf`
   - Title: SeqXGPT Sentence Level AI Generated Text Detection
   - Score: `0.3216600716114044`

2. `Ghostbuster Detecting Text Ghostwritten by Large Language Models.pdf`
   - Title: Ghostbuster Detecting Text Ghostwritten by Large Language Models
   - Score: `0.34038466215133667`

3. `ASurvey of AI-generated Text Forensic Systems Detection Attribution and Characterization.pdf`
   - Title: ASurvey of AI generated Text Forensic Systems Detection Attribution and Characterization
   - Score: `0.34393998980522156`

4. `Unsupervised and Distributional Detection of Machine-Generated Text.pdf`
   - Title: Unsupervised and Distributional Detection of Machine Generated Text
   - Score: `0.3484887182712555`


### Retrieved Source Distribution

- `ASurvey of AI-generated Text Forensic Systems Detection Attribution and Characterization.pdf`: 3 chunks
- `SeqXGPT Sentence-Level AI-Generated Text Detection.pdf`: 3 chunks
- `Ghostbuster Detecting Text Ghostwritten by Large Language Models.pdf`: 2 chunks

### Retrieved Chunks

### Retrieved Chunk 1

- Source: `ASurvey of AI-generated Text Forensic Systems Detection Attribution and Characterization.pdf`
- Page: `2`
- Chunk ID: `430`
- Chunk Type: `main`

```text
LLMs. Consequently, post-hoc detection methods have gained prominence in AI-generated text foren- sics. Therefore, in the scope of our survey, we focus on post-hoc detection, further dividing it into supervised and zero-shot detection based on the training methodology employed. 2.2.2 Supervised Detectors Supervised detectors are trained using annotated datasets that consist of labeled human-written and AI-generated texts, aiming to identify distinctive features between human and AI-generated writ- ing. Initial efforts in AI-generated text detection em- ployed traditional techniques such as Bag-of-Words and TF-IDF encoding, coupled with classifiers like logistic regression, random forest, and SVC (Ip- polito et al., 2019; Jawahar et al., 2020). Subsequent research introduced advanced text s
```

### Retrieved Chunk 2

- Source: `SeqXGPT Sentence-Level AI-Generated Text Detection.pdf`
- Page: `0`
- Chunk ID: `3392`
- Chunk Type: `main`

```text
SeqXGPT: Sentence-Level AI-Generated Text Detection Pengyu Wang, Linyang Li , Ke Ren, Botian Jiang, Dong Zhang, Xipeng Qiu ∗ School of Computer Science, Fudan University Shanghai Key Laboratory of Intelligent Information Processing, Fudan University {pywang22,kren22,btjiang23,dongzhang22}@m.fudan.edu.cn {linyangli19,xpqiu}@fudan.edu.cn Abstract Widely applied large language models (LLMs) can generate human-like content, raising concerns about the abuse of LLMs. Therefore, it is important to build strong AI-generated text (AIGT) detectors. Current works only consider document-level AIGT detection, therefore, in this paper, we first introduce a sentence-level detection challenge by synthesizing a dataset that contains documents that are polished with LLMs, that is, the documents contain sent
```

### Retrieved Chunk 3

- Source: `ASurvey of AI-generated Text Forensic Systems Detection Attribution and Characterization.pdf`
- Page: `3`
- Chunk ID: `436`
- Chunk Type: `main`

```text
tectors is their limited ability to generalize to novel AI generators. Various approaches have been ex- plored to mitigate this issue, focusing on develop- ing transferable techniques for AI-generated text detection. One such avenue involves integrating Energy-Based Models (EBMs) into the detection process (Bakhtin et al., 2019). This integration ex- ploits negative samples generated by multiple auto- regressive language models; specifically, the model assigns lower energy to human-generated text com- pared to text generated by AI models. Another strategy introduced by (Kushnareva et al., 2021a) utilizes Topological Data Analysis (TDA) on at- tention maps produced by transformer models to extract domain-invariant features for AI-generated text detection. This approach involves representing
```

### Retrieved Chunk 4

- Source: `Ghostbuster Detecting Text Ghostwritten by Large Language Models.pdf`
- Page: `0`
- Chunk ID: `2380`
- Chunk Type: `main`

```text
datasets that they were not originally evaluated on (Section 6). In addition, the high false positive rates of these models raise potential ethical concerns be- cause they jeopardize students whose genuine work is misclassified as AI-generated. Furthermore, pre- vious work has indicated that text by non-native speakers of English is disproportionately flagged as AI-generated (Liang et al., 2023). These concerns underscore the need for AI-generated text detectors with strong generalization performance. We present Ghostbuster, a method for detection based on structured search and linear classification (Figure 1). First, Ghostbuster passes paired human- authored and AI-generated documents through a series of weaker language models, ranging from a unigram model to the non-instruction-tuned GPT
```

### Retrieved Chunk 5

- Source: `SeqXGPT Sentence-Level AI-Generated Text Detection.pdf`
- Page: `1`
- Chunk ID: `3398`
- Chunk Type: `main`

```text
existing methods, such as DetectGPT and Sniffer, fail to solve sentence-level AIGT detection. Our proposed SeqXGPT not only obtains promising results in both sentence and document-level AIGT detection challenges, but also exhibits excellent generalization on out-of-distribution datasets. 2 Background The proliferation of Large Language Models (LLMs) such as GPT-4 has given rise to increased concerns about the potential misuse of AI- generated texts (AIGT) (Brown et al., 2020; Zhang et al., 2022; Scao et al., 2022). This emphasizes the necessity for robust detection mechanisms to ensure security and trustworthiness of LLM applications. 2.1 Principal Approaches to AIGT Detection Broadly, AIGT detection methodologies fall into two primary categories: 1. Supervised Learning: This involves trai
```

### Retrieved Chunk 6

- Source: `ASurvey of AI-generated Text Forensic Systems Detection Attribution and Characterization.pdf`
- Page: `0`
- Chunk ID: `419`
- Chunk Type: `main`

```text
ing the challenges of LLM misuses. We present an overview of the existing efforts in AI-generated text forensics by introducing a detailed taxonomy, focusing on three pri- mary pillars: detection, attribution, and char- acterization. These pillars enable a practi- cal understanding of AI-generated text, from identifying AI-generated content (detection), determining the specific AI model involved (attribution), and grouping the underlying intents of the text (characterization). Further- more, we explore available resources for AI- generated text forensics research and discuss the evolving challenges and future directions of forensic systems in an AI era. 1 Introduction The advent of Large Language Models (LLMs) like GPT-4 (OpenAI, 2023), Gemini (Team et al., 2023), and open-source variants 
```

### Retrieved Chunk 7

- Source: `SeqXGPT Sentence-Level AI-Generated Text Detection.pdf`
- Page: `0`
- Chunk ID: `3395`
- Chunk Type: `main`

```text
can efficiently conduct sentence-level AIGT detection. given text is written or modified by an AI system (Mitchell et al., 2023; Li et al., 2023). Current AIGT detection strategies, such as supervised-learned discriminator 2, perplexity- based methods (Mitchell et al., 2023; Li et al., 2023), etc., focus on discriminating whether a whole document is generated by an AI. However, users often modify partial texts with LLMs rather than put full trust in LLMs to generate a whole document. Therefore, it is important to explore fine-grained (e.g. sentence-level) AIGT detection. Building methods that solve the sentence-level AIGT detection challenge is not an incremental modification over document-level AIGT detection. On the one hand, model-wise methods like DetectGPT and Sniffer require a rather
```

### Retrieved Chunk 8

- Source: `Ghostbuster Detecting Text Ghostwritten by Large Language Models.pdf`
- Page: `0`
- Chunk ID: `2377`
- Chunk Type: `main`

```text
Ghostbuster: Detecting Text Ghostwritten by Large Language Models Vivek Verma Eve Fleisig Nicholas Tomlin Dan Klein Computer Science Division, UC Berkeley {vivekverma, efleisig, nicholas_tomlin, klein}@berkeley.edu Abstract We introduce Ghostbuster, a state-of-the-art system for detecting AI-generated text. Our method works by passing documents through a series of weaker language models, running a structured search over possible combinations of their features, and then training a classifier on the selected features to predict whether docu- ments are AI-generated. Crucially, Ghostbuster does not require access to token probabilities from the target model, making it useful for de- tecting text generated by black-box or unknown models. In conjunction with our model, we release three new datas
```


### Manual Observation

- Are the candidate papers reasonable?
- Are the selected papers appropriate for the question?
- Are the retrieved chunks actually useful for answering the question?
- Are there checklist / references / appendix chunks?
- Overall quality: Good / Medium / Poor

---

## Specific AdaDetectGPT query

### Question

How does AdaDetectGPT work?

### Expected Behavior

- Expected retrieval behavior: `specific`
- Expected source keywords: `['AdaDetectGPT']`
- Expected minimum unique sources: `1`

### Actual Retrieval Summary

- Actual mode: `global`
- Number of retrieved chunks: `8`
- Number of unique sources: `3`
- Number of noisy chunks: `0`

### Checks

- Behavior check: **Needs inspection**
- Expected source check: **Pass**
- Source diversity check: **Pass**
- Noise check: **Pass**

### Candidate Papers

1. `AdaDetectGPT Adaptive Detection of LLM-Generated Text with Statistical Guarantees.pdf`
   - Title: AdaDetectGPT Adaptive Detection of LLM Generated Text with Statistical Guarantees
   - Score: `0.6125631332397461`

2. `DetectGPT-SC Improving Detection of Text Generated by Large Language Models through Self-Consistency with Masked Predictions.pdf`
   - Title: DetectGPT SC Improving Detection of Text Generated by Large Language Models through Self Consistency with Masked Predictions
   - Score: `0.7034844160079956`

3. `Fast-DetectGPT Efficient Zero-Shot Detection of Machine-Generated Text via Conditional Probability Curvature.pdf`
   - Title: Fast DetectGPT Efficient Zero Shot Detection of Machine Generated Text via Conditional Probability Curvature
   - Score: `0.710049569606781`

4. `GPT-who AnInformation Density-based Machine-Generated Text Detector.pdf`
   - Title: GPT who AnInformation Density based Machine Generated Text Detector
   - Score: `0.7131985425949097`


### Selected Papers

1. `AdaDetectGPT Adaptive Detection of LLM-Generated Text with Statistical Guarantees.pdf`
   - Title: AdaDetectGPT Adaptive Detection of LLM Generated Text with Statistical Guarantees
   - Score: `0.6125631332397461`

2. `DetectGPT-SC Improving Detection of Text Generated by Large Language Models through Self-Consistency with Masked Predictions.pdf`
   - Title: DetectGPT SC Improving Detection of Text Generated by Large Language Models through Self Consistency with Masked Predictions
   - Score: `0.7034844160079956`

3. `Fast-DetectGPT Efficient Zero-Shot Detection of Machine-Generated Text via Conditional Probability Curvature.pdf`
   - Title: Fast DetectGPT Efficient Zero Shot Detection of Machine Generated Text via Conditional Probability Curvature
   - Score: `0.710049569606781`

4. `GPT-who AnInformation Density-based Machine-Generated Text Detector.pdf`
   - Title: GPT who AnInformation Density based Machine Generated Text Detector
   - Score: `0.7131985425949097`


### Retrieved Source Distribution

- `AdaDetectGPT Adaptive Detection of LLM-Generated Text with Statistical Guarantees.pdf`: 3 chunks
- `DetectGPT-SC Improving Detection of Text Generated by Large Language Models through Self-Consistency with Masked Predictions.pdf`: 3 chunks
- `Fast-DetectGPT Efficient Zero-Shot Detection of Machine-Generated Text via Conditional Probability Curvature.pdf`: 2 chunks

### Retrieved Chunks

### Retrieved Chunk 1

- Source: `AdaDetectGPT Adaptive Detection of LLM-Generated Text with Statistical Guarantees.pdf`
- Page: `1`
- Chunk ID: `213`
- Chunk Type: `main`

```text
Figure 1: Workflow of AdaDetectGPT. Built upon Fast-DetectGPT (Bao et al., 2024), our method adaptively learn a witness functionbwfrom training data by maximizing a lower bound on the TNR, while using normal approximation for FNR control. probability outputs (i.e., logits) from a source LLM to construct the statistics for classification (see e.g., Gehrmann et al., 2019; Mitchell et al., 2023). These works are motivated by the empirical observation that LLM-generated text tends to exhibit higher log-probabilities or larger differences between the logits of original and perturbed tokens. However, as we demonstrated in Section 3, relying solely on the logits can be sub-optimal for detecting LLM-generated text. Our contribution. In this paper, we propose AdaDetectGPT (see Figure 1 for a visual
```

### Retrieved Chunk 2

- Source: `AdaDetectGPT Adaptive Detection of LLM-Generated Text with Statistical Guarantees.pdf`
- Page: `41`
- Chunk ID: `368`
- Chunk Type: `main`

```text
G Broader impact and limitation AdaDetectGPT is a computationally and statistically efficient detector for machine-generated text, thus safeguarding AI systems against fake news, disinformation, and academic plagiarism. Despite AdaDetectGPT’s strong empirical performance in the black-box setting, its theoretical guarantees are mainly established in the white-box setting. Even when restricting to the white-box setting, LLM text generation often involves sampling parameters (e.g., temperature and top_k). Using different parameter values can cause the sampling distribution to deviate from that of the target model we aim to detect. This mismatch invalidates MCLT in practice. Fortunately, we observe that the shape of our statistic remains similar, but shifts toward a positive mean (see Figure S
```

### Retrieved Chunk 3

- Source: `AdaDetectGPT Adaptive Detection of LLM-Generated Text with Statistical Guarantees.pdf`
- Page: `9`
- Chunk ID: `256`
- Chunk Type: `main`

```text
underperforms Binoculars or RADAR. Nonetheless, AdaDetectGPT consistently improves upon Fast-DetectGPT across various datasets, with gains on Essay reaching up to 37.8%. Additionally, we evaluate AdaDetectGPT’s robustness to two adversarial attacks, paraphrasing and decoherence, in the black-box setting. As shown in Table 3, AdaDetectGPT demonstrates greater resilience than Fast-DetectGPT to adversarially perturbed texts. The improvement reaches up to 10% for paraphrasing and up to 85% for decoherence. Finally, we employ the same five LLMs from Table 1 to compare Fast-DetectGPT and AdaDetectGPT in black-box settings. Following Bao et al. (2024), we use GPT-J as the source LLM for detecting each of the remaining four target LLMs. Due to space constraints, the results are presented in Table 
```

### Retrieved Chunk 4

- Source: `Fast-DetectGPT Efficient Zero-Shot Detection of Machine-Generated Text via Conditional Probability Curvature.pdf`
- Page: `21`
- Chunk ID: `2297`
- Chunk Type: `main`

```text
Published as a conference paper at ICLR 2024 used in Table 2, sampling with the three strategies with k = 40 , p = 0 .96, and T = 0 .8. Fast- DetectGPT in the white-box setting obtains the best accuracy on the three sampling strategies, out- performing DetectGPT by relative 95% on Top- p sampling, relative 81% on Top- k sampling, and relative 99% on sampling with a temperature, as shown in Table 9. In the black-box setting, Fast- DetectGPT outperforms DetectGPT by relatively 92%, 80%, and 98% on the three decoding strate- gies, respectively. These results demonstrate that Fast-DetectGPT works consistently in detecting texts produced by different decoding strategies. To elucidate the trajectory of detection accuracy concerning variations in sampling hyper- parameters, we conducted additiona
```

### Retrieved Chunk 5

- Source: `DetectGPT-SC Improving Detection of Text Generated by Large Language Models through Self-Consistency with Masked Predictions.pdf`
- Page: `2`
- Chunk ID: `1519`
- Chunk Type: `main`

```text
of watermarks is also a challenge we need to address. However, with the emergence of ChatGPT, an innovative statistical detection method called DetectGPT [5] has been developed. Its principle is that text generated by the model typically resides in the negative curvature region of the model’s log probability. DetectGPT [ 5] generates and compares multiple variants of model-generated texts to determine whether the texts are machine-generated based on the log probabilities of the original texts and these variants. DetectGPT [5] outperforms the vast majority of existing zero-shot methods in terms of model sample detection, achieving very high AUC. It is based on this concept that DetectGPT-SC was proposed. 3 Methodology Predefined definition X is the original input text. ˆX is the sentence ma
```

### Retrieved Chunk 6

- Source: `DetectGPT-SC Improving Detection of Text Generated by Large Language Models through Self-Consistency with Masked Predictions.pdf`
- Page: `0`
- Chunk ID: `1510`
- Chunk Type: `main`

```text
self-consistency in text generation and continuation. Self-consistency capitalizes on the intuition that AI-generated texts can still be reasoned with by large language models using the same logical reasoning when portions of the texts are masked, which differs from human-generated texts. Using this observation, we subsequently proposed a new method for AI-generated texts detection based on self-consistency with masked predictions to determine whether a text is generated by LLMs. This method, which we call DetectGPT-SC. We conducted a series of experiments to evaluate the performance of DetectGPT-SC. In these experiments, we employed various mask scheme, zero-shot, and simple prompt for completing masked texts and self-consistency predictions. The results indicate that DetectGPT-SC outperf
```

### Retrieved Chunk 7

- Source: `DetectGPT-SC Improving Detection of Text Generated by Large Language Models through Self-Consistency with Masked Predictions.pdf`
- Page: `2`
- Chunk ID: `1520`
- Chunk Type: `main`

```text
"<mask>". P ( ˆX) is the mask content predicted by ChatGPT. DetectGPT-SC is based on the hypothesis that AI-generated texts can still undergo reasoning by large language models using the same logical reasoning process even when certain portions of the texts are masked, which distinguishes it from texts generated by humans. DetectGPT-SC is shown in Figure 1, by masking the input text X multiple times, we obtain ˆX1, ˆX2, and ˆX3, which represent the masked content in X. Simultaneously, we replace the corresponding positions in the input text X with the "<mask>" token. Then, we utilize ChatGPT to generate completions for the masked ˆX1, ˆX2, and ˆX3, resulting in new inferred results: P ( ˆX1), P ( ˆX2), and P ( ˆX3). Next, we employ cosine similarity and Word2Vec to compute the similarity b
```

### Retrieved Chunk 8

- Source: `Fast-DetectGPT Efficient Zero-Shot Detection of Machine-Generated Text via Conditional Probability Curvature.pdf`
- Page: `5`
- Chunk ID: `2227`
- Chunk Type: `main`

```text
experiments, measuring the detection accuracy in AUROC (see Appendix A). Inference Speedup. We compare the inference time (excluding the time for initializing the model) of Fast-DetectGPT and DetectGPT on a Tesla A100 GPU using XSum generations from the five models in Table 2. Despite DetectGPT’s use of GPU batch processing, splitting 100 perturbations into 10 batches, it still requires substantial computational resources. It totals 79,113 seconds (ap- proximately 22 hours) over five runs. In contrast, Fast-DetectGPT completes the task in only 233 seconds (about 4 minutes), achieving a remarkable speedup factor of approximately 340x, highlight- ing its significant performance improvement. White-Box Zero-Shot Machine-Generated Text Detection. We evaluate zero-shot methods us- ing each sourc
```


### Manual Observation

- Are the candidate papers reasonable?
- Are the selected papers appropriate for the question?
- Are the retrieved chunks actually useful for answering the question?
- Are there checklist / references / appendix chunks?
- Overall quality: Good / Medium / Poor

---

## Specific DetectGPT query

### Question

How does DetectGPT detect machine-generated text?

### Expected Behavior

- Expected retrieval behavior: `specific`
- Expected source keywords: `['DetectGPT']`
- Expected minimum unique sources: `1`

### Actual Retrieval Summary

- Actual mode: `global`
- Number of retrieved chunks: `8`
- Number of unique sources: `4`
- Number of noisy chunks: `0`

### Checks

- Behavior check: **Needs inspection**
- Expected source check: **Pass**
- Source diversity check: **Pass**
- Noise check: **Pass**

### Candidate Papers

1. `DetectGPT-SC Improving Detection of Text Generated by Large Language Models through Self-Consistency with Masked Predictions.pdf`
   - Title: DetectGPT SC Improving Detection of Text Generated by Large Language Models through Self Consistency with Masked Predictions
   - Score: `0.4306338429450989`

2. `Fast-DetectGPT Efficient Zero-Shot Detection of Machine-Generated Text via Conditional Probability Curvature.pdf`
   - Title: Fast DetectGPT Efficient Zero Shot Detection of Machine Generated Text via Conditional Probability Curvature
   - Score: `0.467221736907959`

3. `DetectLLM Leveraging Log Rank Information for Zero-Shot Detection of Machine-Generated Text.pdf`
   - Title: DetectLLM Leveraging Log Rank Information for Zero Shot Detection of Machine Generated Text
   - Score: `0.49767881631851196`

4. `DetectLLM Leveraging Log-Rank Information for Zero-Shot Detection of Machine-Generated Text.pdf`
   - Title: DetectLLM Leveraging Log Rank Information for Zero Shot Detection of Machine Generated Text
   - Score: `0.4983159601688385`


### Selected Papers

1. `DetectGPT-SC Improving Detection of Text Generated by Large Language Models through Self-Consistency with Masked Predictions.pdf`
   - Title: DetectGPT SC Improving Detection of Text Generated by Large Language Models through Self Consistency with Masked Predictions
   - Score: `0.4306338429450989`

2. `Fast-DetectGPT Efficient Zero-Shot Detection of Machine-Generated Text via Conditional Probability Curvature.pdf`
   - Title: Fast DetectGPT Efficient Zero Shot Detection of Machine Generated Text via Conditional Probability Curvature
   - Score: `0.467221736907959`

3. `DetectLLM Leveraging Log Rank Information for Zero-Shot Detection of Machine-Generated Text.pdf`
   - Title: DetectLLM Leveraging Log Rank Information for Zero Shot Detection of Machine Generated Text
   - Score: `0.49767881631851196`

4. `DetectLLM Leveraging Log-Rank Information for Zero-Shot Detection of Machine-Generated Text.pdf`
   - Title: DetectLLM Leveraging Log Rank Information for Zero Shot Detection of Machine Generated Text
   - Score: `0.4983159601688385`


### Retrieved Source Distribution

- `DetectLLM Leveraging Log Rank Information for Zero-Shot Detection of Machine-Generated Text.pdf`: 2 chunks
- `DetectLLM Leveraging Log-Rank Information for Zero-Shot Detection of Machine-Generated Text.pdf`: 2 chunks
- `Fast-DetectGPT Efficient Zero-Shot Detection of Machine-Generated Text via Conditional Probability Curvature.pdf`: 2 chunks
- `DetectGPT-SC Improving Detection of Text Generated by Large Language Models through Self-Consistency with Masked Predictions.pdf`: 2 chunks

### Retrieved Chunks

### Retrieved Chunk 1

- Source: `DetectLLM Leveraging Log Rank Information for Zero-Shot Detection of Machine-Generated Text.pdf`
- Page: `2`
- Chunk ID: `1771`
- Chunk Type: `main`

```text
1020 50 100 #(Perturbations) 88 90 92performance(%) XSum 1020 50 100 #(Perturbations) 82 84 86 SQuAD 1020 50 100 #(Perturbations) 92 94 96 WritingP DetectGPT NPR(ours) Figure 2: Comparison of DetectGPT to NPR averaged across six models (in terms of AUROC). (The full results are given in Figure 6 in the Appendix). methods for detecting machine-generated text by evaluating the per-token log probability of texts and using thresholding. Mitchell et al. (2023) observed that machine-generated texts tend to lie in the local curvature of the log probability and proposed De- tectGPT, whose prominent performance can only be guaranteed by the large size of the perturbation function and by a large number of perturbations, and thus costs more computational resources. Other work explored watermarking, w
```

### Retrieved Chunk 2

- Source: `DetectLLM Leveraging Log-Rank Information for Zero-Shot Detection of Machine-Generated Text.pdf`
- Page: `2`
- Chunk ID: `1853`
- Chunk Type: `main`

```text
1020 50 100 #(Perturbations) 88 90 92performance(%) XSum 1020 50 100 #(Perturbations) 82 84 86 SQuAD 1020 50 100 #(Perturbations) 92 94 96 WritingP DetectGPT NPR(ours) Figure 2: Comparison of DetectGPT to NPR averaged across six models (in terms of AUROC). (The full results are given in Figure 6 in the Appendix). methods for detecting machine-generated text by evaluating the per-token log probability of texts and using thresholding. Mitchell et al. (2023) observed that machine-generated texts tend to lie in the local curvature of the log probability and proposed De- tectGPT, whose prominent performance can only be guaranteed by the large size of the perturbation function and by a large number of perturbations, and thus costs more computational resources. Other work explored watermarking, w
```

### Retrieved Chunk 3

- Source: `Fast-DetectGPT Efficient Zero-Shot Detection of Machine-Generated Text via Conditional Probability Curvature.pdf`
- Page: `4`
- Chunk ID: `2219`
- Chunk Type: `main`

```text
Published as a conference paper at ICLR 2024 Algorithm 1 Fast-DetectGPT machine-generated text detection. Input: passage x, sampling model qφ, scoring model pθ, and decision threshold ϵ Output: True – probably machine-generated, False – probably human-written. 1: function FAST DETECT GPT( x, qφ, pθ) 2: ˜xi ∼ qφ(˜x|x), i ∈ [1..N ] ▷ Conditional sampling 3: ˜µ ← 1 N P i log pθ(˜xi|x) ▷ Estimate the mean 4: ˜σ2 ← 1 N −1 P i(log pθ(˜xi|x) − ˜µ)2 ▷ Estimate the variance 5: ˆdx ← (log pθ(x) − ˜µ)/˜σ ▷ Estimate conditional probability curvature 6: return ˆdx > ϵ torch.distributions.categorical.Categorical(logits=lprobs).sample([10000]), where the lprobs is the log probability distribution of qφ(˜xj|x<j) for j from 0 to the length of x. The sampling process plays a pivotal role in guiding us towar
```

### Retrieved Chunk 4

- Source: `DetectLLM Leveraging Log Rank Information for Zero-Shot Detection of Machine-Generated Text.pdf`
- Page: `0`
- Chunk ID: `1761`
- Chunk Type: `main`

```text
to detect machine-generated text, preventing malicious use such as plagiarism, misinforma- tion, and propaganda. In this paper, we intro- duce two novel zero-shot methods for detecting machine-generated text by leveraging the Log- Rank information. One is called DetectLLM- LRR, which is fast and efficient, and the other is called DetectLLM-NPR, which is more ac- curate, but slower due to the need for perturba- tions. Our experiments on three datasets and seven language models show that our proposed methods improve over the state of the art by 3.9 and 1.75 AUROC points absolute. More- over, DetectLLM-NPR needs fewer perturba- tions than previous work to achieve the same level of performance, which makes it more practical for real-world use. We also investi- gate the efficiency-performance t
```

### Retrieved Chunk 5

- Source: `DetectLLM Leveraging Log-Rank Information for Zero-Shot Detection of Machine-Generated Text.pdf`
- Page: `0`
- Chunk ID: `1843`
- Chunk Type: `main`

```text
to detect machine-generated text, preventing malicious use such as plagiarism, misinforma- tion, and propaganda. In this paper, we intro- duce two novel zero-shot methods for detecting machine-generated text by leveraging the Log- Rank information. One is called DetectLLM- LRR, which is fast and efficient, and the other is called DetectLLM-NPR, which is more ac- curate, but slower due to the need for perturba- tions. Our experiments on three datasets and seven language models show that our proposed methods improve over the state of the art by 3.9 and 1.75 AUROC points absolute. More- over, DetectLLM-NPR needs fewer perturba- tions than previous work to achieve the same level of performance, which makes it more practical for real-world use. We also investi- gate the efficiency-performance t
```

### Retrieved Chunk 6

- Source: `DetectGPT-SC Improving Detection of Text Generated by Large Language Models through Self-Consistency with Masked Predictions.pdf`
- Page: `2`
- Chunk ID: `1519`
- Chunk Type: `main`

```text
of watermarks is also a challenge we need to address. However, with the emergence of ChatGPT, an innovative statistical detection method called DetectGPT [5] has been developed. Its principle is that text generated by the model typically resides in the negative curvature region of the model’s log probability. DetectGPT [ 5] generates and compares multiple variants of model-generated texts to determine whether the texts are machine-generated based on the log probabilities of the original texts and these variants. DetectGPT [5] outperforms the vast majority of existing zero-shot methods in terms of model sample detection, achieving very high AUC. It is based on this concept that DetectGPT-SC was proposed. 3 Methodology Predefined definition X is the original input text. ˆX is the sentence ma
```

### Retrieved Chunk 7

- Source: `Fast-DetectGPT Efficient Zero-Shot Detection of Machine-Generated Text via Conditional Probability Curvature.pdf`
- Page: `1`
- Chunk ID: `2207`
- Chunk Type: `main`

```text
supervised classifiers on detection accuracy. This stems from their need for “universal features” that can function across multiple domains and languages (Gehrmann et al., 2019; Mitchell et al., 2023). A typical zero-shot classifier, DetectGPT (Mitchell et al., 2023), works under the assumption that machine-generated text variations typically have lower model probability than the original, while human-written ones could go either way. Despite its effectiveness, employing probability curvature demands the execution of around one hundred model calls or interactions with services such as the OpenAI API to create the perturbation texts, leading to prohibitive computational costs. In this paper, we posit a new hypothesis for detecting machine-generated text. By viewing text generation as a sequ
```

### Retrieved Chunk 8

- Source: `DetectGPT-SC Improving Detection of Text Generated by Large Language Models through Self-Consistency with Masked Predictions.pdf`
- Page: `2`
- Chunk ID: `1520`
- Chunk Type: `main`

```text
"<mask>". P ( ˆX) is the mask content predicted by ChatGPT. DetectGPT-SC is based on the hypothesis that AI-generated texts can still undergo reasoning by large language models using the same logical reasoning process even when certain portions of the texts are masked, which distinguishes it from texts generated by humans. DetectGPT-SC is shown in Figure 1, by masking the input text X multiple times, we obtain ˆX1, ˆX2, and ˆX3, which represent the masked content in X. Simultaneously, we replace the corresponding positions in the input text X with the "<mask>" token. Then, we utilize ChatGPT to generate completions for the masked ˆX1, ˆX2, and ˆX3, resulting in new inferred results: P ( ˆX1), P ( ˆX2), and P ( ˆX3). Next, we employ cosine similarity and Word2Vec to compute the similarity b
```


### Manual Observation

- Are the candidate papers reasonable?
- Are the selected papers appropriate for the question?
- Are the retrieved chunks actually useful for answering the question?
- Are there checklist / references / appendix chunks?
- Overall quality: Good / Medium / Poor

---

## Statistical guarantee query

### Question

Which methods provide statistical guarantees for AI-generated text detection?

### Expected Behavior

- Expected retrieval behavior: `global_or_specific`
- Expected source keywords: `[]`
- Expected minimum unique sources: `1`

### Actual Retrieval Summary

- Actual mode: `global`
- Number of retrieved chunks: `8`
- Number of unique sources: `3`
- Number of noisy chunks: `0`

### Checks

- Behavior check: **Pass**
- Expected source check: **Not required**
- Source diversity check: **Pass**
- Noise check: **Pass**

### Candidate Papers

1. `SeqXGPT Sentence-Level AI-Generated Text Detection.pdf`
   - Title: SeqXGPT Sentence Level AI Generated Text Detection
   - Score: `0.35137027502059937`

2. `Intrinsic Dimension Estimation for Robust Detection of AI-Generated Texts.pdf`
   - Title: Intrinsic Dimension Estimation for Robust Detection of AI Generated Texts
   - Score: `0.35572031140327454`

3. `DetectGPT-SC Improving Detection of Text Generated by Large Language Models through Self-Consistency with Masked Predictions.pdf`
   - Title: DetectGPT SC Improving Detection of Text Generated by Large Language Models through Self Consistency with Masked Predictions
   - Score: `0.35857266187667847`

4. `Unsupervised and Distributional Detection of Machine-Generated Text.pdf`
   - Title: Unsupervised and Distributional Detection of Machine Generated Text
   - Score: `0.3624788224697113`


### Selected Papers

1. `SeqXGPT Sentence-Level AI-Generated Text Detection.pdf`
   - Title: SeqXGPT Sentence Level AI Generated Text Detection
   - Score: `0.35137027502059937`

2. `Intrinsic Dimension Estimation for Robust Detection of AI-Generated Texts.pdf`
   - Title: Intrinsic Dimension Estimation for Robust Detection of AI Generated Texts
   - Score: `0.35572031140327454`

3. `DetectGPT-SC Improving Detection of Text Generated by Large Language Models through Self-Consistency with Masked Predictions.pdf`
   - Title: DetectGPT SC Improving Detection of Text Generated by Large Language Models through Self Consistency with Masked Predictions
   - Score: `0.35857266187667847`

4. `Unsupervised and Distributional Detection of Machine-Generated Text.pdf`
   - Title: Unsupervised and Distributional Detection of Machine Generated Text
   - Score: `0.3624788224697113`


### Retrieved Source Distribution

- `SeqXGPT Sentence-Level AI-Generated Text Detection.pdf`: 3 chunks
- `DetectGPT-SC Improving Detection of Text Generated by Large Language Models through Self-Consistency with Masked Predictions.pdf`: 3 chunks
- `Intrinsic Dimension Estimation for Robust Detection of AI-Generated Texts.pdf`: 2 chunks

### Retrieved Chunks

### Retrieved Chunk 1

- Source: `SeqXGPT Sentence-Level AI-Generated Text Detection.pdf`
- Page: `1`
- Chunk ID: `3398`
- Chunk Type: `main`

```text
existing methods, such as DetectGPT and Sniffer, fail to solve sentence-level AIGT detection. Our proposed SeqXGPT not only obtains promising results in both sentence and document-level AIGT detection challenges, but also exhibits excellent generalization on out-of-distribution datasets. 2 Background The proliferation of Large Language Models (LLMs) such as GPT-4 has given rise to increased concerns about the potential misuse of AI- generated texts (AIGT) (Brown et al., 2020; Zhang et al., 2022; Scao et al., 2022). This emphasizes the necessity for robust detection mechanisms to ensure security and trustworthiness of LLM applications. 2.1 Principal Approaches to AIGT Detection Broadly, AIGT detection methodologies fall into two primary categories: 1. Supervised Learning: This involves trai
```

### Retrieved Chunk 2

- Source: `DetectGPT-SC Improving Detection of Text Generated by Large Language Models through Self-Consistency with Masked Predictions.pdf`
- Page: `0`
- Chunk ID: `1509`
- Chunk Type: `main`

```text
DETECT GPT-SC: I MPROVING DETECTION OF TEXT GENERATED BY LARGE LANGUAGE MODELS THROUGH SELF -C ONSISTENCY WITH MASKED PREDICTIONS Rongsheng Wang Macao Polytechnic University p2213046@mpu.edu.mo Qi Li Iowa State University qli@iastate.edu Sihong Xie∗ HKUST (GZ) sihongxie@hkust-gz.edu.cn ABSTRACT General large language models (LLMs) such as ChatGPT have shown remarkable success, but it has also raised concerns among people about the misuse of AI-generated texts. Therefore, an important question is how to detect whether the texts are generated by ChatGPT or by humans. Existing detectors are built on the assumption that there is a distribution gap between human-generated and AI-generated texts. These gaps are typically identified using statistical information or classifiers. In contrast to pri
```

### Retrieved Chunk 3

- Source: `Intrinsic Dimension Estimation for Robust Detection of AI-Generated Texts.pdf`
- Page: `6`
- Chunk ID: `2576`
- Chunk Type: `main`

```text
estimation, so we use this model for all further experiments in English, and XLM-R of the same size for multilingual experiments. Artificial text detection. We show that intrinsic dimension can lead to a robust method of artificial text detection. In all experiments below, we use the one-feature thresholding classifier (see Section 4). Comparison with universal detectors. First, we show that our detector is the best among general- purpose methods designed to detect texts of any domain, generated by any AI model, without access to the generator itself. Such methods are needed, e.g., for plagiarism detection. To be applicable in real life, the algorithm should provide high artificial text detection rate while avoiding false accusations of real authors. Besides, it should be resistant to adve
```

### Retrieved Chunk 4

- Source: `SeqXGPT Sentence-Level AI-Generated Text Detection.pdf`
- Page: `1`
- Chunk ID: `3400`
- Chunk Type: `main`

```text
a perturbation-based method leveraging average per-token log probabilities. The recent work of Li et al. (2023) extends this further by studying multi-model detection through text perplexities, aiming to trace the precise LLM origin of texts. 2.2 Detection Task Formulations The AIGT detection tasks can be formulated in different setups: 1. Particular-Model Binary AIGT Detection: In this setup, the objective is to discriminate whether a text was produced by a specific known AI model or by a human. Both GPTZero and DetectGPT fall into this category. 2. Mixed-Model Binary AIGT Detection: Here, the detectors are designed to identify AI-generated content without the need to pinpoint the exact model of origin. 3https://gptzero.me/
```

### Retrieved Chunk 5

- Source: `DetectGPT-SC Improving Detection of Text Generated by Large Language Models through Self-Consistency with Masked Predictions.pdf`
- Page: `0`
- Chunk ID: `1510`
- Chunk Type: `main`

```text
self-consistency in text generation and continuation. Self-consistency capitalizes on the intuition that AI-generated texts can still be reasoned with by large language models using the same logical reasoning when portions of the texts are masked, which differs from human-generated texts. Using this observation, we subsequently proposed a new method for AI-generated texts detection based on self-consistency with masked predictions to determine whether a text is generated by LLMs. This method, which we call DetectGPT-SC. We conducted a series of experiments to evaluate the performance of DetectGPT-SC. In these experiments, we employed various mask scheme, zero-shot, and simple prompt for completing masked texts and self-consistency predictions. The results indicate that DetectGPT-SC outperf
```

### Retrieved Chunk 6

- Source: `SeqXGPT Sentence-Level AI-Generated Text Detection.pdf`
- Page: `0`
- Chunk ID: `3395`
- Chunk Type: `main`

```text
can efficiently conduct sentence-level AIGT detection. given text is written or modified by an AI system (Mitchell et al., 2023; Li et al., 2023). Current AIGT detection strategies, such as supervised-learned discriminator 2, perplexity- based methods (Mitchell et al., 2023; Li et al., 2023), etc., focus on discriminating whether a whole document is generated by an AI. However, users often modify partial texts with LLMs rather than put full trust in LLMs to generate a whole document. Therefore, it is important to explore fine-grained (e.g. sentence-level) AIGT detection. Building methods that solve the sentence-level AIGT detection challenge is not an incremental modification over document-level AIGT detection. On the one hand, model-wise methods like DetectGPT and Sniffer require a rather
```

### Retrieved Chunk 7

- Source: `DetectGPT-SC Improving Detection of Text Generated by Large Language Models through Self-Consistency with Masked Predictions.pdf`
- Page: `2`
- Chunk ID: `1517`
- Chunk Type: `main`

```text
Running Title for Header 2 Related Work Recent research has shown promising results in the development of detection methods. The existing detectors are built on the assumption that there is a distributional difference between human-generated texts and AI-generated texts. These differences are typically identified by training classifiers or using statistical information. Classifier-based detectors. Classifier-based detectors are commonly used in natural language processing detection paradigms, especially in fake news and misinformation detection [3]. Guo et al. [4] proposed the ChatGPT Detector, where they initially constructed a dataset consisting of ChatGPT conversations with human questions and answers, and trained a text detection classifier based on this dataset. The use of these metho
```

### Retrieved Chunk 8

- Source: `Intrinsic Dimension Estimation for Robust Detection of AI-Generated Texts.pdf`
- Page: `0`
- Chunk ID: `2544`
- Chunk Type: `main`

```text
proficiency of human writers, can be easily calculated for any language, and can robustly separate natural and AI-generated texts regardless of the generation model and sampling method. In this work, we propose such an invariant for human- written texts, namely the intrinsic dimensionality of the manifold underlying the set of embeddings for a given text sample. We show that the average intrinsic dimensionality of fluent texts in a natural language is hovering around the value 9 for several alphabet-based languages and around 7 for Chinese, while the average intrinsic dimensionality of AI-generated texts for each language is ≈ 1.5 lower, with a clear statistical separation between human-generated and AI-generated distri- butions. This property allows us to build a score-based artificial te
```


### Manual Observation

- Are the candidate papers reasonable?
- Are the selected papers appropriate for the question?
- Are the retrieved chunks actually useful for answering the question?
- Are there checklist / references / appendix chunks?
- Overall quality: Good / Medium / Poor

---

## Comparison between DetectGPT and AdaDetectGPT

### Question

What is the difference between DetectGPT and AdaDetectGPT?

### Expected Behavior

- Expected retrieval behavior: `global`
- Expected source keywords: `['DetectGPT', 'AdaDetectGPT']`
- Expected minimum unique sources: `2`

### Actual Retrieval Summary

- Actual mode: `global`
- Number of retrieved chunks: `8`
- Number of unique sources: `3`
- Number of noisy chunks: `0`

### Checks

- Behavior check: **Pass**
- Expected source check: **Pass**
- Source diversity check: **Pass**
- Noise check: **Pass**

### Candidate Papers

1. `AdaDetectGPT Adaptive Detection of LLM-Generated Text with Statistical Guarantees.pdf`
   - Title: AdaDetectGPT Adaptive Detection of LLM Generated Text with Statistical Guarantees
   - Score: `0.6420181393623352`

2. `Fast-DetectGPT Efficient Zero-Shot Detection of Machine-Generated Text via Conditional Probability Curvature.pdf`
   - Title: Fast DetectGPT Efficient Zero Shot Detection of Machine Generated Text via Conditional Probability Curvature
   - Score: `0.6681676506996155`

3. `DetectGPT-SC Improving Detection of Text Generated by Large Language Models through Self-Consistency with Masked Predictions.pdf`
   - Title: DetectGPT SC Improving Detection of Text Generated by Large Language Models through Self Consistency with Masked Predictions
   - Score: `0.6825336217880249`

4. `GPT-who AnInformation Density-based Machine-Generated Text Detector.pdf`
   - Title: GPT who AnInformation Density based Machine Generated Text Detector
   - Score: `0.6846862435340881`


### Selected Papers

1. `AdaDetectGPT Adaptive Detection of LLM-Generated Text with Statistical Guarantees.pdf`
   - Title: AdaDetectGPT Adaptive Detection of LLM Generated Text with Statistical Guarantees
   - Score: `0.6420181393623352`

2. `Fast-DetectGPT Efficient Zero-Shot Detection of Machine-Generated Text via Conditional Probability Curvature.pdf`
   - Title: Fast DetectGPT Efficient Zero Shot Detection of Machine Generated Text via Conditional Probability Curvature
   - Score: `0.6681676506996155`

3. `DetectGPT-SC Improving Detection of Text Generated by Large Language Models through Self-Consistency with Masked Predictions.pdf`
   - Title: DetectGPT SC Improving Detection of Text Generated by Large Language Models through Self Consistency with Masked Predictions
   - Score: `0.6825336217880249`

4. `GPT-who AnInformation Density-based Machine-Generated Text Detector.pdf`
   - Title: GPT who AnInformation Density based Machine Generated Text Detector
   - Score: `0.6846862435340881`


### Retrieved Source Distribution

- `AdaDetectGPT Adaptive Detection of LLM-Generated Text with Statistical Guarantees.pdf`: 3 chunks
- `Fast-DetectGPT Efficient Zero-Shot Detection of Machine-Generated Text via Conditional Probability Curvature.pdf`: 3 chunks
- `DetectGPT-SC Improving Detection of Text Generated by Large Language Models through Self-Consistency with Masked Predictions.pdf`: 2 chunks

### Retrieved Chunks

### Retrieved Chunk 1

- Source: `AdaDetectGPT Adaptive Detection of LLM-Generated Text with Statistical Guarantees.pdf`
- Page: `4`
- Chunk ID: `229`
- Chunk Type: `main`

```text
0 1 2 3 Differences in statistical measures 0 1 FastDetectGPT AdaDetectGPT Dataset: SQuAD 1  0 1 2 3 4 Differences in statistical measures 0 1 FastDetectGPT AdaDetectGPT Dataset: Writing Figure 2: Boxplots visualizing the differences in the statistical measures between human- and LLM- authored passages, comparing AdaDetectGPT (with a learned witness function) and Fast-DetectGPT (without it). A larger positive difference from zero indicates better detection power. As observed, the difference computed by AdaDetectGPT is consistently larger than that of Fast-DetectGPT across the first quartile, median, and third quartile. The left panel shows statistics evaluated on the SQuAD dataset, while the right panel displays results for the WritingPrompts dataset. function. Next, in Part (d), we extend
```

### Retrieved Chunk 2

- Source: `AdaDetectGPT Adaptive Detection of LLM-Generated Text with Statistical Guarantees.pdf`
- Page: `9`
- Chunk ID: `256`
- Chunk Type: `main`

```text
underperforms Binoculars or RADAR. Nonetheless, AdaDetectGPT consistently improves upon Fast-DetectGPT across various datasets, with gains on Essay reaching up to 37.8%. Additionally, we evaluate AdaDetectGPT’s robustness to two adversarial attacks, paraphrasing and decoherence, in the black-box setting. As shown in Table 3, AdaDetectGPT demonstrates greater resilience than Fast-DetectGPT to adversarially perturbed texts. The improvement reaches up to 10% for paraphrasing and up to 85% for decoherence. Finally, we employ the same five LLMs from Table 1 to compare Fast-DetectGPT and AdaDetectGPT in black-box settings. Following Bao et al. (2024), we use GPT-J as the source LLM for detecting each of the remaining four target LLMs. Due to space constraints, the results are presented in Table 
```

### Retrieved Chunk 3

- Source: `AdaDetectGPT Adaptive Detection of LLM-Generated Text with Statistical Guarantees.pdf`
- Page: `7`
- Chunk ID: `247`
- Chunk Type: `main`

```text
evaluate AdaDetectGPT, we compute the AUC on each of the five datasets, with its witness function bwtrained on two randomly selected datasets that differ from the test dataset. Benchmark methods.In white-box settings, we compare the proposed AdaDetectGPT againsteight state-of-the-art detectors: Likelihood, Entropy, LogRank(Gehrmann et al., 2019), LogRank Ratio (LRR, Su et al., 2023), DetectGPT(Mitchell et al., 2023) and its variants Normalized Perturbed log Rank (NPR, Su et al., 2023), Fast-DetectGPT(Bao et al., 2024), DNAGPT(Yang et al., 2024b). In black-box settings, we further compare against RoBERTaBaseand RoBERTaLarge(Solaiman et al., 2019), Binoculars(Hans et al., 2024), RADAR(Hu et al., 2023), and BiScope(Guo et al., 2024a), but omitDetectGPT,NPRandDNAGPTdue to their high computatio
```

### Retrieved Chunk 4

- Source: `DetectGPT-SC Improving Detection of Text Generated by Large Language Models through Self-Consistency with Masked Predictions.pdf`
- Page: `2`
- Chunk ID: `1519`
- Chunk Type: `main`

```text
of watermarks is also a challenge we need to address. However, with the emergence of ChatGPT, an innovative statistical detection method called DetectGPT [5] has been developed. Its principle is that text generated by the model typically resides in the negative curvature region of the model’s log probability. DetectGPT [ 5] generates and compares multiple variants of model-generated texts to determine whether the texts are machine-generated based on the log probabilities of the original texts and these variants. DetectGPT [5] outperforms the vast majority of existing zero-shot methods in terms of model sample detection, achieving very high AUC. It is based on this concept that DetectGPT-SC was proposed. 3 Methodology Predefined definition X is the original input text. ˆX is the sentence ma
```

### Retrieved Chunk 5

- Source: `Fast-DetectGPT Efficient Zero-Shot Detection of Machine-Generated Text via Conditional Probability Curvature.pdf`
- Page: `18`
- Chunk ID: `2284`
- Chunk Type: `main`

```text
RoBERTa-based classifiers for the detection of GPT-3 generations. In contrast to DetectGPT, which employs the OpenAI API to assess perturbations, we utilize delegate models (specifically, GPT-2, Neo-2.7, and GPT-J) to identify GPT-3 generations. Fast-DetectGPT outperforms supervised RoBERTa-base, RoBERTa-large, and GPTZero classifiers, achieving higher detection accuracy across the three datasets. On average, it improves the AUROC by 0.0310 AUROC (a relative increase of 20%). Conversely, DetectGPT in the white-box setting (us- ing T5-11B/GPT-3) achieves superior detection accuracy on PubMedQA but lags behind on XSum and WritingPrompt compared to RoBERTa-large. In the black-box setting (T5-11B/Neo-2.7), De- tectGPT experiences a significant reduction in detection accuracy, averaging 0.0750 
```

### Retrieved Chunk 6

- Source: `Fast-DetectGPT Efficient Zero-Shot Detection of Machine-Generated Text via Conditional Probability Curvature.pdf`
- Page: `18`
- Chunk ID: `2283`
- Chunk Type: `main`

```text
Fast-DetectGPT (GPT-J/Neo-2.7) 0.9396 0.9492 0.7225 0.8704* Fast-DetectGPT (GPT-J/GPT-J) 0.9329* 0.9568 0.6664 0.8520 Table 7: Detection of GPT-3 generations, evaluated in AUROC. Fast-DetectGPT in the black-box settings (using local models) significantly outperforms DetectGPT in both the black-box setting and the white-box setting (using GPT-3) on News (XSum) and story (WritingPrompts). Fast-DetectGPT uses 6B GPT-J to generate samples and models from 1.5B GPT-2 to 6B GPT-J to score samples, while DetectGPT uses 11B T5 to generate perturbations and models from 1.5B GPT-2 to 6B GPT-J, and GPT-3 service to score them.♢ – we report the official scores from Mitchell et al. (2023) instead of rerunning the experiments after confirming the consistency on RoBERTa-base/large. Table 7 presents a comp
```

### Retrieved Chunk 7

- Source: `DetectGPT-SC Improving Detection of Text Generated by Large Language Models through Self-Consistency with Masked Predictions.pdf`
- Page: `2`
- Chunk ID: `1517`
- Chunk Type: `main`

```text
Running Title for Header 2 Related Work Recent research has shown promising results in the development of detection methods. The existing detectors are built on the assumption that there is a distributional difference between human-generated texts and AI-generated texts. These differences are typically identified by training classifiers or using statistical information. Classifier-based detectors. Classifier-based detectors are commonly used in natural language processing detection paradigms, especially in fake news and misinformation detection [3]. Guo et al. [4] proposed the ChatGPT Detector, where they initially constructed a dataset consisting of ChatGPT conversations with human questions and answers, and trained a text detection classifier based on this dataset. The use of these metho
```

### Retrieved Chunk 8

- Source: `Fast-DetectGPT Efficient Zero-Shot Detection of Machine-Generated Text via Conditional Probability Curvature.pdf`
- Page: `7`
- Chunk ID: `2236`
- Chunk Type: `main`

```text
Detectors are expected to generalize to differ- ent domains and languages for higher usabil- ity. We compare Fast-DetectGPT against su- pervised detectors on both in-distribution and out-distribution datasets. Figure 5 reveals that Fast-DetectGPT achieves competitive detection accuracy on the in-distribution datasets XSum and WMT16-English. However, it significantly outperforms supervised detectors on the out- distribution datasets PubMedQA and WMT16- German. Moreover, it is noteworthy that Fast- DetectGPT consistently outperforms DetectGPT across all four datasets. These results underscore the robustness of Fast-DetectGPT across diverse domains and languages. Detection Method Detection Accuracy (AUROC) Figure 5: Compare with supervised detectors, evaluated in AUROC. We generate 200 test s
```


### Manual Observation

- Are the candidate papers reasonable?
- Are the selected papers appropriate for the question?
- Are the retrieved chunks actually useful for answering the question?
- Are there checklist / references / appendix chunks?
- Overall quality: Good / Medium / Poor

---

# Overall Summary

- Total test cases: `5`
- Behavior check pass: `3/5`
- Expected source check pass: `3/5`
- Source diversity check pass: `5/5`
- Noise check pass: `5/5`

## Interpretation

If behavior checks fail, improve the paper-level catalog or the mode decision rule.

If source checks fail, improve title / abstract extraction or add aliases for method names.

If noise checks fail, improve chunk_type labeling in build_index.py.

If candidate papers are correct but retrieved chunks are poor, add a reranker.

