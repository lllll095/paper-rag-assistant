# Paper RAG Assistant：工程化学术论文 RAG 系统

[![Test](https://github.com/lllll095/paper-rag-assistant/actions/workflows/test.yml/badge.svg)](https://github.com/lllll095/paper-rag-assistant/actions/workflows/test.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

一个工程化的检索增强生成（RAG）系统，面向学术论文问答。
支持 PDF 知识导入、分层论文检索、混合稠密/BM25 检索、
交叉编码器重排序、查询路由和基于来源的答案生成。

---

## RAG 流水线

```text
PDF 论文
  |-- 文本提取和分块
  |-- Chunk 级向量索引（Chroma + bge-small-en-v1.5）
  |-- 论文级目录索引
  |-- 查询路由器（方法 / 对比 / 综述 / 证据 / 实验）
  |-- 分层检索（先找论文，再找 Chunk）
  |-- 混合检索（稠密向量 + BM25）
  |-- 交叉编码器重排序（ms-marco-MiniLM-L6-v2）
  |-- 基于来源的 LLM 答案生成
  |-- 答案质量评估
```

## 核心功能

- PDF 加载与文本提取 - 自动清洗和结构化
- 文本分块 - 带元数据（来源、页码、chunk_id、chunk_type）
- Chroma 向量数据库 - 稠密嵌入存储
- 论文级目录 - 用于文档级路由
- 分层检索 - 先确定相关论文，再检索 Chunk
- 混合检索 - 稠密嵌入 + BM25 关键词搜索
- 交叉编码器重排序 - 精排候选 Chunk
- 查询路由器 - 将问题分类为方法/对比/综述/证据/实验
- 来源导向的答案生成 - 带引用的答案
- 多级评估 - 检索、重排序、混合检索、查询路由、答案质量
- Streamlit 演示界面

## 快速开始

```bash
# 克隆
git clone https://github.com/lllll095/paper-rag-assistant.git
cd paper-rag-assistant

# 创建环境
conda create -n rag-week1 python=3.10
conda activate rag-week1

# 安装
pip install -e ".[dev]"

# 配置
cp .env.example .env
# 编辑 .env 填入 API key

# 构建索引
python src/build_index.py
python src/build_paper_catalog.py

# 运行 RAG
python src/rag_engineered.py

# 启动 Web UI
streamlit run app.py

# 运行测试
python -m pytest tests/ -v
```

## 最终架构

```text
用户问题
  |-- 查询路由器
  |-- 论文级检索
  |-- 候选论文
  |-- 稠密检索 + BM25 检索
  |-- 合并候选 Chunk
  |-- 交叉编码器重排序
  |-- 最佳证据 Chunk
  |-- LLM 答案生成
  |-- 带来源的答案
```

## 评估脚本

| 脚本 | 用途 |
|---|---|
| eval_engineered_rag.py | 评估分层检索质量 |
| eval_reranker_ablation.py | 对比纯向量 vs 重排序 |
| eval_hybrid_retrieval.py | 对比稠密、BM25 和混合 |
| eval_query_router.py | 评估查询分类准确率 |
| eval_answer_quality.py | 评估答案事实性和引用 |

## 项目结构

```
src/
  rag_engineered.py      主 RAG 流水线
  query_router.py        查询分类路由器
  bm25_retriever.py      BM25 关键词检索
  reranker.py            交叉编码器重排序
  load_pdf.py            PDF 文本提取
  split_text.py          文本分块与元数据
  build_index.py         构建向量索引
  build_paper_catalog.py 构建论文目录
  eval_*.py              评估脚本
app.py                   Streamlit 界面
tests/                   测试
```

## 许可

MIT License - 详见 LICENSE
