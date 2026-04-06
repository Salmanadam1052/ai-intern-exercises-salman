# transformer-day1-exercise-salman

## 1️⃣ What is Generative AI?

Generative AI refers to a class of machine learning models capable of producing new content — text, images, audio, code — that resembles the data they were trained on. Unlike traditional discriminative models, which learn to map inputs to fixed labels (e.g., "is this email spam or not?"), generative models learn the underlying distribution of data and can sample from it to produce novel outputs.

Traditional ML is largely task-specific and output-bounded: a classifier outputs a class, a regressor outputs a number. Generative AI is open-ended — the same model trained on text can answer questions, summarize documents, write code, and translate languages. This flexibility comes from training on massive, diverse datasets and learning rich internal representations of language or vision.

**Three real-world applications:**

1. **Text generation & summarization** — LLMs like GPT and Claude generate coherent long-form text and condense documents, powering assistants, search, and content tools.
2. **Image synthesis** — Diffusion models (e.g., Stable Diffusion, DALL·E) generate photorealistic images from text prompts, used in design, advertising, and media.
3. **Code generation** — Models like GitHub Copilot assist developers by auto-completing functions, generating boilerplate, and explaining existing code.

---

## 2️⃣ Self-Attention Explained

**Sentence:** *"The cat sat on the mat"*

Each word is first represented as an embedding vector. Self-attention then asks, for every word: *which other words in this sentence are most relevant to understanding me?*

To answer this, each word produces three vectors:

- **Query (Q):** what this word is looking for — its "question" to the rest of the sequence.
- **Key (K):** what this word is advertising about itself — its "label" for others to match against.
- **Value (V):** the actual information this word contributes if selected.

Attention scores are computed as the dot product of Q with every K, giving a raw measure of compatibility. For example, when processing *"sat"*, its Q will score highly against the K of *"cat"* (the subject doing the sitting) and *"mat"* (where it sat).

**Why scale by √d_k?**  
Dot products grow in magnitude as d_k increases. Large values push the softmax into regions with near-zero gradients, stalling learning. Dividing by √d_k keeps scores in a stable range.

**Why apply Softmax?**  
Softmax converts raw scores into a proper probability distribution that sums to 1. This means the output is a weighted blend of Value vectors, where the weights reflect how much attention each position deserves.

**What problem does this solve over RNNs?**  
RNNs process sequences token-by-token, passing state forward. Long-range dependencies (e.g., a pronoun referring to a noun 20 tokens earlier) are hard to preserve — the signal degrades with distance. Self-attention directly connects every position to every other position in a single operation, making long-range relationships as easy to learn as adjacent ones.

---

## 3️⃣ Encoder vs Decoder

| Component | Encoder | Decoder |
|---|---|---|
| **Primary role** | Build rich contextual representations of input | Generate output tokens sequentially |
| **Self-attention type** | Bidirectional (each token attends to all others) | Masked (each token only attends to past tokens) |
| **Cross-attention** | Not present | Attends to encoder output at each decoding step |
| **Masked attention** | Not used | Applied to prevent attending to future tokens during training |
| **Typical use cases** | Classification, embedding, NER (e.g., BERT) | Text generation, translation (e.g., GPT, decoder side of T5) |

**Masked attention** ensures that during decoding, position *i* cannot see positions *i+1, i+2, …* — this preserves the autoregressive property (generating one token at a time).

**Cross-attention** in the decoder allows each generated token to query the full encoder output, letting the decoder "look at" the source sequence at every step — critical for tasks like translation.

---

## 4️⃣ Vision Transformers (ViT)

CNNs process images through sliding convolutional filters that capture local spatial patterns hierarchically. ViT takes a fundamentally different approach: it treats an image as a sequence of fixed-size patches and applies the standard Transformer encoder directly to that sequence.

**Image patches** are small, non-overlapping rectangular regions of the input image — typically 16×16 pixels. A 224×224 image yields 196 such patches.

Each patch is flattened into a 1D vector and linearly projected into a fixed-size embedding dimension. This projection is learned end-to-end. The result is a sequence of patch embeddings, conceptually equivalent to word token embeddings in NLP.

**Positional embeddings** are added because self-attention is permutation-invariant — it has no inherent notion of order or spatial layout. Without positional information, the model cannot distinguish whether a patch came from the top-left or bottom-right of the image. Learned positional embeddings encode spatial position and are added to the patch embeddings before the Transformer processes them.

Compared to CNNs, ViT has no built-in inductive biases about locality or translation equivariance. CNNs assume nearby pixels are related; ViT makes no such assumption and instead learns global relationships from scratch via attention. This makes ViT more flexible but also more data-hungry — it typically requires large-scale pretraining to match CNN performance.

---

## Running the Code

```bash
pip install numpy
python attention_demo.py
```
