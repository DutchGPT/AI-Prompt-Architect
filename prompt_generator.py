import argparse
import random
from typing import List, Dict, Tuple, Optional
import tkinter as tk
from tkinter import scrolledtext

def set_keyword_weights(custom_weights: Optional[Dict[str, float]] = None) -> Dict[str, float]:
    """Set default and custom keyword weights for prompt generation."""
    default_weights = {
        "masterpiece": 1.5,
        "best quality": 1.5,
        "ultra-detailed": 1.2,
        "intricate": 1.2,
        "sharp focus": 1.2,
        "vibrant colors": 1.1,
        "dynamic pose": 1.1,
        "realistic": 1.0,
        "isolated": 1.2,
        "mind-blowing": 1.5,
        "unique": 1.5,
        "apex": 1.5
    }
    if custom_weights:
        default_weights.update(custom_weights)
    return default_weights

def validate_prompt(prompt: str, negative_prompts: List[str]) -> bool:
    """Ensure the generated prompt does not contain undesirable elements."""
    return all(negative not in prompt for negative in negative_prompts)

def add_context_to_prompt(prompt: str, context: List[str]) -> str:
    """Add specific context to the prompt."""
    if context:
        context_phrase = ', '.join(context)
        return f"{prompt}, context: {context_phrase}"
    return prompt

def get_random_artists(artists: List[str], num_artists: int = 2) -> List[str]:
    """Select random artists for inspiration."""
    return random.sample(artists, num_artists)

def set_camera_and_lighting(
    camera_angles: List[str],
    camera_distances: List[str],
    lighting_options: List[str]
) -> Tuple[str, str, str]:
    """Randomly select camera angles, distances, and lighting conditions."""
    return (random.choice(camera_angles), random.choice(camera_distances), random.choice(lighting_options))

def generate_vivid_prompt(
    subject: str, actions: List[str], features: List[str], camera_angle: str, camera_distance: str,
    lighting: str, style: str, negative_prompts: List[str], emotions: List[str], context: List[str],
    color_accents: List[str], prompt_craft_elements: List[str], artists: List[str], 
    keyword_weights: Dict[str, float], prompt_length: str
) -> str:
    """Generate a single vivid prompt with detailed descriptions."""
    action_phrase = ', '.join(random.sample(actions, k=min(len(actions), 2)))
    negative_phrase = ', '.join(negative_prompts)
    features_phrase = ', '.join(random.sample(features, k=min(len(features), 2)))
    emotions_phrase = ', '.join(random.sample(emotions, k=min(len(emotions), 2)))
    artist_phrase = ', '.join(random.sample(artists, k=2))
    style_phrase = f"style: {style}" if style else ""

    keyword_string = ", ".join([f"{k}:{v}" for k, v in keyword_weights.items()])

    composition_options = ["rule of thirds", "dynamic balance", "negative space", "centralized", "symmetrical"]
    chosen_composition = random.choice(composition_options)

    background_options = ["forest", "ocean", "mountain", "cityscape"]
    chosen_background = random.choice(background_options)
    background_details = random.sample(["mist", "sunset", "clouds"], k=random.randint(1, 2))
    background_phrase = f"{chosen_background} with {', '.join(background_details)}"

    color_accent = random.choice(color_accents) if color_accents else ""
    chosen_prompt_craft = random.choice(prompt_craft_elements)

    template_options = [
        f"{keyword_string}, {chosen_composition}, a {subject} with {features_phrase}, {action_phrase}, "
        f"{camera_distance} {camera_angle} view, {lighting}, {emotions_phrase}, {background_phrase}, "
        f"{color_accent}, {chosen_prompt_craft}, inspired by {artist_phrase}, {style_phrase}. Avoid {negative_phrase}.",
        f"A {subject} with {features_phrase} in {chosen_composition} composition, performing {action_phrase}. "
        f"Captured in {camera_distance} {camera_angle} view with {lighting}, evoking {emotions_phrase}. "
        f"Background: {background_phrase}. Color accent: {color_accent}, technique: {chosen_prompt_craft}. "
        f"Inspired by {artist_phrase}, {style_phrase}. Avoid {negative_phrase}.",
    ]
    prompt = random.choice(template_options)

    if prompt_length == "short":
        prompt = " ".join(prompt.split()[:25])  # Truncate to first 25 words
    elif prompt_length == "medium":
        prompt = " ".join(prompt.split()[:50])  # Truncate to first 50 words
    elif prompt_length == "long":
        pass  # Keep the full prompt

    return add_context_to_prompt(prompt, context)

