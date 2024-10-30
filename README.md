# **MaE: Math Misconceptions and Errors Dataset**

This dataset supports the research described in the paper [A Benchmark for Math Misconceptions: Bridging Gaps in Middle School Algebra with AI-Supported Instruction](https://arxiv.org/abs/your-link) by Nancy Otero, Stefania Druga, and Andrew Lan.

### **Overview**
The **MaE (Math Misconceptions and Errors)** dataset is a collection of 220 diagnostic examples designed by math learning researchers that represent 55 common algebra misconceptions among middle school students. It aims to provide insights into student errors and misconceptions in algebra, supporting the development of AI-enhanced educational tools that can improve math instruction and learning outcomes.

## **Dataset Details**

* Total Misconceptions: 55
* Total Examples: 220
* Topics Covered:

1. **Number sense** (MaE01-MaE05)
   - Understanding numbers and their relationships
2. **Number operations** (MaE06-MaE22)
   - Integer subtraction
   - Fractions and decimal operations
   - Order of operations
3. **Ratios and proportional reasoning** (MaE23-MaE28)
   - Ratio concepts
   - Proportional thinking
   - Problem-solving with ratios
4. **Properties of numbers and operations** (MaE31-MaE34)
   - Commutative, associative, and distributive properties
   - Algebraic manipulations
   - Order of operations
5. **Patterns, relationships, and functions** (MaE35-MaE42)
   - Pattern analysis and generalization
   - Tables, graphs, and symbolic rules
   - Function relationships
6. **Algebraic representations** (MaE43-MaE44)
   - Symbolic expressions and graphs
   - Multiple representations
   - Linear equations
7. **Variables, expressions, and operations** (MaE45-MaE48)
   - Expression structure
   - Polynomial arithmetic
   - Equation creation and reasoning
8. **Equations and inequalities** (MaE49-MaE55)
   - Linear equations and inequalities
   - Proportional relationships
   - Function modeling

Each misconception is represented by four diagnostic examples, featuring both correct and incorrect answers. The examples include detailed explanations to highlight the reasoning behind the errors.

## **Data Format**
The dataset is stored in a JSON format with the following fields:
* **Misconception:** Description of the misconception.
* **Misconception ID:** Unique identifier for each misconception.
* **Topic:** Category of the misconception.
* **4 Diagnostic Examples,** each containing:
  - Question
  - Incorrect answer demonstrating the misconception
  - Correct answer
  - Source reference
  - Images or graphs (where applicable)

## **Validation**

* Dataset tested with GPT-4, achieving 83.9% accuracy when constrained by topic
* Validated by middle school math educators
* 80% of surveyed teachers confirmed encountering these misconceptions in their classrooms

## **Intended Use**
The MaE dataset is designed to:

1. **Support AI development:** AI models can use this dataset to diagnose algebra misconceptions in students' responses.
2. **Aid educators:** Teachers can use the dataset to understand common student errors and adjust instruction accordingly.
3. **Enhance curriculum design:** By identifying frequent misconceptions, curriculum developers can create targeted interventions to address these learning gaps.
