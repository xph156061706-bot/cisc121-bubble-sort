---
title: Cisc121 Bubble Sort
emoji: 🐨
colorFrom: blue
colorTo: green
sdk: gradio
sdk_version: 6.0.1
app_file: app.py
pinned: false
---

Check out the configuration reference at https://huggingface.co/docs/hub/spaces-config-reference

# Bubble Sort Visualizer

This project demonstrates the Bubble Sort algorithm step-by-step using a Gradio web interface. The goal is to allow users to clearly observe how each comparison and swap changes the list over time.

---

### Demo Video

![demo](bubble_sort_demo.gif)



## Problem Breakdown & Computational Thinking

### Decomposition
The problem was broken down into components:
- Convert the text input into a list of integers
- Perform bubble sort and record every comparison
- Display results in a readable format
- Provide an interactive user interface

### Pattern Recognition
Bubble Sort repeatedly compares adjacent pairs and pushes the largest values to the end. This pattern makes the algorithm predictable and traceable.

### Abstraction
Only essential details are shown to the user:
- Which values are compared
- Whether a swap occurred
- The current state of the list after each comparison

### Algorithm Design
The algorithm is implemented as:

```
for each pass:
    for each index i:
        compare i and i+1
        swap if needed
        record step
```

Each recorded step includes:

```
(pass, i, j, snapshot, swapped?)
```

---

## Inputs and Outputs

### Input
- A list of comma-separated integers  
  Example: `5, 1, 4, 2, 8`
- The **Random list** button generates random test data automatically

### Output
A markdown table showing:
- Step number  
- Bubble sort pass number  
- Compared indices
- Array state after comparison  
- Swap indicator  

Example:

| Step | Pass | i | j | Array | Swapped? |
|------|------|---|---|-------|----------|
| 0 | 0 | 0 | 1 | `[1, 5, 4, 2, 8]` | yes |

---

## Code Overview

### Main functions:
- `parse_list()` converts input into integers
- `bubble_sort_steps()` performs the sort and records steps
- `format_steps_markdown()` displays the steps cleanly
- Gradio manages the UI

### Dependencies

```
gradio
```

---

## Run Instructions

### Run locally:

```
python app.py
```

Browser will open automatically at:

```
http://127.0.0.1:7860/
```

---

## Hugging Face Deployment

https://huggingface.co/spaces/puhanx/cisc121-bubble-sort

---

## Author, Credits & Thanks

- Author: **Puhan Xu**  
- Course: **CISC-121-002**
