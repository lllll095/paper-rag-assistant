# Answer-level Evaluation Report

This report evaluates the final answers produced by the engineered RAG system.

It checks answer relevance, groundedness, citation support, completeness, and hallucination risk.

---

## q1: What AI-generated text detection methods are discussed in these papers?

### Question Metadata

- Question type: `survey`
- Expected behavior: summarize multiple methods across papers

### Retrieval Info

- Final retrieval mode: `global`
- Query route: `{'query_type': 'survey', 'retrieval_mode': 'global', 'paper_k': 6, 'chunk_k': 10, 'max_per_source': 3, 'reason': 'The question asks for a broad overview across papers.'}`

### Retrieved Sources

1. `ASurvey of AI-generated Text Forensic Systems Detection Attribution and Characterization.pdf`, page `2`, chunk `430`, type `main`, vector `0.3126138746738434`, bm25 `13.406517717679826`, reranker `5.634542465209961`
2. `SeqXGPT Sentence-Level AI-Generated Text Detection.pdf`, page `0`, chunk `3392`, type `main`, vector `0.33876076340675354`, bm25 `9.174669325441254`, reranker `5.61989688873291`
3. `ASurvey of AI-generated Text Forensic Systems Detection Attribution and Characterization.pdf`, page `3`, chunk `436`, type `main`, vector `0.33706334233283997`, bm25 `unknown`, reranker `5.505354881286621`
4. `Ghostbuster Detecting Text Ghostwritten by Large Language Models.pdf`, page `0`, chunk `2380`, type `main`, vector `0.33417007327079773`, bm25 `12.00118545728993`, reranker `5.462650299072266`
5. `Ghostbuster Detecting Text Ghostwritten by Large Language Models.pdf`, page `2`, chunk `2390`, type `main`, vector `unknown`, bm25 `12.592422438546283`, reranker `5.280979156494141`
6. `SeqXGPT Sentence-Level AI-Generated Text Detection.pdf`, page `1`, chunk `3398`, type `main`, vector `0.3295079171657562`, bm25 `unknown`, reranker `5.27540397644043`
7. `ASurvey of AI-generated Text Forensic Systems Detection Attribution and Characterization.pdf`, page `0`, chunk `419`, type `main`, vector `0.3390544056892395`, bm25 `12.58639807148704`, reranker `5.121118068695068`
8. `SeqXGPT Sentence-Level AI-Generated Text Detection.pdf`, page `0`, chunk `3395`, type `main`, vector `0.3651220202445984`, bm25 `unknown`, reranker `5.0298662185668945`

### Answer

```text
Answer:  
The discussed AI-generated text detection methods include supervised detectors (e.g., Bag-of-Words/TF-IDF with logistic regression, random forest, SVC; LSTM, GRU, CNN), zero-shot detectors, Energy-Based Models (EBMs), Topological Data Analysis (TDA) on attention maps, Ghostbuster (structured search + linear classification using word probabilities from weaker LMs), and SeqXGPT (sentence-level detection using log probability lists from white-box LLMs). Perplexity-based methods and model-wise approaches like DetectGPT and Sniffer are also mentioned, though noted as unsuitable for sentence-level detection.

Explanation:  
The context identifies multiple detection paradigms. Supervised methods are described in [Source 1] and [Source 6], including classical feature engineering (Bag-of-Words, TF-IDF) paired with traditional classifiers, and later deep sequence models (LSTM, GRU, CNN). Zero-shot detection is named as a major category alongside supervised detection in [Source 1]. [Source 3] introduces Energy-Based Models (EBMs) and Topological Data Analysis (TDA) applied to transformer attention maps. [Source 4] details Ghostbuster’s approach—using word probabilities from a hierarchy of weaker language models and structured search over vector/scalar functions. [Source 2] and [Source 6] introduce SeqXGPT, which leverages log probability lists from white-box LLMs for sentence-level detection. [Source 8] references perplexity-based methods and notes limitations of DetectGPT and Sniffer for fine-grained (sentence-level) tasks.

Sources:  
[Source 1], [Source 2], [Source 3], [Source 4], [Source 6], [Source 8]
```

### Basic Citation Check

- Has citation: `True`
- Invalid citations: `[]`
- Citation check: Pass

### LLM Judge Scores

