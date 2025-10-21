# nonRecognition — Adversarial Fuzzer
[![Python Version](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Real fabrics that fight facial recognition. Join the first scientific effort to build reproducible, testable adversarial textiles and open-source software that gives privacy back to people.

<p align="center">
  <img src="./images/nonrecognition_banner.png" alt="Adversarial Fabrics on Kickstarter" style="max-width:100%;height:auto;border-radius:8px;">
</p>

# Real fabrics that fight facial recognition

Join the first scientific effort to build reproducible, testable adversarial textiles and open source software that gives privacy back to people.
<p align="center">
  <a href="https://www.kickstarter.com/projects/hevnsnt/1029985405" target="_blank">
    <img src="./images/kickstarter-logo-green.png" alt="Back us on Kickstarter" width="300">
  </a>
</p>

<p align="center">
  <b><a href="https://www.kickstarter.com/projects/hevnsnt/1029985405">Back us on Kickstarter</a></b><br>
  <i>Limited early rewards and prototype swatches available</i>
</p>


## The Mission

I am a hacker. I see computers and technology differently. For years I have explored how machines perceive us, diving into computer vision. This fast growing field decides who is seen, who is tracked, and who is recognized, with serious and often unsettling consequences for privacy.

I believe physical fabrics can be engineered to confuse facial recognition systems. I built a reproducible, science driven process to design those fabrics, and I test them rigorously across multiple models and real world conditions so the results are practical and repeatable. My goal is simple: to build a wardrobe that protects my privacy — and yours.

### Wait, Hasn't This Been Done Before?

Recently, an interesting concept of hope emerged from the artistic: so-called "adversarial patterns." These brilliant prints and garments held the promise of disrupting machine vision, causing detectors to miss a person entirely. They were fascinating, hopeful, and truly captivating. You might have seen some incredible projects in this space, such as [capable.design](https://capable.design/), [adversarialfashion.com](https://adversarialfashion.com/), and of course Adam Harvey’s work at [adam.harvey.studio](https://adam.harvey.studio/).

These initiatives are truly groundbreaking and deserve immense credit. They pushed the boundaries of what was thought possible, inspiring many (including us!) to think differently about privacy in the age of machine vision. But, as with many pioneering prototypes, they were often fragile, effective only against the weakest detectors and under perfect studio conditions.

It’s important to clarify, however, that much of the existing adversarial clothing primarily targets older "person detection" systems, such as the venerable **HAAR Cascade** models. While effective against those specific, simpler algorithms, these older systems are now easily bypassed by the far more sophisticated, modern facial recognition systems prevalent today. We are absolutely not talking down on these pioneering efforts; they had their place, and they served as crucial stepping stones. In fact, they were a tremendous starting point for our own project. We are, quite literally, standing on their shoulders; they are giants who paved the way.

Our project builds on this foundational work, incorporating similar adversarial techniques alongside principles from projects like CV Dazzle and Hyperface. Our goal is to leverage these insights to specifically fool the most advanced Facial Recognition systems currently in use.

### I Believe We Can Do Better.

I’m [Bill Swearingen](https://about.me/billswearingen). Having spent decades in security uncovering how complex systems fail, I’ve learned how to think differently and exploit technology’s true weak points. I’m the founder of [**SecKC**](https://seckc.org), the world’s largest monthly hacker meetup, and have spoken at major security conferences including [**BlackHat**](https://blackhat.com), [**Shmoocon**](https://en.wikipedia.org/wiki/ShmooCon) and [**DEF CON**](https://defcon.org). That experience drives my latest project, **nonRecognition** — an effort to transform intriguing privacy concepts into robust, repeatable, and verifiable solutions. This isn’t a stunt; it’s a focused, year-long research program asking a hard question: *Can physical fabrics truly defeat state-of-the-art facial recognition in real-world conditions?* Our mission is to uncover the how and the why, and to equip citizens, designers, and researchers with the open tools needed to understand and navigate these critical privacy frontiers.

To answer this, we're building two critical components:

1.  **A Custom Fuzzer and Testing Suite:** This repository. Powerful, open-source software designed to generate, test, and analyze thousands of adversarial designs against numerous recognition systems. This allows us to quantify results, iterate scientifically, and discover truly effective patterns.
2.  **Develop Adversarial Textiles:** Physically printed materials, produced and tested at scale, specifically optimized to confound the most advanced facial recognition models, not just rudimentary detectors.

To illustrate this process, here's a glimpse into our fuzzer at work. Each image below represents a unique adversarial pattern generated and then applied to a facial region, ready for testing against advanced recognition models. These are just a few of the thousands our system evaluates to find those elusive "failure patterns."
<h2 align="center">Fuzzer in Action</h2>
<p align="center">
  <img src="./images/fuzzer-working.png" alt="Fuzzer Working" width="600">
</p>

The fuzzer automatically tests facial recognition resilience by taking baseline images, generating and overlaying diverse adversarial patterns, then running them through multiple detection and recognition models to identify failures or anomalies. These results feed into evolutionary mutation routines for future epochs, refining how patterns evolve to reveal weaknesses in recognition systems. Here is a small sample of the generated adversarial images produced during testing. Each pattern was evolved and evaluated across multiple facial recognition models to measure detection failures and guide future mutation strategies. (Note: this represents only a fraction of the full input model set.)

<table align="center" style="border-collapse:collapse; border-spacing:0; padding:0; margin:0;">
  <tr>
    <td style="padding:0; margin:0;"><a href="./images/pattern_samples/45_shirt_gaiter_feature_collage_seed8374138_sample180500.jpg"><img src="./images/pattern_samples/45_shirt_gaiter_feature_collage_seed8374138_sample180500.jpg" width="200" style="display:block; margin:0; padding:0;"></a></td>
    <td style="padding:0; margin:0;"><a href="./images/pattern_samples/Man_Wearing_Gaiter_3d_wireframe+op_art_chevrons+repeating_texture_object_seed2984227_sample297500.jpg"><img src="./images/pattern_samples/Man_Wearing_Gaiter_3d_wireframe+op_art_chevrons+repeating_texture_object_seed2984227_sample297500.jpg" width="200" style="display:block; margin:0; padding:0;"></a></td>
    <td style="padding:0; margin:0;"><a href="./images/pattern_samples/facemask_1_qr_code+hyperface_like_seed948622_sample197000.jpg"><img src="./images/pattern_samples/facemask_1_qr_code+hyperface_like_seed948622_sample197000.jpg" width="200" style="display:block; margin:0; padding:0;"></a></td>
  </tr>
  <tr>
    <td style="padding:0; margin:0;"><a href="./images/pattern_samples/Woman_Wearing_Hoodie_feature_collage+3d_wireframe+vortex_seed8663387_sample303500.jpg"><img src="./images/pattern_samples/Woman_Wearing_Hoodie_feature_collage+3d_wireframe+vortex_seed8663387_sample303500.jpg" width="200" style="display:block; margin:0; padding:0;"></a></td>
    <td style="padding:0; margin:0;"><a href="./images/pattern_samples/full_body_dress_6_feature_collage_seed1358874_sample290000.jpg"><img src="./images/pattern_samples/full_body_dress_6_feature_collage_seed1358874_sample290000.jpg" width="200" style="display:block; margin:0; padding:0;"></a></td>
    <td style="padding:0; margin:0;"><a href="./images/pattern_samples/Woman_Wearing_Scarf_3d_wireframe+simple_shapes_seed4381582_sample280000.jpg"><img src="./images/pattern_samples/Woman_Wearing_Scarf_3d_wireframe+simple_shapes_seed4381582_sample280000.jpg" width="200" style="display:block; margin:0; padding:0;"></a></td>
  </tr>
  <tr>
    <td style="padding:0; margin:0;"><a href="./images/pattern_samples/full_body_shawl_6_perlin_noise+repeating_texture_object+3d_wireframe_seed3559762_sample370500.jpg"><img src="./images/pattern_samples/full_body_shawl_6_perlin_noise+repeating_texture_object+3d_wireframe_seed3559762_sample370500.jpg" width="200" style="display:block; margin:0; padding:0;"></a></td>
    <td style="padding:0; margin:0;"><a href="./images/pattern_samples/Woman_Wearing_Shawl_dazzle_camouflage+pop_art_collage+blackout_patches_seed9165740_sample173500.jpg"><img src="./images/pattern_samples/Woman_Wearing_Shawl_dazzle_camouflage+pop_art_collage+blackout_patches_seed9165740_sample173500.jpg" width="200" style="display:block; margin:0; padding:0;"></a></td>
    <td style="padding:0; margin:0;"><a href="./images/pattern_samples/Man_Hat_Hide_Face_hyperface_like+landmark_noise+checkerboard_seed9167792_sample240500.jpg"><img src="./images/pattern_samples/Man_Hat_Hide_Face_hyperface_like+landmark_noise+checkerboard_seed9167792_sample240500.jpg" width="200" style="display:block; margin:0; padding:0;"></a></td>
  </tr>
</table>

---

## What Makes This Fuzzer Different?

This isn't just a random pattern generator. It's a purpose-built research tool designed to find *robust* vulnerabilities in *modern* AI models.

* **Targets an Ensemble of Modern Models:** This fuzzer doesn't just target one model. It validates every pattern against an *ensemble* of state-of-the-art systems simultaneously:
    * **InsightFace (`buffalo_l`):** A large, high-accuracy face detector.
    * **InsightFace (`buffalo_s`):** A smaller, faster face detector.
    * **YOLOv8n:** A modern, real-time object detector (used for person detection).
    An anomaly is only registered if it fools the models in a significant way (e.g., fooling *both* face models, or causing a *dramatic* drop in confidence).

* **Genetic Algorithm for "Evolved" Patterns:** The fuzzer learns. When it finds a pattern that causes a failure (an "anomaly"), it saves that pattern's "recipe" to a `PRIORITY_TESTS` list. In the next epoch, it uses these successful recipes as parents for a **genetic algorithm**:
    * **Mutation:** It randomly adds, removes, or swaps pattern layers.
    * **Crossover:** It splices two successful parent recipes together to create a new child.
    This allows the fuzzer to "evolve" increasingly complex and effective patterns over time.

* **Surgical & Saliency-Based Attacks:** The pattern library goes far beyond simple noise. It includes "surgical" attacks that target specific parts of the AI's "brain":
    * **Landmark Attacks:** Patterns that find the baseline facial landmarks (eyes, nose, mouth) and *only* apply noise to those specific points.
    * **Saliency Attacks:** Patterns that mimic features AI models are trained to find, like `saliency_eye_attack` (stamping dozens of eyes) or `recursive_face_tile` (tiling the user's own face) to confuse the model's bounding-box and non-maximum suppression (NMS) logic.

* **Built for Scale and Research:**
    * **Massively Parallel:** Uses Python's `multiprocessing` to run tests across all available CPU cores.
    * **Reproducible:** Saves the exact `recipe.json` and a high-resolution 300 DPI (`.png`) swatch for every successful anomaly, allowing for physical printing and real-world validation.
    * **Stateful:** Can be stopped (Ctrl+C) and resumed (`--resume`) at any time, preserving all learned priority tests.

---

## ⚙️ Core Features ⚙️

-   **Ensemble Model Testing:** Validates against **InsightFace `buffalo_l`**, **InsightFace `buffalo_s`**, and **YOLOv8n** simultaneously.
-   **Genetic Algorithm:** Evolves new test cases from previously successful patterns using mutation and crossover.
-   **Advanced Anomaly Detection:** Detects more than just "no face found."
    -   `FACE_ENSEMBLE`: The primary face was lost by *both* InsightFace models.
    -   `FACE_LOW_CONF`: The primary face was found, but its confidence score dropped below a critical threshold (a "near-miss").
    -   `PERSON`: The YOLOv8 model detected more or fewer people than the baseline.
-   **Massive Pattern Library:** Includes **30+ unique pattern generators** (see list below) designed to attack different parts of the vision pipeline, from low-level filters (noise, gradients) to high-level feature extractors (eyes, faces, text).
-   **Multi-Layering:** Combines up to 3 different pattern types with variable blending into a single complex test case.
-   **Reproducible Outputs:**
    -   Saves anomalous images to `./anomaly/`.
    -   Saves the exact `recipe.json` for each anomaly to `./anomaly_patterns/`.
    -   Optionally saves a **3600x3600px 300 DPI** print-ready `.png` swatch for physical fabric production (`--save-hires-patterns`).
-   **GPU/NPU Auto-Detection:** Automatically utilizes NVIDIA CUDA or Apple CoreML for InsightFace models if available, falling back gracefully to CPU.
-   **Stateful Fuzzing:** Saves progress to `fuzzer_state.pkl` on exit (Ctrl+C) and resumes with the `--resume` flag.
-   **Robust Caching:** Uses per-worker LRU caching for all image assets (`textures`, `tpdne_images`, `abstract_art`) to maximize speed.

---

## 🔬 How It Works 🔬

1.  **Baseline (Main Process):**
    * On start, the fuzzer runs all models in a consistent **CPU-only** environment to establish a "ground truth" for every image in `./input_images/`.
    * It stores the location, confidence, and landmarks for the primary face (for both face models) and the total person count (for YOLO).

2.  **Worker Pool (Parallel):**
    * A persistent `multiprocessing.Pool` is created (one worker per core by default).
    * Each worker process initializes its *own* instance of all three models (InsightFace-L, InsightFace-S, YOLOv8-ORT) and loads all art/texture assets into its own cache.

3.  **Test Generation (Main Process):**
    * The main process enters an infinite loop (an "epoch").
    * For each image, it generates `STOCHASTIC_TESTS_PER_BATCH` (e.g., 1000) new test "recipes."
    * A percentage of these are "evolved" from the `PRIORITY_TESTS` list (mutations/crossovers).
    * The rest are new random combinations of 1-3 pattern layers.

4.  **Execution (Worker Process):**
    * The list of test cases is distributed to the worker pool.
    * For each test case, a worker:
        1.  Loads the original image and mask from its cache.
        2.  Generates the multi-layer pattern based on the recipe (e.g., `perlin_noise` + `saliency_eye_attack`).
        3.  Applies the pattern to the masked area.
        4.  Runs all three models on the modified image.
        5.  Returns the results (face counts, locations, confidence) to the main process.

5.  **Result Processing (Main Process):**
    * The main process receives results as they are completed.
    * It compares the test result against the pre-calculated baseline.
    * **If Anomaly:** The main process saves the image, the pattern swatch, the high-res PNG (if enabled), and the `recipe.json`. It then adds this successful recipe to the `PRIORITY_TESTS` dictionary.
    * **If No Anomaly:** The result is discarded.

6.  **Loop:**
    * At the end of an epoch, the fuzzer starts a new one, now using the *updated* `PRIORITY_TESTS` list to generate even more effective "evolved" patterns.

---

## 🎨 The Adversarial Patterns 🎨

The fuzzer selects from a diverse library of over 30 pattern generators, including:

* **Geometric & Noise:**
    * `simple_shapes`
    * `fractal_noise`
    * `perlin_noise`
    * `hf_noise` (High-Freq Static)
    * `checkerboard`
    * `gradient`
    * `op_art_chevrons`
    * `tiled_logo`
* **Feature-Based & Saliency:**
    * `feature_collage` (stamps random facial features)
    * `saliency_eye_attack` (densely stamps *only* eyes)
    * `recursive_face_tile` (tiles the user's own face)
    * `ascii_face` (draws text-based faces)
    * `animal_print` (procedural leopard/jaguar spots)
    * `trypophobia` (clusters of small, high-contrast holes)
* **Surgical & Landmark-Based:**
    * `landmark_noise` (applies noise/blur *only* to key points)
    * `swapped_landmarks` (pastes the mouth over the eye, etc.)
* **Camouflage & Texture:**
    * `camouflage` (uses textures from the `./textures` dir)
    * `repeating_texture_object`
    * `warped_face` (uses a full face as a warped texture)
* **Structural & Dazzle:**
    * `hyperface_like` (high-contrast blocky pattern)
    * `dazzle_camouflage`
    * `interference_lines` (Moire-like patterns)
    * `3d_wireframe` (projects 3D cubes)
* **Glitch & Sensor Attacks:**
    * `vortex` (twisting distortion)
    * `photonegative_patch`
    * `colorspace_jitter` (noise in Cr/Cb channels only)
    * `selective_blur`
    * `ir_led_attack` (simulates IR glare/bloom)
    * `pixel_sort_glitch`
* **Other:**
    * `random_text`
    * `qr_code`
    * `pop_art_collage`
    * `blackout_patches`

---

## 🛠️ Setup and Installation 🛠️

This repository currently contains research artifacts and documentation related to the Adversarial Fabric Fuzzer project.
The core fuzzer code, model integrations, and data generation routines are not publicly released at this stage.

At this time, the fuzzer is used privately for controlled testing and scientific evaluation of adversarial patterns against multiple facial recognition frameworks. Future releases may include:
	•	Public datasets of anonymized fuzzing results and failure statistics
	•	Non-sensitive components of the testing pipeline for academic replication
	•	Reproducible metrics and visualization tools for analyzing detection anomalies

Until then, this repository will serve as a progress tracker for the project — including research updates, metrics summaries, and high-level implementation details.
If you’re interested in contributing to the open-source release or following the research, please watch this repository for updates or support the project on Kickstarter.