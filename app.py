import random
import gradio as gr
from typing import List, Tuple


# Convert the input string into a list of integers.
# Example: "1, 3, 5" -> [1, 3, 5]
def parse_list(s: str) -> List[int]:
    parts = s.split(",")
    result = []
    for p in parts:
        p = p.strip()
        if not p:
            continue
        result.append(int(p))   # this may raise ValueError, handled later
    return result


# Perform bubble sort and store every comparison and swap.
# Each step is saved as: (pass number, i, j, array snapshot, swapped?)
def bubble_sort_steps(arr: List[int]) -> List[Tuple[int, int, int, List[int], bool]]:
    a = arr[:]  # make a copy so the original list is unchanged
    n = len(a)
    steps = []

    if n <= 1:
        return steps

    # outer loop = number of bubble sort passes
    for p in range(n - 1):
        swapped_this_pass = False

        # compare each pair of neighbors
        for i in range(n - 1 - p):
            j = i + 1
            swapped = False

            # swap if they are in the wrong order
            if a[i] > a[j]:
                a[i], a[j] = a[j], a[i]
                swapped = True
                swapped_this_pass = True

            # save the state of the list after this comparison
            steps.append((p, i, j, a[:], swapped))

        # if there were no swaps in the whole pass, the list is already sorted
        if not swapped_this_pass:
            break

    return steps


# Convert the recorded steps into a Markdown table for Gradio to display
def format_steps_markdown(original: List[int], steps: List[tuple]) -> str:
    lines = []
    lines.append("# Bubble Sort Steps")
    lines.append("")
    lines.append(f"- Original array: `{original}`")

    if not original:
        lines.append("Array is empty – nothing to sort.")
        return "\n".join(lines)

    if not steps:
        lines.append("Array length ≤ 1 – already sorted.")
        lines.append(f"Sorted result: `{original}`")
        return "\n".join(lines)

    final_array = steps[-1][3]
    lines.append(f"- Sorted array: `{final_array}`")
    lines.append("")
    lines.append("Each row shows one comparison in bubble sort.")
    lines.append("If the swap column says yes, a swap happened in that step.")
    lines.append("")

    lines.append("| Step | Pass | i | j | Array after step | Swapped? |")
    lines.append("|------|------|---|---|------------------|----------|")

    for step_index, (p, i, j, snapshot, swapped) in enumerate(steps):
        swap_str = "✅ yes" if swapped else "❌ no"
        lines.append(
            f"| {step_index} | {p} | {i} | {j} | `{snapshot}` | {swap_str} |"
        )

    return "\n".join(lines)


# Handle the user input and return the markdown result
def run_bubble_sort(list_str: str) -> str:
    if not list_str.strip():
        return "Please enter at least one integer."

    try:
        arr = parse_list(list_str)
    except ValueError:
        return "Input contains a non-integer. Example: `5, 3, 10`."

    steps = bubble_sort_steps(arr)
    return format_steps_markdown(arr, steps)


# Generate a random list string, e.g. "7, 2, 9, 1, 3"
def random_list() -> str:
    length = random.randint(5, 8)        # how many numbers
    nums = [random.randint(0, 9) for _ in range(length)]
    return ", ".join(str(x) for x in nums)


# Gradio UI
with gr.Blocks() as demo:
    gr.Markdown("# CISC-121 Bubble Sort Visualizer")
    gr.Markdown(
        "Enter a list of numbers and this app will show each step of bubble sort."
    )

    list_input = gr.Textbox(
        label="Numbers (comma separated)",
        value="1, 2, 3, 4, 5"
    )

    with gr.Row():
        random_button = gr.Button("🎲 Random list")
        run_button = gr.Button("Run Bubble Sort")

    output = gr.Markdown(label="Steps")

    # Random list fills the textbox
    random_button.click(
        fn=random_list,
        inputs=None,
        outputs=list_input
    )

    # Run Bubble Sort uses the current textbox value
    run_button.click(
        fn=run_bubble_sort,
        inputs=list_input,
        outputs=output
    )

if __name__ == "__main__":
    demo.launch()