- Answer relevance: `5/5`
- Groundedness: `5/5`
- Citation support: `5/5`
- Completeness: `5/5`
- Insufficient context handling: `5/5`
- Hallucination risk: `low`
- Overall score: `10/10`
- Verdict: `good`
- Comments: The answer precisely summarizes multiple AI-generated text detection methods across the retrieved papers, with each method explicitly grounded in the context: supervised detectors (BoW/TF-IDF + classifiers; LSTM/GRU/CNN) from [Source 1] and [Source 6]; zero-shot detection as a category named in [Source 1]; EBMs and TDA from [Source 3]; Ghostbuster’s structured search + linear classification using word probabilities from weaker LMs from [Source 4]; SeqXGPT’s use of log probability lists from white-box LLMs from [Source 2] and [Source 6]; and perplexity-based methods/DetectGPT/Sniffer limitations noted in [Source 8]. No claim is unsupported, no source is misattributed, and all cited sources do support the corresponding claims. The answer fully satisfies the expectation to 'summarize multiple methods across papers' using only the provided context.

### Manual Notes

- Is the answer actually useful?
- Are the sources sufficient?
- Are there unsupported claims?
- Should the answer be more concise or more detailed?

---

## q2: How does AdaDetectGPT work?

### Question Metadata

- Question type: `specific_method`
- Expected behavior: explain AdaDetectGPT based on retrieved sources

### Retrieval Info

- Final retrieval mode: `global`
- Query route: `{'query_type': 'method', 'retrieval_mode': 'auto', 'paper_k': 4, 'chunk_k': 8, 'max_per_source': 6, 'reason': 'The question asks about how a method works.'}`

### Retrieved Sources

1. `AdaDetectGPT Adaptive Detection of LLM-Generated Text with Statistical Guarantees.pdf`, page `1`, chunk `213`, type `main`, vector `0.4809427261352539`, bm25 `unknown`, reranker `6.063632011413574`
2. `AdaDetectGPT Adaptive Detection of LLM-Generated Text with Statistical Guarantees.pdf`, page `41`, chunk `368`, type `main`, vector `0.4973980784416199`, bm25 `unknown`, reranker `5.962424278259277`
3. `AdaDetectGPT Adaptive Detection of LLM-Generated Text with Statistical Guarantees.pdf`, page `0`, chunk `210`, type `main`, vector `unknown`, bm25 `7.728740112323405`, reranker `5.667010307312012`
4. `AdaDetectGPT Adaptive Detection of LLM-Generated Text with Statistical Guarantees.pdf`, page `9`, chunk `256`, type `main`, vector `0.44804322719573975`, bm25 `8.84241347657191`, reranker `5.0491943359375`
5. `AdaDetectGPT Adaptive Detection of LLM-Generated Text with Statistical Guarantees.pdf`, page `1`, chunk `215`, type `main`, vector `unknown`, bm25 `8.959452228291966`, reranker `4.9158782958984375`
6. `AdaDetectGPT Adaptive Detection of LLM-Generated Text with Statistical Guarantees.pdf`, page `8`, chunk `252`, type `main`, vector `0.48041218519210815`, bm25 `unknown`, reranker `4.0706939697265625`
7. `Fast-DetectGPT Efficient Zero-Shot Detection of Machine-Generated Text via Conditional Probability Curvature.pdf`, page `8`, chunk `2240`, type `main`, vector `unknown`, bm25 `3.4566614621638627`, reranker `-1.4680233001708984`
8. `DetectGPT Zero-Shot Machine-Generated Text Detection using Probability Curvature.pdf`, page `2`, chunk `1445`, type `main`, vector `unknown`, bm25 `6.7454281321213605`, reranker `-1.7166247367858887`

### Answer

```text
Answer:  
AdaDetectGPT is an adaptive LLM-generated text detector that builds upon Fast-DetectGPT by learning a witness function $ \hat{w} $ from training data to maximize a lower bound on the true negative rate (TNR), while using normal approximation for false negative rate (FNR) control; it leverages logit-level statistics from a source LLM but improves over logits-only methods by adaptively tailoring the detection statistic.

Explanation:  
According to [Source 1], AdaDetectGPT’s workflow (Figure 1) is built upon Fast-DetectGPT and adaptively learns a witness function $ \hat{w} $ from training data to maximize a lower bound on the true negative rate (TNR), while relying on normal approximation for FNR control. It uses probability outputs (logits) from a source LLM to construct classification statistics, but—unlike prior logits-based methods—it does not rely *solely* on raw logits; instead, it learns a witness function to enhance detection effectiveness [Source 1, Source 3]. This adaptive learning provides statistical guarantees on standard classification metrics (TNR, FNR, TPR, FPR) [Source 5], and the method is computationally efficient, with training taking under one minute and low memory usage [Source 6].

Sources:  
[Source 1], [Source 3], [Source 5], [Source 6]
```

