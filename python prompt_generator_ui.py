import json
import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
from tkinter.filedialog import asksaveasfilename

"""
Module for generating customized prompts with a GUI.
Provides functionality for customizing elements, generating prompts,
and saving them to a file.
"""

# Define default options
default_options = {
    "artists": ["Artist1", "Artist2", "Artist3"],
    "styles": ["Style1", "Style2", "Style3"],
    "actions": ["Action1", "Action2", "Action3"],
    "features": ["Feature1", "Feature2", "Feature3"],
    "camera_angles": ["Angle1", "Angle2", "Angle3"],
    "camera_distances": ["Distance1", "Distance2", "Distance3"],
    "lighting_options": ["Lighting1", "Lighting2", "Lighting3"],
    "emotions": ["Emotion1", "Emotion2", "Emotion3"],
    "color_accents": ["Accent1", "Accent2", "Accent3"],
    "prompt_craft_elements": ["Element1", "Element2", "Element3"]
}

# Placeholder function to set camera and lighting
def set_camera_and_lighting(camera_angles, camera_distances, lighting_options):
    """Set camera angle, distance, and lighting options."""
    return camera_angles[0], camera_distances[0], lighting_options[0]

# Function to save custom options
def save_custom_options(filename, options):
    """Save custom options to a JSON file."""
    with open(filename, 'w', encoding='utf-8') as options_file:
        json.dump(options, options_file, ensure_ascii=False, indent=4)

# Load custom options if available
try:
    with open('custom_options.json', 'r', encoding='utf-8') as file:
        custom_options = json.load(file)
except FileNotFoundError:
    custom_options = default_options

# Function to generate prompts (placeholder)
def generate_vivid_prompt(
    subject, actions, features, camera_angle, camera_distance, lighting,
    style, negative_prompts, emotions, context, color_accents,
    prompt_craft_elements, artists, keyword_weights, length
):
    """Generate a vivid prompt based on the given elements."""
    return (
        f"Prompt with {subject}, {actions}, {features}, {camera_angle}, "
        f"{camera_distance}, {lighting}, {style}, {negative_prompts}, {emotions}, "
        f"{context}, {color_accents}, {prompt_craft_elements}, {artists}, "
        f"{keyword_weights}, {length}"
    )

# Function to refine prompts using spaCy (placeholder)
def refine_prompt_with_spacy(prompt):
    """Refine the given prompt using spaCy."""
    return prompt + " (refined)"

# Function to parse input prompt
def parse_input_prompt(subject):
    """Parse the input prompt and return elements for prompt generation."""
    return {
        "actions": default_options['actions'],
        "features": default_options['features'],
        "camera_angles": default_options['camera_angles'],
        "camera_distances": default_options['camera_distances'],
        "lighting_options": default_options['lighting_options'],
        "styles": default_options['styles'],
        "negative_prompts": [],
        "emotions": default_options['emotions'],
        "context": [],
        "color_accents": default_options['color_accents'],
        "prompt_craft_elements": default_options['prompt_craft_elements'],
        "artists": default_options['artists']
    }

# Function to generate custom prompts based on user input
def generate_custom_prompts(subject, num_variations, weights, length, refine):
    """Generate custom prompts based on user input and selected options."""
    prompts = []
    for _ in range(num_variations):
        elements = parse_input_prompt(subject)
        elements["keyword_weights"] = weights
        prompt = generate_vivid_prompt(
            subject, elements["actions"], elements["features"], *set_camera_and_lighting(
                elements["camera_angles"], elements["camera_distances"], elements["lighting_options"]
            ), elements["styles"][0], elements["negative_prompts"], elements["emotions"],
            elements["context"], elements["color_accents"], elements["prompt_craft_elements"],
            elements["artists"], elements["keyword_weights"], length
        )
        if refine:
            prompt = refine_prompt_with_spacy(prompt)
        prompts.append(prompt)
    return prompts

# Function to save prompts to a file
def save_prompts_to_file(prompts):
    """Save the generated prompts to a file."""
    file_path = asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
    if file_path:
        with open(file_path, 'w', encoding='utf-8') as prompts_file:
            for prompt in prompts:
                prompts_file.write(prompt + "\n\n")
        messagebox.showinfo("Success", f"Prompts saved to {file_path}")

# Function to open a customization window
def customize_options():
    """Open a window to customize the prompt generation options."""
    def save_customizations():
        custom_options["artists"] = entry_artists.get().split(", ")
        custom_options["styles"] = entry_styles.get().split(", ")
        custom_options["actions"] = entry_actions.get().split(", ")
        custom_options["features"] = entry_features.get().split(", ")
        custom_options["camera_angles"] = entry_camera_angles.get().split(", ")
        custom_options["camera_distances"] = entry_camera_distances.get().split(", ")
        custom_options["lighting_options"] = entry_lighting_options.get().split(", ")
        custom_options["emotions"] = entry_emotions.get().split(", ")
        custom_options["color_accents"] = entry_color_accents.get().split(", ")
        custom_options["prompt_craft_elements"] = entry_prompt_craft_elements.get().split(", ")
        save_custom_options('custom_options.json', custom_options)
        messagebox.showinfo("Success", "Custom options saved successfully")
        custom_window.destroy()

    custom_window = tk.Toplevel(root)
    custom_window.title("Customize Options")
    custom_window.geometry("600x400")

    # Create input fields for each customizable option
    def create_customization_field(row, label_text, options_key):
        ttk.Label(custom_window, text=label_text).grid(row=row, column=0, padx=10, pady=5, sticky=tk.W)
        entry = ttk.Entry(custom_window, width=50)
        entry.insert(0, ", ".join(custom_options[options_key]))
        entry.grid(row=row, column=1, padx=10, pady=5, sticky=tk.W)
        return entry

    entry_artists = create_customization_field(0, "Artists:", "artists")
    entry_styles = create_customization_field(1, "Styles:", "styles")
    entry_actions = create_customization_field(2, "Actions:", "actions")
    entry_features = create_customization_field(3, "Features:", "features")
    entry_camera_angles = create_customization_field(4, "Camera Angles:", "camera_angles")
    entry_camera_distances = create_customization_field(5, "Camera Distances:", "camera_distances")
    entry_lighting_options = create_customization_field(6, "Lighting Options:", "lighting_options")
    entry_emotions = create_customization_field(7, "Emotions:", "emotions")
    entry_color_accents = create_customization_field(8, "Color Accents:", "color_accents")
    entry_prompt_craft_elements = create_customization_field(9, "Prompt Craft Elements:", "prompt_craft_elements")

    # Save button
    ttk.Button(custom_window, text="Save Customizations", command=save_customizations).grid(row=10, column=0, columnspan=2, pady=10)

