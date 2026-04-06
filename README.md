What is Generative AI? (Max 300 Words)

Generative AI is a type of artificial intelligence designed to create new content—like text, images, audio, or code—based on the patterns it learned from large datasets. Unlike traditional AI that predicts labels or outcomes, generative AI generates new, realistic outputs.

Difference from Traditional Machine Learning:

Traditional ML models focus on classification, regression, or pattern recognition. They answer “what is”.
Generative AI focuses on “what could be”, creating entirely new content rather than just predicting existing patterns.

Examples of Real-World Applications:

Text Generation: ChatGPT can write articles, summarize text, or answer questions.
Image Creation: DALL·E generates realistic images from text descriptions.
Code Assistance: GitHub Copilot suggests or writes code snippets automatically.

Generative AI relies on large models called Large Language Models (LLMs), which understand context, patterns, and relationships in massive datasets to produce coherent and contextually relevant outputs. It is transforming industries like content creation, healthcare, design, and software development.

Self-Attention Explained (Example: “The cat sat on the mat”)

Query (Q), Key (K), Value (V):

Query: What I’m looking for (e.g., “sat” wants to know its related words).
Key: What each word “offers” to the query (each word encodes its own information).
Value: The actual information to pass along if the query finds it relevant.

Steps:

Compute similarity between Query and all Keys → tells us which words are important.
Scale by √d_k: Prevents extremely large dot-product values when the embedding dimension is high, keeping gradients stable.
Apply Softmax: Converts similarity scores into probabilities that sum to 1. This decides how much attention each word receives.

Example:

Query: “sat”
Keys: “The”, “cat”, “sat”, “on”, “the”, “mat”
Attention highlights “cat” as highly relevant → output emphasizes “cat” in context.

Problem Solved:
RNNs struggled with long-range dependencies (e.g., connecting “cat” with “sat”). Attention allows direct connections between any words, regardless of distance, improving context understanding.

| Feature       | Encoder                                   | Decoder                                |
| ------------- | ----------------------------------------- | -------------------------------------- |
| Purpose       | Understand input (text, image, etc.)      | Generate output based on encoded input |
| Input         | Raw input sequence                        | Previous outputs + encoder context     |
| Output        | Contextual representation (hidden states) | Predicted next token or sequence       |
| Use Case      | Translation, summarization (source)       | Translation, text generation (target)  |
| Example Model | BERT                                      | GPT                                    |


Summary: Encoders understand, decoders create. Some models use Encoder-Decoder (T5, BART) for tasks like translation; others are Decoder-only (GPT) for generative tasks.