### Basic Citation Check

- Has citation: `True`
- Invalid citations: `[]`
- Citation check: Pass

### LLM Judge Scores

- Answer relevance: `5/5`
- Groundedness: `5/5`
- Citation support: `5/5`
- Completeness: `4/5`
- Insufficient context handling: `5/5`
- Hallucination risk: `low`
- Overall score: `9/10`
- Verdict: `good`
- Comments: The answer accurately and concisely explains AdaDetectGPT’s core mechanism—adaptive witness function learning from training data, TNR optimization, FNR control via normal approximation, and improvement over logits-only methods—directly supported by Sources 1, 3, 5, and 6. All cited claims (e.g., 'maximizing lower bound on TNR', 'normal approximation for FNR', 'under one minute training', 'statistical guarantees on TNR/FNR/TPR/FPR') appear verbatim or are direct paraphrases of the context. Minor incompleteness: the answer omits explicit mention of its reliance on Fast-DetectGPT’s curvature-based foundation (implied but not elaborated), and does not clarify how the witness function is *used* to transform logits (e.g., via B-splines per Source 6), but this level of technical detail is not required to answer 'how it works' at a conceptual level. No hallucinations; no unsupported claims.

### Manual Notes

- Is the answer actually useful?
- Are the sources sufficient?
- Are there unsupported claims?
- Should the answer be more concise or more detailed?

---

## q3: How does DetectGPT detect machine-generated text?

### Question Metadata

- Question type: `specific_method`
- Expected behavior: explain DetectGPT based on retrieved sources

### Retrieval Info

- Final retrieval mode: `global`
- Query route: `{'query_type': 'method', 'retrieval_mode': 'auto', 'paper_k': 4, 'chunk_k': 8, 'max_per_source': 6, 'reason': 'The question asks about how a method works.'}`

### Retrieved Sources

1. `DetectGPT Zero-Shot Machine-Generated Text Detection using Probability Curvature.pdf`, page `0`, chunk `1433`, type `main`, vector `0.4524148106575012`, bm25 `10.753234279133384`, reranker `8.607498168945312`
2. `DetectGPT Zero-Shot Machine-Generated Text Detection using Probability Curvature.pdf`, page `2`, chunk `1445`, type `main`, vector `unknown`, bm25 `13.58071750216719`, reranker `8.331501960754395`
3. `DetectGPT Zero-Shot Machine-Generated Text Detection using Probability Curvature.pdf`, page `2`, chunk `1450`, type `main`, vector `0.4474771320819855`, bm25 `unknown`, reranker `8.189292907714844`
4. `DetectGPT Zero-Shot Machine-Generated Text Detection using Probability Curvature.pdf`, page `6`, chunk `1472`, type `main`, vector `0.4136630892753601`, bm25 `10.09347475615644`, reranker `7.9210920333862305`
5. `DetectGPT Zero-Shot Machine-Generated Text Detection using Probability Curvature.pdf`, page `6`, chunk `1473`, type `main`, vector `0.41695094108581543`, bm25 `9.487253786066512`, reranker `7.728855133056641`
6. `DetectLLM Leveraging Log-Rank Information for Zero-Shot Detection of Machine-Generated Text.pdf`, page `2`, chunk `1853`, type `main`, vector `0.43436291813850403`, bm25 `7.899461110026238`, reranker `7.708574295043945`
7. `DetectGPT Zero-Shot Machine-Generated Text Detection using Probability Curvature.pdf`, page `1`, chunk `1440`, type `main`, vector `0.4930853247642517`, bm25 `unknown`, reranker `7.427803993225098`
8. `Fast-DetectGPT Efficient Zero-Shot Detection of Machine-Generated Text via Conditional Probability Curvature.pdf`, page `4`, chunk `2219`, type `main`, vector `0.4363716244697571`, bm25 `7.259480098497036`, reranker `7.364211559295654`

### Answer