# Function to create the user interface
def create_ui():
    """Create the main user interface for the prompt generator."""
    def on_generate():
        subject = entry_subject.get()
        num_variations = int(entry_num_variations.get())
        length = var_length.get()
        weights = {
            "masterpiece": scale_masterpiece.get(),
            "best quality": scale_quality.get(),
            "ultra-detailed": scale_detailed.get(),
            "intricate": scale_intricate.get()
        }
        refine = var_refine.get()
        prompts = generate_custom_prompts(subject, num_variations, weights, length, refine)
        text_output.delete(1.0, tk.END)
        for prompt in prompts:
            text_output.insert(tk.END, prompt + "\n\n")

    global root
    root = tk.Tk()
    root.title("Prompt Generator")
    root.geometry("800x600")

    style = ttk.Style()
    style.configure("TLabel", font=("Arial", 12))
    style.configure("TButton", font=("Arial", 12))
    style.configure("TEntry", font=("Arial", 12))
    style.configure("TScale", font=("Arial", 12))
    style.configure("TCheckbutton", font=("Arial", 12))

    ttk.Label(root, text="Subject:").grid(row=0, column=0, padx=10, pady=10, sticky=tk.W)
    entry_subject = ttk.Entry(root, width=50)
    entry_subject.grid(row=0, column=1, padx=10, pady=10, sticky=tk.W)

    ttk.Label(root, text="Number of Variations:").grid(row=1, column=0, padx=10, pady=10, sticky=tk.W)
    entry_num_variations = ttk.Entry(root, width=10)
    entry_num_variations.grid(row=1, column=1, padx=10, pady=10, sticky=tk.W)

    ttk.Label(root, text="Prompt Length:").grid(row=2, column=0, padx=10, pady=10, sticky=tk.W)
    var_length = tk.StringVar(value="short")
    ttk.Radiobutton(root, text="Short", variable=var_length, value="short").grid(row=2, column=1, padx=10, pady=10, sticky=tk.W)
    ttk.Radiobutton(root, text="Medium", variable=var_length, value="medium").grid(row=2, column=2, padx=10, pady=10, sticky=tk.W)
    ttk.Radiobutton(root, text="Long", variable=var_length, value="long").grid(row=2, column=3, padx=10, pady=10, sticky=tk.W)

    ttk.Label(root, text="Keyword Weights:").grid(row=3, column=0, padx=10, pady=10, sticky=tk.W)
    ttk.Label(root, text="Masterpiece:").grid(row=4, column=0, padx=10, pady=10, sticky=tk.W)
    scale_masterpiece = ttk.Scale(root, from_=0, to=10, orient=tk.HORIZONTAL)
    scale_masterpiece.grid(row=4, column=1, padx=10, pady=10, sticky=tk.W)

    ttk.Label(root, text="Best Quality:").grid(row=5, column=0, padx=10, pady=10, sticky=tk.W)
    scale_quality = ttk.Scale(root, from_=0, to=10, orient=tk.HORIZONTAL)
    scale_quality.grid(row=5, column=1, padx=10, pady=10, sticky=tk.W)

    ttk.Label(root, text="Ultra-Detailed:").grid(row=6, column=0, padx=10, pady=10, sticky=tk.W)
    scale_detailed = ttk.Scale(root, from_=0, to=10, orient=tk.HORIZONTAL)
    scale_detailed.grid(row=6, column=1, padx=10, pady=10, sticky=tk.W)

    ttk.Label(root, text="Intricate:").grid(row=7, column=0, padx=10, pady=10, sticky=tk.W)
    scale_intricate = ttk.Scale(root, from_=0, to=10, orient=tk.HORIZONTAL)
    scale_intricate.grid(row=7, column=1, padx=10, pady=10, sticky=tk.W)

    var_refine = tk.BooleanVar(value=False)
    ttk.Checkbutton(root, text="Refine Prompts with spaCy", variable=var_refine).grid(row=8, column=0, columnspan=2, pady=10)

    ttk.Button(root, text="Generate Prompts", command=on_generate).grid(row=9, column=0, columnspan=2, pady=10)

    text_output = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=70, height=10, font=("Arial", 12))
    text_output.grid(row=10, column=0, columnspan=2, padx=10, pady=10)

    ttk.Button(root, text="Save Prompts", command=lambda: save_prompts_to_file(text_output.get(1.0, tk.END).split("\n\n"))).grid(row=11, column=0, columnspan=2, pady=10)

    ttk.Button(root, text="Customize Options", command=customize_options).grid(row=12, column=0, columnspan=2, pady=10)

    root.mainloop()

# Run the UI
if __name__ == "__main__":
    create_ui()