def parse_input_prompt(input_prompt: str) -> Dict[str, List[str]]:
    """Parse the input prompt to extract relevant details."""
    return {
        "subject": [input_prompt],
        "actions": ["running", "jumping", "flying", "gliding"],
        "features": ["sharp claws", "glowing eyes", "sleek feathers", "smooth skin"],
        "camera_angles": ["low-angle", "high-angle", "eye-level"],
        "camera_distances": ["close-up", "medium shot", "long shot"],
        "lighting_options": ["sunset lighting", "golden hour", "moonlit"],
        "styles": ["photorealistic", "digital painting", "watercolor"],
        "negative_prompts": ["blurry", "out of focus", "low resolution"],
        "emotions": ["majestic", "fierce", "playful", "serene"],
        "color_accents": ["red highlights", "blue tones", "golden hues"],
        "prompt_craft_elements": ["bokeh effect", "HDR", "volumetric lighting"],
        "artists": ["Greg Rutkowski", "Alphonse Mucha", "Salvador Dalí", "Hayao Miyazaki"],
        "context": []
    }

def generate_custom_prompts(
    input_prompt: str, num_variations: int = 5, 
    custom_weights: Optional[Dict[str, float]] = None, prompt_length: str = "medium"
) -> List[str]:
    """Generate multiple variations of the prompt based on user input."""
    parsed_details = parse_input_prompt(input_prompt)
    keyword_weights = set_keyword_weights(custom_weights)

    prompts = []
    for _ in range(num_variations):
        actions_sample = random.sample(parsed_details['actions'], 2)
        features_sample = random.sample(parsed_details['features'], 2)
        camera_angle, camera_distance, lighting = set_camera_and_lighting(
            parsed_details['camera_angles'], parsed_details['camera_distances'], parsed_details['lighting_options'])
        style = random.choice(parsed_details['styles'])
        negative_prompts_sample = random.sample(parsed_details['negative_prompts'], 2)
        emotions_sample = random.sample(parsed_details['emotions'], 2)
        artists_sample = get_random_artists(parsed_details['artists'], 2)
        context = parsed_details['context']
        color_accents = parsed_details['color_accents']
        prompt_craft_elements = parsed_details['prompt_craft_elements']

        prompt = generate_vivid_prompt(
            parsed_details['subject'][0], actions_sample, features_sample, camera_angle, camera_distance, lighting, 
            style, negative_prompts_sample, emotions_sample, context, color_accents, prompt_craft_elements, 
            artists_sample, keyword_weights, prompt_length
        )
        
        if validate_prompt(prompt, negative_prompts_sample):
            prompts.append(prompt)

    return prompts

def create_ui():
    """Create a simple tkinter UI for generating prompts."""
    def on_generate():
        subject = entry_subject.get()
        num_variations = int(entry_num_variations.get())
        length = var_length.get()
        weights_input = entry_weights.get()

        custom_weights = {}
        if weights_input:
            weight_pairs = weights_input.split(",")
            for pair in weight_pairs:
                keyword, weight = pair.split(":")
                custom_weights[keyword] = float(weight)
        
        prompts = generate_custom_prompts(subject, num_variations=num_variations, custom_weights=custom_weights, prompt_length=length)
        txt_output.delete(1.0, tk.END)
        for i, prompt in enumerate(prompts, 1):
            txt_output.insert(tk.END, f"Prompt {i}: {prompt}\n\n")

    root = tk.Tk()
    root.title("Prompt Generator")

    tk.Label(root, text="Main Subject:").grid(row=0, column=0, sticky=tk.W)
    entry_subject = tk.Entry(root, width=50)
    entry_subject.grid(row=0, column=1, padx=10, pady=5)

    tk.Label(root, text="Number of Variations:").grid(row=1, column=0, sticky=tk.W)
    entry_num_variations = tk.Entry(root, width=10)
    entry_num_variations.grid(row=1, column=1, padx=10, pady=5, sticky=tk.W)
    entry_num_variations.insert(0, "5")

    tk.Label(root, text="Prompt Length:").grid(row=2, column=0, sticky=tk.W)
    var_length = tk.StringVar(value="medium")
    tk.Radiobutton(root, text="Short", variable=var_length, value="short").grid(row=2, column=1, sticky=tk.W)
    tk.Radiobutton(root, text="Medium", variable=var_length, value="medium").grid(row=2, column=1)
    tk.Radiobutton(root, text="Long", variable=var_length, value="long").grid(row=2, column=1, sticky=tk.E)

    tk.Label(root, text="Custom Weights:").grid(row=3, column=0, sticky=tk.W)
    entry_weights = tk.Entry(root, width=50)
    entry_weights.grid(row=3, column=1, padx=10, pady=5)

    btn_generate = tk.Button(root, text="Generate Prompts", command=on_generate)
    btn_generate.grid(row=4, columnspan=2, pady=10)

    txt_output = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=70, height=20)
    txt_output.grid(row=5, columnspan=2, padx=10, pady=10)

    root.mainloop()

if __name__ == "__main__":
    create_ui()