```text
Answer:  
DetectGPT detects machine-generated text by measuring the curvature of the log probability function of a language model: it compares the log probability of a candidate passage under a model $ p_\theta $ to the average log probability of several perturbed versions of that passage (e.g., rewritten or paraphrased variants) under the same model. Machine-generated text tends to lie in regions of negative curvature—i.e., the original passage has significantly higher log probability than its perturbations—whereas human-written text does not show this disparity.

Explanation:  
DetectGPT leverages the observation that LLM-generated text occupies negative curvature regions of the model’s own log probability surface [Source 1]. It operationalizes this by sampling perturbations $ \tilde{x}_i $ of the input passage $ x $ (e.g., via rewriting using another model like T5), computing $ \log p_\theta(x) $ and the average $ \frac{1}{N}\sum_i \log p_\theta(\tilde{x}_i) $, and flagging $ x $ as machine-generated if the difference exceeds a threshold [Source 3], [Source 7]. This is a zero-shot method—it requires no training data, fine-tuning, or watermarking—and relies solely on the geometry of the model’s probability landscape.

Sources:  
[Source 1], [Source 3], [Source 7]
```

### Basic Citation Check

- Has citation: `True`
- Invalid citations: `[]`
- Citation check: Pass

### LLM Judge Scores

- Answer relevance: `5/5`
- Groundedness: `5/5`
- Citation support: `5/5`
- Completeness: `5/5`
- Insufficient context handling: `5/5`
- Hallucination risk: `low`
- Overall score: `10/10`
- Verdict: `good`
- Comments: The answer precisely explains DetectGPT’s core mechanism—negative curvature of the log probability function—and correctly describes its zero-shot, perturbation-based detection procedure. All key claims (e.g., comparing log pθ(x) to average log pθ(˜xi), use of T5 for perturbations, zero-shot nature, no training/watermarking) are directly supported by Sources 1, 3, and 7. No unsupported details or extraneous speculation appear; the explanation is concise yet complete given the context.

### Manual Notes

- Is the answer actually useful?
- Are the sources sufficient?
- Are there unsupported claims?
- Should the answer be more concise or more detailed?

---

## q4: Which methods provide statistical guarantees for AI-generated text detection?

### Question Metadata

- Question type: `evidence`
- Expected behavior: identify methods with statistical guarantees and cite evidence

### Retrieval Info

- Final retrieval mode: `global`
- Query route: `{'query_type': 'survey', 'retrieval_mode': 'global', 'paper_k': 6, 'chunk_k': 10, 'max_per_source': 3, 'reason': 'The question asks for a broad overview across papers.'}`

### Retrieved Sources

1. `SeqXGPT Sentence-Level AI-Generated Text Detection.pdf`, page `1`, chunk `3398`, type `main`, vector `0.334208607673645`, bm25 `unknown`, reranker `5.327617168426514`
2. `AdaDetectGPT Adaptive Detection of LLM-Generated Text with Statistical Guarantees.pdf`, page `1`, chunk `215`, type `main`, vector `unknown`, bm25 `18.72273401446101`, reranker `5.063398361206055`
3. `AdaDetectGPT Adaptive Detection of LLM-Generated Text with Statistical Guarantees.pdf`, page `0`, chunk `209`, type `main`, vector `0.37700194120407104`, bm25 `11.511815394821955`, reranker `4.880607604980469`
4. `Intrinsic Dimension Estimation for Robust Detection of AI-Generated Texts.pdf`, page `6`, chunk `2576`, type `main`, vector `0.32673242688179016`, bm25 `10.9063954952778`, reranker `4.126020431518555`
5. `SeqXGPT Sentence-Level AI-Generated Text Detection.pdf`, page `1`, chunk `3400`, type `main`, vector `0.3669587969779968`, bm25 `unknown`, reranker `4.082742214202881`
6. `SeqXGPT Sentence-Level AI-Generated Text Detection.pdf`, page `0`, chunk `3395`, type `main`, vector `0.36551475524902344`, bm25 `unknown`, reranker `4.037962913513184`
7. `Intrinsic Dimension Estimation for Robust Detection of AI-Generated Texts.pdf`, page `0`, chunk `2544`, type `main`, vector `0.3520209789276123`, bm25 `13.322657131256387`, reranker `3.231004238128662`
8. `AdaDetectGPT Adaptive Detection of LLM-Generated Text with Statistical Guarantees.pdf`, page `15`, chunk `285`, type `main`, vector `0.37250983715057373`, bm25 `14.140384631025539`, reranker `3.227660655975342`

