# Week 1 RAG-QA Demo

## Question

What is the main contribution of AdaDetectGPT Adaptive Detection of LLM-Generated Text with Statistical Guarantees? Please answer based on the abstract and introduction.

## Answer

The main contribution of AdaDetectGPT is an adaptive LLM-generated text detector that leverages external training data to learn a witness function, while using normal approximation for false negative rate control, thereby providing statistical guarantees not present in prior logits-based detectors.

## Explanation

The abstract and introduction state that existing logits-based detectors are sub-optimal. AdaDetectGPT improves upon them by adaptively learning a witness function from training data to enhance detection effectiveness.

The paper builds on Fast-DetectGPT and optimizes for true negative rate while controlling false negative rate using normal approximation. This provides statistical guarantees and makes the method computationally and statistically efficient.

## Retrieved Sources

1. AdaDetectGPT Adaptive Detection of LLM-Generated Text with Statistical Guarantees.pdf, page 0, chunk 209
2. AdaDetectGPT Adaptive Detection of LLM-Generated Text with Statistical Guarantees.pdf, page 1, chunk 213
3. AdaDetectGPT Adaptive Detection of LLM-Generated Text with Statistical Guarantees.pdf, page 41, chunk 368

## Observation

This demo shows that the basic RAG pipeline is working.

Compared with the earlier vague query:

```text
What is the main contribution of this paper?