### Answer

```text
Answer:  
AdaDetectGPT provides statistical guarantees for AI-generated text detection.

Explanation:  
The paper *AdaDetectGPT: Adaptive Detection of LLM-Generated Text with Statistical Guarantees* explicitly states that it “provides statistical performance guarantees”, including “finite-sample error bounds for its TNR, FNR, true positive rate (TPR) and false positive rate (FPR)” [Source 2]. It further notes that existing logits-based detectors “generally lack systematic statistical analysis”, positioning AdaDetectGPT as a contribution that fills this gap with rigorous theoretical analysis [Source 2]. No other method mentioned in the context is described as offering formal statistical guarantees.

Sources:  
[Source 2], [Source 3]
```

### Basic Citation Check

- Has citation: `True`
- Invalid citations: `[]`
- Citation check: Pass

### LLM Judge Scores

- Answer relevance: `5/5`
- Groundedness: `5/5`
- Citation support: `5/5`
- Completeness: `5/5`
- Insufficient context handling: `5/5`
- Hallucination risk: `low`
- Overall score: `10/10`
- Verdict: `good`
- Comments: The answer correctly identifies AdaDetectGPT as the only method in the retrieved context that provides statistical guarantees, directly quoting and interpreting Source 2’s explicit claim about 'finite-sample error bounds' for TNR, FNR, TPR, and FPR. It accurately notes the absence of such guarantees for other methods (e.g., DetectGPT, Sniffer, SeqXGPT, intrinsic dimension methods) based on the context. All claims are tightly grounded, citations are precise and supportive, and no unsupported assertions or hallucinations are present.

### Manual Notes

- Is the answer actually useful?
- Are the sources sufficient?
- Are there unsupported claims?
- Should the answer be more concise or more detailed?

---

## q5: What is the difference between DetectGPT and AdaDetectGPT?

### Question Metadata

- Question type: `comparison`
- Expected behavior: compare the two methods using evidence from both papers

### Retrieval Info

- Final retrieval mode: `global`
- Query route: `{'query_type': 'comparison', 'retrieval_mode': 'global', 'paper_k': 6, 'chunk_k': 10, 'max_per_source': 4, 'reason': 'The question asks for comparison between methods or papers.'}`

### Retrieved Sources

1. `AdaDetectGPT Adaptive Detection of LLM-Generated Text with Statistical Guarantees.pdf`, page `4`, chunk `229`, type `main`, vector `0.4683022201061249`, bm25 `24.61733296769065`, reranker `6.326869010925293`
2. `AdaDetectGPT Adaptive Detection of LLM-Generated Text with Statistical Guarantees.pdf`, page `9`, chunk `256`, type `main`, vector `0.3740534782409668`, bm25 `unknown`, reranker `4.36726713180542`
3. `AdaDetectGPT Adaptive Detection of LLM-Generated Text with Statistical Guarantees.pdf`, page `0`, chunk `210`, type `main`, vector `unknown`, bm25 `16.138881097467298`, reranker `2.6803369522094727`
4. `AdaDetectGPT Adaptive Detection of LLM-Generated Text with Statistical Guarantees.pdf`, page `7`, chunk `247`, type `main`, vector `0.443564236164093`, bm25 `unknown`, reranker `2.6607179641723633`
5. `DetectGPT-SC Improving Detection of Text Generated by Large Language Models through Self-Consistency with Masked Predictions.pdf`, page `2`, chunk `1519`, type `main`, vector `0.5957632660865784`, bm25 `13.419429149053038`, reranker `2.0015382766723633`
6. `DetectGPT Zero-Shot Machine-Generated Text Detection using Probability Curvature.pdf`, page `12`, chunk `1508`, type `main`, vector `0.5422935485839844`, bm25 `unknown`, reranker `1.9752681255340576`
7. `DetectGPT Zero-Shot Machine-Generated Text Detection using Probability Curvature.pdf`, page `5`, chunk `1470`, type `main`, vector `unknown`, bm25 `12.393047077123628`, reranker `1.8043674230575562`
8. `DetectGPT Zero-Shot Machine-Generated Text Detection using Probability Curvature.pdf`, page `8`, chunk `1486`, type `main`, vector `0.581191897392273`, bm25 `unknown`, reranker `1.5131006240844727`

### Answer

```text
Answer:  
AdaDetectGPT is an adaptive extension of Fast-DetectGPT (not DetectGPT directly), which learns a data-driven witness function to improve detection performance and provides statistical guarantees on error rates; DetectGPT is a zero-shot, curvature-based method relying on log-probability perturbations without learning from training data.

Explanation:  
The context clarifies that AdaDetectGPT builds upon *Fast-DetectGPT*, not DetectGPT directly — though DetectGPT is listed as a benchmark in [Source 4]. AdaDetectGPT “adaptively learns a witness function from training data” to enhance logits-based detection and offers statistical guarantees on true/false positive/negative rates [Source 3]. In contrast, DetectGPT is described as a zero-shot, white-box method that exploits the negative curvature of log-probabilities via perturbed variants (e.g., masked predictions) without requiring training data or learned components [Source 5], [Source 7]. The context does not describe AdaDetectGPT as a modification of DetectGPT itself, but rather as an improvement over Fast-DetectGPT — which itself is a variant or simplification of DetectGPT (as implied by naming and [Source 4] listing both DetectGPT and Fast-DetectGPT as separate baselines). No source defines AdaDetectGPT as derived from DetectGPT; instead, it is positioned as advancing Fast-DetectGPT with adaptivity and theoretical guarantees.

Sources:  
[Source 3], [Source 4], [Source 5], [Source 7]
```

### Basic Citation Check

- Has citation: `True`
- Invalid citations: `[]`
- Citation check: Pass

### LLM Judge Scores

- Answer relevance: `5/5`
- Groundedness: `5/5`
- Citation support: `5/5`
- Completeness: `4/5`
- Insufficient context handling: `5/5`
- Hallucination risk: `low`
- Overall score: `9/10`
- Verdict: `good`
- Comments: The answer correctly distinguishes AdaDetectGPT as an adaptive, trained extension of Fast-DetectGPT (not DetectGPT directly), citing its learned witness function and statistical guarantees ([Source 3], [Source 4]). It accurately characterizes DetectGPT as zero-shot, curvature-based, and perturbation-dependent ([Source 5], [Source 7]), with no training or learned components. All claims are directly supported: [Source 3] states AdaDetectGPT 'adaptively learns a witness function from training data' and provides guarantees on error rates; [Source 4] lists DetectGPT and Fast-DetectGPT as separate baselines, confirming AdaDetectGPT builds on the latter; [Source 5] explains DetectGPT’s curvature principle and perturbation mechanism. The only minor incompleteness is the lack of explicit clarification that Fast-DetectGPT itself is a variant of DetectGPT — but this is reasonably inferred from naming and context ([Source 4] lists both, and [Source 2] compares AdaDetectGPT vs Fast-DetectGPT, not vs DetectGPT), and the answer responsibly avoids asserting unverified lineage. No hallucinations occur.

### Manual Notes

- Is the answer actually useful?
- Are the sources sufficient?
- Are there unsupported claims?
- Should the answer be more concise or more detailed?

---

## q6: Which methods use logits for AI-generated text detection?

### Question Metadata

- Question type: `technical_term`
- Expected behavior: identify logits-related methods if supported by the retrieved context

### Retrieval Info

- Final retrieval mode: `global`
- Query route: `{'query_type': 'survey', 'retrieval_mode': 'global', 'paper_k': 6, 'chunk_k': 10, 'max_per_source': 3, 'reason': 'The question asks for a broad overview across papers.'}`

### Retrieved Sources

1. `SeqXGPT Sentence-Level AI-Generated Text Detection.pdf`, page `1`, chunk `3400`, type `main`, vector `0.37843796610832214`, bm25 `unknown`, reranker `6.267269134521484`
2. `DALD Improving Logits-based Detector without Logits from Black-box LLMs.pdf`, page `3`, chunk `1336`, type `main`, vector `0.4254685044288635`, bm25 `12.442566169287424`, reranker `6.1152777671813965`
3. `DALD Improving Logits-based Detector without Logits from Black-box LLMs.pdf`, page `2`, chunk `1330`, type `main`, vector `0.3458750247955322`, bm25 `unknown`, reranker `5.963219165802002`
4. `DALD Improving Logits-based Detector without Logits from Black-box LLMs.pdf`, page `3`, chunk `1337`, type `main`, vector `unknown`, bm25 `13.264630182583613`, reranker `5.9245405197143555`
5. `Ghostbuster Detecting Text Ghostwritten by Large Language Models.pdf`, page `1`, chunk `2386`, type `main`, vector `unknown`, bm25 `11.90203672886834`, reranker `5.709489822387695`
6. `SeqXGPT Sentence-Level AI-Generated Text Detection.pdf`, page `1`, chunk `3398`, type `main`, vector `0.3624163866043091`, bm25 `unknown`, reranker `5.286731719970703`
7. `DetectLLM Leveraging Log-Rank Information for Zero-Shot Detection of Machine-Generated Text.pdf`, page `0`, chunk `1843`, type `main`, vector `0.41239988803863525`, bm25 `12.191089759801827`, reranker `5.261913299560547`
8. `SeqXGPT Sentence-Level AI-Generated Text Detection.pdf`, page `0`, chunk `3395`, type `main`, vector `0.38384005427360535`, bm25 `unknown`, reranker `5.04334831237793`

### Answer

```text
Answer:  
DetectGPT, Fast-DetectGPT, and DetectLLM (specifically DetectLLM-NPR) are logits-based methods for AI-generated text detection.

Explanation:  
The context explicitly identifies DetectGPT and Fast-DetectGPT as logits-based detection methods that operate in the white-box setting—i.e., they rely on access to the source model’s logits or output probabilities (e.g., p(xₗ|x[1:l−1])) [Source 4]. DetectGPT uses the source model for scoring based on curvature of the log probability function, and Fast-DetectGPT builds on it using a surrogate model and conditional probability sampling—both grounded in logits-derived metrics. DetectLLM is also logits-based: its two variants (DetectLLM-LRR and DetectLLM-NPR) leverage “Log-Rank information”, and DetectLLM-NPR is described as perturbation-based and requiring fewer perturbations than prior work—consistent with logits-driven scoring (e.g., rank statistics over token log-probabilities), as implied by its naming and zero-shot, model-agnostic design [Source 7]. In contrast, methods like GPTZero and Sniffer are mentioned in contexts emphasizing perplexity or document-level binary classification but not logits usage [Source 1, Source 6], and DALD is explicitly *designed to improve logits-based detectors without access to logits*, confirming that logits-based methods (like DetectGPT) are its reference point [Source 2, Source 3, Source 4].

Sources:  
[Source 2], [Source 3], [Source 4], [Source 7]
```

### Basic Citation Check

- Has citation: `True`
- Invalid citations: `[]`
- Citation check: Pass

### LLM Judge Scores

- Answer relevance: `5/5`
- Groundedness: `4/5`
- Citation support: `4/5`
- Completeness: `4/5`
- Insufficient context handling: `5/5`
- Hallucination risk: `medium`
- Overall score: `8/10`
- Verdict: `good`
- Comments: The answer correctly identifies DetectGPT and Fast-DetectGPT as logits-based methods, directly supported by Source 4 (which explicitly names them in '3.2 Logits-based Detection Methods' and describes their reliance on source/surrogate model logits/probabilities). It also correctly notes DALD is *not* logits-based but improves such detectors (Sources 2–4), supporting the contrast. However, 'DetectLLM' being logits-based is *not directly supported*: Source 7 states it leverages 'Log-Rank information' and mentions perturbations, but never says 'logits', 'probabilities', or 'white-box'; 'Log-Rank' is ambiguous — could refer to rank of log-probabilities (logits-adjacent) or something else. So claiming DetectLLM-NPR is logits-based goes slightly beyond the context (hence groundedness/citation_support = 4, not 5). No hallucination of nonexistent methods; all named methods appear in context. Answer is complete *within context limits* and avoids fabricating unsupported claims — hence no insufficient_context_handling issue.

### Manual Notes

- Is the answer actually useful?
- Are the sources sufficient?
- Are there unsupported claims?
- Should the answer be more concise or more detailed?

---

# Overall Summary

- Number of evaluated questions: `6`
- Average overall score: `9.33/10`
- Average groundedness: `4.83/5`
- Average answer relevance: `5.00/5`
- High hallucination risk cases: `0`
- No-citation cases: `0`

## Interpretation

- If relevance is low, improve query routing or retrieval coverage.
- If groundedness is low, improve reranking and context filtering.
- If citation support is low, improve the answer prompt and citation format.
- If completeness is low, increase chunk_k or improve paper catalog.
- If hallucination risk is high, make the answer prompt more conservative.
